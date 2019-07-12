---
title: "Nonlinear Model Predictive Control of a Human-sized Quadrotor"
date: 2018-06-01
publishDate: 2019-07-12T13:51:47.877367Z
authors: ["Andrea Zanelli", "Greg Horn", "Gianluca Frison", "Moritz Diehl"]
publication_types: ["1"]
abstract: "This paper discusses the design, implementation and deployment of an attitude controller for a quadrotor based on nonlinear model predictive control on a low-power embedded system  equipped  with  a  Cortex  A9  CPU  running  at  800MHz. Due to the limited computational power of the available hardware,  a  modified  interior-point  solver  for  the  so-called partially tightened Real-Time Iteration is used. The algorithm splits  the  prediction  horizon  in  two  sections.  A  Riccati-like recursion is exploited that relies on a single linearization of the complementarity conditions per sampling-time for the terminal section. In this way, it is possible to achieve a speedup of a factor3  with  respect  to  a  standard  real-time  iteration  formulation for  the  application  under  consideration.  Simulation  resultsthat show the improvement in performance obtained by using NMPC  over  standard  control  techniques  are  discussed  and experimental  results  using  the  proposed  implementation  a represented."
featured: false
publication: "*2018 European Control Conference (ECC)*"
doi: "10.23919/ECC.2018.8550530"
projects:
- ESR04
---
