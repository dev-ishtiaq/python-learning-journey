import numpy as np
# ----Additon-----------
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

addarr = np.add(arr1, arr2)
print(addarr)

# -------Summation-------
sumarr = np.sum([arr1, arr2])
print(sumarr)


# ------Summation Over an Axis--------
sumarrax = np.sum([arr1, arr2], axis=1)
print(sumarrax)

# -------Cummulative Sum------
customarr = np.cumsum(arr1)
print(customarr)






