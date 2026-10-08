---
name: softening-correction
description: Дешёвая коррекция кривизны ППЭ (fine-tuning на одной точке и калибровка по Гессиану) и оформление бенчмарка curvature-fidelity.
---
# Коррекция и бенчмарк

1. Метод А (база): fine-tuning на одной дополнительной точке по Deng et al. Метод Б: калибровка по Гессиану на нескольких точках.
2. Сравни масштаб смягчения и ошибку частот до и после, на отложенных материалах и молекулах.
3. Бенчмарк: src/curvature_fidelity/benchmark.py — одна функция оценки и один формат таблиц для кристаллов и молекул; README с протоколом запуска.
4. Формат таблиц: system, model, domain, functional, ref_value, pred_value, softening_scale, freq_mape.
5. Тексты разделов Methods и Experiments в paper/main.tex; результаты только из реальных прогонов, иначе \TBD{}.
6. Каждый результат воспроизводится одной командой из scripts/.
