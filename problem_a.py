import sys 

## Set up:

strokes = []
is_firstinput = 1
for line in sys.stdin:
    if is_firstinput:
        n, m, q = map(int, line.split(' '))
    else:
        strokes += [tuple(map(int, line.split(' ')))]

grid = {row:[1 for col in range(m)] for j in range(n)}
regions = 1

## Helper Functions:

def stroke_items(x1, y1, x2, y2):
    """Generate the stroke iterator"""
    stroked = []
    if x1==x2:
        for y_index in range(y1-1,y2):
            stroked += [(x1, y_index)]
    else:  ## y1=y2 here
        for x_index in range(x1-1,x2):
            stroked += [(y1, x_index)]
    return stroked 

for x1, y1, x2, y2 in strokes:
    ## Adding stroke information


    

def open_neigh(grid, x, y):
    pass
