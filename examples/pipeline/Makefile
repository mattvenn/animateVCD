all: test.vcd

test.vcd:
	iverilog -o pipeline pipeline.v
	vvp pipeline
	gtkwave test.vcd gtk-pipeline.gtkw
