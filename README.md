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


![Manim](/img/Shapes-Manim.gif)
