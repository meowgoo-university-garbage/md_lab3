import numpy as np
import matplotlib.pyplot as plt
import math
import time

def main():
    data = np.loadtxt("signal.csv", delimiter=",", skiprows=1)
    t = data[:, 0]
    signal = data[:, 1]
    n = len(signal)

    plt.plot(t, signal)
    plt.show()

main()
