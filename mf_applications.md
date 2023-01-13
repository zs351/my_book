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

# Applications of modular forms

## Elliptic Curves and Modular Forms

````{prf:definition}
:label: elliptic_curve

Let $K$ be a field of characteristic not $2$ or $3$. We say that the set of projective solutions to 

$$
y^2z = x^3 + axz^2 + bz^3
$$

with $a,b\in K$ and $4a^3 + 27b^2 \neq 0$ is an *elliptic curve* in Weierstrass normal form. We call the integer

$$
\Delta(E) := 4a^3 + 27b^2
$$

the discriminant of $E$. 
````

Given an elliptic curve over $\mathbb{Q}$, we can choose coefficients to be integeral, by clearing denominators and then applying a birational transformation to return the elliptic curve to Weierstrass normal form. [Ask for details!] $\tilde{E} := E\left(\mathbb{F}_p\right)$ will be an elliptic curve if and only if $p\not\mid \Delta(E)$. (good reduction at $p$) 

We define $a_p(E)$ to be

$$
a_p(E)\;:=\;p+1-\left|E\left(\mathbb{F}_p\right)\right|
$$

if $p\not\mid \Delta(E)$. If $p\mid \Delta(E)$, we further distinguish two cases

If $\tilde{E}$ has a cusp, we say $E$ has additive reduction.

If $\tilde{E}$ has a node $P$ , we say $E$ has multiplicative reduction. If the slopes of the tangent lines are in $\mathbb{F}_p$, the reduction is said to be split multiplicative. Otherwise, it is non split multiplicative.

````{prf:definition}
:label: L-function of elliptic curve

Let $p$ be a prime. We define the *local part at $p$ of the L-series* as 

$$
L_p(E,s) = \begin{cases}
1 - a_p\;p^{-s} + p^{1-2s}&\text{good reduction}\\
1 - p^{-s}&\text{split multiplicative reduction}\\
1 + p^{-s}&\text{non split multiplicative reduction}\\
1 &\text{additive reduction}
\end{cases}
$$

The *L-function of the elliptic curve $E$* is the product

$$
L(E,s) = \prod_{p\text{ prime}}L_p(E,s)^{-1}
$$
````

````{prf:definition}
:label: modularity

For each modular form $f\in M_k\left(\Gamma_1(N)\right)$ with Fourier expansion $f(\tau) = \sum_{n=0}^{\infty} a_n\;q^n$, define its L-function to be $L(s,f) = \sum_{n=1}^{\infty}a_n\;n^{-s}$. 

An elliptic curve $E$ defined over $\mathbb{Q}$ is *modular* if there is a cusp form $f_{E}(\tau)$ such that 

$$
L(E,s) = L(s,f_{E})
$$
````

We can deduce that $f_E(\tau)$ must be a normalised eigenform of weight 2, thus yielding an algorithm to numerically verify that an elliptic curve over $\mathbb{Q}$ is modular. 




