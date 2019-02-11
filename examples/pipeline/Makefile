all: test.vcd

test.vcd: pipeline.v
	iverilog -o pipeline pipeline.v
	vvp pipeline
	gtkwave test.vcd gtk-pipeline.gtkw
