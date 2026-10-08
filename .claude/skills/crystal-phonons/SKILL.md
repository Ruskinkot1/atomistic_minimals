---
name: crystal-phonons
description: Расчёт фононных частот универсальными MLIP на кристаллах и сравнение с DFT; считает масштаб смягчения и ошибку частот.
---
# Кристаллы: фононы

1. Установи в виртуальное окружение: ase, phonopy, mace-torch, chgnet, matgl.
2. Данные: 50-100 материалов из фононной базы Togo/MDR (PBE), малые ячейки (до 10 атомов в примитивной), частые элементы. Скачай phonopy_params.yaml.xz для каждого. Проверь лицензию записи.
3. Для M3GNet, CHGNet, MACE-MP-0: релаксируй структуру, посчитай силовые константы конечными смещениями (phonopy, те же суперъячейка и шаг, что в эталоне), получи частоты.
4. Метрики из src/curvature_fidelity/metrics.py: softening_slope(f_ref, f_pred) и frequency_mape. Мнимые и близкие к нулю моды (кроме акустических на Γ) убери перед сравнением.
5. Выход: results/crystals.csv с колонками system, model, domain, functional, ref_value, pred_value, softening_scale, freq_mape и scripts/run_crystals.py, воспроизводимый одной командой.
6. Данные в data/, в git не коммить.
