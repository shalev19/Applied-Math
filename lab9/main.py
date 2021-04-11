import numpy as np
import matplotlib.pyplot as plt


def threedline():
    ax = plt.axes(projection='3d')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    x = np.linspace(-10, 10, 25)
    y = np.linspace(-10, 10, 25)

    plt.plot(x, y, np.sin(x) + np.cos(y))
    plt.show()


def drawsurface():
    ax = plt.axes(projection='3d')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    x = np.linspace(-10, 10, 25)
    y = np.linspace(-10, 10, 25)
    X, Y = np.meshgrid(x, y)
    ax.plot_surface(X, Y, np.cos(X) + np.sin(Y))
    plt.show()


def z_func(x, y): return np.cos(x) + np.sin(y)

def display_surface(z_func):
    ax = plt.axes(projection='3d')
    x = np.linspace(-10, 10, 50)
    y = np.linspace(-10, 10, 50)

    X, Y = np.meshgrid(x, y)
    ax.plot_surface(X, Y, z_func(X,Y))
    ax.set_zlim((-10, 10))
    for n in range(0, 360,4):
        ax.view_init(10, n)
        plt.gcf().canvas.draw()
        plt.pause(.001)



threedline()
drawsurface()
display_surface(z_func)