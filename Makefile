GIFS = examples/pipeline/pipeline.gif examples/non-pipeline/non-pipeline.gif examples/MARLANN/MARLANN.gif examples/10seg/10seg.gif
all: $(GIFS)

# $@ The file name of the target of the rule.rule
# $< first pre requisite
# $^ names of all preerquisites

examples/non-pipeline/non-pipeline.gif: 
	./animateVCD.py --config examples/non-pipeline
	convert -delay 50 -morph 0 frames/*svg $@

examples/pipeline/pipeline.gif: 
	./animateVCD.py --config examples/pipeline
	convert -delay 50 -morph 0 frames/*svg $@

examples/MARLANN/MARLANN.gif: 
	./animateVCD.py --config examples/MARLANN
	convert -delay 50 -morph 0 frames/*svg $@

examples/10seg/10seg.gif: 
	./animateVCD.py --config examples/10seg
	convert -delay 50 -morph 0 frames/*svg $@

clean:
	rm -f frames/*svg

.PHONY: all clean

