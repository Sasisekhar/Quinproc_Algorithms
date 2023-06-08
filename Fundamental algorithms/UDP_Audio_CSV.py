import socket
import struct
from matplotlib import pyplot as plt
import pyaudio
from scipy.signal import butter, filtfilt


def butter_lowpass_filter(data, cutoff, order, Fs):
    # Get the filter coefficients 
    b, a = butter(order, Wn = cutoff, fs = Fs, btype='low', analog=False)
    y = filtfilt(b, a, data)
    return y

audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paFloat32, channels=1, rate=8000, output=True, frames_per_buffer=4096)

UDP_IP = "192.168.137.1"
UDP_PORT = 3333
   
sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP

sock.bind((UDP_IP, UDP_PORT))

file = open ('audioData_Combined_retrial.csv', 'w')

while True:

    outData = []
    txData = bytes()

    data, addr = sock.recvfrom(131072) # buffer size is 4096 bytes
    
    y = []
    for i in range(0, 16384, 4):
        a = float(struct.unpack('<f', data[i : i+4])[0])
        y.append(a)

    for i in y[:2048]:
        outData.append(i)

    for i in outData:
        file.write(str(i) + "\n")
        txData += bytes(struct.pack('<f', i))

    stream.write(txData)