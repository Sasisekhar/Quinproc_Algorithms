import serial
import time
from os.path import exists
import matplotlib.pyplot as plt
import sys

ser = serial.Serial("COM5", 115200)

file_name = "EMG_Data_"
counter = 0
while(exists(file_name + str(counter) + ".csv")):
    counter = counter + 1

file = open(file_name + str(counter) + ".csv", 'w')
# file.write("Voltage\n")

print("Writing...")


while(True):
    try:
        data = ser.readline()
        file.write(time.strftime("%d-%b-%Y,%H:%M:%S,", time.localtime(time.time())) + str(data)[2:-5] + "\n")
        print(str(data)[2:-5])
        # plt.clf()
        # plt.plot(plotVar[-500:])
        # plt.ylim([500, 2000])
        # plt.pause(0.00000001)
    except KeyboardInterrupt:
        file.close()
        sys.exit(0)