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

# Introduction to Modular Forms

## The modular group

## Modular functions

````{prf:definition}
:label: modular_function

Let $k$ be an integer. We say that a function is *weakly modular* of weight $k$ if $f$ is meromorphic on the half plane $\mathbb{H}$ and verifies the relation

$$
f(z) = (cz+d)^{-2k}f\left(\frac{az+b}{cz+d}\right)
$$ (modl_fn)
````


### Motivation of the modularity condition

Consider the family of compact of orientable surfaces $\frac{\mathbb{H}}{G}$ where $G$ is a discrete subgroup of $SL_2(\mathbb{R})$. 

To study a surface, we want to study "nice" functions defined on the surface, for instance meromorphic functions. In this case, we want functions invariant with respect to the group action of $G$, i.e.

$$
f(gz) = f(z)\quad\forall\;g\in G
$$

These are hard to produce! So we relax the requirement to

$$
f(gz) = j(g,z)f(z)
$$

and note that if $f,g\neq 0$ satisfy this condition  then $\frac{f}{g}$ would be invariant under $G$.

By definition of group action, for $g_1$, $g_2\in G$, $\left(g_1g_2\right)z = g_1\left(g_2z\right)$. We deduce

$$
j(g_1g_2,z)f(z) = f\left(\left(g_1g_2\right)z\right) = f\left(g_1\left(g_2z\right)\right) = j(g_1,g_2z)f(g_2z) = j(g_1,g_2z)j(g_2,z)f(z)
$$ (j's chain rule)

So 

$$
j(g_1g_2,z)\;=\;j(g_1,g_2z)j(g_2,z)
$$

This is analogous to the chain rule for differentiation, so the easiest guess is

$$
j(g,z) = (gz)' = \frac{ad-bc}{(cz+d)^2} = (cz+d)^{-2}
$$

so that 

$$
(g_1g_2z)' = \left(g_1g_2\right)'(z) = g_2'(z)\cdot g_1'(g_2(z))
$$

and clearly $(cz+d)^{-2k}$ will also satisfy {eq}`j's chain rule`. 

We can rewrite the modularity condition {eq}`modl_fn` as 

$$
\frac{f(gz)}{f(z)} = \left(\frac{d(gz)}{dz}\right)^{-k}
$$

or

$$
f(gz)d(gz)^k\;=\;f(z)(dz)^k
$$

This means that the "differential form of weight $k$" $f(z)(dz)^k$ is *invariant* under $G$. 

$Sz = -\frac{1}{z}$, $Tz = z+1$. Since $G$ is generated by the elements $S$ and $T$, it suffices to check the invariance by $S$ and by $T$. This gives

```{prf:proposition}
:label: functional_equations_mf

Let $f$ be meromorphic on $\mathbb{H}$. The function $f$ is a weakly modular function of weight $2k$ iff it satisfies the two relations

$$
\begin{align}
f(z+1)&= f(z)\\
f\left(-\frac{1}{z}\right) &= z^{2k}\;f(z)
\end{align}
$$
```

Suppose $f(z+1) = f(z)$ is satisfied. We can then express $f$ as a function of $q = e^{2\pi iz}$, function which we will denote by $\tilde{f}$. It is meromorphic in the punctured disc $\left\{q\mid |q|<1,\;q\neq 0\right\}$. If $\tilde{f}$ extends to a meromorphic (resp.) holomorphic function at the origin, we say that $f$ is meromorphic (resp. holomorphic) at $\infty$. This means that $\tilde{f}$ admits a Laurent expansion in a neighbourhood of the origin

$$
\tilde{f}(q) = \sum_{-\infty}^{\infty}a_n\;q^n
$$

where $a_n$ are zero for $n$ small enough (resp. for $n<0$)

````{prf:definition}
:label: modular_fn

A weakly modular function $f$ is called *modular* if it is meromorphic at $\infty$.
````

````{prf:definition}
:label: modular_form

A modular function which is holomorphic everywhere (including $\infty$) is called a *modular form*; if such a function is zero at infinity, it is called a cusp form. 
````

A modular function of weight $2k$ is thus given by a series

$$
f(z) = \sum_{n=0}^{\infty} a_n\;q^n = \sum_{n=0}^{\infty}\;a_ne^{2\pi inz}
$$

which converges for $|q|<1$ (i.e. for Im$(z)>0$), and which verifies the identity

$$
f\left(-\frac{1}{z}\right) = z^{2k}\;f(z)
$$

It is a cusp form if $a_0 = 0$. 

````{prf:lemma}
If $f$ and $f'$ are modular forms of weight $2k$ and $2k'$, the product $ff'$ is a modular form of weight $2k + 2k'$.
````

### Examples of modular forms

````{prf:example}
:label: discriminant_modular_form

We define the $\Delta$ function and the Ramanujan $\tau$ function in the following way

$$
\Delta(z) := \frac{E_4(z)^3 - E_6(z)^2}{1728} = \sum_{n=1}^{\infty}\tau(n)q^n = q\cdot \prod_{n\geq 1}\left(1-q^n\right)^{24}
$$

The Fourier coefficients of $\Delta(z)$ are all integers, and they are also multiplicative, that is $\tau(mn) = \tau(m)\tau(n)$ if $(m,n)=1$. They also satisfy recurrence relations; if $p$ is a prime, then

$$
\tau\left(p^n\right) = \tau(p)\cdot \tau\left(p^{n-1}\right) - p^{11}\cdot \tau\left(p^{n-2}\right)
$$

for $n\geq 2$. These facts are consequences of the theory of *Hecke operators*. 

Fact: $\Delta$ is a cusp form of weight $12$. (In class 1 we took the third formula as the definition)

Question: Is $\tau(n) = 0$ for some $n\in \mathbb{N}$? The consensus is no. 
````

````{prf:example}

Let $k\geq 4$ be an even integer, and let $z\in \mathcal{H}$. The *Eisenstein series* of weight $k$ is 

$$
G_k(z)\;:=\;\frac{(k-1)!}{2(2\pi i)^k}\sum_{\substack{m,n\in \mathbb{Z}\\(m,n)\neq(0,0)}} \;\frac{1}{(mz+n)^k}
$$

```{prf:proposition}
$G_k(z)$ is a nonzero modular form of weight $k$ for $SL_2(\mathbb{Z})$.
```

The modular form $G_k(z)$ has Fourier expansion

$$
    G_k(z)\;:= \; -\frac{B_k}{2k} + \sum_{n\geq 1} \sigma_{k-1}(n)q^n
$$

where we define $\sigma_{r}(n)\;=\;\sum_{d\mid n, d>0}\;d^r\quad\forall\;r\in\mathbb{N}$. 

$$
    E_k(z)\;:=\;\frac{G_k(z)}{-\frac{B_k}{2k}} = 1 - \frac{2k}{B_k}\sum_{n=1}^{\infty}\sigma_{k-1}(n)q^n
$$

is called the *normalised Eisenstein series of weight $k$*. 
````


```{note}
The *Bernoulli numbers* are defined by

$$
\frac{x}{e^x - 1}\; =\; \sum_{k\geq 0}\quad B_k\;\frac{x^k}{k!}\;=\; 1\;-\;\frac{1}{2}\;x\;+\;\frac{1}{12}\;x^2\;-\;\dots
$$

($B_0 = 1$ , $B_1 = -\frac{1}{2}$ , $B_2 = \frac{1}{6}$ , $B_3 = 0$ , $\dots$)

Note that $B_{2n+1} = 0$ for $n\geq 1$ since $\frac{x}{e^x - 1}\;+\;\frac{x}{2}$ is an even function.

They are related to Riemann zeta function by

$$
    \zeta(2n)\;=\;\frac{(-1)^{n+1}\;B_{2n}\;(2\pi)^{2n}}{2\;(2n)!} \neq 0 \quad \forall\;n\in \mathbb{N}
$$
```