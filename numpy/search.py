import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 4, 4])

# x = np.where( arr == 4)

# print(x)

# ---Find the indexes where the values are odd:---
# arr = np.array([10, 14, 93, 41, 8, 7])

# x = np.where(arr%2 == 1)
# print(x)

# --------Find the indexes where the values are even:----
# arr = np.array([10, 14, 93, 41, 8, 7])

# x = np.where(arr%2 == 0)
# print(x)

# -----Search Sorted-------
# arr = np.array([0, 4, 9, 6, 8, 7])

# x = np.searchsorted(arr, 4)
# print(x)

# ----------Search From the Right Side-------
arr = np.array([1,2,3,4,5])

x = np.searchsorted(arr, 4, side="right")
print(x)
