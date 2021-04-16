import numpy as np
from numpy import linalg as LA


def norm(v, p):
    if p == np.inf:
        p = max(abs(v))
    n = sum(abs(v)**p)**(1/p)

    return n


#1
v = np.array([1, -2, 3, 1, 5])
for i in range(9):
    print("norm(v,",i+1,"): ",norm(v, i+1))
print("norm(v,inf): ",norm(v, np.inf))

#1.b
v1 = np.array([1, 5, 2, -2, 7])
print("unit vector of V1: ",v1/norm(v1,2))

#1.b.2
v = np.array([0, 7, -15, 2, 7])
u = np.array([1, 3, -2, -3, 5])
print("distance between V and U: ",norm(v-u, 2))