import matplotlib.pyplot as plt
import numpy as np

from shapes.logSpiral import Spiral
from shapes.point     import points
from shapes.line      import lines

def plotAxes(x, y):
    ax = plt.figure().add_subplot(1, 1, 1)
    
    ax.spines['left'].set_position(('data', x))
    ax.spines['bottom'].set_position(('data', y))
    ax.spines['right'].set_position(('data', x - 1))
    ax.spines['top'].set_position(('data', y - 1))

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

def plotLinePrime(n, X, Y):
    for i in range(n + 1):
        plt.plot(X[i : i + 2], Y[i : i + 2], 'ro-')

def plotLine(n, lines):
    for i in range(n):
        X = [lines[i].point1.x, lines[i].point2.x]
        Y = [lines[i].point1.y, lines[i].point2.y]
        plt.plot(X, Y, 'ro-')

def plotSpiral(n):
    spiral = Spiral()
    lLim = -2 * np.pi
    rLim = (n // 4) * 2 * np.pi + (n % 4) * np.pi
    theta = np.arange(lLim, rLim, 0.1)
    X = list(map(
        lambda x : spiral.a * pow(spiral.p, x / np.pi) * np.cos(x),
        theta
    ))
    Y = list(map(
        lambda y : spiral.a * pow(spiral.p, y / np.pi) * np.sin(y),
        theta
    ))
    plt.plot(X, Y)
    
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
    plotSpiral(n)
    plt.scatter(pointsX, pointsY)
    plt.show()
    
