import numpy as np

arr = np.array([1, 2, 3, 4])

x = np.prod(arr)
print(x)




arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])


x2 = np.prod([arr1, arr2])
print(x2)


newarr = np.prod([arr1, arr2], axis=1)
print(newarr)



