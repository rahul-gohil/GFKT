import math
 
f0 = 0
f1 = 0

def matrixMult(m1, m2):
    x = (m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0])
    y = (m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1])
    z = (m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0])
    w = (m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1])
    m1[0][0] = x
    m1[0][1] = y
    m1[1][0] = z
    m1[1][1] = w
    return m1

def matrixExpo(power):
    I = [[1, 0], [0, 1]]
    m = [[1, 1], [1, 0]]
    while power:
        if power & 1:
            I = matrixMult(I, m)
        m = matrixMult(m, m)
        power //= 2
    return math.sqrt(I[0][0] * pow(f1, 2) + I[0][1] * pow(f0, 2))

def f(n):
    if n == 0:
        return f0
    if n == 1:
        return f1
    return matrixExpo(n - 1)   

