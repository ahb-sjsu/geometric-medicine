"""Figures for Geometric Medicine, Chapters 1 to 13 and 15 to 18 (2026-11-26).

Every figure is drawn from a formula, a definition or numbers printed in its chapter.
The volume is a posited framework: nothing here is a measurement. Figures taken from the
hypothetical scenarios (Sections 12.4 and 16.8) say so in the figure and in the caption.
"""

import math

from figkit import BORDER, BOX, CRITICAL, GOOD, GRID, INK, INK2, INK3, SERIES, SURFACE, Axes, Canvas, legend, reg

P1 = "manuscript/part_i/"
P2 = "manuscript/part_ii/"
P3 = "manuscript/part_iii/"
P4 = "manuscript/part_iv/"
P5 = "manuscript/part_v/"
P6 = "manuscript/part_vi/"

DIM = ["outcomes", "rights", "justice", "autonomy", "trust", "social", "dignity", "institutional", "epistemic"]
DIMS = ["outcomes", "rights", "justice", "autonomy", "trust", "social", "dignity", "instit.", "epistemic"]


def canvas(w, h, title):
    assert len(title) <= 68, (len(title), title)
    return Canvas(w, h, title)


def box(c, x, y, w, h, fill=BOX, stroke=BORDER, opacity=1.0, rx=4, sw=1):
    c.add(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{rx}" fill="{fill}" '
          f'fill-opacity="{opacity}" stroke="{stroke}" stroke-width="{sw}"/>')


def vbar(c, xc, w, yzero, yval, col):
    top, bot = min(yzero, yval), max(yzero, yval)
    c.add(f'<rect x="{xc - w / 2:.2f}" y="{top:.2f}" width="{w:.2f}" height="{max(bot - top, 0.8):.2f}" rx="2" fill="{col}"/>')


def ring(c, x, y, r, col, width=2):
    c.add(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r:.2f}" fill="{SURFACE}" stroke="{col}" stroke-width="{width}"/>')


def disc(c, x, y, r, col):
    c.add(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r:.2f}" fill="{col}"/>')


def signed(v):
    return f"{v:+.2f}"


# ------------------------------------------------------------------ chapter 1
def fig_01_1():
    rows = [(1, 0.45, 0.35), (4, 0.95, 0.30), (5, 0.90, 0.25), (6, 0.80, 0.35), (7, 0.85, 0.30), (9, 0.95, 0.30)]
    assert all(a > b for _, a, b in rows)
    p = reg(P1 + "ch01_qaly_trap.md", "1.1",
            "The two-patient problem of Section 1.6, a worked example and not data. The top row is the QALY estimate, "
            "about 0.35 for both patients. The six rows below are the scores the section gives each patient, on a scale "
            "from 0 to 1. The two patients are 0.10 apart on outcomes and between 0.45 and 0.65 apart on the other five "
            "dimensions, which the scalar does not carry.",
            "## 1.7 Why Not Just Use Multiple Metrics?")
    c = canvas(720, 400, "One QALY estimate, two different patients")
    x0, w = 200, 400
    X = lambda v: x0 + w * v
    for v in (0, 0.25, 0.5, 0.75, 1):
        c.line(X(v), 58, X(v), 336, GRID, 1)
        c.text(X(v), 352, f"{v:g}", 11, "middle", INK2)
    y = 78
    c.text(x0 - 14, y + 4, "QALY estimate", 11.5, "end", INK, "600")
    c.dot(X(0.35), y, INK, 5.5, title="QALY estimate about 0.35, both patients")
    c.text(X(0.35) + 13, y + 4, "about 0.35 for both patients", 11, "start", INK2)
    c.line(40, 101, 680, 101, BORDER, 1)
    for i, (k, a, b) in enumerate(rows):
        y = 126 + 38 * i
        c.text(x0 - 14, y + 4, f"d{k} {DIM[k - 1]}", 11.5, "end", INK2)
        c.line(X(b), y, X(a), y, INK3, 2)
        c.dot(X(b), y, SERIES[1], 5, title=f"Patient B, d{k} {b}")
        c.dot(X(a), y, SERIES[0], 5, title=f"Patient A, d{k} {a}")
        c.text(X(b) - 11, y + 4, f"{b:.2f}", 10.5, "end", INK)
        c.text(X(a) + 11, y + 4, f"{a:.2f}", 10.5, "start", INK)
    c.text(X(0.5), 370, "score on the dimension, 0 to 1 (Section 1.6)", 11, "middle", INK2)
    legend(c, 60, 390, [("Patient A, Margaret Okonkwo", SERIES[0]), ("Patient B, David Kowalski", SERIES[1])])
    c.save(p)


# ------------------------------------------------------------------ chapter 2
def fig_02_1():
    vals = [0.3, 0.5, 0.4, 0.3, 0.2, 0.5, 0.4, 0.6, 0.2]
    keep = {"ESI": {1, 8}, "START": {1}, "CSC": {1}}
    claimed = {"ESI": set(), "START": set(), "CSC": {3}}
    result = {"ESI": "ESI-2", "START": "Immediate", "CSC": "lower priority"}
    p = reg(P1 + "ch02_triage_forced_contraction.md", "2.1",
            "Maria Santos, the worked example of Section 2.4. On the left is the nine-dimensional attribute vector the "
            "section assigns her, each score between 0 and 1. On the right are the dimensions each of three triage systems "
            "preserves, as the section reads them: the Emergency Severity Index keeps outcomes and institutional resources, "
            "START keeps a minimal reading of outcomes, and crisis standards of care keep outcomes and claim justice. "
            "The bottom row is the classification each system returns for the same patient.",
            "## 2.5 Why Clinicians Resist Utilitarian Triage")
    c = canvas(720, 440, "One patient, three triage contractions")
    bx, bw = 160, 240
    cols = {"ESI": 500, "START": 580, "CSC": 660}
    c.text(bx, 66, "attribute vector (Section 2.4)", 11, "start", INK2)
    for name, x in cols.items():
        c.text(x, 66, name, 12, "middle", INK, "600")
    for i, v in enumerate(vals):
        y = 94 + 31 * i
        c.line(40, y + 15.5, 700, y + 15.5, GRID, 1)
        c.text(bx - 12, y + 4, f"d{i + 1} {DIM[i]}", 11.5, "end", INK2)
        c.hrect(bx, y - 7, bw * v, 14, SERIES[2], title=f"d{i + 1} {v}")
        c.text(bx + bw * v + 8, y + 4, f"{v:.1f}", 10.5, "start", INK)
        for name, x in cols.items():
            if i + 1 in keep[name]:
                c.dot(x, y, SERIES[0], 6, title=f"{name} preserves d{i + 1}")
            elif i + 1 in claimed[name]:
                ring(c, x, y, 6, SERIES[0])
            else:
                disc(c, x, y, 2, INK3)
    y = 386
    c.text(440, y, "classification", 11, "end", INK2)
    for name, x in cols.items():
        c.text(x, y, result[name], 10.5, "middle", INK, "600")
    ly = 420
    c.dot(60, ly - 4, SERIES[0], 5)
    c.text(72, ly, "preserved", 11, "start", INK2)
    ring(c, 160, ly - 4, 5, SERIES[0])
    c.text(172, ly, "claimed, typically not implemented", 11, "start", INK2)
    disc(c, 400, ly - 4, 2, INK3)
    c.text(410, ly, "discarded", 11, "start", INK2)
    c.save(p)


# ------------------------------------------------------------------ chapter 3
def fig_03_1():
    rows = [("Hippocratic Oath, 400 BCE", {1, 2, 5}, "named"),
            ("Nuremberg Code, 1947", {4, 9}, "named"),
            ("Informed consent law, 1957–72", {4, 9}, "named"),
            ("Beauchamp & Childress, 1979", {1, 2, 3, 4}, "named"),
            ("Ethics of care, 1982–84", {5, 6}, "named"),
            ("Casuistry, 1988", set(range(1, 10)), "implicit"),
            ("Evidence-based medicine, 1992", {1}, "named"),
            ("Shared decision-making, 1997", {4, 9}, "named"),
            ("Narrative ethics, 2006", set(), "none")]
    named = set().union(*[s for _, s, k in rows if k == "named"])
    assert named == {1, 2, 3, 4, 5, 6, 9}          # no tradition in the table names d7 or d8 outright
    p = reg(P1 + "ch03_history_medical_ethics.md", "3.1",
            "The table of Section 3.10 laid out as a grid: one row for each tradition, one column for each of the nine "
            "dimensions, and a filled mark where the table says the tradition captured that dimension. Casuistry is "
            "entered as the table has it, the full manifold implicitly. Narrative ethics is credited with trajectory "
            "structure and no dimension. Read down the columns: in this reading no tradition names dignity or "
            "institutional legitimacy outright.",
            "## 3.11 Sarah Reads the History")
    c = canvas(720, 420, "Which dimensions each tradition captured, as Section 3.10 reads them")
    X = lambda j: 268 + 50 * j
    for j in range(9):
        c.text(X(j), 58, f"d{j + 1}", 11.5, "middle", INK, "600")
        c.text(X(j), 71, DIMS[j], 9, "middle", INK2)
    for i, (name, dims, kind) in enumerate(rows):
        y = 98 + 30 * i
        c.line(30, y + 15, 696, y + 15, GRID, 1)
        c.text(238, y + 4, name, 11, "end", INK2)
        if kind == "none":
            c.text(X(4), y + 4, "trajectory structure; no dimension named", 10.5, "middle", INK3, italic=True)
            continue
        for j in range(9):
            if j + 1 in dims:
                if kind == "named":
                    c.dot(X(j), y, SERIES[0], 6, title=f"{name}: d{j + 1}")
                else:
                    ring(c, X(j), y, 6, SERIES[0])
    ly = 386
    c.dot(60, ly - 4, SERIES[0], 5)
    c.text(72, ly, "captured, per the table", 11, "start", INK2)
    ring(c, 250, ly - 4, 5, SERIES[0])
    c.text(262, ly, "implicit (casuistry: the full manifold, implicitly)", 11, "start", INK2)
    c.text(60, 408, "The framework's own reading of the history, not a historical finding.", 10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 4
def fig_04_1():
    rows = [("harm", 5, 20, None), ("futility", 10, 30, None),
            ("consent: emergency or incapacitated", 5, 15, None),
            ("consent: competent, non-emergency", None, None, "β ≈ ∞"),
            ("abandonment", 15, 50, None),
            ("sacred value", None, None, "β = ∞")]
    p = reg(P2 + "ch04_clinical_manifold.md", "4.1",
            "The typical calibrations that Definition 4.3 posits for the five clinical-moral boundaries, in the chapter's "
            "normalized units. The horizontal axis is the boundary penalty. A bar spans the range the definition gives. "
            "An arrow marks a penalty the definition sets to infinity: consent of a competent patient outside an emergency, "
            "and the sacred-value boundary. These are posited values, not estimates from data.",
            "### 4.4.3 A Worked Example")
    c = canvas(720, 400, "Posited calibration of the five clinical-moral boundaries")
    x0, w = 262, 370
    X = lambda v: x0 + w * v / 55
    for v in range(0, 51, 10):
        c.line(X(v), 60, X(v), 318, GRID, 1)
        c.text(X(v), 336, str(v), 11, "middle", INK2)
    for i, (name, lo, hi, inf) in enumerate(rows):
        y = 84 + 42 * i
        c.text(x0 - 14, y + 4, name, 11.5, "end", INK2)
        if inf:
            c.arrow(X(0), y, X(55) + 12, y, CRITICAL, 2.5)
            c.text(X(27.5), y - 9, inf, 12, "middle", INK, "600")
        else:
            c.line(X(lo), y, X(hi), y, SERIES[0], 7)
            c.text(X(lo) - 10, y + 4, str(lo), 10.5, "end", INK)
            c.text(X(hi) + 10, y + 4, str(hi), 10.5, "start", INK)
    c.text(x0 + w / 2, 360, "boundary penalty β, normalized units (Definition 4.3, typical calibration)", 11, "middle", INK2)
    c.text(16, 388, "Posited values. None has been estimated.", 10.5, "start", INK3, italic=True)
    c.save(p)


def fig_04_2():
    cur = [0.25, 0.5, 0.5, 0.2, 0.4, 0.3, 0.4, 0.6, 0.3]
    intub = [0.35, 0.5, 0.4, 0.1, 0.3, 0.2, 0.2, 0.7, 0.25]
    supp = [0.20, 0.5, 0.5, 0.3, 0.5, 0.4, 0.5, 0.5, 0.3]
    da = [round(b - a, 4) for a, b in zip(cur, intub)]
    db = [round(b - a, 4) for a, b in zip(cur, supp)]
    assert da == [0.10, 0.0, -0.10, -0.10, -0.10, -0.10, -0.20, 0.10, -0.05]
    assert db == [-0.05, 0.0, 0.0, 0.10, 0.10, 0.10, 0.10, -0.10, 0.0]
    assert abs(sum(x * x for x in da) - 0.1025) < 1e-9
    assert abs((0.15 + 10) - 10.15) < 1e-9
    p = reg(P2 + "ch04_clinical_manifold.md", "4.2",
            "The worked example of Section 4.4.3. Each pair of bars is the change that one action makes on one dimension, "
            "computed from the three attribute vectors the section prints. Intubation raises outcomes and institutional "
            "compliance by 0.10 and lowers six other dimensions. Supportive care lowers those two and raises four. "
            "The edge weights in the legend are the section's illustrative values: the covariance matrix has not been "
            "estimated, and almost all of the weight of intubation is the consent boundary penalty of 10.",
            "## 4.5 The Clinical-Moral Covariance Matrix")
    c = canvas(720, 420, "Intubation or supportive care: the change on each dimension")
    box(c, 70, 43, 12, 12, SERIES[1], SERIES[1], rx=3)
    c.text(88, 53, "Intubation: w ≈ 0.15 + 10 (consent boundary) = 10.15, illustrative", 11.5, "start", INK2)
    box(c, 70, 61, 12, 12, SERIES[0], SERIES[0], rx=3)
    c.text(88, 71, "Supportive care: w ≈ 0.05 + 0 = 0.05, illustrative", 11.5, "start", INK2)
    ax = Axes(c, 70, 92, 620, 236, (0, 9), (-0.25, 0.15), [], [-0.2, -0.1, 0, 0.1], "", "change in the score")
    c.line(ax.x0, ax.Y(0), ax.x0 + ax.w, ax.Y(0), INK3, 1.2)
    for i in range(9):
        xc = ax.X(i + 0.5)
        for off, v, col in ((-12, da[i], SERIES[1]), (12, db[i], SERIES[0])):
            if v == 0:
                c.line(xc + off - 9, ax.Y(0), xc + off + 9, ax.Y(0), col, 3)
                continue
            vbar(c, xc + off, 20, ax.Y(0), ax.Y(v), col)
            c.text(xc + off, ax.Y(v) - 5 if v > 0 else ax.Y(v) + 13, signed(v), 9.5, "middle", INK)
        c.text(xc, ax.y0 + ax.h + 18, f"d{i + 1}", 11.5, "middle", INK, "600")
        c.text(xc, ax.y0 + ax.h + 32, DIMS[i], 9.5, "middle", INK2)
    c.text(16, 408, "A short stroke on the zero line marks no change.", 10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 5
def fig_05_1():
    w1, w5 = 0.7, 0.3
    Q = lambda a, b: w1 * a + w5 * b
    A, B = (0.35, 0.85), (0.65, 0.15)
    assert abs(Q(*A) - 0.5) < 1e-12 and abs(Q(*B) - 0.5) < 1e-12
    p = reg(P2 + "ch05_qaly_irrecoverability.md", "5.1",
            "A schematic of Theorem 5.1 in two of the nine dimensions. The square is the plane of outcomes and one other "
            "dimension. The slanted lines are level sets of a weighted-sum QALY function of the kind Definition 5.1 "
            "allows, drawn with illustrative weights 0.7 and 0.3. States A and B lie on the same level set, so the "
            "function sends both to 0.5 on the axis at the right, and nothing computed from 0.5 can tell them apart. "
            "In nine dimensions the level set has dimension at least 8.",
            "## 5.3 What Exactly Is Lost?")
    c = canvas(720, 400, "Two states on one level set land on the same QALY value")
    X = lambda a: 90 + 270 * a
    Y = lambda b: 330 - 270 * b
    box(c, X(0), Y(1), 270, 270, "none", GRID, rx=0)
    c.text(X(0.5), 356, "outcomes d1", 11.5, "middle", INK2)
    c.text(64, Y(0.5), "another dimension, for example trust d5", 11.5, "middle", INK2, rotate=-90)
    for v in (0, 1):
        c.text(X(v), 344, str(v), 10.5, "middle", INK3)
        c.text(X(0) - 8, Y(v) + 4, str(v), 10.5, "end", INK3)
    for lv in (0.3, 0.5, 0.7):
        a_top, a_bot = max(0.0, (lv - w5) / w1), min(1.0, lv / w1)
        b_top, b_bot = (lv - w1 * a_top) / w5, (lv - w1 * a_bot) / w5
        c.line(X(a_top), Y(b_top), X(a_bot), Y(b_bot), INK if lv == 0.5 else INK3, 2 if lv == 0.5 else 1.3)
        c.text(X((lv - w5 * 0.07) / w1) + 7, Y(0.07) + 4, f"Q = {lv}", 10.5, "start", INK2)
    qx = 540
    YQ = lambda q: 330 - 270 * q
    for pt in (A, B):
        c.line(X(pt[0]), Y(pt[1]), qx - 8, YQ(0.5), INK3, 1.2, dash="4 4")
    c.dot(X(A[0]), Y(A[1]), SERIES[0], 5.5, title="state A (0.35, 0.85)")
    c.dot(X(B[0]), Y(B[1]), SERIES[1], 5.5, title="state B (0.65, 0.15)")
    c.text(X(A[0]) - 11, Y(A[1]) + 4, "A", 12, "end", INK, "600")
    c.text(X(B[0]) - 11, Y(B[1]) + 4, "B", 12, "end", INK, "600")
    c.line(qx, YQ(0), qx, YQ(1), INK2, 1.5)
    for q in (0, 0.3, 0.5, 0.7, 1):
        c.line(qx - 4, YQ(q), qx + 4, YQ(q), INK2, 1.5)
        c.text(qx + 10, YQ(q) + 4, f"{q:g}", 10.5, "start", INK2)
    c.dot(qx, YQ(0.5), CRITICAL, 5.5, title="Q(A) = Q(B) = 0.5")
    c.text(qx, 50, "QALY value Q", 11.5, "middle", INK2)
    c.text(578, YQ(0.5) - 4, "Q(A) = Q(B)", 11.5, "start", INK, "600")
    c.text(578, YQ(0.5) + 12, "= 0.5", 11.5, "start", INK, "600")
    c.text(16, 388, "Schematic. A = (0.35, 0.85), B = (0.65, 0.15), Q = 0.7 d1 + 0.3 d5; the weights are illustrative.",
           10.5, "start", INK3, italic=True)
    c.save(p)


def fig_05_2():
    m = [0.45, 0.8, 0.7, 0.95, 0.9, 0.8, 0.85, 0.7, 0.95]
    d = [0.35, 0.5, 0.5, 0.3, 0.25, 0.35, 0.3, 0.5, 0.3]
    sq = [round((a - b) ** 2, 4) for a, b in zip(m, d)]
    assert sq == [0.01, 0.09, 0.04, 0.4225, 0.4225, 0.2025, 0.3025, 0.04, 0.4225]
    assert abs(sum(sq) - 1.9525) < 1e-9 and abs(math.sqrt(sum(sq)) - 1.40) < 0.005
    assert min(sq) == sq[0]
    p = reg(P2 + "ch05_qaly_irrecoverability.md", "5.2",
            "The two patients of Section 5.11, both with a QALY estimate of 0.35. Each bar is the squared difference "
            "between their scores on one dimension, computed from the two attribute vectors the section prints. The bars "
            "sum to 1.9525, a Euclidean distance of about 1.40. Outcomes, the dimension the standard QALY is a function "
            "of, contributes 0.01, the smallest of the nine. This is a worked example, not data.",
            "## 5.12 Comparison to Other Irrecoverability Results")
    c = canvas(720, 400, "The two patients differ least on the dimension the QALY reads")
    ax = Axes(c, 70, 56, 620, 256, (0, 9), (0, 0.5), [], [0, 0.1, 0.2, 0.3, 0.4, 0.5], "", "squared difference")
    for i, v in enumerate(sq):
        xc = ax.X(i + 0.5)
        c.rect(xc - 12, ax.Y(v), 24, ax.Y(0) - ax.Y(v), CRITICAL if i == 0 else SERIES[0], title=f"d{i + 1} {v}")
        c.text(xc, ax.Y(v) - 6, f"{v:g}", 10.5, "middle", INK)
        c.text(xc, ax.y0 + ax.h + 18, f"d{i + 1}", 11.5, "middle", INK, "600")
        c.text(xc, ax.y0 + ax.h + 32, DIMS[i], 9.5, "middle", INK2)
    c.text(16, 386, "Sum 1.9525; Euclidean distance √1.9525 ≈ 1.40 (Section 5.11). Worked example, not data.",
           10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 6
def fig_06_1():
    p = reg(P2 + "ch06_clinical_astar.md", "6.1",
            "A schematic of the first example of Section 6.4.2, the patient who refuses transfusion. The dashed path is "
            "the QALY-optimal one: it transfuses to maximize outcomes and so crosses the consent boundary, whose penalty "
            "the chapter sets to infinity, which makes the edge weight infinite. The solid path is the clinical geodesic "
            "as the chapter defines it: it respects the refusal, pursues alternatives and reaches the goal region at "
            "finite total cost.",
            "## 6.5 Clinical Reasoning in Practice")
    c = canvas(720, 400, "Forced transfusion has infinite cost; the geodesic goes around")
    c.box(30, 190, 150, 50, "Start v0", "competent refusal")
    c.box(310, 100, 170, 50, "Forced transfusion", "maximizes d1")
    c.box(540, 100, 150, 50, "Highest d1", "edge weight w = ∞")
    c.box(310, 290, 170, 50, "Respect the refusal", "pursue alternatives")
    c.box(540, 290, 150, 50, "Goal region G", "finite total cost")
    # QALY-optimal path, dashed
    c.line(180, 203, 302, 133, SERIES[1], 2.2, dash="6 5")
    c.arrow(296, 136.5, 304, 132, SERIES[1], 2.2)
    c.line(480, 125, 532, 125, SERIES[1], 2.2, dash="6 5")
    c.arrow(526, 125, 534, 125, SERIES[1], 2.2)
    # geodesic, solid
    c.arrow(180, 227, 304, 307, SERIES[0], 2.2)
    c.arrow(480, 315, 534, 315, SERIES[0], 2.2)
    # consent boundary
    c.line(245, 66, 245, 206, CRITICAL, 2, dash="3 5")
    c.text(253, 76, "consent boundary", 11, "start", INK, "600")
    c.text(253, 91, "penalty β = ∞", 11, "start", INK2)
    c.text(395, 172, "QALY-optimal path (dashed)", 11, "middle", INK2)
    c.text(395, 276, "clinical geodesic (solid)", 11, "middle", INK2)
    c.text(16, 388, "Schematic of Section 6.4.2, example 1. No quantity is drawn to scale.", 10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 7
def fig_07_1():
    cols = [(1, "outcomes"), (4, "autonomy"), (7, "dignity"), (8, "institutional")]
    rows = [("Emergency medicine", {1: "low", 7: "high"}),
            ("Palliative care", {7: "low", 1: "moderate"}),
            ("Surgery", {1: "low", 4: "high"}),
            ("Psychiatry", {4: "low", 8: "high"})]
    style = {"low": (7, SERIES[0]), "moderate": (11, SERIES[5]), "high": (15, SERIES[1])}
    p = reg(P2 + "ch07_heuristic_spectrum.md", "7.1",
            "The dimension-specific calibration errors that Proposition 7.2 posits for four specialties. A small mark is a "
            "low error on that dimension, a large mark a high one. A blank cell means the proposition says nothing for "
            "that pair. The profiles are complementary: where one specialty is posited to be poorly calibrated, another "
            "is posited to be well calibrated, which is the chapter's account of why cross-specialty ethics consultation "
            "helps. The levels are the proposition's words and have not been measured.",
            "## 7.4 Clinical Training as Heuristic Calibration")
    c = canvas(720, 380, "Posited calibration error by specialty: complementary profiles")
    X = lambda j: 310 + 110 * j
    for j, (k, name) in enumerate(cols):
        c.text(X(j), 62, f"ε{k}", 12, "middle", INK, "600")
        c.text(X(j), 77, name, 10.5, "middle", INK2)
    for i, (name, prof) in enumerate(rows):
        y = 120 + 58 * i
        c.line(40, y + 37, 690, y + 37, GRID, 1)
        c.text(230, y + 4, name, 12, "end", INK2)
        for j, (k, _) in enumerate(cols):
            if k in prof:
                r, col = style[prof[k]]
                disc(c, X(j), y, r, col)
                c.text(X(j) + r + 7, y + 4, prof[k], 10.5, "start", INK)
    c.text(16, 366, "Blank: not stated. Levels are the words of Proposition 7.2, not measurements.", 10.5, "start", INK3,
           italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 8
def fig_08_1():
    p = reg(P2 + "ch08_consent_gauge.md", "8.1",
            "A schematic of the three alignment conditions of Definition 8.2 and how each can fail (Section 8.4.1). "
            "Left: the patient and the clinician place the same clinical fact differently, a gap in understanding. "
            "Middle: the clinician's estimate of one of the patient's boundary penalties is far from the patient's own. "
            "Right: the two goal regions differ; where they overlap, the joint geodesic aims at the overlap. "
            "Under each panel are the presentation and the intervention the section gives.",
            "## 8.5 The Medical Bond Invariance Principle")
    c = canvas(720, 400, "Three ways shared decision-making can fail to align")
    for x in (245, 475):
        c.line(x, 48, x, 336, GRID, 1)
    heads = ["(a) Epistemic: a gap on d9", "(b) Value: a gap on d2 to d8", "(c) Goal: the regions G differ"]
    for i, hd in enumerate(heads):
        c.text(24 + 230 * i, 66, hd, 12, "start", INK, "600")
    # (a)
    c.line(40, 190, 225, 190, INK3, 1.5)
    c.line(78, 190, 192, 190, INK2, 3)
    c.dot(78, 190, SERIES[1], 5.5)
    c.dot(192, 190, SERIES[0], 5.5)
    c.text(78, 170, "patient: routine", 10.5, "middle", INK2)
    c.text(228, 148, "clinician: high-risk", 10.5, "end", INK2)
    c.line(192, 154, 192, 180, GRID, 1)
    c.text(132, 214, "risk of the surgery, as each sees it", 10, "middle", INK3)
    # (b)
    c.line(270, 236, 455, 236, INK3, 1.5)
    c.rect(300, 106, 24, 130, SERIES[1])
    c.rect(400, 186, 24, 50, SERIES[0])
    c.text(312, 252, "patient's own β", 10, "middle", INK2)
    c.text(412, 252, "clinician's estimate", 10, "middle", INK2)
    # (c)
    c.ellipse(560, 178, 58, 44, 0, SERIES[0], SERIES[0], 2, 0.12)
    c.ellipse(626, 186, 54, 42, 0, SERIES[1], SERIES[1], 2, 0.12)
    c.text(538, 124, "G clinician", 10.5, "middle", INK2)
    c.text(648, 134, "G patient", 10.5, "middle", INK2)
    c.dot(594, 183, INK, 4)
    c.line(594, 189, 594, 244, GRID, 1)
    c.text(594, 256, "joint target, in the overlap", 10, "middle", INK3)
    txt = [("Presents as uninformed deference.", "Intervention: plain language, teach-back."),
           ("Presents as hesitation or refusal.", "Intervention: elicit the patient's values."),
           ("Presents as talking past each other.", "Intervention: negotiate the goal region.")]
    for i, (a, b) in enumerate(txt):
        c.text(24 + 230 * i, 296, a, 10, "start", INK2)
        c.text(24 + 230 * i, 313, b, 10, "start", INK2)
    c.text(16, 386, "Schematic of Definition 8.2 and Section 8.4.1. Nothing is drawn to scale.", 10.5, "start", INK3,
           italic=True)
    c.save(p)


def fig_08_2():
    rows = [("Positive or negative framing", "“90% survive” or “10% die”", True),
            ("Absolute numbers or relative risk", "“2 in 100 have complications” or “the risk is doubled from 1% to 2%”", False),
            ("Gains or losses", "“you will gain 3 years of life” or “without treatment, you will lose 3 years”", True),
            ("Natural frequencies or percentages", "“2 out of 100 patients” or “2% of patients”", True)]
    cis = sum(1 for r in rows if r[2]) / len(rows)
    assert cis == 0.75 and cis < 0.8
    p = reg(P2 + "ch08_consent_gauge.md", "8.2",
            "The consent invariance score of Definition 8.4, worked for an illustrative patient. The four rows are the "
            "meaning-preserving transformations listed in Section 8.3.1. This patient's decision stays the same under "
            "three and changes under one, so the score is 3 of 4, or 0.75. That is below 0.8, the example threshold the "
            "section mentions, and the row that changes shows where more explanation is needed. The responses are "
            "invented to show the computation; no patient was tested.",
            "## Summary")
    c = canvas(720, 400, "Consent invariance score: an illustrative patient")
    c.text(30, 60, "meaning-preserving transformation (Section 8.3.1)", 11, "start", INK2)
    c.text(560, 60, "decision", 11, "start", INK2)
    for i, (name, frames, same) in enumerate(rows):
        y = 88 + 46 * i
        c.line(30, y + 26, 690, y + 26, GRID, 1)
        c.text(30, y, name, 12, "start", INK, "600")
        c.text(30, y + 16, frames, 10, "start", INK2)
        if same:
            c.dot(566, y + 3, GOOD, 5.5)
            c.text(580, y + 7, "stays the same", 11, "start", INK)
        else:
            ring(c, 566, y + 3, 5.5, CRITICAL, 2.5)
            c.text(580, y + 7, "changes", 11, "start", INK, "600")
    x0, w, ya = 150, 410, 312
    X = lambda v: x0 + w * v
    c.text(x0 - 14, ya + 4, "CIS", 12, "end", INK, "600")
    c.line(X(0), ya, X(1), ya, INK3, 1.5)
    for v in (0, 0.25, 0.5, 0.75, 1):
        c.line(X(v), ya - 4, X(v), ya + 4, INK3, 1.5)
        c.text(X(v), ya + 19, f"{v:g}", 10.5, "middle", INK2)
    c.line(X(0.8), ya - 22, X(0.8), ya + 8, INK2, 1.5, dash="4 4")
    c.text(X(0.8) + 6, ya - 14, "example threshold, CIS ≥ 0.8", 10.5, "start", INK2, italic=True)
    c.dot(X(cis), ya, INK, 5.5, title="CIS 0.75")
    c.text(X(cis) - 10, ya - 12, "this patient: 3 of 4 = 0.75", 11, "end", INK)
    c.text(16, 386, "Illustrative responses, not data.", 10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 9
def fig_09_1():
    inf = float("-inf")
    A = [0.8, inf, 0, inf, -0.9, -0.5, -0.8, -0.7, 0]
    B = [-0.4, 0, 0, 0, 0.5, 0.2, 0, 0.3, 0]
    assert [i + 1 for i, v in enumerate(A) if v == inf] == [2, 4]
    p = reg(P3 + "ch09_clinical_cases.md", "9.1",
            "Case 1 of Section 9.1, a worked example. Each pair of bars is the change the section's two tables assign to "
            "one dimension. Path A, transfusing against the refusal, raises outcomes by 0.8 and is entered as minus "
            "infinity on rights and on autonomy; those two bars are drawn running off the scale. Path B, respecting the "
            "refusal and pursuing alternatives, lowers outcomes by 0.4 and raises trust, social impact and institutional "
            "legitimacy. The chapter gives Path A infinite weight and Path B a finite one.",
            '### The Geodesic Is Not a "Compromise"')
    c = canvas(720, 440, "Case 1: Path A is off the scale on rights and on autonomy")
    box(c, 70, 43, 12, 12, SERIES[1], SERIES[1], rx=3)
    c.text(88, 53, "Path A, transfuse against the refusal: edge weight w = ∞", 11.5, "start", INK2)
    box(c, 70, 61, 12, 12, SERIES[0], SERIES[0], rx=3)
    c.text(88, 71, "Path B, respect the refusal and pursue alternatives: w finite", 11.5, "start", INK2)
    ax = Axes(c, 70, 92, 620, 262, (0, 9), (-1.3, 1.0), [], [-1, -0.5, 0, 0.5, 1], "", "change on the dimension")
    c.line(ax.x0, ax.Y(0), ax.x0 + ax.w, ax.Y(0), INK3, 1.2)
    for i in range(9):
        xc = ax.X(i + 0.5)
        for off, v, col in ((-12, A[i], SERIES[1]), (12, B[i], SERIES[0])):
            x = xc + off
            if v == 0:
                c.line(x - 9, ax.Y(0), x + 9, ax.Y(0), col, 3)
            elif v == inf:
                yb = ax.Y(-1.22)
                vbar(c, x, 20, ax.Y(0), yb, col)
                c.add(f'<path d="M{x - 10:.1f},{yb:.1f} L{x + 10:.1f},{yb:.1f} L{x:.1f},{yb + 9:.1f} Z" fill="{col}"/>')
                c.text(x + 24, ax.Y(-1.1), "−∞", 12, "middle", INK, "600")
            else:
                vbar(c, x, 20, ax.Y(0), ax.Y(v), col)
                c.text(x, ax.Y(v) - 5 if v > 0 else ax.Y(v) + 13, f"{v:+.1f}", 9.5, "middle", INK)
        c.text(xc, ax.y0 + ax.h + 20, f"d{i + 1}", 11.5, "middle", INK, "600")
        c.text(xc, ax.y0 + ax.h + 34, DIMS[i], 9.5, "middle", INK2)
    c.text(16, 426, "Entries of the two tables of Section 9.1. A short stroke on the zero line marks no change.",
           10.5, "start", INK3, italic=True)
    c.save(p)


def fig_09_2():
    pre = [-0.9, 0, 0, 0.7, 0.3, -0.5, 0.8, 0, 0.9]
    post = [0.8, 0, 0, 0.7, 0.6, 0.3, 0.2, 0, 0.5]
    assert round(post[0] - pre[0], 2) == 1.7 and round(post[6] - pre[6], 2) == -0.6 and round(post[8] - pre[8], 2) == -0.4
    p = reg(P3 + "ch09_clinical_cases.md", "9.2",
            "Case 5 of Section 9.5, a worked example. Each row is one dimension; the ring is the attribute before deep "
            "brain stimulation and the filled mark is the attribute after, on the section's scale from minus 1 to plus 1. "
            "Outcomes rise from minus 0.9 to plus 0.8, and trust and social impact rise. Dignity and identity fall from "
            "0.8 to 0.2 and epistemic status from 0.9 to 0.5. A scalar that reads outcomes sees only the first row.",
            "### The Consent Paradox of Identity-Altering Interventions")
    c = canvas(720, 440, "Case 5: outcomes rise while identity and self-understanding fall")
    x0, w = 190, 430
    X = lambda v: x0 + w * (v + 1) / 2
    for v in (-1, -0.5, 0, 0.5, 1):
        c.line(X(v), 62, X(v), 372, INK3 if v == 0 else GRID, 1)
        c.text(X(v), 388, f"{v:g}", 11, "middle", INK2)
    for i in range(9):
        y = 84 + 34 * i
        a, b = pre[i], post[i]
        c.text(x0 - 30, y + 4, f"d{i + 1} {DIM[i]}", 11.5, "end", INK2)
        if a == b:
            c.dot(X(a), y, INK3, 5)
            c.text(X(a) + 12, y + 4, f"{a:g}, unchanged", 10.5, "start", INK2)
            continue
        col = SERIES[0] if b > a else SERIES[1]
        s = 1 if b > a else -1
        c.arrow(X(a) + 7 * s, y, X(b) - 9 * s, y, col, 2.2)
        ring(c, X(a), y, 5, INK2)
        c.dot(X(b), y, col, 5)
        c.text(X(a) - 12 * s, y + 4, f"{a:+.1f}", 10.5, "end" if s > 0 else "start", INK)
        c.text(X(b) + 12 * s, y + 4, f"{b:+.1f}", 10.5, "start" if s > 0 else "end", INK)
    ly = 422
    ring(c, 60, ly - 4, 5, INK2)
    c.text(72, ly, "before", 11, "start", INK2)
    c.dot(140, ly - 4, SERIES[0], 5)
    c.text(152, ly, "after, higher", 11, "start", INK2)
    c.dot(260, ly - 4, SERIES[1], 5)
    c.text(272, ly, "after, lower", 11, "start", INK2)
    c.text(704, ly, "worked example (Section 9.5), not data", 10.5, "end", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 10
def fig_10_1():
    n, vents = 30, 12
    lottery = [11, 12, 13, 14]
    fixed = [r for r in range(1, vents + 1) if r not in lottery]
    left = vents - len(fixed)
    assert n - vents == 18 and len(fixed) == 10 and left == 2 and n - len(fixed) - len(lottery) == 16
    p = reg(P4 + "ch10_pandemic_triage.md", "10.1",
            "A schematic of Scenario 1 of Section 10.6: thirty patients who need a ventilator and twelve ventilators. "
            "Each mark is a position in the ranking by expected life-years; no prognosis is drawn. The scalar computation "
            "ventilates ranks 1 to 12 and denies the other 18. One of the modifications the chapter proposes treats ranks "
            "11 to 14 as within measurement error and allocates among them by lottery, which by arithmetic leaves ten "
            "places set by ranking and two ventilators for those four patients.",
            "### Scenario 2: The Slow Surge — Accumulated Decisions Over Weeks")
    c = canvas(720, 400, "Thirty patients, twelve ventilators: where the computations differ")
    X = lambda r: 48 + 21.5 * (r - 1)

    def row(y, title, kind):
        c.text(30, y - 34, title, 11.5, "start", INK, "600")
        for r in range(1, n + 1):
            if kind == "scalar":
                st = "in" if r <= vents else "out"
            else:
                st = "lot" if r in lottery else ("in" if r in fixed else "out")
            if st == "in":
                disc(c, X(r), y, 7, SERIES[0])
            elif st == "lot":
                disc(c, X(r), y, 7, SERIES[5])
            else:
                ring(c, X(r), y, 6, INK3, 1.5)
        for r in (1, 10, 12, 14, 30):
            c.text(X(r), y + 21, str(r), 9.5, "middle", INK3)

    row(118, "Scalar computation: rank by expected life-years, ventilate the top twelve", "scalar")
    c.line(X(12.5), 98, X(12.5), 146, INK2, 1.5, dash="4 4")
    c.text(X(6.5), 162, "12 ventilated", 11, "middle", INK2)
    c.text(X(21.5), 162, "18 denied", 11, "middle", INK2)
    row(246, "One manifold-aware modification: ranks 11 to 14 by lottery", "aware")
    c.text(X(5.5), 290, "10 by ranking", 11, "middle", INK2)
    c.text(X(12.5), 290, "lottery: 2 ventilators, 4 patients", 11, "middle", INK2)
    c.text(X(24), 290, "16 denied", 11, "middle", INK2)
    c.text(X(1) - 8, 139, "rank", 9.5, "end", INK3)
    ly = 334
    disc(c, 60, ly - 4, 6, SERIES[0])
    c.text(72, ly, "ventilated by ranking", 11, "start", INK2)
    disc(c, 240, ly - 4, 6, SERIES[5])
    c.text(252, ly, "allocated by lottery", 11, "start", INK2)
    ring(c, 410, ly - 4, 5.5, INK3, 1.5)
    c.text(422, ly, "denied", 11, "start", INK2)
    c.text(16, 366, "Schematic of Scenario 1, Section 10.6: positions in the ranking only. The chapter lists two further",
           10.5, "start", INK3, italic=True)
    c.text(16, 382, "modifications, on withdrawal from current patients and on monitoring the Bond Index.",
           10.5, "start", INK3, italic=True)
    c.save(p)


def fig_10_2():
    rows = [("Larrey, battlefield triage", {1}, set(), "fill"),
            ("Emergency Severity Index", {1, 8}, set(), "fill"),
            ("START and JumpSTART", {1}, set(), "fill"),
            ("Crisis standards of care", {1}, {3}, "fill"),
            ("Full manifold (proposed)", set(range(1, 10)), set(), "ring")]
    counts = [len(a | b) for _, a, b, _ in rows]
    assert counts == [1, 2, 1, 2, 9]
    p = reg(P4 + "ch10_pandemic_triage.md", "10.2",
            "The dimensional reading of triage systems in Section 10.8, as a grid: one row for each system in the order "
            "the section lists them, one column for each of the nine dimensions, and a mark where the section says the "
            "system acknowledges the dimension. The pandemic crisis standards are entered as the section has them, an "
            "attempted expansion to justice. The last row is the framework's proposal, the full nine. The count at the "
            "right runs 1, 2, 1, 2, 9.",
            "## 10.9 The Ethics of Triage Communication")
    c = canvas(720, 380, "Dimensions each triage system acknowledges, per Section 10.8")
    X = lambda j: 292 + 42 * j
    for j in range(9):
        c.text(X(j), 60, f"d{j + 1}", 11.5, "middle", INK, "600")
        c.text(X(j), 73, DIMS[j], 8.5, "middle", INK2)
    c.text(686, 60, "count", 10.5, "middle", INK2)
    for i, (name, dims, tried, kind) in enumerate(rows):
        y = 106 + 44 * i
        c.line(30, y + 22, 700, y + 22, GRID, 1)
        c.text(250, y + 4, name, 11.5, "end", INK2)
        for j in range(9):
            if j + 1 in tried:
                c.dot(X(j), y, SERIES[5], 6, title=f"{name}: attempted d{j + 1}")
            elif j + 1 in dims:
                if kind == "fill":
                    c.dot(X(j), y, SERIES[0], 6, title=f"{name}: d{j + 1}")
                else:
                    ring(c, X(j), y, 6, SERIES[2])
        c.text(686, y + 4, str(counts[i]), 12, "middle", INK, "600")
    ly = 340
    c.dot(60, ly - 4, SERIES[0], 5)
    c.text(72, ly, "acknowledged", 11, "start", INK2)
    c.dot(190, ly - 4, SERIES[5], 5)
    c.text(202, ly, "attempted expansion", 11, "start", INK2)
    ring(c, 360, ly - 4, 5, SERIES[2])
    c.text(372, ly, "proposed by the framework", 11, "start", INK2)
    c.text(16, 366, "Rows in the order Section 10.8 lists them. The framework's reading, not a historical finding.",
           10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 11
def gini(xs):
    xs = sorted(xs)
    n, tot = len(xs), sum(xs)
    return sum((2 * (i + 1) - n - 1) * x for i, x in enumerate(xs)) / (n * tot)


def fig_11_1():
    n = 100
    g = {k: gini([1.0 / k] * k + [0.0] * (n - k)) for k in range(1, n + 1)}
    assert abs(g[n]) < 1e-12 and abs(g[1] - 0.99) < 1e-12 and all(abs(g[k] - (1 - k / n)) < 1e-9 for k in g)
    p = reg(P4 + "ch11_allocation.md", "11.1",
            "The Gini term of Definition 11.5, computed for a population of 100 in which a fixed total cost is split "
            "equally among a share of the people and the rest bear none. The horizontal axis is the share that bears the "
            "cost; the vertical axis is the Gini coefficient of the costs. Equal cost on everyone gives 0, as the section "
            "says, and concentrating the cost on fewer people moves the coefficient toward 1. The definition adds this "
            "coefficient, times a weight λ the community chooses, to the summed individual edge weights.",
            "### The Equity-Efficiency Frontier")
    c = canvas(720, 400, "The Gini term: zero for equal shares, near one when few bear cost")
    ax = Axes(c, 80, 58, 560, 262, (0, 100), (0, 1), [1, 25, 50, 75, 100], [0, 0.25, 0.5, 0.75, 1],
              "share of the population that bears the cost, percent", "Gini coefficient of the cost")
    c.polyline([(ax.X(k), ax.Y(g[k])) for k in range(1, n + 1)], SERIES[0], 2.2)
    c.dot(ax.X(1), ax.Y(g[1]), SERIES[0], 5, title="1 of 100 bears the cost: Gini 0.99")
    c.dot(ax.X(100), ax.Y(g[100]), SERIES[0], 5, title="all bear equal cost: Gini 0")
    c.text(ax.X(1) + 4, ax.Y(g[1]) - 11, "1 person in 100 bears all of it: 0.99", 11, "start", INK)
    c.text(ax.X(87), ax.Y(0.035), "equal cost on everyone: 0", 11, "end", INK)
    c.text(ax.X(98), ax.Y(0.78), "edge weight on B = Σ individual weights + λ · Gini", 11.5, "end", INK2, italic=True)
    c.text(16, 388, "Computed for 100 people, total cost fixed and split equally among those who bear it.", 10.5, "start",
           INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 12
BI12 = [("White", 412, 3.2), ("Black", 198, 7.4), ("Hispanic", 156, 5.1), ("Other", 81, 4.0)]


def fig_12_1():
    parts = [(1, 0.8), (3, 0.6), (5, 1.9), (7, 0.5), (9, 0.4)]
    assert sum(n for _, n, _ in BI12) == 847
    assert abs(sum(v for _, v in parts) - 4.2) < 1e-9 and abs((7.4 - 3.2) - 4.2) < 1e-9
    assert max(parts, key=lambda t: t[1])[0] == 5
    p = reg(P4 + "ch12_bond_index.md", "12.1",
            "The illustrative case study of Section 12.4. The medical center is hypothetical and every number is invented "
            "to show what the computation would report; the clinical Bond Index has not been computed from clinical data. "
            "Left: the Bond Index the scenario assigns to each of four groups of the 847 hypothetical patients. Right: "
            "the scenario's split of the gap between the Black and White groups, 7.4 minus 3.2, into five dimensions. "
            "Trust carries 1.9 of the 4.2.",
            "### What the Bond Index Reveals")
    c = canvas(720, 420, "Illustrative case: the gap between two groups, split by dimension")
    c.text(60, 64, "Bond Index by group (hypothetical)", 11.5, "start", INK, "600")
    ax = Axes(c, 60, 86, 250, 222, (0, 4), (0, 8), [], [0, 2, 4, 6, 8], "", "clinical Bond Index")
    for i, (name, n, v) in enumerate(BI12):
        xc = ax.X(i + 0.5)
        c.rect(xc - 12, ax.Y(v), 24, ax.Y(0) - ax.Y(v), SERIES[0], title=f"{name} {v}")
        c.text(xc, ax.Y(v) - 6, f"{v:.1f}", 11, "middle", INK)
        c.text(xc, ax.y0 + ax.h + 18, name, 11, "middle", INK2)
        c.text(xc, ax.y0 + ax.h + 32, f"n = {n}", 9.5, "middle", INK3)
    c.text(400, 64, "Black and White gap of 4.2, by dimension", 11.5, "start", INK, "600")
    x0, sc = 500, 90
    for v in (0, 1, 2):
        c.line(x0 + sc * v, 80, x0 + sc * v, 272, GRID, 1)
        c.text(x0 + sc * v, 288, str(v), 10.5, "middle", INK2)
    for i, (k, v) in enumerate(parts):
        y = 102 + 36 * i
        c.text(x0 - 12, y + 4, f"d{k} {DIM[k - 1]}", 11, "end", INK2)
        c.hrect(x0, y - 8, sc * v, 16, CRITICAL if k == 5 else SERIES[2], title=f"d{k} {v}")
        c.text(x0 + sc * v + 8, y + 4, f"{v:.1f}", 10.5, "start", INK)
    c.text(400, 318, "0.8 + 0.6 + 1.9 + 0.5 + 0.4 = 4.2 = 7.4 − 3.2", 11, "start", INK2)
    box(c, 40, 368, 640, 34, BOX, BORDER, rx=6)
    c.text(360, 389, "Hypothetical center, invented numbers (Section 12.4). Nothing here is measured.", 11.5, "middle", INK, "600")
    c.save(p)


def fig_12_2():
    ref = BI12[0][2]
    dr = [(name, round(v / ref, 2)) for name, _, v in BI12]
    assert [d for _, d in dr] == [1.00, 2.31, 1.59, 1.25]

    def zone(d):
        return "acceptable" if d < 1.2 else "yellow" if d < 1.5 else "red" if d < 2.0 else "critical"

    assert [zone(d) for _, d in dr] == ["acceptable", "critical", "red", "yellow"]
    p = reg(P4 + "ch12_bond_index.md", "12.2",
            "The disparity ratios of the illustrative case study of Section 12.4, set against the example thresholds of "
            "Proposition 12.2. Both are hypothetical: the ratios come from invented numbers, and the proposition calls "
            "its thresholds illustrative, not prescriptive. The vertical axis is the ratio of a group's Bond Index to "
            "that of the reference group. In the scenario the three non-reference groups fall in three different zones, "
            "at 1.25, 1.59 and 2.31.",
            "## 12.8 The Limits of the Bond Index")
    c = canvas(720, 400, "Illustrative case: disparity ratios against the example thresholds")
    ax = Axes(c, 70, 58, 450, 262, (0, 4), (0.9, 2.5), [], [1.0, 1.2, 1.5, 2.0, 2.5], "", "disparity ratio, reference = 1")
    for t in (1.2, 1.5, 2.0):
        c.line(ax.x0, ax.Y(t), ax.x0 + ax.w + 16, ax.Y(t), INK2, 1.3, dash="4 4")
    zl = [(1.05, "below 1.2: acceptable variation"), (1.35, "1.2 to 1.5: yellow zone"),
          (1.75, "1.5 to 2.0: red zone"), (2.25, "2.0 and above: critical")]
    for v, lab in zl:
        c.text(ax.x0 + ax.w + 24, ax.Y(v) + 4, lab, 10.5, "start", INK2)
    for i, (name, d) in enumerate(dr):
        xc = ax.X(i + 0.5)
        if d > 1:
            c.line(xc, ax.Y(1.0), xc, ax.Y(d), SERIES[0], 3)
        c.dot(xc, ax.Y(d), SERIES[0], 6, title=f"{name} {d:.2f}")
        c.text(xc + 12, ax.Y(d) - 8, f"{d:.2f}", 11, "start", INK)
        c.text(xc, ax.y0 + ax.h + 18, name, 11, "middle", INK2)
    c.text(ax.X(0.5), ax.y0 + ax.h + 32, "(reference)", 9.5, "middle", INK3)
    box(c, 40, 356, 640, 32, BOX, BORDER, rx=6)
    c.text(360, 376, "Hypothetical ratios (Section 12.4) and illustrative thresholds (Proposition 12.2).", 11.5, "middle", INK, "600")
    c.save(p)


# ------------------------------------------------------------------ chapter 13
def fig_13_1():
    beta, tau = 100, 50
    inc = max(0, beta - tau)
    assert inc == 50 and max(0, 40 - tau) == 0
    a = [0] + [50] * 50
    b = [5 * t for t in range(51)]
    assert a[-1] == 50 and b[-1] == 250
    p = reg(P5 + "ch13_moral_injury_theory.md", "13.1",
            "Cumulative moral injury as Definition 13.1 computes it, for the two clinicians of Implication 3 in "
            "Section 13.3. The horizontal axis counts forced boundary crossings and the vertical axis is the running sum. "
            "One clinician makes a single crossing with an increment of 50 and then none. The other makes fifty crossings "
            "with an increment of 5 each and ends at 250. The sum never falls, because each increment is zero or "
            "positive. The values are the chapter's illustration of the definition, not measurements.",
            "## 13.4 The Two Damage Modes: Hypervigilance and Moral Numbing")
    c = canvas(720, 400, "Definition 13.1 adds every forced crossing: 50 × 5 exceeds 1 × 50")
    ax = Axes(c, 80, 58, 560, 262, (0, 50), (0, 260), [0, 10, 20, 30, 40, 50], [0, 50, 100, 150, 200, 250],
              "forced boundary crossings so far", "cumulative moral injury MI(T)")

    def steps(vals):
        pts = [(ax.X(0), ax.Y(0))]
        for t in range(1, 51):
            pts += [(ax.X(t), ax.Y(vals[t - 1])), (ax.X(t), ax.Y(vals[t]))]
        return pts

    c.polyline(steps(a), SERIES[1], 2.2, title="one crossing, increment 50")
    c.polyline(steps(b), SERIES[0], 2.2, title="fifty crossings, increment 5 each")
    c.dot(ax.X(50), ax.Y(250), SERIES[0], 5)
    c.dot(ax.X(50), ax.Y(50), SERIES[1], 5)
    c.text(ax.X(50) + 11, ax.Y(250) + 4, "250", 11, "start", INK)
    c.text(ax.X(50) + 11, ax.Y(50) + 4, "50", 11, "start", INK)
    box(c, ax.X(2), ax.Y(248), 12, 12, SERIES[0], SERIES[0], rx=3)
    c.text(ax.X(2) + 18, ax.Y(248) + 10, "fifty crossings, increment 5 each", 11.5, "start", INK2)
    box(c, ax.X(2), ax.Y(248) + 20, 12, 12, SERIES[1], SERIES[1], rx=3)
    c.text(ax.X(2) + 18, ax.Y(248) + 30, "one crossing, increment 50, then none", 11.5, "start", INK2)
    c.text(16, 388, "Increment per crossing = max(0, β − τ). The chapter's example: β = 100, τ = 50 gives 50.", 10.5,
           "start", INK3, italic=True)
    c.save(p)


def fig_13_2():
    p = reg(P5 + "ch13_moral_injury_theory.md", "13.2",
            "The two damage modes and moral resilience as Definitions 13.2, 13.3 and 13.6 state them, on one axis: a "
            "clinician's penalty for a boundary after forced crossings, compared with the value before. Moral numbing is "
            "a penalty that has fallen below the earlier value; hypervigilance is one that has risen above it; resilience "
            "is one that stays within a tolerance of it. The lines under each mode are the features the table of "
            "Section 13.4 posits. The chapter gives directions only, so no scale is drawn.",
            "## 13.9 Sarah's Moral Injury")
    c = canvas(720, 380, "Two damage modes and resilience, on the boundary-penalty axis")
    ya = 176
    box(c, 318, ya - 22, 84, 44, GOOD, GOOD, opacity=0.16, rx=4)
    c.line(60, ya, 660, ya, INK3, 1.5)
    c.arrow(310, ya, 82, ya, SERIES[2], 3)
    c.arrow(410, ya, 638, ya, SERIES[1], 3)
    c.line(360, ya - 28, 360, ya + 28, INK, 1.5)
    c.text(360, ya + 46, "β before the forced crossings", 11, "middle", INK2)
    c.text(360, 118, "Moral resilience", 12.5, "middle", INK, "600")
    c.text(360, 136, "|β after − β before| < ε", 11, "middle", INK2)
    L, R = 60, 660
    c.text(L, 76, "Moral numbing", 12.5, "start", INK, "600")
    c.text(L, 94, "β after < β before", 11, "start", INK2)
    c.text(R, 76, "Hypervigilance", 12.5, "end", INK, "600")
    c.text(R, 94, "β after > β before", 11, "end", INK2)
    left = ["h(n) underestimates the cost", "A* follows suboptimal paths: too permissive",
            "often gradual, after many moderate crossings"]
    right = ["h(n) overestimates the cost", "A* misses optimal paths: too cautious",
             "often acute, after a single severe crossing"]
    for i, (a, b) in enumerate(zip(left, right)):
        c.text(L, 252 + 18 * i, a, 10.5, "start", INK2)
        c.text(R, 252 + 18 * i, b, 10.5, "end", INK2)
    c.text(L, ya + 20, "lower penalty", 10, "start", INK3)
    c.text(R, ya + 20, "higher penalty", 10, "end", INK3)
    c.text(16, 366, "Schematic of Definitions 13.2, 13.3 and 13.6 and the table of Section 13.4. Posited, not measured.",
           10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 15
def fig_15_1():
    crossings, inc, staff = 30, 5, 6
    one = [crossings * inc] + [0] * (staff - 1)
    rot = [crossings // staff * inc] * staff
    assert sum(one) == sum(rot) == 150 and rot[0] == 25
    p = reg(P5 + "ch15_prevention.md", "15.1",
            "Principle 2 of Section 15.2, worked with illustrative values: 30 forced boundary crossings, each with an "
            "increment of 5, among six physicians. Left: one physician takes every triage decision and accumulates 150 "
            "while the others accumulate nothing. Right: the same crossings in rotation give each physician 25. The total "
            "is 150 in both arrangements, as the section says. The dashed line is the critical threshold the chapter "
            "posits for an individual; its level here is illustrative, and the threshold has not been measured.",
            "### Principle 3: Provide Boundary-Crossing Support in Real Time")
    c = canvas(720, 400, "Rotation keeps the total and lowers each clinician's share")
    ax = Axes(c, 80, 62, 600, 238, (0, 13.5), (0, 170), [], [0, 50, 100, 150], "", "cumulative moral injury")
    c.line(ax.x0, ax.Y(100), ax.x0 + ax.w, ax.Y(100), INK2, 1.5, dash="4 4")
    c.text(ax.x0 + ax.w, ax.Y(100) - 7, "posited threshold for one clinician (level illustrative)", 10.5, "end", INK2,
           italic=True)
    for g, (vals, cx0) in enumerate(((one, 1), (rot, 7.5))):
        for i, v in enumerate(vals):
            xc = ax.X(cx0 + i)
            c.rect(xc - 12, ax.Y(max(v, 0.6)), 24, ax.Y(0) - ax.Y(max(v, 0.6)), SERIES[g], title=f"physician {i + 1}: {v}")
            c.text(xc, ax.Y(v) - 6, str(v), 11, "middle", INK)
            c.text(xc, ax.y0 + ax.h + 17, str(i + 1), 10.5, "middle", INK3)
    c.text(ax.X(3.5), ax.y0 + ax.h + 38, "one physician takes every decision", 11.5, "middle", INK2)
    c.text(ax.X(10), ax.y0 + ax.h + 38, "the six take turns", 11.5, "middle", INK2)
    c.text(ax.X(3.5), ax.y0 + ax.h + 54, "total 150", 10.5, "middle", INK3)
    c.text(ax.X(10), ax.y0 + ax.h + 54, "total 150", 10.5, "middle", INK3)
    c.text(16, 388, "Illustrative values: 30 forced crossings, increment 5 each, six physicians. Not data.", 10.5, "start",
           INK3, italic=True)
    c.save(p)


def fig_15_2():
    pdf = lambda z, s: math.exp(-0.5 * (z / s) ** 2) / (s * math.sqrt(2 * math.pi))
    s_pre, s_post = 1.0, 0.5
    assert s_post ** 2 < s_pre ** 2
    p = reg(P5 + "ch15_prevention.md", "15.2",
            "What Prediction 15.1 says effective ethics consultation should do to the spread of one boundary penalty "
            "across a population of clinicians. The horizontal axis is a clinician's estimate of the penalty, from "
            "deflated at the left to inflated at the right. Before consultation the estimates are spread widely; after, "
            "the prediction is a smaller variance about the same mean. The curves are illustrative normal curves with "
            "the standard deviation halved. This is a prediction to be tested, not a result.",
            "## 15.4 Moral Resilience in the Geometric Framework")
    c = canvas(720, 380, "Prediction 15.1: a narrower spread of penalties, the same mean")
    X = lambda z: 360 + 86 * z
    Y = lambda d: 290 - 250 * d
    zs = [i / 50 for i in range(-160, 161)]
    c.line(80, 290, 640, 290, INK3, 1.5)
    c.line(360, 74, 360, 290, INK2, 1.3, dash="4 4")
    c.polyline([(X(z), Y(pdf(z, s_pre))) for z in zs], SERIES[1], 2.2, title="before consultation")
    c.polyline([(X(z), Y(pdf(z, s_post))) for z in zs], SERIES[0], 2.2, title="after consultation")
    c.text(366, 68, "mean penalty, unchanged", 11, "start", INK2)
    c.text(X(-1.35), Y(pdf(-1.35, s_pre)) - 12, "before: wide spread", 11.5, "end", INK)
    c.text(X(0.55) + 6, Y(pdf(0.55, s_post)) - 6, "after: narrower spread", 11.5, "start", INK)
    c.text(80, 308, "deflated (numbing)", 10.5, "start", INK3)
    c.text(640, 308, "inflated (hypervigilance)", 10.5, "end", INK3)
    c.text(360, 330, "a clinician's estimate of the boundary penalty β", 11.5, "middle", INK2)
    c.text(16, 366, "Illustrative normal curves, standard deviation halved. A prediction to test, not a measurement.",
           10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 16
def fig_16_1():
    ai = {1: "AI optimizes", 9: "AI monitors"}
    human = set(range(2, 9))
    assert set(ai) | human == set(range(1, 10))
    p = reg(P6 + "ch16_ai_clinical.md", "16.1",
            "A schematic of the division of clinical labor that Definition 16.2 proposes. The AI system computes the "
            "accumulated-cost term g(n), optimizes outcomes and monitors diagnostic uncertainty. The human clinician "
            "computes the heuristic term h(n) and assesses the seven dimensions from rights to institutional legitimacy. "
            "Any action that crosses a moral boundary is authorized by a human. This is the chapter's proposal, not a "
            "description of existing systems.",
            "### The Danger of $h(n)$ Delegation")
    c = canvas(720, 400, "Definition 16.2: who computes which part of f(n) = g(n) + h(n)")
    for x, col, head, l1, l2 in ((40, SERIES[2], "AI system computes g(n)", "evidence synthesis, outcome prediction,",
                                  "drug interactions, diagnostic patterns"),
                                 (390, SERIES[0], "Human clinician computes h(n)", "boundary penalties, trust, the moral",
                                  "estimate of the cost that remains")):
        box(c, x, 58, 290, 92, BOX, col, rx=6, sw=1.5)
        c.text(x + 145, 86, head, 13, "middle", INK, "600")
        c.text(x + 145, 110, l1, 11, "middle", INK2)
        c.text(x + 145, 127, l2, 11, "middle", INK2)
    c.text(360, 112, "+", 22, "middle", INK, "600")
    for k in range(1, 10):
        x = 40 + 72 * (k - 1)
        col = SERIES[2] if k in ai else SERIES[0]
        box(c, x, 196, 64, 58, BOX, col, rx=6, sw=1.5)
        box(c, x + 1, 197, 62, 6, col, col, rx=3)
        c.text(x + 32, 226, f"d{k}", 12.5, "middle", INK, "600")
        c.text(x + 32, 243, DIMS[k - 1], 9.5, "middle", INK2)
        if k in ai:
            c.text(x + 32, 276, ai[k], 10.5, "middle", INK2)
    c.line(112, 266, 608, 266, SERIES[0], 1.5)
    c.line(112, 260, 112, 266, SERIES[0], 1.5)
    c.line(608, 260, 608, 266, SERIES[0], 1.5)
    c.text(360, 284, "the human clinician assesses d2 to d8", 10.5, "middle", INK2)
    box(c, 90, 310, 540, 36, BOX, BORDER, rx=6)
    c.text(360, 333, "Any action that crosses a moral boundary must be authorized by a human.", 12, "middle", INK, "600")
    c.text(16, 386, "Schematic of Definition 16.2: a proposal of the chapter.", 10.5, "start", INK3, italic=True)
    c.save(p)


def fig_16_2():
    rows = [("White", 2.8, 1.00), ("Black", 6.1, 2.18), ("Hispanic", 4.3, 1.54), ("Elderly (>70)", 8.4, 3.00)]
    assert all(round(v / 2.8, 2) == d for _, v, d in rows)
    p = reg(P6 + "ch16_ai_clinical.md", "16.2",
            "The illustrative audit of Section 16.8. The triage system and all of its numbers are hypothetical. Left: the "
            "single figure a scalar evaluation would report, an AUC of 0.89 for clinical accuracy. Right: the Bond Index "
            "the scenario assigns to four populations under the same system, with the ratio to the reference group above "
            "each bar. In the scenario the population over 70 bears three times the manifold cost of the reference "
            "group, which the accuracy figure does not show.",
            "## Chapter Summary")
    c = canvas(720, 400, "Illustrative audit: one accuracy score, an uneven Bond Index")
    c.text(40, 66, "d1 clinical accuracy", 11.5, "start", INK, "600")
    box(c, 40, 82, 200, 110, BOX, BORDER, rx=6)
    c.text(140, 136, "AUC 0.89", 24, "middle", INK, "600")
    c.text(140, 164, "validation cohort (hypothetical)", 10.5, "middle", INK2)
    c.text(40, 222, "d9 epistemic quality:", 11, "start", INK2)
    c.text(40, 239, "no uncertainty is communicated", 11, "start", INK2)
    c.text(330, 66, "d3 justice: Bond Index by population", 11.5, "start", INK, "600")
    ax = Axes(c, 330, 90, 350, 220, (0, 4), (0, 10), [], [0, 2, 4, 6, 8, 10], "", "Bond Index BI(AI, S)")
    for i, (name, v, d) in enumerate(rows):
        xc = ax.X(i + 0.5)
        c.rect(xc - 12, ax.Y(v), 24, ax.Y(0) - ax.Y(v), CRITICAL if d == 3.0 else SERIES[0], title=f"{name} {v}")
        c.text(xc, ax.Y(v) - 19, f"{v:.1f}", 11, "middle", INK)
        c.text(xc, ax.Y(v) - 6, f"ratio {d:.2f}", 9.5, "middle", INK2)
        c.text(xc, ax.y0 + ax.h + 18, name, 10.5, "middle", INK2)
    box(c, 40, 354, 640, 32, BOX, BORDER, rx=6)
    c.text(360, 374, "Hypothetical system, illustrative values (Section 16.8). Nothing here is measured.", 11.5, "middle",
           INK, "600")
    c.save(p)


# ------------------------------------------------------------------ chapter 17
def fig_17_1():
    za, zb = 1.959964, 0.841621          # two-sided alpha 0.05, power 0.80
    need = lambda r: ((za + zb) / math.atanh(r)) ** 2 + 3
    assert abs(math.ceil(need(0.3)) - 84) <= 1      # the chapter prints 84 (exact test); Fisher z gives 85
    assert math.ceil(need(0.4)) == 47
    per_group = 2 * ((za + zb) / 0.5) ** 2
    assert abs(math.ceil(per_group) + 1 - 64) <= 1  # chapter: 64 per group for d = 0.5
    p = reg(P6 + "ch17_measuring_metric.md", "17.1",
            "The sample sizes Section 17.4 prints for its correlation tests, on the curve they come from. The horizontal "
            "axis is the correlation a study assumes; the vertical axis is the number of participants needed to detect it "
            "with 80 percent power at a two-sided significance level of 0.05. The curve is the standard Fisher "
            "approximation; it gives 47 at 0.4, as the chapter prints, and 85 at 0.3 where the chapter prints 84. A "
            "smaller assumed effect needs many more participants. These are planning figures: no study has been run.",
            "### Total Research Program Scope")
    c = canvas(720, 400, "Participants the planned correlation tests need, by assumed effect")
    ax = Axes(c, 80, 58, 540, 258, (0.15, 0.6), (0, 360), [0.2, 0.3, 0.4, 0.5, 0.6], [0, 100, 200, 300],
              "assumed correlation |r|", "participants required")
    rs = [0.15 + 0.45 * i / 120 for i in range(121)]
    c.polyline([(ax.X(r), ax.Y(need(r))) for r in rs], SERIES[0], 2.2)
    for r, n, lab in ((0.3, 84, "r = 0.3: n = 84 (Prediction 1)"), (0.4, 47, "|r| = 0.4: n = 47 (Predictions 3 and 4)")):
        c.dot(ax.X(r), ax.Y(n), CRITICAL, 5.5, title=lab)
        c.text(ax.X(r) + 12, ax.Y(n) - 12, lab, 11.5, "start", INK)
    c.text(16, 374, "Curve: Fisher z approximation, two-sided α = 0.05, power 80%. Marked values are the chapter's.",
           10.5, "start", INK3, italic=True)
    c.text(16, 390, "Planning figures for studies that have not been run.", 10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 18
def fig_18_1():
    ehr = {1, 2, 3, 4, 6, 8}
    cells = [(i, j) for i in range(1, 10) for j in range(1, i + 1)]
    inside = [cc for cc in cells if cc[0] in ehr and cc[1] in ehr]
    assert len(cells) == 45 and len(inside) == 21 and len(cells) - len(inside) == 24
    marked = {(6, 4), (7, 2)}
    p = reg(P6 + "ch18_open_questions.md", "18.1",
            "The 45 distinct entries of the nine-by-nine covariance matrix, one cell for each pair of dimensions and each "
            "diagonal entry. Section 18.1 proposes to estimate the six-by-six submatrix of the dimensions that electronic "
            "health records capture, which has 21 entries, and to use proxy instruments for the remaining 24, each of "
            "which involves trust, dignity or epistemic status. The two outlined cells are the entries Question 1 names "
            "as likely to differ between medical cultures. None of the 45 has been estimated.",
            "## 18.2 What Is the Conservation Law for Clinical Reasoning?")
    c = canvas(720, 400, "The 45 entries of Σ: 21 among EHR dimensions, 24 that need proxies")
    x0, y0, s = 112, 66, 31
    for i, j in cells:
        x, y = x0 + s * (j - 1), y0 + s * (i - 1)
        col = SERIES[0] if (i, j) in inside else SERIES[1]
        box(c, x + 1.5, y + 1.5, s - 3, s - 3, col, col, opacity=0.85, rx=3)
        if (i, j) in marked:
            box(c, x - 1, y - 1, s + 2, s + 2, "none", INK, rx=4, sw=2.2)
    for k in range(1, 10):
        proxy = k not in ehr
        c.text(x0 - 10, y0 + s * (k - 1) + s / 2 + 4, f"d{k}", 11.5, "end", INK if proxy else INK2, "600" if proxy else "normal")
        c.text(x0 + s * (k - 1) + s / 2, y0 + 9 * s + 17, f"d{k}", 11.5, "middle", INK if proxy else INK2,
               "600" if proxy else "normal")
    c.text(x0, y0 + 9 * s + 38, "bold: d5 trust, d7 dignity, d9 epistemic (not in EHR data)", 10.5, "start", INK2)
    tx = 430
    box(c, tx, 86, 12, 12, SERIES[0], SERIES[0], rx=3)
    c.text(tx + 20, 96, "both dimensions in EHR data: 21", 11.5, "start", INK)
    c.text(tx + 20, 113, "d1, d2, d3, d4, d6, d8", 10.5, "start", INK2)
    box(c, tx, 140, 12, 12, SERIES[1], SERIES[1], rx=3)
    c.text(tx + 20, 150, "involves d5, d7 or d9: 24", 11.5, "start", INK)
    c.text(tx + 20, 167, "proxy instruments needed", 10.5, "start", INK2)
    box(c, tx, 194, 12, 12, "none", INK, rx=3, sw=2)
    c.text(tx + 20, 204, "Σ46 and Σ27: named as likely", 11.5, "start", INK)
    c.text(tx + 20, 221, "to vary across cultures (Question 1)", 10.5, "start", INK2)
    c.text(tx, 262, "21 + 24 = 45", 12.5, "start", INK, "600")
    c.text(tx, 284, "None has been estimated.", 12.5, "start", INK, "600")
    c.save(p)
