from animateVCD import TextReplacer, StyleReplacer, compareBitField, convertBinStrToInt, convertBinStrToHex, Hide, isLow, isHigh

# add the animators. The svg_id matches the ID in the SVG file, and the vcd_id is the name of the data in the VCD file
# 1 for the counter
animators = [
    TextReplacer(svg_id='reg-input-a', vcd_id='ra', conversion=convertBinStrToInt()),
    TextReplacer(svg_id='reg-input-b', vcd_id='rb', conversion=convertBinStrToInt()),
    TextReplacer(svg_id='reg-input-c', vcd_id='rc', conversion=convertBinStrToInt()),
    TextReplacer(svg_id='reg-input-d', vcd_id='rd', conversion=convertBinStrToInt()),


    TextReplacer(svg_id='stage1', vcd_id='stage1', conversion=convertBinStrToInt()),
    TextReplacer(svg_id='stage2', vcd_id='stage2', conversion=convertBinStrToInt()),
    TextReplacer(svg_id='out', vcd_id='out', conversion=convertBinStrToInt()),

    TextReplacer(svg_id='clock', vcd_id='clk', conversion=convertBinStrToInt()),
    TextReplacer(svg_id='count', vcd_id='count', conversion=convertBinStrToInt()),

    ]

# how many frames 
frames = 20

# files
svg_file = "examples/non-pipeline/non-pipeline.svg"
vcd_file = "examples/non-pipeline/test.vcd"
