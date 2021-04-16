import numpy as np


def gs(A):
    m, n = A.shape
    R = np.zeros((m, n))
    Q = np.zeros((m, n))
    for j in range(n):
        v = A[:,j]
        for i in range(j-1):
            R[i, j] = np.inner(Q[:, i], v)
            v = v - (R[i, j] * Q[:, i])
        R[j, j] = np.linalg.norm(v)
        Q[:, j] = v / R[j, j]

    if np.inner(Q.all(), Q.all()) == 1:
        print("\nThe matrix Q is orthonormal\n")

    return R, Q


b = np.array([[1, 1, 1], [6, 4, 7], [8, 8, 8]])
RR, QQ = gs(b)
print("R:\n", RR)
print("Q:\n", QQ)


