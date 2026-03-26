# Chapter 2: Triage as Forced Contraction

*Part I: The Problem*

---

> *"Triage is not a medical judgment. It is a moral judgment made under the disguise of a medical judgment."*
> --- Anonymous ICU attending, March 2020

> **THE SORTING**
>
> *The word "triage" comes from the French trier, to sort. Baron Dominique Jean Larrey, Napoleon's chief surgeon, invented the practice on the battlefields of the Napoleonic Wars: sort the wounded into three categories --- those who will survive without treatment, those who will die regardless of treatment, and those who will survive only with treatment. Treat the third group. The logic is impeccable on one dimension. On nine dimensions, it is a catastrophe.*
>
> *Every triage system since Larrey has been a specific contraction of the clinical-moral tensor to a low-dimensional decision. Each system chooses different dimensions to preserve and different dimensions to discard. Each leaves a moral residue on the clinicians who perform it --- a residue that accumulates, that changes them, and that no amount of debriefing can fully dissolve. This chapter examines triage not as a medical procedure but as a mathematical operation: forced contraction of a nine-dimensional clinical-moral state to a binary or ordinal decision under time pressure. The question is not whether to contract --- time pressure makes contraction unavoidable --- but how to contract with minimal information loss, and what moral residue the contraction leaves.*

---

## 2.1 Ninety Seconds

Sarah's emergency department rotation began on a Tuesday in October. She had been warned that the pace would be different from the internal medicine wards: faster, louder, more uncertain. She had not been warned about the sorting.

At 7:42 PM, a bus collision at the intersection of MLK Boulevard and 5th Street produced twelve casualties. They arrived in three waves: four by ambulance within eight minutes, five by ambulance within fifteen minutes, three who walked in from the scene over the next half hour. The attending physician, Dr. Rachel Kim, met the first ambulance at the bay doors.

Sarah watched Dr. Kim triage the first four patients in ninety seconds.

Patient 1: Unresponsive, GCS 4, visible skull deformity, agonal breathing. Dr. Kim: "Bay 1, neurosurgery stat, but ---" She paused, her hand on the patient's wrist, and something passed across her face that Sarah would learn to recognize: the compression of nine dimensions into a single decision. "Bay 1, neurosurgery stat."

Patient 2: Conscious, screaming, open femur fracture, blood pressure 90/60. Dr. Kim: "Bay 3, orthopedics, two units PRBCs running, bilateral large-bore IVs."

Patient 3: Conscious, ambulatory with assistance, holding left arm, no visible hemorrhage. Dr. Kim: "Fast track, X-ray left arm, back of the line."

Patient 4: Unconscious but breathing spontaneously, GCS 8, no visible external injuries. Dr. Kim: "Bay 2, CT head, C-spine precautions, monitor."

Four patients. Four decisions. Ninety seconds. Sarah could not have read the first patient's chart in ninety seconds, let alone assessed, diagnosed, and triaged them. Dr. Kim had contracted four nine-dimensional clinical-moral tensors to an ordinal ranking --- not by algorithm but by pathfinding on a manifold she had traversed thousands of times. Her heuristic function $h(n)$ was so well-calibrated that the computation was invisible: it looked like instinct, like reflex, like the effortless pattern recognition that medical students mistake for talent and that is in fact twenty years of heuristic calibration.

But Sarah noticed something that she could not yet name. When Dr. Kim triaged Patient 1 --- the patient with the skull deformity, the GCS of 4, the agonal breathing --- she hesitated. Not long. Perhaps half a second. And in that half second, Sarah saw something that no triage score captures: the cost of the decision on the dimensions the triage score does not see.

Dr. Kim was not computing $d_1$ alone. She was computing, in a compressed and automatic way, the full edge weight: the Mahalanobis distance across all nine dimensions plus the boundary penalties. Patient 1 had a very low probability of meaningful survival ($d_1$), but she was someone's mother, someone's colleague, someone's friend ($d_6$). She deserved treatment that did not reduce her to a probability ($d_7$). The decision to classify her as "treat but ---" was a boundary crossing: the futility boundary ($\beta_{\text{futile}}$), the threshold where continued intervention becomes not just useless but a violation of the patient's dignity. Dr. Kim crossed the boundary because the alternative --- not summoning neurosurgery at all --- would have crossed the abandonment boundary ($\beta_{\text{abandon}}$), which for this patient at this moment had a higher cost.

The triage score would record: ESI-1. A single integer. The moral computation that produced the integer --- the simultaneous evaluation of nine dimensions, the assessment of two competing boundary crossings, the half-second of hesitation that contained the full weight of clinical ethics --- would not be recorded anywhere.

[Figure 2.1: Dr. Kim's ninety-second triage of four patients, represented on the nine-dimensional clinical decision complex. Each patient occupies a point in the nine-dimensional space. The triage decision contracts each nine-dimensional state to a single ordinal ranking (ESI level). The figure shows the information lost in each contraction: Patient 1 loses the futility/abandonment boundary trade-off; Patient 3 loses the justice dimension (back of the line means waiting longest despite arriving first by ambulance).]

## 2.2 A History of Sorting

Triage is as old as organized military medicine, and every instantiation tells us something about which dimensions of clinical reality a society considers worth preserving under pressure.

### 2.2.1 Larrey's Battlefield (1792)

Baron Dominique Jean Larrey did not invent the idea of sorting casualties. He invented the idea of sorting them by *medical need* rather than by *rank*. Before Larrey, wounded officers were treated before enlisted men regardless of the severity of their injuries. Larrey's innovation was to sort by the single dimension of clinical outcome ($d_1$): treat those who will benefit from treatment, comfort those who will die regardless, and defer those who will survive without treatment.

This was revolutionary for $d_3$ (justice): it replaced a feudal allocation system with an egalitarian one. But it was also a specific contraction. Larrey's system operated on exactly one dimension --- clinical outcome modified by treatability. It had no representation of the soldier's rights ($d_2$), autonomy ($d_4$: no soldier was asked whether they wanted to be treated), trust ($d_5$: the medical relationship was not therapeutic but military), dignity ($d_7$: the sorting happened on the battlefield, in mud and chaos), or understanding ($d_9$: no one explained the triage criteria to the wounded). On the battlefield, under fire, with two hundred casualties and three surgeons, these omissions were not failures of compassion. They were the mathematical cost of a forced contraction to one dimension under time pressure that allowed no other choice.

### 2.2.2 The Red Cross and the Geneva Conventions (1864--1949)

The codification of triage in international humanitarian law introduced $d_2$ (rights) and $d_3$ (justice) as explicit dimensions of the triage calculus. The Geneva Conventions require that wounded combatants receive care without discrimination based on nationality, rank, or political allegiance. This is a gauge invariance condition on the triage function: the triage decision must be invariant under relabeling of the combatants' national identity. Larrey's innovation --- sort by need, not by rank --- was formalized as a legal obligation.

But the Geneva Conventions' triage calculus still operates on a restricted manifold: $d_1$ (medical need) + $d_2$ (right to treatment) + $d_3$ (non-discrimination). The remaining six dimensions --- autonomy, trust, social impact, dignity, institutional legitimacy, epistemic status --- are not addressed. This is not a criticism; it is a description of which dimensions can be preserved under the constraints of armed conflict and which must be sacrificed.

### 2.2.3 Modern Emergency Triage: ESI, START, JumpSTART

The contemporary triage landscape reflects decades of refinement in which different systems have chosen different dimensional projections.

**ESI (Emergency Severity Index)** contracts to two dimensions: $d_1$ (acuity: how sick is the patient?) and $d_8$ (resource need: how many resources will this patient require?). The five ESI levels represent a two-dimensional lattice projected onto a single ordinal scale. ESI-1 (high acuity, immediate resource need) and ESI-5 (low acuity, no resource need) are unambiguous. ESI-3 (moderate acuity, two or more resources) is a vast category that encompasses patients with radically different clinical-moral profiles --- a category so broad that "ESI-3" has become, in many emergency departments, a synonym for "I don't know yet."[^1]

**START (Simple Triage and Rapid Treatment)** is used for mass casualty incidents. It contracts to three physiologic parameters: respiration, perfusion (capillary refill or radial pulse), and mental status. Each is binary (adequate/inadequate), producing four categories: Immediate (red), Delayed (yellow), Minor (green), Expectant (black). START is a three-dimensional binary projection of the clinical state onto four bins. It has no representation of any non-physiologic dimension --- no trust, no autonomy, no dignity, no justice. It is the purest possible $d_1$ contraction, designed for the scenario where time is measured in seconds and the only question is "will this person die in the next few minutes without treatment?"

**JumpSTART** modifies START for pediatric patients, adding a step for assisted ventilations and adjusting the respiratory rate threshold. The modification implicitly acknowledges that the pediatric clinical manifold has different boundary penalties than the adult manifold --- specifically, that the futility threshold ($\beta_{\text{futile}}$) is higher for children, reflecting both the biological reality of greater neuroplasticity and the social reality of greater moral weight assigned to pediatric death. This is not a medical judgment. It is a dimensional weighting decision: society assigns higher $d_7$ (dignity) and $d_6$ (social impact) costs to pediatric death, and these costs shift the boundary even though the $d_1$ calculus might not change.

### 2.2.4 Pandemic Triage: Crisis Standards of Care

COVID-19 forced a new triage paradigm: crisis standards of care (CSC), which explicitly authorize the reallocation of scarce resources (primarily ventilators and ICU beds) based on probability of survival and expected duration of benefit. The dominant framework, articulated by Emanuel et al. (2020), proposed four values for allocation: maximizing benefits, treating equally, promoting and rewarding instrumental value, and giving priority to the worst off.[^2]

Emanuel et al.'s framework is remarkable for its explicit multi-dimensionality. It names four values, not one. But the implementation --- the actual triage algorithm deployed in hospitals --- typically contracted these four values to a single scalar: a composite priority score based on short-term prognosis, long-term prognosis, and (in some versions) life-cycle considerations. The four values were stated in the framework and discarded in the implementation. The gap between the ethical framework (four-dimensional) and the operational protocol (one-dimensional) is precisely the gap this book addresses.

[Figure 2.2: Historical evolution of triage dimensionality. Larrey (1792): $d_1$ only. Geneva Conventions (1864--1949): $d_1 + d_2 + d_3$. ESI (2011): $d_1 + d_8$. START (1983): three binary physiologic parameters within $d_1$. CSC (2020): stated as $d_1 + d_3 + d_7$, implemented as $d_1$ only. Each system is a specific projection of the nine-dimensional clinical decision complex.]

## 2.3 The Anatomy of Forced Contraction

Triage is a forced contraction: the compression of a multi-dimensional clinical-moral state to a low-dimensional decision under constraints that make the compression unavoidable. Every forced contraction has three components, and understanding them separately is essential to understanding what triage does and what it costs.

### 2.3.1 Time Pressure as Dimensional Collapse

In normal clinical reasoning, the clinician navigates the nine-dimensional decision complex at a pace that allows deliberation: consult the chart, examine the patient, discuss with colleagues, consider alternatives, sleep on it. Time permits a full nine-dimensional pathfinding computation.

In triage, time collapses the dimensionality. Dr. Kim had ninety seconds for four patients. At that rate, she could assess perhaps two dimensions per patient: $d_1$ (how sick?) and a rough gestalt of $d_2$--$d_9$ (anything else screaming for attention?). The remaining dimensions were not evaluated, not because they do not matter, but because time did not permit the evaluation.

This is not a failure of the clinician. It is a mathematical constraint. The information capacity of the triage channel --- the number of bits that can be processed per unit time --- is bounded by the clinician's cognitive architecture. Under extreme time pressure, the channel narrows, and the contraction becomes more severe. The clinician compensates by relying more heavily on $h(n)$ (the heuristic, which is fast) and less on $g(n)$ (the evidence-based calculation, which is slow). The triage decision is heuristic-dominated, which means it inherits the heuristic's strengths (speed, pattern recognition) and its weaknesses (bias, framing sensitivity, dimensional omission).

**Definition 2.1 (Forced Contraction).** *A forced contraction is a decision process in which a clinical-moral state $\mathbf{a} \in \mathbb{R}^9$ must be mapped to a decision $d \in D$ (where $D$ is a finite set of triage categories) under a time constraint $t < t_{\text{threshold}}$ that prevents full nine-dimensional pathfinding. The contraction operator $\pi_t: \mathbb{R}^9 \to D$ depends on the available time $t$: as $t$ decreases, $\pi_t$ projects onto fewer dimensions. In the limit of zero time, $\pi_0$ projects onto $d_1$ alone (survival probability). In the limit of infinite time, $\pi_\infty$ is the clinical geodesic on the full manifold.*

### 2.3.2 Resource Constraint as Boundary Imposition

Time pressure collapses the dimensionality of the *assessment*. Resource constraint collapses the dimensionality of the *response*. When there are twelve ventilators and thirty patients, the decision is not "what is the optimal path for each patient?" but "which twelve patients receive ventilators?" The resource constraint converts a pathfinding problem into an allocation problem --- a fundamentally different mathematical object.

In the language of the clinical decision complex, resource constraint imposes new boundaries on the manifold. Without the constraint, every patient has access to the full set of clinical actions (every edge on the complex is available). With the constraint, some edges are removed: the edge "place patient on ventilator" is available for at most twelve patients. The removal of edges changes the topology of the complex --- it disconnects some patients' goal regions from their start nodes, making their optimal paths unreachable. For these patients, the clinical geodesic does not exist on the constrained complex. There is no path from where they are to where they need to be, because the resources that would make the path possible have been allocated to someone else.

This is triage in its starkest form: the allocation decision creates patients for whom no clinical geodesic exists. They are not triaged to a lower priority. They are triaged to *no path*. And the clinician who makes this allocation --- who removes the edges from the complex by directing the ventilator to patient A rather than patient B --- bears the full moral cost of the boundary crossings that the removal entails.

### 2.3.3 Moral Residue as Contraction Cost

The term "moral residue" was introduced by Epstein and Hamric (2009) to describe the lasting psychological effects of morally distressing clinical experiences.[^3] In the geometric framework, moral residue has a precise interpretation: it is the moral cost of the edges that were traversed during the forced contraction but that would not have been traversed on the unconstrained manifold.

When Dr. Kim triaged Patient 1 as "treat but ---," she crossed the futility boundary. On the unconstrained manifold, she might have had time to gather more information, consult with neurosurgery before committing resources, involve the family in a goals-of-care conversation. The unconstrained geodesic would have avoided the futility boundary entirely by approaching it gradually, with more information and more support. The forced contraction required her to cross the boundary immediately, in ninety seconds, with incomplete information, in a hallway. The moral cost of the crossing --- the difference between the boundary penalty on the forced path and the boundary penalty on the unconstrained geodesic --- is the moral residue.

**Definition 2.2 (Moral Residue of Contraction).** *The moral residue of a forced contraction $\pi_t$ applied to a clinical state $\mathbf{a}$ is the difference in clinical friction between the forced path and the unconstrained geodesic:*

$$\text{MR}(\pi_t, \mathbf{a}) = \text{CF}(\gamma_{\pi_t}^*) - \text{CF}(\gamma_{\mathcal{C}}^*)$$

*where $\gamma_{\pi_t}^*$ is the path mandated by the forced contraction and $\gamma_{\mathcal{C}}^*$ is the clinical geodesic on the full manifold.*

Moral residue is always non-negative (the forced path is never cheaper than the unconstrained geodesic, because the forced path is a feasible path and the geodesic is the minimum-cost path). It is zero only when the forced contraction happens to select the same path as the unconstrained geodesic --- that is, when the contraction discards no relevant information. For simple triage decisions (the clearly dying, the clearly stable), the residue may be near zero. For the hardest decisions --- the patients in the middle, the ones where the allocation could go either way --- the residue is highest.

And the residue does not vanish after the decision. It accumulates in the clinician, altering the heuristic function, shifting boundary penalties, changing the clinician's relationship to future decisions. This accumulation is the subject of Chapters 13--15. Here the point is structural: triage is not a free operation. Every contraction has a cost, and the cost is borne by the clinician who performs it.

## 2.4 Three Contractions Compared

To make the anatomy of forced contraction concrete, consider the same patient evaluated by three different triage systems.

**Patient:** Maria Santos, 67 years old, diabetic, presenting to the emergency department with chest pain, shortness of breath, and confusion. Vitals: BP 85/50, HR 120, RR 28, SpO2 88%, temp 38.9C. She speaks only Spanish. Her daughter, who translates, says that Maria does not want "machines" but has not completed an advance directive. Maria has not seen a physician in four years because she lost trust in the medical system after a billing dispute that she perceived as exploitative.

**Nine-dimensional attribute vector:**
- $d_1$ (outcomes): 0.3 (acutely ill, multiple deranging physiologic parameters)
- $d_2$ (rights): 0.5 (right to treatment intact, right to refuse unclear due to $d_9$)
- $d_3$ (justice): 0.4 (language barrier may impede equitable care)
- $d_4$ (autonomy): 0.3 (confusion impairs decision-making capacity)
- $d_5$ (trust): 0.2 (deeply distrustful of the medical system)
- $d_6$ (social): 0.5 (daughter present, engaged, translating)
- $d_7$ (dignity): 0.4 (confused, partially undressed for assessment, in a hallway)
- $d_8$ (institutional): 0.6 (standard protocols apply)
- $d_9$ (epistemic): 0.2 (diagnosis uncertain, patient's wishes unclear, language barrier to information exchange)

### Contraction 1: ESI

The ESI nurse evaluates Maria on two dimensions: acuity (how sick?) and resource need (how many resources?). Maria is hemodynamically unstable (ESI-2: high risk) and will require multiple resources (labs, imaging, IV fluids, likely ICU admission). ESI classification: **ESI-2**.

*What the contraction preserves:* $d_1$ (Maria is sick and needs immediate attention) and $d_8$ (the resource assessment matches institutional protocols).

*What the contraction discards:* $d_4$ (Maria may not want aggressive treatment, but nobody has asked in a language she understands), $d_5$ (Maria distrusts the system, which will affect her cooperation and outcomes), $d_9$ (the diagnosis is uncertain and the patient's wishes are unknown), $d_7$ (Maria is being assessed in a hallway without privacy).

*Moral residue:* Low, because ESI-2 appropriately prioritizes the patient's acute needs. But the residue accumulates downstream: the ESI classification triggers a cascade of aggressive interventions (IV access, blood draws, imaging) that may cross Maria's stated preference against "machines" --- a preference that was registered but not evaluated because the ESI has no dimension for patient preferences.

### Contraction 2: START

If Maria had arrived at a mass casualty scene, the START algorithm would evaluate her as follows. Respiration: present, rate >30 (abnormal). Perfusion: radial pulse present, capillary refill delayed. Mental status: confused, does not follow commands. START classification: **Immediate (Red)**.

*What the contraction preserves:* A minimal $d_1$ assessment --- Maria is acutely physiologically deranged and needs immediate intervention to survive.

*What the contraction discards:* Everything else. START has no representation of Maria's language, culture, preferences, trust, dignity, or understanding. It does not know that she is confused because of sepsis (treatable) versus because of advanced dementia (chronic). It does not know that she does not want "machines." It does not know that her daughter is present and could provide critical history. The contraction is so severe that Maria is reduced to three binary physiologic parameters, and the resulting classification drives a response (aggressive resuscitation, intubation if needed) that may be precisely what Maria does not want.

*Moral residue:* Potentially high, because the START classification may trigger interventions that cross the consent boundary ($\beta_{\text{consent}}$) for a patient whose wishes are unknown but whose daughter has reported a preference against aggressive treatment. The residue falls on the clinician who intubates Maria without knowing whether she would have wanted it --- a boundary crossing that cannot be undone.

### Contraction 3: CSC (Pandemic Triage)

If Maria arrived during a pandemic surge with ICU beds scarce, a crisis standards of care protocol would evaluate her as follows. Short-term prognosis: poor (SOFA score high, multiple organ dysfunction). Long-term prognosis: moderate (diabetes, age 67, baseline functional). Composite priority score: moderate-low. With limited ICU beds, Maria would likely be classified as: **Lower priority for ICU admission**.

*What the contraction preserves:* $d_1$ (survival probability) modified by $d_3$ (the CSC framework claims to incorporate equity, though the implementation typically does not).

*What the contraction discards:* $d_5$ (Maria's distrust, which is the product of a specific history of institutional betrayal and which shapes her willingness to engage with any medical intervention), $d_9$ (the profound uncertainty about Maria's diagnosis, which makes the prognosis estimate unreliable), $d_4$ (Maria's preferences, which are unknown because nobody has asked in her language), $d_7$ (Maria's dignity, which is further compromised by the denial of ICU care).

*Moral residue:* Very high. The CSC protocol denies Maria an ICU bed based on a prognosis estimated under conditions of maximal uncertainty ($d_9 = 0.2$), for a patient whose trust deficit ($d_5 = 0.2$) means she may not cooperate with non-ICU alternatives, from a system she already perceives as exploitative. The clinician who implements this triage decision bears the moral cost of the abandonment boundary crossing ($\beta_{\text{abandon}}$) and the justice boundary crossing ($\beta_{\text{justice}}$: a Spanish-speaking, low-trust, minority patient deprioritized by a system that has not communicated with her in her language). The residue does not vanish. It changes the clinician.

[Figure 2.3: Maria Santos evaluated by three triage systems. Each system projects her nine-dimensional state onto a different subspace. ESI: $d_1 + d_8$ (acuity + resources). START: three binary parameters within $d_1$. CSC: $d_1$ weighted by prognosis. The nine-dimensional attribute vector is the same in all three cases. The triage classifications are different. The moral residue is different. The patient is the same.]

## 2.5 Why Clinicians Resist Utilitarian Triage

The geometric framework resolves a puzzle that has troubled the triage ethics literature: why do experienced clinicians resist utilitarian triage protocols that are mathematically optimal on $d_1$?

The standard explanation is emotional: clinicians resist because triage is emotionally difficult, because they form attachments to patients, because the psychological burden of playing God is too great. This explanation is condescending and wrong. It treats clinician resistance as a weakness to be managed rather than as a signal to be understood.

The geometric explanation is structural: clinicians resist utilitarian triage because their heuristic function $h(n)$ correctly identifies that the utilitarian path crosses moral boundaries whose cost exceeds the utilitarian benefit. The clinicians are computing on the full nine-dimensional manifold. The utilitarian protocol is computing on a one-dimensional projection. The resistance is not emotional irrationality; it is dimensional mismatch.

Consider ventilator reallocation --- the paradigm case of utilitarian triage resistance during COVID-19. A utilitarian protocol says: withdraw the ventilator from Patient A (lower probability of survival) and give it to Patient B (higher probability of survival). The expected $d_1$ benefit is positive. The utilitarian calculation is correct on $d_1$.

But the clinician's $h(n)$ computes the full edge weight of the reallocation:

$$w_{\text{realloc}} = \underbrace{\Delta d_1}_{\text{positive}} + \underbrace{\beta_{\text{abandon}} \cdot 1[\text{withdrawal}]}_{\text{large}} + \underbrace{\beta_{\text{trust}} \cdot 1[\text{breach of implied commitment}]}_{\text{large}} + \underbrace{\Delta d_7[\text{Patient A}]}_{\text{negative}} + \underbrace{\Delta d_5[\text{all patients}]}_{\text{negative}}$$

The abandonment boundary ($\beta_{\text{abandon}}$) is one of the highest-cost boundaries on the clinical manifold. The therapeutic relationship creates an implied commitment: having placed Patient A on a ventilator, the institution has created a fiduciary obligation that withdrawal violates. The trust cost ($\Delta d_5$) affects not just Patient A but all patients: if the hospital withdraws ventilators from current patients, the trust relationship between the institution and its community is damaged for every patient, current and future. The dignity cost ($\Delta d_7$) to Patient A --- being removed from a ventilator to die while a stranger receives it --- is not captured by any utilitarian calculation.

The total edge weight of reallocation can be positive (manifold-suboptimal) even when the $d_1$ component is negative (utilitarian-optimal). The clinicians who resist are not failing to compute the utilitarian calculus. They are computing a richer calculus and finding that the utilitarian-optimal path is manifold-suboptimal.

This does not mean that ventilator reallocation is never justified. The framework computes when it is: reallocation is manifold-optimal when the $d_1$ benefit is large enough to outweigh the boundary costs, which typically requires a very large difference in survival probability between the two patients, a transparent and legitimate reallocation process ($d_8$), and institutional support for the clinician performing the reallocation (to manage the moral injury). The conditions under which reallocation is manifold-optimal are much more restrictive than the conditions under which it is utilitarian-optimal --- and this difference explains the clinician resistance that utilitarian ethicists have found puzzling.

## 2.6 The Moral Algebra of Sorting

Every triage system embeds a moral algebra --- a set of rules for combining dimensional assessments into a single ranking. The algebra is usually implicit, disguised as medical judgment or institutional protocol. The geometric framework makes it explicit.

### 2.6.1 Lexicographic Triage

START uses a lexicographic ordering: first evaluate respiration, then perfusion, then mental status. If respiration is absent, the patient is classified as Expectant (black) regardless of perfusion or mental status. This is a lexicographic contraction: $d_1^{\text{resp}} > d_1^{\text{perf}} > d_1^{\text{mental}}$, where ">" means "evaluated first, and if the evaluation is decisive, the remaining dimensions are not consulted."

Lexicographic contraction has the virtue of speed and the vice of rigidity. It is fast because the algorithm terminates as soon as a decisive criterion is reached. It is rigid because it cannot represent trade-offs between dimensions: a patient with absent respiration but excellent perfusion and mental status (possibly apneic from an airway obstruction that could be quickly relieved) is classified identically to a patient with absent respiration, absent perfusion, and absent mental status (irreversibly dead). The lexicographic order cannot distinguish them because it does not compute past the first criterion.

### 2.6.2 Weighted Sum Triage

APACHE and SOFA scores use a weighted sum: assign numerical scores to multiple parameters and add them. The sum is a linear contraction:

$$\text{Score} = \sum_i w_i \cdot x_i$$

where $x_i$ is the value on parameter $i$ and $w_i$ is its weight. The weighted sum has the virtue of considering multiple parameters simultaneously and the vice of assuming that their contributions are additive and independent. The cross-terms ($\Sigma_{ij}$ in the Mahalanobis distance) are zero in a weighted sum. The interaction between respiratory failure and renal failure --- the fact that they are synergistically worse than the sum of their individual effects --- is invisible to the linear contraction.

### 2.6.3 Threshold Triage

ESI uses a decision tree with thresholds: "Is the patient dying?" (yes/no), "Is the patient high-risk?" (yes/no), "How many resources?" (0/1/2+). The thresholds are boundary-based contractions: they evaluate the patient's position relative to fixed boundaries on the clinical manifold and classify based on which region the patient occupies.

Threshold triage has the virtue of capturing the boundary structure that scored triage discards. It has the vice of treating boundaries as sharp when they are often fuzzy: the boundary between "high-risk" and "not high-risk" is a gradient, not a line, and patients near the boundary may be classified differently by different triage nurses depending on which side of the threshold the patient falls on at the moment of assessment. The noise near the boundary is a consequence of the threshold contraction: the smooth manifold is carved into discrete regions, and the carving introduces discontinuities that do not exist in the underlying clinical reality.

### 2.6.4 Manifold-Optimal Triage

The clinical decision complex suggests a fourth approach: triage not by lexicographic order, weighted sum, or threshold, but by pathfinding on the full manifold. The triage decision is the allocation that minimizes total clinical friction:

$$(\gamma_1^*, \ldots, \gamma_n^*) = \arg\min_{\gamma_1, \ldots, \gamma_n} \sum_{i=1}^n \text{CF}(\gamma_i) \quad \text{subject to } \sum_{i=1}^n r(\gamma_i) \leq R$$

This is computationally more expensive than any of the three simple contractions. It is also more accurate, in the precise sense that it minimizes the moral residue of the triage decision. The framework does not propose manifold-optimal triage for the emergency department at 7:42 PM with twelve casualties arriving simultaneously --- that scenario demands the speed of START or ESI. It proposes manifold-optimal triage for the decisions that are made in advance: the crisis standards of care, the institutional triage protocols, the vaccine allocation algorithms, the organ transplant scoring systems. These decisions have time for full-manifold computation. They affect millions of patients. And the moral residue of getting them wrong falls not on a single clinician in a single moment but on an entire healthcare system over years.

## 2.7 Sarah at the Whiteboard

Three weeks into her emergency department rotation, Sarah stayed late one evening and drew on the whiteboard in the residents' workroom. She drew nine axes, labeled them $d_1$ through $d_9$, and tried to plot Maria Santos's attribute vector. She drew the ESI contraction as a projection onto two axes. She drew the START contraction as a projection onto three binary parameters within $d_1$. She drew the CSC contraction as a projection onto $d_1$ with prognosis weighting.

Dr. Kim found her at the whiteboard at 11 PM.

"What are you doing?"

"Trying to understand what we lose when we triage."

Dr. Kim looked at the whiteboard for a long time. She was not a mathematician; she did not know the word "contraction" or the phrase "Scalar Irrecoverability Theorem." But she had triaged ten thousand patients, and she recognized the structure Sarah was drawing.

"You lose the person," Dr. Kim said. "The score gives you the patient. Triage gives you the priority. But the person --- who they trust, what they're afraid of, what they value, what they understand --- that's what you lose. And you have to lose it, because you have ninety seconds and four patients and three ambulances coming behind them. You lose the person so you can save the body." She paused. "And then the person haunts you."

Sarah looked at her nine axes, at the projections, at the information lost in each contraction. "Is there a way to lose less?"

"Not in ninety seconds," Dr. Kim said. "But in ninety days --- when we write the protocol, when we design the triage criteria, when we decide what the system will do before the bus crash happens --- in ninety days, yes. You can think about all nine dimensions. You can build a system that remembers the person even when the clinician is too busy to." She tapped the whiteboard. "That's what ethics committees are for. They have the time we don't."

This is the insight that the book formalizes: triage under time pressure is inevitably a contraction, and the contraction inevitably has a moral cost. But the *design* of triage systems --- the choice of which dimensions to preserve, which boundaries to protect, which residue to tolerate --- is not time-pressured. It can be computed on the full manifold. And when it is computed on the full manifold, the resulting triage systems produce less moral residue, less clinician damage, and less systematic injustice than systems designed on a one-dimensional projection.

The manifold-optimal triage system does not produce manifold-optimal decisions at the bedside. It produces systems that minimize the cost of the forced contractions that the bedside inevitably requires. It does not eliminate moral residue. It manages it --- prospectively, quantitatively, equitably --- so that the costs of triage fall where they can be borne and not where they will break.

## 2.8 The Residue That Remains

This chapter has argued that triage is forced contraction --- the compression of a nine-dimensional clinical-moral state to a low-dimensional decision under time and resource constraints. The compression is mathematically inevitable, morally costly, and structurally different from what it appears to be on the surface.

On the surface, triage looks like a medical decision: how sick is the patient, and what do they need? Beneath the surface, triage is a moral decision: which dimensions of the patient's clinical-moral reality will we see, and which will we discard? The choice of dimensions is not made by the triaging clinician in the moment of crisis. It is made by the system designers who chose the triage criteria, the institution administrators who chose the triage protocol, and the policy makers who chose the crisis standards of care. These choices are made in advance, under no time pressure, with access to the full manifold. They should be made on the full manifold.

The next chapter traces the geometric intuitions that have been present in medical ethics for twenty-five centuries --- from the Hippocratic Oath through Beauchamp and Childress through narrative ethics --- showing that each tradition captured part of the manifold structure without the vocabulary to name it. Chapter 4 will then construct the clinical decision complex in full: the nine-dimensional weighted simplicial complex that provides the mathematical structure for everything that follows.

But the residue from this chapter remains. It remains in Dr. Kim, who has triaged ten thousand patients and carries the accumulated boundary crossings in her heuristic function. It remains in Maria Santos, who was triaged by three different systems, each of which saw a different slice of her reality and none of which saw the whole. And it remains in Sarah, who stood at a whiteboard at 11 PM and drew nine axes because she knew, without yet having the mathematics, that a person is not a number and that the gap between them has consequences that no scoring system records.

The consequences are measured in moral residue. The residue accumulates. The accumulation is the subject of Part V. But first, we need the history. Before we can build the manifold, we need to understand why twenty-five centuries of medical ethics have been reaching toward it.

---

## Summary

This chapter has examined triage as the paradigm case of forced contraction in clinical medicine. Triage compresses a nine-dimensional clinical-moral state to a binary or ordinal decision under time and resource constraints. The chapter traced the history of triage from Larrey's battlefield (one-dimensional: survival) through the Geneva Conventions (three-dimensional: survival + rights + justice) through modern emergency triage systems (ESI: acuity + resources; START: three binary physiologic parameters) to pandemic crisis standards of care (survival probability with prognosis weighting).

Three structural components of forced contraction were identified: time pressure (which collapses the dimensionality of the assessment), resource constraint (which removes edges from the decision complex, disconnecting some patients from their goal regions), and moral residue (the difference in clinical friction between the forced path and the unconstrained geodesic). A concrete example --- Maria Santos evaluated by ESI, START, and CSC --- demonstrated that each triage system preserves different dimensions and produces different moral residue.

The chapter argued that clinician resistance to utilitarian triage is not emotional irrationality but dimensional mismatch: clinicians compute on the full manifold and correctly identify that the utilitarian-optimal path crosses moral boundaries whose cost exceeds the utilitarian benefit. The geometric framework provides the mathematics for designing triage systems that minimize moral residue --- not at the bedside, where time pressure makes contraction unavoidable, but in advance, where full-manifold computation is possible and its consequences affect millions of patients.

---

[^1]: Gilboy, N., Tanabe, T., Travers, D., & Rosenau, A. M. (2011). Emergency Severity Index (ESI): A Triage Tool for Emergency Department Care. Version 4, AHRQ Publication No. 12-0014. The ESI-3 category has been estimated to encompass 40-60% of all emergency department patients, making it the single largest category and the least informative.

[^2]: Emanuel, E. J., Persad, G., Upshur, R., Thome, B., Parker, M., Glickman, A., Zhang, C., Boyle, C., Smith, M., & Phillips, J. P. (2020). Fair allocation of scarce medical resources in the time of Covid-19. *New England Journal of Medicine*, 382(21), 2049--2055.

[^3]: Epstein, E. G., & Hamric, A. B. (2009). Moral distress, moral residue, and the crescendo effect. *The Journal of Clinical Ethics*, 20(4), 330--342. Epstein and Hamric coined the term "crescendo effect" to describe the cumulative nature of moral residue, a concept that the Moral Injury Accumulation Theorem (Chapter 13) formalizes mathematically.
