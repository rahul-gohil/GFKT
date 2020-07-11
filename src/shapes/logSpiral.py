import solver
import math
import sys

from shapes.point import points, Point
from shapes.line  import Line


a = solver.a
f = solver.f
epsilon = 1e-2
pi = math.pi

def calc_t(p):
    x = 1 / pow(p, (2 * math.atan(pow(p, 1 / a))) / (a * pi))
    y = 1 / pow(1 + pow(p, 2 / a), 0.5)
    z = pow((p * (p * pow(f(1), a) + pow(f(0), a))) / pow(5, 0.5), 1 / a)
    return  z * y * x
    
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
        self.t = calc_t(self.p)
        self.k = math.log(pow(self.p, 2 / solver.a)) / pi

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
        t = r1 * math.exp(-1 * k * theta1)
        if abs(t - spiral.t) < epsilon and abs(k - spiral.k) < epsilon:
            return (
                "logarithmicSpiral",
                {
                    "comment" : "Converged at expected values",
                    "t" : t,
                    "k" : k,
                    "iteration" : i
                }
            )
    else:
        return (
            "logarithmicSpiral",
            {
                "comment" : "Did not converge at expected values of 't' and 'k'",
                "t" : {
                    "expected" : spiral.t,
                    "limitized" : t,
                    "error" : spiral.t - t,
                },
                "k" : {
                    "expected" : spiral.k,
                    "limitized" : k,
                    "error" : spiral.k - k
                }
            }
        )
