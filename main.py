import numpy as np
import matplotlib.pyplot as plt
import time

import math
import cmath

def dft(xs):
    ys = []
    n = float(len(xs))
    for k in range(len(xs)):
        y = 0.0
        for i in range(len(xs)):
            x = xs[i]
            y += x * cmath.exp(-2 * math.pi * 1j * (k / n) * float(i))
        ys.append(y)

    return ys

def fft(xs):
    n = len(xs)

    if n == 1:
        return xs

    if n.bit_count() != 1:
        raise Exception("bad")

    spectrum_even = fft(xs[0::2])
    spectrum_odd  = fft(xs[1::2])

    twiddle = np.exp(-2 * math.pi * 1j * np.arange(n // 2) / n)
    lhs = spectrum_even + twiddle * spectrum_odd
    rhs = spectrum_even - twiddle * spectrum_odd

    return np.concatenate((lhs, rhs))


def main():
    data = np.loadtxt("../../lab2/project/signal.csv", delimiter=",", skiprows=1)
    t = data[:, 0]
    signal = data[:, 1]
    n = len(signal)

    plt.plot(t, signal)
    plt.show()

    ks = np.arange(len(signal), dtype = float) / 20.0
    fs = fft(signal)
    # gs = np.fft.fft(signal)
    phases = (np.angle(fs) + math.pi / 2)
    phases = (phases + math.pi) % (2 * math.pi) - math.pi

    m = 0.01 * np.max(np.abs(fs))
    for i in range(len(ks) // 2 + 1):
        if np.abs(fs[i]) < m:
            continue
        
        print(f"Freq {ks[i]}, abs {np.abs(fs[i]) * 2 / n}, phase {phases[i]}")




    # plt.plot(fs)
    plt.plot(ks, np.real(fs))
    plt.plot(ks, phases)
    plt.show()

main()
