---
title: State and Parameters Estimation Implementations Based on MHE
summary: Fabian Girrbach
authors: ["Fabian Girrbach"]
tags:
- Sensors and Estimation
- Moving Horizon Estimation
date: "2018-12-05T00:00:00Z"
weight: 11

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

Accurate motion tracking and state estimation of a maneuvering kite are crucial for reliable and robust operation of AWE systems. On the other hand, rapid flight maneuvers are still challenging for state-of-the-art estimation algorithms. The objective of this project is to design, analyze, and implement optimization-based moving horizon estimators. The developed moving horizon estimators for sensor fusion using inertial sensors show a more robust estimation behavior. Moreover, the developed algorithms are particularly suited for online-calibration of the employed sensors and system parameters. The additional computational complexity of the algorithm are a challenge for the real-time implementation of moving horizon estimators on embedded systems with restricted computational resources. First, essential steps towards the full integration of optimization-based estimators are taken, and the promising results will influence the design of the next generation of Xsens motion trackers.
