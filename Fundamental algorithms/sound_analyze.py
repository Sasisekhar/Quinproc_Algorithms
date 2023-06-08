import serial
import pyaudio
import numpy as np


ser = serial.Serial("COM5", 115200)

while (True):
    audio = []
    a = 10
    for i in range(0, 4500):
        try:
            a = int(ser.readline()[:-2])
        except:
            pass

        audio.append(a)

    print("* Generating sample...")
    tone_out = np.array(audio, dtype=np.int16)

    print("* Previewing audio file...")

    bytestream = tone_out.tobytes()
    pya = pyaudio.PyAudio()
    stream = pya.open(format=pya.get_format_from_width(width=1,unsigned=True), channels=1, rate=10240, output=True)
    stream.write(bytestream)
    stream.stop_stream()
    stream.close()

    pya.terminate()
    print("* Preview completed!")