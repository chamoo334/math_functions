import numpy as np


def arith_seq_list_n(a1, d, n):
    """ """
    return a1 + d*np.arange(0, n)


def arith_seq_n(a1, d, n):
    """ """
    return a1 + (n-1)*d


def geo_seq_list_n(a1, r, n):
    """ """
    return a1 * r**np.arange(0, n)


def geo_seq_n(a1, r, n):
    """ """
    return a1 * r**(n-1)
