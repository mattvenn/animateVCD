all: test.vcd

test.vcd: non-pipeline.v
	iverilog -o non-pipeline non-pipeline.v
	vvp non-pipeline
	gtkwave test.vcd gtk-non-pipeline.gtkw
