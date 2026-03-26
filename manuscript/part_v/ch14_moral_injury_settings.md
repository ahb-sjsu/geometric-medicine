# Chapter 14: Moral Injury in the Wild — Pandemic, Palliative, Psychiatric

> *"The theory of moral injury is tested not in the seminar room but in the ICU, the hospice, and the locked ward — three clinical settings where the manifold's boundaries are crossed every day."*

---

Chapter 13 developed the mathematical theory: moral injury as cumulative forced boundary crossing, the two damage modes, the Moral Injury Index, the accumulation theorem. Theory must be tested against clinical reality. This chapter applies the framework to three clinical settings where moral injury is endemic — the pandemic ICU, palliative care, and psychiatry. Each setting has a characteristic moral injury signature: a specific pattern of boundary crossings, a specific damage mode, and a specific interaction between institutional policy and clinician heuristic. The framework generates predictions for each setting that are testable against the existing empirical literature and, where the literature is insufficient, against future study.

---

## 14.1 Setting 1: The Pandemic ICU

### The Moral Injury Signature

The pandemic ICU is the setting where the geometric theory of moral injury was developed — it was the COVID-19 pandemic that forced the distinction between burnout and moral injury into clinical consciousness. The pandemic ICU's moral injury signature is:

**Dominant boundary crossings:**
- $\beta_{\text{abandon}}$: Denying ventilators, denying ICU admission, withdrawing life support for reallocation
- $\beta_{\text{justice}}$: Age-based or comorbidity-based deprioritization
- $\beta_{\text{dignity}}$: Restricting family visitation, patients dying alone
- Degraded $d_9$: Extreme prognostic uncertainty in a novel disease

**Dominant damage mode:** Mixed — acute hypervigilance from early triage decisions, transitioning to moral numbing over weeks of sustained boundary crossing.

**Characteristic trajectory:** The moral injury trajectory in a pandemic ICU follows a predictable arc:

1. **Phase 1 (Days 1–7): Acute distress.** The first triage decisions are experienced as deeply distressing. $\beta_k$ values are at pre-crisis levels. Each boundary crossing produces a large $\Delta \text{MI}(t)$ because the gap between $\beta_k^{(\text{clin})}$ and $\tau$ is large.

2. **Phase 2 (Days 7–21): Hypervigilance.** The cumulative MI triggers hypervigilance on the most severely crossed boundaries. Clinicians become risk-averse, over-triage, hold resources in reserve. Clinical efficiency decreases. Colleagues notice "paralysis" in decision-making.

3. **Phase 3 (Days 21+): Moral numbing.** Sustained boundary crossing desensitizes the hypervigilant response. $\beta_k$ deflates toward or below pre-crisis levels. Clinical efficiency returns — but at the cost of moral sensitivity. The clinician crosses boundaries without the distress that would have prevented crossing in the pre-crisis period.

4. **Phase 4 (Post-pandemic): Mixed residue.** After the crisis, the clinician's $\beta_k$ profile is permanently altered: some boundaries are inflated (hypervigilance on the most traumatic crossings), others are deflated (numbing on the most frequent crossings). The moral injury vector $\vec{\text{MI}}$ is non-zero on multiple components.

[Figure 14.1: The pandemic moral injury trajectory: $\beta_{\text{abandon}}$ over time showing the three-phase arc (acute distress → hypervigilance → moral numbing) with schematic moral injury accumulation curve]

### Five Predictions and the Empirical Evidence

The framework generates five specific predictions about pandemic moral injury:

**Prediction 14.1: Higher MI among ICU clinicians than non-triage specialties.**

*Rationale:* ICU clinicians make more triage decisions (more boundary crossings) than clinicians in non-triage specialties. The moral injury increment is proportional to boundary-crossing frequency.

*Evidence:* Consistent. Greenberg et al. (2020) documented higher moral distress among ICU staff compared to general ward staff. Lai et al. (2020) found that frontline healthcare workers (ICU and emergency) reported significantly higher psychological distress than non-frontline workers. The specificity of the prediction — that the differential is driven by triage decisions, not by exposure to death per se — is partially supported by evidence that palliative care workers (who are exposed to death but do not make triage decisions) showed lower moral distress than ICU workers during the pandemic.

**Prediction 14.2: Higher MI among clinicians who disagreed with the triage protocol.**

*Rationale:* Moral injury is the gap $\beta_k^{(\text{clin})} - \tau$. Clinicians who agree with the protocol have $\beta_k$ values aligned with the protocol's boundary crossings, producing small gaps. Clinicians who disagree have $\beta_k$ values that diverge from the protocol, producing large gaps.

*Evidence:* Consistent. Rushton (2018) documented that moral distress was highest among clinicians whose personal ethical commitments conflicted with institutional protocols. Lamiani et al. (2017) found that perceived ethical violations by the organization were stronger predictors of moral distress than individual patient care decisions.

**Prediction 14.3: MI correlated with number of triage decisions, not just severity.**

*Rationale:* The Accumulation Theorem states that $\text{MI}(T) = \sum_t \Delta \text{MI}(t)$ — cumulative moral injury is the sum of individual boundary-crossing increments. More triage decisions means more increments.

*Evidence:* Partially consistent. Dodek et al. (2016) found that moral distress was correlated with the frequency of ethically challenging situations, not just their severity. However, few studies have specifically measured the number of triage decisions as a distinct predictor, separate from overall workload — a measurement gap that the framework identifies.

**Prediction 14.4: MI dissociable from burnout.**

*Rationale:* MI ($h(n)$-damage) and burnout ($g(n)$-depletion) are structurally independent. The prediction is that clinicians with high MI and low burnout exist (well-rested but morally damaged) and that clinicians with low MI and high burnout exist (exhausted but morally intact).

*Evidence:* Consistent. Dean et al. (2019) explicitly argued for the MI-burnout distinction and provided case examples of clinicians with high moral distress and low burnout scores. Mantri et al. (2020) found that MISS-HP scores and MBI scores were moderately correlated but statistically distinguishable, with different demographic and occupational predictors.

**Prediction 14.5: MI partially predictable from pre-pandemic $\beta_k$ profiles.**

*Rationale:* Clinicians with higher pre-crisis $\beta_k$ values on the boundaries most likely to be crossed by the pandemic protocol should show higher MI. This prediction is novel — it implies that moral injury vulnerability can be assessed before a crisis.

*Evidence:* Not yet tested. This is the framework's most distinctive prediction. Testing it requires longitudinal measurement of clinician $\beta_k$ profiles before and after a crisis, which has not been done. The prediction is falsifiable: if pre-crisis $\beta_k$ profiles do not predict post-crisis MI, the framework's mechanism (MI as forced crossing of personally valued boundaries) is wrong.

---

## 14.2 Setting 2: Palliative Care

### The Moral Injury Signature

Palliative care presents a different moral injury pattern than the pandemic ICU. The boundary crossings are not acute and dramatic but chronic and gradual. The dominant damage mode is moral numbing rather than hypervigilance. The moral injury vector is concentrated on different components.

**Dominant boundary crossings:**
- $\beta_{\text{futile}}$: Continuing aggressive treatment when the clinical outcome is hopeless, at family insistence or institutional pressure
- $\beta_{\text{dignity}}$: Prolonging dying in a medicalized setting that compromises the patient's dignity
- $\beta_{\text{consent}}$: Making treatment decisions for patients who lack decision-making capacity, using proxy consent of uncertain quality

**Dominant damage mode:** Moral numbing — gradual deflation of $\beta_{\text{futile}}$ through repeated exposure to futile treatment.

**Characteristic trajectory:** Unlike the pandemic ICU's dramatic arc, the palliative care trajectory is a slow erosion:

1. **Year 1:** The clinician enters palliative care with well-calibrated $\beta_k$ values. Futile treatment is distressing. Each family request for "everything" produces moral distress because the clinician's $\beta_{\text{futile}}$ assigns high cost to continuing treatment without benefit.

2. **Years 2–5:** Repeated encounters with futile treatment gradually deflate $\beta_{\text{futile}}$. The clinician processes more futile treatment orders without distress. Colleagues describe the clinician as "experienced" and "comfortable with end-of-life care." The comfort is partially genuine expertise and partially moral numbing.

3. **Years 5+:** The clinician's $\beta_{\text{futile}}$ has stabilized at a deflated level. They continue aggressive treatment in cases where, early in their career, they would have advocated for comfort care. They have become the "efficient" palliative care clinician who processes orders without moral friction. The efficiency is valued by the institution but represents a degradation of clinical judgment on the futility dimension.

### The Palliative Paradox

Palliative care produces a paradox: the clinicians who specialize in end-of-life care — who are most needed as moral exemplars — are the most exposed to the boundary crossings that produce moral numbing. The institution's most morally sensitive clinicians are placed in the setting most likely to erode their moral sensitivity.

**Proposition 14.1 (The Palliative Paradox).** *The clinical setting that most requires intact $\beta_{\text{futile}}$ — palliative care — is the setting most likely to produce $\beta_{\text{futile}}$ deflation through moral numbing. The paradox is structural: the same boundary crossings that define the clinical work are the ones that damage the heuristic function needed to evaluate the clinical work.*

The paradox has no clean resolution. But the framework suggests mitigation strategies:

1. **Rotation**: Limit the duration of continuous palliative care assignment. Clinicians who rotate between palliative care and other specialties have periodic $\beta_{\text{futile}}$ recalibration opportunities.

2. **Structured ethics support**: Regular ethics consultations (not crisis-triggered but scheduled) that explicitly recalibrate $\beta_{\text{futile}}$ by discussing cases where the clinician's numbed heuristic might have led to suboptimal decisions.

3. **Peer observation**: Pair experienced palliative care clinicians with less experienced colleagues. The less experienced colleague's intact $\beta_{\text{futile}}$ serves as a reference point — if the experienced clinician notices that the colleague's moral distress at a particular case is higher than their own, this is diagnostic of numbing.

### Moral Numbing vs. Genuine Expertise

A critical question: how do we distinguish moral numbing (pathological $\beta_k$ deflation) from genuine expertise (appropriate $\beta_k$ recalibration)?

An expert palliative care clinician may have lower $\beta_{\text{futile}}$ than a novice — not because of numbing but because they have a more accurate assessment of when treatment is truly futile and when it is not. Their $\beta_{\text{futile}}$ has been *calibrated* by experience rather than *deflated* by injury.

**Definition 14.1 (Calibration vs. Numbing).** *Genuine calibration and moral numbing produce opposite predictions about decision quality:*

- *Calibration: The clinician's decisions on the futility boundary are more accurate (closer to manifold-optimal) than a novice's. The clinician correctly identifies cases where continued treatment is truly futile and cases where it is not.*

- *Numbing: The clinician's decisions on the futility boundary are less accurate than they would have been with intact $\beta_k$. The clinician fails to identify cases where continued treatment is truly futile, processing them as routine rather than evaluating them critically.*

*The distinguishing test: Does the clinician's sensitivity to futility boundary cases decrease (numbing) or does their specificity increase (calibration)? A calibrated clinician becomes better at identifying the boundary; a numbed clinician becomes less responsive to it.*

---

## 14.3 Setting 3: Psychiatry

### The Moral Injury Signature

Psychiatric moral injury has a unique structure: the boundary crossings are not only frequent but *conflicted*. The clinician's heuristic function is simultaneously told "this crossing is necessary" (by the clinical evidence and the risk assessment) and "this crossing is wrong" (by the clinician's moral commitment to patient autonomy). The result is not a simple inflation or deflation of $\beta_k$ but a *splitting* of the boundary penalty into two values: one for the institutional perspective and one for the personal perspective.

**Dominant boundary crossings:**
- $\beta_{\text{consent}}$: Involuntary admission, forced medication, physical restraint
- $\beta_{\text{dignity}}$: Seclusion, loss of personal autonomy, institutional control of bodily functions
- $\beta_{\text{autonomy}}$: Overriding patient decisions in the service of patient safety

**Dominant damage mode:** Conflicted heuristic — the clinician develops two simultaneous estimates of the boundary penalty, one supporting crossing (the institutional perspective: "this patient needs to be restrained for safety") and one opposing it (the personal perspective: "restraining a person against their will violates their dignity").

**Characteristic trajectory:**

1. **Early career:** The clinician performs their first involuntary commitment. The experience is deeply distressing — the gap between $\beta_{\text{consent}}^{(\text{clin})}$ and $\tau$ is large. The clinician questions whether they chose the right specialty.

2. **Mid-career:** The clinician has performed hundreds of involuntary interventions. They have developed a split $\beta_{\text{consent}}$: one estimate for "this patient is a danger to themselves or others" (the institutional justification, where $\beta_{\text{consent}}$ is low — the crossing is necessary) and another for "I am forcibly medicating a human being against their will" (the personal assessment, where $\beta_{\text{consent}}$ remains high).

3. **Late career:** The split either resolves (one perspective dominates) or persists (chronic moral tension). Clinicians whose institutional perspective dominates may exhibit moral numbing on autonomy violations. Clinicians whose personal perspective dominates may develop hypervigilance that makes them reluctant to intervene even when intervention is clinically indicated.

### The Conflicted Heuristic

**Definition 14.2 (Conflicted Heuristic).** *A clinician has a conflicted heuristic on boundary $k$ when they simultaneously maintain two boundary penalty estimates:*

$$\beta_k^{(\text{institutional})} < \tau < \beta_k^{(\text{personal})}$$

*The institutional estimate says the crossing is within tolerance; the personal estimate says it is not. The clinician crosses the boundary (following the institutional mandate) while experiencing moral injury (the personal penalty exceeds threshold).*

The conflicted heuristic is unique to settings where the institution provides a justification for the boundary crossing that the clinician partially accepts. In the pandemic ICU, there is typically no justification that the clinician accepts — the triage protocol overrides the clinician's judgment, and the clinician experiences the override as a pure violation. In psychiatry, the institution provides a justification (patient safety) that the clinician partially endorses, creating the split.

**Proposition 14.2 (Psychiatric Moral Injury Is Qualitatively Distinct).** *Psychiatric moral injury differs from pandemic and palliative moral injury in its heuristic structure:*

- *Pandemic MI: Single $\beta_k$ exceeding threshold → pure violation. The clinician disagrees with the mandate.*
- *Palliative MI: Single $\beta_k$ gradually deflating → numbing. The clinician's sensitivity erodes.*
- *Psychiatric MI: Split $\beta_k$ → chronic conflict. The clinician simultaneously agrees and disagrees with the crossing.*

*The three settings produce different symptoms, different damage patterns, and require different interventions. Treating all three as "moral injury" without distinguishing their geometric structure is a form of scalar reduction — collapsing a three-dimensional typology to a single label.*

### Involuntary Treatment: The Moral Injury Cost of Saving Lives

Psychiatry's defining clinical act — involuntary treatment of a patient who refuses care due to impaired judgment — is a forced boundary crossing that the geometric framework can analyze with precision.

The clinician restrains a patient. The clinical justification is strong: the patient is psychotic, a danger to themselves and others, and unable to make an informed treatment decision. The manifold analysis supports the intervention (Chapter 9, Case 3). The clinician agrees that the intervention is necessary.

And yet the moral injury occurs. The clinician's $\beta_{\text{consent}}^{(\text{personal})}$ exceeds threshold, even though $\beta_{\text{consent}}^{(\text{institutional})}$ does not. The *physical act* of restraining a human being — of holding a person down while medication is injected — crosses a boundary that no amount of clinical justification can render costless on the personal manifold.

**This is the distinctive cruelty of psychiatric moral injury: the clinician is morally injured by doing the right thing.** The pandemic clinician is morally injured by being forced to do the wrong thing (deny a ventilator). The palliative clinician is morally injured by being unable to do the right thing (provide comfort care when the family insists on aggressive treatment). The psychiatric clinician is morally injured by doing the right thing (intervening to save a patient who cannot consent) because the right thing requires crossing a boundary that the clinician's personal manifold assigns a penalty exceeding threshold.

---

## 14.4 Emergency Medicine: A Fourth Setting

### The Unique Structure of Emergency Moral Injury

Although the chapter focuses on three primary settings (pandemic ICU, palliative care, psychiatry), a brief analysis of emergency medicine reveals a fourth moral injury pattern that further validates the multi-dimensional taxonomy.

**Dominant boundary crossings in emergency medicine:**
- $\beta_{\text{abandon}}$: Discharging patients who need admission when the hospital is full
- $\beta_{\text{justice}}$: Implicit or explicit triage based on insurance status, race, or appearance
- $d_9$ degradation: Making life-or-death decisions with minimal clinical information ("this patient arrived three minutes ago and I need to decide now")

**Dominant damage mode:** Rapid-cycling mixed. Unlike the pandemic ICU (sustained acute crossing), palliative care (chronic gradual crossing), or psychiatry (conflicted crossing), emergency medicine produces rapid alternation between boundary crossings and non-crossings. A single shift might include twelve triage decisions, of which three cross moral boundaries. The clinician cycles between boundary-crossing distress and non-crossing competence within hours.

**Characteristic trajectory:** Emergency clinicians develop a distinctive $\beta_k$ profile: moderately deflated boundaries on all dimensions (generalized numbing from chronic low-level crossing), combined with occasional hypervigilant spikes on the abandonment dimension (triggered by specific cases that resemble prior traumatic triage decisions).

**Proposition 14.3 (Emergency Medicine MI Pattern).** *Emergency medicine moral injury is characterized by rapid-cycling mixed damage — alternating boundary crossings and non-crossings within single shifts — producing a distinctive $\beta_k$ profile of generalized moderate numbing with dimension-specific hypervigilant spikes. This pattern is distinct from the three primary patterns (pandemic: sustained acute; palliative: chronic gradual; psychiatry: conflicted) and requires its own measurement and intervention strategy.*

The emergency medicine pattern supports the framework's central claim: moral injury is not a single construct but a family of related pathologies, distinguished by their boundary-crossing patterns, damage modes, and $\beta_k$ profiles. Scalar measurement collapses these distinctions; vector measurement preserves them.

---

## 14.5 Cross-Setting Comparison

### The Moral Injury Taxonomy

[Figure 14.2: Three-panel comparison showing the moral injury vector, dominant damage mode, and characteristic trajectory for each clinical setting]

| Feature | Pandemic ICU | Palliative Care | Psychiatry |
|---|---|---|---|
| **Dominant boundary** | $\beta_{\text{abandon}}$ | $\beta_{\text{futile}}$ | $\beta_{\text{consent}}$ |
| **Crossing frequency** | High (acute) | Moderate (chronic) | Moderate (intermittent) |
| **Damage mode** | Mixed (hypervigilance → numbing) | Moral numbing | Conflicted heuristic |
| **MI vector** | $(0, +, 0, ++, 0)$ | $(0, ++, +, 0, 0)$ | $(0, 0, ++, 0, 0)$ |
| **Time course** | Weeks (crisis-driven) | Years (career-long) | Months to years |
| **Key predictor** | Triage decision frequency | Duration in specialty | Involuntary commitment count |
| **Intervention** | Triage committee, lottery | Rotation, ethics support | Supervision, autonomy-maximizing protocols |

### Measurement Implications

The three-setting taxonomy has implications for how moral injury should be measured. The existing instruments — MISS-HP (Moral Injury Symptom Scale for Health Professionals) and MDS-R (Moral Distress Scale–Revised) — are scalar measures: they produce a single score. The geometric framework predicts that scalar moral injury instruments will fail to distinguish between the three setting-specific patterns.

**Prediction 14.6 (Setting-Specific MI Patterns).** *Clinicians in different settings should show different profiles on a multi-dimensional moral injury instrument that measures boundary-specific damage. The MISS-HP, as a scalar instrument, will show elevated scores in all three settings but will not distinguish between the settings' characteristic patterns. A vector-valued instrument that measures $\beta_k$-specific changes would show setting-specific profiles.*

This prediction is testable: administer both the MISS-HP (scalar) and a boundary-specific instrument (vector) to clinicians in pandemic ICU, palliative care, and psychiatry settings, and test whether the vector instrument distinguishes settings that the scalar instrument conflates.

---

## 14.5 COVID-19 as Natural Experiment: Detailed Analysis

### The Pandemic Triage Setting Expanded

The COVID-19 pandemic provided an unprecedented natural experiment for the moral injury framework. Across thousands of hospitals in dozens of countries, clinicians were simultaneously exposed to boundary crossings that the framework's predictions address.

**Boundary crossing 1: Denying ventilators ($\beta_{\text{abandon}}$).**

The most dramatic boundary crossing: a clinician tells a patient (or the patient's family) that a ventilator is not available. The clinician has been trained — their $h(n)$ has been calibrated through years of medical education — to provide treatment to every patient who needs it. The denial violates this calibration.

The framework predicts that the MI from ventilator denial should be proportional to the clinician's $\beta_{\text{abandon}}$ and inversely proportional to the perceived fairness of the allocation process ($d_8$: institutional legitimacy). A clinician who denies a ventilator under a transparent, pre-established, committee-based protocol should experience less MI than a clinician who denies a ventilator based on their individual judgment — because the former has lower $\Delta d_8$ (the institution bears the boundary-crossing cost) while the latter bears the full cost on their personal manifold.

**Boundary crossing 2: Restricting family visitation ($\beta_{\text{dignity}}$).**

The pandemic required restricting family access to dying patients — an intervention that crossed the dignity boundary ($d_7$) and the social impact boundary ($d_6$). Patients died alone. Families could not say goodbye. Video calls replaced bedside presence.

The MI from visitation restriction is distinct from the MI from ventilator denial: it does not cross the abandonment boundary (the clinician is still providing care) but it crosses the dignity and social boundaries repeatedly. The framework predicts that this MI should accumulate gradually (daily crossings) and produce numbing on $\beta_{\text{dignity}}$ — clinicians who initially found the visitation restriction devastating eventually processed it as routine.

**Boundary crossing 3: Decision-making under extreme uncertainty (degraded $d_9$).**

In the early months of the pandemic, prognostic accuracy for COVID-19 was poor. Clinicians were making triage decisions — allocating ventilators, assigning patients to ICU vs. floor — based on uncertain estimates of survival probability. The uncertainty itself is a form of manifold damage: the clinician's $d_9$ (epistemic status) is degraded, meaning that the edge weights in the clinical decision complex are unreliable.

Making high-stakes decisions with unreliable edge weights is intrinsically more costly than making the same decisions with reliable weights — the expected suboptimality of the chosen path is higher. The framework predicts that MI from decisions under uncertainty should correlate with the degree of prognostic uncertainty, independent of the clinical outcome.

### What the Pandemic Literature Shows

The empirical literature on COVID-19 moral injury is substantial and broadly consistent with the framework's predictions:

- **Greenberg et al. (2020)**: Healthcare workers during the pandemic reported high levels of moral distress, with themes including inability to provide optimal care, witnessing patients die alone, and feeling that institutional protocols were inadequate. These themes map onto $\beta_{\text{abandon}}$, $\beta_{\text{dignity}}$, and $d_8$ (institutional legitimacy) respectively.

- **Rushton et al. (2021)**: Found that moral resilience — measured by the Rushton Moral Resilience Scale — was negatively correlated with moral distress but not with burnout, supporting the MI-burnout distinction.

- **Mantri et al. (2020)**: Found that MISS-HP scores were elevated among healthcare workers exposed to COVID-19 patients, with the highest scores among those making allocation decisions — consistent with the prediction that triage decisions (boundary crossings) are the primary driver.

- **Shale (2020)**: Described the "moral injury" of healthcare workers as distinct from burnout, using language remarkably close to the geometric framework's formulation: "a deep sense that one has violated one's own moral code" — which is precisely the experience of crossing a boundary where $\beta_k^{(\text{clin})} > \tau$.

---

## 14.6 Sarah Across Three Settings

### Pandemic ICU (Month 1)

Sarah's pandemic experience was detailed in Chapter 10. Her moral injury vector after the pandemic:

$$\vec{\text{MI}}_{\text{pandemic}} = (\text{MI}_{\text{harm}} = 0, \text{MI}_{\text{futile}} = 12, \text{MI}_{\text{consent}} = 0, \text{MI}_{\text{abandon}} = 47, \text{MI}_{\text{sacred}} = 0)$$

Dominant injury: abandonment boundary crossings from triage decisions. Damage mode: hypervigilance followed by numbing on $\beta_{\text{abandon}}$.

### Palliative Care Rotation (Month 6)

Six months after the pandemic, Sarah rotates through palliative care. She watches Dr. Nakamura, a senior palliative care attending with fifteen years of experience, manage a case that disturbs Sarah deeply.

A 91-year-old man with metastatic pancreatic cancer, predicted survival of two weeks, is receiving full-code care at his daughter's insistence. The patient is nonverbal, possibly in pain, and has no advance directive. Dr. Nakamura orders another round of IV antibiotics, adjusts the ventilator settings, and moves to the next patient.

Sarah asks: "Shouldn't we have a goals-of-care conversation with the daughter?"

Dr. Nakamura pauses. "We've had three," he says. "She's not ready."

Sarah watches Dr. Nakamura move through the rest of his patients — three more in similar situations — with efficient, compassionate competence. No visible distress. No hesitation. No moral friction.

Later, over coffee, Sarah asks Dr. Nakamura how he manages the moral weight of continuing futile treatment. He is quiet for a long moment.

"I used to feel it," he says. "Every case. Every family that wanted everything. I'd go home and think about it. I don't do that anymore."

Sarah recognizes the trajectory: hypervigilance (he felt it once), followed by numbing (he does not feel it now). She does not know whether Dr. Nakamura's equanimity is genuine expertise or moral numbing. The framework distinguishes the two — but the distinction requires longitudinal $\beta_k$ measurement that is not available to her.

Her palliative care moral injury vector:

$$\vec{\text{MI}}_{\text{palliative}} = (\text{MI}_{\text{harm}} = 0, \text{MI}_{\text{futile}} = 8, \text{MI}_{\text{consent}} = 3, \text{MI}_{\text{abandon}} = 0, \text{MI}_{\text{sacred}} = 0)$$

Moderate injury from futility boundary crossings; small contribution from consent boundary in incapacitated patients.

### Psychiatry Rotation (Month 9)

Sarah restrains Mr. Torres (Chapter 9, Case 3). She experiences the split heuristic firsthand:

$\beta_{\text{consent}}^{(\text{institutional})}$: "This patient is psychotic, dangerous, and unable to consent. Restraint is necessary and justified."

$\beta_{\text{consent}}^{(\text{personal})}$: "I am holding down a screaming human being while another person injects him with a drug he does not want. This is violence."

Both assessments are correct. The clinical justification is sound (Chapter 9 proved this). The personal assessment is also accurate — the act is a form of coercion, regardless of its clinical justification. The moral injury occurs in the gap between the two assessments.

Her psychiatry moral injury vector:

$$\vec{\text{MI}}_{\text{psychiatry}} = (\text{MI}_{\text{harm}} = 0, \text{MI}_{\text{futile}} = 0, \text{MI}_{\text{consent}} = 15, \text{MI}_{\text{abandon}} = 0, \text{MI}_{\text{sacred}} = 0)$$

Concentrated injury from consent boundary crossings.

### The Composite Vector

Sarah's total moral injury vector after all three rotations:

$$\vec{\text{MI}}_{\text{total}} = (0, 20, 18, 47, 0)$$

The vector tells a story that a scalar MI score cannot: Sarah's moral injury is concentrated on the abandonment dimension (pandemic triage) with substantial contributions from futility (palliative care) and consent (psychiatry). Her $h(n)$ has been altered on three different boundaries, each in a different setting, each producing a different damage pattern. A scalar MI score would report a single number — "Sarah has moderate-to-severe moral injury" — and lose the dimensional structure that determines which interventions might help.

Sarah needs different support for each component: structured debriefing for the abandonment injury, ethical supervision for the futility injury, and autonomy-maximizing protocol training for the consent injury. A scalar diagnosis produces a scalar treatment; a vector diagnosis produces a targeted intervention.

---

## Chapter Summary

Three clinical settings — pandemic ICU, palliative care, and psychiatry — produce structurally distinct moral injury patterns. The pandemic ICU produces acute, high-frequency boundary crossings on the abandonment dimension, with a characteristic trajectory from hypervigilance to moral numbing. Palliative care produces chronic, gradual boundary crossings on the futility dimension, with the Palliative Paradox: the setting that most needs intact moral sensitivity is the setting most likely to erode it. Psychiatry produces conflicted boundary crossings on the consent dimension, where the clinician simultaneously agrees with and is morally injured by the clinically justified intervention. The three-setting taxonomy demonstrates that "moral injury" is not a single construct but a multi-dimensional pattern requiring setting-specific assessment and intervention — and that scalar MI instruments will fail to distinguish patterns that a vector-valued approach captures.

---

[^1]: The hypervigilance-to-numbing trajectory in pandemic ICU settings mirrors the PTSD literature's observation of initial hyperarousal followed by emotional numbing in trauma survivors. The geometric framework provides a mechanism — $\beta_k$ inflation followed by $\beta_k$ deflation — that generates both responses as opposite phases of the same process.

[^2]: The distinction between moral numbing and genuine expertise (Definition 14.1) is clinically crucial but empirically difficult. The framework predicts that a calibrated clinician's sensitivity (correctly identifying boundary cases) increases over time, while a numbed clinician's sensitivity decreases. This prediction is testable using clinical vignettes that probe boundary sensitivity, administered longitudinally.

[^3]: The conflicted heuristic in psychiatry (Definition 14.2) has not, to my knowledge, been characterized in the existing moral injury literature. The dual $\beta_k$ structure — institutional and personal estimates of the same boundary penalty — may explain why psychiatric moral injury is qualitatively different from ICU or palliative moral injury and why interventions designed for one setting may not transfer to another.
