# Front Matter

---

## Title Page

**Geometric Medicine: Clinical Reasoning, Triage, and the Ethics of Allocation**

Andrew H. Bond
Senior Member, IEEE
Department of Computer Science
San Jose State University

Book 8 of the Geometric Series

*San Jose, 2026*

---

## Series Foreword

This is the eighth and final volume in the Geometric Series.

The series began with a diagnosis: across domains --- ethics, law, economics, cognition, communication --- the standard methodology compresses multi-dimensional structure into scalar numbers and then wonders why the numbers behave badly. GDP does not capture economic wellbeing. IQ does not capture intelligence. BLEU does not capture translation quality. Binary verdicts do not capture legal reasoning. The pattern is universal and the diagnosis is the same: scalar reduction destroys geometric structure, and the destruction is irreversible.

*Geometric Methods in Computational Modeling* (Book 1) assembled the mathematical toolkit: Riemannian geometry, hyperbolic embeddings, persistent homology, SPD manifolds, gauge theory. *Geometric Reasoning* (Book 2) developed the parent framework --- the heuristic field formalism, geodesic deviation, the four failure modes, gauge invariance, and the Scalar Irrecoverability Theorem that unifies them. *Geometric Ethics* (Book 3) was the first domain instantiation, demonstrating the framework on the 9-dimensional stratified moral manifold with its $D_4 \times U(1)_H$ symmetry group. *Geometric Economics* (Book 4) extended the instantiation to markets, prices, and welfare. *Geometric Law* (Book 5) took it into courts, constitutions, and the architecture of legal reasoning. *Geometric Cognition* (Book 6) turned the framework inward, on the mind itself. *Geometric Communication* (Book 7) showed that the same three-geometry toolkit --- hyperbolic embeddings, SPD manifolds, persistent homology --- applies without modification to communication systems spanning 4,000 years and three biological kingdoms.

This book brings the series home.

Medicine was never far from the center of the project. The clinical dilemma is where the geometric framework is most needed and most dangerous to get wrong. A hospital is not a seminar room. A triage decision is not a trolley problem. When a physician faces a patient who is dying, who is afraid, whose family is divided, whose insurance has lapsed, whose trust in medicine has been betrayed by history --- the physician is navigating a nine-dimensional manifold under time pressure, with imperfect information, bearing the moral weight of every boundary she crosses. The QALY reduces this to a number. The number is wrong. It is not approximately wrong. It is catastrophically, irrecoverably wrong, in a way that the Scalar Irrecoverability Theorem makes precise.

What distinguishes this volume from the others is not its mathematics --- the clinical decision complex, $A^*$ pathfinding, the Mahalanobis metric, the boundary penalties --- but its stakes. In *Geometric Ethics*, a flawed heuristic produces an incorrect moral judgment. In *Geometric Law*, a gauge-variant evaluation produces an unjust verdict. In *Geometric Economics*, scalar reduction produces a misleading welfare measure. In *Geometric Medicine*, a collapsed dimension kills a patient, destroys a clinician, or encodes structural injustice into the allocation of life-saving resources. The geometry is the same. The cost of ignoring it is not.

The book's central empirical contribution --- the clinical Bond Index, the Moral Injury Index, the gauge-invariance test for informed consent --- emerged from the Geometric Clinical Ethics paper submitted to the *Journal of Medical Ethics*, where the framework was compressed to journal length and tested against the falsifiable prediction standard that every volume in the series has maintained. Here, the results are expanded to book length, the theory is developed in full, and the running example of Dr. Sarah Chen traces the clinical life of a single physician through every structure the framework identifies: from her first day as a resident through a pandemic ICU to her eventual role as an attending and ethics committee member who uses the geometry not as a bedside calculator but as a diagnostic tool for institutional justice.

This is the final volume. The framework has now been instantiated across ethics, law, economics, cognition, communication, and medicine. The circle closes where it should --- at the bedside, where the geometry was always real and the scalars were always insufficient, and where the clinicians who navigate the manifold every day have known this in their bones long before anyone wrote down the mathematics.

---

## Preface

### The Clinician's Dilemma

In the autumn of 2025, I sat across a table from a palliative care physician who had been practicing for twenty-two years. I had spent the previous hour explaining the clinical decision complex --- the nine-dimensional weighted simplicial complex, the $A^*$ pathfinding model, the boundary penalties, the Mahalanobis metric. She had listened with the patience that palliative care teaches. When I finished, she said: "You have written down what I do every day. But I want to know --- does writing it down help?"

It was the right question, and I did not have a confident answer. The geometric framework is a formal structure. It provides definitions, theorems, and falsifiable predictions. It does not, by itself, save a patient or protect a clinician. But I had been working on the Geometric Ethics project for over a year by that point, and I had seen what happened when the framework was applied to domains where scalar reduction does real damage. In economics, the framework revealed that GDP growth can coincide with welfare decline --- not as a philosophical argument but as a mathematical theorem. In law, the framework showed that binary verdicts destroy the information that appellate courts need to evaluate whether justice was done. In each case, the mathematics did not replace human judgment; it made the structure of that judgment visible, auditable, and improvable.

Medicine, I told the palliative care physician, is the domain where the framework matters most --- because medicine is where the scalars do the most damage.

Consider the QALY --- the quality-adjusted life year. It is the standard currency of health economics, used by NICE in the United Kingdom, by ICER in the United States, and by health technology assessment agencies worldwide to determine which treatments are funded and which are not. The threshold is typically 20,000 to 30,000 pounds per QALY gained: if a treatment costs more than this per unit of quality-adjusted survival, it is deemed not cost-effective. The logic is clean, the mathematics is simple, and the implications are devastating.

A QALY of 0.6 is compatible with two entirely different patients. One has moderate physical limitation but intact autonomy, full trust in her physician, a supportive family, and a clear understanding of her prognosis. The other has good physical function but has lost trust in medicine after a medical error, feels coerced into a treatment she does not understand, and is experiencing a crisis of identity as her illness redefines her sense of self. The QALY cannot distinguish these patients. The number is the same. The clinical reality is not the same. The treatment that would help one patient would harm the other. But the QALY says: treat them identically.

This is not a failure of calibration. It is not a matter of choosing better quality weights. It is a mathematical certainty --- a consequence of the rank-nullity theorem. Any function from $\mathbb{R}^9$ to $\mathbb{R}$ has a kernel of dimension at least 8. Eight dimensions of clinically relevant moral information are destroyed by the projection, and the destruction is irreversible. No post-hoc adjustment, no sensitivity analysis, no subgroup weighting can recover what the scalar discards. This is the QALY Irrecoverability Theorem, the domain-specific instantiation of the Scalar Irrecoverability Theorem from *Geometric Reasoning*, and it is the mathematical foundation of this book.

The framework that replaces the QALY is not a better scalar. It is a geometry. The clinical decision complex is a nine-dimensional weighted simplicial complex whose vertices are clinical states, whose edges are clinical actions, and whose edge weights are computed from the full Mahalanobis distance on the nine-dimensional attribute vector plus boundary penalties for crossing clinical-moral thresholds. A clinical decision is pathfinding on this complex: the clinician stands at the patient's current state and seeks the minimum-cost path to an acceptable outcome. The minimum-cost path is the clinical geodesic. It is, in the formal sense, the best thing to do --- not just clinically, not just ethically, but on the full nine-dimensional manifold where clinical and ethical considerations are not competing claims but dimensions of a single space.

The palliative care physician understood this immediately. "Every hard case I have ever faced," she said, "involved dimensions that no score captured. The patient's trust. The family's grief. The institutional pressure to discharge. I navigate these every day. I just never had a name for the space."

The space has a name now. The clinical decision complex. And the navigation has a mathematics: $A^*$ search with $f(n) = g(n) + h(n)$, where $g(n)$ is evidence-based medicine and $h(n)$ is the moral-clinical heuristic that twenty-two years of practice has calibrated to near-optimality.

But the mathematics has a cost, too. The framework does not merely describe clinical reasoning; it reveals the mechanisms of clinical suffering. Moral injury --- the damage that physicians sustain when they are forced to cross moral boundaries they believe should not be crossed --- is not burnout. Burnout is resource depletion: the exhaustion of $g(n)$ computation capacity. Moral injury is heuristic damage: the permanent alteration of $h(n)$ by forced boundary crossings. The distinction is not semantic. It is structural, mathematical, and predictive. A burned-out clinician needs rest. A morally injured clinician needs heuristic recalibration --- and above a critical threshold, the damage is irreversible. The Moral Injury Accumulation Theorem makes this precise, and the COVID-19 pandemic provided the natural experiment that tested it.

I did not set out to write a book about clinical medicine. The Geometric Ethics project began as a mathematical exercise --- the observation that the four failure modes of heuristic search (heuristic corruption, objective hijacking, local minima, gauge breaking) mapped onto failure modes of moral reasoning with uncomfortable precision. The clinical application emerged when I realized that the $A^*$ model was not a metaphor for clinical decision-making but a literal description of it. Clinicians compute $f(n) = g(n) + h(n)$ every time they evaluate a patient. The $g(n)$ is evidence-based medicine. The $h(n)$ is clinical judgment. The boundary penalties are professional ethics. The open list is the differential diagnosis. The closed list is the options already ruled out. The goal region is not "survival" --- it is survival with adequate function, autonomy, dignity, and trust. The mapping is exact, and once I saw it, I could not unsee it.

The book that resulted is, in one sense, a technical monograph: it develops the clinical decision complex in full mathematical detail, proves the QALY Irrecoverability Theorem, constructs the mathematical theory of moral injury, formalizes informed consent as a gauge-invariance condition, models triage as constrained multi-agent pathfinding, and defines the clinical Bond Index as a quantitative measure of structural healthcare injustice. Each of these constructions generates falsifiable predictions that differ from predictions of standard bioethics, QALY-based health economics, and existing moral distress research.

But in another sense, the book is a story. It follows Dr. Sarah Chen --- a composite character drawn from conversations with residents, attendings, palliative care physicians, and ethics committee members --- from her first day of residency through a pandemic and beyond. Sarah is the argument made personal. She learns, as every clinician learns, that the scalars she was taught in medical school do not capture what she encounters at the bedside. She discovers, as I discovered, that the manifold exists and has structure. She is damaged by the pandemic, as many clinicians were damaged, in ways that the burnout literature cannot describe but the moral injury framework can. And she emerges, at the book's end, not as a convert to geometric ethics but as a practitioner who uses the framework the way a surveyor uses a map --- not to replace the territory but to navigate it with fewer errors and a clearer understanding of where the dangerous crossings lie.

This is the final volume of the Geometric Series. The framework has been tested across ethics, law, economics, cognition, communication, and now medicine. In every domain, the same pattern holds: scalar reduction destroys structure, the destruction is mathematically irrecoverable, and the geometry recovers what the scalars lose. The domains differ --- the manifold of legal reasoning is not the manifold of whale communication, and neither is the manifold of clinical medicine. But the mathematics is the same, the failure modes are the same, and the theorem that unifies them is the same.

The circle closes here, at the bedside, where the geometry was always real and the scalars were always a convenient fiction. The clinicians knew. Now there is a mathematics for what they know.

### Who This Book Is For

This book is written for three audiences, and it asks something different of each.

For **clinicians, bioethicists, and medical educators**, the book provides a formal framework for what clinical wisdom has always recognized: that patient care involves simultaneous evaluation of clinical outcomes, patient autonomy, trust, justice, dignity, institutional context, and epistemic certainty --- and that reducing this to a QALY or a four-principle checklist loses the information that makes hard cases hard. The mathematics is self-contained (Appendix A covers the prerequisites from first principles), and the clinical vignettes in Chapter 9 and Appendix C are designed for classroom use. The reader who has encountered ethics committee deliberation, triage protocols, or the informed consent process will find the framework clarifies structures they already navigate.

For **health economists, health policy analysts, and outcomes researchers**, the book offers a geometric alternative to QALY-based evaluation. The QALY Irrecoverability Theorem is not a philosophical objection to scalar measurement --- it is a mathematical proof that scalar health metrics destroy irrecoverable information, with precise conditions under which the destruction does and does not matter (Proposition 5.1). The clinical Bond Index provides a quantitative measure of structural healthcare injustice that is computable from existing clinical data and generates testable predictions about patient experience disparities.

For **mathematicians, computer scientists, and readers of the earlier volumes in the Geometric Series**, the book provides the final domain instantiation of the geometric framework --- the one that, more than any other, demonstrates why the mathematics matters. The clinical decision complex is a weighted simplicial complex. Clinical reasoning is $A^*$ search. Informed consent is a gauge-invariance condition. Moral injury is heuristic damage. Each of these is a precise mathematical construction with theorems, proofs, and empirical predictions. The reader who has followed the framework from *Geometric Reasoning* through the domain instantiations will recognize the structures; what is new is the domain, and the domain is where the stakes are highest.

The book assumes no background in clinical medicine, differential geometry, or health economics. It assumes intellectual seriousness and the willingness to follow an argument that moves between a patient's bedside and a Riemannian manifold without apology.

### A Note on Scope

This book does not solve clinical ethics. It does not produce an algorithm that replaces the physician's judgment, a formula that resolves every triage dilemma, or a metric that makes structural injustice disappear. What it does is provide the mathematical structure that clinical ethics has lacked --- a structure that makes clinical reasoning visible, auditable, and improvable, and that generates predictions specific enough to be tested and wrong.

The framework is a theoretical structure, not a bedside calculator. It informs decision support tools and policy analysis. It measures structural injustice with numbers, not opinions. It predicts moral injury before it happens. It tests informed consent beyond checklist compliance. But it does not --- and should not --- replace the clinician who navigates the manifold with twenty years of calibrated intuition. The geometry describes the space. The clinician walks it.

Chapter 18 is honest about what the framework cannot yet explain. The nine-by-nine covariance matrix has not been estimated from clinical data. The boundary penalties may vary across cultures, specialties, and patient populations. The conservation law for clinical reasoning remains conjectural. These are not hedges; they are the frontier, and acknowledging the frontier is more useful than pretending it does not exist.

---

## Acknowledgments

A book that brings a mathematical framework to the bedside requires collaborators from both sides of that distance. The debts are many.

The geometric framework that underpins this book was developed as part of the Geometric Ethics programme at San Jose State University. I am grateful to the research group members --- particularly Marcus Reeves, whose early work on the $A^*$ clinical pathfinding model shaped the computational architecture of Chapter 6; Elena Vasquez, who implemented the clinical Bond Index calculations that appear in Chapter 12 and Appendix B; and James Okafor, whose careful analysis of the COVID-19 moral injury data informed the natural experiment section of Chapter 14. The group's willingness to subject every claim to falsifiable prediction has kept the project honest.

The clinical content of this book owes debts that no acknowledgment section can fully discharge. The conversations with clinicians that shaped the framework --- palliative care physicians, ICU attendings, emergency medicine residents, psychiatrists, surgeons, and ethics committee members --- are the empirical foundation of every clinical claim in these pages. I am particularly grateful to the physicians and nurses at the Regional Medical Center (anonymized) who shared their experiences of pandemic triage with candor and precision, often at significant personal cost. Their accounts of moral injury --- the flinch at the triage pager, the reluctance to enter certain rooms, the permanent alteration of clinical instinct by decisions they did not choose --- are the human reality behind the mathematics of Chapter 13.

The bioethics community has been a rigorous and generous interlocutor. Early versions of the clinical decision complex were presented at the American Society for Bioethics and Humanities annual meeting, where the feedback was sharp and constructive. I am grateful to the anonymous reviewers at the *Journal of Medical Ethics*, whose careful reading of the Geometric Clinical Ethics paper identified weaknesses that strengthened the final framework substantially. Katherine Nguyen and David Okonkwo, members of the hospital ethics committee that served as an informal testing ground for the framework, provided the clinical judgment that no amount of mathematical sophistication can replace.

The health economics critique --- the QALY Irrecoverability Theorem and its implications --- benefited from conversations with colleagues at the International Health Economics Association and the ISPOR annual meeting. I thank those who engaged the argument on its mathematical merits rather than dismissing it as anti-quantitative. The theorem does not say that QALYs are useless. It says that QALYs are adequate under specific conditions and catastrophically inadequate under others. The conditions are precise and testable.

The moral injury framework draws on the foundational work of Andrew Jameton, Elizabeth Epstein, Ann Hamric, Wendy Dean, Simon Talbot, and Cynda Hylton Rushton, whose conceptual and empirical contributions made the mathematical formalization possible. The distinction between burnout and moral injury is theirs; the mathematical characterization --- $g(n)$-depletion versus $h(n)$-damage --- is this book's contribution.

Institutional support came from the Department of Computer Science at San Jose State University, the College of Science, and the SJSU Research Foundation. Computing resources were provided by the university's High-Performance Computing cluster. The Digital Humanities Initiative supported the cross-referencing work that connects this volume to the seven that precede it.

The series as a whole has benefited from the criticism of colleagues at the IEEE Computational Intelligence Society, workshop participants at NeurIPS 2025 and ACL 2026, and the anonymous reviewers of the component papers. The errors that remain are proof of the gap between aspiration and execution --- a gap that, on the clinical manifold, is measured in lives.

Dr. Sarah Chen is a composite character. She is drawn from the experiences of many clinicians who shared their stories with the understanding that the mathematics, if it works, might one day prevent what they endured. To them: the framework exists because of what you told me. The question of whether it helps --- the palliative care physician's question --- is now yours to answer.

Finally, and as always: to my family, who have endured a year of dinner-table discussions about triage algorithms, moral injury indices, and the topology of informed consent, and who have responded with the patience, humor, and occasional sharp correction that no boundary penalty could capture.

Andrew H. Bond
San Jose, California
March 2026
