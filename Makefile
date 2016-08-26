
#############################
## modify this list to add files.  
## NB: they will appear in the combined PDF
##     in the order listed.

FILES += draft-irtf-icnrg-ccnxmessages-04
FILES += draft-irtf-icnrg-ccnxsemantics-04
FILES += draft-mosko-icnrg-selectors-01

FILES += draft-mosko-icnrg-beginendfragment-01
FILES += draft-mosko-icnrg-ccnxchunking-02
FILES += draft-mosko-icnrg-ccnxuri-03
FILES += draft-mosko-icnrg-ccnxfragmentation-01
FILES += draft-mosko-icnrg-ccnxserialversion-01
FILES += draft-mosko-icnrg-ccnxtimeversion-02
FILES += draft-mosko-icnrg-cachecontrol-00

#FILES += draft-wood-icnrg-ccnxoverudp

#############################

TXT =  $(foreach x, $(FILES), $(x).txt)
HTML = $(foreach x, $(FILES), $(x).html)
PDF  = $(foreach x, $(FILES), $(x).pdf)

#############################
.PHONY: clean format pdf

all: format

format: $(TXT) $(HTML) $(PDF)

EXE := rfc2629/xml2rfc.tcl

%.txt: %.xml $(EXE)
	tclsh $(EXE) xml2rfc $< $@

%.html: %.xml $(EXE)
	tclsh $(EXE) xml2rfc $< $@

clean: 
	rm -f $(TXT) $(HTML) x.pdf $(FINAL)

$(FINAL): format
	sed -i "" 's/<br \/>[(ccnx)|(icnrg)].*<\/h1>/<\/h1>/' *.html
	htmldoc -f $(FINAL) --book --color --no-title --linkstyle plain --toclevels 1 --header "c h" --footer "  1" ${HTML}

install:
	@echo "Nothing to install from RFC directory"

%.pdf: %.html
	htmldoc -f $@ --book --color --no-title --linkstyle plain --toclevels 0 --header "c h" --footer "  1" $<

#pdf: $(HTML)
#	for f in *.html; do htmldoc -f $${f/html/pdf} --book --color --no-title --linkstyle plain --toclevels 0 --header "c h" --footer "  1" $$f; done

