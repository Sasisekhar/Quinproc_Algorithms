from scipy.fft import fft, fftfreq
import socket
import struct
from matplotlib import pyplot as plt
import numpy as np
from math import floor

UDP_IP = "192.168.137.1"
UDP_PORT = 3333
   
sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP

sock.bind((UDP_IP, UDP_PORT))

fig = plt.figure()
ax = fig.add_subplot(2, 1, 1)
ax1 = fig.add_subplot(2, 1, 2)

while True:
    data, addr = sock.recvfrom(131072)

    y = []

    for i in range(0, 16384, 4):
        a = float(struct.unpack('<f', data[i : i+4])[0])
        y.append(a)

    yf_l = fft(y[:2048])
    yf_r = fft(y[-2048:])
    xf = fftfreq(2048, 1 / 16000)

    ax.clear()
    ax1.clear()

    ax.plot(xf, np.abs(yf_l))
    # ax.set_ylim([0, 10000000])
    # ax.set_xlim([-2000, 2000])

    ax1.plot(xf, np.abs(yf_r))
    # ax1.set_ylim([0, 10000000])
    # ax1.set_xlim([-2000, 2000])
    plt.pause(0.00001)