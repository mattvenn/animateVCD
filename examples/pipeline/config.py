from animateVCD import TextReplacer, StyleReplacer, compareBitField, convertBinStrToInt, convertBinStrToHex

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
    
    ]

# how many frames 
frames = 20

# files
svg_file = "pipeline.svg"
vcd_file = "test.vcd"
