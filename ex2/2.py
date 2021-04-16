
import numpy as np
import matplotlib.pyplot as plt
import time


L = 8

x = np.zeros([L, L])
x[1, 1:3] = 1
x[1, 5:7] = 1
x[3, 3:5] = 1
x[5:7, 1::5] = 1
x[6, 2:6] = 1
plt.imshow(x, cmap='gray')
plt.show()

# 2.a-------------------------
y = np.ones([L, L])
y[1, 1:3] = 0
y[1, 5:7] = 0
y[3, 3:5] = 0
y[5:7, 1::5] = 0
y[6, 2:6] = 0
plt.imshow(y, cmap='gray')
plt.show()
# ----------------------------

# 2.b-------------------------
def facesimilarity(mat1, mat2):
    mat11 = np.ravel(mat1)
    mat22 = np.ravel(mat2)


    mat11 = mat11 / np.linalg.norm(mat11)
    mat22 = mat22 / np.linalg.norm(mat22)

    return np.inner(mat11, mat22)
# ----------------------------

# 2.c-------------------------

ipN = 0
Th = 0.7
j = 0

while ipN < Th:
    xtest = np.zeros([L, L])
    xtest[1:L-1, 1:L-1] = np.random.randint(0, 2, [L-2, L-2])

    normal = 1
    ipN = facesimilarity(x, xtest)

    if ipN > Th:
        print('ipN = ', ipN, 'access permitted')
        plt.imshow(xtest, cmap='gray')
        plt.show()
    else:
        print('ipN = ', ipN, 'access denied')

    print('sum Xtest = ', sum(sum(xtest)))

    
    j = j+1
    time.sleep(0.1)

print(j)