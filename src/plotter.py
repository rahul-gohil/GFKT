import matplotlib.pyplot as plt
import numpy as np

from shapes.logSpiral import Spiral
from shapes.point     import points
from shapes.line      import lines

def zoom_factory(ax,base_scale = 2.):
    '''https://gist.github.com/tacaswell/3144287'''
    def zoom_fun(event):
        # get the current x and y limits
        cur_xlim = ax.get_xlim()
        cur_ylim = ax.get_ylim()
        # set the range
        cur_xrange = (cur_xlim[1] - cur_xlim[0])*.5
        cur_yrange = (cur_ylim[1] - cur_ylim[0])*.5
        xdata = event.xdata # get event x location
        ydata = event.ydata # get event y location
        if event.button == 'up':
            # deal with zoom in
            scale_factor = 1/base_scale
        elif event.button == 'down':
            # deal with zoom out
            scale_factor = base_scale
        else:
            # deal with something that should never happen
            scale_factor = 1
            print(event.button)
        # set new limits
        ax.set_xlim([xdata - cur_xrange*scale_factor,
                     xdata + cur_xrange*scale_factor])
        ax.set_ylim([ydata - cur_yrange*scale_factor,
                     ydata + cur_yrange*scale_factor])
        ax.figure.canvas.draw() # force re-draw

    fig = ax.get_figure() # get the figure of interest
    # attach the call back
    fig.canvas.mpl_connect('scroll_event',zoom_fun)

    #return the function
    return zoom_fun

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
    scale = 1.3
    f = zoom_factory(ax, base_scale = scale)

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
    
