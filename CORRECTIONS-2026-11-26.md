# Geometric Medicine: corrections of 2026-11-26

These corrections were made on 2026-11-26 at the author's direction after a review of the Geometric Series.

Paths are under `manuscript/` unless a file at the repository root is named. Section and definition numbers are the ones in force after the corrections.

## Reconciled

1. **`part_ii/ch05_qaly_irrecoverability.md`, Theorem 5.1, part 3.** The text cited the clinical geodesic as "Definition 4.3". It now cites Definition 6.2. Definition 4.3 is the clinical-moral boundaries, and the clinical geodesic is defined in Definition 6.2 of Chapter 6.

2. **`part_ii/ch05_qaly_irrecoverability.md`, Theorem 5.1, and `appendices/appendix_a_math.md`, Theorem A.2.** Both said "any function". They now say "any continuous function". The proof printed in Section 5.2 uses differentiability, and for the other case a continuity argument. Without continuity the non-injectivity claim is false, because the two spaces have the same cardinality and an injection exists. Definition 5.1 and the corollaries are unchanged, since every QALY function they name is continuous.

3. **`part_ii/ch05_qaly_irrecoverability.md`, proof of Theorem 5.1 (data-processing paragraph) and Proposition 5.2.** Both glossed "full-rank covariance" as "all nine dimensions are informationally independent". They now gloss it as "no dimension is a linear function of the others". Full rank excludes linear dependence only, and the same chapter treats the independent case (diagonal covariance) separately in the paragraph after Proposition 5.2.

4. **`part_ii/ch05_qaly_irrecoverability.md`, Section 5.12.** The Scalar Irrecoverability Theorem was said to be applied in *Geometric Ethics* "(Ch. 16)". It now says "(Ch. 15)". In *Geometric Ethics* v1.28 the theorem is Theorem 15.1, Section 15.6, and Chapter 16 does not mention it.

5. **`part_ii/ch04_clinical_manifold.md`, Definitions 4.6 and 4.7.** Clinical Friction (Section 4.8) was numbered 4.7 and Clinical Strata (Section 4.9) was numbered 4.6. They are now 4.6 and 4.7, in the order they appear. No other passage cites either number.

6. **`part_ii/ch04_clinical_manifold.md`, footnote 1.** "See Appendix E for the complete notation guide" now reads "Appendix D". The notation guide is `appendices/appendix_d_notation.md`, and there is no Appendix E.

7. **`part_ii/ch04_clinical_manifold.md`, Section 4.4.1.** "The Mahalanobis distance is invariant under affine transformations of the attribute space" now adds "invertible" and "provided $\Sigma$ is transformed with the coordinates". The invariance holds only on that condition, which the example of two measurement scales in the same paragraph assumes.

8. **`part_ii/ch04_clinical_manifold.md`, Section 4.4.3.** The text said the Mahalanobis term "is strictly greater than" the squared Euclidean length 0.1025 "because" of the off-diagonal terms. It now says the term "can exceed" that length "when" the off-diagonal terms amplify the cost. The inequality does not hold for a general covariance matrix, and the chapter says in the same sentence that the matrix is not yet estimated. The illustrative value 0.15 is unchanged.

9. **`part_ii/ch04_clinical_manifold.md`, Section 4.5.2, and `part_vi/ch17_measuring_metric.md`, Section 17.1.** Chapter 4 said the discrete choice experiment "yields the off-diagonal entries of $\Sigma^{-1}$ ... directly". Chapter 17, which the passage summarizes, says only that the marginal rates of substitution are "related to" the inverse covariance matrix. Chapter 4 now uses the weaker wording of Chapter 17.

10. **`part_i/ch03_history_medical_ethics.md`, Section 3.5.** "This metric ... is estimated from clinical decision data (Chapter 17)" now reads "is to be estimated". Chapters 4, 17 and 18 and the README all say the covariance matrix has not been estimated.

11. **`part_ii/ch08_consent_gauge.md`, Theorem 8.1.** The opening sentence said valid consent "is equivalent to" a gauge-invariance condition. It now says valid consent "requires" one. The formal statement ("consent is valid only if") and the proof give the necessary direction only.

12. **`part_ii/ch06_clinical_astar.md`, Section 6.7, `part_vi/ch17_measuring_metric.md`, Section 17.4, `part_vi/ch18_open_questions.md`, Section 18.10.** Six currency amounts were written with a bare dollar sign. They are now written `\$`. In the published page of Chapter 6 the two bare signs on one line are read as the delimiters of a formula.

13. **`part_iv/ch12_bond_index.md`, Section 12.5, and `part_vi/ch17_measuring_metric.md`, Section 17.2, Step 1.** Chapter 12 listed the dimensions taken from electronic health records as $d_1, d_2, d_6, d_8$, and Step 1 of the Chapter 17 pipeline listed $d_1, d_2, d_4, d_6, d_8$. Both now list $d_1, d_2, d_3, d_4, d_6, d_8$. The tables of Section 12.3 and Section 17.2 each list those six, and the summaries of Chapters 17 and 18 say "six of nine".

14. **`part_vi/ch17_measuring_metric.md`, Section 17.1.** "45 unique entries (9 diagonal + 36 off-diagonal, divided by 2 for symmetry)" now reads "counting each symmetric pair once". 9 + 36 is already 45, and the 36 is the count after symmetry.

15. **`part_vi/ch17_measuring_metric.md`, Study 1, feasibility.** "250 coder-hours for 500 consultations" now reads "250 hours per coder for 500 consultations (500 coder-hours for the two independent coders)". The protocol in the same study has two coders code every consultation independently, at 30 minutes each.

16. **`part_vi/ch17_measuring_metric.md`, Section 17.3.** The predictions were called "pre-registered claims". They are now "pre-specified claims", the word the chapter summary uses. The repository holds no registration.

17. **`part_vi/ch17_measuring_metric.md`, Sections 17.4 and 17.6.** The correlation of $-0.4$ (and $-0.41$) was labelled as between "framing invariance" and health literacy. It is now labelled as between "framing variance" and health literacy. Prediction 3 says framing-variant patients have lower literacy, which is a negative correlation with variance and a positive one with invariance.

18. **`part_vi/ch18_open_questions.md`, Section 18.1.** "the remaining 27 entries" now reads "the remaining 24 entries". The matrix has 45 unique entries and a 6 by 6 symmetric submatrix has 21.

19. **`part_vi/ch18_open_questions.md`, Section 18.4.** "The framework assumes that the clinical decision complex has the structure of a smooth Riemannian manifold" contradicted Section 4.1, which defines the complex as a weighted simplicial complex and not a smooth manifold. The sentence now names both and relates them: the complex is formally a simplicial complex, and the geometric vocabulary treats it as if it were Riemannian.

20. **`part_vi/ch18_open_questions.md`, section numbers.** Two sections were numbered 18.5. The second and the sections after it are renumbered, so the chapter now runs 18.1 to 18.10. "The Frontier, Honestly Stated" is now Section 18.9 and "Sarah's Grant Proposal" is Section 18.10. No other chapter cites these sections by number.

21. **`part_v/ch15_prevention.md`, Definitions 15.3 and 15.4.** Morally Sustaining Culture (Section 15.6) was numbered 15.4 and Functional Adaptation (Section 15.7) was numbered 15.3. They are now 15.3 and 15.4, in order of appearance.

22. **`part_v/ch15_prevention.md`, Section 15.4.** Moral resilience is defined in Definition 13.6 with one condition and in Definition 15.2 with three. A sentence now relates them: Definition 13.6 states the first condition and Definition 15.2 adds the other two.

23. **`part_vi/ch16_ai_clinical.md`, Propositions 16.5 and 16.6.** The proposition of Section 16.5 was numbered 16.6 and the proposition of Section 16.6 was numbered 16.5. They are now in order.

24. **`part_vi/ch16_ai_clinical.md`, Section 16.4, `part_vi/ch18_open_questions.md`, Section 18.5, and `OUTLINE.md`.** The No Escape Theorem was cited as "proved in *Geometric Ethics* (Ch. 19)" and as "The general theorem is proved". In *Geometric Ethics* v1.28 it is Theorem 18.1 of Chapter 18, tagged "Theorem (conditional on Req. 1–4)", and Appendix F lists it as a Conditional Theorem. The text now cites Chapter 18, Theorem 18.1, and calls it a conditional theorem. Chapter 16 now says the theorem "is read here as stating" the sacred-boundary result.

25. **`part_v/ch14_moral_injury_settings.md`, Section 14.7.** "The clinical justification is sound (Chapter 9 proved this)" now reads "argued this". Chapter 9, Case 3, gives a case analysis and no theorem.

26. **`appendices/appendix_b_code.md`, Section B.4.1.** The Bond Index computation was cited as "Chapter 17, Section 17.3". It is Section 17.2 ("Measuring the Bond Index from EHR Data").

27. **`README.md` and `OUTLINE.md`.** The README listed *Geometric Ethics* as "Published (v1.23)". The current release is v1.28 (its `CHANGES-v1.28.md`). The outline's cross-reference table gave the general Bond Index as "GE Ch. 16". It is in Chapter 18 of *Geometric Ethics*, as Section 12.1 of this book already says, and the row now adds that the clinical Bond Index is a different quantity.

## Marked as illustrative or simulated

1. **`part_vi/ch17_measuring_metric.md`, Section 17.6 ("Sarah's Experiment").** The section reported a pilot of the consent test ($n = 84$, $r = -0.41$, p-values) as "preliminary results" and said "the geometric prediction is confirmed in the pilot". Sarah Chen is a composite character (front matter), and the repository holds no such study or data. The heading now ends "An Illustrative Scenario". The first sentence says it is an illustrative scenario and that no such study has been run. The results are introduced as hypothetical and invented to show what the analysis would report. The closing sentence says the hypothetical pilot comes out as the prediction says a real one should.

2. **`part_vi/ch17_measuring_metric.md`, Section 17.4, Prediction 3.** "Sarah's pilot: $n = 84$, $r = -0.41$ — effect size confirmed" now reads "Sarah's hypothetical pilot (Section 17.6, illustrative; no such study has been run) ... the effect size the design assumes".

3. **`part_vi/ch18_open_questions.md`, Section 18.9, claim 6.** "Status: Formally developed, pilot data supportive, full study not yet conducted" now reads "Formally developed, untested; illustrated by a hypothetical pilot (Section 17.6), full study not yet conducted". The only pilot is the scenario of Section 17.6.

4. **`part_iv/ch12_bond_index.md`, Section 12.4 (published chapter).** The section was headed "Case Study" and reported a Bond Index computed for 847 patients of "a large academic medical center", with a results table and a decomposition by dimension. Section 18.9 and the README say the clinical Bond Index has not been computed from clinical data, and the repository holds no data or output for this case. The heading now reads "Illustrative Case Study". The first paragraph says the center is hypothetical and the numbers are invented to show what the computation would report. The population line, the results heading and the decomposition heading are marked hypothetical or illustrative. The numbers are unchanged and consistent: the four group sizes sum to 847, the ratios are 7.4/3.2 = 2.31, 5.1/3.2 = 1.59 and 4.0/3.2 = 1.25, and the decomposition sums to 4.2.

5. **`part_iv/ch12_bond_index.md`, Section 12.9.** "Sarah presents the Bond Index results" now reads "the illustrative Bond Index results of Section 12.4".

6. **`part_vi/ch16_ai_clinical.md`, Section 16.8.** Sarah's audit of an AI triage system gives an AUC of 0.89 and a table of Bond Index values. The first sentence now says the scenario is illustrative and the system and its numbers are hypothetical, and the table is introduced with "(illustrative values)". The ratios are consistent with the table (6.1/2.8 = 2.18, 4.3/2.8 = 1.54, 8.4/2.8 = 3.00).

7. **`part_v/ch14_moral_injury_settings.md`, Section 14.7.** Sarah's moral injury vectors are introduced with "(the values here and below are illustrative)". The composite vector is consistent with the three it sums (12 + 8 = 20, 3 + 15 = 18, 47).

8. **`part_v/ch14_moral_injury_settings.md`, Section 14.4.** "a fourth moral injury pattern that further validates the multi-dimensional taxonomy" now reads "further illustrates". The section is an analysis within the framework and reports no test.

9. **`OUTLINE.md`, Chapter 17, Sarah's thread.** "Her preliminary results show a correlation ... the geometric prediction confirmed" now says the pilot results are hypothetical and illustrative.

## Withdrawn or updated

1. **Dihedral group $D_4$ for the Hohfeldian positions.** *Geometric Ethics* withdrew $D_4$ in its version 1.25: no quarter-turn is demonstrated, and the correlative and the negation commute and generate the Klein four-group $V_4$, of order 4.
   - `part_ii/ch04_clinical_manifold.md`, Section 4.2.2. A dated note stands before the Hohfeldian paragraph. The paragraph said "The $D_4$ dihedral symmetry of jural relations --- correlative and negation symmetries". It now says "The Klein four-group $V_4$ symmetry of jural relations --- the correlative and negation symmetries". The paragraph uses only the two commuting operations (it swaps a right with its correlative duty), so its statement stands as written under $V_4$.
   - `appendices/appendix_d_notation.md`: the row "$D_4$, Dihedral group of order 8" is now "$V_4$, Klein four-group, of order 4", with the earlier name recorded.
   - `backmatter/index_framework.md`: three entries now name $V_4$.
   - `front_matter.md`, Preface: "its $D_4 \times U(1)_H$ symmetry group" now reads "$V_4 \times U(1)_H$ symmetry group (posited; the earlier $D_4 \times U(1)_H$ was withdrawn in its version 1.25)". *Geometric Ethics* v1.28 states this group as Posit 12.3.
   - `OUTLINE.md`, cross-reference table: the row now names V4.
   - No theorem, proposition, definition or prediction of this book depends on a quarter-turn, on order 8, or on a group built from $D_4$. Nothing is marked withdrawn.

2. **Conservation of Harm.** *Geometric Ethics* withdrew Conservation of Harm on 2026-06-19 (ledger entry GE-HARM-CONSERVATION) and kept the invariance of harm accounting under re-description.
   - `part_vi/ch18_open_questions.md`, Section 18.2. A dated note stands at the head of the section. The sentence "the BIP-invariance of the moral Lagrangian implies conservation of harm" now says it "is taken to imply the invariance of harm accounting" and records that the conservation law was withdrawn. Candidate 3 was called "the clinical analogue of harm conservation" and is now called the analogue of the invariance of harm accounting. The section states open questions only, so no result is withdrawn. The candidates stand as open candidates.

3. **Other withdrawn or refuted results of *Geometric Ethics*.** The book does not cite the SU(2) gauge prediction, hysteresis, or any other claim that the ledger of *Geometric Ethics* lists as withdrawn or refuted.

4. **Clinical Bond Index note, `part_iv/ch12_bond_index.md`, Section 12.1.** Checked against *Geometric Ethics* v1.28 and left unchanged. The clinical Bond Index is Definition 21.10 of Chapter 21 there, the Bond Index is in Chapter 18, and Chapter 21 carries the same statement that the two share a name and are different quantities.

## Unresolved

Each item needs the author. The text is unchanged.

1. **Citations of findings to named studies.** Chapters 10 and 14 attribute specific empirical findings to papers: Greenberg et al. (2020) for higher moral distress in ICU staff than ward staff, and for less distress in high-mortality units with clear protocols (Sections 10.5, 14.1, 14.6); Rushton (2018), a book published before the pandemic, as "the pandemic literature" (Section 10.5); Lai et al. (2020), Lamiani et al. (2017), Dodek et al. (2016), Mantri et al. (2020), Rushton et al. (2021) and Shale (2020) in Chapter 14. The bibliography lists Greenberg et al. (2020) as a BMJ article on managing mental health challenges and does not list Lai, Lamiani, Dodek, Mantri, Rushton et al. (2021) or Shale. Nothing in the repository shows what those papers found. The author would need to check each attributed finding against the paper and add the missing references. Also missing from the bibliography: Maydeu-Olivares and Coffman (2006), Stewart et al. (2011), Mitchell et al. (2019), Gebru et al. (2021), Shalowitz et al. (2006).

2. **Acknowledgments, `front_matter.md`.** The acknowledgments thank named research-group members for work the repository does not contain (an implementation of "the clinical Bond Index calculations that appear in Chapter 12", an "analysis of the COVID-19 moral injury data"), a "Regional Medical Center (anonymized)", named ethics-committee members, and presentations at named meetings. One named member shares a surname with the patient of Chapter 9, Case 1. The author would need to confirm each acknowledgment. The Preface also calls this "the final volume" and speaks of "the seven that precede it", says the framework was "tested against the falsifiable prediction standard", and calls the Bond Index, the Moral Injury Index and the consent test the book's "central empirical contribution". The README says the volume is posited and untested.

3. **Appendix B, code.** The appendix says `ch21_clinical.py` and `ch27_bioethics.py` "produce the computational results in this book", that line references are to "versions archived with this volume", that "all computational results in this book can be reproduced", and that "in every pandemic scenario tested, the divergence fraction is non-zero". Neither module is in this repository or in the *Geometric Ethics* repository. The author would need to supply the code and its output, or the sentences need rewording.

4. **Proposition 5.2 (information loss).** The chain $I(\mathbf{a}; Q(\mathbf{a})) \leq H(Q(\mathbf{a})) \leq H(a_1)$ is stated for any QALY function and with differential entropy. The second inequality does not hold for an arbitrary $Q$, and the mutual information of a continuous variable with a deterministic function of itself is not bounded by a differential entropy. A correct statement needs new mathematics.

5. **Definitions 7.1 to 7.3 (heuristic categories).** As written, a heuristic that overestimates slightly is both $\varepsilon$-admissible (Definition 7.2) and inadmissible (Definition 7.3, "$h_C(n) > h^*(n)$ for some relevant $n$"). Section 13.4 uses the other reading, inadmissible meaning $h(n) > (1 + \varepsilon) h^*(n)$. "Strictly admissible" is defined as far below $h^*$ and then applied to any finite penalty. The author would need to choose the definition.

6. **Boundary penalties outside Definition 4.3.** Definition 4.3 defines five boundaries. Later chapters use penalties named trust, justice, rights, dignity, autonomy, delay, liability, resource denial and cost. In Section 10.3, Case A, the bullets name $\beta_{\text{abandon}}$ and $\beta_{\text{rights}}$ and the formula and Theorem 10.1 use $\beta_{\text{abandon}}$ and $\beta_{\text{trust}}$. Definition 13.5 gives the moral injury vector five components, while Chapter 14 lists dignity, justice and autonomy crossings as dominant in three settings. The author would need to extend Definition 4.3 or map the later names onto it.

7. **Triage committee and the abandonment boundary.** Section 13.5 says a committee decision distributes the abandonment cost across its members. Section 15.2 says that with a committee "the abandonment boundary is not crossed". In Section 10.10 the committee decides and Sarah communicates, and Sections 13.9 and 14.7 give her a large abandonment injury from it. These are three different accounts.

8. **Theorems stated without proof or with an argument that is not a proof.** Theorem 9.1 (the constant $K$, the "curvature" of a simplicial complex and the distance between two paths are undefined) and Theorem 11.1 have no proof. Theorem 13.1, parts 2 and 3, asserts empirical claims (irreversibility above a threshold, independence from burnout) and its "proof" restates the model. Theorem 16.1 follows at once from an infinite edge cost, and its mechanism differs from Theorem 18.1 of *Geometric Ethics*, which concerns canonicalization, grounded evaluation, audit and external verification. The author would need to decide whether these are theorems, propositions or posits.

9. **Sample sizes in the narrative.** Section 17.6 says Sarah's full study has $n = 300$. Prediction 3 proposes $n = 200$ patients, and 300 is the number of clinicians for Prediction 2 and for the grant of Section 18.10. Section 18.10 budgets "100 clinician-hours of vignette coding", while Study 1 needs 500 coder-hours. Which study each figure refers to cannot be told from the text.

10. **Study designs.** Section 17.1 says retrospective coding of consultation records needs no "IRB consent". Record review normally needs ethics review or a waiver. The same section says a resolution V fractional factorial design for nine two-level factors needs "approximately 50–80 vignettes". A regular design of that resolution needs 128 runs, and no source is given for the smaller figure.

11. **Section 18.3, Stage 2.** The medical Bond Invariance Principle is called "a continuous symmetry group". The re-descriptions the book lists (language, chart format, framing) are discrete, and Noether's theorem needs a continuous symmetry.

12. **`part_i/ch01_qaly_trap.md`, Section 1.3.** "the same pattern identified in ... *Geometric Ethics* (Chapter 16)". Chapter 16 of *Geometric Ethics* v1.28 is on moral uncertainty. The intended chapter may be Chapter 2 (the failure of scalar ethics) or Chapter 15 (Theorem 15.1), and the text does not say which.

13. **Bibliography labels.** The bibliography labels *Geometric Reasoning* as Bond (2026b) and *Geometric Ethics* as Bond (2026c). The README and Theorem A.2 use Bond (2026c) for *Geometric Reasoning*. The book numbers in the Preface (Ethics as Book 3, Medicine after seven others) differ from the series numbering, in which this is Volume 8 of 14.

14. **Footnotes without markers.** Chapter 4 and Chapters 9 to 18 each end with footnote texts that no place in the chapter refers to. They print at the end of the chapter with a return link that leads nowhere. The author would need to say where each marker belongs.

15. **Figures.** Every figure in the book is a bracketed description ("[Figure 13.1: ...]"), and no figure files exist. In the description of Figure 13.1 the directions are reversed: with the boundary penalty on the horizontal axis, hypervigilance (a larger penalty) is said to shift left and numbing to shift right.

16. **Disparity ratio.** Definition 12.2 divides by the Bond Index of the reference population and is undefined when that index is zero, a case Proposition 12.1 allows.

## Found while drawing the figures (2026-11-26), not changed

These were noticed while the figures were drawn and are left for the author. No figure draws them.

1. Section 2.4 gives Maria Santos a respiratory rate of 28; the START paragraph treats a rate above 30 as abnormal.
2. Attribute scales differ: Chapters 2, 4 and 6 score on 0 to 1, Section 9.5 on -0.9 to +0.9, and Section 9.1 enters changes of minus infinity on d2 and d4, which fit no stated scale.
3. Section 5.11 calls the Euclidean distance a lower bound on the Mahalanobis distance. That is false in general, and it is the error correction 8 removed from Section 4.4.3.
4. Definition 5.1 makes the standard QALY a function of a1 alone, yet Margaret (a1 = 0.45) and David (a1 = 0.35) have the same QALY.
5. Section 6.7 states a Bond Index "much higher than" a dollar amount, for one patient.
6. Section 9.1: Path B's weight is given as (0.4) squared over sigma_1 squared, ignoring the +0.5, +0.2 and +0.3 changes in its own table; the text then says the alternatives keep zero cost on d2 through d9. The case calls an urgent laparotomy in the emergency department "non-emergency". The patient is David Okafor here, James Okafor in Section 1.1, and Patient B of Section 1.6 is David Kowalski.
7. Section 10.3, Case A: "0.50 expected life-years per life-year at stake" is a difference of survival probabilities; the d1 gain is added as a cost in CF(reallocate); and the penalty is compared with a d1 change of 0.5 while Definition 4.3 puts the abandonment penalty at 15 to 50, on which scale reallocation is never optimal.
8. Section 10.8 dates ESI to 2011 and lists it before START (1983); says Larrey discarded social status (d6) and military rank (d8) where Section 2.2.1 credits the same move to d3; White et al. is cited as 2009 in Section 10.3 and 2020 in Section 10.8; "Definition 5 in the GCE paper" (Section 10.5) has no reference.
9. Definition 11.3, condition 2, writes the sacred-value penalty as finite; Definition 4.3 fixes it as infinite.
10. Implication 3 of Chapter 13 ("frequency matters more than severity") compares totals of 50 and 250 and so shows only that a larger sum is larger. Section 13.9 has Sarah's abandonment penalty inflated and then deflated; Section 15.8 says it is still inflated and that the dignity penalty is the deflated one.
11. Section 17.6: 23% of 84 is not a whole number of patients (19 of 84 is 22.6%).

## Figure placeholders

The bracketed figure descriptions that stood in Chapters 1 to 11 and 13 were taken out when the drawn figures went in, and are kept with a verdict on each in figures/PLACEHOLDERS.md. Chapter 14 is not published and keeps its two.
