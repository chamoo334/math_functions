import numpy as np
import sympy as sym


def make_matrix(some_list):
    return np.matrix(some_list)


def get_rows_cols(some_matrix):
    if type(some_matrix).__module__ != np.__name__:
        return False
    return some_matrix.shape


def matrix_mult(mat_a, mat_b):
    if get_rows_cols(mat_a)[1] != get_rows_cols(mat_b)[0]:
        return False
    return mat_a@mat_b


def transpose_mat(some_matrix):
    if type(some_matrix).__module__ != np.__name__:
        return False
    return some_matrix.T


def square_sym_matrix(some_matrix):
    if type(some_matrix).__module__ != np.__name__:
        return False
    return matrix_mult(some_matrix, transpose_mat(some_matrix))

def identity_matrix(int_a):
    if type(int_a) != int:
        return False
    return np.identity(int_a)


def zeros_matrix(some_tuple):
    if type(some_tuple) != tuple:
        return False
    return np.zeros(some_tuple)


def diag_matrix(some_list):
    if type(some_list) != list or len(some_list != 0):
        return False
    return np.diag(some_list)

def diag_to_vec(some_diag):
    return np.diagonal(some_diag)


def triangular_matrix(some_matrix, u_or_l, kth=None):
    if kth is None:
        if u_or_l == 'upper':
            return np.triu(some_matrix)
        return np.tril(some_matrix)

    if u_or_l == 'lower':
        return np.tril(some_matrix, kth)
    
    return np.triu(some_matrix, kth)


def matrix_pseudoinverse(some_matrix):
    return np.linalg.pinv(some_matrix)


def matrix_inverse(some_matrix):
    #TODO: check for full rank and square
    if type(some_matrix).__module__ != np.__name__:
        return False
    return np.linalg.inv(some_matrix)


m = 5
test = np.random.randint(-m, m+1, (m, m))
test[:,0] = test[:,1]