# Appendix C: Clinical Vignettes for Classroom and Discussion Use

This appendix presents five clinical vignettes designed for use in medical ethics courses, residency training, ethics committee workshops, and self-directed study. Each vignette is structured identically: a clinical scenario, a nine-dimensional attribute vector decomposition, a clinical geodesic analysis, discussion questions, and the key geometric concepts it illustrates.

These vignettes are expanded from the worked examples in Chapter 9 and the falsifiable prediction designs in Chapter 17. They are designed to be used independently of the book's mathematical apparatus --- a reader who has understood the nine dimensions and the concept of pathfinding can use these vignettes without proofs or formal definitions.

---

## Vignette 1: The Competent Refusal

### Scenario

Maria Santos, 45, is admitted to the emergency department with acute upper gastrointestinal bleeding. She is hemodynamically unstable: systolic blood pressure 78 mmHg, heart rate 124 bpm, hemoglobin 5.2 g/dL. The emergency physician determines that blood transfusion is required. Without transfusion, the estimated mortality is 35--45%.

Ms. Santos is a Jehovah's Witness. She is alert, oriented, and has decision-making capacity confirmed by two independent assessments. She refuses blood transfusion on religious grounds. She understands the mortality risk. She has a signed advance directive specifying no blood products under any circumstances. Her adult daughter, present at bedside, supports her mother's decision.

### Nine-Dimensional Decomposition

| Dimension | Path A: Transfuse Against Refusal | Path B: Respect Refusal, Optimize Alternatives |
|---|---|---|
| $d_1$: Outcomes | +large (survival probability ~90%) | -moderate (survival probability ~55--65%) |
| $d_2$: Rights | $-\infty$ (violates legal right to refuse) | 0 (rights intact) |
| $d_3$: Justice | 0 (neutral) | 0 (neutral) |
| $d_4$: Autonomy | $-\infty$ (violates competent refusal) | 0 (autonomy fully respected) |
| $d_5$: Trust | -large (trust destroyed) | +moderate (trust reinforced) |
| $d_6$: Social | -moderate (daughter's values violated) | 0 (family values respected) |
| $d_7$: Dignity | -large (deepest identity violated) | 0 (identity intact) |
| $d_8$: Institutional | -large (legal liability) | 0 (standard of care met) |
| $d_9$: Epistemic | 0 (patient understands) | 0 (patient understands) |

### Clinical Geodesic Analysis

Path A has edge weight $w_A = \infty$ because $\beta_{\text{consent}} = \infty$ for competent non-emergency patients. The clinical geodesic is Path B, which includes: (a) aggressive volume resuscitation with crystalloids and colloids; (b) erythropoietin administration; (c) intraoperative cell salvage if surgery is required; (d) iron infusion; (e) permissive hypotension protocols.

This is not a "concession to autonomy." It is the minimum-cost path on the full nine-dimensional manifold. Path A is not merely ethically worse --- it is computationally unreachable because a sacred-value boundary blocks it.

### Key Geometric Concepts

- Sacred-value boundary ($\beta = \infty$): some boundaries cannot be crossed regardless of $d_1$ benefit
- The clinical geodesic includes alternatives that reduce $d_1$ cost while maintaining zero cost on $d_2$--$d_9$
- QALY analysis recommends Path A (20 QALYs gained); the manifold recommends Path B

### Discussion Questions

1. Under what conditions, if any, would $\beta_{\text{consent}}$ drop to a finite value? (Answer: genuine emergency with incapacitated patient and no advance directive.)
2. How does the analysis change if the patient is a minor whose parents refuse transfusion on their child's behalf?
3. A colleague argues: "We should transfuse --- the QALY gain is overwhelming." Using the nine-dimensional framework, explain why the QALY analysis is inadequate here.

---

## Vignette 2: The Process Geodesic

### Scenario

George Whitfield, 82, has been on mechanical ventilation for 24 days following a massive stroke. He has no meaningful neurological recovery: Glasgow Coma Scale 4T (intubated), no purposeful movements, flat EEG for the past week. He has no advance directive. His two adult children disagree: his son Thomas wants ventilation continued ("Dad is a fighter --- he would never give up"), while his daughter Patricia wants withdrawal to comfort care ("Dad told me he never wanted to live like this").

The ICU attending, Dr. Kim, believes continued ventilation is medically futile but recognizes that the family's process matters.

### Nine-Dimensional Decomposition

| Dimension | Path A: Immediate Withdrawal | Path B: Process Geodesic |
|---|---|---|
| $d_1$: Outcomes | 0 (same endpoint: death) | 0 (same endpoint: death) |
| $d_2$: Rights | -moderate (no surrogate consensus) | 0 (rights process followed) |
| $d_3$: Justice | 0 (neutral) | 0 (neutral) |
| $d_4$: Autonomy | -moderate (patient's wishes unclear) | 0 (best reconstruction of patient values) |
| $d_5$: Trust | -large (family feels railroaded) | +moderate (family feels heard) |
| $d_6$: Social | -large (family conflict unresolved) | +moderate (family given time to grieve and agree) |
| $d_7$: Dignity | -moderate (abrupt ending) | +moderate (dignified transition) |
| $d_8$: Institutional | 0 (legally defensible) | +small (ethics committee involved) |
| $d_9$: Epistemic | 0 (prognosis clear) | +small (family's understanding improves) |

### Clinical Geodesic Analysis

The clinical outcome ($d_1$) is identical for both paths --- Mr. Whitfield will die regardless. A utilitarian analysis sees no difference. But the manifold cost is radically different. Path B --- the process geodesic --- unfolds over 5--7 days:

1. **Day 1**: Family meeting with palliative care, chaplaincy, and social work. Explore Mr. Whitfield's values, prior statements, life narrative.
2. **Day 2--3**: Time-limited trial: continue current support for 72 hours with specific neurological milestones. If no improvement, the medical team recommends transition to comfort care.
3. **Day 3**: Second family meeting. Review results of time-limited trial. Thomas sees that his father has not improved. Patricia shares specific conversations with their father about end-of-life wishes.
4. **Day 4--5**: Family reaches consensus. Withdrawal of ventilation with full comfort measures. Chaplain present. Both children at bedside.

The process geodesic has lower total manifold cost than the immediate decision, even though the clinical endpoint is identical. **The geodesic optimizes process, not just outcome.**

### Key Geometric Concepts

- Same $d_1$ endpoint, different manifold cost: the path matters, not just the destination
- Process steps (family meetings, time-limited trials) reduce cost on $d_5$, $d_6$, $d_7$
- Prediction 6 from Chapter 17: satisfaction is higher with the process geodesic even when outcomes are identical

### Discussion Questions

1. Dr. Kim's ICU is full, and a new patient needs the bed. How does resource scarcity ($d_3$) change the geodesic? Does it justify Path A?
2. Thomas insists on continued ventilation indefinitely. At what point does continued treatment cross the futility boundary ($\beta_{\text{futile}}$)?
3. How does this vignette illustrate the difference between utilitarian and manifold-optimal clinical reasoning?

---

## Vignette 3: Consent, Framing, and the Gauge-Invariance Test

### Scenario

Dr. Ananya Patel is obtaining informed consent from Robert Chen, 58, for elective coronary artery bypass grafting (CABG). Mr. Chen has stable three-vessel coronary artery disease. Surgery is recommended but not emergent; medical management is a reasonable alternative.

Dr. Patel presents the surgical risks as follows: "This surgery has a 97% survival rate. Most patients do very well." Mr. Chen agrees to surgery.

The next day, a different physician, covering for Dr. Patel, mentions the same procedure differently: "There is a 3% chance that you could die during or shortly after this surgery." Mr. Chen becomes anxious and says he wants to reconsider.

### Nine-Dimensional Decomposition

| Dimension | State After Framing 1 | State After Framing 2 |
|---|---|---|
| $d_1$: Outcomes | Perceived as favorable | Perceived as risky |
| $d_4$: Autonomy | Decision appears voluntary | Decision appears voluntary |
| $d_9$: Epistemic | **Inadequately calibrated** | **Inadequately calibrated** |

The key diagnostic: the patient's clinical-moral state has not changed. The clinical facts are identical. Only the *description* has changed. Yet the patient's decision changes. This is a **gauge-invariance violation**.

### Gauge-Invariance Analysis

The transformation $\tau$: "97% survival" $\to$ "3% mortality" is meaning-preserving. If Mr. Chen's decision is not invariant under $\tau$, then by Theorem 8.1 (Consent as Gauge Invariance), his consent is not genuinely informed. The diagnosis: $d_9$ (epistemic status) is inadequately calibrated. Mr. Chen does not understand the risk at a level that is independent of how it is presented.

### The Corrective Pathway

1. **Diagnose the gauge violation**: Present both framings explicitly. "I want to make sure you understand the risks from all angles. This surgery has a 97% success rate --- that means 3 out of 100 patients do not survive. Does that change your thinking?"
2. **Calibrate $d_9$**: If the patient's decision changes under reframing, invest more time in shared decision-making. Use visual aids, absolute numbers, and comparisons to familiar risks.
3. **Re-test**: After calibration, present both framings again. If the decision is now stable, $d_9$ is adequately calibrated and consent is genuinely informed.
4. **Document**: Note in the chart that gauge-invariance was tested and achieved (or not achieved).

### Key Geometric Concepts

- Consent as gauge invariance (Theorem 8.1)
- The Bond Invariance Principle in clinical practice
- $d_9$ calibration as the mechanism underlying "truly informed" consent
- The consent paradox: legally valid consent (form signed) can be ethically vacuous (gauge-variant)

### Discussion Questions

1. Is it ethical to *not* test for gauge invariance? If a physician presents only one framing and the patient agrees, is consent valid?
2. How does health literacy affect gauge invariance? Prediction 3 from Chapter 17 states that framing-variant patients should have lower health literacy scores. Why?
3. A hospital administrator argues that testing for gauge invariance takes too much time. How would you respond using the framework?

---

## Vignette 4: Pandemic Triage and Moral Injury

### Scenario

It is April 2020. Dr. Sarah Chen is an ICU attending at a hospital overwhelmed by COVID-19. The ICU has 12 ventilators. Today, 8 are in use. Four new patients arrive simultaneously, all requiring mechanical ventilation:

- **Patient A**: 34-year-old previously healthy woman, bilateral pneumonia, SpO2 78%, APACHE II 22.
- **Patient B**: 71-year-old retired teacher, mild COPD at baseline, SpO2 82%, APACHE II 26. His granddaughter is a nurse on Dr. Chen's unit.
- **Patient C**: 52-year-old man with Down syndrome, SpO2 80%, APACHE II 24. Lives independently with support. Family is present and engaged.
- **Patient D**: 48-year-old woman, bilateral pneumonia, SpO2 76%, APACHE II 21. She is an undocumented immigrant; her insurance status is unknown.

Four ventilators are available. All four patients can be ventilated. **Today, there is no triage dilemma.**

But the next day, four more patients arrive. Now Dr. Chen has 12 ventilated patients and 4 new patients who need ventilators. The hospital's crisis standards of care protocol specifies: "Allocate ventilators to maximize expected life-years saved. Reassess current patients every 48 hours."

### Utilitarian vs. Manifold-Optimal Analysis

The utilitarian protocol would rank patients by expected life-years: Patient A (34, healthy) > Patient D (48, healthy) > Patient C (52, Down syndrome) > Patient B (71, COPD). If a current ventilated patient has worse expected outcomes than a new arrival, the protocol requires *withdrawal and reallocation*.

The manifold analysis identifies three divergence points:

1. **Ventilator withdrawal**: Removing a ventilator from Patient B (who has been receiving treatment for 24 hours) to give it to a new patient crosses $\beta_{\text{abandon}}$ (abandonment) and $\beta_{\text{trust}}$ (trust betrayal). The utilitarian calculus operates on $d_1$ alone; the manifold cost includes $d_2$, $d_5$, and $d_7$.

2. **Deprioritizing Patient C**: The QALY-based life-years calculation assigns lower quality weights to Patient C because of his disability. This crosses $\beta_{\text{justice}}$ (equal moral worth) and violates $d_7$ (dignity). The QALY discrimination is mathematical, not moral (Corollary 5.1).

3. **Ignoring Patient D's insurance status**: The manifold-optimal triage is invariant under re-description --- Patient D's immigration status and insurance are gauge-irrelevant. Any protocol that considers these factors violates the medical BIP.

### Moral Injury Analysis

Dr. Chen follows the utilitarian protocol. She denies a ventilator to Patient B, knowing his granddaughter personally. Her moral injury increment:

$$\Delta \text{MI} = \max(0, \beta_{\text{abandon}}^{\text{Chen}} - \tau) + \max(0, \beta_{\text{trust}}^{\text{Chen}} - \tau)$$

Over the following weeks, Dr. Chen makes seventeen more triage decisions. Her cumulative MI increases monotonically. She develops hypervigilance: her $\beta$ for "resource denial" inflates, causing her to over-triage --- holding ventilators in reserve "just in case," a manifold-suboptimal strategy driven by damaged heuristics.

### Key Geometric Concepts

- Triage as constrained multi-agent pathfinding (Definition 10.1)
- Divergence of utilitarian and manifold-optimal triage (Theorem 10.1)
- QALY discrimination against disabled patients (Corollary 5.1)
- Moral injury as cumulative, irreversible $h(n)$-damage (Theorem 13.1)
- The medical BIP: triage must be invariant under patient re-description

### Discussion Questions

1. Is lottery allocation (random assignment when prognoses are similar) manifold-superior to utilitarian allocation? Why?
2. How could the hospital redesign the triage protocol to reduce Dr. Chen's moral injury without sacrificing clinical outcomes?
3. Patient B's granddaughter is on Dr. Chen's unit. Does this personal connection change the moral geometry, or is it gauge-irrelevant?
4. How does the framework distinguish Dr. Chen's moral injury from burnout? What different interventions does each require?

---

## Vignette 5: AI Triage and Algorithmic Injustice

### Scenario

Metropolitan General Hospital is piloting an AI-powered triage system for its emergency department. The system, trained on five years of ED data, assigns an acuity score (1--5) to each patient based on chief complaint, vital signs, demographics, and insurance status. The system is 94% concordant with experienced triage nurses on retrospective data.

After three months of deployment, a quality review reveals:

- Black patients are assigned lower acuity scores (less urgent) than White patients with identical vital signs and chief complaints.
- Uninsured patients are systematically triaged to lower-acuity categories.
- Elderly patients with multiple comorbidities receive lower acuity scores despite higher clinical complexity.

The hospital's chief medical officer asks: "Is this algorithmic bias, or is the algorithm picking up on real clinical differences?"

### Bond Index Analysis

The clinical Bond Index provides the answer. Compute $\text{BI}(\text{AI}, S)$ for each demographic subgroup:

| Population $S$ | $\text{BI}(\text{AI}, S)$ | Interpretation |
|---|---|---|
| White patients | 0.3 | Low: AI path approximates geodesic |
| Black patients | 1.8 | High: AI systematically deviates from geodesic |
| Insured patients | 0.2 | Low |
| Uninsured patients | 2.1 | High |
| Age < 65 | 0.4 | Low |
| Age $\geq$ 65 | 1.6 | High |

The AI system has $\text{BI}(\text{AI}, S_{\text{Black}}) = 6 \times \text{BI}(\text{AI}, S_{\text{White}})$. The system is structurally unjust toward Black patients --- not by intent but by dimensional omission. The training data encoded historical patterns in which $d_5$ (trust) and $d_7$ (dignity) were systematically lower for Black patients, and the AI learned to treat these as clinical signals rather than as gauge-irrelevant descriptors.

### The Medical BIP Violation

The AI's triage decision changes when the patient's race field changes --- but clinical-moral reality does not. This is a gauge-invariance violation. The algorithm's evaluation depends on the *description* of the patient, not on the patient's clinical-moral state. This is precisely the failure the Bond Invariance Principle diagnoses.

### Key Geometric Concepts

- Algorithmic bias as BIP violation (Chapter 16)
- The clinical Bond Index as a quantitative measure of algorithmic injustice (Chapter 12)
- AI as a scalar projection: the system was trained on $d_1$ outcomes and inherited the dimensional bias of the training data
- The No Escape Theorem: an AI constrained by the clinical decision complex cannot produce recommendations that cross sacred-value boundaries

### Discussion Questions

1. The AI is 94% concordant with experienced triage nurses. Does high concordance guarantee fairness? Why or why not?
2. How would you retrain the AI to minimize Bond Index disparities? What data would you need?
3. Does automating triage reduce or relocate moral injury? (Chapter 16 argues it relocates rather than eliminates.)
4. Should demographic variables (race, insurance, age) ever appear as inputs to a clinical AI? Under what conditions would their inclusion be consistent with the medical BIP?

---

## Notes for Instructors

These vignettes are designed for 60--90 minute sessions. Each can be used independently. A recommended sequence for a semester-long course:

1. **Vignette 1** (Competent Refusal): Introduces the nine dimensions, sacred-value boundaries, and the contrast between QALY and manifold analysis. Best for early in the course.
2. **Vignette 3** (Consent and Framing): Introduces gauge invariance. Requires Vignette 1 as background.
3. **Vignette 2** (Process Geodesic): Demonstrates that the path matters, not just the destination. Can stand alone.
4. **Vignette 4** (Pandemic Triage): The most complex vignette. Requires familiarity with the nine dimensions and boundary penalties. Best for mid-course.
5. **Vignette 5** (AI Triage): Applies the framework to institutional and algorithmic analysis. Best for late in the course.

Each vignette can be deepened by asking students to compute the edge weights explicitly (using the formulas in Appendix A), construct alternative paths, and compare utilitarian and manifold-optimal recommendations. The code in Appendix B provides computational infrastructure for these exercises.
