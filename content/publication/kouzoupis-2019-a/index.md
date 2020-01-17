---
title: "A dual Newton strategy for tree-sparse quadratic programs and its implementation in the open-source software treeQP"
date: 2019-03-05
publishDate: 2019-03-05
authors: ["Dimitris Kouzoupis", "Emil Klintberg", "Gianluca Frison", "Sebastien Gros", "Moritz Diehl"]
publication_types: ["2"]
abstract: "Summary This paper presents a dual Newton scheme for tree-sparse quadratic programs as they may arise in the field of stochastic programming. Previous work suggests to introduce auxiliary variables to decompose the tree into scenarios and use Newton's method to solve a dual problem formulation. Following a different approach, we apply the same principle directly on the tree-sparse problem, avoiding the increase in dimensionality. In combination with a tailored algorithm for the calculation of the step direction, which is typically the most expensive operation per iteration, the proposed algorithm achieves a linear complexity in the number of nodes and supports parallel processing of the tree branches in a stage-wise fashion. An open-source implementation of the presented dual Newton strategy is publicly available in treeQP, a toolbox of open-source solvers for tree-sparse quadratic programs."
featured: false
publication: "*International Journal of Robust and Nonlinear Control*"
doi: "10.1002/rnc.4503"
---

