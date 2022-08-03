from animateVCD import TextReplacer, StyleReplacer, compareBitField, convertBinStrToInt, convertBinStrToHex, Hide, isLow, isHigh, convertLookupTable
instructions = {0: "xx", 1: "A", 2: "B", 4: "C", 8: "D", 16: "E", 24: "add/mult", 32: "write"}

# add the animators. The svg_id matches the ID in the SVG file, and the vcd_id is the name of the data in the VCD file
# 1 for the counter
animators = [
    TextReplacer(svg_id='clock', vcd_id='clk', conversion=convertBinStrToInt()),
    TextReplacer(svg_id='clock2', vcd_id='clk2', conversion=convertBinStrToInt()),
    TextReplacer(svg_id='count', vcd_id='count', conversion=convertBinStrToInt()),

    TextReplacer(svg_id='stage0-text', vcd_id='inst', conversion=convertLookupTable(instructions)),
    TextReplacer(svg_id='stage1-text', vcd_id='stage0', conversion=convertLookupTable(instructions)),
    TextReplacer(svg_id='stage1-2-text', vcd_id='stage1', conversion=convertLookupTable(instructions)),
    TextReplacer(svg_id='stage2-text', vcd_id='stage1_2', conversion=convertLookupTable(instructions)),
    TextReplacer(svg_id='stage2-3-text', vcd_id='stage2', conversion=convertLookupTable(instructions)),
    TextReplacer(svg_id='stage3-text', vcd_id='stage3', conversion=convertLookupTable(instructions)),
    TextReplacer(svg_id='stage3-4-text', vcd_id='stage3_4', conversion=convertLookupTable(instructions)),

    Hide(svg_id='stage0-arrow', vcd_id='stage0_arrow', compare=isLow()),
    Hide(svg_id='stage1-arrow', vcd_id='stage1_arrow', compare=isLow()),

    Hide(svg_id='stage0-text', vcd_id='stage0_show', compare=isLow()),
    Hide(svg_id='stage0-box', vcd_id='stage0_show', compare=isLow()),

    Hide(svg_id='stage1-text', vcd_id='stage1_show', compare=isLow()),
    Hide(svg_id='stage1-box', vcd_id='stage1_show', compare=isLow()),

    Hide(svg_id='stage1-2-text', vcd_id='stage1_2_show', compare=isLow()),
    Hide(svg_id='stage1-2-box', vcd_id='stage1_2_show', compare=isLow()),
    Hide(svg_id='stage1-2-arrow', vcd_id='stage1_2_arrow', compare=isLow()),

    ]

# how many frames 
frames = 20

# files
svg_file = "examples/inter-clock-animation/inter.svg"
vcd_file = "examples/inter-clock-animation/test.vcd"
