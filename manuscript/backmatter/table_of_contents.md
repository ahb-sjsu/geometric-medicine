# Table of Contents

---

## Front Matter

- Title Page
- Series Foreword
- Preface: The Clinician's Dilemma
- Acknowledgments

---

## Part I: The Problem

**Chapter 1. The QALY Trap**
*Why clinical medicine evaluates patients by scalar metrics --- QALYs, APACHE scores, Glasgow Coma Scale, Charlson indices --- and what this destroys. Two patients with identical QALYs whose optimal treatments are radically different. The Scalar Irrecoverability Theorem predicts exactly what the QALY discards: eight of nine dimensions of clinically relevant information.*

**Chapter 2. Triage as Forced Contraction**
*Emergency triage is the medical analogue of moral contraction. The full clinical tensor must be compressed to a binary decision or ordinal ranking under time pressure. From Napoleonic origins through modern ESI to pandemic crisis standards of care, each triage system is a specific contraction of the clinical tensor, and each discards different dimensions.*

**Chapter 3. A Brief History of Medical Ethics, Geometrically**
*The geometric framework's precursors across twenty-five centuries: the Hippocratic Oath as a boundary condition, Beauchamp and Childress's four principles as four of nine manifold dimensions, Jonsen and Toulmin's casuistry as case-based reasoning without a similarity metric, Charon's narrative ethics as the humanistic correction to scalar reduction. Each tradition captures part of the manifold. None captures all nine dimensions simultaneously.*

---

## Part II: The Framework

**Chapter 4. The Clinical Decision Complex**
*The formal construction of the domain-specific manifold: a nine-dimensional weighted simplicial complex. Vertices (clinical states), edges (clinical actions), higher simplices (care bundles). The nine clinical-moral dimensions. The $9 \times 9$ clinical-moral covariance matrix $\Sigma$ and its critical cross-dimensional terms. Clinical-moral boundaries: harm, consent, futility, abandonment, sacred values.*

**Chapter 5. The QALY Irrecoverability Theorem**
*The domain-specific Scalar Irrecoverability Theorem, proved in full. QALY discrimination against elderly, disabled, and minority populations is mathematical, not moral. The precise conditions under which QALY analysis is and is not adequate.*

**Chapter 6. Clinical Reasoning as $A^*$ Pathfinding**
*Clinical decisions as pathfinding on the clinical decision complex. The evaluation function $f(n) = g(n) + h(n)$: evidence-based medicine plus clinical wisdom. The clinical geodesic as the minimum-cost path on the full nine-dimensional manifold. Mapping to clinical practice: start node, goal region, edge cost, boundary penalty, open list, closed list, optimal path, path not found.*

**Chapter 7. Clinical Heuristics and the $\varepsilon$-Admissibility Spectrum**
*What makes clinical judgment good, bad, damaged, or biased. The Clinical Heuristic Admissibility Theorem. The four-category heuristic hierarchy: strictly admissible, $\varepsilon$-admissible, inadmissible, gauge-variant. Clinical training as heuristic calibration. Ethics consultations as heuristic recalibration.*

**Chapter 8. Informed Consent as Gauge Invariance and the Medical BIP**
*Valid consent as a gauge-invariance condition: the patient's decision must be invariant under meaning-preserving reframing. The Consent Paradox in Low Health Literacy. Shared decision-making as manifold alignment: epistemic, value, and goal alignment as three independent failure modes. Algorithmic bias as a BIP violation.*

---

## Part III: Clinical Applications

**Chapter 9. Clinical Geodesics in Practice**
*Five worked examples: (1) the competent patient who refuses treatment, (2) withdrawing life support, (3) psychiatric involuntary treatment, (4) the proxy decision, (5) deep brain stimulation and identity. Nine-dimensional decomposition, clinical geodesic computation, and comparison with principlism and QALY analysis for each case.*

---

## Part IV: The Ethics of Allocation

**Chapter 10. Pandemic Triage as Manifold Allocation**
*Triage as constrained multi-agent pathfinding. The Divergence Theorem: when utilitarian and manifold-optimal triage diverge. Ventilator withdrawal, age-based deprioritization, lottery allocation. Why clinicians resist utilitarian triage. COVID-19 as a natural experiment.*

**Chapter 11. Vaccine Allocation, Organ Transplant, and the Geometry of Scarcity**
*Population-level allocation: vaccine prioritization, organ transplant scoring, public health mandates. Collective geodesics versus Nash equilibrium. Vaccine hesitancy as heuristic miscalibration. The geometric conditions for justified public health mandates.*

**Chapter 12. The Clinical Bond Index and Structural Healthcare Injustice**
*The clinical Bond Index: $\text{BI}(P, S) = \mathbb{E}[\text{CF}(\gamma_P^*) - \text{CF}(\gamma_C^*)]$. Detecting racial disparities, disability discrimination, and age discrimination as numerical quantities. Measuring structural injustice from existing clinical data. The empirical path: instruments, proxies, and operationalizations for all nine dimensions.*

---

## Part V: Moral Injury

**Chapter 13. The Mathematical Theory of Moral Injury**
*Moral injury is not burnout. Burnout is $g(n)$-depletion; moral injury is $h(n)$-damage. The Moral Injury Accumulation Theorem: cumulative, irreversible above threshold, structurally distinct from burnout. Two damage modes: hypervigilance and moral numbing. The Moral Injury Index for prospective policy evaluation.*

**Chapter 14. Moral Injury in the Wild: Pandemic, Palliative, Psychiatric**
*The theory applied to three settings: pandemic ICU (acute boundary crossing, COVID-19 predictions), palliative care (chronic low-level boundary crossing, desensitization versus hypervigilance), psychiatry (autonomy boundary crossing, conflicted heuristics).*

**Chapter 15. Preventing and Repairing Moral Injury**
*Ethics consultations as heuristic recalibration. Institutional design to minimize MI: boundary-crossing distribution, process support, g(n)/h(n) separation. Moral resilience versus moral numbing. The limits of repair: irreversibility above $\text{MI}_{\text{crit}}$.*

---

## Part VI: Horizons

**Chapter 16. AI in Clinical Reasoning**
*Clinical decision support on the full manifold. Algorithmic bias as BIP violation. AI and moral injury: automation relocates but does not eliminate boundary crossing. The No Escape Theorem for medical AI.*

**Chapter 17. Measuring the Clinical Metric**
*The empirical challenge: estimating $\Sigma$ from clinical data. Proposed experimental designs. The six falsifiable predictions with specific instruments, sample sizes, and falsification criteria. Measuring the Bond Index from EHR data and existing survey instruments.*

**Chapter 18. Open Questions**
*The frontier, honestly stated. Can we measure the clinical metric from routine data? What is the conservation law for clinical reasoning? Is the clinical manifold Riemannian? How does the No Escape Theorem constrain medical AI? Can the Moral Injury Index be validated prospectively? What is the right dimensionality? Cross-cultural variation in the metric tensor.*

---

## Appendices

**Appendix A. Mathematical Prerequisites**
*Smooth manifolds, Riemannian metrics, geodesics, the Mahalanobis distance, simplicial complexes, $A^*$ search, boundary penalties, gauge invariance, the Scalar Irrecoverability Theorem. Self-contained, with references to Geometric Methods (Bond, 2026a) and Geometric Reasoning (Bond, 2026b) for proofs.*

**Appendix B. The Clinical Decision Complex: Code Walkthrough**
*Python implementation of the clinical decision complex, $A^*$ pathfinding, moral injury accumulation, Bond Index calculation, and triage divergence analysis. Based on ch21\_clinical.py and ch27\_bioethics.py. Reproducibility guide.*

**Appendix C. Clinical Vignettes for Classroom and Discussion Use**
*Five vignettes: competent refusal, process geodesic, consent and framing, pandemic triage and moral injury, AI triage and algorithmic injustice. Nine-dimensional decompositions, clinical geodesic analyses, and discussion questions for each. Notes for instructors.*

**Appendix D. Notation and Conventions**
*Consistent with the Geometric Series. $\mathcal{C}$ for clinical decision complex, $\Sigma$ for covariance matrix, $\beta_k$ for boundary penalties, $\text{MI}$ for moral injury, $\text{BI}$ for Bond Index, $\text{CF}$ for clinical friction, $d_1$--$d_9$ for the nine clinical-moral dimensions.*

---

## Backmatter

- Bibliography
- Index
- About the Author
- The Geometric Series
