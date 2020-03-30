class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    # in order to sort points based on their x coordinate
    def __lt__(self, other):
      return self.x < other.x

    def __repr__(self):
      return '(%d,%d)' %(self.x,self.y)

    def __str__(self):
      return '(%d,%d)' %(self.x,self.y)
