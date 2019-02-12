all: test.vcd

test.vcd: non-pipeline.v non-pipeline_tb.v
	iverilog -o non-pipeline non-pipeline_tb.v non-pipeline.v
	vvp non-pipeline
	gtkwave test.vcd gtk-non-pipeline.gtkw
