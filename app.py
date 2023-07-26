import matplotlib.pyplot as plt
import numpy as np
from sympy.abc import n, l, r, Z
from sympy.physics import hydrogen
from sympy.utilities.lambdify import lambdify

R_nl = lambdify((n, l, r), hydrogen.R_nl(n, l, r))

Z = 1
n, l = 3, 0
r = np.linspace(0, 30, 1000)

pdf = R_nl(n, l, r)**2 * (r ** 2)

plt.xlim([0, 30])
plt.ylim([0, 1])
plt.plot(r, pdf)
plt.show()

input()

