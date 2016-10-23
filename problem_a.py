## We solve this problem by passing over the grid each time and checking to see
##   if consecutive squares have the same number - if they do we update the grid

import sys

from copy import deepcopy
from itertools import count

## Set up:

strokes = []
is_firstinput = 1
for line in sys.stdin:
    if is_firstinput:
        n, m, q = map(int, line.split(' '))
        is_firstinput = 0
    else:
        strokes += [tuple(map(int, line.split(' ')))]

grid = {i:{j:1 for j in range(m)} for i in range(n)}
iterator = count(start=1, step=1)
for x in range(n):
    for y in range(m):
        if grid[x][y] != 0:
            grid[x][y] = next(iterator)
            
## Helper Functions:

def stroke_items(x1, y1, x2, y2):
    """Generate the stroke iterator"""
    stroked = []
    if x1==x2:
        for y_index in range(y1-1, y2):
            stroked += [(x1-1, y_index)]
    else:  ## y1=y2 here
        for x_index in range(x1-1, x2):
            stroked += [(x_index, y1-1)]
    return stroked


def neighbours(grid, x, y):
    """Checks the valid neighbours of (x,y)"""
    possible = [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]
    for pos in possible[:]:
        if -1 in pos or pos[0] >= n or pos[1] >= m:
            possible.remove(pos)
        elif grid[pos[0]][pos[1]] == 0:
            possible.remove(pos)
    return possible


def compute_regions(base_grid, x1, y1, x2, y2):
    """Computes the number of regions by setting each unstroked square
to be the next integer, then setting neighbours value to be the smallest one
Result is the number of distinct integers in grid"""
    updated = 1
    while updated == 1:
        updated = 0
        for x in range(n):
            for y in range(m):
                local_val = base_grid[x][y]
                if local_val == 0:
                    continue
                neigh_vals = tuple(
                    base_grid[a][b] for a, b in neighbours(base_grid, x, y)
                    )
                if neigh_vals == ():
                    continue
                else:
                    neigh_val = max(neigh_vals)
                if local_val < neigh_val:
                    base_grid[x][y] = neigh_val
                    updated = 1
            
    distinct_vals = set()
    for x in grid:
        distinct_vals = distinct_vals.union(base_grid[x].values())
    return len(distinct_vals) - 1

## Actual work

for x1, y1, x2, y2 in strokes:
    ## Updating stroke information
    stroke = stroke_items(x1, y1, x2, y2)
    for x, y in stroke:
        grid[x][y] = 0
    
    for x in range(max(x1-2, 0), min(x2+1, n)): 
        for y in range(max(y1-2, 0), min(y2+1, m)):
            if grid[x][y] != 0:
                grid[x][y] = next(iterator)
            
    print(compute_regions(grid, x1, y1, x2, y2))
