---
title: Low-Order Aerodynamic Models in the Optimization of Multi-Kite Systems
summary: Rachel Leuthold
authors: ["rachel-leuthold"]
tags:
- System Design and Optimisation
- Optimal Control
- Multi-Kite Airborne Wind Energy System
date: "2018-11-27T00:00:00Z"
weight: 3

# Optional external URL for project (replaces project detail page).
external_link: ""

image:
  focal_point: Smart

links:
- icon: twitter
  icon_pack: fab
  name: Follow
  url: https://twitter.com/kite_power
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

Optimal control is one strategy to prepare for the preliminary design of multi-kite airborne wind
energy systems (MAWES). However, the solution of an optimal control problem (OCP) can only be as
good as the modeled physical constraints. This thesis intends to find a wake induction model that is
sufficiently fast to work in interactive numerical optimization, while being sufficiently accurate to give
meaningful OCP solutions. Work so far has determined that: a wake model is necessary, that the
model should be valid over applicable wind environments, that the model should include unsteady
effects. A fast wake model suitable for MAWES (an engineering induction model) has been proposed,
and work is ongoing to synthesize a model with a wider region of validity.
