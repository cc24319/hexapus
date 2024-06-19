import numpy as np
from scipy.optimize import linprog

# EX 1
# minimizar 5x1 + x2
# sujeito a 2x1 + x2 >= 6
# x1 + x2 >= 4
# x1 + 5x2 >= 10
# x1, x2 >= 0

"""
# Setting the inequality constraints matrix

A_ub = np.array([[-2, -1], [-1, -1], [-1, -5]])
# Setting the inequality constraints vector

b_ub = np.array([-6, -4, -10])
# Setting the coefficients of the linear objective function vector

c = np.array([5, 1])
# Solving linear programming problem

res = linprog(c, A_ub = A_ub, b_ub = b_ub,)

print('Optimal value:', round(res.fun, ndigits=2),
      '\nx values:', res.x, 
      '\nNumber of iterations performed:', res.nit,
      '\nStatus:', res.message,)
"""


#EX 2

# maximizar 2x1 − 3x2
# sujeito a x1 + 2x2 ≤ 6
# 2x1 − x2 ≤ 8
# x1, x2 ≥ 0

#transforma em minimizar invertendo o sinal

"""
A_ub = np.array([[1,2], [2, -1]])

b_ub = np.array([[6, 8] ])

c = np.array([[-2, 3]])

x_bounds = [(0, None), (0, None)]

res = linprog(c, A_ub = A_ub, b_ub = b_ub, bounds=x_bounds)

print('Optimal value:', round(res.fun, ndigits=2),
      '\nx values:', res.x, 
      '\nNumber of iterations performed:', res.nit,
      '\nStatus:', res.message,)


"""
# EX 3
# maximizar 15(x1 + 2x2) + 11(x2 − x3)
# sujeito a 3x1 ≥ x1 + x2 + x3
# 0 ≤ xj ≤ 1 j = 1, 2, 3

#transforma em minimizar invertendo o sinal
# 15(x1 + 2x2) + 11(x2 − x3) --> - 15x1 - 41x2 + 11x3
# 3x1 ≥ x1 + x2 + x3 --> 2x1 - x2 -x3 >=0


A_ub = [[-2, -1, -1]]

b_ub = [0]

c = [-15, -41, 11]

x_bounds = [(0, 1), (0, 1), (0, 1)]

res = linprog(c, A_ub = A_ub, b_ub = b_ub, bounds=x_bounds)

print('Optimal value:', round(res.fun, ndigits=2),
      '\nx values:', res.x, 
      '\nNumber of iterations performed:', res.nit,
      '\nStatus:', res.message,)

""" A_eq = [[1, 1, 1, 1]]
b_eq = [400]

A_ub = [[-1, 2, 0, 0], [0, -1, 2, 0], [0, 0, -1, 2]]
b_ub = [0, 0, 0]

# Setting the inequality constraints vector


# Setting the coefficients of the linear objective function vector
c = np.array([0,0, 10, 10])

x_bounds = [(0,None), (0,None),(0,None),(0,None)]

# Solving linear programming problem
res = linprog(c, A_eq = A_eq, b_eq = b_eq, A_ub= A_ub, b_ub=b_ub, bounds=x_bounds)

print('Optimal value:', round(res.fun, ndigits=2),
      '\nx values:', res.x, 
      '\nNumber of iterations performed:', res.nit,
      '\nStatus:', res.message,) """