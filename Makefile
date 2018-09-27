all: build/plot.pdf

build/plot.pdf: plot.py | build
	python plot.py

build:
	mkdir -p build

clean:
	rm -rf build

.PHONY: all clean