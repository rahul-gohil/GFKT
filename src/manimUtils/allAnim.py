import sys
sys.path.append('..')

from src.csvUtils.reader import *
from manimlib.imports    import *

n = int(sys.argv[2])
X, Y = readPoints(n)
a, k, p = readSpiral()
_min = min(min(X), min(Y))
_max = max(max(X), max(Y))
CONFIG = {
        "x_min": 1.2 * _min,
        "x_max": 1.2 * _max,
        "y_min": 1.2 * _min,
        "y_max": 1.2 * _max,
        "x_tick_frequency": 10,
        "y_tick_frequency": 10,
        "graph_origin": ORIGIN,
        "function_color": WHITE,
        "axes_color": BLUE,
    }
    
def parametricFunction(Object):

    return ParametricFunction(
                lambda t : Object.coords_to_point(
                    *np.array([
                        a * pow(p, t / np.pi) * np.cos(t),
                        a * pow(p, t / np.pi) * np.sin(t),
                        0
                    ])[:-1]
                ),
                color = RED,
                t_min = -4 * np.pi,
                t_max = ((n // 4) * 2 + (n % 4)) * np.pi
            )

def connectPoints(Object, X, Y):

    return VMobject().set_points_as_corners(
            list(map(
                lambda x, y : Object.coords_to_point(x, y),
                X, Y
            ))
        )
        
def plotPoints(Object):
    
    for i, j in zip(X, Y):
        Object.add(
            Dot(Object.coords_to_point(
                i, j
            ))
        )
        Object.wait(0.75)
    
class Shapes1(GraphScene):

    CONFIG = CONFIG
    
    def construct(self):
        
        self.setup_axes(animate=True)
        plotPoints(self)
        
        self.play(ShowCreation(
            connectPoints(self, X, Y),
            run_time = 4
        ))
        self.play(ShowCreation(
            connectPoints(self, X[::2], Y[::2]),
            run_time = 2
        ))
        self.play(ShowCreation(
            connectPoints(self, X[1::2], Y[1::2]),
            run_time = 2
        ))
        self.play(ShowCreation(
            parametricFunction(self),
            run_time = 6
        ))
        self.wait(5)
        
class Shapes2(GraphScene):

    CONFIG = CONFIG
    
    def construct(self):
        
        self.setup_axes(animate=True)
        plotPoints(self)

        self.play(ShowCreation(
            parametricFunction(self),
            run_time = 6
        ))
        self.wait(5)
        
class Shapes3(GraphScene):

    CONFIG = CONFIG
    
    def construct(self):
        
        self.setup_axes(animate=True)
        plotPoints(self)
            
        self.play(ShowCreation(
            connectPoints(self, X, Y),
            run_time = 4
        ))
        self.play(ShowCreation(
            parametricFunction(self),
            run_time = 6
        ))
        self.wait(5)
