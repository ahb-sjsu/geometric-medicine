# Chapter 1: The QALY Trap

*Part I: The Problem*

---

> *"The good physician treats the disease; the great physician treats the patient who has the disease."*
> --- William Osler

> **THE CLINICAL TRAJECTORY**
>
> *In 1977, Milton Weinstein and William Stason published "Foundations of Cost-Effectiveness Analysis for Health and Medical Practices" in the New England Journal of Medicine. They proposed a deceptively simple idea: combine life expectancy with a quality weight between 0 (death) and 1 (perfect health) to produce a single number --- the quality-adjusted life year, or QALY --- that could guide resource allocation across the entire medical system. The idea was brilliant in its parsimony. It was also, in a precise mathematical sense, catastrophic.*
>
> *The QALY did not merely simplify clinical reality. It compressed a nine-dimensional clinical-moral state into a scalar, and the compression destroyed exactly the information that matters most in hard cases: whether the patient trusts the physician, whether they understand what is being proposed, whether the treatment respects their dignity, whether the allocation is just. These are not philosophical luxuries. They are dimensions of clinical reality that clinicians navigate every day --- dimensions that the QALY, by mathematical necessity, cannot see.*
>
> *This chapter introduces the problem. The next seventeen chapters build the solution.*

---

## 1.1 Sarah's First Patient

Dr. Sarah Chen's hands were not shaking as she presented her first patient on the internal medicine service. She had practiced the format: age, sex, chief complaint, history of present illness, past medical history, medications, allergies, review of systems, physical exam, assessment and plan. She had the labs memorized. She had rehearsed the differential diagnosis. She was, by every measure of medical school preparation, ready.

"Seventy-two-year-old male," she began, reading from her index cards. "Admitted with community-acquired pneumonia. APACHE II score of 18, predicted mortality 25 percent. Charlson Comorbidity Index 4. Estimated QALY value 0.4 based on age and comorbidities. Plan: IV antibiotics, supplemental oxygen, monitor for clinical deterioration."

Dr. Margaret Torres, the attending physician, listened with her arms crossed. She was fifty-three, with the particular stillness of a clinician who has heard ten thousand presentations and learned that the most important information is usually what the presenter leaves out.

"What's his name?" Dr. Torres asked.

Sarah blinked. "Mr. James Okafor."

"Does he trust us?"

Sarah opened her mouth, closed it, and looked at her index cards. The question was not on any card. It was not in any scoring system she had learned. "I --- I didn't assess that."

"Does he understand what we're proposing? The IV antibiotics, the oxygen, the monitoring --- does he know why we're doing each of those things?"

"He signed the consent form."

"That's not what I asked. What does his family think? Does he have a family? What does he value --- what matters to him about getting better?"

Sarah felt the floor shift beneath her, not physically but epistemically. Every question Dr. Torres asked pointed to a dimension of the patient's reality that her presentation had not captured. Not because she had been careless, but because the tools she had been given --- APACHE scores, Charlson indices, QALY estimates --- had no place to put the answers.

"Let me ask it differently," Dr. Torres said, her voice gentler now. "You told me his QALY is 0.4. What does that number mean?"

"It means his quality of life is 40 percent of perfect health, adjusted for ---"

"It means nothing." Dr. Torres held up a hand. "I don't say that to be harsh. I say it because a QALY of 0.4 is compatible with a patient who has moderate physical limitation but intact autonomy, full trust in his medical team, strong family support, clear understanding of his condition, and a deep sense of dignity about how he wants to live and die. It is equally compatible with a patient who has reasonable physical function but has lost all trust in the medical system, feels coerced into treatment, has no family support, does not understand what we are doing to him, and has been stripped of every form of dignity by the way we have treated him. The number is the same. The patients are not the same. The treatment should not be the same. And if you build your clinical reasoning on the number, you will treat them identically and be wrong about both."

Sarah stared at the number on her card: 0.4. It looked different now. It looked like a shadow cast by a nine-dimensional object onto a one-dimensional wall --- a shadow that preserved the object's height but discarded its depth, its color, its texture, its weight, its warmth, its history, its meaning.

She did not yet have the mathematics to describe what she was seeing. But she had the clinical intuition, planted in that moment by an attending who had navigated the manifold for twenty-five years and knew, in her bones, that the map was not the territory.

This book provides the mathematics.

[Figure 1.1: Two patients with identical QALY scores of 0.4, visualized in the nine-dimensional clinical decision complex. Patient A has moderate physical limitation ($d_1 = 0.4$) but intact trust ($d_5 = 0.9$), autonomy ($d_4 = 0.9$), dignity ($d_7 = 0.8$), and understanding ($d_9 = 0.8$). Patient B has better physical function ($d_1 = 0.6$) but degraded trust ($d_5 = 0.2$), coerced autonomy ($d_4 = 0.3$), diminished dignity ($d_7 = 0.3$), and poor understanding ($d_9 = 0.2$). The QALY projection collapses both to the same scalar. The nine-dimensional profiles are radically different, and the clinical geodesic --- the optimal path through the decision space --- differs accordingly.]

## 1.2 The Scalar Menagerie of Clinical Medicine

Medicine has generated a remarkable collection of scalar metrics, each invented to solve a real problem, each capturing something genuine, and each destroying geometric structure that its inventors did not know existed. Sarah will encounter every one of them during her training. Each will tell her something useful. None will tell her enough.

### 1.2.1 The QALY: Quality-Adjusted Life Year

The QALY is the dominant metric in health economics and health technology assessment. Its construction is straightforward:

$$\text{QALY} = \sum_{t=0}^{T} q(t) \cdot \Delta t$$

where $q(t) \in [0, 1]$ is the quality weight at time $t$ (1 = perfect health, 0 = death) and $T$ is the time horizon. The quality weight is typically elicited through standard gamble, time trade-off, or visual analogue scale methods, each of which asks the patient (or a population proxy) to express their health state as a fraction of perfect health.[^1]

The QALY was designed for cost-effectiveness analysis: comparing interventions across different diseases and populations by expressing all health benefits in a common currency. It enabled questions like "Is this cancer drug a better use of NHS funds than that diabetes program?" by translating both into QALYs gained per pound sterling spent. NICE (the National Institute for Health and Care Excellence) adopted a threshold of 20,000--30,000 pounds per QALY gained as the standard for recommending treatments --- a threshold that has shaped healthcare policy for hundreds of millions of people.[^2]

What does the QALY destroy?

**Trajectory.** Two patients can have the same QALY integral --- the same area under the quality-time curve --- with radically different trajectories. Patient A improves steadily from $q = 0.2$ to $q = 0.8$ over two years; Patient B declines from $q = 0.8$ to $q = 0.2$ over the same period. Their QALYs are identical. Their clinical situations are opposite. The patient who is improving needs maintenance and encouragement. The patient who is declining needs reassessment and possibly palliative transition. The integral discards the derivative --- the direction of change --- and the derivative is often more clinically relevant than the integral.

**Comorbidity interaction.** The quality weight is typically assumed to be multiplicative across conditions: a patient with both arthritis ($q = 0.7$) and depression ($q = 0.6$) is assigned $q = 0.42$. But comorbidities interact non-linearly. Depression reduces the patient's capacity to manage arthritis (exercise, medication adherence, social support). Arthritis limits the patient's access to depression treatments (physical activity, social engagement). The interaction term --- the $\Sigma_{ij}$ cross-covariance that the clinical decision complex captures --- is discarded by the multiplicative assumption. The scalar cannot represent interaction because interaction is inherently multi-dimensional: it lives in the off-diagonal entries of the covariance matrix.

**Patient values.** The quality weight is supposed to capture patient preferences, but it compresses all preferences into a single trade-off: health state versus perfect health. A retired philosophy professor with advanced cancer who values intellectual engagement over longevity has different preferences than a young construction worker with chronic pain who values physical function above all else. The QALY assigns them quality weights based on their health states, not their values. The difference between "I want to think clearly even if I die sooner" and "I want to move freely even if I think less clearly" is precisely the information that the scalar projection destroys --- it is the direction in the nine-dimensional value space, not the magnitude, and magnitude is all the scalar preserves.

**Distributional equity.** A QALY is a QALY regardless of who receives it. The QALY framework is explicitly egalitarian at the individual level --- one life-year at quality 0.5 is worth the same whether it accrues to a billionaire or a homeless person. But this apparent fairness conceals a structural inequity: populations with lower baseline quality weights (the elderly, the disabled, those with chronic conditions) generate fewer QALYs from any intervention, and cost-per-QALY thresholds therefore systematically deprioritize them. This is not a bug in the implementation. It is a mathematical consequence of the scalar projection, as the QALY Irrecoverability Theorem (Chapter 5) will prove.

### 1.2.2 The Glasgow Coma Scale

The Glasgow Coma Scale (GCS) was introduced by Teasdale and Jennett in 1974 to provide a standardized assessment of consciousness after traumatic brain injury.[^3] It scores three components --- eye opening (1--4), verbal response (1--5), and motor response (1--6) --- and sums them to produce a total score between 3 (deep coma) and 15 (fully conscious).

The GCS is one of the most widely used clinical scores in medicine. It is fast, reliable, and reproducible. It is also a scalar projection of a three-dimensional assessment, and the projection destroys clinically critical structure.

A GCS of 9 can be decomposed as $E4 + V1 + M4$ (eyes open spontaneously, no verbal response, withdrawal from pain) or $E1 + V3 + M5$ (no eye opening, inappropriate words, localizing to pain). The first pattern suggests a patient with intact arousal but destroyed language function --- possibly a brainstem lesion sparing the reticular activating system. The second suggests a patient with suppressed arousal but partially preserved cortical function --- possibly a metabolic encephalopathy. The prognosis, the diagnostic workup, and the treatment are completely different. The scalar is the same.

The GCS's designers knew this. Teasdale and Jennett explicitly warned against using the total score without the component breakdown. The field heard the warning, adopted the total score, and built triage protocols on it. The scalar was too convenient. The components were too cumbersome. The information was too important to lose and too inconvenient to keep.

### 1.2.3 The APACHE Score

The Acute Physiology and Chronic Health Evaluation (APACHE) system, now in its fourth iteration, predicts ICU mortality from a weighted combination of acute physiologic variables, age, and chronic health status.[^4] APACHE II uses twelve physiologic variables, each scored 0--4 for deviation from normal, plus age and chronic health points, to produce a score from 0 to 71. Higher scores predict higher mortality.

APACHE is useful for case-mix adjustment, benchmarking ICU performance, and research stratification. It is also a scalar compression of a twelve-dimensional physiologic state, and the compression destroys the same kind of information the QALY destroys, only at a different level of abstraction.

Two patients with APACHE II = 22 and predicted mortality of 40 percent can have completely different physiologic profiles: one with isolated respiratory failure (high $\text{PaO}_2$ deviation, normal cardiovascular and renal parameters) and the other with multi-organ dysfunction (moderate deviations across six systems). The first patient needs aggressive respiratory support; the second needs a coordinated multi-system approach. The score cannot distinguish them because the sum discards the pattern.

### 1.2.4 The Emergency Severity Index

The Emergency Severity Index (ESI) is the standard triage system in US emergency departments. It assigns patients to one of five levels based on acuity and expected resource needs: ESI-1 (immediate life-threatening), ESI-2 (high-risk or confused/lethargic/disoriented), ESI-3 (two or more resources needed), ESI-4 (one resource), ESI-5 (no resources).[^5]

The ESI is a five-level ordinal scale --- barely above a binary --- that compresses the full clinical state into a single integer. It is the triage version of the QALY: necessary, useful, and structurally inadequate. Chapter 2 will examine triage in detail as the paradigm case of forced scalar contraction.

### 1.2.5 Patient-Reported Outcome Measures

PROMs (Patient-Reported Outcome Measures) represent an attempt to capture what matters to patients rather than what matters to clinicians or health economists. The EQ-5D, the most widely used PROM for QALY calculation, assesses five dimensions: mobility, self-care, usual activities, pain/discomfort, and anxiety/depression. Each dimension is scored on three or five levels, and the combination is converted to a utility score using population-derived value sets.

The EQ-5D is genuinely multi-dimensional --- five dimensions rather than one. But five is not nine, and the five dimensions of the EQ-5D map onto a subset of $d_1$ (clinical outcomes) with partial coverage of $d_7$ (dignity via self-care) and $d_6$ (social impact via usual activities). Trust ($d_5$), autonomy ($d_4$), justice ($d_3$), epistemic status ($d_9$), institutional legitimacy ($d_8$), and rights ($d_2$) are absent. The EQ-5D is a better map than the QALY, but it is a map of the physical terrain that omits the social, relational, and institutional landscape in which every patient actually lives.

And even the EQ-5D is typically contracted to a scalar --- the utility index --- before being used in policy analysis. The multi-dimensional assessment is gathered and then discarded in the final step. The information is collected, priced, and thrown away.

## 1.3 The Geometry That Scalars Destroy

The previous section catalogued five clinical metrics and their specific losses. A pattern emerges --- the same pattern identified in *Geometric Communication* (Chapter 1) and *Geometric Ethics* (Chapter 16). Each clinical metric destroys one or more of four fundamental geometric structures:

**Metric structure.** The continuous distance between clinical-moral states --- the fact that a patient who trusts their physician is clinically closer to a good outcome than a patient who does not, that a patient who understands their diagnosis is closer to informed consent than a patient who does not. Clinical scoring systems replace this continuous metric with discrete ordinal scales (GCS: integers 3--15) or scalar projections (QALY: real number 0--1) that discard the distance structure between states. Two patients at GCS 9 are treated as equidistant from consciousness, regardless of which components are intact and which are destroyed.

**Cross-dimensional structure.** The interaction between clinical-moral dimensions --- the covariance matrix $\Sigma$ that encodes how trust and outcome interact ($\Sigma_{15}$), how autonomy and understanding co-depend ($\Sigma_{49}$), how justice and dignity conflict ($\Sigma_{37}$). Scalar metrics erase all cross-dimensional information because a single number has no off-diagonal terms. The QALY cannot represent the fact that a treatment with uncertain outcomes ($d_1$) is more costly when the trust relationship is fragile ($d_5$), because representing this requires at least a $2 \times 2$ matrix, and the QALY is a $1 \times 1$ scalar.

**Boundary structure.** The thresholds where clinical-moral regimes change discontinuously --- the consent boundary ($\beta_{\text{consent}}$), the harm boundary ($\beta_{\text{harm}}$), the futility boundary ($\beta_{\text{futile}}$), the abandonment boundary ($\beta_{\text{abandon}}$). Scalar metrics smooth over these boundaries because a single number cannot represent both the position and the proximity to a threshold. The QALY of a patient one day from death and the QALY of a patient in stable chronic illness can be identical, even though one is at the boundary of the futility regime and the other is in the interior of the treatment regime. The boundary is invisible to the scalar.

**Trajectory structure.** The path through clinical-moral space --- the direction of change, the curvature of the trajectory, the sequence of clinical actions that connect the present state to the goal. A scalar is a point; it has no direction, no curvature, no path. The QALY integral averages over time and discards the temporal structure. The GCS is a snapshot that discards all dynamics. The APACHE score is an admission-day cross-section that has no representation of trajectory. Clinical reasoning, by contrast, is fundamentally about trajectory: Where is the patient going? What path will take them to the best accessible outcome? What obstacles lie along the path?

[Figure 1.2: The four geometric structures destroyed by clinical scalar metrics. (a) Metric: continuous clinical-moral distance replaced by ordinal or scalar projection. (b) Cross-dimensional: $\Sigma_{ij}$ covariance between dimensions erased by dimensional collapse. (c) Boundary: clinical-moral thresholds invisible to continuous scalars. (d) Trajectory: temporal path structure discarded by point-in-time or integral summaries.]

These four structures are not peripheral luxuries. They are the mathematical substance of what clinical reasoning *is*. Metric structure is what allows clinicians to judge which patients are "sicker" in the morally relevant sense --- not just physiologically more deranged but further from an acceptable outcome on the full manifold. Cross-dimensional structure is what makes clinical ethics hard --- the reason "balancing autonomy against beneficence" is not like balancing apples against apples but like navigating a space where the dimensions interact, curve into each other, and cannot be traded at fixed exchange rates. Boundary structure is what makes clinical ethics *clinical* --- the thresholds where everything changes, where a competent patient's refusal converts an obligation to treat into a prohibition on treating, where a diagnosis of futility transforms aggressive care from beneficent to harmful. Trajectory structure is what makes clinical reasoning *reasoning* --- a temporal process of navigating from one state to another, not a static evaluation of a single state.

A measurement apparatus that destroys all four is not measuring clinical-moral reality. It is measuring something else --- something correlated with clinical-moral reality, perhaps, but structurally impoverished in exactly the dimensions that matter for the hardest decisions.

## 1.4 The Scalar Irrecoverability Theorem (Preview)

The losses catalogued above are not merely inconvenient. They are mathematically irreversible. This is the content of the Scalar Irrecoverability Theorem, proved in *Geometric Reasoning* (Ch. 13) and here previewed in its clinical form. The full clinical version --- the QALY Irrecoverability Theorem --- is proved in Chapter 5.

**Theorem 1.1 (Scalar Irrecoverability for Clinical Metrics, Preview).** *Let $\mathbf{a} \in \mathbb{R}^9$ be the attribute vector of a patient's clinical-moral state across the nine dimensions of the clinical decision complex. For any scalar projection $Q: \mathbb{R}^9 \to \mathbb{R}$ (including but not limited to QALYs, APACHE scores, and triage indices), there exist clinically and morally distinct states $\mathbf{a}_1$ and $\mathbf{a}_2$ such that $Q(\mathbf{a}_1) = Q(\mathbf{a}_2)$ despite $\mathbf{a}_1$ and $\mathbf{a}_2$ differing on a substantive subset of the nine dimensions. The information destroyed by $Q$ --- namely, the identity of which dimensions are intact and which are compromised --- is not recoverable from $Q(\mathbf{a}_1)$ and $Q(\mathbf{a}_2)$ alone.*

The proof is immediate from the rank-nullity theorem: a function $Q: \mathbb{R}^9 \to \mathbb{R}$ has a kernel of dimension at least 8 at every regular point. This means that for any QALY value, there is an eight-dimensional space of clinical-moral states that map to that same value. Everything in that eight-dimensional space is invisible to the QALY. The information that distinguishes states within the kernel --- the information that tells you whether the patient trusts the physician, understands the diagnosis, has intact dignity, or is being treated justly --- is irrecoverably gone.

The theorem has a sharpened corollary that is particularly devastating for the QALY:

**Corollary 1.1.1 (QALY Discrimination Is Mathematical, Not Moral).** *The well-documented biases of QALY-based allocation against the elderly, the disabled, and minority populations are not failures of implementation. They are mathematical consequences of dimensional collapse. Populations whose health needs are concentrated on non-outcome dimensions ($d_4$: autonomy for disabled patients, $d_5$: trust for minority patients with historical institutional betrayal, $d_7$: dignity for elderly patients) are systematically disadvantaged by any scalar projection that weights $d_1$ (clinical outcomes) most heavily.*

This is not a philosophical argument. It is a theorem. The discrimination is in the dimensionality, not in the calibration. No recalibration of quality weights can fix it, because the problem is not that the weights are wrong but that the weights compress dimensions that should not be compressed. You cannot represent the difference between "I don't trust you because of Tuskegee" and "I trust you completely" in a number that has no trust dimension. You cannot represent the difference between "my dignity requires that I die at home" and "my dignity requires that every possible treatment be tried" in a number that has no dignity dimension. The QALY has no trust dimension. The QALY has no dignity dimension. The QALY has no justice dimension. And so the QALY cannot see --- cannot in principle see --- the moral information that matters most for the populations most vulnerable to healthcare injustice.

[Figure 1.3: Scalar irrecoverability in clinical context. The nine-dimensional clinical-moral state space is projected onto the one-dimensional QALY axis. The preimage of a QALY value $Q = 0.4$ is an eight-dimensional hyperplane. All patients on this hyperplane are indistinguishable to QALY-based allocation. The hyperplane contains patients with radically different trust, autonomy, dignity, justice, and understanding profiles. The information that distinguishes them --- the information needed for equitable, patient-centered care --- is irrecoverable from the scalar.]

## 1.5 What This Costs

The irrecoverability theorem is a mathematical fact. But mathematics does not suffer. Patients do. Clinicians do. Institutions do. The costs of scalar clinical evaluation are concrete, documented, and ongoing.

### 1.5.1 The NICE Threshold and Its Casualties

The National Institute for Health and Care Excellence has used the QALY framework to evaluate health technologies since its establishment in 1999. Its threshold of 20,000--30,000 pounds per QALY gained has determined which treatments are available to sixty-seven million people in England and Wales. The framework has genuine virtues: it brings consistency, transparency, and accountability to resource allocation decisions that would otherwise be made by political negotiation or clinical anarchy. The Geometric framework does not argue that NICE should abandon cost-effectiveness analysis. It argues that NICE should upgrade its dimensionality.

Consider the case of treatments for rare diseases. A drug that extends life by two years for a patient with a rare metabolic disorder has a straightforward QALY calculation. But a drug that extends life by two years for a patient with a rare disease that the patient has spent decades learning to live with --- developing coping strategies, building community, constructing an identity around the condition --- has costs and benefits on $d_4$ (autonomy: the patient's hard-won independence may be disrupted by a new treatment regimen), $d_5$ (trust: the patient may have deep skepticism of a medical system that historically neglected their condition), and $d_7$ (dignity: the condition is part of who they are, not merely something they "have"). The QALY captures only the $d_1$ benefit. The threshold applies to the scalar. The patient's full reality is invisible to the decision.

### 1.5.2 Triage by Numbers

In March 2020, as COVID-19 overwhelmed hospital systems in northern Italy, clinicians faced a triage problem of unprecedented scale. The Italian College of Anesthesia, Analgesia, Resuscitation and Intensive Care (SIAARTI) published emergency guidelines recommending that ICU access be based on "the greater probability of therapeutic success" --- a scalar criterion based on clinical outcomes ($d_1$), modified by a "clinical appropriateness" assessment that functioned as a proxy for remaining life expectancy.[^6]

The guidelines were humane, thoughtful, and produced by physicians under extraordinary pressure. They were also, in the geometric framework, a forced contraction of the nine-dimensional clinical tensor to a one-dimensional survival probability. The contraction discarded justice ($d_3$: the guidelines could produce systematic age-based deprioritization), dignity ($d_7$: patients denied ICU care died alone, without family, in hallway beds), trust ($d_5$: communities that already distrusted the medical system experienced the triage as confirmation of their worst fears), and the clinicians' own moral architecture ($h(n)$: the clinicians who implemented the triage suffered moral injury that persisted long after the pandemic receded).

Chapter 2 examines triage as forced contraction in detail. Chapter 10 develops the geometric triage framework. Here the point is simpler: the scalar triage criterion was not wrong on $d_1$. It was wrong on the manifold. And the costs of being wrong on the manifold were borne by patients who died without dignity, families who were denied closure, and clinicians whose heuristic functions were permanently damaged by the boundaries they were forced to cross.

### 1.5.3 Algorithmic Bias in Clinical Prediction

In 2019, Obermeyer et al. published a landmark study in *Science* demonstrating that a widely used commercial algorithm for identifying patients who need extra care was systematically biased against Black patients.[^7] The algorithm used health costs as a proxy for health needs --- a scalar projection that assumed higher costs correlated with sicker patients. But Black patients, facing barriers to healthcare access, generated lower costs at the same level of illness. The algorithm assigned them lower risk scores, and the lower scores reduced their access to care programs.

In the geometric framework, this is a Bond Invariance Principle violation: the algorithm's evaluation changed when the patient's race changed, even though the underlying clinical-moral state was held constant. The evaluation was not gauge-invariant under patient re-description. Chapter 8 develops the medical BIP in full. Here the point is that the bias was not in the algorithm's logic but in its dimensionality. By projecting clinical need onto a cost scalar, the algorithm inherited every correlation between cost and race, access and socioeconomic status, utilization and trust. The scalar could not separate clinical need from structural injustice because clinical need and structural injustice live on different dimensions of the manifold, and the scalar has only one dimension.

### 1.5.4 The Cost to Clinicians

Perhaps the most profound cost of scalar clinical evaluation is what it does to the clinicians who are forced to implement it. The QALY asks clinicians to evaluate patients as numbers. The triage protocol asks them to sort patients by a single criterion. The institutional guideline asks them to follow a scalar threshold. And the clinicians' own moral architecture --- their nine-dimensional heuristic function $h(n)$, calibrated over years of training and clinical experience --- tells them that the scalar is wrong.

This is not burnout. Burnout is resource depletion: the clinician's cognitive and emotional capacity for computation is exhausted by overwork. What scalar evaluation produces is something structurally different: it forces clinicians to act on a projection they know to be incomplete, to make decisions on one dimension that they know should be made on nine. The resulting damage is not to their computational capacity ($g(n)$) but to their moral architecture ($h(n)$). It is moral injury --- the subject of Chapters 13--15 --- and it is a predictable, measurable, preventable consequence of forcing nine-dimensional clinical reasoning through a one-dimensional evaluation pipe.

Sarah will learn this over the next three years. She will learn it not from a textbook but from the patients whose trust she cannot capture in a score, the families whose grief she cannot represent in a metric, and the quiet damage to her own moral architecture that accumulates with every decision she is forced to make on insufficient dimensions.

## 1.6 The Two-Patient Problem

To make the abstraction concrete, consider the problem that every first-year medical student should be able to solve but that no scalar metric can solve correctly.

**Patient A.** Margaret Okonkwo, 68 years old, retired professor of English literature. Advanced pancreatic cancer, estimated prognosis 6--12 months. Physical function moderately impaired ($d_1 = 0.45$). She is alert, engaged, reading two novels simultaneously, and writing letters to her grandchildren. She understands her diagnosis fully ($d_9 = 0.95$). She trusts her oncologist completely ($d_5 = 0.9$). She has decided, autonomously and with full understanding, that she does not want further chemotherapy; she wants to maximize her cognitive function for her remaining months, even at the cost of survival time ($d_4 = 0.95$). Her dignity is intact ($d_7 = 0.85$). Her family supports her decision ($d_6 = 0.8$).

QALY estimate: approximately 0.35 (moderate quality weight times limited life expectancy).

**Patient B.** David Kowalski, 42 years old, construction worker. Chronic low back pain following a workplace injury three years ago. Physical function significantly impaired ($d_1 = 0.35$). He does not understand the difference between the three treatment options presented to him ($d_9 = 0.3$). He distrusts the workers' compensation system that is paying for his care ($d_5 = 0.25$). He feels coerced into accepting a surgical option by an insurer that will discontinue his benefits if he "refuses appropriate treatment" ($d_4 = 0.3$). He has lost his sense of himself as a provider and a physical person ($d_7 = 0.3$). His marriage is strained by the injury ($d_6 = 0.35$). He signed the surgical consent form because he felt he had no choice.

QALY estimate: approximately 0.35 (moderate quality weight times substantial life expectancy, discounted by disability weight).

The QALY-optimal treatment for Patient A is further chemotherapy (maximizes expected QALYs). The QALY-optimal treatment for Patient B is surgery (maximizes expected QALYs through functional restoration).

The manifold-optimal treatment for Patient A is palliative care focused on cognitive preservation --- because on the full nine-dimensional manifold, the path through further chemotherapy crosses the patient's explicitly stated value boundary ($d_4$: she has chosen quality over quantity, and that choice is informed and autonomous) at a cost that exceeds any $d_1$ benefit. The clinical geodesic respects the refusal and optimizes the five months, not the twelve.

The manifold-optimal treatment for Patient B is not surgery --- not yet. It is, first, a series of clinical actions on the non-$d_1$ dimensions: a health literacy intervention ($d_9$), a conversation about genuine options without coercion ($d_4$), an effort to build trust ($d_5$), and a referral to a social worker for the marital strain ($d_6$). Only after these dimensions are addressed can the surgical decision be genuinely informed. The patient's consent is currently gauge-variant: if you described the surgery as "a 70 percent chance of significant improvement" and then redescribed it as "a 30 percent chance of no improvement or worsening," his decision would change, because he does not genuinely understand the options. The consent form is legally valid. It is ethically vacuous.

The QALY says: same number, same treatment priority.

The manifold says: different patients, different dimensions, different geodesics, different urgencies, different ethical obligations. And the information that distinguishes them --- trust, understanding, autonomy, dignity, social context --- is exactly the information that the QALY, by mathematical necessity, has destroyed.

[Figure 1.4: The two-patient problem. Patient A and Patient B have identical QALY projections (0.35) but radically different nine-dimensional attribute vectors. Patient A's needs are concentrated on $d_1$ (outcomes, via palliative optimization) with intact non-$d_1$ dimensions. Patient B's needs are concentrated on $d_4$ (autonomy), $d_5$ (trust), $d_7$ (dignity), and $d_9$ (understanding), with $d_1$ treatment contingent on resolving these dimensions first. The clinical geodesics diverge immediately from the start node.]

## 1.7 Why Not Just Use Multiple Metrics?

The natural response to scalar irrecoverability is: use multiple metrics. Report the EQ-5D dimensions separately. Track the GCS components individually. Add patient satisfaction scores, trust measures, and health literacy assessments alongside the QALY.

This response is correct in spirit and insufficient in practice, for three reasons.

**First, multiple scalars are not a manifold.** Five separate scores --- one for each EQ-5D dimension --- do not capture the interaction between dimensions. The covariance matrix $\Sigma$ has 36 off-diagonal entries (for a $9 \times 9$ matrix), and each entry encodes a clinically meaningful interaction: how trust affects the cost of uncertain outcomes ($\Sigma_{15}$), how autonomy depends on understanding ($\Sigma_{49}$), how justice and dignity trade off in allocation decisions ($\Sigma_{37}$). A list of scores discards all interaction terms. The manifold includes them.

**Second, multiple scalars have no decision algorithm.** When the five EQ-5D dimensions point in different directions --- when mobility improves but anxiety worsens, when self-care is preserved but usual activities are restricted --- how does the clinician decide? Principlism says "balance." Health economics says "convert to a utility score" (i.e., contract back to a scalar). The clinical decision complex provides the decision algorithm: pathfinding on the full manifold, with edge weights that incorporate the cross-dimensional costs and boundary penalties that determine which path is optimal.

**Third, the final contraction always happens.** Even when multiple dimensions are measured, the decision point forces a contraction. The NICE committee must decide: fund or not fund. The triage nurse must decide: ESI-1 or ESI-2. The clinician must decide: treat or do not treat. The question is not whether to contract but how --- and the geometric framework provides the mathematics of optimal contraction: contraction that minimizes information loss and preserves the distinctions that matter most for the specific decision at hand.

The Scalar Irrecoverability Theorem does not say that scalars are useless. It says that scalars are lossy, that the loss is irrecoverable from the scalar alone, and that the consequences of the loss fall disproportionately on the patients and clinicians least able to absorb them. The clinical decision complex does not abolish scalar decision-making. It provides the structure from which scalar decisions can be derived --- the nine-dimensional manifold from which any scalar projection can be computed, and on which the projection's information loss can be measured, understood, and managed.

## 1.8 What This Book Does

This book constructs the missing mathematics of clinical ethics. It does so in six steps, each corresponding to a major result:

**The clinical decision complex** (Chapter 4). A nine-dimensional weighted simplicial complex on which clinical decisions are pathfinding problems. Vertices are clinical states carrying nine-dimensional attribute vectors. Edges are clinical actions carrying Mahalanobis-distance costs plus boundary penalties. Higher simplices are care bundles that must be evaluated jointly.

**The QALY Irrecoverability Theorem** (Chapter 5). The domain-specific Scalar Irrecoverability Theorem, proved in full: any scalar QALY function $Q: \mathbb{R}^9 \to \mathbb{R}$ is non-injective, its information loss is irrecoverable, and the QALY-maximizing path diverges from the clinical geodesic by an unbounded amount. The theorem establishes that QALY discrimination against elderly, disabled, and minority populations is mathematical, not moral.

**Clinical A* pathfinding** (Chapter 6). The computational architecture of clinical decision-making: $f(n) = g(n) + h(n)$, where $g(n)$ is the accumulated clinical cost (evidence-based medicine) and $h(n)$ is the moral-heuristic estimate (clinical wisdom). The minimum-cost path on the full manifold is the clinical geodesic --- the recommended plan of care.

**The heuristic admissibility spectrum** (Chapter 7). What makes clinical judgment good, bad, damaged, or biased, characterized as a four-level hierarchy of heuristic quality: strictly admissible, $\varepsilon$-admissible, inadmissible, and gauge-variant. Medical training is heuristic calibration. Ethics consultation is heuristic recalibration.

**Informed consent as gauge invariance** (Chapter 8). Valid consent is equivalent to a gauge-invariance condition: the patient's decision must survive meaning-preserving reframing. If "90% survival" and "10% mortality" produce different decisions, consent is not genuinely informed --- regardless of what the form says.

**The clinical Bond Index** (Chapter 12). A quantitative measure of structural healthcare injustice: the expected deviation between the clinical geodesic and the path mandated by institutional policy, stratified by patient population. Structural injustice becomes an empirical claim with a numerical value, not a philosophical opinion.

Along the way, the book develops the mathematical theory of moral injury (Chapters 13--15), the geometric theory of triage (Chapters 10--11), and the application of the framework to pandemic response, organ transplant allocation, and AI-assisted clinical reasoning (Chapters 10--11, 16). Every construction is grounded in the formal definitions and theorems of the GCE paper, submitted to the *Journal of Medical Ethics*. Every claim generates falsifiable predictions (Chapter 17) that differ from predictions of standard bioethics and QALY-based health economics.

## 1.9 The Plan of the Book

The book proceeds in six parts.

**Part I (Chapters 1--3)** establishes the problem and its history. Chapter 2 examines triage as the paradigm case of forced contraction --- the medical analogue of moral contraction from *Geometric Ethics* (Ch. 15). Chapter 3 traces the geometric intuitions buried in twenty-five centuries of medical ethics, from the Hippocratic Oath (a boundary condition) through Beauchamp and Childress (four dimensions) through narrative ethics (the humanistic protest against scalar reduction), showing that each tradition captures part of the manifold without the vocabulary to name the whole.

**Part II (Chapters 4--8)** constructs the framework. Chapter 4 builds the clinical decision complex --- the nine-dimensional weighted simplicial complex that is the domain-specific manifold for this book. Chapter 5 proves the QALY Irrecoverability Theorem. Chapter 6 develops Clinical A* pathfinding. Chapter 7 characterizes the heuristic admissibility spectrum. Chapter 8 formalizes informed consent as gauge invariance.

**Part III (Chapter 9)** applies the framework to the cases that define clinical ethics: the competent patient who refuses life-saving treatment, withdrawing life support, psychiatric involuntary treatment, proxy decision-making, and deep brain stimulation and identity.

**Part IV (Chapters 10--12)** addresses the ethics of allocation: pandemic triage as manifold allocation, vaccine and organ transplant distribution, and the clinical Bond Index as a measure of structural healthcare injustice.

**Part V (Chapters 13--15)** develops the mathematical theory of moral injury: what it is (heuristic damage, not burnout), how it accumulates, and how institutions can prevent and repair it.

**Part VI (Chapters 16--18)** looks forward: AI in clinical reasoning, measuring the clinical metric empirically, and the open questions that the framework cannot yet answer.

A single thread runs through the book: the clinical life of Dr. Sarah Chen. We met her in this chapter, presenting her first patient with a QALY and learning that the number was not the patient. We will follow her through diagnosis, treatment planning, informed consent conversations, pandemic triage, moral injury, and institutional reform. Her trajectory --- from naive scalar ethics through geometric awakening to institutional action --- is the book's argument made personal.

The mathematics starts in Chapter 4. The motivation starts here. And the motivation is simple: a patient is not a number. A clinician is not a calculator. And the gap between what clinical ethics knows and what clinical metrics can express has consequences measured not in decimals but in lives, trust, dignity, and the quiet accumulation of moral damage in the people who have dedicated their careers to healing.

The manifold exists. The clinicians are already pathfinding on it. Now there is a mathematics for what they do.

---

## Summary

This chapter has argued that clinical medicine evaluates patients and clinical decisions by scalar metrics --- QALYs, APACHE scores, Glasgow Coma Scale, Emergency Severity Index, and patient-reported outcome measures --- that systematically destroy the geometric structure of clinical-moral reality. Each metric collapses a nine-dimensional clinical-moral state into a scalar, and the collapse is irreversible: the Scalar Irrecoverability Theorem proves that no scalar projection can preserve the full structure of the clinical-moral state space. What is lost includes metric structure (continuous clinical-moral distance), cross-dimensional structure (the covariance between dimensions that makes clinical ethics hard), boundary structure (the thresholds where clinical-moral regimes change), and trajectory structure (the path through clinical-moral space that constitutes clinical reasoning).

The costs are not theoretical. They manifest as QALY-based policies that systematically disadvantage the elderly, the disabled, and minority populations; triage protocols that discard justice, dignity, and trust in the name of outcome maximization; algorithmic bias that inherits structural injustice through dimensional collapse; and moral injury in clinicians forced to act on one dimension when they know they should act on nine.

The alternative is geometric clinical evaluation: reasoning on the clinical decision complex --- the nine-dimensional weighted simplicial complex where clinical-moral reality lives --- with tools that preserve the structure that scalars destroy. The book develops these tools and validates them against the full range of clinical ethics, from bedside decisions to pandemic response to institutional policy design.

The argument begins, in Chapter 2, with the oldest and most urgent form of scalar clinical evaluation: triage.

---

[^1]: Weinstein, M. C., & Stason, W. B. (1977). Foundations of cost-effectiveness analysis for health and medical practices. *New England Journal of Medicine*, 296(13), 716--721. The paper has been cited over 5,000 times and remains the foundational reference for QALY methodology.

[^2]: National Institute for Health and Care Excellence. (2013). Guide to the methods of technology appraisal 2013. NICE Process and Methods Guides, London. The threshold has been debated extensively; see Claxton et al. (2015) for an empirical estimate suggesting the true threshold may be closer to 13,000 pounds per QALY.

[^3]: Teasdale, G., & Jennett, B. (1974). Assessment of coma and impaired consciousness: A practical scale. *The Lancet*, 304(7872), 81--84. The GCS has been cited over 10,000 times and is used in virtually every emergency department and trauma center worldwide.

[^4]: Knaus, W. A., Draper, E. A., Wagner, D. P., & Zimmerman, J. E. (1985). APACHE II: A severity of disease classification system. *Critical Care Medicine*, 13(10), 818--829.

[^5]: Gilboy, N., Tanabe, T., Travers, D., & Rosenau, A. M. (2011). Emergency Severity Index (ESI): A Triage Tool for Emergency Department Care. Version 4, AHRQ Publication No. 12-0014.

[^6]: Vergano, M., Bertolini, G., Giannini, A., Gristina, G. R., Livigni, S., Mistraletti, G., Riccioni, L., & Petrini, F. (2020). Clinical ethics recommendations for the allocation of intensive care treatments in exceptional, resource-limited circumstances. *Minerva Anestesiologica*, 86(5), 469--472.

[^7]: Obermeyer, Z., Powers, B., Vogeli, C., & Mullainathan, S. (2019). Dissecting racial bias in an algorithm used to manage the health of populations. *Science*, 366(6464), 447--453. The study found that at any given risk score, Black patients were considerably sicker than White patients, and the algorithm reduced the number of Black patients identified for extra care by more than half.
