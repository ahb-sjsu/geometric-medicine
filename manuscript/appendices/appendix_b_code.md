# Appendix B: Code Walkthrough

This appendix provides a guided walkthrough of the Python implementations that produce the computational results in this book. The code is organized in two modules: `ch21_clinical.py` (individual clinical decision-making, pathfinding, and moral injury) and `ch27_bioethics.py` (population-level allocation, the bioethical decision complex, and the clinical Bond Index). Both modules are self-contained and depend only on NumPy and SciPy.

All code examples are presented in the order they appear in the text. Line references are to the versions archived with this volume.

---

## B.1 The Clinical Decision Complex

The clinical decision complex is implemented as a weighted graph with 9-dimensional attribute vectors on vertices and Mahalanobis-plus-boundary-penalty weights on edges.

### B.1.1 Attribute Vectors

Each clinical state is represented by a 9-dimensional NumPy array:

```python
import numpy as np

# A clinical state: 9-dimensional attribute vector
# [d1: outcomes, d2: rights, d3: justice, d4: autonomy,
#  d5: trust, d6: social, d7: dignity, d8: institutional,
#  d9: epistemic]
state_a = np.array([0.7, 0.9, 0.8, 0.95, 0.6, 0.7, 0.85, 0.9, 0.5])
state_b = np.array([0.9, 0.9, 0.8, 0.95, 0.4, 0.7, 0.85, 0.9, 0.5])
```

The attribute vector captures the patient's clinical-moral state across all nine dimensions. Values are normalized to $[0, 1]$, where 1 represents the best achievable state on that dimension and 0 represents the worst.

### B.1.2 The Covariance Matrix

The $9 \times 9$ clinical-moral covariance matrix $\Sigma$ encodes cross-dimensional dependencies:

```python
def build_covariance_matrix(
    diagonal_weights: np.ndarray,
    cross_terms: dict[tuple[int, int], float]
) -> np.ndarray:
    """
    Construct the clinical-moral covariance matrix.

    Parameters
    ----------
    diagonal_weights : array of shape (9,)
        Variance of each clinical-moral dimension.
    cross_terms : dict mapping (i, j) pairs to covariance values
        Cross-dimensional dependencies (e.g., outcomes x trust).

    Returns
    -------
    Sigma : array of shape (9, 9)
        Symmetric positive-definite covariance matrix.
    """
    Sigma = np.diag(diagonal_weights)
    for (i, j), value in cross_terms.items():
        Sigma[i, j] = value
        Sigma[j, i] = value  # Symmetry
    # Verify positive definiteness
    eigenvalues = np.linalg.eigvalsh(Sigma)
    assert np.all(eigenvalues > 0), "Covariance matrix is not positive definite"
    return Sigma

# Example: critical cross-terms from the GCE paper
Sigma = build_covariance_matrix(
    diagonal_weights=np.ones(9),
    cross_terms={
        (0, 4): 0.3,   # Sigma_15: outcomes x trust
        (3, 8): 0.25,  # Sigma_49: autonomy x epistemic
        (2, 6): 0.2,   # Sigma_37: justice x dignity
    }
)
```

The cross-terms are the mathematically critical components. $\Sigma_{15}$ (outcomes $\times$ trust) encodes the fact that uncertain clinical outcomes are costlier when the therapeutic relationship is fragile. $\Sigma_{49}$ (autonomy $\times$ epistemic) encodes the fact that respecting autonomy requires adequate patient understanding. These are not philosophical assertions --- they are estimable from clinical decision data (see Chapter 17 for the experimental design).

### B.1.3 Edge Weights: Mahalanobis Distance Plus Boundary Penalties

```python
def clinical_edge_weight(
    state_from: np.ndarray,
    state_to: np.ndarray,
    Sigma_inv: np.ndarray,
    boundaries: list[dict],
) -> float:
    """
    Compute the clinical edge weight (Equation 4.2).

    Parameters
    ----------
    state_from, state_to : arrays of shape (9,)
    Sigma_inv : array of shape (9, 9), inverse covariance matrix
    boundaries : list of boundary definitions, each with:
        'check': callable returning True if boundary is crossed
        'penalty': float, the boundary penalty beta_k

    Returns
    -------
    weight : float, total clinical-moral cost of this action
    """
    delta = state_to - state_from
    mahalanobis = float(delta @ Sigma_inv @ delta)

    boundary_cost = sum(
        b['penalty'] for b in boundaries
        if b['check'](state_from, state_to)
    )

    return mahalanobis + boundary_cost
```

The boundary penalties represent clinical-moral thresholds. Each boundary has a detection function (does this action cross the boundary?) and a penalty value ($\beta_k$). Sacred-value boundaries have $\beta_k = \infty$ (represented computationally as `float('inf')`), which makes paths through them unreachable by $A^*$ search.

### B.1.4 Defining Boundaries

```python
# Example boundary definitions
def harm_boundary(state_from, state_to):
    """The Hippocratic boundary: does this action directly cause harm?"""
    return state_to[0] < state_from[0] - 0.2  # Significant outcome decline

def consent_boundary(state_from, state_to):
    """Does this action proceed without adequate informed consent?"""
    return state_to[3] < 0.3  # Autonomy drops below consent threshold

def futility_boundary(state_from, state_to):
    """Does this action continue treatment beyond clinical benefit?"""
    return state_from[0] < 0.1 and state_to[0] < 0.15  # Negligible outcome gain

def abandonment_boundary(state_from, state_to):
    """Does this action withdraw care from a dependent patient?"""
    return state_from[4] > 0.5 and state_to[4] < 0.2  # Trust collapse

boundaries = [
    {'check': harm_boundary, 'penalty': 5.0},
    {'check': consent_boundary, 'penalty': float('inf')},  # Sacred value
    {'check': futility_boundary, 'penalty': 3.0},
    {'check': abandonment_boundary, 'penalty': 8.0},
]
```

---

## B.2 Clinical $A^*$ Pathfinding

The clinical geodesic is computed by $A^*$ search on the clinical decision complex.

```python
import heapq

def clinical_astar(
    graph: dict,           # adjacency list: {node: [(neighbor, action), ...]}
    start: str,
    goals: set[str],
    states: dict,          # {node: np.ndarray} attribute vectors
    Sigma_inv: np.ndarray,
    boundaries: list[dict],
    heuristic_fn: callable,
) -> tuple[list[str], float]:
    """
    A* pathfinding on the clinical decision complex.

    Returns the clinical geodesic (minimum-cost path)
    and its total clinical friction.
    """
    open_list = [(0.0, start, [start])]
    g_costs = {start: 0.0}

    while open_list:
        f_cost, current, path = heapq.heappop(open_list)

        if current in goals:
            return path, g_costs[current]

        for neighbor, action in graph[current]:
            edge_w = clinical_edge_weight(
                states[current], states[neighbor],
                Sigma_inv, boundaries
            )

            if edge_w == float('inf'):
                continue  # Sacred-value boundary: path blocked

            tentative_g = g_costs[current] + edge_w

            if tentative_g < g_costs.get(neighbor, float('inf')):
                g_costs[neighbor] = tentative_g
                h = heuristic_fn(states[neighbor], goals, states)
                f = tentative_g + h
                heapq.heappush(open_list, (f, neighbor, path + [neighbor]))

    return None, float('inf')  # No path found: ethics consultation needed
```

The return value `None` corresponds to the clinical situation "path not found" --- a genuine ethical impasse where no available clinical action reaches an acceptable outcome without crossing a sacred-value boundary. This is the formal trigger for ethics consultation (Chapter 6, Table 6.1).

---

## B.3 Moral Injury Computation

The Moral Injury Index is computed from a sequence of clinical decisions and their boundary-crossing events.

```python
def compute_moral_injury(
    decisions: list[dict],
    clinician_betas: dict[str, float],
    threshold_tau: float,
) -> dict:
    """
    Compute cumulative moral injury (Equation 13.2).

    Parameters
    ----------
    decisions : list of dicts, each with:
        'boundaries_crossed': list of boundary names
        'time': int, time step
    clinician_betas : dict mapping boundary names to clinician's
        personal boundary penalty values
    threshold_tau : float, clinician's tolerance threshold

    Returns
    -------
    result : dict with 'cumulative_mi', 'trajectory', 'above_critical'
    """
    cumulative = 0.0
    trajectory = []
    MI_CRITICAL = 15.0  # Threshold for irreversible damage

    for decision in decisions:
        delta_mi = sum(
            max(0.0, clinician_betas.get(b, 0.0) - threshold_tau)
            for b in decision['boundaries_crossed']
        )
        cumulative += delta_mi
        trajectory.append({
            'time': decision['time'],
            'delta_mi': delta_mi,
            'cumulative_mi': cumulative,
        })

    return {
        'cumulative_mi': cumulative,
        'trajectory': trajectory,
        'above_critical': cumulative > MI_CRITICAL,
    }
```

The Moral Injury Accumulation Theorem (Theorem 13.1) is visible in the code: `cumulative` is monotonically non-decreasing (each `delta_mi >= 0`), the `above_critical` flag marks irreversible heuristic damage, and the computation is independent of burnout metrics.

### B.3.1 The Moral Injury Index for Policy Evaluation

```python
def moral_injury_index(
    policy: callable,
    case_distribution: list[dict],
    clinician_population: list[dict],
) -> float:
    """
    Compute the Moral Injury Index MI(P) (Definition 13.3).

    Estimates expected cumulative MI imposed by policy P
    on the clinician population over the case distribution.
    """
    total_mi = 0.0
    n_simulations = len(case_distribution) * len(clinician_population)

    for case in case_distribution:
        for clinician in clinician_population:
            decisions = policy(case)  # Policy determines actions
            result = compute_moral_injury(
                decisions,
                clinician['betas'],
                clinician['tau'],
            )
            total_mi += result['cumulative_mi']

    return total_mi / n_simulations
```

This function enables *prospective* policy evaluation: before implementing a triage protocol or resource allocation rule, estimate its expected moral injury on the clinician workforce. Policies with high MI(P) should be redesigned before deployment (Chapter 15).

---

## B.4 The Clinical Bond Index

The clinical Bond Index measures structural healthcare injustice.

```python
def clinical_bond_index(
    policy_paths: dict[str, list[float]],
    geodesic_paths: dict[str, list[float]],
    population: list[str],
) -> float:
    """
    Compute BI(P, S) = E[CF(gamma_P*) - CF(gamma_C*)] (Definition 12.1).

    Parameters
    ----------
    policy_paths : dict mapping patient ID to list of edge weights
        on the policy-mandated path
    geodesic_paths : dict mapping patient ID to list of edge weights
        on the clinical geodesic
    population : list of patient IDs in population S

    Returns
    -------
    bond_index : float, the expected manifold cost deviation
    """
    deviations = []
    for patient_id in population:
        policy_cost = sum(policy_paths[patient_id])
        geodesic_cost = sum(geodesic_paths[patient_id])
        deviations.append(policy_cost - geodesic_cost)

    return np.mean(deviations)
```

### B.4.1 Detecting Structural Injustice

```python
def detect_structural_injustice(
    policy_paths: dict,
    geodesic_paths: dict,
    populations: dict[str, list[str]],
) -> dict[str, float]:
    """
    Compute Bond Index for each population subgroup.

    If BI(P, S1) >> BI(P, S2), policy P imposes systematically
    higher moral cost on population S1 --- structural injustice.
    """
    results = {}
    for group_name, members in populations.items():
        results[group_name] = clinical_bond_index(
            policy_paths, geodesic_paths, members
        )
    return results

# Example usage (Chapter 12):
# bi_results = detect_structural_injustice(
#     policy_paths, geodesic_paths,
#     populations={
#         'Black patients': black_patient_ids,
#         'White patients': white_patient_ids,
#         'Disabled patients': disabled_patient_ids,
#         'Non-disabled patients': nondisabled_patient_ids,
#     }
# )
# If bi_results['Black patients'] >> bi_results['White patients'],
# the policy is structurally unjust toward Black patients.
```

The Bond Index converts "structural injustice" from a philosophical claim to an empirical measurement. It is computable from clinical data using existing instruments (Chapter 17, Section 17.3).

---

## B.5 The Bioethical Decision Complex (Population Scale)

The population-level extension from `ch27_bioethics.py` handles multi-agent allocation problems: triage, vaccine distribution, and organ transplant.

```python
def triage_allocation(
    patients: list[dict],
    resource_budget: int,
    Sigma_inv: np.ndarray,
    boundaries: list[dict],
) -> list[dict]:
    """
    Constrained multi-agent pathfinding (Definition 10.1).

    Minimize total clinical friction subject to resource constraints.
    This is the manifold-optimal triage, distinct from utilitarian
    triage which minimizes total d1 cost alone.
    """
    # Compute clinical friction for each patient's geodesic
    for patient in patients:
        patient['geodesic_cost'] = compute_geodesic_cost(
            patient['state'], patient['goal'],
            Sigma_inv, boundaries
        )

    # Greedy allocation by manifold cost (not by d1 alone)
    # Sort by ratio of clinical friction reduction per resource unit
    patients_sorted = sorted(
        patients,
        key=lambda p: p['geodesic_cost'] / p.get('resource_need', 1),
        reverse=True
    )

    allocated = []
    remaining_budget = resource_budget
    for patient in patients_sorted:
        need = patient.get('resource_need', 1)
        if need <= remaining_budget:
            allocated.append(patient)
            remaining_budget -= need

    return allocated
```

### B.5.1 Comparing Utilitarian and Manifold-Optimal Triage

```python
def triage_divergence_analysis(
    patients: list[dict],
    resource_budget: int,
    Sigma_inv: np.ndarray,
    boundaries: list[dict],
) -> dict:
    """
    Compute the divergence between utilitarian and manifold-optimal
    triage (Theorem 10.1).
    """
    # Utilitarian: maximize d1 (outcomes) only
    utilitarian = sorted(
        patients, key=lambda p: p['state'][0], reverse=True
    )[:resource_budget]

    # Manifold-optimal: minimize total clinical friction
    manifold = triage_allocation(
        patients, resource_budget, Sigma_inv, boundaries
    )

    util_ids = {p['id'] for p in utilitarian}
    manifold_ids = {p['id'] for p in manifold}

    return {
        'utilitarian_allocation': util_ids,
        'manifold_allocation': manifold_ids,
        'divergent_patients': util_ids.symmetric_difference(manifold_ids),
        'divergence_fraction': len(
            util_ids.symmetric_difference(manifold_ids)
        ) / len(patients),
    }
```

The divergence analysis (Chapter 10) demonstrates the Divergence Theorem: utilitarian and manifold-optimal triage coincide only when decisions activate only $d_1$ and no boundaries are crossed. In every pandemic scenario tested, the divergence fraction is non-zero.

---

## B.6 Reproducibility

All computational results in this book can be reproduced by:

1. Installing dependencies: `pip install numpy scipy`
2. Running `ch21_clinical.py` for individual clinical decision results (Chapters 4--9, 13--15)
3. Running `ch27_bioethics.py` for population-level allocation results (Chapters 10--12)
4. Comparing output against the tables and figures in the relevant chapters

Random seeds are fixed where stochastic elements appear. The code requires Python 3.10 or later. No GPU is required --- all computations run on CPU in under one minute on commodity hardware.
