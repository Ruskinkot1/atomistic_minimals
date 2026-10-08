"""Hypothesis schematics for the poster. SYNTHETIC curves: NOT experimental results.
Run: python scripts/make_poster_figures.py  -> docs/poster/*.png, *.svg
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.join(os.path.dirname(__file__), "..", "docs", "poster")
os.makedirs(OUT, exist_ok=True)
DARK, ACC, BLUE, GREY = "#14213D", "#B94A1B", "#1F5FA8", "#8A93A3"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 15,
                     "axes.spines.top": False, "axes.spines.right": False,
                     "axes.edgecolor": DARK, "text.color": DARK,
                     "axes.labelcolor": DARK, "xtick.color": DARK, "ytick.color": DARK})
NOTE = "Схема гипотезы на синтетических данных, не результат эксперимента"


def save(fig, name):
    for ext in ("png", "svg"):
        fig.savefig(os.path.join(OUT, f"{name}.{ext}"), dpi=200, bbox_inches="tight")
    plt.close(fig)


# H1: DFT vs softened model along a bond-stretch coordinate
x = np.linspace(-0.6, 0.6, 300)
dft = 12.0 * x**2 * (1 + 0.6 * x**2)
s = 0.7
model = s * dft
fig, ax = plt.subplots(figsize=(7, 5))
ax.plot(x, dft, color=DARK, lw=3.5, label="DFT (эталон)")
ax.plot(x, model, color=ACC, lw=3.5, label="Универсальная модель (s < 1)")
ax.fill_between(x, model, dft, color=ACC, alpha=0.12)
ax.set_xlabel("Смещение вдоль координаты, Å")
ax.set_ylabel("Энергия, эВ")
ax.legend(frameon=False, loc="upper center")
ax.set_title("Г1: модель занижает кривизну ППЭ", loc="left", fontweight="bold")
fig.text(0.01, -0.09, NOTE, fontsize=11, color=GREY)
save(fig, "h1_pes_softening")

# H2: parity plot, slope < 1 for crystals and molecules
rng = np.random.default_rng(0)
ref = rng.uniform(0.5, 6, 120)
fig, axs = plt.subplots(1, 2, figsize=(11, 5), sharey=True)
for ax, (title, sl, col) in zip(axs, [("Кристаллы: фононные частоты", 0.88, BLUE),
                                      ("Молекулы: колебательные частоты", 0.90, ACC)]):
    pred = sl * ref + rng.normal(0, 0.12, ref.size)
    ax.scatter(ref, pred, s=22, color=col, alpha=0.75)
    ax.plot([0, 6.5], [0, 6.5], color=DARK, lw=2, label="y = x (идеал)")
    ax.plot([0, 6.5], [0, 6.5 * sl], color=col, lw=2.5, ls="--", label=f"наклон s < 1")
    ax.set_title(title, fontsize=14, loc="left", fontweight="bold")
    ax.set_xlabel("DFT")
    ax.legend(frameon=False, loc="upper left")
axs[0].set_ylabel("Модель")
fig.suptitle("Г2: смещение есть и у кристаллов, и у молекул", x=0.01, y=1.05, ha="left",
             fontweight="bold", fontsize=16)
fig.text(0.01, -0.09, NOTE, fontsize=11, color=GREY)
save(fig, "h2_parity_domains")

# H3: uncertainty vs error / vs softening (the central hypothesis)
n = 200
err = rng.uniform(0.1, 1.0, n)
soft = rng.uniform(0.0, 1.0, n)
unc = err + rng.normal(0, 0.08, n)
fig, axs = plt.subplots(1, 2, figsize=(11, 5), sharey=True)
axs[0].scatter(err, unc, s=22, color=BLUE, alpha=0.75)
axs[0].set_xlabel("Абсолютная ошибка")
axs[0].set_title("Неопределённость растёт с ошибкой", fontsize=14, loc="left", fontweight="bold")
axs[1].scatter(soft, unc, s=22, color=ACC, alpha=0.75)
axs[1].set_xlabel("Степень смягчения, −log(s)")
axs[1].set_title("…но не со смягчением (Г3)", fontsize=14, loc="left", fontweight="bold")
axs[0].set_ylabel("Неопределённость")
fig.suptitle("Г3: неопределённость слепа к систематическому смягчению", x=0.01, y=1.05, ha="left",
             fontweight="bold", fontsize=16)
fig.text(0.01, -0.09, NOTE + ". Ожидаемая картина при подтверждении Г3.", fontsize=11, color=GREY)
save(fig, "h3_uncertainty_blind")

# H4: correction
fig, ax = plt.subplots(figsize=(7, 5))
labels = ["Исходная\nмодель", "Fine-tuning\nна 1 точке", "Калибровка\nпо гессиану"]
vals = [0.7, 0.9, 0.95]
bars = ax.bar(labels, vals, color=[GREY, BLUE, ACC], width=0.55)
ax.axhline(1.0, color=DARK, lw=2, ls="--")
ax.text(2.45, 1.015, "s = 1", ha="right", fontsize=13)
ax.set_ylim(0, 1.15)
ax.set_ylabel("Масштаб смягчения s")
ax.set_title("Г4: дешёвая коррекция возвращает s к 1", loc="left", fontweight="bold")
fig.text(0.01, -0.09, NOTE + ". Значения условные.", fontsize=11, color=GREY)
save(fig, "h4_correction")
print("saved to", os.path.abspath(OUT))
