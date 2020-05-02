from shapes.prettyPrint import prettify
from shapes.logSpiral   import Spiral as spiral
from shapes.point       import points
from shapes.line        import Line, lines

triangles = []

class Triangle:

    def __init__(self, line1, line2, line3):
        self.line1 = line1
        self.line2 = line2
        self.line3 = line3

def makeTriangles(n):
    for i in range(1, n):
        triangles.append(Triangle(
            triangles[i - 1].line2,
            Line(points[i - 1], points[i]),
            lines[i]
        ))

def limitizeTriangle():
    for i in range(2, len(triangles) - 1):
        a = triangles[i + 1].line1.length() /\
            triangles[i].line1.length()
        b = triangles[i + 1].line2.length() /\
            triangles[i].line2.length()
        c = triangles[i + 1].line3.length() /\
            triangles[i].line3.length()
        if a == b and b == c:
            converged = {
                "triangles" : {
                    "comment" : "Converged to similarity between triangles",
                    "factor" : a
                }
            }
            print(prettify(converged))
            break
    else:
        expected = pow(spiral.p, 0.5)
        errors = {
            "triangles" : {
                "comment" : "Did not converge to similarity",
                "a" : {
                    "expected" : expected,
                    "limitized" : a
                },
                "b" : {
                    "expected" : expected,
                    "limitized" : b
                },
                "c" : {
                    "expected" : expected,
                    "limitized" : c
                }
            }
        }
        print(prettify(errors))
