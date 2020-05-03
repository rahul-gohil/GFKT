# GFKT
GFKT is a visualizer for generating [Kepler Triangles](https://en.wikipedia.org/wiki/Kepler_triangle) and through their special arrangement obatining [Logarithmic Spirals](https://en.wikipedia.org/wiki/Logarithmic_spiral).


[![DOI](https://zenodo.org/badge/256438420.svg)](https://zenodo.org/badge/latestdoi/256438420)
## Getting Started
To start visualizing these plots on your system, follow these steps.

Clone or download the repository, then once inside the main `GFKT` folder run,
```
python3 -m pip install -r requirements.txt
```
You will need to install other components of manim separately, to do this visit [their repository](https://github.com/3b1b/manim#installation)
## Plotting
GFKT uses 2 libraries to plot which are matplotlib and manimlib.

To start plotting `cd` into `src` folder and execute the command,
```
python3 main.py
```
By default the plotting library is matplotlib, to use manim you can specify `-manim` command line argument.

For just obtaining results you can specify `-noplot` command line argument.


Test run with `-noplot`
```
~/GFKT/src$ python3 main.py -noplot
Enter x1, y1, f(0) & f(1)	0 0 3 4
Enter the number of points	150
{
    "lines": {
        "comment": "Converged at expected values",
        "Angle Factor": 90.0,
        "Satisfaction Factor": 0,
        "iteration": 35
    },
    "triangles": {
        "comment": "Converged to similarity between triangles",
        "factor": 1.272019649514069,
        "iteration": 36
    },
    "logarithmicSpiral": {
        "comment": "Converged at expected values",
        "a": 2.7035313754910306,
        "k": 0.1531744812651672,
        "iteration": 118
    }
}
```
If you want a plot, the program will ask you for the number of points to plot.
### Poltting with `matplotlib`
It will generate a standard plot.

You can use your mouse wheel to directly zoom in/out of the plot.


![Mpl-plot](/img/Shapes-Mpl.gif)
### Plotting with `manim`
To get a `480p` video for the plot, just run the file as is, but to get a `1080p` video remove the `-pl` option in `main.py` file at the bottom.

It will generate a video similar to this gif.(Recommended to plot 10 ~ 20 points)


![Manim-plot](/img/Shapes-Manim.gif)

## Acknowledgements
[tacaswell](https://gist.github.com/tacaswell/3144287) for `zoomFactory.py` - adds zooming properties to matplotlib plots.
