import math

f0 = 0
f1 = 0
a = 1
b = 1
init = []

def rho(a, b):
    p = (1 + pow(5, 0.5)) / 2
    if b == 1:
        return pow(p, 4 / a) / (pow(p, 2 / a) + 1)
    if b == 2:
        return pow(p, 3 / a) / (pow(p, 1 / a) + 1)

def fibonacci(n):
    phi = (1 + math.sqrt(5)) / 2

    return (
        pow(phi, n)
        - (
            math.cos(n * math.pi)
            * pow(phi, -n)
        )
    ) / math.sqrt(5)

def f(n):
    n = int(n)
    if n < 2 * b:
        return init[n]
    return pow(
        fibonacci(n // b) * pow(f(b + (n % b)), a)
        + fibonacci((n // b) - 1) * pow(f(n % b), a),
        1 / a
    ).real
