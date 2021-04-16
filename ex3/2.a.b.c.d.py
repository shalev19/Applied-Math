import numpy as np
import matplotlib.pyplot as plt
import time
import sounddevice as sd


# a
def sigcreate(dur, f0, fs, u):
    nsig = int(fs*dur)

    tt = np.linspace(0, dur, nsig)
    sig = np.cos(2 * np.pi * f0 * tt + 2 * np.pi * u * (tt ** 2))
    return sig, tt


# b //create chirp sign
dur1 = 0.5
fss = 44100
f00 = 1000
uu = 500
sig1, ttt = sigcreate(dur1, f00, fss, uu)
Nsig = int(dur1*fss)
plt.subplot(2, 2, 1)
plt.plot(ttt[:200], sig1[:200])
plt.subplot(2, 2, 2)
plt.plot(ttt[-200:], sig1[-200:])

plt.show()
sd.play(sig1, fss)
time.sleep(5)

# c  add chirpn sign to the noise
dur2 = 10
L = int(dur2*fss)
xxnoise = np.random.randn(L)
ttnoise = np.linspace(0, dur2, L)


tstart = 7
nstart = int(tstart*fss)
xnsig = np.copy(xxnoise)
xnsig[nstart:nstart+Nsig] = xnsig[nstart:nstart+Nsig] + 0.1*sig1

plt.plot(ttnoise[nstart:nstart+Nsig], xnsig[nstart:nstart+Nsig])
plt.show()
sd.play(xnsig[nstart:nstart+Nsig], fss)
time.sleep(5)

# d
def findsig(frame, L, signal,fss, xnsig):
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

    return i/fss*step, i

print(findsig(Nsig,L, sig1,fss,xnsig))
