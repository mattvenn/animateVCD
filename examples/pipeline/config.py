from animateVCD import TextReplacer, StyleReplacer, compareBitField, convertBinStrToInt, convertBinStrToHex, Hide, isLow, isHigh

# add the animators. The svg_id matches the ID in the SVG file, and the vcd_id is the name of the data in the VCD file
# 1 for the counter
animators = [
    TextReplacer(svg_id='reg-input-a', vcd_id='ra', conversion=convertBinStrToInt()),
    TextReplacer(svg_id='reg-input-b', vcd_id='rb', conversion=convertBinStrToInt()),
    TextReplacer(svg_id='reg-input-c', vcd_id='rc', conversion=convertBinStrToInt()),
    TextReplacer(svg_id='reg-input-d', vcd_id='rd', conversion=convertBinStrToInt()),

    TextReplacer(svg_id='stage1_c', vcd_id='stage1_c', conversion=convertBinStrToInt()),
    TextReplacer(svg_id='stage1_d', vcd_id='stage1_d', conversion=convertBinStrToInt()),
    TextReplacer(svg_id='stage2_d', vcd_id='stage2_d', conversion=convertBinStrToInt()),

    TextReplacer(svg_id='stage1', vcd_id='stage1', conversion=convertBinStrToInt()),
    TextReplacer(svg_id='stage2', vcd_id='stage2', conversion=convertBinStrToInt()),
    TextReplacer(svg_id='out', vcd_id='out', conversion=convertBinStrToInt()),

    TextReplacer(svg_id='clock', vcd_id='clk', conversion=convertBinStrToInt()),
    TextReplacer(svg_id='count', vcd_id='count', conversion=convertBinStrToInt()),

    StyleReplacer(svg_id='arrow-a', vcd_id='clk', replace=('opacity:0.4', 'opacity:1.0'), compare=isHigh()),
    StyleReplacer(svg_id='arrow-b', vcd_id='clk', replace=('opacity:0.4', 'opacity:1.0'), compare=isHigh()),
    StyleReplacer(svg_id='arrow-c', vcd_id='clk', replace=('opacity:0.4', 'opacity:1.0'), compare=isHigh()),
    StyleReplacer(svg_id='arrow-d', vcd_id='clk', replace=('opacity:0.4', 'opacity:1.0'), compare=isHigh()),
    StyleReplacer(svg_id='arrow-s1-1', vcd_id='clk', replace=('opacity:0.4', 'opacity:1.0'), compare=isHigh()),
    StyleReplacer(svg_id='arrow-s1-2', vcd_id='clk', replace=('opacity:0.4', 'opacity:1.0'), compare=isHigh()),
    StyleReplacer(svg_id='arrow-s1-3', vcd_id='clk', replace=('opacity:0.4', 'opacity:1.0'), compare=isHigh()),
    StyleReplacer(svg_id='arrow-s2-1', vcd_id='clk', replace=('opacity:0.4', 'opacity:1.0'), compare=isHigh()),
    StyleReplacer(svg_id='arrow-s2-2', vcd_id='clk', replace=('opacity:0.4', 'opacity:1.0'), compare=isHigh()),
    StyleReplacer(svg_id='arrow-out', vcd_id='clk', replace=('opacity:0.4', 'opacity:1.0'), compare=isHigh()),
    
    ]

# how many frames 
frames = 20

# files
svg_file = "examples/pipeline/pipeline.svg"
vcd_file = "examples/pipeline/test.vcd"
