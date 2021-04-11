import numpy as np
import matplotlib.pyplot as plt

def integrate(func, a, b, nrects):
    """
    :param func: the function to integrate
    :param a: start of the integration; should be lower than b
    :param b: end of the integration; should be higher than a
    :param nrects: number of rectangles to sum
    :return: the value of the integrated function between a and b
    """

    area = 0
    x = a
    dx = (b - a) / nrects

    while x < b:
        area += dx * (func(x) + func(x + dx)) / 2
        x += dx

    return area


def xx(x):
    return x**3

def showintegral(func, a, b, nmax, speed):
    n = 1
    xx = np.linspace(a, b, 1000)

    for j in range(n, nmax):
        plt.clf()
        plt.plot(xx, func(xx))
        dx = (b - a) / n
        for i in np.arange(a, b, dx):
            plt.plot([i, i], [0, func(i)])
            plt.plot([i + dx, i + dx], [0, func(i)])
            plt.plot([i, i + dx], [func(i), func(i)])
            plt.plot([i, i + dx], [func(i), func(i)])
            plt.show(block=False)
        n += 1
        plt.pause(speed)

