import math

from shapes.prettyPrint import prettify
from solver             import f

points = []

class Point:


    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, point):
        return math.sqrt(
            pow(self.x - point.x, 2) + pow(self.y - point.y, 2)
        )

    def debug(self, n):
        print(prettify({
            n : {
                "X" : self.x,
                "Y" : self.y
            }
        }))

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

def shiftPoints(x1, y1):
    for i in range(len(points)):
        points[i].x = points[i].x - x1
        points[i].y = points[i].y - y1
