import numpy as np
from scipy.sparse import csr_matrix

# arr = np.array([0,0,1,2,0,1,0,0,3,0])
# print(csr_matrix(arr))


arr = np.array([[0, 0, 1], [2, 0, 1], [0, 0, 3]])
# print(csr_matrix(arr))

# print(csr_matrix(arr).count_nonzero())


m= csr_matrix(arr)
m.eliminate_zeros()
print(m)

