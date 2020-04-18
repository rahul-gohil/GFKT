import matplotlib.pyplot as plt

from plotUtils.functions import *
from shapes.logSpiral    import Spiral
from shapes.point        import points
from shapes.line         import lines


def plot(n, init):
    plotAxes(init[0].x, init[0].y)
    pointsX = [init[0].x, init[1].x] + list(map(
        lambda i : points[i].x,
        range(n)
    ))
    pointsY = [init[0].y, init[1].y] + list(map(
        lambda i : points[i].y,
        range(n)
    ))
    plotLinePrime(n, pointsX, pointsY)
    plotLine(n, lines)
    plotSpiral(n, Spiral())
    plt.scatter(pointsX, pointsY)
    plt.show()
    
