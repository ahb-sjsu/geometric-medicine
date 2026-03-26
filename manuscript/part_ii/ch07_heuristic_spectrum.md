# Chapter 7: Clinical Heuristics and the $\varepsilon$-Admissibility Spectrum

*Part II: The Framework*

---

> *"The good clinician is not the one who knows the most. The good clinician is the one whose intuitions are best calibrated to the moral landscape of the decision."*
> --- Adapted from the GCE paper

> **THE SPECTRUM**
>
> *If clinical reasoning is A* search, the quality of clinical judgment reduces to the quality of the heuristic function $h(n)$. A good heuristic leads the search to the optimal path. A bad heuristic leads it astray. A damaged heuristic --- one warped by moral injury, cognitive bias, or institutional pressure --- can make a competent clinician systematically avoid beneficial treatments or systematically cross boundaries that should not be crossed. This chapter characterizes the full spectrum of heuristic quality, from the strictly admissible prohibitions that should never be overridden, through the $\varepsilon$-admissible intuitions of well-trained clinicians, to the inadmissible heuristics of the morally injured and the gauge-variant heuristics of the cognitively biased.*

---

## 7.1 Admissibility: The Central Concept

In A* search, a heuristic $h(n)$ is *admissible* if it never overestimates the true remaining cost:

$$h(n) \leq h^*(n) \quad \text{for all } n$$

where $h^*(n)$ is the true optimal cost from $n$ to the nearest goal in $G$. When the heuristic is admissible, A* is guaranteed to find the optimal path --- the clinical geodesic. When the heuristic is inadmissible (it overestimates the cost somewhere), A* may miss the optimal path by avoiding regions of the search space that the heuristic incorrectly labels as expensive.

The clinical instantiation is immediate:

**Theorem 7.1 (Clinical Heuristic Admissibility).** *Let $h_C(n)$ be a clinical moral heuristic --- a function that assigns high cost to actions violating professional ethical norms and low cost to actions consistent with them:*

$$h_C(n) = \sum_k \beta_k \cdot P(\text{remaining path from } n \text{ crosses boundary } k)$$

*If the boundary penalties $\beta_k$ are calibrated by clinical training and professional socialization to be lower bounds on the true moral cost of boundary crossing (i.e., $\beta_k \leq \beta_k^*$, where $\beta_k^*$ includes the full cost: malpractice liability, professional censure, patient harm, institutional trust damage, and psychological distress to the clinician), then $h_C$ is admissible and A* search finds the optimal clinical path.*

**Proof.** The clinical heuristic $h_C(n) = \sum_k \beta_k \cdot P_k(n)$ estimates the remaining cost as the expected boundary penalty cost. Each $\beta_k \leq \beta_k^*$ by assumption, and the remaining Mahalanobis distance cost (which $h_C$ ignores) is non-negative. Therefore $h_C(n) \leq h^*(n)$, satisfying the admissibility condition. By the correctness of A* with admissible heuristics (Hart, Nilsson, & Raphael, 1968), the search finds the minimum-cost path. $\square$

The theorem's clinical content is this: if medical training calibrates moral intuitions as *lower bounds* on the true cost of ethical violations --- if the clinician learns to feel at least as much discomfort from boundary crossings as the full institutional, legal, relational, and psychological cost would justify --- then the clinician's pathfinding will find the optimal clinical path. The heuristic will guide the search toward the geodesic, not away from it.

The question is: what happens when the calibration fails?

## 7.2 The Four-Category Hierarchy

Clinical heuristics form a hierarchy of four categories, ordered by their relationship to admissibility. Each category has a distinctive clinical signature and a distinctive failure mode.

### 7.2.1 Category I: Strictly Admissible

**Definition 7.1 (Strictly Admissible Heuristic).** *A heuristic is strictly admissible when $h_C(n) \ll h^*(n)$ for all relevant $n$ --- the estimate dramatically underestimates the true cost. This occurs when the true cost of boundary crossing is so catastrophic that any finite estimate is a lower bound.*

**Clinical examples:**
- Non-consensual treatment of a competent patient: $\beta_{\text{consent}} = 100$, but $\beta_{\text{consent}}^* \approx \infty$ (career-ending malpractice, criminal charges, permanent trust destruction, institutional legitimacy crisis). Any finite $\beta$ is admissible.
- Non-therapeutic experimentation on patients: $\beta_{\text{sacred}} = $ any finite value, $\beta_{\text{sacred}}^* = \infty$. The heuristic is admissible regardless of calibration.
- Deliberate non-palliative killing: same structure.

Strictly admissible heuristics have a distinctive clinical property: they are *prohibitions*. The boundary penalty is so high that no clinical scenario produces a geodesic that crosses the boundary. These are the absolute constraints of clinical ethics --- the sacred-value boundaries that no cost-benefit analysis can override. The heuristic underestimates the cost; A* explores the paths on the other side of the boundary; and it always concludes that those paths are more expensive than going around.

The clinical virtue of strict admissibility is certainty: the clinician never needs to compute whether to cross these boundaries, because the heuristic correctly identifies them as prohibitions. The clinical vice is that strict admissibility depends on correct identification of which boundaries are sacred. A clinician who treats a non-sacred boundary as sacred ($\beta_{\text{futile}} = \infty$ when it should be finite, for example) will refuse to withdraw futile treatment even when withdrawal is the geodesic.

### 7.2.2 Category II: $\varepsilon$-Admissible

**Definition 7.2 ($\varepsilon$-Admissible Heuristic).** *A heuristic is $\varepsilon$-admissible when $h_C(n) \leq (1 + \varepsilon) \cdot h^*(n)$ for all relevant $n$ and some small $\varepsilon > 0$. The heuristic may slightly overestimate the true cost but stays within a bounded error. An $\varepsilon$-admissible heuristic produces paths that cost at most $(1 + \varepsilon)$ times the optimal path cost.*

This is the normal operating range of well-trained clinicians. Their boundary penalties are approximately correct --- close enough that the resulting clinical path is near-optimal, not exactly optimal but within a small multiplicative factor of the geodesic.

**Clinical signature:** The $\varepsilon$-admissible clinician makes good decisions most of the time, with occasional minor suboptimalities that are clinically insignificant. They might slightly over-weight the risk of a procedure ($\beta_{\text{harm}}$ slightly too high) or slightly under-weight the cost of delay ($\beta_{\text{delay}}$ slightly too low), but the resulting paths are close to optimal.

**The $\varepsilon$ of clinical training:** Medical education is a process of reducing $\varepsilon$ --- of calibrating the heuristic toward admissibility. A first-year resident has a large $\varepsilon$ (many boundary penalties are miscalibrated by a large factor). A fifth-year attending has a small $\varepsilon$ (most boundary penalties are approximately correct). The $\varepsilon$ decreases with experience because each clinical encounter provides feedback: the clinician predicts $h(n)$, observes the actual remaining cost $h^*(n)$, and adjusts the heuristic by the discrepancy.

**Proposition 7.1 (Clinical Training as $\varepsilon$-Reduction).** *The goal of clinical training is to reduce the heuristic error $\varepsilon$ from the large values typical of untrained clinicians to the small values typical of experienced practitioners. This is accomplished through:*

1. *Supervised pathfinding: the trainee makes decisions under attending supervision, receiving feedback on boundary penalty calibration.*
2. *Case-based learning: analysis of paradigm cases calibrates the boundary penalties for standard clinical scenarios.*
3. *Simulation: standardized patient encounters allow heuristic calibration without real-world consequences.*
4. *M&M conferences: retrospective analysis of cases where the clinical path deviated from the geodesic (complications, errors, near-misses) identifies systematic heuristic miscalibrations.*

### 7.2.3 Category III: Inadmissible

**Definition 7.3 (Inadmissible Heuristic).** *A heuristic is inadmissible when $h_C(n) > h^*(n)$ for some relevant $n$ --- the estimate overestimates the true cost, causing A* to avoid paths that are actually optimal.*

Inadmissible heuristics produce clinicians who avoid beneficial interventions because they overestimate the moral cost. The overestimation is not random; it is systematic, produced by specific damage mechanisms.

**Damage mechanism 1: Moral injury (hypervigilance).** A clinician who has been forced to cross a boundary involuntarily --- who has denied a ventilator, withdrawn life support against their judgment, performed a procedure they considered futile --- may develop an inflated $\beta$ for that boundary type. The inflation is a trauma response: the boundary crossing was painful, so the heuristic adjusts upward to prevent future crossings. The adjustment is adaptive in the short term (it protects the clinician from repeated moral injury) but maladaptive in the long term (it causes the clinician to avoid beneficial interventions that require crossing the boundary).

**Example:** A clinician who was forced to implement utilitarian triage during the pandemic develops an inflated $\beta_{\text{resource denial}}$. Post-pandemic, this clinician over-triages --- holds ventilators in reserve "just in case," delays discharge to avoid the possibility of readmission, orders unnecessary tests to avoid missing a diagnosis. Each of these behaviors is a detour on the clinical decision complex, adding cost to the clinical path because the heuristic incorrectly labels the direct path as too expensive.

**Damage mechanism 2: Defensive medicine.** The legal environment inflates $\beta_{\text{liability}}$ beyond its true clinical-moral cost. A clinician practicing defensive medicine is not computing $h^*(n)$; they are computing a liability-inflated $h_{\text{legal}}(n)$ that adds the cost of a hypothetical lawsuit to every path that involves diagnostic uncertainty. The result is over-testing, over-treating, and under-communicating: the clinician orders more tests (to reduce $d_9$ uncertainty and thereby reduce $\beta_{\text{liability}}$), prescribes more aggressively (to avoid the "failure to treat" boundary), and avoids difficult conversations (to avoid the "documentation risk" boundary).

**Damage mechanism 3: Personal trauma.** A clinician who has experienced a bad outcome from a specific clinical path may develop an inflated $\beta$ for that path type, unrelated to the true population-level cost. The clinician who lost a patient to a drug reaction may develop an inflated $\beta$ for prescribing that drug, even when the population-level risk is low and the clinical benefit is high.

**Clinical signature:** The inadmissible clinician is recognizable by their avoidance patterns: they consistently decline to do things that other clinicians consider reasonable, they over-test and over-treat in specific clinical scenarios, and they may articulate their avoidance in moral terms ("I could never do that again") that reveal the boundary penalty inflation.

### 7.2.4 Category IV: Gauge-Variant

**Definition 7.4 (Gauge-Variant Heuristic).** *A heuristic is gauge-variant when its value depends on the description of the clinical situation rather than on the clinical situation itself. Formally, if $\tau$ is a meaning-preserving transformation of the clinical information, a gauge-variant heuristic satisfies $h_C(\tau(n)) \neq h_C(n)$.*

This is the only category that deserves the label "cognitive bias." The other categories (inadmissible, $\varepsilon$-admissible, strictly admissible) are systematic over- or under-estimates of the true cost. Gauge-variant heuristics are not systematically wrong in any direction; they are *inconsistent* --- they produce different estimates for the same clinical situation depending on how the situation is described.

**Gauge-variant heuristic 1: Omission bias.** Acting (performing a procedure, prescribing a drug, making a decision) feels more costly than not acting (waiting, observing, deferring), even when not acting causes more harm. The heuristic assigns higher $h(n)$ to paths that involve active intervention than to paths that involve passive observation, regardless of the true costs. A clinician with omission bias will delay a beneficial intervention (because the perceived cost of acting is inflated) while tolerating a harmful status quo (because the perceived cost of not acting is deflated).

Omission bias is gauge-variant because the distinction between "acting" and "not acting" is often a matter of framing, not of clinical reality. A clinician who *continues* a medication is "not acting" (maintaining the status quo), while a clinician who *discontinues* a medication is "acting" (making a change). But the two clinicians are making the same clinical decision --- they are both evaluating whether the medication should be part of the treatment plan. The distinction between continuing and discontinuing is a gauge transformation (a redescription of the same decision), and a gauge-invariant heuristic would assign the same cost to both.

**Gauge-variant heuristic 2: Framing effects.** "90% survival rate" and "10% mortality rate" are meaning-preserving transformations of each other. A gauge-invariant heuristic assigns the same $h(n)$ to both descriptions. A gauge-variant heuristic assigns different $h(n)$ values --- typically, higher cost (more pessimistic assessment) to the mortality frame and lower cost (more optimistic assessment) to the survival frame.

The framing effect in clinical reasoning has been extensively documented. Clinicians recommend more aggressive treatment when outcomes are framed in terms of survival than when they are framed in terms of mortality, even though the information content is identical.[^1] This is a gauge violation: the clinical decision depends on the description, not on the clinical reality.

**Gauge-variant heuristic 3: Anchoring.** The first piece of information received about a patient disproportionately influences the heuristic estimate, regardless of its relevance. A clinician who reads "52-year-old woman with a history of anxiety" before reading "presenting with chest pain and shortness of breath" may anchor on "anxiety" and underestimate the $d_1$ cost of missing a cardiac diagnosis. A clinician who reads "52-year-old woman with a family history of heart disease" before reading "presenting with chest pain and shortness of breath" may anchor on "heart disease" and overestimate the $d_1$ cost of missing a cardiac diagnosis. The information is the same; the order has changed; the heuristic has changed.

**Clinical significance:** Gauge-variant heuristics are the most dangerous category because they produce *inconsistent* clinical paths --- the same patient, described differently, receives different care. This is a Bond Invariance Principle violation (Chapter 8): the clinical evaluation is not invariant under patient re-description. And the inconsistency is invisible to the clinician, because the heuristic adjustment happens automatically, beneath conscious awareness.

[Figure 7.1: The four-category heuristic hierarchy. Strictly admissible: $h_C \ll h^*$ (prohibitions, always safe). $\varepsilon$-admissible: $h_C \leq (1+\varepsilon) h^*$ (well-trained clinicians, near-optimal). Inadmissible: $h_C > h^*$ for some $n$ (damaged clinicians, avoidance patterns). Gauge-variant: $h_C(\tau(n)) \neq h_C(n)$ (biased clinicians, inconsistent care).]

## 7.3 The Anatomy of $\varepsilon$

The error $\varepsilon$ in the $\varepsilon$-admissibility condition is not a single number; it is dimension-specific. A clinician may have excellent calibration on $d_1$ ($\varepsilon_1 \approx 0.05$) and poor calibration on $d_7$ ($\varepsilon_7 \approx 0.5$). The overall $\varepsilon$ is the maximum dimension-specific error:

$$\varepsilon = \max_k \varepsilon_k$$

This decomposition is clinically useful. It identifies where the clinician's heuristic is most miscalibrated and therefore where training or recalibration efforts should be focused.

**Proposition 7.2 (Dimension-Specific $\varepsilon$-Profiles).** *Different clinical specialties have different $\varepsilon$-profiles:*

- *Emergency medicine: Low $\varepsilon_1$ (excellent $d_1$ calibration under acute conditions), high $\varepsilon_7$ (poor $d_7$ calibration due to time pressure that prevents dignity considerations).*
- *Palliative care: Low $\varepsilon_7$ (excellent $d_7$ calibration), moderate $\varepsilon_1$ (outcome calibration is less critical when outcomes are secondary to process).*
- *Surgery: Low $\varepsilon_1$ (excellent outcome calibration), high $\varepsilon_4$ (autonomy calibration may be poor due to the paternalistic tradition of surgical culture).*
- *Psychiatry: Low $\varepsilon_4$ (excellent autonomy calibration, given the constant engagement with consent and capacity issues), high $\varepsilon_8$ (institutional calibration may be poor due to tension between clinical judgment and institutional mandates).*

These profiles are testable predictions. The framework predicts that specialty-specific heuristic miscalibrations will manifest as specialty-specific patterns of clinical decision suboptimality --- and that cross-specialty ethics consultations are effective precisely because they bring complementary $\varepsilon$-profiles to a shared clinical problem.

## 7.4 Clinical Training as Heuristic Calibration

The central thesis of this section is that the primary function of clinical training --- medical school, residency, fellowship, continuing medical education --- is not to teach clinicians to compute $g(n)$ (evidence-based medicine is taught through didactics and self-study) but to calibrate $h(n)$ (clinical wisdom is learned through supervised pathfinding on the clinical decision complex).

### 7.4.1 The Apprenticeship Model, Geometrized

Medical education has retained the apprenticeship model --- learning by supervised practice --- for centuries, long after other professions abandoned it. The geometric framework explains why: the heuristic function $h(n)$ cannot be learned from textbooks. It must be calibrated by experience, under supervision, with feedback.

A textbook can teach the boundary penalties in the abstract: "do not treat without consent." But the clinician's $h(n)$ requires calibration to the specific clinical landscape: How does it feel when the consent boundary is approached? How do you recognize that you are near the boundary? How do you navigate around it? What does it cost to cross it, and how does that cost manifest in the patient's trajectory and in your own psychological state?

These are not questions that can be answered in a lecture. They are questions that are answered by experience --- by standing at the bedside and watching the boundaries approach, by making decisions under supervision and receiving feedback on the calibration, by traversing the manifold enough times that the heuristic becomes automatic, intuitive, and approximately correct.

### 7.4.2 The M&M Conference as Heuristic Audit

The morbidity and mortality (M&M) conference is a centuries-old institution in which clinicians collectively review cases with bad outcomes. The stated purpose is quality improvement; the geometric purpose is heuristic auditing.

An M&M case analysis is a retrospective comparison of the clinical path that was taken ($\gamma_{\text{actual}}$) with the clinical geodesic ($\gamma^*$) that should have been taken. The analysis identifies where the paths diverge and diagnoses the cause of the divergence:

- Was $g(n)$ miscalibrated? (The evidence was misinterpreted, the Bayesian update was wrong, the treatment guidelines were not followed.)
- Was $h(n)$ miscalibrated? (The clinician over- or under-estimated a boundary penalty, the heuristic was gauge-variant, the moral intuition was damaged.)
- Was the goal region misspecified? (The clinician and patient disagreed about acceptable outcomes without realizing the disagreement.)
- Was the complex itself incorrect? (The available edges were not what the clinician thought --- a treatment option was available but not considered, or a treatment option was considered but not actually available.)

Each diagnosis points to a different corrective action: evidence review (for $g(n)$ errors), heuristic recalibration (for $h(n)$ errors), communication improvement (for goal region errors), or system redesign (for complex errors).

## 7.5 Ethics Consultations as Heuristic Recalibration

When a clinician requests an ethics consultation, the geometric interpretation is: "My $h(n)$ is producing a path that I am uncomfortable with, and I need help recalibrating."

The ethics consultant brings three resources to the recalibration:

1. **A different $h(n)$.** The consultant has different experiences, different boundary penalties, and different dimensional weightings. The consultant's $h(n)$ may identify boundaries that the primary clinician has not noticed, or assign different costs to boundaries that the primary clinician has noticed but weighted differently.

2. **An explicit dimensional decomposition.** The primary clinician's $h(n)$ operates automatically, without conscious access to the dimensional weights. The ethics consultant makes the weights explicit: "You're weighing autonomy heavily here, but have you considered the trust implications?" This explicitness allows the clinician to examine their heuristic and adjust it consciously.

3. **Population-level calibration data.** The ethics consultant has seen many similar cases and has calibrated their heuristic across a population. This population-level calibration can correct the primary clinician's case-specific calibration, which may be skewed by the current patient's particular features.

**Proposition 7.3 (Ethics Consultations Reduce $\varepsilon$-Variance).** *The framework predicts that effective ethics consultations should reduce the variance of $\beta_k$ estimates in the clinician population (making heuristics more consistent across clinicians) without reducing the mean (maintaining appropriate boundary sensitivity). Consultations that reduce both variance and mean are not recalibration; they are desensitization --- a form of institutional moral numbing.*

This prediction is testable. Survey clinicians before and after ethics consultations for their $\beta_k$ estimates on the case's relevant boundaries. The prediction is that the post-consultation variance is lower (clinicians converge toward agreement) while the mean is stable (the group's average boundary sensitivity is preserved).

## 7.6 Defensive Medicine as Heuristic Inflation

Defensive medicine --- ordering tests, treatments, or procedures to reduce legal risk rather than to improve clinical care --- is the most common form of institutional heuristic inflation in contemporary medicine.

The geometric analysis is precise. Defensive medicine inflates $\beta_{\text{liability}}$: the boundary penalty for "failing to test" or "failing to treat" is set higher than the true clinical-moral cost of the failure, because the legal cost of a missed diagnosis is added to the moral cost. The inflation is rational from the individual clinician's perspective: the legal system imposes financial and reputational costs that exceed the moral cost of the diagnostic error. But the inflation distorts the clinical geodesic: the path that minimizes legal risk is not the path that minimizes total clinical-moral friction.

**Proposition 7.4 (Defensive Medicine as Geodesic Distortion).** *Let $\gamma_C^*$ be the clinical geodesic computed with true boundary penalties $\beta_k^*$, and let $\gamma_D^*$ be the geodesic computed with liability-inflated boundary penalties $\beta_k^D > \beta_k^*$. Then $\gamma_D^*$ systematically over-tests (higher $d_3$ cost from resource consumption and higher $d_1$ cost from iatrogenic harm of unnecessary procedures), over-treats (higher $d_7$ cost from interventions the patient does not need or want), and under-communicates (higher $d_9$ cost from spending time on documentation rather than patient communication).*

The moral injury implications are significant. When the institution's legal environment inflates $\beta_{\text{liability}}$ beyond the clinician's moral calibration, the clinician is forced to follow a path ($\gamma_D^*$) that their own $h(n)$ identifies as suboptimal. This is a forced boundary crossing of a different kind: not the crossing of a moral boundary but the *avoidance* of the geodesic under institutional pressure. The clinician knows that the extra test is unnecessary, that the additional treatment is not indicated, that the documentation time would be better spent talking to the patient. The institutional geodesic mandates the detour anyway. The resulting moral distress is the heuristic's protest: the clinician's $h(n)$ is correctly calibrated, but the institutional $\beta_{\text{liability}}$ is overriding it.

## 7.7 Sarah's Heuristic Calibration

Sarah's heuristic function at the start of residency was uncalibrated. She had two specific miscalibrations that Dr. Torres identified and corrected:

**Inflated $\beta_{\text{difficult conversation}}$.** Sarah avoided goals-of-care conversations because she overestimated their cost. She imagined that the conversation would be painful ($d_7$: the patient would be distressed), damaging to trust ($d_5$: the patient would lose confidence), and futile ($d_1$: the conversation would not change the clinical outcome). Her $\beta$ for "having the difficult conversation" was approximately 15 --- higher than her $\beta$ for "doing nothing and hoping the situation resolves."

Dr. Torres corrected this by supervised pathfinding. She took Sarah into goals-of-care conversations, showed her how to navigate them, and demonstrated that the conversations typically *improved* $d_5$ (patients trust clinicians who are honest), *improved* $d_7$ (patients feel dignified when their values are heard), and *improved* $d_9$ (patients understand their situation better after the conversation). Sarah's $\beta_{\text{difficult conversation}}$ dropped from 15 to 3 over the course of six months of supervised practice.

**Deflated $\beta_{\text{watchful waiting}}$.** Sarah underestimated the cost of delay. She was comfortable with "let's see how this develops" because it avoided the immediate cost of intervention. Her $\beta$ for "waiting" was approximately 1 --- lower than her $\beta$ for "acting," even when the waiting allowed the patient to deteriorate.

Dr. Torres corrected this by showing Sarah the trajectory costs of delay: the patient whose sepsis was not treated for four hours because "let's see if the fever resolves," the patient whose cancer diagnosis was delayed by three months because "let's repeat the imaging in six months." Sarah's $\beta_{\text{watchful waiting}}$ increased from 1 to 5 over the course of the year, reflecting a more accurate estimate of the cost of delay on $d_1$ and $d_9$.

By the end of her second year, Sarah's $h(n)$ was $\varepsilon$-admissible with $\varepsilon \approx 0.15$ --- still far from the $\varepsilon \approx 0.05$ of an experienced attending, but well within the range of competent clinical reasoning. She could navigate the manifold with reasonable accuracy, recognizing boundaries before she reached them, estimating remaining costs within a factor of 1.15 of the true costs, and seeking help (ethics consultation, attending supervision) when she recognized that her heuristic was uncertain.

Three years later, the pandemic would damage her heuristic. Chapters 13--15 describe what happened to her $h(n)$ when she was forced to cross boundaries she had been carefully trained to respect.

## 7.8 The Interaction Between $\varepsilon$-Admissibility and Moral Injury

The relationship between the heuristic hierarchy and moral injury (Chapters 13--15) is bidirectional and clinically consequential.

**Moral injury degrades admissibility.** A clinician who begins their career with an $\varepsilon$-admissible heuristic ($\varepsilon \approx 0.1$) may, after repeated forced boundary crossings, develop an inadmissible heuristic on the violated dimensions. The inflation or deflation of boundary penalties shifts the heuristic out of the $\varepsilon$-admissible range on specific dimensions while leaving it calibrated on others. The result is a clinician who makes excellent decisions in one domain (e.g., diagnostic reasoning, where $d_1$ and $d_9$ are primary) but systematically suboptimal decisions in another domain (e.g., triage, where the violated boundary is active).

**Proposition 7.5 (Moral Injury as Dimensional $\varepsilon$-Degradation).** *Moral injury produces dimension-specific $\varepsilon$-degradation: the overall heuristic error $\varepsilon = \max_k \varepsilon_k$ increases not because all dimensions are miscalibrated but because the violated dimension's $\varepsilon_k$ has increased substantially. The clinical signature is domain-specific avoidance or desensitization that does not affect unrelated clinical domains.*

This prediction is testable. Survey clinicians who report moral injury for their $\beta_k$ estimates on the violated boundary type. Compare to clinicians without moral injury on the same boundary type. The prediction is that morally injured clinicians show significantly higher $\varepsilon_k$ (either inflated $\beta_k$ for hypervigilant clinicians or deflated $\beta_k$ for morally numb clinicians) on the specific boundary where the injury occurred, with no significant difference on other boundaries.

**Admissibility analysis identifies the injury mechanism.** Conversely, the heuristic hierarchy provides a diagnostic tool for moral injury: by measuring the dimension-specific $\varepsilon_k$ profile of a clinician, one can identify which boundaries have been damaged and in which direction (inflation vs. deflation). This moves moral injury from a global assessment ("this clinician is distressed") to a dimensional assessment ("this clinician has inflated $\beta_{\text{futile}}$ and deflated $\beta_{\text{dignity}}$ as a result of palliative care moral injury"). The dimensional assessment points to a specific recalibration strategy: restore $\beta_{\text{futile}}$ to its appropriate value through structured case review, and restore $\beta_{\text{dignity}}$ through supervised dignity-preserving care.

## 7.9 Institutional Heuristics

The chapter has focused on individual clinician heuristics. But institutions also have heuristics --- institutional norms, protocols, guidelines, and cultural expectations that function as collective $h(n)$ estimates. Institutional heuristics interact with individual heuristics and can either support or undermine individual calibration.

**Supportive institutional heuristics.** A hospital culture that values goals-of-care conversations, provides protected time for consent processes, supports ethics consultations, and structures M&M conferences for constructive heuristic recalibration provides an institutional environment that supports individual $\varepsilon$-admissibility. The institution's collective $h(n)$ --- its norms about what matters and how to navigate the manifold --- is aligned with the individual clinician's heuristic, creating a feedback loop that maintains calibration.

**Undermining institutional heuristics.** A hospital culture that values throughput over process, penalizes clinicians for taking time with patients, discourages ethics consultations as "slowing things down," and uses M&M conferences for blame rather than learning provides an institutional environment that systematically degrades individual $\varepsilon$-admissibility. The institution's collective $h(n)$ --- which emphasizes $d_1$ and $d_8$ at the expense of $d_4$, $d_5$, $d_7$, and $d_9$ --- forces individual clinicians to override their own calibrated heuristics in favor of the institutional heuristic, producing moral distress and eventual moral injury.

**Proposition 7.6 (Institutional Heuristic Determines Individual $\varepsilon$-Trajectory).** *A clinician's long-term $\varepsilon$-trajectory --- whether their heuristic improves, stagnates, or degrades over time --- is determined more by the institutional heuristic environment than by the clinician's initial calibration or individual training. Well-calibrated clinicians in undermining institutional environments degrade toward inadmissibility. Poorly calibrated clinicians in supportive institutional environments improve toward $\varepsilon$-admissibility. The institution is the clinician's heuristic ecosystem.*

This proposition has direct implications for physician retention and workforce health. It predicts that clinician moral distress and attrition correlate not with the inherent difficulty of the clinical work (which determines the frequency of boundary encounters) but with the institutional heuristic environment (which determines whether boundary encounters degrade or maintain the clinician's heuristic). A difficult job in a supportive environment produces calibrated clinicians. An easy job in an undermining environment produces damaged clinicians.

## 7.10 Summary Table: The Four Categories

| Category | Condition | Clinical Signature | Cause | Intervention |
|---|---|---|---|---|
| Strictly admissible | $h_C \ll h^*$ | Absolute prohibitions | Correct identification of sacred values | None needed (these are correct) |
| $\varepsilon$-admissible | $h_C \leq (1+\varepsilon)h^*$ | Near-optimal clinical decisions | Good training and experience | Continued calibration through practice |
| Inadmissible | $h_C > h^*$ (some $n$) | Avoidance of beneficial interventions | Moral injury, defensive medicine, trauma | Ethics consultation, M&M review, institutional support |
| Gauge-variant | $h_C(\tau(n)) \neq h_C(n)$ | Inconsistent care across framings | Cognitive bias, poor metacognition | Awareness training, decision support, BIP testing |

The hierarchy is the diagnostic framework for clinical judgment quality. By identifying which category a clinician's heuristic falls into --- and on which dimensions --- the framework enables targeted interventions that restore the heuristic toward $\varepsilon$-admissibility. The interventions are not punitive; they are calibrative. A clinician with an inadmissible heuristic is not a bad clinician; they are a damaged clinician whose $h(n)$ has been altered by forces beyond their control. The institutional response should be recalibration, not discipline.

---

## Summary

This chapter has characterized the full spectrum of clinical heuristic quality through a four-category hierarchy: strictly admissible (prohibitions whose true cost exceeds any estimate), $\varepsilon$-admissible (well-trained clinicians whose boundary penalties are approximately correct), inadmissible (clinicians with inflated boundary penalties from moral injury, defensive medicine, or personal trauma), and gauge-variant (clinicians whose heuristics depend on framing rather than clinical reality). Medical training is heuristic calibration --- the reduction of $\varepsilon$ from the large values of untrained clinicians to the small values of experienced practitioners. Ethics consultations are heuristic recalibration --- the correction of inadmissible heuristics toward $\varepsilon$-admissibility. Defensive medicine is heuristic inflation --- the systematic overestimation of boundary penalties due to institutional pressure.

The heuristic hierarchy generates testable predictions: specialty-specific $\varepsilon$-profiles (emergency medicine has low $\varepsilon_1$ and high $\varepsilon_7$), the effectiveness of ethics consultations (variance reduction without mean shift), the clinical signature of moral injury (systematic avoidance of specific boundary crossings, measurable as inflated $\beta_k$ values on specific dimensions), and the role of institutional culture in determining long-term heuristic trajectories.

---

[^1]: McNeil, B. J., Pauker, S. G., Sox, H. C., & Tversky, A. (1982). On the elicitation of preferences for alternative therapies. *New England Journal of Medicine*, 306(21), 1259--1262. This landmark study demonstrated that clinicians and patients make different treatment choices when identical outcomes are described in terms of survival versus mortality. The effect has been replicated extensively; see Moxey, A., O'Connell, D., McGettigan, P., & Henry, D. (2003) for a systematic review.
