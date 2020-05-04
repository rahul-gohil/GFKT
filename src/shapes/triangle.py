from shapes.logSpiral   import Spiral
from shapes.point       import points
from shapes.line        import Line, lines

triangles = []

class Triangle:

    def __init__(self, line1, line2, line3):
        self.line1 = line1
        self.line2 = line2
        self.line3 = line3

    def debug(self, label):
        return {
            label : {
                "line1" : self.line1.debug("line1"),
                "line2" : self.line2.debug("line2"),
                "line3" : self.line3.debug("line3")
            }
        }

def makeTriangles(n):
    for i in range(1, n):
        triangles.append(Triangle(
            triangles[i - 1].line2,
            Line(points[i - 1], points[i]),
            lines[i]
        ))

def limitizeTriangle():
    '''Limitizes similarity between triangles'''
    for i in range(2, len(triangles) - 1):
        a = triangles[i + 1].line1.length() /\
            triangles[i].line1.length()
        b = triangles[i + 1].line2.length() /\
            triangles[i].line2.length()
        c = triangles[i + 1].line3.length() /\
            triangles[i].line3.length()
        if a == b and b == c:
            return (
                "triangles",
                {
                    "comment" : "Converged to similarity between triangles",
                    "factor" : a,
                    "iteration" : i
                }
            )
    else:
        expected = pow(Spiral().p, 0.5)
        return (
            "triangles",
            {
                "comment" : "Did not converge to similarity",
                "a" : {
                    "expected" : expected,
                    "limitized" : a,
                    "error" : expected - a
                },
                "b" : {
                    "expected" : expected,
                    "limitized" : b,
                    "error" : expected - b
                },
                "c" : {
                    "expected" : expected,
                    "limitized" : c,
                    "error" : expected - c
                }
            }
        )
