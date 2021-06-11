import sympy as sym


def get_primes(num_a, as_list = False):
    """ Returns num_a prime factors as dictionary or list """

    if as_list:
        return sym.factor_list(num_a)
    return sym.factorint(num_a)


