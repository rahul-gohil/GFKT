import math
import sys

from shapes.prettyPrint import prettify
from shapes.point       import *

epsilon = sys.float_info.epsilon
lines = []

class Line:
    '''
    Using Slope Point Form with 2 Points
    y = m * x + c
    m = slope
    c = constant
    '''

    def calcSlope(self):
        '''
        slope = (y2 - y1) / (x2 - x1)
        Denomiator - 0 -> (Not Defined)
        Numerator - 0 -> (0)
        '''
        numerator = self.point2.y - self.point1.y
        denominator = self.point2.x - self.point1.x
        if not denominator:
            return None
        if not numerator:
            return 0
        return numerator / denominator

    def calcConst(self):
        '''
        c = y - m * x
        '''
        if self.slope is None:
            return self.point1.x
        return self.point1.y - self.slope * self.point1.x

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        self.slope = self.calcSlope()
        self.constant = self.calcConst()

    def satisfy(self, point):
        if self.slope is None:
            return self.constant - point.x
        if self.slope == 0:
            return self.constant - point.y
        factor = point.y - self.slope * point.x - self.constant
        if factor < epsilon or factor > 1 / epsilon:
            '''
            factor tends to zero, and then tends to -inf or +inf
            due to floating point precision error
            '''
            return 0
        return factor

    def angle(self, line):
        assert self.slope != line.slope, 'Both Lines are Parallel. Cannot Calculate Angle'
        assert self.slope is not None or line.slope is not None, 'Slope cannot be None'
        '''
        Assume that both slopes exist.
        theta = arctan(|(m2 - m1) / (1 + m1 * m2)|)
        '''
        m1 = line.slope
        m2 = self.slope
        if abs(1 + m1 * m2) < epsilon:
            '''
            if the denominator becomes less than epsilon, it treats it as zero
            and gives division by zero error
            '''
            return 90.0
        theta = math.degrees(math.atan(
            abs((m2 - m1) / (1 + (m1 * m2))
            )
        ))
        return theta

    def length(self):
        return self.point2.distance(self.point1)

    def debug(self, n):
        print(prettify({
            n : {
                "Point1" : {
                    "X" : self.point1.x,
                    "Y" : self.point1.y
                },
                "Point2" : {
                    "X" : self.point2.x,
                    "Y" : self.point2.y
                },
                "Slope" : self.slope,
                "Constant" : self.constant
            }
        }))



def makeLines(n):
    for i in range(2, n):
        lines.append(Line(lines[i - 2].point2, points[i]))

def limitizeLine():
    '''
    Satisfy P(n + 2) to L(n) -> Satisfaction Factor (Should Tend to Zero)
    Get Angle between L(n) & L(n + 1) -> Angle Factor (Should Tend to 90)
    '''
    for i in range(500):
        satisfactionFactor = lines[i].satisfy(points[i + 2])
        angleFactor = lines[i].angle(lines[i + 1])
        if satisfactionFactor == 0 and angleFactor == 90:
            converged = {
                "lines" : {
                    "comment" : "Converged at expected values",
                    "Angle Factor" : angleFactor,
                    "Satisfaction Factor" : satisfactionFactor
                }
            }
            print(prettify(converged))
            break
    else:
        errors = {
            "lines" : {
                "comment" : "Did not converge at expected values",
                "Satisfaction Factor" : {
                    "expected" : 0,
                    "limitized" : satisfactionFactor,
                    "error" : satisfactionFactor
                },
                "Angle Factor" : {
                    "expected" : 90,
                    "limitized" : angleFactor,
                    "error" : 90 - angleFactor
                }
            }
        }
        print(prettify(errors))
