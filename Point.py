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