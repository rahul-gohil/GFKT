import matplotlib.pyplot as plt

from mpl.functions import *
from shapes.logSpiral    import Spiral
from shapes.point        import points
from shapes.line         import lines


def plot(n, init):
    plotAxes(init[0].x, init[0].y)
    X = [init[0].x, init[1].x] + list(map(
        lambda i : points[i].x,
        range(n)
    ))
    Y = [init[0].y, init[1].y] + list(map(
        lambda i : points[i].y,
        range(n)
    ))
    plotLinePrime(n, X, Y)
    plotLine(n, lines)
    plotSpiral(n, Spiral())
    plt.scatter(X, Y)
    plt.show()
