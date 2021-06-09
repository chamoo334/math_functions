import sympy as sym
import numpy as np

def add_polys(poly_a, poly_b):
    """ """
    a = sym.sympify(poly_a)
    b = sym.sympify(poly_b)
    return a+b


def mul_polys(poly_a, poly_b, expand=True):
    """ """
    a = sym.sympify(poly_a)
    b = sym.sympify(poly_b)

    if expand:
        return sym.expand(a*b)
    return a*b


def div_polys(poly_a, poly_b):
    """ Returns the quotient and remainder of polynomial division"""
    a = sym.sympify(poly_a)
    b = sym.sympify(poly_b)
    return sym.div(a, b, domain ='QQ')


def factor_poly(equation_str):
    """ Returns the factored form """
    return sym.factor(sym.sympify(equation_str))


def get_discrim(poly_a):
    """ Return the discriminant of a polynomial """
    return sym.discriminant(poly_a)


def get_poly_roots(poly_a):
    """ Returns a list that contains the roots of a polynomial """
    expr = sym.sympify(poly_a).as_poly()
    return np.roots(expr.all_coeffs()).tolist()


# sym.pprint(factor_poly("-2*x**2 + 7*x -6"))

