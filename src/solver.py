import math

f0 = 0
f1 = 0

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
    return pow(
        fibonacci(n) * pow(f1, 2)
        + fibonacci(n - 1) * pow(f0, 2),
        0.5
    ).real
