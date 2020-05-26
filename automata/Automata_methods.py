import numpy as np

def initialize_grids():
   grid_dim = (3, 3)
   grid = np.mat('0,1,0;0,1,0;0,1,0')
   live_or_die_results = np.zeros(grid_dim, dtype=int)
   return grid, live_or_die_results

def live_or_die(population, x):
   if (population < 2 or population > 3) and x == 1:
      ld = -1
   elif population == 3 and x == 0:
      ld = 1
   else:
      ld = 0
   return ld

def sum_neighbors(A, i, j)->object:
   rows, columns = A.shape
   r0, r1 = max(0, i-1), min(rows-1, i+1)
   c0, c1 = max(0, j-1), min(columns-1, j+1)
   rs = list({r0, i, r1})
   cs = [[c] for c in list({c0, j, c1})]
   return A[rs, cs].sum() - A[i, j]


