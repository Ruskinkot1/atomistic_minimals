"""Poster figure for the crystal part: lattice + phonon dispersion DFT vs softened model.
SYNTHETIC schematic, NOT a result. Run: python scripts/make_poster_crystals.py -> docs/poster/crystals.*
"""
import os, itertools
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.join(os.path.dirname(__file__), "..", "docs", "poster")
os.makedirs(OUT, exist_ok=True)
DARK, ACC, BLUE, GREY, BG = "#14213D", "#B94A1B", "#1F5FA8", "#6A7179", "#F6F4EE"
plt.rcParams.update({"font.family": "DejaVu Sans", "text.color": DARK,
                     "axes.edgecolor": DARK, "axes.labelcolor": DARK,
                     "xtick.color": DARK, "ytick.color": DARK})

fig = plt.figure(figsize=(16, 6.4), facecolor=BG)

# --- left: rock-salt-like 2x2x2 lattice ---
ax = fig.add_subplot(1, 2, 1, projection="3d", facecolor=BG)
pts = np.array(list(itertools.product(range(3), repeat=3)), float)
par = pts.sum(1) % 2
for p, c, s in [(0, BLUE, 700), (1, ACC, 400)]:
    q = pts[par == p]
    ax.scatter(q[:, 0], q[:, 1], q[:, 2], s=s, color=c, edgecolor=DARK, linewidth=1.2, depthshade=True)
for a, b in itertools.combinations(range(len(pts)), 2):
    if np.isclose(np.linalg.norm(pts[a] - pts[b]), 1.0):
        ax.plot(*zip(pts[a], pts[b]), color=GREY, lw=1.6, alpha=0.7, zorder=0)
ax.set_axis_off()
ax.view_init(elev=22, azim=-58)
ax.set_title("Кристалл: объект проверки\n(схематичная решётка)", fontsize=16, fontweight="bold", loc="left")

# --- right: phonon dispersion ---
ax2 = fig.add_subplot(1, 2, 2, facecolor="white")
k = np.linspace(0, 1, 200)
def branches(scale):
    ac = scale * 3.2 * np.abs(np.sin(np.pi * k))
    ac2 = scale * 2.2 * np.abs(np.sin(np.pi * k))
    op = scale * (6.0 - 0.9 * np.sin(np.pi * k) ** 2)
    op2 = scale * (5.1 - 0.5 * np.sin(np.pi * k) ** 2)
    return [ac, ac2, op2, op]
for i, (d, m) in enumerate(zip(branches(1.0), branches(0.88))):
    ax2.plot(k, d, color=DARK, lw=3, label="DFT (эталон)" if i == 0 else None)
    ax2.plot(k, m, color=ACC, lw=3, ls="--", label="Универсальная модель (s < 1)" if i == 0 else None)
ax2.fill_between(k, branches(0.88)[3], branches(1.0)[3], color=ACC, alpha=0.12)
for x in (0, 0.5, 1):
    ax2.axvline(x, color="#DAD6CA", lw=1)
ax2.set_xticks([0, 0.5, 1]); ax2.set_xticklabels(["Γ", "X", "M"], fontsize=15)
ax2.set_ylabel("Частота, ТГц", fontsize=15)
ax2.legend(frameon=False, fontsize=14, loc="lower center")
for sp in ("top", "right"):
    ax2.spines[sp].set_visible(False)
ax2.set_title("Фононы: модель «мягче» DFT\n(ожидаемая картина, Г1)", fontsize=16, fontweight="bold", loc="left")
fig.text(0.01, -0.01, "Схема на синтетических данных, не результат эксперимента. Планируем 50–100 материалов с эталонными DFT-фононами.",
         fontsize=11, color=GREY)
for ext in ("png", "svg"):
    fig.savefig(os.path.join(OUT, f"crystals.{ext}"), dpi=200, bbox_inches="tight", facecolor=BG)
print("ok")
