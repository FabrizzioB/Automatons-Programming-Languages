def areNeighbours(a, b, delta):
    return any(True for (x,_,y) in delta if {x,y} == {a,b})
