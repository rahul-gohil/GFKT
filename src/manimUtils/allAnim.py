import sys
sys.path.append('..')

from src.csvUtils.reader import *
from manimlib.imports    import *

class Shapes1(GraphScene):

    points = int(sys.argv[2])
    X, Y = readPoints(points)
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
        return VMobject().set_points_as_corners(
            list(map(
                lambda x, y : self.coords_to_point(x, y),
                X, Y
            ))
        )
    
    def construct(self):
        n = Shapes1.points
        self.setup_axes(animate=True)
        a, k, p = readSpiral()
        for i, j in zip(Shapes1.X, Shapes1.Y):
            self.add(
                Dot(self.coords_to_point(
                    i, j
                ))
            )
            self.wait(0.75)
        self.play(ShowCreation(
            self.connectPoints(Shapes1.X, Shapes1.Y),
            run_time = 4
        ))
        self.play(ShowCreation(
            self.connectPoints(Shapes1.X[::2], Shapes1.Y[::2]),
            run_time = 2
        ))
        self.play(ShowCreation(
            self.connectPoints(Shapes1.X[1::2], Shapes1.Y[1::2]),
            run_time = 2
        ))
        self.play(ShowCreation(
            ParametricFunction(
                lambda t : self.coords_to_point(
                    *np.array([
                        a * pow(p, t / np.pi) * np.cos(t),
                        a * pow(p, t / np.pi) * np.sin(t),
                        0
                    ])[:-1]
                ),
                color = RED,
                t_min = -4 * np.pi,
                t_max = ((n // 4) * 2 + (n % 4)) * np.pi
            ),
            run_time = 6
        ))
        self.wait(5)
        
class Shapes2(GraphScene):

    points = int(sys.argv[2])
    X, Y = readPoints(points)
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
    
    def construct(self):
        n = Shapes2.points
        self.setup_axes(animate=True)
        a, k, p = readSpiral()
        for i, j in zip(Shapes2.X, Shapes2.Y):
            self.add(
                Dot(self.coords_to_point(
                    i, j
                ))
            )
            self.wait(0.75)

        self.play(ShowCreation(
            ParametricFunction(
                lambda t : self.coords_to_point(
                    *np.array([
                        a * pow(p, t / np.pi) * np.cos(t),
                        a * pow(p, t / np.pi) * np.sin(t),
                        0
                    ])[:-1]
                ),
                color = RED,
                t_min = -4 * np.pi,
                t_max = ((n // 4) * 2 + (n % 4)) * np.pi
            ),
            run_time = 6
        ))
        self.wait(5)
        
class Shapes3(GraphScene):

    points = int(sys.argv[2])
    X, Y = readPoints(points)
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
        return VMobject().set_points_as_corners(
            list(map(
                lambda x, y : self.coords_to_point(x, y),
                X, Y
            ))
        )
    
    def construct(self):
        n = Shapes3.points
        self.setup_axes(animate=True)
        a, k, p = readSpiral()
        for i, j in zip(Shapes3.X, Shapes3.Y):
            self.add(
                Dot(self.coords_to_point(
                    i, j
                ))
            )
            self.wait(0.75)
            
        self.play(ShowCreation(
            self.connectPoints(Shapes3.X, Shapes3.Y),
            run_time = 4
        ))
        
        self.play(ShowCreation(
            ParametricFunction(
                lambda t : self.coords_to_point(
                    *np.array([
                        a * pow(p, t / np.pi) * np.cos(t),
                        a * pow(p, t / np.pi) * np.sin(t),
                        0
                    ])[:-1]
                ),
                color = RED,
                t_min = -4 * np.pi,
                t_max = ((n // 4) * 2 + (n % 4)) * np.pi
            ),
            run_time = 6
        ))
        self.wait(5)
