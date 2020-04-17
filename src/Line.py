from Point import *

import math
import sys

epsilon = sys.float_info.epsilon
lines = []

class Line:
    '''
    Using Slope Point Form with 2 Points
    y = m * x + c
    m = slope
    c = constant
    '''
    
    count = 0
    
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
        elif not numerator:
            return 0
        else:
            return numerator / denominator
    
    def calcConst(self):
        '''
        c = y - m * x
        '''
        if self.slope is None:
            return self.point1.x
        else:
            return self.point1.y - self.slope * self.point1.x
    
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        self.slope = self.calcSlope()
        self.constant = self.calcConst()
        Line.count += 1
        
    def satisfy(self, point):
        if self.slope is None:
            return self.constant - point.x
        elif self.slope == 0:
            return self.constant - point.y
        else:
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
        
    def debug(self):
        print(
            'Point1.x :', round(self.point1.x, 5),
            'Point1.y :', round(self.point1.y, 5),
            'Point2.x :', round(self.point2.x, 5),
            'Point2.y :', round(self.point2.y, 5),
            'Slope :', round(self.slope, 5),
            'Constant :', round(self.constant, 5)
        )
        


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
            print(
                'Converged at Satisfaction Factor',
                satisfactionFactor,
                'and Angle Factor',
                angleFactor,
                'in Iteration', i
            )
            break
    else:
        print('Did not converge to expected values of SF and AF')
        print(
            'Expected SF', 0,
            'Limitized SF', satisfactionFactor,
            'Error', 0 - satisfactionFactor
        )
        print(
            'Expected AF', 90,
            'Limitized AF', angleFactor,
            'Error', 90 - angleFactor
        )
