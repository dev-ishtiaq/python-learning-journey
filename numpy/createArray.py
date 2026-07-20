# -----nd array--------
import numpy as np
# arr = np.array([1,4,6,7,8])

# print(arr)
# print(type(arr))


# ------tuple-------
# arr = np.array((1,4,6,7,8))

# print(arr)
# print(type(arr))


# --------Check Number of Dimensions----------
# a = np.array(50)
# b = np.array([1,4,6,7,8])
# c = np.array([[1,5,8,9,4], [2,5,7,9,6]])
# print(a.ndim)
# print(b.ndim)
# print(c.ndim)


# ---------Higher Dimensional Arrays---------


array = np.array([1,2,3,4,5], ndmin=4)

print(array)
print("number of dimension: ",array.ndim)
