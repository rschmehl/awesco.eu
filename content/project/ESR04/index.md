---
title: Efficient Numerical Methods for NMPC in AWE Applications with Stability Guarantees
summary: Andrea Zanelli
authors: ["Andrea Zanelli"]
tags:
- Sensors and Estimation
- Optimal Control
date: "2018-12-06T00:00:00Z"
weight: 4

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

This report summarizes the work carried out by the ESR in the field of numerical methods for
nonlinear model predictive control (NMPC) with applications to airborne wind energy (AWE) systems.
In particular, the ESR has focuses on the development of efficient algorithms and software
implementations that exploit inexact optimal control formulations and inexact quantities that can be
computed with lower computational effort.
The present document describes the motivation for the need of efficient NMPC algorithms and the
challenges that need to be overcome in order to obtain real-time feasible implementation that can
be leveraged in applications with short sampling times. Both theoretical and practical contributions
have been made in the field.
Approximate schemes with stability and feasibility guarantees have been developed that can lead to
significantly improved computation times with limited control performance degradation. These
schemes are based both on the usa of approximate optimal control formulations, e.g. by
approximating some of the constraints in the nonlinear programs (NLP) to be solved, and on the use
approximate quantities in the algorithms used to so such problems, e.g. approximating the
sensitivities involved. Finally, the special class of “real-time” algorithms is studied. In this last
approach the NLP are never solved to local optimality, but rather a single Newton-type step is used
to track the optimal manifold as the state of system evolves. In this way a suboptimal, but stabilizing
scheme, is obtained that can achieve considerably shorter computation times. The results already
present in the literature on the so called real-time iteration (RTI) scheme are extended to a broader
class of methods called generalized real-time iterations (gRTI).
The algorithms and software implementations have been tested on real-world systems with
promising results in terms of both control performance and computation times.
