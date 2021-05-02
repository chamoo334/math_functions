import sympy as sym
#TODO: create a game of some sort for testing factoring of polynomials

x,y = sym.symbols('x,y')

poly = x**2 + 4*x + 3
print(sym.factor(poly))

expr = 2*x**3*3*y - 2*x**2*y + 6*x**2
print(sym.factor(expr))