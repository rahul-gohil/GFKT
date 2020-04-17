import math
import sys

from shapes.point  import points
from shapes.line   import Line
from solver        import f


epsilon = sys.float_info.epsilon
pi = math.pi

def calc_a(p):
    x = pow(p, -1 * math.atan(math.sqrt(p)) / pi)
    y = (p * pow(f(1), 2) + pow(f(0), 2)) * (1 + p)
    z = pow(p, 3) * math.sqrt(5)
    return math.sqrt(y / z) * x
    
def angle(n, slope):
    s = math.atan(slope)
    m = (n // 4) * 2 * pi
    if n % 4 == 0:
        return m + s
    elif n % 4 == 1 or n % 4 == 2:
        return m + pi + s
    else:
        return m + 2 * pi + s

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
        
            
def limitizeLogSpiral(center, n):
    spiral = Spiral()
    I0 = center
    for i in range(2, n):
        r1 = points[i].distance(I0)
        r2 = points[i + 1].distance(I0)
        theta1 = angle(i, Line(I0, points[i]).slope)
        theta2 = angle(i + 1, Line(I0, points[i + 1]).slope)
        k = math.log(r1 / r2) / (theta1 - theta2)
        a = r1 * math.exp(-1 * k * theta1)
        if spiral.a - a < epsilon and spiral.k - k < epsilon:
            print(
                'Converged at "a"', a,
                'and', '"k"', k,
                'in Iteration', i
            )
            break
    else:
        print('Did not converge at expected values of "a" and "k"')
        print(
            'Expected "a"', spiral.a,
            'Limitized "a"', a,
            'Error', spiral.a - a
        )
        print(
            'Expected "k"', spiral.k,
            'Limitized "k"', k,
            'Error', spiral.k - k
        )
