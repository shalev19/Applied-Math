# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import matplotlib.pyplot as plt

def func(x): return x**2

def fourier_approx(func, nmax=25, speed=0.5):
    """
    :param f: the function to approximate
    :param nmax: maximum number of coefficients to calculate
    :param speed: animation speed in seconds, defaults to 0.5 seconds
    """
    x = np.linspace(-np.pi, np.pi, 1000)
    xx = func(x)
    dx = x[1]-x[0]
    a0 = (1/np.pi) * np.trapz(xx, x, dx)
    fx = a0/2

    for k in range(1, nmax):
        a = (1/np.pi) * np.trapz(xx*np.cos(k*x), x, dx)
        b = (1 / np.pi) * np.trapz(xx * np.sin(k * x), x, dx)
        fx += a*np.cos(k*x) + b*np.sin(k*x)

        plt.clf()
        plt.ylim((-4, 4))
        plt.xlim((-np.pi, np.pi))
        plt.plot(x, fx)
        plt.plot(x, xx)
        plt.show(block=False)
        plt.pause(speed)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   fourier_approx(lambda x: x)