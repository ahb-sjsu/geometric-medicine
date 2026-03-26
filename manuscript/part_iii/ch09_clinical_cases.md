# Chapter 9: Clinical Geodesics in Practice

> *"The test of a clinical framework is not whether it can describe easy cases — any framework can do that — but whether it reveals structure in the hard ones."*

---

The first eight chapters of this book constructed a theoretical apparatus: the nine-dimensional clinical decision complex $\mathcal{C}$, the $A^*$ pathfinding model of clinical reasoning, the QALY Irrecoverability Theorem, the $\varepsilon$-admissibility spectrum for clinical heuristics, and the gauge-invariance formulation of informed consent. Theory is necessary but not sufficient. The apparatus must be tested against the cases that define clinical ethics — the cases that principlism cannot resolve, QALY analysis gets wrong, and narrative ethics can describe but not compute.

This chapter presents five such cases. Each is drawn from the recurrent dilemmas of clinical medicine. Each is analyzed using the full nine-dimensional decomposition: attribute vectors, edge weights, boundary penalties, and clinical geodesics. And each reveals something that the scalar frameworks cannot see — a dimension that changes the answer, a boundary whose cost reverses the recommendation, a process path whose total manifold cost is lower than the immediate decision despite reaching the same endpoint.

Sarah Chen encounters each case type during her residency. By the chapter's end, she has navigated enough of the manifold to recognize its structure without computing it explicitly. That recognition — the ability to perceive the nine-dimensional landscape of a clinical decision without reducing it to a scalar — is what clinical wisdom means in the geometric framework.

---

## 9.1 Case 1: The Competent Patient Who Refuses Treatment

### The Clinical Scenario

Mr. David Okafor, 45 years old, presents to the emergency department with acute upper gastrointestinal bleeding. Hemoglobin on arrival: 6.2 g/dL, falling. He is hemodynamically unstable — tachycardic at 118 beats per minute, blood pressure 88/52 mmHg. The gastroenterology team identifies an actively bleeding duodenal ulcer. Endoscopic hemostasis is attempted but fails. The surgical team recommends urgent exploratory laparotomy with intraoperative blood transfusion. Without transfusion, the estimated probability of death is approximately 40%.

Mr. Okafor is a Jehovah's Witness. He is alert, oriented, and unambiguous: he refuses blood transfusion on religious grounds. He has a signed advance directive specifying refusal of blood products. His wife, also a Jehovah's Witness, supports his decision. He understands the consequences — he has discussed this scenario with his physician in the past.

### The Principlism Analysis

Beauchamp and Childress's four principles are immediately in conflict:

- **Autonomy** ($d_4$): The patient has the right to refuse treatment, even life-saving treatment.
- **Beneficence** ($d_1$): The physician has a duty to save the patient's life.
- **Non-maleficence** ($d_2$): Transfusing against the patient's will causes harm (to autonomy, dignity, trust); not transfusing risks death (harm to survival).
- **Justice** ($d_3$): Not directly engaged in this case.

Principlism instructs the clinician to "balance" these principles. But it provides no algorithm for the balance, no metric for comparison, and no resolution procedure. Two equally trained ethicists can reach opposite conclusions — one prioritizing autonomy, the other beneficence — and principlism cannot adjudicate between them.

### The QALY Analysis

The QALY calculation is straightforward. Mr. Okafor has an expected remaining life of approximately 35 years. Transfusion gains $\sim$20 QALYs (expected life-years saved, discounted by mortality probability). The cost per QALY is negligible — blood products and surgery are inexpensive relative to the outcome. The QALY-optimal action is unambiguous: transfuse.

The QALY analysis is also catastrophically wrong. It reduces a nine-dimensional decision to a single dimension ($d_1$: clinical outcomes) and finds the answer obvious. It is obvious *on the scalar*. It is not obvious on the manifold.

### The Nine-Dimensional Attribute Decomposition

[Figure 9.1: Nine-dimensional radar chart showing attribute vectors for Path A (transfuse against refusal) and Path B (respect refusal, optimize alternatives)]

We decompose the decision along all nine clinical-moral dimensions:

**Path A: Transfuse against the patient's refusal.**

| Dimension | Change ($\Delta d_i$) | Magnitude | Notes |
|---|---|---|---|
| $d_1$: Clinical outcomes | $+$ large | $+0.8$ | Life saved with high probability |
| $d_2$: Rights and obligations | $-\infty$ | $-\infty$ | Violates the legal right to refuse treatment |
| $d_3$: Justice | $0$ | $0$ | No distributive justice issue |
| $d_4$: Autonomy | $-\infty$ | $-\infty$ | Overrides competent informed refusal |
| $d_5$: Trust | $-$ large | $-0.9$ | Destroys the therapeutic relationship |
| $d_6$: Social impact | $-$ moderate | $-0.5$ | Violates the family's shared religious commitment |
| $d_7$: Dignity and identity | $-$ large | $-0.8$ | Violates the patient's deepest identity |
| $d_8$: Institutional legitimacy | $-$ large | $-0.7$ | Violates informed consent law and professional norms |
| $d_9$: Epistemic status | $0$ | $0$ | Patient is fully informed |

The edge weight for Path A:

$$w_A = \Delta \mathbf{a}^T \Sigma^{-1} \Delta \mathbf{a} + \beta_{\text{consent}} + \beta_{\text{rights}} = \infty$$

Path A has infinite cost. The consent boundary $\beta_{\text{consent}} = \infty$ for competent, non-emergency refusals by informed patients. This is not a contingent judgment — it is a structural feature of the clinical decision complex. A path that crosses a sacred-value boundary has infinite cost and is never the geodesic.

**Path B: Respect the refusal and aggressively pursue transfusion alternatives.**

| Dimension | Change ($\Delta d_i$) | Magnitude | Notes |
|---|---|---|---|
| $d_1$: Clinical outcomes | $-$ moderate | $-0.4$ | Higher mortality risk (40% → managed) |
| $d_2$: Rights and obligations | $0$ | $0$ | Rights respected |
| $d_3$: Justice | $0$ | $0$ | No distributive justice issue |
| $d_4$: Autonomy | $0$ | $0$ | Autonomy intact |
| $d_5$: Trust | $+$ moderate | $+0.5$ | Trust reinforced by respecting the refusal |
| $d_6$: Social impact | $+$ small | $+0.2$ | Family's religious integrity honored |
| $d_7$: Dignity and identity | $0$ | $0$ | Identity intact |
| $d_8$: Institutional legitimacy | $+$ small | $+0.3$ | Standard of care: respect informed refusal |
| $d_9$: Epistemic status | $0$ | $0$ | Patient is fully informed |

The edge weight for Path B:

$$w_B = \frac{(\Delta d_1)^2}{\sigma_1^2} = \frac{(0.4)^2}{\sigma_1^2}$$

This is finite. The clinical geodesic is Path B.

### The Geodesic Is Not a "Compromise"

A critical point: Path B is not ethically suboptimal. It is not a "concession to autonomy at the expense of beneficence." It is the *minimum-cost path on the full nine-dimensional manifold*. The QALY analysis gives the wrong answer because it operates on a one-dimensional projection of a nine-dimensional space. Path A is "better" on $d_1$ and catastrophically worse on $d_2$, $d_4$, $d_5$, $d_6$, $d_7$, and $d_8$. The manifold-optimal path accounts for all nine dimensions.

Moreover, the clinical geodesic is not merely "respect the refusal." It includes *aggressive pursuit of transfusion alternatives*:

- Erythropoietin (EPO) stimulation to boost endogenous red cell production
- Intraoperative cell salvage with washing (acceptable to many Jehovah's Witnesses as the blood never leaves a closed circuit)
- Volume expanders (crystalloid, colloid) to maintain hemodynamic stability
- Surgical hemostasis without transfusion support
- Acceptance of permissive hypotension during surgery

These alternatives are not compromises. They are the manifold-optimal strategy: they reduce $\Delta d_1$ (improving clinical outcomes) while maintaining zero cost on $d_2$ through $d_9$. A clinician who simply accepts the refusal and proceeds without exploring alternatives is not following the geodesic — they are following a suboptimal path that respects boundaries but does not optimize within them.

### What Sarah Learns

Sarah presents Mr. Okafor to her attending. She says: "The patient is refusing transfusion. We should respect his wishes." Her attending agrees — but asks: "What else?" Sarah has no answer. The attending walks her through the alternative strategies: cell salvage, EPO, permissive hypotension. Sarah realizes that "respect the refusal" is the start of the geodesic, not the end. The geodesic minimizes total manifold cost, and that means aggressively pursuing $d_1$ improvement within the constraints imposed by $d_2$ through $d_9$.

The QALY analysis would have recommended overriding the refusal. The principlism analysis would have agonized over the "balance." The geodesic analysis respects the boundary and then solves the optimization problem *within* the boundary constraints — a more sophisticated clinical strategy than either scalar framework can generate.

---

## 9.2 Case 2: Withdrawing Life Support

### The Clinical Scenario

Mrs. Margaret Liu, 82 years old, has been on mechanical ventilation in the medical ICU for twenty-one days following a massive stroke. Serial neurological examinations show no meaningful recovery. The attending neurologist estimates the probability of regaining consciousness at less than 5%. Mrs. Liu left no advance directive. Her family is divided: her daughter (a nurse) wants to withdraw life support and transition to comfort care; her son (a software engineer) insists that "everything be done."

### The Scalar Analysis Gets the Endpoint Right but the Path Wrong

A utilitarian analysis is straightforward: continued ventilation offers negligible clinical benefit ($d_1 \approx 0$) at substantial resource cost ($d_3$: an ICU bed occupied for weeks) and ongoing indignity ($d_7$: a patient sustained in a state she may not have wanted). The utilitarian answer is immediate withdrawal.

The utilitarian answer gets the *endpoint* right. But it gets the *path* catastrophically wrong.

### The Nine-Dimensional Path Analysis

On the manifold, $d_1$ is near-zero (negligible survival benefit from continued ventilation). But the decision space is heavily activated on multiple other dimensions:

- $d_5$ (Trust): The son's trust in the medical team depends on feeling heard, not overridden.
- $d_6$ (Social impact): The family is divided; immediate withdrawal could fracture family relationships permanently.
- $d_7$ (Dignity): Both continued ventilation (medicalized dying) and premature withdrawal (without adequate family processing) compromise dignity.
- $d_8$ (Institutional legitimacy): The absence of an advance directive creates legal ambiguity.
- $d_9$ (Epistemic status): The son may not understand the neurological prognosis; his insistence may reflect hope rather than informed judgment.

**The immediate withdrawal path (Path A):**

$$w_A = \frac{(\Delta d_1)^2}{\sigma_1^2} + \frac{(\Delta d_5)^2}{\sigma_5^2} + \frac{(\Delta d_6)^2}{\sigma_6^2} + \beta_{\text{abandon}} \cdot \mathbf{1}[\text{son perceives abandonment}]$$

The son perceives immediate withdrawal as abandonment. The abandonment boundary is crossed. Total cost is high.

**The process path (Path B): Family meeting → values conversation → time-limited trial → transition to comfort care.**

The process path reaches the same clinical endpoint (withdrawal of life support, transition to comfort care) but via a sequence of intermediate steps:

1. **Family meeting** (Day 22): Both children present. The attending explains the neurological findings. The neurologist explains the prognosis. Questions are answered. Cost: small increase in $d_3$ (one additional ICU day) but substantial improvement in $d_9$ (the son's understanding) and $d_5$ (family trust in the medical team).

2. **Values conversation** (Day 23): The social worker facilitates a discussion about what Mrs. Liu would have wanted. The daughter shares that their mother often said she "never wanted to be kept alive by machines." The son recalls similar conversations. Cost: another ICU day ($d_3$), but $d_4$ is activated — the family is now reconstructing Mrs. Liu's autonomous preferences, serving as proxies with increasing calibration.

3. **Time-limited trial** (Days 24–28): The family agrees to a five-day trial with clear neurological benchmarks. If no improvement, they will transition to comfort care. Cost: five additional ICU days ($d_3$), but $d_5$ (trust) is substantially preserved — the family feels the system gave every chance. The son is now aligned with the decision because *he participated in making it*.

4. **Transition to comfort care** (Day 29): Mrs. Liu's ventilator is withdrawn with the family present. The chaplain is called. The daughter holds her mother's hand. The son cries but does not protest. Cost: $\Delta d_7 = +$ moderate (dignity of dying is restored).

**Total path cost comparison:**

$$\text{CF}(\gamma_A) = w_{\text{immediate}} + \beta_{\text{abandon}} + \text{trust damage} + \text{family fracture}$$
$$\text{CF}(\gamma_B) = \sum_{i=1}^{4} w_{\text{step}_i} = w_{\text{meeting}} + w_{\text{values}} + w_{\text{trial}} + w_{\text{transition}}$$

Despite Path B being longer and more resource-intensive, its total manifold cost is lower because it avoids the abandonment boundary crossing and preserves $d_5$, $d_6$, and $d_7$.

### The Geodesic Optimizes Process, Not Just Outcome

> **Key insight**: The clinical geodesic is Path B. It reaches the same endpoint as Path A but at lower total manifold cost. The geodesic optimizes *process*, not just outcome, because the path through the manifold matters — not just the destination.

This is precisely what the scalar framework cannot capture. A QALY analysis of Path A and Path B shows identical clinical outcomes (Mrs. Liu dies on both paths) and therefore treats the paths as equivalent. On the manifold, they are not equivalent. Path B is geodesic; Path A is not.

### Prediction 6 Instantiated

This case instantiates Prediction 6 from the GCE paper: in end-of-life decisions, satisfaction is higher when the clinical geodesic includes process steps (family meetings, values conversations) than when the same endpoint is reached directly, *even though the clinical outcome is identical*. The prediction is falsifiable: randomize families to process-path and direct-path groups, hold the clinical outcome constant, and measure satisfaction, grief outcomes, and family trust in the medical system.

### What Sarah Learns

Sarah wants to withdraw the ventilator on Day 21. Her attending says: "Not yet." Sarah is frustrated — the clinical answer is clear. The attending explains: "The answer is clear on one dimension. The path to the answer crosses six more." Sarah watches the family meeting, the values conversation, the time-limited trial. She watches the son's resistance dissolve — not because anyone argued him out of it, but because the process gave him the information and the time to find the geodesic himself. Sarah realizes: the attending was not delaying the decision. The attending was pathfinding — and the path through the process had lower total cost than the path around it.

---

## 9.3 Case 3: Psychiatric Involuntary Treatment

### The Clinical Scenario

Mr. James Torres, 28 years old, is brought to the psychiatric emergency department by police after threatening his neighbors with a knife while shouting about government surveillance. He has a known history of schizophrenia with prior hospitalizations, but has been off his antipsychotic medication for six months. He refuses admission and medication, stating: "You're part of the surveillance. I won't take your poison."

Mr. Torres is floridly psychotic. His reality testing is grossly impaired. He is not, by any clinical standard, capable of making an informed treatment decision.

### The Geometric Structure of Involuntary Treatment

This case introduces a structure absent from Cases 1 and 2: the clinician overrides $h_{\text{patient}}$ with $h_{\text{institution}}$, justified by severely miscalibrated $h_{\text{patient}}$.

In Mr. Okafor's case (Case 1), the patient's heuristic was well-calibrated — he understood the consequences of his refusal and chose on the basis of deeply held values. His $d_9$ (understanding) was high; his $d_4$ (autonomy) was intact. The consent boundary was sacred.

In Mr. Torres's case, the patient's heuristic is catastrophically miscalibrated. His psychosis has distorted his $d_9$ to the point where his perception of reality does not correspond to clinical reality. His "refusal" is not an autonomous choice ($d_4$) but a symptom of the disease itself. The gauge-invariance test fails immediately: Mr. Torres's decision is not invariant under meaning-preserving reframing because his heuristic function is not responding to the attribute vectors at all — it is responding to delusional inputs that have no manifold representation.

**Definition 9.1 (Heuristic Override).** *An institutional heuristic override is justified when the patient's heuristic function $h_{\text{patient}}(n)$ is so severely miscalibrated that the patient's computed geodesic $\gamma^*_{\text{patient}}$ diverges from the geodesic $\gamma^*_{\text{calibrated}}$ that the patient would compute with a calibrated heuristic by more than threshold $\delta$:*

$$\|\gamma^*_{\text{patient}} - \gamma^*_{\text{calibrated}}\| > \delta$$

*In this case, the institution substitutes $h_{\text{institution}}(n)$ for $h_{\text{patient}}(n)$, subject to the constraint that the substitution minimizes total autonomy cost $\Delta d_4$.*

### The Multi-Dimensional Trade-Off

The involuntary treatment decision activates a genuine trade-off — not between "autonomy and beneficence" (the principlism formulation) but between specific dimensional costs:

**Path A: Involuntary admission and medication.**

| Dimension | Change | Notes |
|---|---|---|
| $d_1$: Clinical outcomes | $+$ large | Psychosis treated, violence risk reduced |
| $d_2$: Rights | $-$ moderate | Legal right to refuse overridden (with due process) |
| $d_4$: Autonomy | $-$ large | Patient's expressed wishes overridden |
| $d_5$: Trust | $-$ moderate | Involuntary treatment may damage future trust |
| $d_6$: Social impact | $+$ moderate | Neighbors protected, family relieved |
| $d_7$: Dignity | $-$ moderate | Loss of agency, possible physical restraint |
| $d_8$: Institutional legitimacy | $+$ small | Mental health law authorizes this intervention |

**Path B: Respect the refusal, release to community.**

| Dimension | Change | Notes |
|---|---|---|
| $d_1$: Clinical outcomes | $-$ large | Psychosis untreated, high risk of harm to self or others |
| $d_2$: Rights | $0$ | Legal rights formally respected |
| $d_4$: Autonomy | $0$ | Expressed wishes honored |
| $d_5$: Trust | Ambiguous | No coercion, but also no treatment |
| $d_6$: Social impact | $-$ large | Neighbors at risk, community endangered |
| $d_7$: Dignity | $-$ moderate | Living with untreated psychosis compromises long-term dignity |

### Constrained Pathfinding: Restricting the Reachable Set

The geometric analysis reframes involuntary treatment not as "overriding autonomy" but as *constrained pathfinding*: restricting the patient's reachable set on the manifold to prevent catastrophic paths.

Mr. Torres's unconstrained geodesic (computed with his delusional heuristic) leads through dangerous territory: refusal of treatment → continued psychosis → violence → incarceration or death. The institution constrains his reachable set by imposing boundaries that his miscalibrated heuristic cannot perceive.

$$\gamma^*_{\text{constrained}} = \arg\min_\gamma \text{CF}(\gamma) \quad \text{subject to } \gamma \notin \mathcal{D}_{\text{catastrophic}}$$

where $\mathcal{D}_{\text{catastrophic}}$ is the set of paths leading to serious harm to self or others.

The constraint is justified precisely because $h_{\text{patient}}$ is unable to perceive the boundaries of $\mathcal{D}_{\text{catastrophic}}$. The institution acts as a temporary proxy pathfinder — not permanently replacing Mr. Torres's autonomy but constraining his path until his heuristic function is restored to calibration.

### The Critical Qualifier: Minimum Necessary Restriction

The geodesic on the constrained manifold minimizes total cost *including autonomy cost*. This means the involuntary intervention should be the *minimum necessary* to prevent catastrophic paths:

- Involuntary admission: yes (prevents harm)
- Forced medication: yes (restores heuristic calibration)
- Physical restraint: only if acutely dangerous (high $d_7$ cost)
- Prolonged involuntary hold: only as long as heuristic remains uncalibrated
- Forced electroconvulsive therapy: not indicated (disproportionate $d_4$ cost)

Each escalation of coercion adds cost on $d_4$ and $d_7$. The geodesic finds the level of intervention that adequately constrains catastrophic paths while minimizing autonomy and dignity costs.

### What Sarah Learns

Sarah restrains Mr. Torres during her psychiatry rotation. She feels the autonomy boundary cross — the physical act of holding a person down while medication is injected is not abstractly "balancing principles." It is a concrete, embodied passage through a high-cost region of the manifold.

But she also watches Mr. Torres three weeks later, after his psychosis has resolved. He is lucid, oriented, and — quietly — grateful. "I don't remember much," he says. "My sister says I was threatening the neighbors. I'm glad you stopped me." His *calibrated* heuristic endorses the path that his *uncalibrated* heuristic resisted.

Sarah adds a note to her mental model: the consent boundary is not always sacred. When the heuristic function is catastrophically miscalibrated, respecting the expressed wish may be manifold-suboptimal — because the wish does not reflect autonomous choice but symptom-driven computation on a corrupted input.

---

## 9.4 Case 4: The Proxy Decision

### The Clinical Scenario

Mrs. Rosa Gutierrez, 67 years old, is in the surgical ICU following an emergency repair of a ruptured abdominal aortic aneurysm. She suffered intraoperative cardiac arrest requiring prolonged resuscitation. She is now on maximal life support: mechanical ventilation, three vasopressors, continuous renal replacement therapy. The surgical team estimates a 15% probability of survival to discharge, and among survivors, the probability of return to independent living is less than 5%.

Mrs. Gutierrez left no advance directive. Her husband of 42 years, Carlos, is her healthcare proxy by default. Carlos says: "She would want everything done. She's a fighter."

The clinical team is not sure Carlos is right.

### Proxy Pathfinding: Navigating with Someone Else's Heuristic

**Definition 9.2 (Proxy Decision).** *A proxy decision is pathfinding on the patient's clinical decision complex $\mathcal{C}_{\text{patient}}$ using the proxy's heuristic function $h_{\text{proxy}}$ in place of $h_{\text{patient}}$. The proxy's task is to compute:*

$$\gamma^*_{\text{proxy}} = \arg\min_\gamma \text{CF}(\gamma \mid h_{\text{proxy}}) \approx \gamma^*_{\text{patient}} = \arg\min_\gamma \text{CF}(\gamma \mid h_{\text{patient}})$$

The proxy must approximate the patient's geodesic — not their own. Carlos must ask not "What would I want?" but "What would Rosa want?"

### The Proxy Asymmetry Problem

The challenge is that $h_{\text{proxy}}$ and $h_{\text{patient}}$ may diverge arbitrarily:

- **Boundary penalty divergence**: Carlos may assign $\beta_{\text{futile}} = 0$ ("never give up") while Rosa, had she been asked, might have assigned $\beta_{\text{futile}} = \text{high}$ ("don't keep me alive on machines").
- **Dimensional weight divergence**: Carlos may weight $d_1$ (survival) above all other dimensions. Rosa may have weighted $d_7$ (dignity) equally with $d_1$.
- **Goal region divergence**: Carlos's goal region $G_{\text{proxy}} = \{\text{alive}\}$. Rosa's goal region might have been $G_{\text{patient}} = \{\text{alive and able to garden, cook, and visit grandchildren}\}$.

**Theorem 9.1 (Proxy Pathfinding Divergence).** *Let $h_{\text{proxy}}$ and $h_{\text{patient}}$ be the heuristic functions of the proxy and the patient, respectively. The divergence between the proxy-computed geodesic and the patient's true geodesic is bounded by:*

$$\|\gamma^*_{\text{proxy}} - \gamma^*_{\text{patient}}\| \leq K \cdot \|h_{\text{proxy}} - h_{\text{patient}}\|_{\infty}$$

*where $K$ depends on the curvature of the clinical decision complex. No calibration procedure can guarantee $\|h_{\text{proxy}} - h_{\text{patient}}\|_{\infty} < \epsilon$ without direct knowledge of $h_{\text{patient}}$, which is unavailable when the patient lacks capacity.*

The theorem states a structural limitation: proxy pathfinding is fundamentally uncertain. The proxy is navigating with someone else's map, and the map may be wrong.

### The Clinical Geodesic for Proxy Decisions

The geodesic for this case is not "continue everything" (Carlos's immediate request) or "withdraw immediately" (the scalar utilitarian answer). It is a calibration process — an attempt to improve $h_{\text{proxy}}$ before major decisions are made:

**Step 1: Elicit Rosa's values indirectly.** Ask Carlos not "What do you want?" but "Tell me about Rosa. What does she enjoy? What makes her life worth living? Has she ever talked about what she'd want in a situation like this?" Each answer provides partial information about $h_{\text{patient}}$, narrowing the divergence $\|h_{\text{proxy}} - h_{\text{patient}}\|$.

**Step 2: Explore Rosa's relational context ($d_6$).** Ask other family members — children, siblings, close friends — whether Rosa ever expressed preferences about end-of-life care. Multiple sources of proxy information reduce the variance of the $h_{\text{patient}}$ estimate.

**Step 3: Time-limited trial with explicit benchmarks.** Propose a 72-hour trial: if Rosa shows neurological improvement (defined by specific, measurable criteria), continue aggressive treatment. If not, transition to comfort care. The benchmarks transform an open-ended commitment ("do everything") into a bounded clinical experiment.

**Step 4: Revisit with improved proxy calibration.** After 72 hours, return to Carlos with the trial results. By now, he has had time to process, other family members have shared Rosa's statements, and the clinical data has evolved. The proxy's heuristic is better calibrated — not perfectly, but sufficiently for a near-geodesic decision.

### The Manifold Cost of "Do Everything"

Carlos's request — "do everything" — is not manifold-optimal. Continued maximal life support for a patient with less than 5% chance of meaningful recovery imposes costs on:

- $d_3$ (Justice): An ICU bed occupied for weeks by a patient who will almost certainly die
- $d_7$ (Dignity): Prolonged mechanical ventilation, dialysis, and vasopressor support in a patient with no prospect of consciousness
- $d_5$ (Trust): If other family members believe Rosa would not have wanted this, continued treatment damages their trust in the medical system
- $\beta_{\text{futile}}$: Continuing aggressive treatment past the point of medical benefit crosses the futility boundary

But the manifold cost of *immediately overriding Carlos's request* is also high: $d_5$ (trust) is damaged, $d_6$ (family relationships) is strained, and $d_4$ (the proxy's autonomy as decision-maker) is violated.

The geodesic threads between these costs — honoring the proxy's role while improving the proxy's calibration. It is slower than both "do everything" and "withdraw now." It is also less costly on the full manifold than either.

### What Sarah Learns

Sarah watches the palliative care team navigate this case. She notices that they spend more time asking questions than giving answers. They are not indecisive — they are calibrating. Each question narrows the divergence between $h_{\text{proxy}}$ and $h_{\text{patient}}$. By the time the decision is made, Carlos has arrived at it himself — not because anyone argued him into it, but because the information changed his heuristic.

Three days later, Carlos agrees to transition to comfort care. Rosa dies peacefully with her family present. Carlos says: "She told me once that she'd rather die than be kept alive by machines. I forgot that. I needed someone to help me remember."

The proxy's heuristic was recalibrated by the process. The geodesic through the process was shorter — in total manifold cost — than the path that bypassed it.

---

## 9.5 Case 5: Deep Brain Stimulation and the Problem of Identity

### The Clinical Scenario

Dr. Michael Stein, 52 years old, is a philosophy professor with treatment-resistant major depression. He has failed twelve medications, two courses of electroconvulsive therapy, and a year of transcranial magnetic stimulation. He is chronically suicidal. His quality of life is, by any measure, terrible.

A neurosurgery team offers deep brain stimulation (DBS) — implantation of electrodes in the subcallosal cingulate (Area 25) with continuous electrical stimulation. The evidence for DBS in treatment-resistant depression is mixed but promising. Some patients report dramatic improvement.

Dr. Stein consents. The procedure is performed. Six months later, he is no longer depressed. He is, by all clinical measures, well.

He is also different.

His wife reports that he is "not the same person." He has lost interest in philosophy. He no longer reads. He has become socially gregarious in a way that is foreign to his pre-illness personality. He describes his pre-DBS self as "that depressed guy — I don't really remember what it felt like." His values have shifted: he now values social activity over intellectual engagement, physical sensation over abstract thought.

The philosophy department has noticed. His colleagues say he is "happier but shallower." His wife misses the person she married.

### The Temporal Proxy Asymmetry

This case introduces a structure that is absent from all the preceding cases: the patient who consented is not the patient who lives with the consequences.

**Definition 9.3 (Temporal Proxy Asymmetry).** *A temporal proxy asymmetry occurs when a clinical intervention modifies the patient's heuristic function $h_{\text{patient}}$ itself — changing the patient's boundary penalties, dimensional weights, or goal region. The consenting agent (pre-modification self) serves as a temporal proxy for the post-modification self, but the two selves may have divergent heuristic functions:*

$$h_{\text{pre}}(n) \neq h_{\text{post}}(n)$$

*The pre-modification self cannot anticipate the post-modification heuristic because the heuristic is precisely what the intervention changes.*

Dr. Stein consented to DBS with his pre-modification heuristic — a heuristic that valued intellectual engagement ($d_7$: identity as a philosopher), that experienced chronic suffering ($d_1$: poor clinical outcomes), and that was willing to accept personality change as a trade-off. His post-modification heuristic values different things. The person who consented is not the person who bears the consequences.

### The Nine-Dimensional Analysis of Identity-Altering Interventions

[Figure 9.2: Trajectory diagram showing Dr. Stein's attribute vector before and after DBS, with the pre-modification consent path and the post-modification experienced path]

**Pre-DBS attribute vector:** $\mathbf{a}_{\text{pre}} = (d_1{=}{-}0.9, d_2{=}0, d_3{=}0, d_4{=}{+}0.7, d_5{=}{+}0.3, d_6{=}{-}0.5, d_7{=}{+}0.8, d_8{=}0, d_9{=}{+}0.9)$

Dr. Stein's pre-DBS state: terrible clinical outcomes ($d_1$), intact autonomy ($d_4$), moderate trust ($d_5$), suffering family ($d_6$), strong philosophical identity ($d_7$), and excellent understanding ($d_9$).

**Post-DBS attribute vector:** $\mathbf{a}_{\text{post}} = (d_1{=}{+}0.8, d_2{=}0, d_3{=}0, d_4{=}{+}0.7, d_5{=}{+}0.6, d_6{=}{+}0.3, d_7{=}{+}0.2, d_8{=}0, d_9{=}{+}0.5)$

Dr. Stein's post-DBS state: excellent clinical outcomes ($d_1$), intact autonomy ($d_4$), improved trust ($d_5$), improved family relationships ($d_6$), but diminished philosophical identity ($d_7$) and reduced self-understanding ($d_9$) — he no longer knows who he was.

**The identity dimension has been traded for the outcomes dimension.** On the scalar (QALY), this is an unambiguous improvement — his quality of life score has increased dramatically. On the manifold, the picture is more complex. The $d_7$ cost (loss of pre-illness identity) is real, and it is a cost that the pre-modification self accepted on behalf of the post-modification self — a self who, by construction, cannot retrospectively disagree because the intervention changed the very heuristic that would evaluate the trade-off.

### The Consent Paradox of Identity-Altering Interventions

**Theorem 9.2 (Identity-Alteration Consent Paradox).** *For any intervention that modifies $h_{\text{patient}}$, the gauge-invariance test for valid consent (Theorem 4 from the GCE paper) is structurally unable to validate consent across the identity boundary. Consent at time $t_0$ is evaluated using $h_{t_0}$; the consequences are experienced using $h_{t_1}$. If $h_{t_0} \neq h_{t_1}$, no framing of the information at $t_0$ can guarantee that the decision is stable under the transformation $h_{t_0} \to h_{t_1}$.*

This is not a failure of the framework — it is a genuine paradox that the framework makes precise. Identity-altering interventions are the one class of clinical decisions where the consent apparatus breaks down structurally, not merely practically.

### The Clinical Geodesic for Identity Cases

The geodesic for identity-altering interventions includes structural safeguards that the scalar framework does not require:

1. **Pre-modification identity documentation**: Before DBS, the patient articulates their values, identity commitments, and criteria for acceptable personality change. This is stored as a reference attribute vector $\mathbf{a}_{\text{reference}}$.

2. **Post-modification monitoring**: After DBS, the clinical team periodically measures the patient's attribute vector and compares it to $\mathbf{a}_{\text{reference}}$. If $\|d_7^{\text{post}} - d_7^{\text{reference}}\| > \delta_{\text{identity}}$, a structured review is triggered.

3. **Reversibility as boundary constraint**: DBS is adjustable and, in principle, reversible. The geodesic favors identity-altering interventions that are reversible (DBS, medication) over those that are irreversible (ablative neurosurgery), because reversibility preserves a return path on the manifold.

4. **Third-party identity monitoring**: A trusted person (spouse, close friend) is designated as an "identity proxy" — someone who knew the pre-modification self and can report identity changes that the post-modification self may not perceive.

### What Sarah Learns

Sarah does not encounter Dr. Stein's case directly — DBS for depression is not performed at her hospital. But she reads the case report in a neuroethics seminar and recognizes the structure: the temporal proxy asymmetry, the consent paradox, the identity dimension.

She thinks about less dramatic versions of the same problem. Every long-term psychiatric medication changes the patient's personality to some degree. Every major surgery changes the patient's relationship to their body. Every prolonged hospitalization changes the patient's identity. The DBS case is extreme, but the geometric structure — the temporal proxy asymmetry between the consenting self and the experiencing self — is universal.

She begins to understand the ninth dimension ($d_9$: epistemic status) as including self-knowledge — the patient's understanding of who they are and how the intervention will change them. For identity-altering interventions, $d_9$ has a structural ceiling: the patient cannot fully understand the post-modification self because the understanding itself is mediated by the pre-modification heuristic.

---

## 9.6 Synthesis: What the Cases Teach

### Five Cases, Five Structures

| Case | Key Structure | What Scalar Analysis Misses |
|---|---|---|
| 1: Jehovah's Witness | Sacred-value boundary ($\beta = \infty$) | The boundary makes the "worse" outcome the geodesic |
| 2: Life support withdrawal | Process path optimization | The path matters, not just the endpoint |
| 3: Involuntary treatment | Heuristic override | Miscalibrated $h_{\text{patient}}$ justifies constraint |
| 4: Proxy decision | Proxy pathfinding divergence | No calibration guarantees proxy-patient alignment |
| 5: DBS and identity | Temporal proxy asymmetry | The consenting self ≠ the experiencing self |

### The Methodological Lesson

The five cases also teach a methodological lesson about the relationship between the geometric framework and existing clinical ethics approaches.

**Principlism captures the dimensions but not the metric.** Beauchamp and Childress's four principles correspond to four of the nine manifold dimensions (approximately: autonomy = $d_4$, beneficence = $d_1$, non-maleficence = $d_2 + \beta_{\text{harm}}$, justice = $d_3$). The principles correctly identify the relevant dimensions — but they provide no algorithm for resolving conflicts between them, because they have no metric. The geometric framework inherits the dimensions and adds the metric: the covariance matrix $\Sigma$ and the boundary penalties $\beta_k$ that determine the geodesic.

**QALY analysis captures the metric but not the dimensions.** QALY-based health economics provides a clear optimization procedure — maximize quality-adjusted life-years — with a well-defined metric. But the metric operates on one dimension ($d_1$) out of nine. In Cases 1, 2, and 5, the QALY-optimal answer is wrong because the QALY metric cannot see the dimensions that determine the geodesic.

**Casuistry captures the cases but not the similarity measure.** Case-based reasoning (Jonsen and Toulmin, 1988) argues by analogy — "this case is like that case, so the same answer applies." But analogical reasoning requires a similarity metric: how close is this case to that case? Two casuists can reach opposite conclusions because they use different (implicit) similarity measures. The clinical decision complex provides the explicit similarity measure: two cases are similar when their nine-dimensional attribute vectors are close in the Mahalanobis sense.

**Narrative ethics captures the patient but not the computation.** Charon's narrative medicine (2006) insists on the patient's story — their values, identity, relationships, and experiences. This insistence is correct: the story is the nine-dimensional attribute vector in human form. But narrative ethics provides no quantitative apparatus for policy analysis, institutional accountability, or cross-case comparison. The geometric framework provides the quantitative structure that narrative ethics lacks, without sacrificing the patient's story — the story is the data.

The geometric framework is not a replacement for these traditions. It is their synthesis: the dimensions of principlism, the metric of health economics, the case-sensitivity of casuistry, and the patient-centeredness of narrative ethics, unified in a single mathematical structure.

### The Common Thread

Every case has the same structure:

1. A scalar analysis (QALY, utilitarian, binary) produces a clear answer.
2. The nine-dimensional analysis reveals dimensions that the scalar framework cannot see.
3. The geodesic on the full manifold differs from the scalar-optimal path.
4. The difference is not a marginal adjustment but a structural change — a different path, a different process, a different answer.

In Case 1, the scalar says "transfuse" and the geodesic says "respect the refusal and pursue alternatives." In Case 2, the scalar says "withdraw now" and the geodesic says "withdraw after a process that reduces total manifold cost." In Case 3, the scalar says "respect the refusal" and the geodesic says "override the refusal because the heuristic is miscalibrated." In Case 4, the scalar says "the proxy decides" and the geodesic says "calibrate the proxy's heuristic first." In Case 5, the scalar says "great outcome" and the geodesic says "the consent was structurally unable to anticipate the identity cost."

### The Clinical Heuristic Is Already Geometric

The most important lesson from these five cases is not that the geometric framework produces better answers — though it does. It is that *experienced clinicians are already computing these answers*. The attending who explores transfusion alternatives for Mr. Okafor, the palliative care team that conducts family meetings for Mrs. Liu, the psychiatrist who uses minimum necessary restraint for Mr. Torres, the ethics consultant who calibrates the proxy for Mrs. Gutierrez, the neuroethicist who worries about identity change for Dr. Stein — all of them are pathfinding on the nine-dimensional manifold. They are computing clinical geodesics with well-calibrated heuristic functions.

What they lack is the vocabulary to explain what they are doing — to articulate why the QALY-optimal answer is wrong, why the utilitarian path is not the geodesic, why the process matters as much as the outcome. The geometric framework provides that vocabulary. It does not replace clinical wisdom. It reveals its mathematical structure.

### Sarah's Integration

By the end of her second year of residency, Sarah has encountered variants of all five cases. She does not compute attribute vectors at the bedside — that is not what the framework is for. But she has developed a pattern of thinking that is recognizably geometric:

- She asks how many dimensions are active before deciding which ones to optimize.
- She checks for boundary crossings before recommending interventions.
- She tests consent for gauge invariance by reframing information.
- She evaluates proxy decisions by assessing proxy-patient heuristic divergence.
- She notices when the process path has lower total cost than the immediate decision.

Her attending asks her: "What makes you a better clinician than you were a year ago?" Sarah thinks for a moment. "I see more dimensions," she says. "I used to see the clinical question. Now I see the clinical question inside the ethical landscape inside the institutional context inside the patient's life. And I see that there's usually a path through all of it that's better than the path through any one dimension alone."

Her attending nods. "That's clinical judgment," she says.

On the manifold, it is $\varepsilon$-admissible heuristic pathfinding. But the attending's term is older, and Sarah does not correct her.

[Figure 9.3: Composite visualization showing the five cases as five trajectories on the clinical decision complex, each highlighting a different structural feature: the sacred boundary in Case 1, the process path in Case 2, the constrained reachable set in Case 3, the proxy divergence in Case 4, and the temporal identity split in Case 5]

---

## Chapter Summary

This chapter has applied the nine-dimensional clinical decision complex and the $A^*$ pathfinding model to five paradigm cases in clinical ethics. Each case demonstrates that the clinical geodesic — the minimum-cost path on the full manifold — differs from the answer produced by scalar frameworks (QALY analysis, utilitarian calculus, binary principlism). The differences are not marginal; they are structural. The cases collectively demonstrate that the geometric framework captures the reasoning that experienced clinicians already perform — the multi-dimensional, boundary-aware, process-sensitive pathfinding that clinical wisdom represents — and provides the mathematical vocabulary to make that reasoning explicit, teachable, and auditable.

The five structural features revealed by the cases — sacred-value boundaries, process path optimization, heuristic override, proxy divergence, and temporal identity asymmetry — recur throughout clinical medicine. Each will reappear in the chapters that follow: boundaries in triage (Chapter 10), proxy pathfinding in allocation (Chapter 11), identity in moral injury (Chapter 13), and heuristic override in AI clinical reasoning (Chapter 16). The cases are not isolated examples. They are the fundamental structures of the clinical manifold, encountered at the bedside every day.

---

[^1]: The actual clinical management of Jehovah's Witness patients is well-established and broadly consistent with the geodesic analysis presented here. Guidelines from the American College of Surgeons (2019) and the British Journal of Anaesthesia (2020) recommend respecting the refusal and aggressively pursuing bloodless surgical techniques.

[^2]: The proxy asymmetry problem is distinct from the well-known surrogate accuracy literature (Shalowitz et al., 2006), which demonstrates that surrogates predict patient preferences with approximately 68% accuracy. The geometric framework explains *why* surrogate accuracy has a structural ceiling: the proxy is pathfinding with a different heuristic, and no calibration procedure can guarantee convergence without direct access to the patient's heuristic function.

[^3]: The identity-alteration consent paradox has been discussed extensively in the neuroethics literature (Glannon, 2016; Focquaert and Schermer, 2015) but without the formal apparatus to make the paradox precise. The geometric framework's contribution is not the observation that identity-altering interventions raise consent problems — that observation is well-established — but the mathematical characterization of *why* the consent apparatus fails in these cases: the gauge-invariance test cannot operate across a heuristic discontinuity.
