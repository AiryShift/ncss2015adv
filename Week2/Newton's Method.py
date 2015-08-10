ITERATIONS = 10


def newton_sqrt(k):
    x = k / 2
    for _ in range(ITERATIONS):
        x = x - (x ** 2 - k) / (2 * x)
    return x
