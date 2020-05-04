import sys
sys.path.append('..')

from src.csvUtils.reader import *
from manimlib.imports    import *

n = int(sys.argv[2])
X, Y = readPoints(n)
a, k, p = readSpiral()

_min = min(*X, *Y)
_max = max(*X, *Y)

class Shapes(GraphScene):

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

    def logSpiralSequence(self, create, fade):
        '''Create and Fade sequence for logSpiral'''
        self.play(
            create,
            run_time = 6
        )
        self.play(
            fade,
            run_time = 3
        )

    def plotPoints(self):

        for i, j in zip(X, Y):
            self.add(
                Dot(self.coords_to_point(
                    i, j
                ))
            )
            self.wait(0.75)

    def parametricFunction(self):

        return ParametricFunction(
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
        )


    def connectPoints(self, X, Y):
        '''Similar to plt.scatter(X, Y) in mpl'''
        return VMobject().set_points_as_corners(
            list(map(
                lambda x, y : self.coords_to_point(x, y),
                X, Y
            ))
        )

    def construct(self):

        self.setup_axes(animate = True)
        logSpiral = self.parametricFunction()
        Create = ShowCreation(logSpiral)
        Fade = FadeOut(logSpiral)
        linePrime = self.connectPoints(X, Y)
        line = [
            self.connectPoints(X[::2], Y[::2]),
            self.connectPoints(X[1::2], Y[1::2])
        ]

        self.plotPoints()

        self.logSpiralSequence(Create, Fade)
        self.play(ShowCreation(
            linePrime,
            run_time = 4
        ))
        self.logSpiralSequence(Create, Fade)
        self.play(ShowCreation(
            line[0],
            run_time = 2
        ))
        self.play(ShowCreation(
            line[1],
            run_time = 2
        ))
        self.play(
            Create,
            run_time = 6
        )
        self.wait(5)
