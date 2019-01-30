all: animate.gif

# $@ The file name of the target of the rule.rule
# $< first pre requisite
# $^ names of all preerquisites

animate.gif: animateVCD.py 10seg.svg test.vcd
	python animateVCD.py
	convert -delay 50 -morph 0 frames/*svg $@

clean:
	rm -f animate.gif
	rm -f frames/*svg

.PHONY: all clean

