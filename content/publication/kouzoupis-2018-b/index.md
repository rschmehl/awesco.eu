---
title: "A dual Newton strategy for scenario decomposition in robust multistage MPC"
date: 2017-12-21
publishDate: 2017-12-21
authors: ["Dimitris Kouzoupis", "Emil Klintberg", "Moritz Diehl", "Sebastien Gros"]
publication_types: ["2"]
abstract: "Summary This paper considers the solution of tree-structured quadratic programs as they may arise in multistage model predictive control. In this context, sampling the uncertainty on prescribed decision points gives rise to different scenarios that are linked to each other via the so-called nonanticipativity constraints. Previous work suggests to dualize these constraints and apply Newton's method on the dual problem to achieve a parallelizable scheme. However, it has been observed that the globalization strategy in such an approach can be expensive. To alleviate this problem, we propose to dualize both the nonanticipativity constraints and the dynamics to obtain a computationally cheap globalization. The dual Newton system is then reformulated into small highly structured linear systems that can be solved in parallel to a large extent. The algorithm is complemented by an open-source software implementation that targets embedded optimal control applications."
featured: false
publication: "*International Journal of Robust and Nonlinear Control*"
doi: "10.1002/rnc.4019"
---

