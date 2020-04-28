'''https://gist.github.com/tacaswell/3144287'''

import matplotlib.pyplot as plt

def zoomFactory(ax, base_scale = 2.):
    
    def zoomFun(event):
        cur_xlim = ax.get_xlim()
        cur_ylim = ax.get_ylim()
        cur_xrange = (cur_xlim[1] - cur_xlim[0]) * .5
        cur_yrange = (cur_ylim[1] - cur_ylim[0]) * .5
        xdata = event.xdata
        ydata = event.ydata
        if event.button == 'up':
            scale_factor = 1 / base_scale
        elif event.button == 'down':
            scale_factor = base_scale
        else:
            scale_factor = 1
        ax.set_xlim([
            xdata - cur_xrange * scale_factor,
            xdata + cur_xrange * scale_factor
        ])
        ax.set_ylim([
            ydata - cur_yrange * scale_factor,
            ydata + cur_yrange * scale_factor
         ])
        ax.figure.canvas.draw()

    fig = ax.get_figure()
    fig.canvas.mpl_connect('scroll_event', zoomFun)

    return zoomFun
