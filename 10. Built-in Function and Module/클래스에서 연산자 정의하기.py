class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)

    def __str__(self):
        return 'Point('+str(self.x)+', '+str(self.y)+')'
