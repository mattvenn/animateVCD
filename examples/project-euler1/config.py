from animateVCD import (
    TextReplacer,
    StyleReplacer,
    compareBitField,
    convertBinStrToInt,
    convertBinStrToBin,
    convertLookupTable,
)

animators = []

shifts = {0b00001: "5", 0b00010: "5", 0b00100: "5", 0b01000: "0", 0b10000: "0"}

animators += [
    TextReplacer(svg_id="cycles", vcd_id="#cycle", conversion=convertBinStrToInt()),
    TextReplacer(svg_id="five_or_zero", vcd_id="shift5", conversion=convertLookupTable(shifts), offset=-1),
    TextReplacer(svg_id="c3", vcd_id="c3", conversion=convertBinStrToInt()),
    TextReplacer(svg_id="c5", vcd_id="c5", conversion=convertBinStrToInt()),
    TextReplacer(svg_id="v5.prev", vcd_id="v5", conversion=convertBinStrToInt(), offset=-1),
    TextReplacer(svg_id="c5.prev", vcd_id="c5", conversion=convertBinStrToInt(), offset=-1),
    TextReplacer(svg_id="c3.prev", vcd_id="c3", conversion=convertBinStrToInt(), offset=-1),
    TextReplacer(svg_id="output", vcd_id="result", conversion=convertBinStrToInt()),
    TextReplacer(svg_id="output.prev", vcd_id="result", conversion=convertBinStrToInt(), offset=-1),
    TextReplacer(svg_id="c5_lt_1000", vcd_id="c5_lt_1000", conversion=convertBinStrToInt(), offset=-1),
    TextReplacer(svg_id="c3_lt_1000", vcd_id="c3_lt_1000", conversion=convertBinStrToInt(), offset=-1)
]

# 1 for each segment in the display
for bit in range(5):
    animators.append(
        StyleReplacer(svg_id="shift5.%d" % bit, vcd_id="shift5", replace=("fill:#abc738", "fill:#00ff00"),
            compare=compareBitField(bit), offset=-1,
        )
    )
    animators.append(
        StyleReplacer(svg_id="shift5n.%d" % bit, vcd_id="shift5", replace=("fill:#808080", "fill:#000000"),
            compare=compareBitField(bit), offset=-1,
        )
    )
    animators.append(
        StyleReplacer(svg_id="shift1.%d" % bit, vcd_id="shift5", replace=("fill:#abc738", "fill:#00ff00"),
            compare=compareBitField(bit), offset=-1,
        )
    )
    animators.append(
        StyleReplacer(svg_id="shift1n.%d" % bit, vcd_id="shift5", replace=("fill:#808080", "fill:#000000"),
            compare=compareBitField(bit), offset=-1,
        )
    )


for e in [
    "bracket_top",
    "bracket_bottom",
    "bracket_add",
    "bracket_mult",
    "v5.prev",
    "c5.prev",
    "c5_add",
    "c5_eq",
    "five_or_zero",
]:
    animators.append(
        StyleReplacer(svg_id=e, vcd_id="c5_lt_1000", replace=("opacity:0.25", "opacity:1"),
            compare=compareBitField(0), offset=-1,
        )
    )

for e in ["c3.prev", "c3_add", "c3_add2", "c3_3", "c3_eq"]:
    animators.append(
        StyleReplacer(svg_id=e, vcd_id="c3_lt_1000", replace=("opacity:0.25", "opacity:1"),
            compare=compareBitField(0), offset=-1,
        )
    )

# how many frames
frames = 350

sync = True

# files
svg_file = "examples/project-euler1/euler1.svg"
vcd_file = "examples/project-euler1/euler1.vcd"
