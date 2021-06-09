import math

def comm_denom(int_a, int_b):
    """ Returns the greates common denominator of two integers """
    return math.gcd(int_a, int_b)


print(comm_denom(5, 15))