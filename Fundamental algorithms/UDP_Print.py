import socket
import struct

UDP_IP = "192.168.137.1"
UDP_PORT = 3333
   
sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP

sock.bind((UDP_IP, UDP_PORT))

outData = []

while True:
    data, addr = sock.recvfrom(8192)

    for i in range(0, 8192, 4):
        a = float(struct.unpack('<f', data[i : i+4])[0])
        outData.append(a)

    print(outData)

