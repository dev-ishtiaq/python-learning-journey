import numpy as np

arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
a = np.unique(arr)
# print(a)

arr1 = ([2,5,4,7,9,8])
arr2 = ([2,3,5,7,9,10])

# Finding Union
newrr = np.union1d(arr1, arr2)
# print(newrr)

# Finding Intersection
arr3 = ([2,5,4,7,9,8])
arr4 = ([2,3,5,7,9,10])

newarr = np.intersect1d(arr3, arr4)
# print(newarr)


# Finding Difference
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])
newset = np.setdiff1d(set1, set2, assume_unique=True)
print(newset)


set3= np.array([1, 2, 3, 4])
set4= np.array([3, 4, 5, 6])

newset2 = np.setxor1d(set3, set4, assume_unique=True)
print(newset2)

