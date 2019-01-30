from Verilog_VCD import parse_vcd
from bs4 import BeautifulSoup
import logging

# wrap up Verilog_VCD with a method to fetch all data for a specific key
class VCDHelper(object):

    def __init__(self, vcd_file):
        self.vcd = parse_vcd(vcd_file)

    def fetch(self, name):
        for key in self.vcd.keys():
            if name in self.vcd[key]['nets'][0]['name']:
                data = (self.vcd[key]['tv'])
                return data

# handy conversion functions to convert the kind of values a VCD file has to something we might want in the SVG
def convertBinStrToInt():
    def convert(value):
        return str(int(value,2))
    return convert

def compareBitField(bit):
    def convert(value):
        logging.debug("compare %s with bit %d" % (value, bit))
        try:
            return int(value[-(bit+1)])
        except IndexError:
            return False
    return convert

# Animators work on a piece of SVG and update it depending on the VCD file
class Animator(object):

    def __init__(self, svg_id, vcd_id):
        self.svg_id = svg_id
        self.vcd_id = vcd_id

    def add_vcd_data(self, data):
        self.data = data

    def animate(self, soup, frame):
        try:
            self.update(soup, frame)
        except AttributeError:
            exit("animator for [%s] failed looking for tag [%s]" % (self.vcd_id, self.svg_id))

# Replace a piece of text in the SVG with something from the VCD
class TextReplacer(Animator):
    
    def __init__(self, svg_id, vcd_id, conversion):
        self.svg_id = svg_id
        self.vcd_id = vcd_id
        self.conversion = conversion

    def update(self, soup, frame):
        elem = soup.find("",{"id": self.svg_id}).find("tspan")
        elem.string = self.conversion(self.data[frame][1])

# Replace a style depending on a comparison in the VCD
class StyleReplacer(Animator):

    def __init__(self, svg_id, vcd_id, replace, compare):
        self.svg_id = svg_id
        self.vcd_id = vcd_id
        self.compare = compare
        self.replace = replace

    def update(self, soup, frame):
        if self.compare(self.data[frame][1]):
            elem = soup.find("", {"id": self.svg_id})
            elem['style'] = elem['style'].replace(*self.replace)

# AnimateSVG class takes an SVG file and a bunch of Animator objects
class AnimateSVG(object):
    
    def __init__(self, svg_file, vcd_file):
        self.animators = []
        self.svg_file = svg_file
        self.vcd = VCDHelper(vcd_file)
        self.max_frames = 1e6

    def addAnimators(self, animators):
        for a in animators:
            self.addAnimator(a)

    # add the animator to the list, and fetch its data
    def addAnimator(self, animator):
        vcd_data=self.vcd.fetch(animator.vcd_id)
        animator.add_vcd_data(vcd_data)

        if vcd_data is None:
            exit("no data for [%s] found in VCD. Make sure VCD file is not compressed and vcd_id is valid" % animator.vcd_id)

        if len(vcd_data) < self.max_frames:
            self.max_frames = len(vcd_data)
        self.animators.append(animator)

    # animate method is called with a number of frames to iterate over
    # everytime, call each animators update method with the parsed SVG file and the current frame number
    # writes the output to an SVG file
    def animate(self, frames):
        if frames > self.max_frames:
            exit("max frames is %d" % self.max_frames)

        for frame in range(frames):
            logging.info("frame %03d" % frame)
            with open(self.svg_file) as fh:
                soup = BeautifulSoup(fh, "lxml")
                
                for a in self.animators:
                    a.animate(soup, frame)

            with open("frames/frame_%03d.svg" % frame, 'w') as fh:
                fh.write(str(soup))

if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    from config import animators, frames, svg_file, vcd_file
    animate = AnimateSVG(svg_file, vcd_file)
    animate.addAnimators(animators)

    # do the animation
    animate.animate(frames)
