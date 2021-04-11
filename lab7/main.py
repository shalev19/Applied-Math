import numpy as np
import matplotlib.pyplot as plt


def printRoots(z, n):
    rad = np.sqrt(np.real(z)**2 + np.imag(z)**2)
    roots = np.zeros(n,dtype=complex)
    for k in range(n):
        zk = rad**(1/n)*(np.cos((np.angle(z)+2*np.pi*k)/n) + 1.j*np.sin((np.angle(z)+2*np.pi*k)/n))
        roots[k] = zk
    return roots


if __name__ == '__main__':
    z1 = np.complex(7 + 5j)
    rootsarr = printRoots(z1, 5)
    print(rootsarr)
    theta = np.angle(rootsarr)

    r = np.abs(rootsarr)
    plt.polar(theta, r, marker="X", linewidth=0)
    plt.show()

