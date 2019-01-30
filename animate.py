from Verilog_VCD import parse_vcd
from bs4 import BeautifulSoup

vcd = parse_vcd('test.vcd')

def fetch_data(name):
    for key in vcd.keys():
        if name in vcd[key]['nets'][0]['name']:
            data = (vcd[key]['tv'])
            return data

#import  ipdb; ipdb.set_trace()
counter = fetch_data('counter')
segs = fetch_data('segs')

for frame in range(16):
    print("frame %03d" % frame)
    with open("7seg.svg") as fh:
        
        soup = BeautifulSoup(fh, "lxml")

        # counter
        elem = soup.find("",{"id": "count"}).find("tspan")
        elem.string = str(int(counter[frame][1],2))

        # 10 segment display
        for seg in range(10):
            try:
                print("seg %02d : %s" % (seg, segs[frame][1][-(seg+1)]))
                if int(segs[frame][1][-(seg+1)]): # -seg because index from right side (LSB)
                    elem = soup.find("", {"id": "seg%d" % seg})
                    elem['style'] = elem['style'].replace('fill:none', 'fill:red')
            except IndexError: # data in vcd is not 0 padded, so 5 would be 101. So trying to fetch 4th digit will result in index error
                pass

    with open("frames/frame_%03d.svg" % frame, 'w') as fh:
        fh.write(str(soup))
