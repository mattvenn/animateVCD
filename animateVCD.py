#!/usr/bin/env python
from Verilog_VCD import parse_vcd
from bs4 import BeautifulSoup
import re
import logging
import sys
import argparse

# wrap up Verilog_VCD with a method to fetch all data for a specific key
class VCDHelper(object):
    def __init__(self, vcd_file):
        self.vcd = parse_vcd(vcd_file)

    def fetch(self, name):
        for key in self.vcd.keys():
            vcd_name = self.vcd[key]["nets"][0]["name"]
            # regex so don't have to provide the register width
            m = re.search("^([^[]+)(\[\d+:\d+\])?$", vcd_name)
            if m is not None:
                if m.group(1) == name:
                    data = self.vcd[key]["tv"]
                    return data


# handy conversion functions to convert the kind of values
# a VCD file has to something we might want in the SVG


def convertBinStrToIntBase(fmt, padding=0):
    def convert(value):
        try:
            return fmt.format(int(value, 2), fill=padding)
        except ValueError:
            return "xx" if padding == 0 else "x" * padding

    return convert


def convertBinStrToBin(padding=0):
    return convertBinStrToIntBase("{0:0{fill}b}", padding)


def convertBinStrToOct(padding=0):
    return convertBinStrToIntBase("{0:0{fill}o}", padding)


def convertBinStrToInt(padding=0):
    return convertBinStrToIntBase("{0:0{fill}d}", padding)


def convertBinStrToHex(padding=0):
    return convertBinStrToIntBase("{0:0{fill}x}", padding)


def convertBinStrToUHex(padding=0):
    return convertBinStrToIntBase("{0:0{fill}X}", padding)


def convertBinStrToASCII():
    return convertBinStrToIntBase("{0:0{fill}c}")


def convertLookupTable(table):
    def convert(value):
        try:
            intvalue = int(value, 2)
        except (ValueError):
            try:
                return table[value]
            except (KeyError):
                return "xx"
        return table[intvalue]

    return convert


def isHigh():
    def compare(value):
        logging.debug("compare %s" % (value))
        try:
            if int(value):
                return True
        except ValueError:
            return False

    return compare


def isLow():
    def compare(value):
        logging.debug("compare %s" % (value))
        try:
            if int(value) == 0:
                return True
        except ValueError:
            return False

    return compare


def compareBitField(bit):
    def compare(value):
        logging.debug("compare %s with bit %d" % (value, bit))
        try:
            # -(bit+1) to index from the end of the string as bitfield is MSB->LSB
            return int(value[-(bit + 1)])
        except IndexError:
            return False

    return compare


# Animators work on a piece of SVG and update it depending on the VCD file
class Animator(object):
    def __init__(self, svg_id, vcd_id, offset=0):
        self.svg_id = svg_id
        self.vcd_id = vcd_id
        self.offset = offset

    def add_sync_vcd_data(self, sync_clock, rising, vcd, clocks):
        self.data = []
        vcd_index = 0

        self.data.append(vcd[vcd_index][1])  # append initial value (pre first clock)
        last = None
        for i, e in enumerate(sync_clock):
            if last != None:
                t, v = e
                if (len(vcd) - 1) > vcd_index and int(t) >= int(vcd[vcd_index + 1][0]):
                    vcd_index += 1
                if (rising, last[1], v) in ((True, "0", "1"), (False, "1", "0")):
                    self.data.append(vcd[vcd_index][1])
                    clocks -= 1
                    if clocks == 0:
                        break
            last = e

        logging.debug("filled data for %s: %s" % (self.vcd_id, self.data))

    def add_async_vcd_data(self, vcd, clocks):
        self.data = []
        vcd_index = 0
        last_vcd = vcd[vcd_index][1]  # vcd data is list of tuples: (clock, value)

        for clock in range(clocks):
            try:
                if vcd[vcd_index][0] == clock:
                    last_vcd = vcd[vcd_index][1]
                    vcd_index += 1
            except IndexError:
                pass
            self.data.append(last_vcd)
        logging.debug("filled data for %s: %s" % (self.vcd_id, self.data))

    def animate(self, soup, frame):
        try:
            elem = soup.find("", {"id": self.svg_id})
            if elem is None:
                exit("couldn't find tag [%s] in SVG" % self.svg_id)

            if self.vcd_id[0] == "#":  # special signal
                if self.vcd_id == "#cycle":
                    signal = bin(frame)[2:]
                else:
                    exit("invalid signal [%s] referenced" % self.vcd_id)
            else:
                idx = frame + self.offset
                idx = max(idx, 0)
                if idx > len(self.data) - 1:
                    logging.debug(
                        "warning: clipping the %s range, check the offsets"
                        % (self.vcd_id)
                    )
                idx = min(idx, len(self.data) - 1)
                signal = self.data[idx]

            self.update(soup, frame, elem, signal)
        except (AttributeError, TypeError):
            exit(
                "animator for [%s] failed looking for tag [%s]"
                % (self.vcd_id, self.svg_id)
            )


# Replace a piece of text in the SVG with something from the VCD
class TextReplacer(Animator):
    def __init__(self, svg_id, vcd_id, conversion, offset=0):
        super().__init__(svg_id, vcd_id, offset)
        self.conversion = conversion

    def update(self, soup, frame, elem, signal):
        text = elem.find("tspan")
        text.string = self.conversion(signal)


# Replace a style depending on a comparison in the VCD
class StyleReplacer(Animator):
    def __init__(self, svg_id, vcd_id, replace, compare, offset=0):
        super().__init__(svg_id, vcd_id, offset)
        self.compare = compare
        self.replace = replace

    def update(self, soup, frame, elem, signal):
        if self.compare(signal):
            elem["style"] = elem["style"].replace(*self.replace)


# Hide an element depending on a comparison in the VCD
class Hide(Animator):
    def __init__(self, svg_id, vcd_id, compare, offset=0):
        super().__init__(svg_id, vcd_id, offset)
        self.compare = compare

    def update(self, soup, frame, elem, signal):
        if self.compare(signal):
            elem["style"] += ";display:none"


# AnimateSVG class takes an SVG file and a bunch of Animator objects
class AnimateSVG(object):
    def __init__(self, svg_file, vcd_file, frames):
        self.animators = []
        self.svg_file = svg_file
        self.vcd = VCDHelper(vcd_file)
        self.frames = frames

        self.sync = False
        self.sync_clock = None
        self.rising_edge = True

    def asyncProc(self):
        max_frames = self.vcd.fetch("clk")[-1][
            0
        ]  # does this works with other VCD scheme apart from iverilog?
        if frames > max_frames:
            exit("max frames is %d" % max_frames)

    def addSyncClock(self, clockname, rising_edge):
        self.sync_clock = self.vcd.fetch(clockname)
        counts = {("0", "1"): 0, ("1", "0"): 0}

        # count both edges
        for i in range(len(self.sync_clock) - 1):
            counts[(self.sync_clock[i][1], self.sync_clock[i + 1][1])] += 1

        max_frames = counts[("0", "1") if rising_edge else ("1", "0")]
        if frames > max_frames:
            exit("max frames is %d" % max_frames)

        self.sync = True
        self.rising_edge = rising_edge

    def addAnimators(self, animators):
        for a in animators:
            self.addAnimator(a)

    # add the animator to the list, and fetch its data
    def addAnimator(self, animator):
        if animator.vcd_id[0] == "#":
            self.animators.append(animator)
            return

        vcd_data = self.vcd.fetch(animator.vcd_id)

        if vcd_data is None:
            exit(
                "no data for [%s] found in VCD. Make sure VCD file is not compressed and vcd_id is valid"
                % animator.vcd_id
            )

        if self.sync:
            animator.add_sync_vcd_data(
                self.sync_clock, self.rising_edge, vcd_data, self.frames
            )
        else:
            animator.add_async_vcd_data(vcd_data, self.frames)

        self.animators.append(animator)

    # animate method is called with a number of frames to iterate over
    # everytime, call each animators update method with the parsed SVG file
    # and the current frame number writes the output to an SVG file
    def animate(self):
        for frame in range(self.frames):
            logging.info("frame %03d" % frame)
            with open(self.svg_file) as fh:
                soup = BeautifulSoup(fh, "xml")

                for a in self.animators:
                    a.animate(soup, frame)

            with open("frames/frame_%03d.svg" % frame, "w") as fh:
                fh.write(str(soup))


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="animate a VCD file with an SVG")
    parser.add_argument(
        "--config",
        required=True,
        help="directory that contains the config.py configuration file",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        dest="verbose_count",
        action="count",
        default=1,
        help="increases log verbosity for each occurence.",
    )

    args = parser.parse_args()
    log_level = max(3 - args.verbose_count, 0) * 10
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # config in a separate python file as it can be quite programatic
    sys.path.append(args.config)
    try:
        import config

        # load config baseline
        animators, frames, svg_file, vcd_file = (
            config.animators,
            config.frames,
            config.svg_file,
            config.vcd_file,
        )
        logging.info("vcd: %s svg: %s frames: %d" % (vcd_file, svg_file, frames))
    except ImportError:
        exit("no config.py found in %s" % args.config)

    # optional values
    sync = config.sync if hasattr(config, "sync") else False
    sync_clock = config.sync_clock if hasattr(config, "sync_clock") else "clk"
    rising_edge = config.rising_edge if hasattr(config, "rising_edge") else True

    animate = AnimateSVG(svg_file, vcd_file, frames)
    if sync:
        animate.addSyncClock(sync_clock, rising_edge)
    else:
        animate.asyncProc()

    animate.addAnimators(animators)

    # do the animation
    animate.animate()
