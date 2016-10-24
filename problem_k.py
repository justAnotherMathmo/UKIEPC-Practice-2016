##This one's actually pretty simple.
##It's pretty clear that the closest point has to come when one dog changes
##  direction - so follow the time and look at each vertex along both paths in
##  the order they're hit (n.b. this isn't just alternating one from each path -
##  the dogs walk at a constant pace, but the lengths between vertices aren't
##  necessarily the same for both paths, so it's possible to have eg 10 vertices
##  on one path before we hit the next vertex on the other path).
##At each vertex in the method above, calculate the distance between the dogs
##When one dog reaches their kennel (the last vertex), stop counting.
##Take the minimum of the distances inferred above
