import sympy as sym


def get_func_limit(str_func, lim_point, val=None):
    """ Receives function as a string and lim_point and val as lists.
    lim_point and val order must correlate with each other and overall order
    should be that in which user wants to take the limits."""
    expr = sym.sympify(str_func)

    if val is not None and type(val) != list:
        val = sym.symbols(val)
        return sym.limit(expr, val, lim_point)

    elif val is None:
        all_sym = list(expr.free_symbols)
    
    else:
        all_sym = [sym.symbols(each) for each in val]

    sol = expr.limit(all_sym[0], lim_point[0])
    for i in range(1, len(all_sym)):
        sol = sol.limit(all_sym[i], lim_point[i])

    return sol
