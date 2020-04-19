from csvUtils.functions import *

def writeToCsv(points, lines, triangles, spiral):
    writePoints(
        points,
        ['X', 'Y']
    )
    writeLines(
        lines,
        ['Point1', 'Point2']
    )
    writeTriangles(
        triangles,
        ['Line1', 'Line2', 'Line3']
    )
    writeLogSpiral(
        spiral,
        ['a', 'k', 'p']
    )
