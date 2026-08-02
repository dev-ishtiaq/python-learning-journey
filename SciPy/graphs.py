import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix


arr = np.array([[0, 0, 1], 
                [2, 0, 1], 
                [0, 0, 3]])

newarr = csr_matrix(arr)

print(connected_components(newarr))


# -----------Dijkstra---------------

arr2 = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])
newarr2 = csr_matrix(arr2)
print(dijkstra(newarr2, return_predecessors=True, indices=0))
