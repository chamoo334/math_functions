import numpy as np
import math


def lin_space(lower, upper, total):
    """ Returns list of linearly spaced values """
    return np.linspace(lower, upper, total).tolist()


def log_space(lower, upper, total):
    """ Returns list log-spaced values """
    a = np.log10(lower)
    b = np.log10(upper)
    return np.logspace(a, b, total).tolist()


def get_log(value):
    """ """
    if type(value) == list:
        return np.log(p.array(value))
    
    return np.log(value)


def log_w_base(value, base):
    """ """
    if type(value) == list:
        return np.log(np.array(value)) / np.log(base)
    
    return math.log(value, base)

    