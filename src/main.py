import solver
import sys
import os

from matplotlibUtils.plotter import plot
from csvUtils.writer         import writeToCsv

from shapes.logSpiral import *
from shapes.triangle  import *
from shapes.point     import *
from shapes.line      import *

engine = 'mpl'
if len(sys.argv) > 1:
    if sys.argv[1] == '-manim':
        engine = 'manim'
    if sys.argv[1] != '-manim':
        raise ValueError('Argument should be -manim')
    
f = solver.f

x1, y1, solver.f0, solver.f1 = map(
    float,
    input("Enter x1, y1, f(0) & f(1)\t").split()
)
n = int(input("Enter the number of points\t"))

assert x1 < f(0),   "f(0) has to be greater than x1"
assert y1 < f(1),   "f(1) has to be greater than y1"
assert f(0) < f(1), "f(1) has to be greater than f(0)"
assert n <= 1400,   "Too Large for computing f(n)"

I0 = Point(x1, y1)
I1 = Point(f(0) + x1, y1)
points.append(Point(f(0) + x1, f(1) + y1))
makePoints(n)

lines.append(Line(I0, points[0]))
lines.append(Line(I1, points[1]))
makeLines(n + 1)

T0 = Triangle(Line(I0, I1), Line(I1, points[0]), lines[0])
triangles.append(T0)
makeTriangles(n + 1)

limitizeLine()
limitizeTriangle()
limitizeLogSpiral(I0, n)

if engine == 'mpl':
    plot(17, [I0, I1])
if engine == 'manim':
    writeToCsv([I0, I1] + points, lines, triangles, Spiral())
    os.system(
        'manim ./manimUtils/allAnim.py Shapes -pl'
    )
