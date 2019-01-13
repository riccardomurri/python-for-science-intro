#! /usr/bin/make -f

# display usage help
usage:
	@echo "Type 'make ACTION', where ACTION is one of the following:"
	@echo
	@echo "clean -- Remove all temporary LaTeX files"
	@echo
	@echo "all -- Recompile all LaTeX files"
	@echo


# clean up temporary LaTeX files
clean:
	cd tex && rm -f *~ *.aux *.log *.nav *.out *.rel *.snm *.toc *.vrb


# remake all LaTeX files
all: $(patsubst tex/%.tex,%.pdf,$(wildcard tex/*.tex))


# the default wildcard rule for generating PDFs from `.tex` files
%.pdf: tex/%.tex tex/s3it.sty tex/beamerthemes3it.sty
	cd tex \
		&& pdflatex -output-directory $(CURDIR) -halt-on-error $< \
		&& pdflatex -output-directory $(CURDIR) -halt-on-error $<

# additional per-file dependencies
#
# these were generated from `\includegraphics` commands in the LaTeX source with::
#
#     $ egrep --only-matching '\\includegraphics\[.+\]\{([A-Za-z0-9/._-]+)\}' *.tex \
#         | sed -r -e 's|^([a-zA-Z0-9]+)\.tex:\\includegraphics.+\{([a-zA-Z0-9/._-]+)\}|\1.pdf: \1.tex \2|'
#
