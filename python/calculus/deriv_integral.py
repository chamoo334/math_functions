import sympy as sym


def deriv(some_func, deriv_to=None):
    """ Returns derivatie of some_func. Partial derivative requires 
    deriv_to as variable."""
    if type(some_func) == str:
        return sym.diff(sym.sympify(some_func))

    if deriv_to is not None:
        if type(deriv_to) == str:
            deriv_to = sym.symbol(deriv_to)
        return sym.diff(some_func, deriv_to)
    
    return sym.diff(some_func)


def integr(some_func, some_bounds = None):
    """ Integrates some_func. Definite integral create by some_bounds =
    (variable, lower, upper)."""
    if type(some_func) == str:
        some_func = sym.sympify(some_func)

    if some_bounds is not None:
        if type(some_bounds[0]) == str:
            some_bounds = (sym.symbols(some_bounds[0]), some_bounds[1], some_bounds[2])
        return sym.integrate(some_func, some_bounds)

    return sym.integrate(some_func)

