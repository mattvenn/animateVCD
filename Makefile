all: animate.gif

# $@ The file name of the target of the rule.rule
# $< first pre requisite
# $^ names of all preerquisites

animate.gif: animate.py 7seg.svg
	python animate.py --vcd test.vcd --svg 7seg.svg --frames 16
	convert -delay 50 -morph 0 frames/*svg $@

clean:
	rm -f animate.gif
	rm -f frames/*svg

.PHONY: all clean

