# TODO: print mult_table using LaTex 

import numpy as np
import sympy as sym
from matplotlib import rcParams
rcParams['text.usetex'] = True

num = range(1, int(input("Enter a number to create a multiplication table: "))+1)
mult_table = np.zeros((len(num), len(num)))

for row in num:
    for col in num:
        mult_table[row-1][col-1] = row * col


print(mult_table)
