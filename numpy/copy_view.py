import numpy as np

# arr = np.array([1,3,5,6,7])

# cp = arr.copy()
# arr[0] = 42

# print(arr)
# print(cp)

arr = np.array([1, 2, 3, 4 ,5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)