import matplotlib.pyplot as plt
import numpy as np

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __lt__(self, other):
      return self.x < other.x

    def __repr__(self):
      return '(%.1f,%.1f)' %(self.x,self.y)

    def __str__(self):
      return '(%.1f,%.1f)' %(self.x,self.y)

allPoints = list()

'''
allPoints.append(Point(3,9))
allPoints.append(Point(3.5,6))
allPoints.append(Point(6,1))
allPoints.append(Point(9,0))
'''
#np.random.seed(1921)
for i in range(20):
  allPoints.append(Point(100*np.random.rand(),100*np.random.rand()))
print(allPoints)

# Returns true if point p is left of the line ab
def isLeftOf(p,a,b):
  return (np.sign((b.x - a.x) * (p.y - a.y) - (b.y - a.y) * (p.x - a.x)) >= 0 )

# Returns true if point p is right of the line ab
def isRightOf(p,a,b):
  return (np.sign((b.x - a.x) * (p.y - a.y) - (b.y - a.y) * (p.x - a.x)) <= 0 )

# Sort points by their x-coordinate
allPoints = sorted(allPoints)
print(allPoints)

# Start with a trivial hull(a triangle of the first points)
hullPoints = allPoints[:3]
print('----')
print(hullPoints)

# Store edges in CCW (counter-clock wise) order 
hullEdge = {}
if (isRightOf(hullPoints[0], hullPoints[1], hullPoints[2])):
  hullEdge= {
      hullPoints[0]: {'prev': hullPoints[1], 'next': hullPoints[2]},
      hullPoints[1]: {'prev': hullPoints[2], 'next': hullPoints[0]},
      hullPoints[2]: {'prev': hullPoints[0], 'next': hullPoints[1]}
  }
else:
  hullEdge= {
      hullPoints[0]: {'prev': hullPoints[2], 'next': hullPoints[1]},
      hullPoints[2]: {'prev': hullPoints[1], 'next': hullPoints[0]},
      hullPoints[1]: {'prev': hullPoints[0], 'next': hullPoints[2]}
  }

print('----')
print(hullEdge)

# Returns true if the point p is upper tangent of point p.
# q1 is the previous point of p and q2 is the next point, when moving CCW in a polygon
def isUpperTangent(p, q, q1, q2):
  return isLeftOf(p,q,q2) and isRightOf(p,q1,q)

def isLowerTangent(p, q, q1, q2):
  return isRightOf(p,q,q2) and isLeftOf(p,q1,q)

n = len(allPoints)

for i in range(3,n):
  pi = allPoints[i]
  print('Adding point pi=%s'%(pi))
  # j is the rightmost index of the convex hull
  j = len(hullPoints) - 1

  # Look for upper tangent point
  u = j
  upperTangent = hullPoints[u]
  while(not isUpperTangent(pi, upperTangent, hullEdge[upperTangent]['prev'], hullEdge[upperTangent]['next'])):
    #print('- its not %s'%(upperTangent)) 
    u -= 1
    upperTangent = hullPoints[u]
  print('  Upper tangent point: %s' %(upperTangent))

  # Look for lower tangent point
  lowerTangent = hullEdge[upperTangent]['prev']
  while(not isLowerTangent(pi, lowerTangent, hullEdge[lowerTangent]['prev'], hullEdge[lowerTangent]['next'])):
      print('     Removing %s' %(lowerTangent))
      temp = lowerTangent
      lowerTangent = hullEdge[lowerTangent]['prev']
      hullEdge.pop(temp,None)
      hullPoints.remove(temp)
  print('  Lower tangent point: %s' %(lowerTangent))

  # Update convex hull by adding the new point
  hullPoints.append(pi)
  hullEdge[pi] = {'prev': lowerTangent, 'next': upperTangent}
  hullEdge[lowerTangent]['next'] = pi
  hullEdge[upperTangent]['prev'] = pi
  print('')

print('Generating plot...')
pointsArray = list()
for point in allPoints:
  pointsArray.append([point.x, point.y])
pointsArray = np.array(pointsArray)

hullEdge[pi] = {'prev': lowerTangent, 'next': upperTangent}
hull = list()
point = hullPoints[0]
for i in range(len(hullPoints)):
  hull.append([point.x, point.y])
  point = hullEdge[point]['next']
hull.append(hull[0])
hull = np.array(hull)

plt.plot(pointsArray[:,0], pointsArray[:,1], 'o')
plt.plot(hull[:,0], hull[:,1], 'r--')

plt.show()
print('Plot was generated')