#!/bin/bash
# converts Latex code in original document file.svg into outline font in new document file_tex.svg

fname=$( basename -s .svg $1 )
echo $fname

# export svg to pdf and pdf_tex files
inkscape --export-pdf=$fname.pdf --export-latex --export-area-page $1

# compile with latex
pdflatex -jobname=tmp "\def\filename{$fname.pdf_tex}\input{template.tex}"

# simple PDF to SVG converter using minimally Cairo v1.2.6 and Poppler 0.5.4 (by David Barton)
# see http://www.cityinthesky.co.uk/opensource/pdf2svg/
pdf2svg tmp.pdf $fname'_tex.svg'

# clean up
rm -f tmp.* $fname.pdf $fname.pdf_tex