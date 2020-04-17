from Solver import *

import math

points = []

class Point:

    count = 0
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        Point.count += 1
        
    def distance(self, point):
        return math.sqrt(
            pow(self.x - point.x, 2) + pow(self.y - point.y, 2)
        )
        
    def debug(self):
        print(
            'X :', self.x,
            'Y :', self.y
        )
        
def makePoints(n):
    for i in range(1, n + 1):
        m = i % 4
        if m == 1:
            p = Point(points[i - 1].x - f(i + 1), points[i - 1].y)
        elif m == 2:
            p = Point(points[i - 1].x, points[i - 1].y - f(i + 1))
        elif m == 3:
            p = Point(points[i - 1].x + f(i + 1), points[i - 1].y)
        else:
            p = Point(points[i - 1].x, points[i - 1].y + f(i + 1))
        points.append(p)
