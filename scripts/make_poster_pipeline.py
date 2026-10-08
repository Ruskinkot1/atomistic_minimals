"""Poster figures: the problem and the planned end-to-end pipeline (a plan, not results).
Run: python scripts/make_poster_pipeline.py -> docs/poster/pipeline.*, problem.*
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = os.path.join(os.path.dirname(__file__), "..", "docs", "poster")
os.makedirs(OUT, exist_ok=True)
DARK, ACC, BLUE, GREY, BG, LIGHT = "#14213D", "#B94A1B", "#1F5FA8", "#6A7179", "#F6F4EE", "#FFFFFF"
plt.rcParams.update({"font.family": "DejaVu Sans", "text.color": DARK})


def save(fig, name):
    for ext in ("png", "svg"):
        fig.savefig(os.path.join(OUT, f"{name}.{ext}"), dpi=200, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)


def box(ax, x, y, w, h, title, body, color=DARK):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.12",
                                fc=LIGHT, ec=color, lw=2.5))
    ax.text(x + w / 2, y + h - 0.28, title, ha="center", va="top", fontsize=15, fontweight="bold", color=color)
    ax.text(x + w / 2, y + h - 0.85, body, ha="center", va="top", fontsize=12, color=GREY, linespacing=1.4)


def arrow(ax, x1, y1, x2, y2, color=DARK):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=22, lw=2.5, color=color))


# ---- Pipeline ----
fig, ax = plt.subplots(figsize=(16, 7.2), facecolor=BG)
ax.set_xlim(0, 16); ax.set_ylim(0, 7.2); ax.axis("off")
ax.text(0.2, 6.9, "Планируемый пайплайн проекта", fontsize=22, fontweight="bold", va="top")
w, h = 3.3, 2.3
box(ax, 0.2, 3.9, w, h, "1. Данные", "Кристаллы: 50–100 с DFT-\nфононами. Молекулы: ~100\nс DFT-гессианами", BLUE)
box(ax, 4.2, 3.9, w, h, "2. Модели", "M3GNet, CHGNet,\nMACE-MP-0, MACE-OFF\n(только инференс)", BLUE)
box(ax, 8.2, 3.9, w, h, "3. Кривизна", "Гессиан по силам →\nчастоты колебаний,\nсравнение с DFT", BLUE)
box(ax, 12.2, 3.9, w, h, "4. Метрики", "Масштаб смягчения s,\nошибка частот", BLUE)
for x in (3.55, 7.55, 11.55):
    arrow(ax, x, 5.05, x + 0.62, 5.05, BLUE)
box(ax, 4.2, 0.5, w, h, "5. Неопределённость", "Ансамбль и латентное\nрасстояние: ловят ли\nсмягчение, а не ошибку?", ACC)
box(ax, 8.2, 0.5, w, h, "6. Коррекция", "Fine-tuning на 1 точке\nпротив калибровки\nпо гессиану", ACC)
box(ax, 12.2, 0.5, w, h, "7. Бенчмарк", "Единый протокол\ncurvature-fidelity,\nкод, таблицы, данные", DARK)
arrow(ax, 13.85, 3.85, 13.85, 2.85, DARK)
arrow(ax, 13.2, 3.85, 6.0, 2.85, ACC)
arrow(ax, 12.5, 3.85, 9.9, 2.85, ACC)
arrow(ax, 11.55, 1.65, 12.2 - 0.0, 1.65, ACC)
arrow(ax, 7.55, 1.65, 8.2, 1.65, ACC)
ax.text(0.2, 1.65, "Всё считается\nлокально,\nна ноутбуке", fontsize=15, fontweight="bold", color=ACC, va="center")
ax.text(0.2, 0.05, "План, а не результат: эксперименты ещё не запущены.", fontsize=11, color=GREY)
save(fig, "pipeline")

# ---- Problem ----
fig, axs = plt.subplots(1, 3, figsize=(16, 5.2), facecolor=BG)
x = np.linspace(-0.6, 0.6, 300)
dft = 12 * x**2 * (1 + 0.6 * x**2)
ax = axs[0]
ax.plot(x, dft, color=DARK, lw=3.5, label="DFT"); ax.plot(x, 0.7 * dft, color=ACC, lw=3.5, label="Модель")
ax.fill_between(x, 0.7 * dft, dft, color=ACC, alpha=0.12)
ax.set_title("1. Поверхность «мягче» DFT", loc="left", fontweight="bold", fontsize=15)
ax.set_xlabel("Смещение атомов"); ax.set_ylabel("Энергия"); ax.legend(frameon=False)
ax = axs[1]
ax.axis("off")
ax.set_title("2. Следствия", loc="left", fontweight="bold", fontsize=15)
for i, t in enumerate(["Частоты колебаний занижены", "Динамика слишком «мягкая»", "Барьеры и фононы неточны"]):
    ax.text(0.02, 0.8 - i * 0.26, "•  " + t, fontsize=15, transform=ax.transAxes)
ax = axs[2]
ax.axis("off")
ax.set_title("3. Открытый вопрос", loc="left", fontweight="bold", fontsize=15)
ax.text(0.02, 0.78, "Видит ли это\nнеопределённость модели?", fontsize=17, fontweight="bold", color=ACC, transform=ax.transAxes, va="top")
ax.text(0.02, 0.38, "Если нет, низкая неопределённость\nне гарантирует верной кривизны.", fontsize=13, color=GREY, transform=ax.transAxes, va="top")
for a in (axs[0],):
    a.spines[["top", "right"]].set_visible(False)
fig.text(0.01, -0.02, "Схема на синтетических данных, не результат эксперимента.", fontsize=11, color=GREY)
save(fig, "problem")
print("ok")
