import matplotlib.pyplot as plt
import numpy as np
import solver
import math

from mpl.zoomFactory import zoomFactory


f = solver.f

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
    zoomFactory(ax, base_scale = 1.2)

def plotLinePrime(n, X, Y):
    for i in range(n + 1):
        plt.plot(X[i : i + 2], Y[i : i + 2], 'ro-')

def plotLine(n, lines):
    for i in range(n):
        X = [lines[i].point1.x, lines[i].point2.x]
        Y = [lines[i].point1.y, lines[i].point2.y]
        plt.plot(X, Y, 'ro-')

def plotSpiral(n, spiral):
    '''Plots Spiral based on cartesion equation
    x = r * cos(theta),
    y = r * sin(theta),
    where r  = t * phi^(theta / pi)
    '''
    theta = np.arange(
        -4 * np.pi,
        n * np.pi / 2,
        0.1
    )
    X = list(map(
        lambda x :
            spiral.t
            * pow(spiral.p, (2 * x) / (solver.a * np.pi))
            * np.cos(x),
        theta
    ))
    Y = list(map(
        lambda y :
            spiral.t
            * pow(spiral.p, (2 * y) / (solver.a * np.pi))
            * np.sin(y),
        theta
    ))
    plt.plot(X, Y)
