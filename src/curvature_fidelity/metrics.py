import numpy as np


def softening_slope(f_ref, f_pred):
    """Least-squares slope of predicted vs reference values through the origin.
    <1 means systematic softening."""
    f_ref, f_pred = np.asarray(f_ref), np.asarray(f_pred)
    return float(f_ref @ f_pred / (f_ref @ f_ref))


def frequency_mape(f_ref, f_pred):
    f_ref, f_pred = np.asarray(f_ref), np.asarray(f_pred)
    return float(np.mean(np.abs(f_pred - f_ref) / np.abs(f_ref)))
