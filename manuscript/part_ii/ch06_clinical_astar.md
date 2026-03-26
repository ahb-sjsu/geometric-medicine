# Chapter 6: Clinical Reasoning as A* Pathfinding

*Part II: The Framework*

---

> *"Clinical judgment is not a black box. It is a search algorithm with a well-calibrated heuristic --- and the fact that the clinician cannot describe the algorithm does not mean the algorithm does not exist."*
> --- After Herbert Simon

> **THE ALGORITHM**
>
> *Every clinical decision is a search. The clinician stands at the patient's current state and seeks a path to an acceptable outcome. The search is guided by two sources of information: what the evidence says (how much has the path cost so far?) and what experience says (how much will the remaining path cost?). This chapter formalizes clinical reasoning as A* pathfinding on the clinical decision complex, with the evaluation function $f(n) = g(n) + h(n)$. The construction maps every component of clinical reasoning --- diagnosis, treatment planning, prognosis, clinical intuition --- onto a precise element of the A* algorithm. The result is not a replacement for clinical judgment. It is a mathematics of clinical judgment --- a formal description of what good clinicians do when they do it well, and what goes wrong when they do it badly.*

---

## 6.1 The Pathfinding Model

**Definition 6.1 (Clinical Decision as Pathfinding).** *A clinical decision is a pathfinding problem on the clinical decision complex $\mathcal{C}$:*

- *Start node $v_0$: The patient's current clinical-moral state --- diagnosis, prognosis, current treatments, relationships, institutional context.*
- *Goal region $G$: The set of acceptable clinical-moral outcomes (not just "survival" but survival with adequate function, autonomy, dignity, and trust).*
- *Path $\gamma$: A sequence of clinical actions $(v_0, v_1, \ldots, v_m)$ where each $(v_i, v_{i+1})$ is an available clinical action (edge on $\mathcal{C}$).*
- *Cost function: $f(n) = g(n) + h(n)$, where:*
  - *$g(n)$: the accumulated clinical cost from $v_0$ to the current state $n$ --- the sum of edge weights along the clinical path so far.*
  - *$h(n)$: the moral-heuristic estimate of the remaining cost from $n$ to the nearest acceptable outcome in $G$.*

This definition maps the A* search algorithm --- invented by Hart, Nilsson, and Raphael in 1968 for robot pathfinding --- onto clinical decision-making.[^1] The mapping is not metaphorical; it is structural. Every component of the A* algorithm has a precise clinical counterpart.

### 6.1.1 The Component Mapping

| A* Component | Clinical Counterpart | What It Captures |
|---|---|---|
| Start node $v_0$ | Patient's presenting condition | Where we are |
| Goal region $G$ | Acceptable outcome set | Where we want to go |
| Edge cost $w(v_i, v_j)$ | Full 9D cost of clinical action | What each step costs |
| $g(n)$: accumulated cost | Evidence-based medicine (EBM) | What we have spent |
| $h(n)$: heuristic estimate | Clinical wisdom / ethical intuition | What we think remains |
| Boundary penalty $\beta_k$ | Professional ethical norm | Where the fences are |
| Open list | Treatment options under consideration | What we might try |
| Closed list | Options evaluated and dismissed | What we have ruled out |
| Optimal path $\gamma^*$ | Clinical geodesic | The recommended plan of care |
| Path not found | Clinical-moral impasse | Ethics consultation needed |

The table is not a loose analogy. Each row identifies a formal correspondence between a computational element of A* and a clinical practice. The correspondence is what makes the framework operational: it tells us what a specific clinical activity (diagnosis, treatment planning, ethics consultation) is *doing* in the formal model, and therefore what can go wrong with it and how to fix it.

## 6.2 The $g(n)$ Component: Evidence-Based Medicine

The accumulated cost $g(n) = \sum_{i=0}^{k-1} w(v_i, v_{i+1})$ is the total clinical-moral cost of the path so far --- the sum of edge weights from the start node to the current state.

$g(n)$ is the evidence-based medicine component of clinical reasoning. It is:

**Slow.** Computing $g(n)$ requires evaluating each edge weight along the path, which in turn requires assessing the nine-dimensional impact of each clinical action. This is what medical students learn in didactics: the physiology, pharmacology, and epidemiology that determine how treatments affect clinical outcomes ($d_1$), the medical law that determines the rights and obligations ($d_2$), the health policy that determines the resource implications ($d_3$, $d_8$).

**Deliberate.** $g(n)$ computation is System 2 in Kahneman's terminology: conscious, effortful, rule-based. The clinician consults guidelines, reviews evidence, performs Bayesian calculations (pretest probability $\times$ likelihood ratio = posttest probability), and updates the accumulated cost as new information arrives.

**Data-driven.** The evidence for $g(n)$ comes from clinical trials, systematic reviews, meta-analyses, and outcome registries. It is the product of the EBM revolution (Chapter 3): the systematic replacement of opinion-based $g(n)$ with evidence-based $g(n)$.

**Primarily calibrated on $d_1$.** The EBM evidence base is overwhelmingly about clinical outcomes. The cost of a treatment on $d_5$ (trust), $d_7$ (dignity), or $d_9$ (patient understanding) is rarely measured in clinical trials. This means that $g(n)$ is well-calibrated on one dimension and poorly calibrated on the remaining eight --- a dimensional asymmetry that has consequences for the clinical geodesic.

### 6.2.1 $g(n)$ in Diagnostic Reasoning

Diagnosis is $g(n)$ computation in its purest form. The clinician starts at $v_0$ (presenting symptoms) and evaluates a sequence of diagnostic tests, each of which changes the patient's position on $d_9$ (epistemic status) at a cost on other dimensions ($d_1$: risk of the test, $d_3$: resource cost, $d_7$: dignity cost of invasive procedures).

A diagnostic workup is a path through the clinical decision complex, and the accumulated cost $g(n)$ at each step is the total cost of the tests performed so far. A good diagnostic workup minimizes $g(n)$ while reaching a state where $d_9$ is high enough to support treatment decisions. An over-zealous workup --- the "shotgun approach" of ordering every available test --- has high $g(n)$ (accumulated costs from unnecessary tests) with marginal $d_9$ gain. An under-zealous workup has low $g(n)$ but leaves $d_9$ too low for informed treatment planning.

The Bayesian framework of diagnostic reasoning --- prior probability $\times$ likelihood ratio $= $ posterior probability --- is a specific computation within the $g(n)$ framework. Each diagnostic test is an edge on the complex, and its effect on $d_9$ is determined by the test's sensitivity, specificity, and the prior probability of disease. The Bayesian update is the change in the attribute vector's $d_9$ component produced by traversing the diagnostic edge.

### 6.2.2 $g(n)$ in Treatment Planning

Treatment planning is $g(n)$ computation for a multi-step path. The clinician evaluates a sequence of treatments --- neoadjuvant chemotherapy, then surgery, then adjuvant radiation --- and computes the accumulated cost of each step, including the cross-dimensional costs (chemotherapy's $d_7$ impact, surgery's $d_1$ risk, radiation's $d_6$ burden on the family) and the boundary crossings (surgery crosses $\beta_{\text{harm}}$, but the clinical geodesic through it has lower total cost than the geodesic around it).

Treatment planning is where the multi-step nature of clinical reasoning becomes explicit. A single-step analysis might reject surgery because of its immediate $d_1$ risk and $d_7$ cost. But a multi-step analysis that includes the post-surgical recovery, the reduction in disease burden, and the improvement in long-term $d_1$ may show that the geodesic passes *through* surgery and comes out the other side with lower total friction than any path that avoids it.

This is the clinical analogue of the A* algorithm's core insight: local cost is not global cost. An edge with high weight may be part of the minimum-cost path if the alternative routes have even higher total weight. Clinical judgment that evaluates only the immediate cost of the next action is greedy search, not A* search, and greedy search does not find the geodesic.

## 6.3 The $h(n)$ Component: Clinical Wisdom

The heuristic estimate $h(n)$ is the clinician's assessment of the remaining cost from the current state $n$ to the nearest acceptable outcome in $G$. It is:

**Fast.** $h(n)$ computation is near-instantaneous --- the experienced clinician walks into the room, looks at the patient, and has a sense of "how far we have to go." This is System 1 in Kahneman's terminology: automatic, effortless, pattern-based.

**Experience-based.** $h(n)$ is calibrated not by evidence but by experience --- thousands of patients, thousands of outcomes, thousands of traversals of the clinical decision complex that have tuned the clinician's boundary penalties and distance estimates. An attending with twenty years of experience has a well-calibrated $h(n)$. A medical student has an uncalibrated $h(n)$ that may over- or under-estimate the remaining cost on any dimension.

**Multi-dimensional.** Unlike $g(n)$, which is primarily calibrated on $d_1$, $h(n)$ operates on all nine dimensions simultaneously. The clinician's heuristic estimate includes not just "how likely is this patient to survive?" ($d_1$) but also "how difficult will the consent conversation be?" ($d_4 + d_9$), "will the family cope?" ($d_6$), "will the patient's dignity be preserved?" ($d_7$), and "do I trust the institution to support this decision?" ($d_8$). These assessments are intuitive, not computed --- but they are real assessments of real dimensions, and their accuracy is what distinguishes clinical wisdom from clinical naivety.

**Vulnerable to damage.** $h(n)$ can be damaged by moral injury (Chapter 13--15), by cognitive bias (Chapter 7), and by institutional pressure. A clinician whose $h(n)$ has been inflated by moral injury --- who overestimates the cost of boundary crossings because they have been traumatized by past forced crossings --- will avoid beneficial interventions in borderline cases. A clinician whose $h(n)$ has been deflated by moral numbing --- who underestimates the cost of boundary crossings because they have been desensitized by repeated violations --- will cross boundaries too easily. Both forms of damage degrade the quality of clinical pathfinding.

### 6.3.1 The Two-Component Architecture

The $f(n) = g(n) + h(n)$ architecture explains a fundamental feature of clinical reasoning that has puzzled cognitive scientists: the dual-process nature of clinical judgment.

Experienced clinicians exhibit two modes of reasoning: fast pattern recognition ("this patient is sick --- I can feel it") and slow analytical reasoning ("the probability of PE given this D-dimer is..."). These modes are not independent systems; they are the $h(n)$ and $g(n)$ components of the same evaluation function, operating at different speeds and on different information.

When the two components agree --- when $h(n)$ says "this patient is going to do badly" and $g(n)$ confirms "the evidence says the prognosis is poor" --- clinical reasoning is fast and confident. When they disagree --- when $h(n)$ says "something is wrong" but $g(n)$ says "the numbers look fine" --- clinical reasoning slows down, becomes effortful, and recruits additional information sources (more tests, more opinions, more time). This "override" phenomenon --- the experienced clinician who orders additional workup because "something doesn't feel right" despite normal labs --- is the clinical heuristic overriding the accumulated cost when the heuristic detects curvature that the data has not yet revealed.

The framework provides a precise characterization of when each component should dominate:

- **$g(n)$ should dominate when the evidence is strong and the heuristic is uncalibrated.** A medical student performing a diagnostic workup should follow the evidence (guidelines, probability calculations, structured decision rules) rather than their intuition, because their $h(n)$ is poorly calibrated and their $g(n)$ is grounded in well-validated evidence.

- **$h(n)$ should dominate when the evidence is sparse and the heuristic is well-calibrated.** An experienced palliative care physician having a goals-of-care conversation should follow their intuition (the multi-dimensional sense of what matters to this patient and this family) rather than the evidence, because the evidence for the non-$d_1$ dimensions is sparse and the physician's $h(n)$ has been calibrated by thousands of such conversations.

- **Both should contribute when the evidence is moderate and the heuristic is moderate.** Most clinical reasoning operates in this regime: the clinician uses the evidence to compute $g(n)$ on $d_1$ and the heuristic to estimate $h(n)$ on the remaining dimensions, and the sum $f(n) = g(n) + h(n)$ guides the pathfinding.

## 6.4 The Clinical Geodesic

**Definition 6.2 (Clinical Geodesic).** *The clinical geodesic $\gamma^*$ from a patient's initial state $v_0$ to a goal region $G$ on the clinical decision complex $\mathcal{C}$ is the minimum-cost path:*

$$\gamma^* = \arg\min_\gamma \sum_{i=0}^{m-1} w(v_i, v_{i+1}) \quad \text{subject to } \gamma(0) = v_0, \; \gamma(\text{end}) \in G$$

*where $w$ is the full nine-dimensional clinical edge weight (Definition 4.2).*

The clinical geodesic is the recommended plan of care. It is optimal not in the sense of maximizing outcomes ($d_1$) but in the sense of minimizing total clinical-moral friction across all nine dimensions, with boundary penalties that encode the cost of crossing ethical thresholds.

### 6.4.1 Properties of the Clinical Geodesic

**The geodesic optimizes process, not just outcome.** Two paths may reach the same clinical outcome but differ in their process costs. A path to withdrawal of life support that includes family meetings, values conversations, a time-limited trial, and a gradual transition to comfort care has lower total manifold cost than a path that withdraws support immediately --- even though the endpoint (death of the patient) is the same. The difference is in the process: the first path preserves $d_5$ (trust with the family), $d_6$ (family support), $d_7$ (dignity of the dying process), and $d_9$ (understanding of the situation). The geodesic chooses the process path because the process costs are real costs on the manifold, not luxuries to be discarded when time is short.

**The geodesic may pass through harm.** The harm boundary ($\beta_{\text{harm}}$) is high but finite. A geodesic that passes through surgery --- which crosses the harm boundary (the surgeon cuts into healthy tissue) --- may have lower total cost than a geodesic that avoids surgery but permits the disease to progress. This is why surgery exists: the geodesic through harm has lower total friction than the geodesic around it. The harm boundary does not prohibit harm; it prices it. And the price is worth paying when the alternative is more costly.

**The geodesic may not exist.** When resource constraints remove edges from the complex, the goal region may become unreachable. A patient who needs a ventilator but cannot get one has no geodesic from their current state to the survival goal region. The clinical decision complex represents this honestly: "no path found" is the formal equivalent of "ethics consultation," the point at which the standard pathfinding algorithm fails and the clinician must escalate to a higher-level analysis.

### 6.4.2 Comparison to the QALY-Optimal Path

The QALY-optimal path $\gamma_Q^*$ is the path that maximizes the integral $\int Q(\mathbf{a}(t)) \, dt$ --- the path that produces the highest QALY score. Theorem 5.1 (QALY Irrecoverability) proves that $\gamma_Q^*$ can diverge from $\gamma^*$ by an unbounded amount.

The divergence occurs whenever the geodesic and the QALY path cross different boundaries or activate different dimensions. Three canonical examples:

1. **The Jehovah's Witness case.** QALY path: transfuse (maximizes $d_1$). Geodesic: respect the refusal, pursue alternatives (because forced transfusion has $w = \infty$ due to $\beta_{\text{consent}}$).

2. **The divided-family withdrawal case.** QALY path: withdraw immediately (maximizes $d_1$ by freeing resources). Geodesic: withdraw through a process path (family meetings, time-limited trial) that has higher $d_1$ cost but lower total manifold cost.

3. **The pandemic triage case.** QALY path: reallocate the ventilator to the patient with better prognosis (maximizes total $d_1$). Geodesic: context-dependent, because the reallocation crosses $\beta_{\text{abandon}}$ and $\beta_{\text{trust}}$ boundaries whose costs may exceed the $d_1$ benefit.

[Figure 6.1: The clinical geodesic vs. the QALY-optimal path for the Jehovah's Witness case. The QALY path (dashed) heads directly toward high $d_1$ via forced transfusion but hits the consent boundary ($\beta_{\text{consent}} = \infty$). The geodesic (solid) respects the boundary and routes through alternative treatments (erythropoietin, cell salvage), reaching a lower $d_1$ endpoint but with finite total cost. The QALY path has infinite cost on the manifold; the geodesic has the minimum finite cost.]

## 6.5 Clinical Reasoning in Practice

### 6.5.1 The Differential Diagnosis as Tree Search

The differential diagnosis --- the list of possible diagnoses being considered for a patient --- is the open list of A* search. Each candidate diagnosis defines a different subgraph of the clinical decision complex (different treatment options, different prognoses, different boundary structures), and the clinician evaluates each candidate by computing $f(n) = g(n) + h(n)$ for the paths it implies.

The clinician adds candidates to the differential (expanding the open list) when new information suggests unexplored branches. The clinician removes candidates from the differential (moving them to the closed list) when diagnostic tests rule them out. The differential narrows as the search progresses, until either a single diagnosis remains (the path is clear) or the differential reaches an irreducible uncertainty (the path branches and the clinician must decide which branch to follow under uncertainty).

### 6.5.2 The Attending's "Gestalt"

Medical students are often mystified by the attending's "clinical gestalt" --- the ability to walk into a room, look at a patient, and say "this patient is septic" before the vital signs are fully assessed. The gestalt is not mystical. It is a well-calibrated $h(n)$: a heuristic that has been trained over thousands of patient encounters to estimate the remaining cost from the current state to various outcomes.

The gestalt is fast because $h(n)$ is fast --- it is the pattern-recognition, System 1 component of clinical reasoning. It is accurate because the attending's $h(n)$ has been calibrated by feedback: the attending has seen thousands of patients whose initial presentation predicted their trajectory, and the $h(n)$ has been adjusted by each discrepancy between prediction and outcome. The medical student lacks this calibration, which is why the student must rely on $g(n)$ (evidence, guidelines, calculations) while the attending can navigate by $h(n)$ alone.

### 6.5.3 The Ethics Consultation as Heuristic Reset

When the clinician's pathfinding algorithm fails --- when $h(n)$ says "I don't know how to proceed" or when $g(n)$ and $h(n)$ disagree irreconcilably --- the clinical algorithm has reached "path not found." The standard response is an ethics consultation.

An ethics consultation is, in the framework, a heuristic reset: the ethics consultant brings a different $h(n)$ --- calibrated by different experiences, different boundary penalties, different dimensional weightings --- and applies it to the same clinical decision complex. The consultation does not change $\mathcal{C}$ (the clinical facts are the same) or $g(n)$ (the evidence is the same). It changes $h(n)$ --- the estimate of remaining cost --- by providing an alternative perspective on the boundaries, the goal region, and the relative weights of the nine dimensions.

This is why ethics consultations often produce consensus despite starting from disagreement: the disagreement is usually about $h(n)$ (different estimates of which boundaries are relevant, which dimensions are most important, how far we are from an acceptable outcome), and the consultation process recalibrates $h(n)$ by making the dimensional analysis explicit.

## 6.6 The Cost Function in Detail

The total cost function $f(n) = g(n) + h(n)$ has a specific structure that maps onto distinct clinical activities:

### 6.6.1 The Mahalanobis Component of $g(n)$

The Mahalanobis distance component of each edge weight in $g(n)$ is:

$$d_{\text{Mahal}}^2(v_i, v_j) = \Delta \mathbf{a}^T \Sigma^{-1} \Delta \mathbf{a}$$

This measures the "clinical-moral distance" traveled by the action --- how much the patient's nine-dimensional state changes, weighted by the covariance structure. A treatment that changes $d_1$ by a large amount but leaves all other dimensions unchanged has a Mahalanobis cost determined by $\Sigma_{11}^{-1}$. A treatment that changes $d_1$ and $d_5$ simultaneously has a Mahalanobis cost that includes the cross-term $\Sigma_{15}^{-1}$, which may be larger or smaller than the sum of the individual terms depending on the correlation between outcomes and trust.

### 6.6.2 The Boundary Component of $g(n)$

The boundary penalty component of each edge weight in $g(n)$ is:

$$\sum_k \beta_k \cdot \mathbf{1}[\text{boundary } k \text{ crossed}]$$

This is the cost of crossing clinical-moral boundaries --- the discrete, discontinuous component of the edge weight that makes the clinical decision complex a simplicial complex rather than a smooth manifold. The boundary component is where clinical ethics happens in its most dramatic form: the decision to cross or not cross a boundary ($\beta_{\text{harm}}$: do I perform the surgery? $\beta_{\text{consent}}$: do I treat without consent? $\beta_{\text{futile}}$: do I continue treatment that is not helping?) is the discrete clinical-moral judgment that no amount of $d_1$ evidence can resolve.

### 6.6.3 The Heuristic $h(n)$

The heuristic estimate has the form:

$$h_C(n) = \sum_k \beta_k \cdot P(\text{remaining path from } n \text{ crosses boundary } k)$$

This is the clinician's estimate of the boundary crossings that lie ahead. It is computed not from evidence (there are no clinical trials measuring the probability of future boundary crossings) but from experience: the clinician who has navigated many similar paths has an intuitive sense of which boundaries are likely to be crossed and at what cost.

The heuristic is admissible if and only if it never overestimates the true remaining cost. Chapter 7 develops the admissibility conditions in full.

## 6.7 Sarah Watches an Attending Navigate

In her second year, Sarah was assigned to a month on the hospitalist service with Dr. James Park, an attending with fifteen years of inpatient experience. She noticed that Dr. Park made clinical decisions in a distinctive pattern.

When he entered a patient's room, he spent the first thirty seconds in silence. He looked at the patient, at the monitors, at the whiteboard, at the family members. Then he asked questions --- but not the questions Sarah expected. He did not start with "How are you feeling?" ($d_1$). He started with "Do you have any questions for me?" ($d_9$), or "Is there anything about the plan that concerns you?" ($d_4$, $d_7$), or "How is the family holding up?" ($d_6$). He was sampling the non-$d_1$ dimensions before computing the $d_1$ plan.

When Sarah asked him why, he said something that she would remember for the rest of her career: "The lab values tell me the $g(n)$. What I need from the patient is the $h(n)$."

He did not use those symbols. He did not know the framework. But he was describing, in clinical language, the two-component architecture of clinical decision-making: the evidence component ($g(n)$, from the labs and the chart) and the heuristic component ($h(n)$, from the bedside assessment of the patient's trust, understanding, dignity, and social context).

Sarah watched Dr. Park navigate a difficult discharge decision. The patient --- a 78-year-old woman with heart failure, living alone, with a daughter who lived two hours away --- was medically ready for discharge ($g(n)$ said: go home, start outpatient management). But Dr. Park hesitated.

"She doesn't understand the medication changes," he said. "$d_9$ is too low. And she doesn't trust the home health aide we've arranged --- she's never had a stranger in her house." He paused. "If I discharge her now, she won't take the new medications, she won't let the aide in, she'll be readmitted in a week, and she'll trust us even less." He was computing $h(n)$: the heuristic estimate of the remaining cost if the path from here goes through premature discharge. The heuristic said the remaining cost was high --- not because of $d_1$ (the heart failure was compensated) but because of $d_5$ (trust) and $d_9$ (understanding).

Dr. Park kept the patient an extra day. He spent thirty minutes with her explaining the medication changes (improving $d_9$). He introduced the home health aide in person, in the hospital, where the patient felt safe (improving $d_5$). He called the daughter and included her in the discharge planning (improving $d_6$).

The extra day cost the hospital $1,800 in bed charges. The thirty-minute conversation cost $200 in physician time. The Bond Index for the alternative path --- premature discharge, readmission, further trust erosion --- was estimated by Dr. Park's $h(n)$ at something much higher than $2,000.

Dr. Park did not compute the Bond Index. He computed $f(n) = g(n) + h(n)$ and found that the geodesic included an extra day and two conversations. The evidence ($g(n)$) said discharge. The heuristic ($h(n)$) said wait. The heuristic was right, on the full manifold.

## 6.8 When Pathfinding Fails

The A* algorithm guarantees finding the optimal path if the heuristic is admissible and the goal region is reachable. Both conditions can fail in clinical medicine.

**The heuristic is inadmissible.** A clinician with damaged $h(n)$ (from moral injury, cognitive bias, or poor training) may overestimate the remaining cost, causing A* to avoid beneficial paths. Or the heuristic may be gauge-variant --- sensitive to framing rather than clinical reality --- causing the pathfinding to depend on how the problem is described rather than what the problem is. Chapter 7 addresses both failure modes.

**The goal region is unreachable.** When resource constraints, disease progression, or institutional barriers remove edges from the complex, the goal region may become unreachable. There is no path from the current state to any acceptable outcome. This is clinical futility --- not in the narrow sense of "treatment will not work" but in the broader sense of "no path to an acceptable outcome exists on the available complex."

When the goal region is unreachable, the clinical algorithm produces "path not found." The standard response is to redefine the goal region: shift from curative goals to palliative goals, from survival goals to comfort goals, from individual goals to family goals. The stratum transition from acute to palliative care (Chapter 4) is precisely this redefinition: the original goal region $G_{\text{acute}}$ (survival with good function) is unreachable, so the goal region is redefined as $G_{\text{palliative}}$ (comfort, dignity, family support), and a new geodesic is computed on the palliative stratum.

This redefinition is one of the most difficult clinical-moral tasks in medicine. It requires the clinician to acknowledge that the original goal is unreachable, to communicate this to the patient and family, and to construct a new goal that is acceptable to all parties. The geometric framework names what this task is: a goal region renegotiation on the clinical decision complex, triggered by the unreachability of the original goal on the current stratum.

## 6.9 The Computational Architecture of Clinical Reasoning

| Clinical Activity | A* Component | Primary Component |
|---|---|---|
| Diagnostic workup | Edge traversal on $d_9$ subgraph | $g(n)$: evidence-driven |
| Treatment planning | Multi-step path evaluation | $g(n)$: evidence-driven |
| Clinical intuition ("this patient is sick") | Heuristic evaluation of $h(n)$ | $h(n)$: experience-driven |
| Goals-of-care conversation | Goal region specification | Joint $g(n)$ and $h(n)$ |
| Ethics consultation | Heuristic recalibration | $h(n)$: reset |
| Triage | Forced contraction of $f(n)$ | $h(n)$-dominated (time pressure) |
| Informed consent | Calibration of $\mathcal{C}_{\text{patient}}$ | $d_9$ and $d_4$ alignment |
| Palliative transition | Goal region redefinition | Stratum change |
| M&M conference | Retrospective path analysis | $g(n)$ and $h(n)$ audit |

The table maps the full repertoire of clinical reasoning onto the A* framework. The mapping is not perfect --- clinical reasoning is messier, more context-dependent, and more emotionally laden than any algorithm. But the mapping identifies the computational structure beneath the messiness and thereby enables a precise analysis of what goes wrong when clinical reasoning fails: which component ($g(n)$ or $h(n)$) is miscalibrated, on which dimension, and why.

## 6.10 The Clinical Geodesic Is Not a Treatment Plan

A common misunderstanding must be addressed directly. The clinical geodesic is not a treatment plan. It is the *mathematical object that the treatment plan approximates*.

A treatment plan is a document: a list of interventions, timelines, milestones, and contingencies. It is written in clinical language, reviewed by the care team, and shared with the patient. It is a practical tool, not a mathematical object.

The clinical geodesic is the minimum-cost path on the nine-dimensional clinical decision complex. It is a sequence of vertices and edges with computable costs. It may or may not correspond to a standard treatment plan; when it does, the treatment plan is manifold-optimal; when it does not, the treatment plan is suboptimal, and the divergence between the plan and the geodesic is measurable (this is what the Bond Index quantifies).

The distinction matters because treatment plans are often constrained by institutional protocols, insurance requirements, formulary restrictions, and time pressures that force the plan away from the geodesic. These constraints are real and sometimes unavoidable. But they should be recognized as constraints --- as forces that push the treatment path away from the optimal --- rather than treated as features of the optimal path itself.

A hospital that mandates a specific discharge protocol is not implementing the clinical geodesic for every patient. It is implementing an institutional path ($\gamma_P^*$) that approximates the geodesic for the average patient and diverges from it for patients whose attribute vectors differ substantially from the average. The Bond Index $\text{BI}(P, S)$ measures the expected divergence for patient population $S$. When $\text{BI}$ is high, the protocol is not serving the population well, and redesign is warranted.

## 6.11 Integration: The Full $f(n) = g(n) + h(n)$ Architecture

Let us trace the full architecture through a single clinical encounter to show how all the components integrate.

**Patient:** Rosa Martinez, 55 years old, presenting with a newly discovered breast mass. Mammogram shows a suspicious lesion. Biopsy is recommended.

**Start node $v_0$:** $\mathbf{a}(v_0) = (0.7, 0.6, 0.6, 0.7, 0.5, 0.6, 0.7, 0.6, 0.4)$. Rosa is physically well ($d_1 = 0.7$), has moderate trust in the medical system ($d_5 = 0.5$ --- she has had mixed experiences with healthcare), and has limited understanding of the diagnostic process ($d_9 = 0.4$ --- she does not know what a biopsy involves or why it is necessary).

**Goal region $G$:** Determined jointly by Rosa and her clinician. Rosa's primary goal: "I want to know what's going on and make a decision I understand" ($d_9 \geq 0.7$, $d_4 \geq 0.7$). Clinician's primary goal: "Determine whether the mass is malignant and establish a treatment plan" ($d_9 \geq 0.8$ for diagnostic certainty, $d_1$ optimization for treatment planning).

**Step 1: Diagnostic edge (biopsy recommendation).**

$g(n)$ computation: The evidence supports biopsy for suspicious mammographic findings. Sensitivity and specificity of core needle biopsy are well-established. The $d_1$ cost is low (minor procedure, minimal complication risk). The $d_3$ cost is low (biopsy is standard of care, no resource allocation dilemma). The $g(n)$ component strongly favors biopsy.

$h(n)$ computation: The clinician's heuristic assesses the non-$d_1$ costs. Rosa's $d_5$ is moderate --- will the biopsy recommendation erode or build trust? The clinician's experience suggests that a well-explained biopsy builds trust (patients appreciate thoroughness), but a poorly explained biopsy damages trust (patients feel rushed or dismissed). Rosa's $d_9$ is low --- she does not understand why the biopsy is necessary. The clinician's heuristic estimates high remaining cost if $d_9$ is not addressed: Rosa may refuse the biopsy (stalling the geodesic) or consent without understanding (gauge-variant consent).

**Clinical decision:** Before recommending the biopsy, spend 15 minutes explaining the mammographic finding, the purpose of the biopsy, the procedure itself, and the possible outcomes. This is a $d_9$-improvement action --- an edge on the complex that moves Rosa from $d_9 = 0.4$ to $d_9 \approx 0.7$. The cost of the 15 minutes is real ($d_3$: clinician time is a resource) but small relative to the cost of proceeding with uncalibrated $d_9$.

**Step 2: After the conversation, Rosa understands the biopsy and agrees.** Her attribute vector has shifted: $d_9 = 0.7$ (she understands), $d_5 = 0.6$ (trust improved by the conversation), $d_4 = 0.8$ (her consent is informed and autonomous). The clinician applies the gauge-invariance test: "I mentioned that the biopsy will tell us whether the mass is concerning. Another way to say the same thing is that there's a chance the mass is not cancer and we're doing the biopsy to find out. Does that change how you feel?" Rosa: "No, I want to know either way." Consent is gauge-invariant.

**Step 3: Biopsy is performed.** Result: ductal carcinoma in situ (DCIS). The diagnostic edge has been traversed, $d_9$ shifts upward (diagnosis is now known), and the clinical decision complex branches: treatment options include lumpectomy + radiation, mastectomy, or active surveillance.

**Step 4: Treatment decision.** The clinician computes $g(n)$ for each option (evidence from clinical trials on DCIS outcomes). The clinician computes $h(n)$ by assessing Rosa's values: she values physical wholeness ($d_7$) highly, she trusts her surgeon ($d_5 = 0.7$ now, after the biopsy experience), she wants to understand all options ($d_9$ requirement). The clinical geodesic favors lumpectomy + radiation (lowest total manifold cost: good $d_1$, preserved $d_7$, intact $d_5$) over mastectomy (higher $d_7$ cost) and over active surveillance (higher remaining uncertainty, $d_9$ cost of ongoing monitoring).

The entire trajectory --- from presenting mass through diagnosis through treatment decision --- is a path on the clinical decision complex, guided by $f(n) = g(n) + h(n)$ at each step. The evidence ($g(n)$) determines the clinical options. The heuristic ($h(n)$) determines which options respect the patient's full nine-dimensional reality. The geodesic integrates both, producing a path that is clinically sound and morally adequate.

This is what clinical reasoning does. The framework makes it visible.

---

## Summary

This chapter has formalized clinical reasoning as A* pathfinding on the clinical decision complex, with the evaluation function $f(n) = g(n) + h(n)$. The $g(n)$ component is evidence-based medicine: slow, deliberate, data-driven, primarily calibrated on $d_1$ (clinical outcomes). The $h(n)$ component is clinical wisdom: fast, automatic, experience-driven, operating on all nine dimensions. The clinical geodesic is the minimum-cost path from the patient's current state to the goal region on the full nine-dimensional manifold. The geodesic optimizes process (not just outcome), may pass through harm (when the harm boundary has finite cost and the alternative is worse), and may not exist (when the goal region is unreachable under resource constraints).

The framework maps every component of clinical reasoning --- diagnosis, treatment planning, clinical intuition, ethics consultation, triage, informed consent, palliative transition --- onto a precise element of the A* algorithm. The mapping enables a structural analysis of clinical reasoning failures: which component is miscalibrated, on which dimension, and by how much. A full worked example traced the evaluation function through a breast cancer diagnosis, demonstrating how $g(n)$ and $h(n)$ integrate at each step of the clinical trajectory.

The next chapter addresses the heuristic component in detail: what makes clinical judgment good, bad, damaged, or biased.

---

[^1]: Hart, P. E., Nilsson, N. J., & Raphael, B. (1968). A formal basis for the heuristic determination of minimum cost paths. *IEEE Transactions on Systems Science and Cybernetics*, 4(2), 100--107. The A* algorithm has been rediscovered and renamed many times in different fields; its clinical instantiation is original to the Geometric Ethics programme (Bond, 2026).
