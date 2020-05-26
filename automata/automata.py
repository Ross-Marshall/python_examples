import numpy as np
import Automata_methods as AM
import time

grid, LD_results = AM.initialize_grids()
print(grid)

for i in range(100):
    for index, x in np.ndenumerate(grid):
       neighbors = AM.sum_neighbors(grid, index[0], index[1])
       ld = AM.live_or_die(neighbors, x)
       LD_results.itemset(index, ld)
    grid = grid + LD_results
    print(grid)
    time.sleep(1)
    i += 1
