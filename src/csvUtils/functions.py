import csv

from os import path, mkdir

listifyP = lambda points : list(map(
    lambda point : [point.x, point.y],
    points
))

listifyL = lambda lines : list(map(
    lambda line : listifyP([
        line.point1,
        line.point2
    ]),
    lines
))

def write(fileName, fields, rows):
    try:
        mkdir(path.join(
            path.abspath('.'),
            'data'
        ))
    except:
        pass
    with open('./data/' + fileName, 'w') as _file:
        csvWriter = csv.writer(_file)
        csvWriter.writerow(fields)
        csvWriter.writerows(rows)
        
def writePoints(points, fields):
    rows = listifyP(points)
    write('Points.csv', fields, rows)
    
def writeLines(lines, fields):
    rows = listifyL(lines)
    write('Lines.csv', fields, rows)
    
def writeTriangles(triangles, fields):
    rows = list(map(
        lambda triangle : listifyL([
            triangle.line1,
            triangle.line2,
            triangle.line3
        ]),
        triangles
    ))
    write('Triangles.csv', fields, rows)
    
def writeLogSpiral(spiral, fields):
    rows = [[
        spiral.a,
        spiral.k,
        spiral.p
    ]]
    write('LogSpiral.csv', fields, rows)
