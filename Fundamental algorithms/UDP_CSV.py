import socket
import struct

# UDP_IP = "172.31.45.151"
UDP_IP = "192.168.137.1"
# UDP_PORT = 4444
UDP_PORT = 3333
   
sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP

sock.bind((UDP_IP, UDP_PORT))
file = open ('audioData_all_four.csv', 'w')

# file.write("Left,Right\n")

outData = []

while True:

    y_l_1 = []
    y_r_1 = []
    y_l_2 = []
    y_r_2 = []
        
    for i in range(0, 2):
        data, addr = sock.recvfrom(131104)

        for i in range(0, 16388, 4):
            a = float(struct.unpack('<f', data[i : i+4])[0])
            outData.append(a)

        batch = outData.pop()
        
        if(batch == 1.0 and len(y_l_1) == 0):
            for i in outData[:2048]:
                y_l_1.append(i)
            
            for i in outData[-2048:]:
                y_r_1.append(i)
        elif(batch == 2.0 and len(y_l_2) == 0):
            for i in outData[:2048]:
                y_l_2.append(i)
            
            for i in outData[-2048:]:
                y_r_2.append(i)


    try:
        for i in range(0, 2048):
            file.write(str(y_l_1[i]) + "," + str(y_r_1[i]) + "," +  str(y_l_2[i]) + "," + str(y_r_2[i]) + "\n")
    except:
        print("Missed packet")