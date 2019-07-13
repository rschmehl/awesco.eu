---
title: "Hardware Tailored Linear Algebra for Implicit Integrators in Embedded NMPC"
date: 2017-10-18
publishDate: 2017-10-18
authors: ["Gianluca Frison", "Rien Quirynen", "Andrea Zanelli", "Moritz Diehl", "John Bagterp Jørgensen"]
publication_types: ["2"]
abstract: "Nonlinear Model Predictive Control (NMPC) requires the efficient treatment of the dynamic model in the form of a system of continuous-time differential equations. Newton-type optimization relies on a numerical simulation method in addition to the propagation of first or higher order derivatives. In the case of stiff or implicitly defined dynamics, implicit integration schemes are typically preferred. This paper proposes a tailored implementation of the necessary linear algebra routines (LU factorization and triangular solutions), in order to allow for a considerable computational speedup of such integrators. In particular, the open-source BLASFEO framework is presented as a library of efficient linear algebra routines for small to medium-scale embedded optimization applications. Its performance is illustrated on the nonlinear optimal control example of a chain of masses. The proposed library allows for considerable speedups and it is found to be overall competitive with both a code-generated solver and a high-performance BLAS implementation."
featured: false
publication: "*IFAC-PapersOnLine*"
doi: "10.1016/j.ifacol.2017.08.2026"
projects:
- ESR04
---

