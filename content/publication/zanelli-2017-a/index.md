---
title: "A partially tightened real-time iteration scheme for nonlinear model predictive control"
date: 2017-12-12/2017-12-15
publishDate: 2017-12-12
authors: ["Andrea Zanelli", "Rien Quirynen", "Gianluca Frison", "Moritz Diehl"]
publication_types: ["1"]
abstract: "In this paper, a strategy is proposed to reduce the computational burden associated with the solution of problems arising in nonlinear model predictive control The prediction horizon is split into two sections and the constraints associated with the terminal one are tightened using a barrier formulation In this way, when using the Real-Time Iteration scheme, variables associated with such stages can be efficiently eliminated from the quadratic subproblems by a single backward Riccati sweep After eliminating the tightened stages, a quadratic problem with a reduced horizon is solved where the original constraints are used The solution is then expanded to the full horizon with a single forward Riccati sweep By doing so, the online computational burden associated with the solution of the optimization problems can be largely reduced Numerical results are reported where, using the proposed scheme, a speedup of about one order of magnitude can be achieved without compromising closed-loop performance"
featured: false
publication: "*2017 IEEE 56th Annual Conference on Decision and Control (CDC)*"
url_pdf: "https://cdn.syscop.de/publications/Zanelli2017a.pdf"
doi: "101109/CDC20178264306"
projects:
- ESR04
---

