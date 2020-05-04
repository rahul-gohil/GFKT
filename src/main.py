import solver
import json
import sys
import os

from csvUtils.writer         import writeToCsv
from mpl.plotter import plot

from shapes.logSpiral import *
from shapes.triangle  import *
from shapes.point     import *
from shapes.line      import *

def prettify(d):
    '''Prettifies dictionary'''
    return json.dumps(
        d,
        sort_keys = False,
        indent = 4,
        separators = (
            ',',
            ': '
        )
    )

engine = 'mpl'
if len(sys.argv) > 1:
    if sys.argv[1] == '-manim':
        engine = 'manim'
    elif sys.argv[1] == '-noplot':
        engine = None
    else:
        raise ValueError('Argument should be -manim or -noplot')

f = solver.f

x1, y1, solver.f0, solver.f1 = map(
    float,
    input("Enter x1, y1, f(0) & f(1)\t").split()
)

assert 0 <= f(0),   "f(0) has to be positive"
assert 0 <= f(1),   "f(1) has to be positive"
assert x1 < f(0),   "f(0) has to be greater than x1"
assert y1 < f(1),   "f(1) has to be greater than y1"
assert f(0) < f(1), "f(1) has to be greater than f(0)"

n = int(input("Enter the number of points\t"))

assert n <= 1400,   "Too Large for computing f(n)"

if engine is not None:
    n1 = int(input("Enter the number of points to plot\t"))

I0 = Point(x1, y1)
I1 = Point(f(0) + x1, y1)
points.append(Point(f(0) + x1, f(1) + y1))
makePoints(n)

lines.append(Line(I0, points[0]))
lines.append(Line(I1, points[1]))
makeLines(n + 1)

T0 = Triangle(
    Line(I0, I1),
    Line(I1, points[0]),
    lines[0]
)
triangles.append(T0)
makeTriangles(n + 1)

print(prettify(
    dict([
        limitizeLine(),
        limitizeTriangle(),
        limitizeLogSpiral(I0, n)
    ])
))

I0.x, I0.y = 0, 0
I1.x, I1.y = f(0), 0
shiftPoints(x1, y1)

if engine is not None:
    if engine == 'mpl':
        plot(n1 - 2, [I0, I1])
    if engine == 'manim':
        writeToCsv(
            [I0, I1] + points,
            lines,
            triangles,
            Spiral()
        )
        os.system(
            f'manim ./manim/allAnim.py {n1} Shapes -pl'
        )
