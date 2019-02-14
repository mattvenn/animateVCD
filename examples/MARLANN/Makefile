all: test.vcd

# $@ The file name of the target of the rule.rule
# $< first pre requisite
# $^ names of all preerquisites

test.vcd: test.v marlann.v config.py
	iverilog -o pipeline marlann.v test.v
	vvp pipeline
#	gtkwave test.vcd gtk-marlann.gtkw

.PHONY: all prog clean
