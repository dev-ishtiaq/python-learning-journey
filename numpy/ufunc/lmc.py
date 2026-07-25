import numpy as np

# -------Finding LCM (Lowest Common Multiple)-------
arr = np.array([3, 6, 9])

x = np.lcm.reduce(arr)
print(x)



arr2 = np.arange(1, 11)

x2 = np.lcm.reduce(arr2)

print(x2)