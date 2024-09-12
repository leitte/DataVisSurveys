---
layout: post
excerpt_image: NO_EXCERPT_IMAGE
title: "A Survey of GPU-Based Large-Scale Volume Visualization"
date: 2014-01-01
authors: J. Beyer, M. Hadwiger & H. Pfister
venue: "Eurographics Conference on Visualization"
doi: 10.2312/eurovisstar.20141175
categories:
  - survey
  - field data
  - performance
---
This survey gives an overview of the current state of the art in GPU techniques for interactive large-scale volume visualization. Modern techniques in this ﬁeld have brought about a sea change in how interactive visualization and analysis of giga-, tera-, and petabytes of volume data can be enabled on GPUs. In addition to combining the parallel processing power of GPUs with out-of-core methods and data streaming, a major enabler for interactivity is making both the computational and the visualization effort proportional to the amount and resolution of data that is actually visible on screen, i.e., “output-sensitive” algorithms and system designs. This leads to recent output-sensitive approaches that are “ray-guided,” “visualization-driven,” or “display-aware.” In this survey, we focus on these characteristics and propose a new categorization of GPU-based large-scale volume visualization techniques based on the notions of actual output-resolution visibility and the current working set of volume bricks—the current subset of data that is minimally required to produce an output image of the desired display resolution. For our purposes here, we view parallel (distributed) visualization using clusters as an orthogonal set of techniques that we do not discuss in detail but that can be used in conjunction with what we discuss in this survey.
