# Appendix A: Mathematical Prerequisites

This appendix collects the mathematical definitions and results used throughout the book. It is self-contained for readers unfamiliar with differential geometry, simplicial complexes, or search algorithms; those with background in these areas may skip directly to the chapters. Full proofs and extended treatments can be found in *Geometric Methods in Computational Modeling* (Bond, 2026a) and *Geometric Reasoning* (Bond, 2026c).

---

## A.1 Smooth Manifolds

**Definition A.1 (Topological Manifold).** A *topological manifold* of dimension $n$ is a Hausdorff, second-countable topological space $M$ such that every point $p \in M$ has a neighborhood homeomorphic to an open subset of $\mathbb{R}^n$.

**Definition A.2 (Chart).** A *chart* on $M$ is a pair $(U, \varphi)$ where $U \subseteq M$ is open and $\varphi: U \to \mathbb{R}^n$ is a homeomorphism onto its image. The coordinates $x^1, \ldots, x^n$ given by $\varphi$ are *local coordinates* on $U$.

**Definition A.3 (Smooth Structure).** A *smooth atlas* is a collection of charts $\{(U_\alpha, \varphi_\alpha)\}$ covering $M$ such that all transition maps $\varphi_\beta \circ \varphi_\alpha^{-1}$ are smooth ($C^\infty$). A *smooth manifold* is a topological manifold equipped with a maximal smooth atlas.

*Clinical interpretation*: A clinical assessment framework (e.g., a triage protocol, a QALY calculator, an ethics committee rubric) is a chart on the clinical manifold. Each framework provides local coordinates for the patient's clinical-moral state. The transition map between charts is the conversion procedure between frameworks. The smoothness requirement says that small changes in a patient's state should produce small changes in any well-constructed clinical assessment. (See Chapter 4.)

---

## A.2 Riemannian Metrics and Geodesics

**Definition A.4 (Riemannian Metric).** A *Riemannian metric* on a smooth manifold $M$ is a smooth assignment of a positive-definite inner product $g_p: T_pM \times T_pM \to \mathbb{R}$ to each tangent space $T_pM$.

In local coordinates, $g = g_{ij} \, dx^i \otimes dx^j$, where $g_{ij}(p) = g_p(\partial_i, \partial_j)$.

**Definition A.5 (Geodesic).** A curve $\gamma: [0,1] \to M$ is a *geodesic* if it satisfies

$$\frac{d^2 \gamma^k}{dt^2} + \Gamma^k_{ij} \frac{d\gamma^i}{dt} \frac{d\gamma^j}{dt} = 0$$

where $\Gamma^k_{ij}$ are the Christoffel symbols of the Levi-Civita connection.

**Definition A.6 (Geodesic Distance).** The *geodesic distance* between $p, q \in M$ is

$$d(p, q) = \inf_\gamma \int_0^1 \sqrt{g_{\gamma(t)}(\dot{\gamma}(t), \dot{\gamma}(t))} \, dt$$

where the infimum is over all smooth curves from $p$ to $q$.

*Clinical interpretation*: The metric determines which clinical states are "close" --- i.e., which transitions have low cost. The clinical geodesic is the minimum-cost path from the patient's current state to an acceptable outcome. (See Chapters 4 and 6.)

---

## A.3 The Mahalanobis Distance

**Definition A.7 (Mahalanobis Distance).** Given a positive-definite matrix $\Sigma \in \text{SPD}(n)$ and vectors $\mathbf{a}, \mathbf{b} \in \mathbb{R}^n$, the *Mahalanobis distance* between $\mathbf{a}$ and $\mathbf{b}$ with respect to $\Sigma$ is

$$d_\Sigma(\mathbf{a}, \mathbf{b}) = \sqrt{(\mathbf{a} - \mathbf{b})^\top \Sigma^{-1} (\mathbf{a} - \mathbf{b})}$$

When $\Sigma = I$ (the identity matrix), this reduces to Euclidean distance. When $\Sigma$ captures covariance between dimensions, the Mahalanobis distance weights the contribution of each dimension and its cross-dimensional interactions.

**Proposition A.1.** The squared Mahalanobis distance $d_\Sigma^2(\mathbf{a}, \mathbf{b})$ is a positive-definite quadratic form. It defines a Riemannian metric on $\mathbb{R}^n$ with constant metric tensor $g_{ij} = (\Sigma^{-1})_{ij}$.

*Clinical interpretation*: The clinical edge weight (Definition 4.2 in Chapter 4) uses the Mahalanobis distance with the $9 \times 9$ clinical-moral covariance matrix $\Sigma$. This captures the crucial cross-dimensional dependencies: a treatment with uncertain outcomes ($d_1$) is costlier when the trust relationship is fragile ($d_5$), because $\Sigma_{15}$ is non-zero. Euclidean distance would treat these dimensions as independent; the Mahalanobis distance captures their interaction. (See Chapters 4--5.)

---

## A.4 Simplicial Complexes

**Definition A.8 (Abstract Simplicial Complex).** An *abstract simplicial complex* $K$ on a vertex set $V$ is a collection of non-empty subsets of $V$ (called *simplices*) such that: (a) every singleton $\{v\} \in K$ for $v \in V$; (b) if $\sigma \in K$ and $\tau \subseteq \sigma$ with $\tau \neq \emptyset$, then $\tau \in K$.

A simplex $\sigma$ with $|\sigma| = k + 1$ is a *$k$-simplex*. Vertices are 0-simplices, edges are 1-simplices, triangles are 2-simplices, and so on.

**Definition A.9 (Weighted Simplicial Complex).** A *weighted simplicial complex* is a simplicial complex $K$ together with a weight function $w: K \to \mathbb{R}_{\geq 0}$ that assigns a non-negative cost to each simplex.

*Clinical interpretation*: The clinical decision complex $\mathcal{C}$ (Definition 4.1) is a weighted simplicial complex. Vertices are clinical states (carrying 9-dimensional attribute vectors). Edges are clinical actions (carrying Mahalanobis + boundary penalty weights). Higher simplices are care bundles --- jointly administered interventions that must be evaluated as a unit. (See Chapter 4.)

---

## A.5 The $A^*$ Search Algorithm

**Definition A.10 ($A^*$ Search).** Given a weighted graph $G = (V, E, w)$ with start vertex $v_0$, goal set $G \subseteq V$, and heuristic function $h: V \to \mathbb{R}_{\geq 0}$, $A^*$ search finds a minimum-cost path from $v_0$ to $G$ by expanding vertices in order of $f(n) = g(n) + h(n)$, where:

- $g(n)$ is the cost of the cheapest known path from $v_0$ to $n$
- $h(n)$ is an estimate of the cost from $n$ to the nearest goal vertex

**Definition A.11 (Admissibility).** A heuristic $h$ is *admissible* if $h(n) \leq h^*(n)$ for all $n$, where $h^*(n)$ is the true minimum cost from $n$ to the goal.

**Theorem A.1 (Hart, Nilsson, and Raphael 1968).** If $h$ is admissible and consistent (i.e., $h(n) \leq w(n, n') + h(n')$ for every edge $(n, n')$), then $A^*$ returns an optimal path.

**Definition A.12 ($\varepsilon$-Admissibility).** A heuristic $h$ is *$\varepsilon$-admissible* if $h(n) \leq (1 + \varepsilon) \cdot h^*(n)$ for all $n$. An $\varepsilon$-admissible heuristic guarantees that $A^*$ returns a path costing at most $(1 + \varepsilon)$ times the optimum.

*Clinical interpretation*: Clinical reasoning is $A^*$ search on the clinical decision complex. The start node is the patient's presenting condition. The goal region is the set of acceptable clinical-moral outcomes. $g(n)$ is evidence-based medicine (accumulated clinical cost). $h(n)$ is clinical wisdom (the moral-heuristic estimate). Admissibility requires that clinical training calibrates boundary penalties as lower bounds on true moral cost. The $\varepsilon$-admissibility spectrum classifies clinical heuristics into four categories: strictly admissible, $\varepsilon$-admissible, inadmissible, and gauge-variant. (See Chapters 6--7.)

---

## A.6 Boundary Penalties and Edge Weights

**Definition A.13 (Clinical Edge Weight).** The weight of a clinical action $(v_i, v_j)$ on the clinical decision complex $\mathcal{C}$ is:

$$w(v_i, v_j) = \underbrace{\Delta \mathbf{a}^\top \Sigma^{-1} \Delta \mathbf{a}}_{\text{Mahalanobis distance}} + \underbrace{\sum_k \beta_k \cdot \mathbf{1}[\text{boundary } k \text{ crossed}]}_{\text{boundary penalties}}$$

where $\Delta \mathbf{a} = \mathbf{a}(v_j) - \mathbf{a}(v_i)$ is the change in the 9-dimensional attribute vector, $\Sigma$ is the $9 \times 9$ clinical-moral covariance matrix, and $\beta_k$ is the penalty for crossing clinical-moral boundary $k$.

**Remark.** The edge weight has two components. The Mahalanobis component measures the *distance* traveled on the manifold --- how much the patient's clinical-moral state changes. The boundary component measures the *cost* of crossing ethical thresholds --- the discontinuous jumps in moral cost at professional norms (harm, consent, futility, abandonment, sacred values). The total weight is the sum of continuous and discontinuous costs. (See Chapters 4--5.)

---

## A.7 Gauge Invariance

**Definition A.14 (Gauge Transformation).** A *gauge transformation* $\tau$ is a meaning-preserving re-description of the clinical situation --- a change in how information is framed, presented, or described that does not alter the underlying clinical-moral state.

**Definition A.15 (Gauge Invariance).** A clinical evaluation $E$ is *gauge-invariant* if $E(\tau(x)) = E(x)$ for all meaning-preserving transformations $\tau$.

**Definition A.16 (Bond Invariance Principle).** An ethical evaluation is valid only if it is gauge-invariant: the evaluation must depend on the clinical-moral state, not on its description.

*Clinical interpretation*: Informed consent is a gauge-invariance condition: the patient's clinical decision must be invariant under meaning-preserving reframing. If "90% survival rate" and "10% mortality rate" produce different treatment decisions, the patient's heuristic is gauge-variant, and consent is not genuinely informed regardless of what the form says. Algorithmic bias in medical AI is also a gauge-invariance violation: if a clinical decision support system produces different recommendations for the same clinical state described with different demographic labels, the system violates the medical BIP. (See Chapter 8.)

---

## A.8 The Scalar Irrecoverability Theorem

**Theorem A.2 (Scalar Irrecoverability; Bond 2026c).** Let $Q: \mathbb{R}^n \to \mathbb{R}$ be any function mapping an $n$-dimensional state to a scalar ($n > 1$). Then:

1. $Q$ is not injective: multiple distinct states map to the same scalar value.
2. The information destroyed by $Q$ is irrecoverable: there exists no function $\psi: \mathbb{R} \to \mathbb{R}^n$ such that $\psi \circ Q = \text{id}$.
3. The optimal path on the full $n$-dimensional manifold is in general different from the scalar-optimal path, and the divergence is not bounded by any function of $Q$ alone.

**Proof sketch.** By the rank-nullity theorem, the kernel of $dQ$ has dimension $\geq n - 1$ at every regular point. Information in the kernel is irrecoverable by the data processing inequality. Part (3) follows by constructing specific examples where the scalar-optimal and manifold-optimal paths diverge arbitrarily.

*Clinical interpretation*: This is the QALY Irrecoverability Theorem (Theorem 5.1). With $n = 9$, any QALY function destroys at least 8 dimensions of clinical-moral information. The destruction is mathematical, not a failure of implementation. (See Chapter 5.)
