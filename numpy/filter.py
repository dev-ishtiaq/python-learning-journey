import numpy as np

# arr = np.array([1,4,7,9])

# x = [True, False, False, True]

# newarr = arr[x]

# print(newarr)

# ---------Creating the Filter Array ------

# arr = np.array([2,5,7,8,10,11])

# filter_arr = []

# for element in arr:
#     if element > 7:
#         filter_arr.append(True)
#     else:
#         filter_arr.append(False)

# newarr = arr[filter_arr]
# print(filter_arr)
# print(newarr)


# a = np.array([5,4,8,6,9,10,12])

# fa = []

# for x in a:
#     if x % 2 == 0:
#         fa.append(True)
#     else:
#         fa.append(False)

# na = a[fa]

# print(fa)
# print(na)


# ---directly filter ---------

arr = np.array([14,51,78,61,21,24])


newarr = arr > 15

filter_arr = (arr[newarr])
print(arr)
print(filter_arr)