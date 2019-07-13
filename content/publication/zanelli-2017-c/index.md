---
title: "A homotopy-based nonlinear interior-point method for NMPC"
date: 2017-10-18
publishDate: 2017-10-18
authors: ["Andrea Zanelli", "Rien Quirynen", "Juan Jerez", "Moritz Diehl"]
publication_types: ["2"]
abstract: "This paper introduces a homotopy-based nonlinear interior-point method that can exploit warm-starts for an efficient real-time implementation of nonlinear model predictive control (NMPC). The algorithm performs a homotopy on a tightened problem with a fixed value of the barrier parameter during which the initial state is changed gradually. Once an approximate solution to the tightened problem is obtained, a second homotopy is performed that shrinks the barrier parameter in order to compute a solution to the original problem. Theoretical results are presented on the local convergence, which provide a second order contraction estimate for both phases of the algorithm. In order to assess the potential of the proposed scheme, it has been implemented in the software package FORCES NLP. Its performance on a non-trivial NMPC case study is shown, where a speedup of up to one order of magnitude is obtained."
featured: false
publication: "*IFAC-PapersOnLine*"
doi: "10.1016/j.ifacol.2017.08.2175"
projects:
- ESR04
---

