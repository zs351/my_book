#RKHS
---
layout:     post
title:      "Part 2: Characterising RKHS with linear operators on Hilbert space"
subtitle:   "In this article, we will see how an RKHS can be constructed by a linear operator on a Hilbert space, which has an important example linking probability and RKHS of stationary kernels, i.e. Bochner's Theorem. For the second part, we will see any complete orthogonal system (CONS) in a separable Hilbert space will give rise to a characterisation of RKHS."
date:       2020-09-24 12:00
author:     "Eden"
tags: 		  [kernel, fundamentals of RKHS]
category:   math
---

```{math}

\newcommand\calH{\mathcal{H}}
\newcommand\calX{\mathcal{X}}
\newcommand\calF{\mathcal{F}}
\newcommand\floor[1]{\lfloor#1\rfloor}
\newcommand{\bmat}{\left[\begin{array}}
\newcommand{\emat}{\end{array}\right]}
\newcommand\inner[2]{\left\langle #1, #2 \right\rangle}
\newcommand\norm[1]{\lVert #1 \rVert}

```


_**Disclaimer.** This post is served as a summarisation of my study notes on RKHS theory [1], and classes I took on relevant topics, containing theoretical details from [1, 2] along with my interpretations directed by my personal interests on those topics. I am by no means an expert in functional analysis and spectral theory, so please feel free to point out any mistakes in the post.
<br/><br/>_

In this article, we will see the characterisation of RKHS as an image space of a linear operator associated with a feature map $\phi: \mathcal{X}\to\mathcal{H}$ on a (separable) Hilbert space $\mathcal{H}$. The construction of the reproducing kernel from $\phi$ is obvious as shown in [Part 1], however, what is more worthy of presenting is the direct construction of RKHS from a Hilbert space via the linear operator itself. We will show why this view is useful in practice via an import example, which is the Bochner's theorem. For Section 2, we will characterise RKHS with any CONS of the separable Hilbert space $\mathcal{H}$.

In the article, we use $\mathcal{H}$ to denote Hilbert space if without specification; and we use 'linear operator' and 'linear map' interchangeably. The theory can be easily extended to spaces of complex-valued functions, but we here only present the results with real-valued functions for simplicity.

Consider a feature map $\phi : \mathcal{X}\to \mathcal{H}$, then we define a linear operator $L : \mathcal{H}\to \mathcal{F}(\mathcal{X})$ from a Hilbert space $\mathcal{H}$ on $\mathcal{X}$ to the space of all real-valued functions on $\mathcal{X}$, s.t.

<h2 class="section-heading">RKHS via linear mappings</h2>

Consider a feature map $\phi : \mathcal{X}\to \mathcal{H}$, then we define a linear operator $L : \mathcal{H}\to \mathcal{F}(\mathcal{X})$ from a Hilbert space $\mathcal{H}$ on $\mathcal{X}$ to the space of all real-valued functions on $\mathcal{X}$, s.t.
<div>
$$
  L\mathbf{f} = \left\langle \mathbf{f}, \phi(\cdot)\right\rangle_{\mathcal{H}}\; \forall \mathbf{f}\in \mathcal{H}
$$
    
<h2 class="section-heading">RKHS via linear mappings</h2>
Consider a feature map $\phi : \mathcal{X}\to \mathcal{H}$, then we define a linear operator $L : \mathcal{H}\to \mathcal{F}(\mathcal{X})$ from a Hilbert space $\mathcal{H}$ on $\mathcal{X}$ to the space of all real-valued functions on $\mathcal{X}$, s.t.
<div>
$$
  L\mathbf{f} = \left\langle \mathbf{f}, \phi(\cdot)\right\rangle_{\mathcal{H}}\; \forall \mathbf{f}\in \mathcal{H}
$$



<h2 class="section-heading">References</h2>
1. Saitoh, S and Sawano, Y. Theory of reproducing kernels and applications. Springer, 2016.
2. Hofmann T, Schölkopf B, Smola AJ. Kernel methods in machine learning. The annals of statistics. 2008 Jun 1:1171-220.
3. Stein, M. Interpolation of spatial data: some theory for kriging. Springer Science & Business Media, 2012.
4. Wendland, H. Scattered data approximation. Vol.17. Cambridge university press, 2004.
