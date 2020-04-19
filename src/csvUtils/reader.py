import csv

def read(fileName, n):
    rows = []
    with open(fileName, 'r') as _file:
        csvReader = csv.reader(_file)
        fields = next(csvReader)
        for row in csvReader:
            rows.append(row)
    rows = list(map(
        lambda i : list(map(
            lambda x : float(x),
            rows[i]
        )),
        range(n)
    ))
    return rows[:n]

def readPoints(n):
    rows = read('../data/Points.csv', n)
    X = list(map(
        lambda row : row[0],
        rows
    ))
    Y = list(map(
        lambda row : row[1],
        rows
    ))
    return(X, Y)
    
def readSpiral():
    rows = read('../data/LogSpiral.csv', 1)
    return rows[0][0], rows[0][1], rows[0][2]
