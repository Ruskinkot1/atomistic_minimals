"""Poster figure: example crystal (NaCl) and how it enters a universal MLIP. Schematic.
Run: python scripts/make_poster_crystal_input.py -> docs/poster/crystal_to_model.*
"""
import os, itertools
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle

OUT = os.path.join(os.path.dirname(__file__), "..", "docs", "poster")
os.makedirs(OUT, exist_ok=True)
DARK, ACC, BLUE, GREY, BG = "#14213D", "#B94A1B", "#1F5FA8", "#6A7179", "#F6F4EE"
plt.rcParams.update({"font.family": "DejaVu Sans", "text.color": DARK})

fig = plt.figure(figsize=(18, 6.6), facecolor=BG)
a = 5.64  # NaCl lattice constant, Angstrom

# 1: unit cell (3D)
ax = fig.add_axes([0.0, 0.05, 0.27, 0.8], projection="3d", facecolor=BG)
fcc = [(0,0,0),(.5,.5,0),(.5,0,.5),(0,.5,.5)]
na = [np.array(p) for p in fcc]
cl = [np.array(p) + np.array([.5,0,0]) for p in fcc]
for pts, c, s in [(na, BLUE, 900), (cl, ACC, 500)]:
    for p in pts:
        for sh in itertools.product((0,1), repeat=3):
            q = (p + np.array(sh)) 
            if (q <= 1.0001).all():
                ax.scatter(*(q * a), s=s, color=c, edgecolor=DARK, linewidth=1.2, depthshade=True)
for s_, e_ in itertools.combinations(list(itertools.product((0,1), repeat=3)), 2):
    if sum(abs(np.array(s_) - np.array(e_))) == 1:
        ax.plot(*zip(np.array(s_) * a, np.array(e_) * a), color=DARK, lw=1.8)
ax.set_axis_off(); ax.view_init(elev=20, azim=-60)
fig.text(0.02, 0.9, "1. Кристалл: NaCl", fontsize=18, fontweight="bold")
fig.text(0.02, 0.04, "Кубическая ячейка a = 5.64 Å: 4 Na (синие)\nи 4 Cl (оранжевые); атомы на гранях\nпоказаны и у соседних граней", fontsize=12, color=GREY)

# right-hand schematic area
bx = fig.add_axes([0.27, 0.0, 0.73, 1.0], facecolor=BG)
bx.set_xlim(0, 13.4); bx.set_ylim(0, 6.6); bx.axis("off")

def box(x, y, w, h, title, body, color):
    bx.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.12", fc="white", ec=color, lw=2.5))
    bx.text(x + w/2, y + h - 0.2, title, ha="center", va="top", fontsize=15, fontweight="bold", color=color)
    bx.text(x + w/2, y + h - 0.8, body, ha="center", va="top", fontsize=12, color=GREY, linespacing=1.45)

def arrow(x1, y1, x2, y2, c=DARK):
    bx.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=22, lw=2.5, color=c))

# 2: input tensors
box(0.2, 1.2, 3.2, 4.4, "2. Вход модели",
    "Номера атомов Z:\n[11, 11, …, 17, 17]\n\nКоординаты r (Å)\n\nВекторы ячейки\n(3×3, периодичность)", BLUE)
arrow(3.5, 3.4, 4.1, 3.4)
# 3: graph
gx = fig.add_axes([0.27 + 0.73*4.2/13.4, 0.2, 0.73*3.2/13.4, 0.55], facecolor="white")
gx.set_xlim(-1.4, 1.4); gx.set_ylim(-1.7, 1.4); gx.set_aspect("equal", adjustable="box"); gx.set_xticks([]); gx.set_yticks([])
for sp in gx.spines.values(): sp.set_edgecolor(ACC); sp.set_linewidth(2.5)
pos = {"c": (0, 0)}
ring = [(np.cos(t), np.sin(t)) for t in np.linspace(0, 2*np.pi, 7)[:-1]]
for p in ring:
    gx.plot([0, p[0]], [0, p[1]], color=GREY, lw=2)
gx.add_patch(Circle((0, 0), 1.25, fill=False, ls="--", ec=ACC, lw=1.8))
for p in ring:
    gx.add_patch(Circle(p, 0.14, fc=ACC, ec=DARK, lw=1.2))
gx.add_patch(Circle((0, 0), 0.19, fc=BLUE, ec=DARK, lw=1.4))
gx.text(0, -1.45, "радиус обрезки ≈ 5–6 Å", ha="center", va="center", fontsize=11, color=ACC)
fig.text(0.27 + 0.73*5.8/13.4, 0.87, "3. Граф", fontsize=15, fontweight="bold", color=ACC, ha="center")
fig.text(0.27 + 0.73*5.8/13.4, 0.08, "узел — атом, ребро — соседи\nв пределах радиуса", fontsize=12, color=GREY, ha="center", va="top")
arrow(7.5, 3.4, 8.1, 3.4)
# 4: model
box(8.2, 1.2, 2.6, 4.4, "4. Модель",
    "M3GNet, CHGNet,\nMACE-MP-0:\nпередача сообщений\nмежду соседями\n\nвеса заморожены", DARK)
arrow(10.9, 3.4, 11.5, 3.4)
# 5: outputs
box(11.6, 1.2, 1.7, 4.4, "5. Выход", "Энергия E\n\nСилы F = −∇E\n\nГессиан H = ∂²E\n→ частоты", DARK)
fig.suptitle("Как кристалл заходит в универсальную модель", x=0.01, y=1.03, ha="left", fontsize=22, fontweight="bold")
fig.text(0.01, -0.03, "Схема процесса; значения иллюстративные. Для частот сравниваем Гессиан модели с DFT.", fontsize=11, color=GREY)
for ext in ("png", "svg"):
    fig.savefig(os.path.join(OUT, f"crystal_to_model.{ext}"), dpi=180, bbox_inches="tight", facecolor=BG)
print("ok")
