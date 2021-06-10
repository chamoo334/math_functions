import numpy as np
from convert_deg_rad import *

def get_sin(val, is_rad=True, bound=True):
    """ Returns sin of radian. Set is_rad boolean to False if using degrees. 
        Set bound boolean to True to remain within unit circle"""
    if not is_rad:
        val = deg_2_rad(val, bound)
    return np.sin(val)


def get_cos(val, is_rad=True, bound=True):
    """ Returns sin of radian. Set is_rad boolean to False if using degrees. 
        Set bound boolean to True to remain within unit circle"""
    if not is_rad:
        val = deg_2_rad(val, bound)
    return np.cos(val)


def get_tan(val, is_rad=True, bound=True):
    """ Returns sin of radian. Set is_rad boolean to False if using degrees. 
        Set bound boolean to True to remain within unit circle"""
    if not is_rad:
        val = deg_2_rad(val, bound)
    return np.tan(val)


def get_arcsin(val, is_rad=True, bound=True):
    """ Returns sin of radian. Set is_rad boolean to False if using degrees. 
        Set bound boolean to True to remain within unit circle"""
    if not is_rad:
        val = deg_2_rad(val, bound)
    return np.arcsin(val)


def get_arccos(val, is_rad=True, bound=True):
    """ Returns sin of radian. Set is_rad boolean to False if using degrees. 
        Set bound boolean to True to remain within unit circle"""
    if not is_rad:
        val = deg_2_rad(val, bound)
    return np.arccos(val)


def get_arctan(val, is_rad=True, bound=True):
    """ Returns sin of radian. Set is_rad boolean to False if using degrees. 
        Set bound boolean to True to remain within unit circle"""
    if not is_rad:
        val = deg_2_rad(val, bound)
    return np.arctan(val)


def get_sinh(val, is_rad=True, bound=True):
    """ Returns sin of radian. Set is_rad boolean to False if using degrees. 
        Set bound boolean to True to remain within unit circle"""
    if not is_rad:
        val = deg_2_rad(val, bound)
    return np.sinh(val)


def get_cosh(val, is_rad=True, bound=True):
    """ Returns sin of radian. Set is_rad boolean to False if using degrees. 
        Set bound boolean to True to remain within unit circle"""
    if not is_rad:
        val = deg_2_rad(val, bound)
    return np.cosh(val)


def get_tanh(val, is_rad=True, bound=True):
    """ Returns sin of radian. Set is_rad boolean to False if using degrees. 
        Set bound boolean to True to remain within unit circle"""
    if not is_rad:
        val = deg_2_rad(val, bound)
    return np.tanh(val)


def get_arcsinh(val, is_rad=True, bound=True):
    """ Returns sin of radian. Set is_rad boolean to False if using degrees. 
        Set bound boolean to True to remain within unit circle"""
    if not is_rad:
        val = deg_2_rad(val, bound)
    return np.sinh(val)


def get_arccosh(val, is_rad=True, bound=True):
    """ Returns sin of radian. Set is_rad boolean to False if using degrees. 
        Set bound boolean to True to remain within unit circle"""
    if not is_rad:
        val = deg_2_rad(val, bound)
    return np.cosh(val)


def get_arctanh(val, is_rad=True, bound=True):
    """ Returns sin of radian. Set is_rad boolean to False if using degrees. 
        Set bound boolean to True to remain within unit circle"""
    if not is_rad:
        val = deg_2_rad(val, bound)
    return np.tanh(val)
