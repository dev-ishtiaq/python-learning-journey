import numpy as np

# arr1 = ([[1,3,5],[5,7,8]])
# arr2 = ([[4,6,7],[1,3,5]])

# arr = np.concatenate((arr1, arr2), axis=1)
# arrs = np.stack((arr1, arr2), axis=1)
# print(arr)
# print(arrs)


# arr1 = np.array([1, 2, 3])

# arr2 = np.array([4, 5, 6])

# arr = np.hstack((arr1, arr2))
# print(arr)

# arr1 = np.array([1, 2, 3])

# arr2 = np.array([4, 5, 6])

# arr = np.vstack((arr1, arr2))
# print(arr)


arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))
print(arr)