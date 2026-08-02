# from scipy.optimize import root
# import numpy as np

from scipy.optimize import minimize



def eqn(x):
    return x**2 + x + 2
mymin = minimize(eqn, 0, method='BFGS')
print(mymin)


# def eqn(x):
#   return x + np.cos(x)

# myroot = root(eqn, 0)

# print(myroot.x)