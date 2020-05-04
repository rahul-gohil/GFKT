from os import path, mkdir

from csvUtils.functions import *

def writeToCsv(points, lines, triangles, spiral):
    '''Creates src/data to store csv files and writes'''
    try:
        mkdir(path.join(
            path.abspath('.'),
            'data'
        ))
    except OSError:
        pass
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
