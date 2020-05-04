import math
import sys

from shapes.point import points, Point
from shapes.line  import Line
from solver       import f


epsilon = 1e-10
pi = math.pi

def calc_a(p):
    x = pow(p, -1 * math.atan(math.sqrt(p)) / pi)
    y = (p * pow(f(1), 2) + pow(f(0), 2))
    z = p * math.sqrt(5)
    return math.sqrt(y / z) * x

def angle(n, slope):
    '''Calculates theta(n)'''
    s = math.atan(slope)
    m = (n // 4) * 2 * pi
    if n % 4 == 0:
        return m + s
    if n % 4 == 1 or n % 4 == 2:
        return m + s + pi
    if n % 4 == 3:
        return m + s + 2 * pi

class Spiral:
    '''
    Logarithmic Spiral has polar equation of the form
    r = a * e^(k * theta), where a and k are constant
    Parametric form : x = rcos(theta), y = rsin(theta)
    '''

    def __init__(self):
        self.p = (1 + math.sqrt(5)) / 2
        self.a = calc_a(self.p)
        self.k = math.log(self.p) / pi

def r(n):
    return pow(
        pow(points[n].x, 2)
        + pow(points[n].y, 2),
        0.5
    ).real

def sine(n):
    return math.sin(
        angle(n, Line(Point(0, 0), points[n]).slope)
    )

def cosine(n):
    return math.cos(
        angle(n, Line(Point(0, 0), points[n]).slope)
    )

def limitizeLogSpiral(center, n):
    '''Calculates limit of spiral constants "a" and "k"'''
    spiral = Spiral()
    I0 = center
    for i in range(n):
        r1 = points[i].distance(I0)
        r2 = points[i + 1].distance(I0)
        theta1 = angle(i, Line(I0, points[i]).slope)
        theta2 = angle(i + 1, Line(I0, points[i + 1]).slope)
        k = math.log(r1 / r2) / (theta1 - theta2)
        a = r1 * math.exp(-1 * k * theta1)
        if abs(a - spiral.a) < epsilon and abs(k - spiral.k) < epsilon:
            return (
                "logarithmicSpiral",
                {
                    "comment" : "Converged at expected values",
                    "a" : a,
                    "k" : k,
                    "iteration" : i
                }
            )
    else:
        return (
            "logarithmicSpiral",
            {
                "comment" : "Did not converge at expected values of 'a' and 'k'",
                "a" : {
                    "expected" : spiral.a,
                    "limitized" : a,
                    "error" : spiral.a - a,
                },
                "k" : {
                    "expected" : spiral.k,
                    "limitized" : k,
                    "error" : spiral.k - k
                }
            }
        )
