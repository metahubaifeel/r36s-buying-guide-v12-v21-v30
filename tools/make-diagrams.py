#!/usr/bin/env python3
"""Draw docs/03-finish-revision-matrix.png and docs/05-should-you-buy-flowchart.png.

Run from the repository root:  python3 tools/make-diagrams.py

Both images are drawn from literal rectangles, text and the finish data in
FINISHES below. No image model is involved anywhere in this repository. The
FINISHES table is a hand-copy of the shop's own catalogue
(`storefront/src/lib/catalog.ts`): 14 finishes against 3 board revisions.

Every photograph in docs/ is a real photograph of a real unit or of a supplier
sample board, cropped and downscaled only.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")

# (display name, swatch hex, revisions this finish can be ordered on)
FINISHES = [
    ("Transparent Purple", "#795b9f", ["v12", "v21", "v30"]),
    ("Transparent Black", "#55555d", ["v12", "v21", "v30"]),
    ("White", "#eeeeed", ["v12", "v21", "v30"]),
    ("Yellow", "#e9ba40", ["v12", "v21"]),
    ("Transparent Pink", "#d98dab", ["v30"]),
    ("Bright Pink", "#e8aac0", ["v12"]),
    ("Soft Blue", "#54c6ce", ["v12"]),
    ("Solid Purple", "#9276bf", ["v12"]),
    ("Transparent Green", "#55a891", ["v12"]),
    ("Transparent Red", "#b94c58", ["v12"]),
    ("Transparent Lake Blue", "#50a8bb", ["v12"]),
    ("Solid Red", "#c94950", ["v12"]),
    ("Transparent Orange", "#dc8a4c", ["v12"]),
    ("Transparent Blue", "#466dbb", ["v12"]),
]


def box(ax, x, y, w, h, text, fc, fs=10, weight="normal"):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                                boxstyle="round,pad=0.010,rounding_size=0.02",
                                linewidth=1.1, facecolor=fc, edgecolor="#1b1b1b", zorder=2))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs,
            zorder=3, linespacing=1.55, fontweight=weight)


def arrow(ax, x, y1, y2):
    ax.add_patch(FancyArrowPatch((x, y1), (x, y2), arrowstyle="-|>", mutation_scale=13,
                                 linewidth=1.2, color="#4a4a4a", zorder=1))


# ------------------------------------------------- finish x revision matrix
fig, ax = plt.subplots(figsize=(9.6, 9.2), dpi=170)
ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
ax.text(0.035, 0.972, "R36S finishes x board revisions", fontsize=14.5, fontweight="bold")
ax.text(0.035, 0.930,
        "Copied from the shop's own catalogue (storefront/src/lib/catalog.ts): 14 finishes, 3 revisions.\n"
        "A green cell means that finish and that board can be ordered together.",
        fontsize=8.6, color="#3a3a3a", linespacing=1.55)

x0, colw = 0.475, 0.168
for j, (h, a, b) in enumerate([("V12", "13 finishes", "no built-in WiFi"),
                               ("V21", "4 finishes", "WiFi optional"),
                               ("V30", "4 finishes", "WiFi optional")]):
    cx = x0 + j * (colw + 0.018)
    ax.text(cx + colw / 2, 0.878, h, fontsize=12.5, fontweight="bold", ha="center")
    ax.text(cx + colw / 2, 0.852, a, fontsize=7.6, ha="center", color="#3a3a3a")
    ax.text(cx + colw / 2, 0.832, b, fontsize=7.6, ha="center", color="#8a2f2f")

ytop, rh = 0.800, 0.0495
for i, (name, hexv, revs) in enumerate(FINISHES):
    y = ytop - i * rh
    ax.add_patch(Rectangle((0.035, y - 0.034), 0.036, 0.034, facecolor=hexv,
                           edgecolor="#9a9a9a", linewidth=0.8))
    ax.text(0.083, y - 0.017, name, fontsize=9.4, va="center")
    for j, rev in enumerate(["v12", "v21", "v30"]):
        cx = x0 + j * (colw + 0.018)
        ok = rev in revs
        ax.add_patch(Rectangle((cx, y - 0.034), colw, 0.034,
                               facecolor="#dff0d8" if ok else "#f4f4f4",
                               edgecolor="#c4c4c4", linewidth=0.8))
        if ok:
            ax.text(cx + colw / 2, y - 0.017, "available", fontsize=8.4, ha="center",
                    va="center", color="#2f5d2a")
ax.text(0.035, 0.040,
        "A shell colour is not proof of the board inside. The revision is stated in your written quote and printed\n"
        "on the board itself — see the two silkscreen photographs in this repository.",
        fontsize=8.5, color="#3a3a3a", linespacing=1.6)
fig.savefig(os.path.join(DOCS, "03-finish-revision-matrix.png"), bbox_inches="tight",
            facecolor="white")
plt.close(fig)

# ------------------------------------------------- should-you-buy flowchart
fig, ax = plt.subplots(figsize=(11.5, 8.0), dpi=170)
ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
ax.text(0.5, 0.968, "Is an R36S the right handheld for you?", ha="center",
        fontsize=14, fontweight="bold")
ax.text(0.5, 0.932, 'Answer the five questions. One honest "no" is enough to look elsewhere.',
        ha="center", fontsize=9.6, color="#4a4a4a")

qs = [
    ("Do you mainly want 8-bit and 16-bit systems — NES, SNES,\nGB / GBC / GBA, Mega Drive, arcade?",
     "yes - keep going", "no - PSP, N64, DS, Saturn, PS2 and GameCube will disappoint you"),
    ("Are you comfortable with folders, card formats, flashing an\nimage and picking a .dtb for your board?",
     "yes - keep going", "no - buy something sold as a finished appliance"),
    ("Can you live without phone-style standby, and with a full\nshutdown every night?",
     "yes - keep going", "no - it has no true suspend; plan to power it off"),
    ("Is a 3.5-inch 4:3 screen and about 1 GB of RAM enough?\n(our own unit reports 895 MB total)",
     "yes - keep going", "no - a larger Android handheld is the honest answer"),
    ("Are you happy to buy a bare device: no card, no ROMs,\nno charging cable in the box?",
     "yes - a good fit", "no - a bundle seller matches what you actually want"),
]
ytop, bh, pitch = 0.868, 0.098, 0.153
for i, (q, yes, no) in enumerate(qs):
    y = ytop - i * pitch
    box(ax, 0.030, y - bh, 0.485, bh, q, "#eaf2fb", fs=9.8)
    ax.text(0.535, y - 0.030, yes, fontsize=8.5, color="#2f5d2a", va="center")
    ax.text(0.535, y - 0.070, no, fontsize=8.5, color="#8a2f2f", va="center")
    if i < len(qs) - 1:
        arrow(ax, 0.272, y - bh - 0.004, y - pitch + 0.006)
y = ytop - len(qs) * pitch
ax.text(0.5, y - 0.045,
        "The R36S is a cheap, repairable, community-supported 4:3 handheld. It is not a console with a warranty desk,\n"
        "and this shop makes no clone claim and sells no games.",
        ha="center", fontsize=8.7, color="#3a3a3a", linespacing=1.65)
fig.savefig(os.path.join(DOCS, "05-should-you-buy-flowchart.png"), bbox_inches="tight",
            facecolor="white")
plt.close(fig)
print("wrote", DOCS)
