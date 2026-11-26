# Figure placeholders replaced by drawn figures (2026-11-26)

Before the figures of 2026-11-26 were drawn, these chapters carried bracketed descriptions
of intended figures. They were taken out of the chapters when the drawn figures went in,
because their numbers collided with the drawn figures and several described content the
chapter does not contain. They are kept here as the original figure plan. The numbers are
the placeholders' own, not those of the drawn figures. Each carries the verdict reached
when the figures were drawn.

## Placeholder 1.1 (manuscript/part_i/ch01_qaly_trap.md)

[Figure 1.1: Two patients with identical QALY scores of 0.4, visualized in the nine-dimensional clinical decision complex. Patient A has moderate physical limitation ($d_1 = 0.4$) but intact trust ($d_5 = 0.9$), autonomy ($d_4 = 0.9$), dignity ($d_7 = 0.8$), and understanding ($d_9 = 0.8$). Patient B has better physical function ($d_1 = 0.6$) but degraded trust ($d_5 = 0.2$), coerced autonomy ($d_4 = 0.3$), diminished dignity ($d_7 = 0.3$), and poor understanding ($d_9 = 0.2$). The QALY projection collapses both to the same scalar. The nine-dimensional profiles are radically different, and the clinical geodesic --- the optimal path through the decision space --- differs accordingly.]

**Verdict:** Wrong. Its values (d1 = 0.4 and 0.6, QALY 0.4 and so on) appear nowhere in the chapter. Replaced by drawn Figure 1.1, the two patients of Section 1.6.

## Placeholder 1.2 (manuscript/part_i/ch01_qaly_trap.md)

[Figure 1.2: The four geometric structures destroyed by clinical scalar metrics. (a) Metric: continuous clinical-moral distance replaced by ordinal or scalar projection. (b) Cross-dimensional: $\Sigma_{ij}$ covariance between dimensions erased by dimensional collapse. (c) Boundary: clinical-moral thresholds invisible to continuous scalars. (d) Trajectory: temporal path structure discarded by point-in-time or integral summaries.]

**Verdict:** Not drawn. A four-panel restatement of prose with nothing to compute.

## Placeholder 1.3 (manuscript/part_i/ch01_qaly_trap.md)

[Figure 1.3: Scalar irrecoverability in clinical context. The nine-dimensional clinical-moral state space is projected onto the one-dimensional QALY axis. The preimage of a QALY value $Q = 0.4$ is an eight-dimensional hyperplane. All patients on this hyperplane are indistinguishable to QALY-based allocation. The hyperplane contains patients with radically different trust, autonomy, dignity, justice, and understanding profiles. The information that distinguishes them --- the information needed for equitable, patient-centered care --- is irrecoverable from the scalar.]

**Verdict:** Not drawn in Chapter 1; the idea is drawn Figure 5.1. It says hyperplane, which holds only for a linear Q.

## Placeholder 1.4 (manuscript/part_i/ch01_qaly_trap.md)

[Figure 1.4: The two-patient problem. Patient A and Patient B have identical QALY projections (0.35) but radically different nine-dimensional attribute vectors. Patient A's needs are concentrated on $d_1$ (outcomes, via palliative optimization) with intact non-$d_1$ dimensions. Patient B's needs are concentrated on $d_4$ (autonomy), $d_5$ (trust), $d_7$ (dignity), and $d_9$ (understanding), with $d_1$ treatment contingent on resolving these dimensions first. The clinical geodesics diverge immediately from the start node.]

**Verdict:** Drawn as Figure 1.1, without the part on diverging geodesics.

## Placeholder 2.1 (manuscript/part_i/ch02_triage_forced_contraction.md)

[Figure 2.1: Dr. Kim's ninety-second triage of four patients, represented on the nine-dimensional clinical decision complex. Each patient occupies a point in the nine-dimensional space. The triage decision contracts each nine-dimensional state to a single ordinal ranking (ESI level). The figure shows the information lost in each contraction: Patient 1 loses the futility/abandonment boundary trade-off; Patient 3 loses the justice dimension (back of the line means waiting longest despite arriving first by ambulance).]

**Verdict:** Not drawn. The chapter gives no vectors for Dr. Kim's four patients, and 'arriving first by ambulance' is unsupported: all four came in the first wave.

## Placeholder 2.2 (manuscript/part_i/ch02_triage_forced_contraction.md)

[Figure 2.2: Historical evolution of triage dimensionality. Larrey (1792): $d_1$ only. Geneva Conventions (1864--1949): $d_1 + d_2 + d_3$. ESI (2011): $d_1 + d_8$. START (1983): three binary physiologic parameters within $d_1$. CSC (2020): stated as $d_1 + d_3 + d_7$, implemented as $d_1$ only. Each system is a specific projection of the nine-dimensional clinical decision complex.]

**Verdict:** Inconsistent. It lists ESI (2011) before START (1983) and states CSC as d1 + d3 + d7, where Section 2.2.4 gives four values and Section 10.8 gives d1 + d3. Drawn from Section 10.8 as Figure 10.2.

## Placeholder 2.3 (manuscript/part_i/ch02_triage_forced_contraction.md)

[Figure 2.3: Maria Santos evaluated by three triage systems. Each system projects her nine-dimensional state onto a different subspace. ESI: $d_1 + d_8$ (acuity + resources). START: three binary parameters within $d_1$. CSC: $d_1$ weighted by prognosis. The nine-dimensional attribute vector is the same in all three cases. The triage classifications are different. The moral residue is different. The patient is the same.]

**Verdict:** Drawn as Figure 2.1.

## Placeholder 3.1 (manuscript/part_i/ch03_history_medical_ethics.md)

[Figure 3.1: Principlism as a four-dimensional projection of the nine-dimensional clinical decision complex. The four principles map to $d_1$ (beneficence), $d_2 + \beta_{\text{harm}}$ (non-maleficence), $d_3$ (justice), and $d_4$ (autonomy). The remaining five dimensions ($d_5$--$d_9$) are discarded. The "conflict" between autonomy and beneficence is, on the full manifold, resolved by the metric: the clinical geodesic navigates both dimensions simultaneously.]

**Verdict:** Not drawn as its own figure; the Beauchamp and Childress row of drawn Figure 3.1 covers it.

## Placeholder 3.2 (manuscript/part_i/ch03_history_medical_ethics.md)

[Figure 3.2: Twenty-five centuries of manifold discovery. Timeline showing each tradition and its dimensional contribution to the clinical decision complex. The nine dimensions accumulate across the history, with each tradition adding or foregrounding specific dimensions. The geometric framework (2026) captures all nine simultaneously and provides the resolution algorithm --- pathfinding on the full manifold --- that the history has been seeking.]

**Verdict:** Drawn as Figure 3.1. Overstated: the Section 3.10 table does not show the nine dimensions accumulating; d7 and d8 are named by no tradition.

## Placeholder 4.1 (manuscript/part_ii/ch04_clinical_manifold.md)

[Figure 4.1: The clinical decision complex for a simple clinical scenario. Vertices: healthy, diagnosed, treated, recovered, deceased. Edges: diagnostic test, treatment, supportive care, disease progression. Each vertex carries a nine-dimensional attribute vector; each edge carries a weight computed from the Mahalanobis distance plus boundary penalties. The clinical geodesic is the minimum-cost path from "diagnosed" to "recovered."]

**Verdict:** Not drawn. The five-vertex scenario and its weights are not in the chapter.

## Placeholder 4.2 (manuscript/part_ii/ch04_clinical_manifold.md)

[Figure 4.2: The nine clinical-moral dimensions with their interactions. A $9 \times 9$ matrix showing the major covariance terms $\Sigma_{ij}$. Heavy lines connect dimensions with strong positive covariance (e.g., $\Sigma_{49}$: autonomy requires understanding). Dashed lines connect dimensions with potential negative covariance (e.g., $\Sigma_{18}$: institutional protocols may constrain optimal outcomes in individual cases).]

**Verdict:** Unsupported. The covariance matrix is not estimated; the 'strong' and 'negative' terms and Sigma_18 appear only in the placeholder.

## Placeholder 4.3 (manuscript/part_ii/ch04_clinical_manifold.md)

[Figure 4.3: The intubation decision on the clinical decision complex. Two edges from the current state: intubation (improving $d_1$, $d_8$ but worsening $d_3$, $d_4$, $d_5$, $d_6$, $d_7$, $d_9$ and crossing $\beta_{\text{consent}}$) and supportive care (slightly worsening $d_1$, $d_8$ but preserving all other dimensions). Edge weights shown. The clinical geodesic selects supportive care despite its lower $d_1$ value.]

**Verdict:** Drawn as Figure 4.2. 'Preserving all other dimensions' understates it: supportive care raises four.

## Placeholder 5.1 (manuscript/part_ii/ch05_qaly_irrecoverability.md)

[Figure 5.1: The QALY Irrecoverability Theorem visualized. The nine-dimensional clinical-moral state space is projected onto the one-dimensional QALY axis. The level set $Q^{-1}(c)$ is an 8-dimensional submanifold (shown as a plane for $d = 3$). Distinct clinical-moral states A and B, with radically different profiles on $d_5$--$d_9$, map to the same QALY value. The information distinguishing them is irrecoverable.]

**Verdict:** Drawn as Figure 5.1, in two dimensions.

## Placeholder 6.1 (manuscript/part_ii/ch06_clinical_astar.md)

[Figure 6.1: The clinical geodesic vs. the QALY-optimal path for the Jehovah's Witness case. The QALY path (dashed) heads directly toward high $d_1$ via forced transfusion but hits the consent boundary ($\beta_{\text{consent}} = \infty$). The geodesic (solid) respects the boundary and routes through alternative treatments (erythropoietin, cell salvage), reaching a lower $d_1$ endpoint but with finite total cost. The QALY path has infinite cost on the manifold; the geodesic has the minimum finite cost.]

**Verdict:** Drawn as Figure 6.1. Erythropoietin and cell salvage are in Chapter 9, not Chapter 6, and are left out.

## Placeholder 7.1 (manuscript/part_ii/ch07_heuristic_spectrum.md)

[Figure 7.1: The four-category heuristic hierarchy. Strictly admissible: $h_C \ll h^*$ (prohibitions, always safe). $\varepsilon$-admissible: $h_C \leq (1+\varepsilon) h^*$ (well-trained clinicians, near-optimal). Inadmissible: $h_C > h^*$ for some $n$ (damaged clinicians, avoidance patterns). Gauge-variant: $h_C(\tau(n)) \neq h_C(n)$ (biased clinicians, inconsistent care).]

**Verdict:** Not drawn. It depends on Definitions 7.1 to 7.3, which overlap (Unresolved item 5).

## Placeholder 8.1 (manuscript/part_ii/ch08_consent_gauge.md)

[Figure 8.1: The three modes of alignment failure. (a) Epistemic misalignment: the patient's $d_1$ attribute vectors do not match the clinician's. (b) Value misalignment: the patient's boundary penalties do not match the clinician's. (c) Goal misalignment: the patient's goal region $G_{\text{patient}}$ does not overlap with the clinician's goal region $G_{\text{clin}}$. Each failure has a different clinical presentation and a different intervention.]

**Verdict:** Drawn as Figure 8.1. Panel (c) said the goal regions do not overlap; Section 8.4.1 says the goals are not contradictory, so the drawing shows an overlap.

## Placeholder 9.1 (manuscript/part_iii/ch09_clinical_cases.md)

[Figure 9.1: Nine-dimensional radar chart showing attribute vectors for Path A (transfuse against refusal) and Path B (respect refusal, optimize alternatives)]

**Verdict:** Drawn as Figure 9.1, as bars; a radar chart cannot carry minus infinity.

## Placeholder 9.2 (manuscript/part_iii/ch09_clinical_cases.md)

[Figure 9.2: Trajectory diagram showing Dr. Stein's attribute vector before and after DBS, with the pre-modification consent path and the post-modification experienced path]

**Verdict:** Drawn as Figure 9.2, before and after per dimension. The consent path against experienced path has no data.

## Placeholder 9.3 (manuscript/part_iii/ch09_clinical_cases.md)

[Figure 9.3: Composite visualization showing the five cases as five trajectories on the clinical decision complex, each highlighting a different structural feature: the sacred boundary in Case 1, the process path in Case 2, the constrained reachable set in Case 3, the proxy divergence in Case 4, and the temporal identity split in Case 5]

**Verdict:** Not drawn. Five trajectories with no coordinates would be invented geometry.

## Placeholder 10.1 (manuscript/part_iv/ch10_pandemic_triage.md)

[Figure 10.1: Schematic showing $n = 30$ patients on the clinical manifold, with individually optimal geodesics (dashed) and resource-constrained feasible paths (solid), highlighting the deviation between individual geodesics and constrained allocations]

**Verdict:** Drawn as Figure 10.1, as ranked positions; geodesics for 30 patients are not given.

## Placeholder 10.2 (manuscript/part_iv/ch10_pandemic_triage.md)

[Figure 10.2: Dimensional activation map of COVID-19 triage decisions, showing which of the nine clinical-moral dimensions were activated by different triage scenarios, with predicted and observed moral injury correlation]

**Verdict:** Wrong. It asks for an observed moral injury correlation; there is none in the repository.

## Placeholder 10.3 (manuscript/part_iv/ch10_pandemic_triage.md)

[Figure 10.3: Historical evolution of triage dimensionality, from Larrey (1D) through ESI (2D) and pandemic ethics (2D) to the manifold-optimal framework (9D)]

**Verdict:** Drawn as Figure 10.2. 'Evolution' is misleading: the counts in Section 10.8 run 1, 2, 1, 2.

## Placeholder 11.1 (manuscript/part_iv/ch11_allocation.md)

[Figure 11.1: The equity-efficiency frontier for vaccine allocation, showing utilitarian, egalitarian, and manifold-optimal allocations, with specific COVID-19 prioritization schemes plotted on the frontier]

**Verdict:** Wrong. It asks for COVID-19 prioritization schemes plotted on the frontier; the chapter has no such data. Replaced by drawn Figure 11.1, the Gini term.

## Placeholder 13.1 (manuscript/part_v/ch13_moral_injury_theory.md)

[Figure 13.1: Phase diagram showing the two damage modes as perturbations of the pre-injury heuristic. The horizontal axis is boundary penalty $\beta_k$; the vertical axis is clinical decision quality. The optimal operating point (pre-injury $\varepsilon$-admissible heuristic) is at the peak. Hypervigilance shifts left (increased $\beta_k$, decreased quality); moral numbing shifts right (decreased $\beta_k$, decreased quality).]

**Verdict:** Wrong: left and right reversed, and its quality curve is given by no formula. Replaced by drawn Figure 13.2.
