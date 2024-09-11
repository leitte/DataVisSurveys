---
layout: post
excerpt_image: NO_EXCERPT_IMAGE
title: "A Visual Analytics Framework for Reviewing Streaming Performance Data"
date: 2020-01-26
authors: S. P. Kesavan, T. Fujiwara, J. Li, C. J. Ross, M. Mubarak, C. Carothers, R. Ross & K. Ma
venue: "IEEE Pacific Visualization Symposium"
doi: 10.1109/PacificVis48177.2020.9280
categories:
  - Review
---
Understanding and tuning the performance of extreme-scale parallel computing systems demands a streaming approach due to the computational cost of applying offline algorithms to vast amounts of performance log data. Analyzing large streaming data is challenging because the rate of receiving data and limited time to comprehend data make it difficult for the analysts to sufficiently examine the data without missing important changes or patterns. To support streaming data analysis, we introduce a visual analytic framework comprising of three modules: data management, analysis, and interactive visualization. The data management module collects various computing and communication performance metrics from the monitored system using streaming data processing techniques and feeds the data to the other two modules. The analysis module automatically identifies important changes and patterns at the required latency. In particular, we introduce a set of online and progressive analysis methods for not only controlling the computational costs but also helping analysts better follow the critical aspects of the analysis results. Finally, the interactive visualization module provides the analysts with a coherent view of the changes and patterns in the continuously captured performance data. Through a multi-faceted case study on performance analysis of parallel discrete-event simulation, we demonstrate the effectiveness of our framework for identifying bottlenecks and locating outliers.
