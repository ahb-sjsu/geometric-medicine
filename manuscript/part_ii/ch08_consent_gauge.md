# Chapter 8: Informed Consent as Gauge Invariance

*Part II: The Framework*

---

> *"If the patient's decision changes when you describe the same surgery as '90% survival' instead of '10% mortality,' the consent form is a legal fiction. The patient has not consented to the procedure. The patient has consented to the framing."*
> --- GCE paper, Section 6

> **THE TEST**
>
> *Informed consent is the central moral transaction of clinical medicine. It is the moment when the patient's autonomy meets the clinician's expertise, when the patient's values meet the clinical evidence, when the person meets the numbers. For half a century, consent has been evaluated by a legal checklist: disclosure, comprehension, voluntariness, capacity. This chapter proposes a different test --- a test grounded in the Bond Invariance Principle, the central symmetry requirement of the Geometric Ethics programme. Valid consent is gauge-invariant: the patient's decision survives meaning-preserving reframing. If it does not survive, consent is not genuinely informed, regardless of what the form says.*

---

## 8.1 The Consent Checklist and Its Failures

The standard legal test for valid informed consent requires four elements:[^1]

1. **Disclosure:** The clinician has disclosed the material risks, benefits, and alternatives of the proposed treatment.
2. **Comprehension:** The patient has understood the disclosed information.
3. **Voluntariness:** The patient's decision is free from coercion or undue influence.
4. **Capacity:** The patient has the mental capacity to make the decision.

This is a checklist. Each box is checked or unchecked. If all four boxes are checked, consent is legally valid. If any box is unchecked, consent is not valid (and the clinician faces potential liability for battery or negligence).

The checklist has genuine virtues. It is clear, operational, and legally enforceable. It provides a minimum standard below which consent is not merely inadequate but illegal. It has protected millions of patients from unwanted interventions.

The checklist also has a structural failure that no amount of legal refinement can fix: it evaluates the *process* of consent (was information disclosed? was capacity assessed?) without evaluating the *quality* of consent (does the patient's decision reflect their genuine values? would the decision change if the same information were presented differently?).

The gap between process and quality is the gap between the legal checklist and the gauge-invariance test.

### 8.1.1 Case Study: The Consent Form That Meant Nothing

David Kowalski (Chapter 1, Patient B) signed a consent form for spinal surgery. The form documented that the surgeon disclosed the risks (infection, nerve damage, failed back surgery syndrome), the benefits (potential pain relief, functional improvement), and the alternatives (physical therapy, pain management, watchful waiting). David signed the form in front of a witness. All four boxes were checked.

But David did not understand the information. His health literacy was low ($d_9 = 0.3$). He could not distinguish between "a 70% chance of significant improvement" and "a 30% chance of no improvement or worsening" --- not because the information was not disclosed, but because he lacked the mathematical literacy to interpret probability statements. He felt coerced by his workers' compensation insurer, which had informed him that refusing "appropriate treatment" could result in benefit termination ($d_4 = 0.3$). He did not trust the surgeon, whom he had met for the first time fifteen minutes before the consent conversation ($d_5 = 0.25$).

The consent was legally valid. Every box was checked. And the consent was ethically vacuous. David's decision did not reflect his genuine values; it reflected his fear of losing his benefits, his incomprehension of the probabilities, and his distrust of a stranger who held his future in his hands.

The gauge-invariance test would have detected this. If the surgeon had re-described the surgery as "a procedure that has a 30% chance of not helping you and a small but real chance of making you worse," David's decision would have changed. The decision was framing-dependent --- gauge-variant --- which means that David was not consenting to the surgery. He was consenting to the description of the surgery. And the two are not the same thing.

## 8.2 Consent as Manifold Calibration

The geometric framework provides a deeper characterization of informed consent than the legal checklist.

**Definition 8.1 (Informed Consent as Manifold Calibration).** *Valid informed consent requires that the patient's clinical decision complex $\mathcal{C}_{\text{patient}}$ be calibrated --- that the patient's attribute vectors, edge weights, and boundary penalties approximate the true clinical-moral costs closely enough that the patient's clinical geodesic is a good approximation of the geodesic they would compute with perfect information. Formally:*

$$\|w_{\text{patient}}(v_i, v_j) - w_{\text{true}}(v_i, v_j)\| < \varepsilon \quad \text{for all relevant edges } (v_i, v_j)$$

*where $\varepsilon$ is the tolerance for manifold miscalibration.*

The patient does not need to compute exact edge weights. They do not need to know the covariance matrix, the boundary penalties, or the Mahalanobis distance formula. They need weights close enough that the geodesic they would compute on their miscalibrated manifold is approximately the same as the geodesic they would compute with perfect information.

This is a substantially different requirement from the legal checklist. The checklist asks: "Was information disclosed?" The calibration requirement asks: "Is the patient's representation of the decision landscape close enough to the true landscape that their navigation produces approximately the right path?" The checklist evaluates the input to the consent process. The calibration requirement evaluates the output.

### 8.2.1 What Calibration Requires on Each Dimension

Manifold calibration has a dimension-specific decomposition:

**$d_1$ calibration:** The patient understands the clinical outcomes --- the probabilities of success, failure, complications, and alternative outcomes. This is what traditional consent disclosure focuses on.

**$d_2$ calibration:** The patient understands their rights --- the right to refuse, the right to a second opinion, the right to withdraw consent at any time. This is addressed by the voluntariness element of the legal checklist.

**$d_4$ calibration:** The patient's decision is genuinely autonomous --- free from coercion, undue influence, and decision-making incapacity. This is addressed by the voluntariness and capacity elements of the legal checklist.

**$d_5$ calibration:** The patient trusts the clinician enough to integrate the disclosed information rather than dismissing it. A distrustful patient may hear the disclosure but not believe it, producing a miscalibrated $d_1$ weight on their manifold even though the information was accurately disclosed. Trust calibration is not part of the legal checklist.

**$d_7$ calibration:** The patient's decision reflects their values about dignity, identity, and quality of life --- not just their values about survival and function. A patient who consents to aggressive chemotherapy because they believe "good patients fight" rather than because they genuinely prefer longevity over comfort has miscalibrated $d_7$ weights on their manifold. Value calibration is not part of the legal checklist.

**$d_9$ calibration:** The patient understands the information well enough to use it. This goes beyond the checklist's comprehension element, which typically asks "do you have any questions?" (a test that detects conscious confusion but not unconscious misunderstanding). $d_9$ calibration requires that the patient can apply the information to their own situation --- that they understand not just the statistics but what the statistics mean for them.

The legal checklist addresses $d_1$ and $d_4$ partially, $d_2$ partially, and $d_5$, $d_7$, $d_9$ not at all. The manifold calibration requirement addresses all six relevant dimensions simultaneously.

## 8.3 Consent as Gauge Invariance

The central theorem of this chapter connects informed consent to the Bond Invariance Principle --- the symmetry requirement that is the foundational axiom of the Geometric Ethics programme.

**Theorem 8.1 (Consent as Gauge Invariance).** *Valid informed consent is equivalent to a gauge-invariance condition: the patient's clinical decision must be invariant under changes in the description of the options, dependent only on the attribute vectors of the options. Formally, if $\tau$ is a meaning-preserving transformation of the clinical information (e.g., reframing "90% survival rate" as "10% mortality rate"), then consent is valid only if:*

$$\gamma^*_{\text{patient}}(\tau(x)) = \gamma^*_{\text{patient}}(x) \quad \text{for all meaning-preserving } \tau$$

*If the patient's decision changes under reframing ($\tau$), then either $d_9$ (understanding) or $d_4$ (voluntariness) is inadequately calibrated, and consent is not genuinely informed.*

**Proof.** The Bond Invariance Principle (BIP) requires that ethical evaluations be invariant under meaning-preserving transformations. If the patient's decision varies under $\tau$, the heuristic function $h_{\text{patient}}(n)$ is gauge-variant --- it depends on the framing rather than on the underlying clinical reality. This implies that $d_9$ (the patient's understanding of the options) is not calibrated to the true attribute vectors but is instead sensitive to surface features of the presentation. Equivalently, the patient is not making an informed decision; they are making a framed decision. A framed decision is not informed consent; it is the appearance of informed consent, which is ethically vacuous regardless of its legal validity. $\square$

### 8.3.1 The Gauge-Invariance Test

The theorem implies a concrete diagnostic test for consent quality:

**Test Protocol.** Present the patient with the clinical information in two meaning-preserving frames:

- Frame 1: "This surgery has a 90% success rate."
- Frame 2: "This surgery has a 10% failure rate."

If the patient's decision is the same in both frames, the decision is gauge-invariant, and consent is (on this dimension) genuinely informed. If the patient's decision changes, the decision is gauge-variant, and consent is not genuinely informed regardless of the consent form's legal validity.

The test can be extended to other meaning-preserving transformations:

- Positive framing vs. negative framing ("90% survive" vs. "10% die")
- Absolute numbers vs. relative risk ("2 in 100 have complications" vs. "the risk is doubled from 1% to 2%")
- Gains vs. losses ("you will gain 3 years of life" vs. "without treatment, you will lose 3 years")
- Natural frequencies vs. percentages ("2 out of 100 patients" vs. "2% of patients")

Each transformation tests a specific dimension of the patient's understanding. A patient who is invariant under all meaning-preserving transformations has fully calibrated $d_9$. A patient who is variant under one or more transformations has a specific miscalibration that the clinician can address before proceeding.

### 8.3.2 The Consent Paradox in Low Health Literacy

**Corollary 8.1 (The Consent Paradox).** *Patients with low health literacy can sign consent forms (satisfying the legal checklist) while having $d_9$ values so low that their manifold is grossly miscalibrated. The consent is legally valid but ethically vacuous: the patient's clinical geodesic on their miscalibrated manifold may be radically different from the geodesic they would compute with adequate understanding.*

The paradox is starkest for patients with the lowest health literacy. A patient who cannot interpret a probability statement ("there is a 15% chance of recurrence") is making a decision on a manifold where the $d_1$ edge weights are essentially random. The patient has signed the form. The patient "understands" in the sense that they can repeat back the clinician's words. But the patient's decision manifold is so miscalibrated that the geodesic they compute bears no systematic relationship to the geodesic they would compute with genuine understanding.

The gauge-invariance test detects this directly. If the patient's decision changes when "15% chance of recurrence" is reframed as "85% chance of no recurrence," the patient does not genuinely understand probability. No amount of form-signing changes this fact.

**Proposition 8.1 (Consent Quality Correlates with Health Literacy).** *The framework predicts that framing-variant patients will have lower health literacy scores (REALM, NVS) and lower self-reported understanding than framing-invariant patients, controlling for the content of the disclosure.*

This prediction is testable by the experimental design described in Chapter 17 (Prediction 3): present patients with framing-variant and framing-invariant versions of consent information, measure treatment choice consistency, and correlate with health literacy instruments.

## 8.4 Shared Decision-Making as Manifold Alignment

If informed consent is manifold calibration, shared decision-making (SDM) is manifold alignment --- the process of bringing the patient's and clinician's clinical decision complexes into sufficient agreement to compute a joint geodesic.

**Definition 8.2 (Manifold Alignment).** *Shared decision-making between clinician and patient is manifold alignment: the process of bringing the patient's clinical decision complex $\mathcal{C}_{\text{patient}}$ into sufficient agreement with the clinician's complex $\mathcal{C}_{\text{clin}}$ on the relevant edges and vertices that a jointly computed clinical geodesic is acceptable to both parties. This requires three independent alignment conditions:*

1. **Epistemic alignment ($d_9$):** *The patient understands the clinical facts (diagnosis, prognosis, treatment options, risks) with sufficient accuracy that their $d_1$ attribute vectors approximate the clinician's.*

2. **Value alignment ($d_2$--$d_8$):** *The clinician understands the patient's boundary penalties ($\beta_k^{(\text{patient})}$) well enough that the clinical geodesic respects the patient's moral manifold, not just the clinician's.*

3. **Goal alignment ($G$):** *The patient and clinician agree on the goal region $G$ --- what counts as an acceptable outcome.*

### 8.4.1 Three Modes of Alignment Failure

Each alignment condition can fail independently, and each failure has a distinctive clinical presentation:

**Epistemic misalignment ($d_9$ gap).** The patient does not understand the clinical situation. The patient thinks the surgery is routine; the clinician knows the surgery is high-risk. The patient thinks the prognosis is months; the clinician knows the prognosis is weeks. The gap is on $d_9$: the patient's understanding of the clinical facts is insufficient.

*Clinical presentation:* The patient agrees to everything the clinician recommends, not because of informed consent but because of uninformed deference. The patient's decision is gauge-variant: if the clinical information were re-described more clearly, the decision would change.

*Intervention:* Improve communication. Use plain language, visual aids, teach-back methods, and the gauge-invariance test to verify that the patient's understanding is calibrated.

**Value misalignment ($d_2$--$d_8$ gap).** The clinician does not understand the patient's values. The clinician recommends aggressive chemotherapy ($d_1$-optimal) for a patient who values quality of life over longevity ($d_7$-optimal). The gap is not on $d_9$ (the patient understands the options) but on $d_2$--$d_8$ (the clinician does not understand the patient's boundary penalties).

*Clinical presentation:* The patient hesitates, asks for time, seeks second opinions, or ultimately refuses the recommendation. The clinician may interpret this as "difficulty" or "non-compliance" when it is actually a rational response to a recommendation that does not respect the patient's values.

*Intervention:* Elicit the patient's values. Ask not "What do you want us to do?" (which invites deference) but "What matters most to you about your health?" (which invites value expression). Map the patient's stated values onto the nine-dimensional boundary structure.

**Goal misalignment ($G$ disagreement).** The clinician and patient have different goal regions. The clinician's goal is remission (high $d_1$). The patient's goal is being well enough to attend her granddaughter's graduation in six weeks (high $d_1$ for a specific duration, high $d_6$, high $d_7$). The goals are not contradictory, but they define different regions in the nine-dimensional space, and the geodesics to each region may diverge.

*Clinical presentation:* The clinician and patient talk past each other. The clinician discusses long-term prognosis; the patient discusses short-term function. Both are frustrated because each thinks the other is not listening.

*Intervention:* Explicitly negotiate the goal region. "What would a good outcome look like for you?" is the goal-alignment question. The answer defines $G_{\text{patient}}$, which may differ from $G_{\text{clin}}$. The joint geodesic must navigate toward the intersection of the two goal regions, or, if the intersection is empty, toward the point in $G_{\text{patient}}$ that is closest to $G_{\text{clin}}$ (respecting patient autonomy) or vice versa (respecting clinical reality).

[Figure 8.1: The three modes of alignment failure. (a) Epistemic misalignment: the patient's $d_1$ attribute vectors do not match the clinician's. (b) Value misalignment: the patient's boundary penalties do not match the clinician's. (c) Goal misalignment: the patient's goal region $G_{\text{patient}}$ does not overlap with the clinician's goal region $G_{\text{clin}}$. Each failure has a different clinical presentation and a different intervention.]

## 8.5 The Medical Bond Invariance Principle

The gauge-invariance test for consent is an instance of a broader symmetry requirement: the medical Bond Invariance Principle (BIP).

**Definition 8.3 (Medical Bond Invariance Principle).** *Clinical evaluations must be invariant under patient re-description. The same clinical-moral state, described by different physicians, in different languages, with different chart formats, should receive the same clinical evaluation. Formally, if $\tau_{\text{re-desc}}$ is a re-description of the patient's state that preserves the attribute vector $\mathbf{a}$, then:*

$$\gamma^*_{\mathcal{C}}(\tau_{\text{re-desc}}(\mathbf{a})) = \gamma^*_{\mathcal{C}}(\mathbf{a})$$

*The clinical geodesic should not depend on the description. It should depend only on the patient's clinical-moral state.*

The medical BIP has three immediate applications:

### 8.5.1 Algorithmic Bias as BIP Violation

A clinical algorithm that produces different recommendations based on the patient's race, zip code, or insurance status is violating the medical BIP --- the evaluation changes when the description changes in a way that should be gauge-invariant.

The Obermeyer et al. (2019) algorithm (Chapter 1) violated the BIP in a specific way: it used health costs as a proxy for health needs, and since costs correlate with race due to differential access, the algorithm's recommendations were gauge-variant under race re-description. If you could change the patient's race on the intake form (a re-description that should be gauge-invariant for clinical need), the algorithm's recommendation would change. This is a BIP violation, detectable by the gauge-invariance test, and measurable by the Bond Index (Chapter 12).

### 8.5.2 Language as Gauge Transformation

A patient whose clinical information is described in English should receive the same clinical evaluation as a patient whose clinical information is described in Spanish. Language is a gauge transformation: it changes the description without changing the clinical-moral state. The BIP requires that clinical evaluations be invariant under translation.

This requirement is routinely violated. Patients who speak the clinician's language receive different care than patients who require interpreters --- not because their clinical states are different, but because the communication channel ($d_9$) is degraded by translation, and the degraded channel produces a less calibrated clinical decision complex. The BIP violation is indirect: the language difference degrades $d_9$, the degraded $d_9$ changes the clinical evaluation, and the changed evaluation violates gauge invariance.

### 8.5.3 Chart Format as Gauge Transformation

The same clinical information presented in different chart formats (handwritten vs. electronic, narrative vs. structured, chronological vs. problem-oriented) should produce the same clinical evaluation. Chart format is a gauge transformation: it changes the presentation without changing the content.

This requirement is also routinely violated. Clinicians form different impressions of the same patient depending on how the chart is organized --- a phenomenon known as "chart bias" that is well-documented in the medical literature.[^2] A patient whose chart leads with a psychiatric diagnosis ("56-year-old male with schizophrenia presenting with chest pain") receives different evaluation than a patient whose chart leads with the presenting complaint ("56-year-old male presenting with chest pain, past history of schizophrenia"), even though the information content is identical. The ordering of information is a gauge transformation. The clinical evaluation should be invariant under it. When it is not, the evaluation is gauge-variant, and the BIP is violated.

## 8.6 Sarah Learns the Gauge Test

During her third year, Sarah was assigned to a surgical rotation. She watched the consent process for elective surgeries and noticed a pattern: surgeons described procedures in optimistic frames ("95% of patients do very well"), patients readily agreed, and consent forms were signed in five minutes. The process was efficient, legally valid, and ethically untested.

Sarah began informally applying the gauge-invariance test. After the surgeon left, she would ask the patient: "The surgeon mentioned that 95% of patients do very well. Another way to say the same thing is that 1 in 20 patients have a significant problem. Does that change how you feel about the surgery?"

She tracked twenty patients over three weeks. Fourteen said it did not change their decision --- their consent was gauge-invariant on this transformation. Six said it changed how they felt --- they wanted more information, more time, or more discussion. Of these six, three ultimately proceeded with surgery after further conversation (their consent became gauge-invariant after additional calibration of $d_9$), and three requested more time to decide (their consent was not yet gauge-invariant and they knew it).

Sarah reported her findings to the surgery department's quality improvement committee. The response was mixed. Several surgeons objected: "We can't scare patients with negative framing." Sarah pointed out that the gauge-invariance test does not advocate negative framing; it tests whether the consent is robust to framing. If the patient's decision survives the reframing, the consent is genuine and the surgeon should feel confident. If the decision does not survive, the consent is framing-dependent and the surgeon is proceeding with a patient who has not genuinely consented --- a legal and moral risk regardless of the form.

The committee did not adopt the gauge-invariance test as a standard protocol. But two surgeons began using it informally, and one reported that it had identified a patient whose consent was dramatically gauge-variant: the patient had agreed to bypass surgery when told "this will prevent future heart attacks" but wavered when told "this surgery has a 3% risk of stroke, and without the surgery, there is a 15% chance you will have another heart attack in the next five years." The patient's understanding of the risk-benefit trade-off was so miscalibrated that the two descriptions --- which conveyed the same information --- produced opposite decisions. The surgeon delayed the surgery, spent an additional hour on consent counseling, and ultimately proceeded with a patient whose consent was genuine.

"That hour," the surgeon told Sarah, "was the best hour I spent all month. That patient almost had a surgery she didn't actually want."

## 8.7 The Limits of Gauge Invariance

The gauge-invariance test is a necessary condition for genuine informed consent, not a sufficient one. A patient whose decision is gauge-invariant has a calibrated $d_9$ (understanding is robust to reframing), but may still have:

- **Coerced autonomy ($d_4$ failure).** The patient understands the options perfectly and always makes the same choice regardless of framing --- but the choice is driven by coercion (the insurer will cancel benefits) rather than by genuine preference. The consent is gauge-invariant but not voluntary.

- **Miscalibrated values ($d_7$ failure).** The patient's decision is gauge-invariant, but the decision reflects internalized values that the patient would reject upon reflection. A patient who consents to aggressive treatment because "good patients fight" has a gauge-invariant but value-miscalibrated consent: the decision does not change under framing, but it might change under values clarification.

- **Proxy distortion ($d_6$ failure).** The patient's decision is gauge-invariant, but the decision is driven by family pressure rather than by the patient's own values. The patient's $d_6$ (social impact) concerns are dominating their $d_4$ (autonomy) and $d_7$ (dignity) concerns, producing a decision that is robust to information framing but sensitive to social framing.

These limitations do not diminish the gauge-invariance test's value. They identify its place in a broader framework: gauge invariance tests $d_9$ calibration (does the patient understand?). Voluntariness assessments test $d_4$ calibration (is the patient free?). Values clarification tests $d_7$ calibration (does the patient's decision reflect their values?). Social context assessment tests $d_6$ calibration (is the patient's decision their own?). Each test addresses a different dimension of the manifold, and genuine informed consent requires adequate calibration on all of them.

## 8.8 Consent in the Clinical Decision Complex

Informed consent, in the geometric framework, is a manifold calibration operation that transforms the patient from a passive recipient of clinical decisions into an active co-navigator of the clinical decision complex.

Before consent: the clinician navigates $\mathcal{C}_{\text{clin}}$ alone, using the clinician's boundary penalties ($\beta_k^{(\text{clin})}$), the clinician's dimensional weights, and the clinician's goal region ($G_{\text{clin}}$).

After consent: the clinician and patient navigate a joint manifold, using the patient's boundary penalties ($\beta_k^{(\text{patient})}$) where the patient has expressed clear values, the clinician's boundary penalties where the patient has deferred, and a jointly defined goal region ($G_{\text{joint}}$) that respects both the patient's values and the clinical realities.

The consent process is the transition from $\mathcal{C}_{\text{clin}}$ to $\mathcal{C}_{\text{joint}}$. The gauge-invariance test verifies that the transition has been performed correctly --- that the patient's integration into the joint manifold is based on genuine understanding ($d_9$), genuine autonomy ($d_4$), and genuine values ($d_7$), not on framing artifacts that would dissolve under re-description.

When consent is genuine --- when the gauge-invariance test is passed, the voluntariness assessment is clear, and the values are aligned --- the resulting clinical geodesic has a remarkable property: it is the path that both the clinician and the patient would choose if both had perfect information and perfect freedom. It is not a compromise between the clinician's preferences and the patient's preferences. It is the path that emerges when the full moral-clinical landscape is visible to both parties and both parties navigate it together.

This is what informed consent is for. Not the form. Not the signature. Not the legal checklist. The form is a record. The signature is a formality. The checklist is a minimum standard. What consent is *for* is manifold alignment: bringing two navigators together on a shared landscape so that the path they follow respects both the terrain (clinical reality) and the traveler's values (patient autonomy). The gauge-invariance test is the diagnostic that tells us whether the alignment has been achieved.

## 8.9 Consent in Special Populations

The gauge-invariance framework illuminates consent challenges in populations where standard consent processes frequently fail.

### 8.9.1 Pediatric Consent and Assent

Children cannot provide legal consent. Parents or guardians consent on their behalf. But the geometric framework distinguishes between the guardian's consent (a proxy navigation of the clinical decision complex using the guardian's $h(n)$, which may or may not approximate the child's) and the child's assent (the child's own engagement with the decision at a level appropriate to their developmental stage).

Assent is partial gauge-invariance: the child's decision may not be fully invariant under all meaning-preserving transformations (a seven-year-old cannot reason about probability), but it should be invariant under the transformations the child can comprehend ("this medicine will help your tummy feel better" should produce the same response regardless of whether it is said by a nurse or a doctor, in the clinic or at home). The $d_9$ calibration threshold for assent is lower than for consent --- the child need not understand the statistics, only the gist --- but the gauge-invariance requirement still applies at the child's level of comprehension.

### 8.9.2 Psychiatric Consent and Capacity

Patients with psychiatric illness present the most difficult consent challenges in medicine, because the illness itself can impair the capacity for gauge-invariant decision-making.

A patient in acute psychosis may have $d_9 \approx 0$ (no understanding of their situation) and $d_4 \approx 0$ (no capacity for autonomous decision-making). Involuntary treatment in this case is geometrically justified: the patient's manifold is so miscalibrated that their "decisions" bear no systematic relationship to their genuine values. Treatment aims to restore $d_9$ and $d_4$ to levels where genuine consent becomes possible.

But psychiatric consent exists on a spectrum. A patient with mild depression may have $d_9 = 0.7$ and $d_4 = 0.6$ --- moderate understanding and moderate autonomy. Their decisions may be partially gauge-variant (the depression biases their assessment toward pessimistic outcomes) without being fully incapacitated. The geometric framework handles this intermediate case through $\varepsilon$-calibration: the patient's manifold is approximately calibrated, and the clinical geodesic should respect their decisions while accounting for the systematic bias.

The difficult cases --- the patient with anorexia nervosa who refuses nutrition, the patient with depression who refuses antidepressants, the patient with psychosis who has lucid intervals --- are cases where $d_9$ and $d_4$ fluctuate, making the gauge-invariance test time-dependent. A decision that is gauge-invariant during a lucid interval may not be gauge-invariant during a psychotic episode. The framework's response: consent obtained during gauge-invariant periods should be honored during gauge-variant periods, provided the patient's values (as expressed during lucidity) are not contradicted by the current presentation. This is the temporal extension of the advance directive: a gauge-invariant decision made at time $t_1$ governs action at time $t_2$ when gauge invariance is no longer achievable.

### 8.9.3 Emergency Consent and Implied Consent

In genuine emergencies --- the unconscious trauma patient, the patient in cardiac arrest, the patient seizing in the emergency department --- there is no time for consent processes. The standard legal doctrine is implied consent: a reasonable person would consent to life-saving treatment, and the unconscious patient is presumed to be a reasonable person.

In the geometric framework, implied consent is a default geodesic: when $d_4$ is unavailable (the patient cannot express preferences) and $d_9$ is unavailable (the patient cannot receive information), the clinician navigates the clinical decision complex using the standard boundary penalties ($\beta_k^{(\text{profession})}$) and the default goal region ($G_{\text{default}} = $ survival with maximal function). The default geodesic is manifold-optimal under the assumption that the patient's attribute vector is approximately average on the non-assessable dimensions.

The default geodesic fails when the patient is not average --- when the patient has an advance directive that prohibits resuscitation, when the patient has religious objections to specific treatments, when the patient has a known preference that deviates from the default. The Medic Alert bracelet, the advance directive, the POLST form --- these are pre-computed segments of the patient's personal geodesic, communicated in advance precisely because the patient anticipates a future moment when $d_4$ and $d_9$ will be unavailable. The framework formalizes what these documents do: they constrain the default geodesic by communicating the patient's boundary penalties ($\beta_k^{(\text{patient})}$) and goal region ($G_{\text{patient}}$) in advance.

### 8.9.4 Research Consent and Double Consent

Clinical trial consent adds a layer to the standard consent framework: the patient must consent not only to the treatment but to the uncertainty about which treatment they will receive. In a randomized controlled trial, the patient consents to an edge on the clinical decision complex that branches into two or more possible paths, and the branching is determined by randomization rather than by clinical judgment.

Research consent requires a specific form of $d_9$ calibration: the patient must understand randomization (that they will be assigned to a treatment group by chance, not by clinical merit), equipoise (that the clinical community genuinely does not know which treatment is better), and the possibility of receiving the control intervention (which may be inferior to the experimental intervention). These are cognitively demanding concepts, and the gauge-invariance test is particularly informative: "You have a 50% chance of getting the new drug and a 50% chance of getting the standard drug" should produce the same decision as "You have a 50% chance of not getting the new drug," and a patient whose decision changes under this reframing does not genuinely understand randomization.

## 8.10 Toward a Consent Quality Metric

The gauge-invariance framework suggests a quantitative metric for consent quality: the **consent invariance score** (CIS), defined as the proportion of meaning-preserving transformations under which the patient's decision remains stable.

**Definition 8.4 (Consent Invariance Score).** *Let $\tau_1, \ldots, \tau_m$ be a set of $m$ meaning-preserving transformations of the clinical information (e.g., survival vs. mortality framing, absolute vs. relative risk, natural frequencies vs. percentages). The consent invariance score is:*

$$\text{CIS} = \frac{1}{m} \sum_{j=1}^{m} \mathbf{1}[\gamma^*_{\text{patient}}(\tau_j(x)) = \gamma^*_{\text{patient}}(x)]$$

*CIS = 1 means the patient's decision is invariant under all tested transformations (fully informed). CIS = 0 means the patient's decision changes under every transformation (not informed at all). CIS between 0 and 1 indicates partial calibration with specific miscalibrations that can be identified by examining which transformations produce decision changes.*

The CIS is not proposed as a replacement for the legal consent checklist; it is proposed as a supplement that measures what the checklist does not: the quality of the patient's understanding as revealed by the stability of their decisions under re-description. A CIS threshold (e.g., CIS $\geq 0.8$) could be used as an institutional quality standard for consent processes, with patients below the threshold receiving additional explanation before proceeding.

The CIS is empirically measurable, falsifiable (it predicts specific correlations with health literacy --- see Prediction 3, Chapter 17), and actionable (low CIS identifies which transformations the patient fails, pointing to specific areas where additional explanation is needed). It transforms consent quality from a binary legal judgment (valid/invalid) to a continuous quality metric that enables improvement.

---

## Summary

This chapter has formalized informed consent as a gauge-invariance condition on the clinical decision complex. Valid consent requires that the patient's clinical decision be invariant under meaning-preserving reframing --- that the patient's choice of treatment survives translation from one description to another without change. The gauge-invariance test is a concrete, falsifiable diagnostic: present the clinical information in two meaning-preserving frames and check whether the patient's decision is the same.

The framework distinguishes consent-as-calibration (the patient's clinical decision complex is calibrated to within tolerance of the true clinical-moral costs) from consent-as-gauge-invariance (the patient's decision is invariant under re-description) and identifies three independent alignment conditions for shared decision-making: epistemic alignment ($d_9$: the patient understands), value alignment ($d_2$--$d_8$: the clinician understands the patient's values), and goal alignment ($G$: both parties agree on acceptable outcomes). Each condition can fail independently, and each has a distinctive clinical presentation and intervention.

The medical Bond Invariance Principle extends gauge invariance from consent to all clinical evaluations: the same clinical-moral state, re-described in a different language, by a different physician, in a different chart format, should receive the same evaluation. Algorithmic bias, language barriers, and chart bias are specific violations of the medical BIP, detectable by the gauge-invariance test and measurable by the Bond Index. Special populations --- pediatric, psychiatric, emergency, and research --- each present specific challenges to gauge-invariant consent that the framework addresses through population-specific calibration requirements.

---

[^1]: The four-element formulation is standard in U.S. medical law. See Faden, R. R., & Beauchamp, T. L. (1986). *A History and Theory of Informed Consent*. Oxford University Press. The U.K. standard, following *Montgomery v Lanarkshire Health Board* [2015] UKSC 11, has moved toward a patient-centered standard that is closer to the gauge-invariance requirement: the clinician must disclose what a reasonable patient in the patient's position would want to know.

[^2]: Tversky, A., & Kahneman, D. (1981). The framing of decisions and the psychology of choice. *Science*, 211(4481), 453--458. The original demonstration of framing effects in decision-making. For the clinical setting specifically, see McNeil, B. J., et al. (1982) and Moxey, A., et al. (2003). Chart ordering effects are documented in Mamede, S., et al. (2017). The influence of case history on the interpretation of clinical findings. *Academic Medicine*, 92(10), 1459--1465.
