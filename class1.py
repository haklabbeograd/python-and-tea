import math

class Point:
    count = 0
    def __init__(self, x, y): #constructor
        self.x = x # data attribute
        self.y = y
        Point.count += 1
    def norm(self):# method
        return math.sqrt(self.x ** 2 + self.y ** 2)
    def __del__(self):
        print 'released memory for', self
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __iter__(self):
        return iter([self.x, self.y])

#print Point.count
#p = Point(1,2)
#print Point.count
