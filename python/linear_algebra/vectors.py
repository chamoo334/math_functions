import numpy as np
import sympy as sym


def create_row_vec(r_vec_list):
    """ """
    return np.array(r_vec_list)


def create_col_vec(c_vec_list):
    """ """
    c_vec_list = [[x] for x in c_vec_list]
    return np.array(c_vec_list)


def get_vec_magnitude(vec_a):
    """ """
    if type(vec_a).__module__ != np.__name__:
        return False
    return np.linalg.norm(vec_a)


def dot_product(vec_a, vec_b):
    """ """
    return np.dot(vec_a, vec_b)


def outer_product(vec_a, vec_b):
    """ """
    return np.outer(vec_a, vec_b)


def transpose_vec(some_vec):
    if type(some_vec).__module__ != np.__name__:
        return False
    return np.transpose(some_vec)


test1 = create_row_vec([10, 20, 3])
test2 = create_row_vec([5, 15, 3])

dp = dot_product(test1, test2)
print(dp)
print(get_vec_magnitude(test1))