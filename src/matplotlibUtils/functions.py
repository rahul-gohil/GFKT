import matplotlib.pyplot as plt
import numpy as np
import math

from matplotlibUtils.zoomFactory import zoomFactory
from solver import f
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
    theta = np.arange(
        -4 * np.pi,
        ((n // 4) * 2 + (n % 4)) * np.pi,
        0.01
    )
    X = list(map(
        lambda x :
            spiral.a
            * pow(spiral.p, x / np.pi)
            * np.cos(x),
        theta
    ))
    Y = list(map(
        lambda y :
            spiral.a
            * pow(spiral.p, y / np.pi)
            * np.sin(y),
        theta
    ))
    plt.plot(X, Y)
