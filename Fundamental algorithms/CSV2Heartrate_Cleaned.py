import matplotlib.pyplot as plt
import math
import numpy as np
import pandas as pd
from scipy.signal import find_peaks
from scipy.signal import butter, filtfilt
from scipy.fft import fft, fftfreq
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



y = pd.read_csv("audioData_Backend_9.csv")
y = y.to_numpy()
y = [i[0] for i in y]
# y = y[16000:-16000]
x = [i for i in range(len(y))]


N = len(y)
T = 1.0/8000.0

yf_prev = fft(y)
xf_prev = fftfreq(N, T)[:N//2]

lpf_y = butter_lowpass_filter(y, 150, 7, 8000)
bpf_y = butter_highpass_filter(lpf_y, 30, 7, 8000)

bpf_y = [10*i for i in bpf_y]
bpf_y = np.array(bpf_y)

yf = fft(bpf_y)
xf = fftfreq(N, T)[:N//2]

minY = min(bpf_y)
posY = [(i + (minY * -1) + 1.0) for i in bpf_y]

log_y = [math.log(i) for i in posY]

# minY = min(log_y)
# negY = [(i - minY) for i in log_y]

lpf_log_y = butter_lowpass_filter(log_y, 50, 7, 8000)

e_lpf_log_y = [math.exp(i) for i in lpf_log_y]


yf_after = fft(e_lpf_log_y)
xf_after = fftfreq(N, T)[:N//2]

meanY = sum(e_lpf_log_y)/len(e_lpf_log_y)
medianY = sorted(e_lpf_log_y)[(len(e_lpf_log_y) - 1)//2]
normalized_data = [(i - meanY)/medianY for i in e_lpf_log_y]

yf_norm = fft(normalized_data)
xf_norm = fftfreq(N, T)[:N//2]

Gaussian_signal = gaussian_filter1d(normalized_data, 500)

Gaussian_signal = [-1*i for i in Gaussian_signal]

yf_gauss = fft(Gaussian_signal)
xf_gauss = fftfreq(N, T)[:N//2]

# threshold_height = sorted(Gaussian_signal)[math.ceil((len(Gaussian_signal)-1)/2)]
threshold_height = sum(Gaussian_signal)/len(Gaussian_signal)
peaks, _ = find_peaks(Gaussian_signal) #Take initial height to be mean

peakPltY = []
peakPltX = []
for i in range(len(peaks)):
    peakPltY.append(Gaussian_signal[peaks[i]])
    peakPltX.append(x[peaks[i]])

BPM = (len(peaks)/(2.0*len(Gaussian_signal)/8000.0))*60.0

print("BPM: ", BPM)

fig = plt.figure()
fig.suptitle("Peaks, Heartrate = %f BPM" % BPM, fontsize=15)
plt.plot(x, Gaussian_signal)
plt.plot(peakPltX, peakPltY,'x')
plt.plot([threshold_height for i in range(len(x))], linestyle = '--')

rows = 3
columns = 1

fig1 = plt.figure()
fig1.suptitle("Time Domain Signals", fontsize=15)
ax1 = fig1.add_subplot(rows,columns,1)
ax2 = fig1.add_subplot(rows,columns,2)
ax3 = fig1.add_subplot(rows,columns,3)

ax1.title.set_text("After BPF")
ax2.title.set_text("After Normalization")
ax3.title.set_text("After Gaussian")

# ax1.plot(x[16000:64000], bpf_y[16000:64000])
# ax2.plot(x[16000:64000], normalized_data[16000:64000])
# ax3.plot(x[16000:64000], Gaussian_signal[16000:64000])

ax1.plot(x, bpf_y)
ax2.plot(x, normalized_data)
ax3.plot(x, Gaussian_signal)

fig2 = plt.figure()

plt.plot(xf_prev, 2.0/N * np.abs(yf_prev[0:N//2]), label = 'Before BPF')
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]), label = 'After BPF')
plt.plot(xf_norm, 2.0/N * np.abs(yf_norm[0:N//2]), label = 'After Normalization')
plt.plot(xf_gauss, 2.0/N * np.abs(yf_gauss[0:N//2]), label = 'After Gaussian')

plt.legend()
plt.grid()
plt.show()