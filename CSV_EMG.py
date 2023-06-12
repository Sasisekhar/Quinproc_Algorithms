import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.signal import butter, filtfilt, find_peaks
from scipy.ndimage import gaussian_filter1d

def butter_lowpass_filter(sig, cutoff, order, Fs):
    # Get the filter coefficients 
    b, a = butter(order, Wn = cutoff, fs = Fs, btype='low', analog=False)
    y = filtfilt(b, a, sig)
    return y

def butter_highpass_filter(sig, cutoff, order, Fs):
    # Get the filter coefficients 
    b, a = butter(order, Wn = cutoff, fs = Fs, btype='highpass', analog=False)
    y = filtfilt(b, a, sig)
    return y

df = pd.read_csv("EMG_Data_0.csv")
df = df.to_numpy()

EMG = [i[2] for i in df]
time = [int(i[1].split(":")[2]) for i in df]
# time = [i[1] for i in df]
fs = time.count(time[time.count(time[0])])  #find the number of occurances of 
                                            #the same second value(taking second 
                                            # value because first value will be incomplete)

EMG = EMG - np.mean(EMG)
plt.plot(EMG)
plt.title("Raw Data")

lpf_EMG = butter_lowpass_filter(EMG,3, 4, fs)
# lpf_EMG = [i*10 for i in lpf_EMG]
bpf_EMG = butter_highpass_filter(lpf_EMG, 0.1, 4, fs)

# plt.figure()
plt.plot(bpf_EMG)
plt.title("BPF Data")

plt.figure()
bpf_EMG = [i/np.max(bpf_EMG) for i in bpf_EMG]
e_bpf_EMG = [np.exp(i) for i in bpf_EMG]

e_bpf_EMG = e_bpf_EMG - np.mean(e_bpf_EMG)

plt.plot(e_bpf_EMG)
plt.title("Exponential Data")

Gaussian_signal = gaussian_filter1d(e_bpf_EMG, 250)
Gaussian_signal = [i*10 for i in Gaussian_signal]
for i in range(len(Gaussian_signal)):
    if(Gaussian_signal[i] < 0):
        Gaussian_signal[i] = 0

peaks, _ = find_peaks(Gaussian_signal, threshold=0.0)
print("Number of Contractions: " + str(len(peaks)/2))

peakY = [Gaussian_signal[i] for i in peaks]

plt.plot(Gaussian_signal)
plt.plot(peaks, peakY, 'x')
plt.title("Gaussian Data")
plt.suptitle("Contractions: " + str(len(peaks)/2))

plt.show()