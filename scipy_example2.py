# Inverse of a matrix

# 4 5     1 0
# 3 2     0 1
# from scipy import linalg
# import numpy as np
# two_d_array = np.array([ [4,5], [3,2] ])
# inv = linalg.inv( two_d_array )
# print(inv)



# Plotting a graph
# from matplotlib import pyplot as plt
# import numpy as np 
# fre  = 5 
# fre_samp = 50
# t = np.linspace(0, 2, 2 * fre_samp )
# a = np.sin(fre  * 2 * np.pi * t)
# print(t)
# print(a)
# figure, axis = plt.subplots()
# axis.plot(t, a)
# axis.set_xlabel ('Time (s)')
# axis.set_ylabel ('Signal amplitude')
# plt.show()



# Input/Output
# import numpy as np
# from scipy import io as sio
# array = np.ones((4, 4))
# sio.savemat('example.mat', {'ar': array}) 
# data = sio.loadmat('example.mat')
# print(data['ar'])


# Image processing 
from scipy import misc,ndimage
from matplotlib import pyplot as plt
import numpy as np
panda = misc.face()
print(panda)
# plt.imshow( panda )
# plt.show()


#Flip Down   
# flip_down = np.flipud(panda)
# plt.imshow(flip_down)
# plt.show()

# Rotate
# panda_rotate = ndimage.rotate(panda, 135)
# plt.imshow(panda_rotate)
# plt.show()


# Integration
# from scipy import integrate
# f = lambda x : x**2
# integration = integrate.quad(f, 0 , 1)
# print(integration)


# Combinations
from scipy.special import comb
com = comb(5, 2, exact = False, repetition=True)
print(com)


# Permutations
from scipy.special import perm
per = perm(5, 2, exact = True)
print(per)


# Exponentials
from scipy.special import exp10
exp = exp10([1,10])
print(exp)