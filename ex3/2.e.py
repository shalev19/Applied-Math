
import numpy as np
import matplotlib.pyplot as plt
import time


chirp = np.load('chirp.npy')
# b //create chirp sign
dur1 = 0.5
fss = 44100
f00 = 1000
uu = 500
Nsig = int(dur1*fss)


xnsig= np.load('xnsig.npy')
dur2 = 16
L = (dur2*fss)


def findsig(frame, L, signal,dur,fss,xnsig):
    step = 100
    iplen = int((L - frame) / step)
    maxinner = 0
    i = 0
    ip = np.zeros(iplen)


    for j in range(iplen):
        xtest = xnsig[j * step:j * step + frame]
        ip[j] = np.inner(xtest / np.linalg.norm(xtest), signal / np.linalg.norm(signal))
        if (maxinner < ip[j]):
            maxinner = ip[[j]]
            i = j
    ttt = np.linspace(0,dur,num=iplen)
    plt.plot(ttt,ip)
    plt.show()
    return i/fss*step, i

print(findsig(Nsig,L,chirp,dur2,fss,xnsig))