# Appendix D: Notation and Conventions

Consistent with the Geometric Series. Where domain-specific notation extends the parent conventions, the extension is marked with (GM).

---

## Manifolds and Spaces

| Symbol | Meaning | Introduced |
|---|---|---|
| $\mathcal{C}$ | Clinical decision complex (weighted simplicial complex) (GM) | Ch. 4 |
| $M$ | General manifold | Ch. 3, App. A |
| $\mathbb{R}^9$ | Nine-dimensional clinical-moral attribute space | Ch. 4 |
| $T_pM$ | Tangent space at $p \in M$ | App. A |
| $G$ | Goal region (acceptable clinical-moral outcomes) (GM) | Ch. 6 |

## Metrics, Distances, and Costs

| Symbol | Meaning | Introduced |
|---|---|---|
| $g$ | Riemannian metric on $M$ | Ch. 3, App. A |
| $g_{ij}$ | Metric components in local coordinates | App. A |
| $d(p, q)$ | Geodesic distance between $p$ and $q$ | App. A |
| $d_\Sigma(\mathbf{a}, \mathbf{b})$ | Mahalanobis distance with covariance $\Sigma$ (GM) | Ch. 4, App. A |
| $\Sigma$ | $9 \times 9$ clinical-moral covariance matrix (GM) | Ch. 4 |
| $\Sigma_{ij}$ | Cross-dimensional covariance between $d_i$ and $d_j$ (GM) | Ch. 4 |
| $w(v_i, v_j)$ | Clinical edge weight (Mahalanobis + boundary penalties) (GM) | Ch. 4 |
| $\text{CF}(\gamma)$ | Clinical friction: total path cost of $\gamma$ on $\mathcal{C}$ (GM) | Ch. 10 |

## The Nine Clinical-Moral Dimensions (GM)

| Symbol | Meaning | Introduced |
|---|---|---|
| $d_1$ | Clinical outcomes (survival, morbidity, function, symptom burden) | Ch. 4 |
| $d_2$ | Rights and obligations (right to treatment, duty of care, non-maleficence) | Ch. 4 |
| $d_3$ | Justice and fairness (equitable access, distributive justice) | Ch. 4 |
| $d_4$ | Autonomy (self-determination, voluntariness, freedom from coercion) | Ch. 4 |
| $d_5$ | Trust (therapeutic relationship, fiduciary duty, confidentiality) | Ch. 4 |
| $d_6$ | Social and relational impact (family, caregivers, community) | Ch. 4 |
| $d_7$ | Dignity and identity (sense of self, bodily integrity, personal values) | Ch. 4 |
| $d_8$ | Institutional legitimacy (standard of care, guidelines, regulatory compliance) | Ch. 4 |
| $d_9$ | Epistemic status (diagnostic certainty, prognostic accuracy, patient understanding) | Ch. 4 |

## Search and Pathfinding (GM)

| Symbol | Meaning | Introduced |
|---|---|---|
| $f(n)$ | Total evaluation function: $f(n) = g(n) + h(n)$ | Ch. 6 |
| $g(n)$ | Accumulated clinical cost from start to $n$ (evidence-based medicine) | Ch. 6 |
| $h(n)$ | Moral-heuristic estimate of remaining cost (clinical wisdom) | Ch. 6 |
| $h^*(n)$ | True minimum cost from $n$ to goal (unknown; $h$ approximates) | Ch. 7 |
| $\varepsilon$ | Admissibility tolerance: $h(n) \leq (1+\varepsilon) h^*(n)$ | Ch. 7 |
| $v_0$ | Start node (patient's presenting condition) | Ch. 6 |
| $\gamma$ | Path on $\mathcal{C}$ (sequence of clinical actions) | Ch. 6 |
| $\gamma^*$ | Clinical geodesic (minimum-cost path on the full manifold) | Ch. 6 |
| $\gamma_P^*$ | Policy-mandated path (path required by institutional policy $P$) | Ch. 12 |
| $\gamma_U^*$ | Utilitarian-optimal path (minimizes $d_1$ cost only) | Ch. 10 |

## Boundary Penalties (GM)

| Symbol | Meaning | Introduced |
|---|---|---|
| $\beta_k$ | Penalty for crossing clinical-moral boundary $k$ | Ch. 4 |
| $\beta_k^*$ | True cost of crossing boundary $k$ (including all consequences) | Ch. 7 |
| $\beta_k^{(\text{clin})}$ | Clinician's personal boundary penalty for boundary $k$ | Ch. 13 |
| $\beta_{\text{harm}}$ | Harm boundary ("first, do no harm") | Ch. 4 |
| $\beta_{\text{consent}}$ | Consent boundary (treating without valid consent) | Ch. 4 |
| $\beta_{\text{futile}}$ | Futility boundary (treating beyond clinical benefit) | Ch. 4 |
| $\beta_{\text{abandon}}$ | Abandonment boundary (withdrawing care from dependent patient) | Ch. 4 |
| $\beta_{\text{sacred}}$ | Sacred-value boundary ($= \infty$; absolute prohibition) | Ch. 4 |
| $\tau$ | Clinician's tolerance threshold for boundary crossing cost | Ch. 13 |

## Moral Injury (GM)

| Symbol | Meaning | Introduced |
|---|---|---|
| $\Delta \text{MI}(t)$ | Moral injury increment at time $t$ | Ch. 13 |
| $\text{MI}(T)$ | Cumulative moral injury at time $T$ | Ch. 13 |
| $\text{MI}_{\text{crit}}$ | Critical threshold for irreversible heuristic damage | Ch. 13 |
| $\text{MI}(P)$ | Moral Injury Index of policy $P$ | Ch. 13 |

## Structural Justice (GM)

| Symbol | Meaning | Introduced |
|---|---|---|
| $\text{BI}(P, S)$ | Clinical Bond Index of policy $P$ for population $S$ | Ch. 12 |
| $S$ | Patient population (demographic subgroup) | Ch. 12 |
| $P$ | Institutional policy | Ch. 12 |

## Gauge Invariance

| Symbol | Meaning | Introduced |
|---|---|---|
| $\tau$ | Meaning-preserving re-description (gauge transformation) | Ch. 8 |
| BIP | Bond Invariance Principle | Ch. 8 |
| $D_4$ | Dihedral group of order 8 (Hohfeldian symmetry on $d_2$) | Ch. 4 |

## Triage (GM)

| Symbol | Meaning | Introduced |
|---|---|---|
| $N$ | Set of patients in a triage problem | Ch. 10 |
| $R$ | Resource constraint (ventilators, beds, hours) | Ch. 10 |
| $r(\gamma_i)$ | Resource cost of patient $i$'s path | Ch. 10 |

## Conventions

- **Bold lowercase** ($\mathbf{a}$, $\mathbf{v}$): vectors in $\mathbb{R}^n$
- **Bold uppercase** ($\mathbf{S}$, $\Sigma$): matrices
- **Calligraphic** ($\mathcal{C}$, $\mathcal{M}$): complexes and abstract spaces
- **Blackboard bold** ($\mathbb{R}$): standard mathematical spaces
- **Greek lowercase** ($\gamma$, $\beta$, $\varepsilon$, $\tau$): curves, penalties, tolerances, transformations
- **Subscript indices** ($g_{ij}$, $\Sigma_{ij}$): tensor and matrix components
- **Superscript $(*)$**: optimal (geodesic) path or true cost
- **Superscript $(\text{clin})$**: clinician-specific value
- Einstein summation convention is used in Appendix A but not in the main text
- All logarithms are natural ($\ln$) unless specified as $\log_2$ or $\log_{10}$
- Statistical significance: * $p < 0.05$, ** $p < 0.01$, *** $p < 0.001$
- Dimension labels $d_1$--$d_9$ always refer to the nine clinical-moral dimensions (Definition 4.1)
- The symbol $G$ is context-dependent: goal region (Chapters 6--9) or gauge group (Chapter 8). Context disambiguates.
