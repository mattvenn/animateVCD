from animateVCD import Hide, TextReplacer, StyleReplacer, compareBitField, convertLookupTable, convertBinStrToInt, convertBinStrToHex, isHigh, isLow
instructions = {"0": "XX", "1": "nop", "2": "ld data", "4": "ld coeff", "8": "add", "16": "mult", "24": "add/mult", "32": "write"}
pipe_colour_1 = 'fill:#c8c4b7'
pipe_colour_2 = 'fill:#bcd35f'
# add the animators. The svg_id matches the ID in the SVG file, and the vcd_id is the name of the data in the VCD file
animators = [
    TextReplacer(svg_id='clock', vcd_id='clk', conversion=convertBinStrToInt()),
    TextReplacer(svg_id='count', vcd_id='count', conversion=convertBinStrToInt()),

    TextReplacer(svg_id='next_inst', vcd_id='inst', conversion=convertLookupTable(instructions)),
    TextReplacer(svg_id='inst1', vcd_id='inst1',    conversion=convertLookupTable(instructions)),
    TextReplacer(svg_id='inst2', vcd_id='inst2',    conversion=convertLookupTable(instructions)),
    TextReplacer(svg_id='inst3', vcd_id='inst3',    conversion=convertLookupTable(instructions)),
    TextReplacer(svg_id='inst4', vcd_id='inst4',    conversion=convertLookupTable(instructions)),
    TextReplacer(svg_id='inst5', vcd_id='inst5',    conversion=convertLookupTable(instructions)),

    StyleReplacer(svg_id='pip1', vcd_id='load_data', replace=(pipe_colour_1, pipe_colour_2), compare=isHigh()),
    StyleReplacer(svg_id='pip2', vcd_id='load_coeff', replace=(pipe_colour_1, pipe_colour_2), compare=isHigh()),
    StyleReplacer(svg_id='pip3', vcd_id='mult',      replace=(pipe_colour_1, pipe_colour_2), compare=isHigh()),
    StyleReplacer(svg_id='pip4', vcd_id='add',     replace=(pipe_colour_1, pipe_colour_2), compare=isHigh()),
    StyleReplacer(svg_id='pip5', vcd_id='write',    replace=(pipe_colour_1, pipe_colour_2), compare=isHigh()),

    StyleReplacer(svg_id='mem', vcd_id='mem_access', replace=('fill:#ffccaa', 'fill:orange'), compare=isHigh()),
    StyleReplacer(svg_id='collision', vcd_id='collision', replace=('fill:none', 'fill:red'), compare=isHigh()),

    Hide(svg_id='arrow-trans1', vcd_id='clk', compare=isLow()),
    Hide(svg_id='arrow-trans2', vcd_id='clk', compare=isLow()),
    Hide(svg_id='arrow-trans3', vcd_id='clk', compare=isLow()),
    Hide(svg_id='arrow-trans4', vcd_id='clk', compare=isLow()),
    Hide(svg_id='arrow-trans5', vcd_id='clk', compare=isLow()),
    ]

# how many frames 
frames = 40

# files
svg_file = "examples/MARLANN/marlann.svg"
vcd_file = "examples/MARLANN/test.vcd"
