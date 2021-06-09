import sympy as sym

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
    expr = sym.sympify(equation_str)
    return sym.factor(expr)


def get_discrim(poly_a):
    """ Return the discriminant of a polynomial """
    return sym.discriminant(poly_a)


# sym.pprint(factor_poly("-2*x**2 + 7*x -6"))

