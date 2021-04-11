import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


def square_wave(k):
    fig = plt.figure()  # type: plt.Figure
    ax = fig.gca()  # type: plt.Axes
    ax.set_xlim(-np.pi, 3 * np.pi)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    circle = plt.Circle((0, 0), 4 / np.pi, fill=0)
    ax.add_artist(circle)
    line = plt.Line2D([0, circle.radius], [0, 0])
    ax.add_artist(line)
    # ==== added code below  ==== #
    circles = [circle]
    lines = [line]

    for n in range(1,k):
        i = n*2+1
        newCircle = plt.Circle((circles[n-1].radius, 0), 4 / (i * np.pi), fill=0)
        circles.append(newCircle)
        ax.add_artist(newCircle)
        newLine = plt.Line2D([circles[n-1].radius, circles[n-1].radius + newCircle.radius], [0, 0])
        lines.append(newLine)
        ax.add_artist(newLine)

    pencil = plt.Line2D([], [])
    ax.add_artist(pencil)
    steps = 50

    wave_x = np.linspace(np.pi, 3 * np.pi, steps)
    wave_y = np.zeros(steps)
    wave = plt.Line2D(wave_x, wave_y)
    ax.add_artist(wave)

    angles = np.linspace(0, 2 * np.pi, steps + 1)[:steps]

    def update(frame):
        for m in range(1, k):
            t = angles[frame]  # get the angle
            xx = []
            yy = []
            xx.append(circles[0].radius * np.cos(t))
            yy.append(circles[0].radius * np.sin(t))

            lines[0].set_data([0, xx[0]], [0, yy[0]])

            for i in range(1, len(circles)):
                xx.append(xx[i - 1] + circles[i].radius * np.cos((2 * i + 1) * t))
                yy.append(yy[i - 1] + circles[i].radius * np.sin((2 * i + 1) * t))
                lines[i].set_data([xx[i - 1], xx[i]], [yy[i - 1], yy[i]])
                circles[i].set_center((xx[i - 1], yy[i - 1]))

            pencil.set_data([xx[-1], np.pi], [yy[-1], yy[-1]])

            wave_y[1:] = wave_y[:-1]
            wave_y[0] = yy[-1]
            wave.set_ydata(wave_y)
            return

    anim = animation.FuncAnimation(fig, update, init_func=lambda: None, frames=steps, interval=2000//steps)
    plt.show()



square_wave(5)