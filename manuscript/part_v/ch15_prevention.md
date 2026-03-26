# Chapter 15: Preventing and Repairing Moral Injury

> *"If moral injury is heuristic damage, then prevention is heuristic protection — and the institution, not the individual, must provide it."*

---

The Moral Injury Accumulation Theorem (Chapter 13) states that moral injury is cumulative, irreversible above threshold, and structurally distinct from burnout. This is honest but not hopeless. The theorem also implies that moral injury is prospectively predictable — the Moral Injury Index can estimate a policy's moral injury burden before implementation — and that institutional design can reduce the frequency and severity of forced boundary crossings. The question is not whether moral injury can be eliminated (it cannot — clinical medicine necessarily involves boundary crossings) but whether institutions can be designed so that $\text{MI}(T) < \text{MI}_{\text{crit}}$ for the clinicians who work within them.

This chapter addresses institutional design, ethics support, and individual resilience through the geometric lens. If moral injury is $h(n)$-damage, then prevention is $h(n)$-protection, and the tools of protection must target the specific mechanisms of damage: forced boundary crossing, heuristic inflation, heuristic deflation, and the accumulation of boundary-crossing residue.

---

## 15.1 The Institutional Responsibility

### Why Prevention Is an Institutional Problem

A persistent misconception frames moral injury as an individual resilience problem: some clinicians are "tougher" and can handle boundary crossings; others are "more vulnerable" and break down. The geometric framework rejects this framing.

Moral injury is not a function of individual weakness. It is a function of institutional policy. The moral injury increment $\Delta \text{MI}(t) = \max(0, \beta_k^{(\text{clin})} - \tau) \cdot \mathbf{1}[\text{boundary } k \text{ crossed}]$ has two components: the clinician's boundary penalty ($\beta_k^{(\text{clin})}$, which reflects their moral sensitivity and is generally a positive trait) and the institutional mandate to cross the boundary ($\mathbf{1}[\text{boundary } k \text{ crossed}]$, which is a policy decision).

The institution controls the second component. A policy that minimizes unnecessary boundary crossings reduces $\text{MI}$ for all clinicians — those with high $\beta_k$ (who are protected from crossings that exceed their threshold) and those with moderate $\beta_k$ (who accumulate less total MI even if individual crossings are below threshold).

**Proposition 15.1 (Prevention Is Institutional).** *The primary determinant of clinician moral injury is institutional policy, not individual resilience. The Moral Injury Index $\text{MI}(P)$ is a property of the policy $P$, not a property of the clinician. Institutional design that reduces $\text{MI}(P)$ protects all clinicians; individual resilience training that increases $\tau$ protects only the trained individuals and does not reduce the structural moral injury imposed by the policy.*

This proposition shifts the burden of prevention from the individual ("clinicians need resilience training") to the institution ("policies need moral injury assessment"). Both are valuable, but the institutional lever is primary.

---

## 15.2 Four Design Principles for Moral Injury Prevention

### Principle 1: Minimize Unnecessary Boundary Crossings

Not all boundary crossings are necessary. Many policies force clinicians across boundaries that could be avoided by policy redesign.

**Example: Triage by individual physician vs. triage committee.**

When a triage protocol requires individual physicians to deny resources to their own patients, each denial crosses the abandonment boundary ($\beta_{\text{abandon}}$) for the physician with a direct therapeutic relationship. When the same triage decision is made by a committee that has no prior relationship with any of the patients, the abandonment boundary is not crossed — because the committee members have no therapeutic relationship to abandon.

The clinical outcome is identical. The moral injury is lower. The boundary crossing was unnecessary — it was an artifact of the policy's assignment of decision authority to the treating physician rather than to a separate triage committee.

**Example: Lottery vs. criterion-based allocation among similar-prognosis patients.**

When patients have comparable prognoses, a criterion-based allocation (by age, social value, or other discriminator) crosses the justice boundary ($\beta_{\text{justice}}$). A lottery does not — it treats all patients equally. The clinical outcome is approximately equivalent ($d_1$ differential is within measurement error). The boundary crossing was unnecessary.

**Design guideline**: For every boundary crossing mandated by a policy, ask: *Is this crossing necessary for the clinical objective?* If removing the boundary crossing would not substantially change $d_1$ outcomes, remove it. The manifold cost of unnecessary boundary crossings accrues to the clinician workforce as moral injury without any offsetting clinical benefit.

### Principle 2: Distribute Boundary Crossings Equitably

When boundary crossings are necessary, they should be distributed across the clinician workforce rather than concentrated on a few individuals.

**Example: Triage rotation.**

During a pandemic surge, triage decisions are made daily. If the same physician makes every triage decision (because they are the most senior, the most experienced, or the most willing), their $\text{MI}(T)$ accumulates rapidly while their colleagues' $\text{MI}(T)$ remains low. Rotating the triage responsibility — each physician takes a triage shift on a regular schedule — distributes the boundary crossings and prevents any individual from exceeding $\text{MI}_{\text{crit}}$.

**Example: End-of-life conversations.**

In many ICUs, the most difficult conversations (withdrawal of life support, transition to comfort care) are assigned to the most senior physician. This concentrates the $\beta_{\text{abandon}}$ and $\beta_{\text{dignity}}$ crossings on one person. Distributing these conversations — with adequate supervision and support — reduces the moral injury concentration.

**Design guideline**: Map the boundary crossings mandated by a policy and identify whether they are concentrated on specific individuals or roles. If concentrated, redistribute. The total $\text{MI}$ across the workforce is the same (the same number of boundary crossings must occur), but no individual exceeds their critical threshold.

### Principle 3: Provide Boundary-Crossing Support in Real Time

When boundary crossings are necessary and equitably distributed, the institution should provide support at the moment of crossing — not days or weeks later.

**Example: Immediate debrief after triage decisions.**

After a clinician makes a triage decision that crosses a moral boundary, a brief structured debrief (10–15 minutes) within the same shift can reduce the moral injury increment. The debrief does not erase the boundary crossing — the heuristic alteration is real — but it provides:

1. **Validation**: Acknowledgment that the crossing was morally costly and that the clinician's distress is appropriate.
2. **Contextualization**: Placement of the crossing within the institutional framework — "the protocol required this; you did not choose it."
3. **Heuristic recalibration**: Explicit comparison of the clinician's $\beta_k$ response with the protocol's justification, providing an opportunity for conscious recalibration that may prevent the $\beta_k$ from inflating (hypervigilance) or deflating (numbing) beyond its appropriate range.

**Design guideline**: Debrief after every morally costly decision, not quarterly. Moral injury is cumulative; recalibration must be frequent enough to prevent $\beta_k$ drift between debrief sessions.

### Principle 4: Separate $g(n)$ and $h(n)$ Support Systems

Burnout ($g(n)$-depletion) and moral injury ($h(n)$-damage) require different support systems. Institutions that conflate the two — offering "wellness programs" that address staffing (burnout) but not ethics (moral injury) — provide the wrong treatment for half the problem.

**$g(n)$ support (burnout prevention):**
- Adequate staffing ratios
- Reasonable work hours
- Protected time off
- Physical wellness resources
- Peer support groups focused on workload management

**$h(n)$ support (moral injury prevention):**
- Ethics consultation availability
- Structured debrief after morally costly decisions
- Prospective Moral Injury Index assessment of new policies
- Triage committee structures that reduce individual boundary-crossing burden
- Moral resilience training (see Section 15.4)

**Design guideline**: Audit the institution's "clinician wellness" program. Does it address both $g(n)$ and $h(n)$? If the program consists entirely of yoga classes, meditation apps, and scheduling flexibility, it addresses burnout but not moral injury. Add ethics consultation, structured debrief, and prospective MI assessment.

---

## 15.3 Ethics Consultations as Heuristic Recalibration

### The Mechanism of Recalibration

Ethics consultations — including formal ethics committee consultations, clinical ethics debriefs, and Morbidity and Mortality (M&M) conferences — function as heuristic recalibration mechanisms in the geometric framework.

**Definition 15.1 (Heuristic Recalibration).** *An ethics consultation provides heuristic recalibration when it restores the clinician's boundary penalties $\beta_k$ toward their $\varepsilon$-admissible values — correcting both inflation (hypervigilance) and deflation (numbing) without eliminating appropriate boundary sensitivity.*

The key phrase is "without eliminating appropriate boundary sensitivity." The goal is not to make boundary crossings painless — that would be moral numbing. The goal is to maintain the clinician's $\beta_k$ at the level that produces optimal pathfinding on the manifold: high enough to avoid unnecessary crossings, low enough to allow necessary ones.

### What Effective Recalibration Looks Like

**For hypervigilant clinicians ($\beta_k$ inflated):**

The ethics consultation identifies the specific boundary that has been inflated and provides calibrated information about the boundary's true cost. A clinician who has developed an inflated $\beta_{\text{abandon}}$ after a traumatic triage decision needs to hear: "The boundary has a real cost, and your distress is appropriate. But the boundary's cost does not extend to every patient interaction — you can discharge a patient who is ready without crossing the abandonment boundary."

The recalibration is *specific*: it addresses the inflated boundary without deflating other boundaries. It reduces $\beta_{\text{abandon}}$ toward its pre-injury value without affecting $\beta_{\text{consent}}$, $\beta_{\text{futile}}$, or other boundary penalties.

**For morally numbed clinicians ($\beta_k$ deflated):**

The ethics consultation identifies the boundary that has been deflated and provides cases where the boundary was appropriately valued. A clinician who has developed a deflated $\beta_{\text{futile}}$ after years of palliative care needs to hear: "This case is different from the ones where continuing treatment was appropriate. The patient has no prospect of benefit. The family's request does not override the patient's right to a dignified death."

The recalibration *re-sensitizes* the boundary — restoring the penalty that habitual crossing has eroded.

### The Framework's Prediction About Effective Ethics Consultation

**Prediction 15.1 (Ethics Consultation Reduces $\beta_k$ Variance).** *Effective ethics consultation should reduce the variance of $\beta_k$ estimates in the clinician population — making heuristics more consistent across clinicians — without reducing the mean — maintaining appropriate average boundary sensitivity.*

Formally: Let $\sigma^2_{\beta_k}(\text{pre})$ be the variance of $\beta_k$ estimates across clinicians before ethics consultation, and $\sigma^2_{\beta_k}(\text{post})$ be the variance after. The prediction is:

$$\sigma^2_{\beta_k}(\text{post}) < \sigma^2_{\beta_k}(\text{pre}) \quad \text{while} \quad \overline{\beta_k}(\text{post}) \approx \overline{\beta_k}(\text{pre})$$

The variance reduction corresponds to making the clinician population more consistent in their moral judgments (convergence of inflated and deflated heuristics toward the mean). The mean preservation corresponds to maintaining appropriate overall sensitivity.

This prediction is testable: survey clinicians' $\beta_k$ estimates before and after a structured ethics consultation series and measure the change in variance and mean.

---

## 15.4 Moral Resilience in the Geometric Framework

### Rushton's Moral Resilience, Formalized

Cynda Rushton (2018) defined moral resilience as "the capacity of an individual to sustain or restore their integrity in response to moral complexity, confusion, distress, or setbacks." In the geometric framework, moral resilience is the maintenance of $\varepsilon$-admissible $h(n)$ despite boundary crossings below threshold.

**Definition 15.2 (Geometric Moral Resilience).** *A clinician exhibits moral resilience when:*

*1. Boundary penalties remain stable: $|\beta_k^{(t)} - \beta_k^{(0)}| < \varepsilon_{\text{resilience}}$ for all $k$ and all $t$ up to a critical accumulation threshold.*

*2. Heuristic admissibility is maintained: $h(n)$ remains $\varepsilon$-admissible — the clinician continues to find near-optimal paths on the manifold despite accumulated moral cost.*

*3. Professional identity is intact: $d_7$ (dignity and identity) on the clinician's own manifold remains above threshold — the clinician continues to identify as a competent, ethical professional.*

### Resilience vs. Numbing: The Precise Distinction

Moral resilience and moral numbing can look similar from the outside: both produce a clinician who continues to function competently after boundary crossings. The geometric framework provides the distinguishing criterion:

- **Resilience**: $\beta_k$ remains stable. The clinician processes the boundary crossing, integrates it into their moral framework, and maintains the boundary penalty at its calibrated level. The clinician *feels* the cost of the crossing but does not allow it to permanently alter their heuristic.

- **Numbing**: $\beta_k$ deflates. The clinician processes the boundary crossing by reducing the perceived cost of the boundary. The clinician *stops feeling* the cost — not because they have integrated it but because they have suppressed it.

The test: present the clinician with a boundary case identical to ones they have crossed repeatedly. A resilient clinician will still report moral distress (appropriate $\beta_k$). A numbed clinician will not (deflated $\beta_k$). The resilient clinician's distress is not weakness — it is the correct output of a well-calibrated heuristic function.

### Building Moral Resilience: What the Framework Prescribes

The geometric framework suggests that moral resilience training should focus on three capabilities:

**Capability 1: Boundary awareness.** The clinician learns to identify which boundaries are being crossed, on which dimensions, with what penalties. This is metacognitive — the clinician observes their own heuristic function rather than being passively driven by it.

**Capability 2: Conscioous recalibration.** When the clinician notices that $\beta_k$ has shifted (either inflated or deflated), they can consciously adjust — not by suppressing the shift but by comparing their current $\beta_k$ with their pre-injury reference value and identifying whether the shift reflects genuine recalibration (the boundary's true cost has changed) or heuristic damage (the boundary's perceived cost has changed without a change in true cost).

**Capability 3: Source attribution.** The clinician learns to distinguish between forced boundary crossings (imposed by institutional policy — moral injury) and voluntary boundary crossings (part of the clinician's own geodesic computation — not moral injury). Forced crossings produce moral injury; voluntary crossings do not. A clinician who performs a risky surgery that they believe is the right decision for the patient has crossed the harm boundary voluntarily — this is clinical courage, not moral injury. A clinician who performs a triage decision that they believe is wrong has crossed the abandonment boundary involuntarily — this is moral injury.

---

## 15.5 Institutional Design: Concrete Recommendations

### For Pandemic Preparedness

1. **Pre-establish triage committees.** Before a pandemic, designate a rotating triage committee that will make allocation decisions during crisis standards of care. Train the committee in manifold-aware triage (Chapter 10). Ensure that treating clinicians do not make triage decisions for their own patients.

2. **Compute the Moral Injury Index for the crisis protocol.** Before implementing crisis standards of care, estimate $\text{MI}(P)$ by surveying the clinician workforce for $\beta_k$ distributions and analyzing the protocol for boundary-crossing scenarios. If $\text{MI}(P) > \text{MI}_{\text{crit}}$, redesign the protocol.

3. **Implement lottery tiebreaking.** For patients with similar prognoses, use lottery allocation rather than criterion-based allocation. This reduces $\beta_{\text{justice}}$ crossings without affecting $d_1$ outcomes.

4. **Schedule real-time debrief.** After every triage decision, the deciding clinician (or committee member) receives a 10–15 minute structured debrief within the same shift. Not optional. Not quarterly. Every time.

5. **Rotate triage duty.** No clinician makes triage decisions for more than three consecutive shifts. Rotation distributes $\text{MI}$ across the workforce.

### For Palliative Care Programs

1. **Limit continuous assignment duration.** Clinicians should not work exclusively in palliative care for more than two consecutive years without a rotation to a different clinical setting. Rotation provides $\beta_{\text{futile}}$ recalibration opportunities.

2. **Implement scheduled ethics review.** Monthly (not crisis-triggered) case review sessions where the palliative care team examines recent cases for possible moral numbing: "Would we have made the same decision five years ago? If not, has the clinical situation changed or has our sensitivity changed?"

3. **Pair experienced and novice clinicians.** The novice's intact $\beta_{\text{futile}}$ provides a reference for the experienced clinician's potentially deflated $\beta_{\text{futile}}$. If the novice shows distress at a case that the experienced clinician finds routine, the discrepancy is diagnostic.

### For Psychiatric Services

1. **Autonomy-maximizing protocols.** For every involuntary intervention (restraint, forced medication, seclusion), require documentation of why less restrictive alternatives were insufficient. The documentation forces the clinician to demonstrate that the boundary crossing was minimized — reducing $d_4$ cost and therefore reducing $\Delta \text{MI}$.

2. **Clinical supervision for autonomy boundary crossings.** After every involuntary intervention, the clinician discusses the case with a supervisor — not to second-guess the decision but to process the moral cost of the crossing. The supervisor helps the clinician maintain the distinction between institutional justification ($\beta_{\text{consent}}^{(\text{institutional})}$ appropriately low) and personal response ($\beta_{\text{consent}}^{(\text{personal})}$ appropriately high) without allowing either to dominate.

3. **Patient feedback integration.** When patients recover capacity, ask about their experience of involuntary treatment. Patient expressions of gratitude ("I'm glad you stopped me") provide genuine recalibration data — evidence that the boundary crossing was beneficial from the patient's calibrated perspective, even though it was resisted from the patient's uncalibrated perspective.

### For All Clinical Settings

1. **Audit existing wellness programs for $h(n)$ support.** If the program addresses only burnout ($g(n)$-depletion), add moral injury ($h(n)$-damage) components: ethics consultation, structured debrief, $\beta_k$ monitoring.

2. **Measure moral injury, not just burnout.** Use both MBI (burnout) and MISS-HP (moral injury) in clinician wellness assessments. Track separately. Intervene separately.

3. **Prospective Moral Injury Index for new policies.** Before implementing any new clinical policy, compute $\text{MI}(P)$. If the Index exceeds a threshold, require policy redesign before implementation.

---

## 15.6 The Role of Institutional Culture

### Culture as Ambient $\beta_k$ Calibration

Beyond specific policies and interventions, the institution's culture — its unwritten norms, its informal hierarchies, its collective attitudes toward moral cost — functions as an ambient $\beta_k$ calibration environment. A culture that acknowledges moral cost ("triage is hard, and your distress is appropriate") maintains higher $\beta_k$ sensitivity than a culture that denies it ("this is what we signed up for — toughen up").

**Definition 15.4 (Morally Sustaining Culture).** *An institutional culture is morally sustaining when it:*

*1. Acknowledges moral cost: Boundary crossings are recognized as inherently costly, not as routine events to be processed without comment.*

*2. Distributes moral cost visibly: The clinicians who bear the most moral cost are identified and supported, rather than being expected to absorb the cost silently.*

*3. Separates moral cost from personal weakness: Moral distress is recognized as the appropriate response of a well-calibrated heuristic, not as a sign of insufficient resilience.*

*4. Provides recalibration infrastructure: Ethics consultations, debriefs, and peer support are structurally embedded in the clinical workflow, not available only in crisis.*

### The "Toughen Up" Failure Mode

The most common institutional failure mode for moral injury is the "toughen up" culture: the implicit expectation that clinicians should absorb boundary crossings without distress. This culture has three damaging effects:

1. **It pathologizes appropriate moral sensitivity.** Clinicians who experience distress after triage decisions are told (implicitly or explicitly) that their distress reflects inadequate preparation or insufficient commitment. The message is: your $\beta_k$ is too high; good clinicians have lower boundary penalties. This encourages moral numbing as a survival strategy.

2. **It prevents early detection.** Clinicians in a "toughen up" culture do not report moral distress — they hide it, because reporting is interpreted as weakness. The proxy indicators for approaching $\text{MI}_{\text{crit}}$ (Section 13.7) are suppressed, preventing early intervention.

3. **It concentrates moral cost on vulnerable individuals.** In a culture that does not distribute moral cost visibly, the cost falls disproportionately on junior clinicians (who have less institutional power to resist boundary-crossing mandates), female clinicians (who are culturally expected to perform more emotional labor), and minority clinicians (who may face additional boundary crossings related to institutional racism).

**Proposition 15.2 (The "Toughen Up" Culture Maximizes Moral Injury).** *An institutional culture that discourages the expression of moral distress maximizes cumulative moral injury in the clinician workforce, because it prevents recalibration (no debriefs, no ethics consultations sought), promotes numbing (clinicians reduce $\beta_k$ to avoid the social cost of distress), and prevents early detection (clinicians approaching $\text{MI}_{\text{crit}}$ are not identified).*

The proposition implies that cultural change — from "toughen up" to morally sustaining — is one of the most impactful institutional interventions for moral injury prevention. It is also one of the hardest, because culture is not a policy that can be rewritten by committee but a set of norms that must be changed through sustained leadership, modeling, and structural reinforcement.

### Measurement of Institutional Moral Culture

The framework suggests that institutional moral culture can be measured by proxy:

- *Moral distress reporting rate*: The proportion of clinicians who report moral distress when surveyed confidentially. A low rate in a high-boundary-crossing environment suggests cultural suppression, not absence of distress.

- *Ethics consultation utilization*: The frequency of ethics consultation requests per 1000 patient-days. Low utilization in a complex clinical environment suggests either that ethics support is unavailable or that the culture discourages seeking it.

- *$\beta_k$ variance across seniority levels*: If junior and senior clinicians have similar $\beta_k$ profiles, the culture maintains calibration across career stages. If senior clinicians have systematically lower $\beta_k$ (deflation through experience or numbing), the culture may be producing cumulative moral injury rather than genuine expertise.

---

## 15.7 The Limits of Repair

### What Cannot Be Undone

The Moral Injury Accumulation Theorem states that MI is irreversible above $\text{MI}_{\text{crit}}$. The framework is honest about this: some moral injuries cannot be undone.

A clinician who has crossed the abandonment boundary forty-seven times during a pandemic — who has told forty-seven patients or families that a life-saving resource is not available — carries a permanently altered $\beta_{\text{abandon}}$. No debrief, no ethics consultation, no resilience training can restore the pre-pandemic heuristic. The boundary has been crossed too many times. The heuristic has been permanently rewritten.

This is not a failure of the framework. It is a prediction of the framework — a prediction that should inform institutional design. If the framework is correct, the primary institutional objective is *prevention* (keeping $\text{MI}(T) < \text{MI}_{\text{crit}}$), not *cure* (restoring damaged heuristics). The emphasis on prevention is not pessimistic; it is realistic.

### Functional Adaptation for Clinicians Above Threshold

For clinicians whose $\text{MI}(T)$ exceeds $\text{MI}_{\text{crit}}$, the goal shifts from restoration to functional adaptation: developing compensatory strategies that produce near-optimal clinical paths despite permanently altered heuristics.

**Definition 15.3 (Functional Adaptation).** *A clinician with $\text{MI}(T) > \text{MI}_{\text{crit}}$ achieves functional adaptation when they:*

*1. Recognize their altered $\beta_k$ profile — aware of which boundaries are inflated (hypervigilance) and which are deflated (numbing).*

*2. Compensate consciously — using deliberate $d_9$-mediated reasoning to override the damaged heuristic in situations where the damage would produce suboptimal decisions.*

*3. Maintain adequate clinical performance — despite permanently altered heuristics, the clinician produces paths that are $\varepsilon'$-optimal, where $\varepsilon' > \varepsilon$ (the tolerance is wider) but still clinically acceptable.*

Functional adaptation is not the same as recovery. The clinician's heuristic is permanently altered. But with conscious compensation, the altered heuristic can produce acceptable clinical decisions — not optimal (the damage prevents optimality) but adequate (the conscious compensation narrows the gap between the damaged heuristic and the optimal path).

---

## 15.7 Sarah's Repair

After the pandemic, Sarah participates in a structured debrief program — twelve sessions over six months, facilitated by a clinical ethicist and a psychologist.

Session 3: Sarah identifies her inflated $\beta_{\text{abandon}}$. She realizes that she has been over-triaging since the pandemic — holding ICU beds in reserve, delaying discharges, requesting unnecessary consultations. Each behavior is driven by the inflated boundary penalty: her heuristic overestimates the cost of releasing a patient who might deteriorate.

Session 6: Sarah identifies her deflated $\beta_{\text{dignity}}$. She realizes that she no longer flinches when patients die without family present — a boundary crossing that devastated her during the pandemic but now feels routine. The debrief facilitator points out the deflation: "You used to advocate fiercely for family presence at the end of life. When did you stop?"

Session 9: Sarah practices conscious compensation. In a triage simulation, she notices her inflated $\beta_{\text{abandon}}$ pushing her toward over-conservative allocation. She overrides the heuristic: "My gut says hold the ventilator. But my gut is wrong — it's been wrong since the pandemic. The clinical evidence says this patient doesn't need it."

Session 12: Sarah assesses her trajectory. Her $\beta_{\text{abandon}}$ is still inflated — the debrief did not erase it. Her $\beta_{\text{dignity}}$ is partially restored — the debrief re-sensitized her to the boundary, though not to its pre-pandemic level. She is not the clinician she was before the pandemic. She is a different pathfinder on the same manifold.

She does not know whether she is better or worse. She knows she is different. And she knows that the difference is not random — it is the predictable consequence of forty-seven boundary crossings that the institution required and that her heuristic could not absorb without permanent alteration.

The institution cannot give her back the clinician she was. What it can give her — and what the debrief program provides — is the vocabulary to name what happened, the metacognitive tools to compensate for the damage, and the institutional commitment not to let it happen again without at least counting the cost.

---

## Chapter Summary

If moral injury is $h(n)$-damage, prevention must target the mechanisms of damage: forced boundary crossing, heuristic inflation, and heuristic deflation. Four institutional design principles emerge: minimize unnecessary boundary crossings (redesign policies to avoid crossings that do not serve clinical objectives), distribute necessary boundary crossings equitably (rotate triage duty, distribute difficult conversations), provide boundary-crossing support in real time (debrief after every morally costly decision, not quarterly), and separate $g(n)$ and $h(n)$ support systems (burnout prevention and moral injury prevention are different problems requiring different interventions). Ethics consultations function as heuristic recalibration — restoring inflated or deflated $\beta_k$ toward $\varepsilon$-admissible values — and should reduce $\beta_k$ variance without reducing mean sensitivity. Moral resilience is the maintenance of stable $\beta_k$ despite boundary crossings below threshold, distinguishable from moral numbing by the persistence of appropriate boundary sensitivity. For clinicians above $\text{MI}_{\text{crit}}$, the goal shifts from restoration (which is impossible) to functional adaptation — conscious compensation for permanently altered heuristics. The institutional lever is primary: policy redesign reduces moral injury for all clinicians, while individual resilience training protects only the trained.

---

[^1]: The principle of "debrief after every morally costly decision" may seem impractical in crisis conditions. The framework's response: the alternative — not debriefing and allowing $\beta_k$ drift to produce moral numbing or hypervigilance — is more costly in the long run. A 10-minute debrief costs less than a permanently damaged clinician.

[^2]: The recommendation to compute the Moral Injury Index prospectively for new policies parallels the requirement for environmental impact assessment before major construction projects. Both are prospective assessments of harm that institutional policy will produce, computed before the harm occurs.

[^3]: Functional adaptation for clinicians above $\text{MI}_{\text{crit}}$ is not unique to moral injury. Clinicians who develop physical disabilities during their careers routinely develop compensatory strategies that maintain clinical competence despite permanently altered function. The framework's contribution is identifying that the same adaptation process applies to heuristic damage — and that the adaptation is possible because conscious reasoning ($d_9$-mediated deliberation) can partially substitute for automatic heuristic evaluation ($h(n)$-driven pathfinding).
