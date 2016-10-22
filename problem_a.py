## We solve this problem by passing over the grid each time and checking to see
##   if consecutive squares have the same number - if they do we update the grid

import sys

from copy import deepcopy

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
iterator = (i for i in range(1, m*n+1))
for x in range(n):
    for y in range(m):
        if grid[x][y] != 0:
            grid[x][y] = next(iterator)

## Helper Functions:

def stroke_items(x1, y1, x2, y2):
    """Generate the stroke iterator"""
    stroked = []
    if x1==x2:
        for y_index in range(y1-1,y2):
            stroked += [(x1, y_index)]
    else:  ## y1=y2 here
        for x_index in range(x1-1,x2):
            stroked += [(x_index, y1)]
    return stroked


def neighbours(grid, x, y):
    """Checks the valid neighbours of (x,y)"""
    possible = [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]
    for pos in possible[:]:
        if -1 in pos or pos[0] >= m or pos[1] >= n:
            possible.remove(pos)
        elif grid[pos[1]][pos[0]] == 0:
            possible.remove(pos)
    return possible


def compute_regions(base_grid):
    """Computes the number of regions by setting each unstroked square
to be the next integer, then setting neighbours value to be the smallest one
Result is the number of distinct integers in grid"""
    new_grid = deepcopy(base_grid)
    updated = 1
    while updated == 1:
        updated = 0
        for x in range(n):
            for y in range(m):
                local_val = new_grid[x][y]
                neigh_vals = tuple(
                    new_grid[b][a] for a, b in neighbours(new_grid, x, y)
                    )
                if neigh_vals == ():
                    continue
                else:
                    neigh_val = min(neigh_vals)
                if local_val > neigh_val:
                    new_grid[x][y] = neigh_val
                    updated = 1
            
    distinct_vals = set()
    for x in grid:
        distinct_vals = distinct_vals.union(grid[x].values())
    return len(distinct_vals) - 1


for stroke_start_end in strokes:
    ## Updating stroke information
    stroke = stroke_items(*stroke_start_end)
    for x, y in stroke:
        grid[x][y] = 0

    print(compute_regions(grid))
