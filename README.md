# AWESCO network website

This website is derived from the hugo [academic kickstart](https://github.com/sourcethemes/academic-kickstart) project.

It is based on [version 4.4 (WIP)](https://sourcethemes.com/academic/updates/v4.4.0/) of hugo academic.

## Requirements

* Hugo Extended v0.55.6+

## Literature database

My aim for this website was to build the entire `publications` folder from the BibTeX file `bibliography.bib`, with minimal adjustments. This can be done by using a modified version of the academic admin tool. Setup this toolchain by cloning the source code from [this](https://github.com/rschmehl/academic-admin) repository and install locally by executing

    pip3 install -e .

from within the source code top level directory. The content of the `publication` folder is then built by

    academic import --bibtex content/publication/bibliography.bib --overwrite

More information can be found in the `README.md` file of the `content/publication` folder.

## Synchronizing local development with public server

Run from home directory

    rclone sync public/ awesco-new:httpdocs

## Updating

[Configure Git to sync your fork with the original Spoon-Knife repository](https://help.github.com/en/articles/fork-a-repo#keep-your-fork-synced)
