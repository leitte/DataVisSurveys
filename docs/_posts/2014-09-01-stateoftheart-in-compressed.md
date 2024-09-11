---
layout: post
excerpt_image: NO_EXCERPT_IMAGE
title: "State‐of‐the‐Art in Compressed GPU‐Based Direct Volume Rendering"
date: 2014-09-01
authors: M. Balsa, E. Gobbetti, J. A. Iglesias-Guitian, M. Makhinya, F. Marton, R. Pajarola & S. Suter
venue: "Computer graphics forum (Print)"
doi: 10.1111/cgf.12280
categories:
  - spatial data
---
Great advancements in commodity graphics hardware have favoured graphics processing unit (GPU)‐based volume rendering as the main adopted solution for interactive exploration of rectilinear scalar volumes on commodity platforms. Nevertheless, long data transfer times and GPU memory size limitations are often the main limiting factors, especially for massive, time‐varying or multi‐volume visualization, as well as for networked visualization on the emerging mobile devices. To address this issue, a variety of level‐of‐detail (LOD) data representations and compression techniques have been introduced. In order to improve capabilities and performance over the entire storage, distribution and rendering pipeline, the encoding/decoding process is typically highly asymmetric, and systems should ideally compress at data production time and decompress on demand at rendering time. Compression and LOD pre‐computation does not have to adhere to real‐time constraints and can be performed off‐line for high‐quality results. In contrast, adaptive real‐time rendering from compressed representations requires fast, transient and spatially independent decompression. In this report, we review the existing compressed GPU volume rendering approaches, covering sampling grid layouts, compact representation models, compression techniques, GPU rendering architectures and fast decoding techniques.
