import sympy as sym
#TODO: determine whether dynamic piecewise is possible


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


# def piece_wise(str_sym_list, str_func_list, str_domain_list):
#     all_pieces = [sym.sympify(each) for each in str_func_list]
#     all_domains = [sym.sympify(each) for each in str_domain_list]
#     test = "sym.Piecewise((sym.sympify("+str_func_list[0]+"),sym.sympify("+str_domain_list[0]+"))"
#     for i in range(1, len(str_func_list)):
#         test += ",(sym.sympify("+str_func_list[i]+"),sym.sympify("+str_domain_list[i]+"))"
#     test += ")"
#     print(test)
#     test2 = exec(test)
#     # print(test)


# list_a = ['0', '-2*x', 'x**3/10']
# list_b = ['x<0', '(x>=0) & (x<10)','x>=10']
# list_c = ['x']
# piece_wise(list_c, list_a, list_b)
