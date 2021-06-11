import numpy as np
from convert_deg_rad import *

def pythagorean_ab(other,c):
    """ Returns leg value of a right triangle. """
    return np.sqrt(c**2 - other**2)


def pythagorean_c(a, b):
    """ Returns hypotenuse of a right triangle."""
    return np.sqrt(a**2 + b**2)


def euler(k, mag=1, is_rad=True):
    """ Returns Euler notation"""
    if not is_rad:
        k = deg_2_rad(k)
    return mag*np.exp(1j*k)
