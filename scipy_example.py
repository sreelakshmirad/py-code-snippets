
# 1. scipy.cluster Vector
# 2. scipy.constants	Physical and mathematical constants
# 3. scipy.integrate	Integration 
# 4. scipy.interpolate	Interpolation
# 5. scipy.linalg	Linear algebra 
# 6. scipy.ndimage	n-dimensional image package
# 7. scipy.optimize	Optimization
# 8. scipy.signal	Signal processing
# 9. scipy.sparse	Sparse matrices

# Constants

# 1.pi pi
# 2.golden Golden Ratio
# 3.c Speed of Light
# 4.h Planck constant
# 5.G Gravitational constant

from scipy import constants
print("sciPy - pi = %.16f"%constants.pi)


# Determinant of a matrix

# 1 2
# 3 4

# 1 2 4
# 2 4 6
# 6 7 8
# from scipy import linalg
# import numpy as np
# A = np.array([[1,2,3],[4,5,6],[7,8,8]])
# det = linalg.det(A)
# print(det)


# Interpolation

import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
x = np.linspace(0, 5)
y = np.sin(x**2/3+4)

print (x,y)
plt.plot(x, y)
plt.show()