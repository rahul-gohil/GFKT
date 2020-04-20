# GFKT
GFKT is a visualizer for how we can generate [Kepler Triangles](https://en.wikipedia.org/wiki/Kepler_triangle) and through their special arrangement we can obtain these [Logarithmic Spirals](https://en.wikipedia.org/wiki/Logarithmic_spiral).
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
Converged at Satisfaction Factor 0 and Angle Factor 90.0 in Iteration 37
Converged to Similarity between Triangles in Iteration 40
Converged at "a" 2.7035313755677604 and "k" 0.15317448126501637 in Iteration 141
```
If you want a plot, the program will ask you for the number of points to plot.
### Using `-manim`
To get a `480p` video for the plot, just run the file as is, but to get a `1080p` video remove the `-pl` option in `main.py` file at the bottom.

It will generate a video similar to this gif.


![Manim-plot](/img/Shapes-Manim.gif)

## Acknowledgements
[tacaswell](https://gist.github.com/tacaswell/3144287) for `zoomFactory.py` - adds zooming properties to matplotlib plot.
