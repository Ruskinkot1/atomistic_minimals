import numpy as np


def numerical_hessian(atoms, calc, delta=0.01):
    """Finite-difference Hessian (eV/A^2) from forces; shape (3N, 3N)."""
    atoms = atoms.copy()
    atoms.calc = calc
    n = len(atoms)
    x0 = atoms.get_positions()
    h = np.zeros((3 * n, 3 * n))
    for i in range(n):
        for k in range(3):
            fs = []
            for s in (+1, -1):
                x = x0.copy()
                x[i, k] += s * delta
                atoms.set_positions(x)
                fs.append(atoms.get_forces().ravel())
            h[3 * i + k] = -(fs[0] - fs[1]) / (2 * delta)
    return 0.5 * (h + h.T)


def vibrational_frequencies(atoms, hessian):
    """Frequencies in cm^-1 (imaginary reported as negative)."""
    from ase.units import _e, _amu, _c
    m = np.repeat(atoms.get_masses(), 3)
    dyn = hessian / np.sqrt(np.outer(m, m))
    w2 = np.linalg.eigvalsh(dyn) * _e / (1e-20 * _amu)  # s^-2
    w = np.sign(w2) * np.sqrt(np.abs(w2))
    return w / (2 * np.pi * _c * 100)
