import sys
sys.path.append('..')

from manimlib.imports import *
from csvUtils.reader import *

class Shapes(GraphScene):

    X, Y = readPoints(13)
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
    
    def connectPoints(self, X, Y):
        return VMobject().set_points_as_corners([
            *[self.coords_to_point(x, y)
            for x, y in zip(X, Y)]
        ])
    
    def construct(self):
        self.setup_axes(animate=True)
        a, k, p = readSpiral()
        self.play(ShowCreation(
            ParametricFunction(
                lambda t : np.array([
                    a * pow(p, t / np.pi) * np.cos(t),
                    a * pow(p, t / np.pi) * np.sin(t),
                    0
                ]),
                color = RED,
                t_min = -25,
                t_max = 10
            )
        ))
        for i, j in zip(Shapes.X, Shapes.Y):
            self.add(
                Dot(self.coords_to_point(
                    i, j
                ))
            )
            self.wait()
        self.play(ShowCreation(
            self.connectPoints(Shapes.X, Shapes.Y)
        ))
        self.play(ShowCreation(
            self.connectPoints(Shapes.X[::2], Shapes.Y[::2])
        ))
        self.play(ShowCreation(
            self.connectPoints(Shapes.X[1::2], Shapes.Y[1::2])
        ))
        self.wait(5)
        
