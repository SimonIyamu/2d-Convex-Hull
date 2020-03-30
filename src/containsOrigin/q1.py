from Point import Point

# Compute the area the triangle that is formed by the 3 input points
def area(a, b, c): 
    return abs((a.x * (b.y - c.y) + b.x * (c.y - a.y)  
                + c.x * (a.y - b.y)) / 2.0) 

# Return true if the given points form a triangle
def isTriangle(a, b, c):
    return (area(a, b, c)>0)

# Return true if the triangle formed by the given points
# contains the axis origin (0,0). 
def containsOrigin(a, b, c): 
    origin = Point(0,0)

    # Calculate area of triangles abc, obc, oac, oab
    abc = area(a, b, c) 
    obc = area(origin, b , c) 
    oac = area(origin, a, c) 
    oab = area(origin, a, b) 
      
    # If sum abc == obc, oac, oab
    # Then o is inside the triangle
    return (abc == obc + oac + oab)

# Lets make 3 points so that p2==p3
p1 = Point(0,2)
p2 = Point(2,0)
p3 = Point(2,0)
print('Points: p1(%d,%d) p2(%d,%d) p3(%d,%d)' %(p1.x,p1.y,p2.x,p2.y,p3.x,p3.y,))
print('The points form a triangle: ' + str(isTriangle(p1,p2,p3)))
print('---')

# Lets make 3 points so that p3 is in line p1p2
p1 = Point(0,2)
p2 = Point(2,0)
p3 = Point(1,1)
print('Points: p1(%d,%d) p2(%d,%d) p3(%d,%d)' %(p1.x,p1.y,p2.x,p2.y,p3.x,p3.y,))
print('The points form a triangle: ' + str(isTriangle(p1,p2,p3)))
print('---')

# This triangle contains the axis origin
p1 = Point(0,2)
p2 = Point(2,0)
p3 = Point(-1,-1)
print('Points: p1(%d,%d) p2(%d,%d) p3(%d,%d)' %(p1.x,p1.y,p2.x,p2.y,p3.x,p3.y,))
print('The points form a triangle: ' + str(isTriangle(p1,p2,p3)))
print('The points contain the axis origin: ' + str(containsOrigin(p1,p2,p3)))
print('---')

# This triangle does not contains the axis origin
p1 = Point(0,2)
p2 = Point(2,0)
p3 = Point(1,0)
print('Points: p1(%d,%d) p2(%d,%d) p3(%d,%d)' %(p1.x,p1.y,p2.x,p2.y,p3.x,p3.y,))
print('The points form a triangle: ' + str(isTriangle(p1,p2,p3)))
print('The points contain the axis origin: ' + str(containsOrigin(p1,p2,p3)))