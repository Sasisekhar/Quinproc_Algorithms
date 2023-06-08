import socket
import struct
from matplotlib import pyplot as plt
import numpy as np

UDP_IP = "192.168.137.1"
UDP_PORT = 3333
   
sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP

sock.bind((UDP_IP, UDP_PORT))

fig = plt.figure()
ax = fig.add_subplot(2, 1, 1)
ax1 = fig.add_subplot(2, 1, 2)

y_l = []
y_r = []

while True:
    data, addr = sock.recvfrom(131072)

    y = []

    for i in range(0, 16384, 4):
        a = float(struct.unpack('<f', data[i : i+4])[0])
        y.append(a)

    for i in y[:2048]:
        y_l.append(i)
    
    for i in y[-2048:]:
        y_r.append(i)
    
    y_l = y_l[-20000:]
    y_r = y_r[-20000:]

    xf = np.linspace(0, len(y_l) - 1, num = len(y_l))

    ax.clear()
    ax1.clear()

    ax.plot(xf, y_l)
    ax1.plot(xf, y_r)

    plt.pause(0.00001)