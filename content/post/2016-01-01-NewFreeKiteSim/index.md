---
title: 'New Version of FreeKiteSim released'
subtitle: 'Version 0.4 of the open source kite power system simulation software FreeKiteSim was just released.'
summary: Version 0.4 of the open source kite power system simulation software FreeKiteSim was just released.
authors:
- roland-schmehl
tags:
- Open Source Software
- Kite Power System simulation
- Dynamic System Model
categories: []
date: "2016-01-01T00:00:00Z"
lastmod: "2016-01-01T00:00:00Z"
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal point options: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight
image:
  caption: 'Image credit: Uwe Fechner'
  focal_point: ""
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---

The FreeKiteSim project aims at the development of a free kite-power system simulator for educational purposes and research. It is intended to be used to

* provide a learning environment for students and PhD researchers who are investigating airborne wind energy,
* train kite pilots and winch operators. In this case kite and winch are operated with joysticks,
* develop and test automatic control software for kite-power systems.


For more information, visit the [project page](https://bitbucket.org/ufechner/freekitesim) on bitbucket and subscribe to the [mailing list](https://groups.google.com/forum/#!forum/free-kitesim) to stay updated on the latest changes.

The most striking improvements of this new version are a 6-fold speed increase of the simulator which was achieved by updating the code to use numba 0.18 and reimplementing the core functions such that they do not have to allocate memory for temporary calculation results.
Furthermore, a bug was fixed which makes the tether drag calculation significantly more accurate. The underlying calculations are explained in the paper [Dynamic Model of a Pumping Kite Power System](https://doi.org/10.1016/j.renene.2015.04.028), which was published in Renewable Energy. The preprint of the paper can be downloaded from [arxiv](http://arxiv.org/abs/1406.6218).

Apart from the simulation code, we also updated the installation script and uploaded a meta-package to our [conda package server](https://conda.binstar.org/ufechner). This way, if you are already using conda, the installation can easily be done by getting the freekitesim package. Obviously the installation script can still be used as a clean way without the whole conda environment system.

The complete list of changes is as follows

* Updated the code for the use of numba 0.18.2 leading to much faster execution and a large decrease of the startup time
* Reimplemented the core functions to not allocate memory for temporary arrays leading to an execution time decrease by a factor of 3, making the code 6 times faster in total
* Code enables the use of different wind profile laws
* Fixed a bug in the tether drag calculation which should be much more accurate now
* Next to the installation script the installation can be done by using a conda package
* Uses newest packages except for pandas and cgkit which need to be pinned with conda.
