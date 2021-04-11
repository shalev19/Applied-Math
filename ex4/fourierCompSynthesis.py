import numpy as np
import matplotlib.pyplot as plt
import time


def FourierCompSynthesis(cn, func, m, N):
    """
     FourierCompSynthesis for construting a partial sum of a complex Fourier series
     Inputs: cn - coefficients of complex exponentials (strings
     func - the function (string) for which the complex Fourier series coeffs were
     calculated.
     m - the series partial sum index, N - number of points on the x axis
     Output - FourierCompSynthesis returns the Fourier partial sum of order m
     Usage: y = FourierCompSynthesis(cn, func, m, N(
    """
    x = np.linspace(-np.pi, np.pi, N)
    fx = eval(func)
    sm = np.zeros(len(x), dtype=complex)
    n = 0
    dx = x[1] - x[0]
    c0 = eval(cn)
    sm += c0

    for n in range(1, m):
        plt.clf()
        stitle = 'Fourier series partial sum n = ' + str(n)

        plt.title(stitle)
        c_n = eval(cn)
        sm += c_n * np.exp(1.j*n*x)
        n *= -1
        c_n = eval(cn)
        sm += c_n * np.exp(1.j * n * x)

        plt.plot(x, sm.real)
        plt.plot(x, fx, 'r')
        plt.show(block=False)
        plt.pause(0.5)
    return sm

