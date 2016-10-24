##The easiest way I've found to think of this problem is like a graph theory
##  problem.
##First, we re-write the problem slightly - we look at a set of pairs (a_0, a_1)
##  and pick one from each pair. What we want is the minimal such sum so that
##  every number we pick is distinct.
##This is equivalent to the problem as to find the maxmial height, we add up all
##  of the side lengths and just subtract this from that.
##Now, formulate our new problem as a graph theory one - create a graph whose
##  vertices are the numbers that appear as a side length, with a and b sharing
##  an edge if block (a,b) exists. We wish to label the edges with a number on
##  one of the two vertices it's connected to so that no two edges share the
##  same number
##There is a slight issue that is easily dealt with - if we have blocks of the
##  form (a, a) or two blocks of the form (a, b), then just add a or a+b to the
##  total and ignore those blocks from now on.
##Now, look at the connected components of the graph. If it contains a cycle,
##  then we're done - this forces the sum to be the sum of all the vertices
##  in that component. Otherwise, it's a tree - then the sum here is the sum of
##  all the vertices minus the value of the largest vertex that is a leaf.
##
##This gives an algorithm as follows:
##    1) Create the graph as above
##    2) Identify connected components
##    3) In each connected component, determine if acyclic (to do this, just
##            compare the number of edges to the number of vertices)
##    4) Determine the sum for each connected component as above
##    5) Sum all of these values
##    6) Subtract that total from the sum of all lengths on the blocks that
##        we began with - this is the result.
