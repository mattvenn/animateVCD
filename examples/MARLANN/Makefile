all: test.vcd

# $@ The file name of the target of the rule.rule
# $< first pre requisite
# $^ names of all preerquisites

test.vcd: test.v pipeline.v
	iverilog -o pipeline pipeline.v test.v
	vvp pipeline
	gtkwave test.vcd gtk-pipe.gtkw

.PHONY: all prog clean
