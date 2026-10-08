# Paper build

Draft only: no experiments have been run; all results are `\TBD{...}` placeholders (red text).

Build (from this directory):

    pdflatex main && bibtex main && pdflatex main && pdflatex main
    # or: tectonic main.tex

`neurips_2026.sty` is not included; swap the `article` class for it when available.
Bib entries marked "to be verified" have titles recalled from memory and need checking.
