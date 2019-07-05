---
title: Flight Dynamic and Aero-Elastic Analysis of Inflatable Tethered Wings
summary: Mikko Folkersma
authors: ["mikko-folkersma"]
tags:
- Modelling and Simulation
- Fluid Structure Interaction
date: "2018-12-06T00:00:00Z"

# Optional external URL for project (replaces project detail page).
external_link: ""

image:
  focal_point: Smart

url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
#slides: example
---

An accurate aerodynamic model of a kite operating in AWE system is essential, the kite must both be aerodynamically efficient and have a high steering capability. This project is about developing such a model, describing a fluid-structure interaction (FSI) model for inflatable membrane wings such as leading edge inflatable and ram-air kites. The proposed model combines three open-source software packages: [OpenFOAM](https://www.openfoam.com), mem4py and [preCICE](https://www.precice.org/). OpenFOAM is a popular computational fluid dynamics (CFD) software which is used to calculate the exterior flow and the stresses around the wing. For the structural deformation mem4py is used which specifically developed for membrane structures. The two solvers OpenFOAM and mem4py are coupled with preCICE coupling tool. The aerodynamic model in OpenFOAM has been validated by simulating rigid leading edge inflatable kite airfoils and comparing the results to available experimental results. The coupled FSI model is verified with an extended lid-driven cavity flow test case which includes a flexible membrane. After the verification and validation steps the coupled solver is used to study the aerodynamics of a ramair wing section
