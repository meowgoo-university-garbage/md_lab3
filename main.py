import numpy as np
import matplotlib.pyplot as plt
import time

import math
import cmath

def dft(xs, ks):
    ys = []
    n = float(len(xs))
    for k in range(len(xs)):
        y = 0.0
        for i in range(len(xs)):
            x = xs[i]
            y += x * cmath.exp(-2 * math.pi * 1j * (k / n) * float(i))
        ys.append(y)

    return ys


def main():
    data = np.loadtxt("signal.csv", delimiter=",", skiprows=1)
    t = data[:, 0]
    signal = data[:, 1]
    n = len(signal)

    plt.plot(t, signal)
    plt.show()

    ks = np.arange(0, 4096, 1, dtype = float)
    ks /= 20.0
    fs = dft(signal, ks)
    # gs = np.fft.fft(signal)
    freqs = np.fft.fftfreq(len(signal), d = 20.0 / 4096.0)

    # plt.plot(fs)
    plt.plot(ks, fs)
    plt.show()

main()
