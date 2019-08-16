## Guidelines for publication input

We use the academic admin tool for importing publications from a central bibliography file (bibliography.bib).

### Works with standard version of academic admin Tool

`academic import --bibtex content/publication/bibliography.bib --overwrite`

* The publication abstract is imported via the bibtex field `abstract`.
* The month and year of the publication are imported via the fields `month` and `year`.

### Works only with [my own fork](https://github.com/rschmehl/academic-admin) of the tool

* Biblatex date format works
* Files `cite.bib` are generated
* Field entry `projects` can be used to specify project association

### Important

* Do *not* use dots to abbreviate middle initials in the BibTeX file. This disturbs the recognition of author names.
* There is one BibTeX entry `Folkersma2019a` which includes a Latex formula in the abstract. The admin tool does not transfer this properly to the markdown file, and for this reason I have kept this single entry in a separate file `bibliography2.bib` which needs to be processed separately.
* Also included in `bibliography2.bib` are PhD theses for which the `publication` entry needs to be populated manually (this could also be coded into the academic tool)
