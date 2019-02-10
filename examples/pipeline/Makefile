all: animate

animate:
	iverilog -o pipeline pipeline.v
	vvp pipeline
	gtkwave test.vcd gtk-pipeline.gtkw
	python animateVCD.py
