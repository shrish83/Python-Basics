import numpy as np

##numpy array
np1 = np.array([1,2,3,4])
print(np1)

mat1 = np.array([[1,2],[3,4]])
print(mat1)

#whether 1d array or 2d
print(np1.shape)
print(mat1.shape)

#data type in mat1 and np1
print(np1.dtype)  #elements are integer of 32 bit long

#range
Mat2 = np.arange(0,10,1)  # 1-d array
print(Mat2)

Mat3 = np.limspace(0,10,20) #startpoint = 0, endpoint= 10, noOf elements  = 20
print(Mat3)

Mat4 = np.random.rand(5,5)
Mat5 = np.random.randn(5,5)

## Also try: np.diag, np.zeros, np.ones


