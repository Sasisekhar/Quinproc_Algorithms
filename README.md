# Quinproc Algorithms
This repository contains all the algorithms pertaining to the Wireless Maternal Monitoring device and the basic python scripts that helped develop the same.

The structure and contents of the repository is explained herewith. Further explanation regarding the working of the code is provided in the form of comments.

## Repository structure

```cpp
│
├── EMG Testing
│   ├── Serial2txt.py
│   ├── EMG_Data_0.csv
│   ⋮
│   └── EMG_Data_N.csv //N --> Number of samples
├── Heartrate_testing
│   ├── UDP2BPM_CSV_WAV.py
│   ├── audioData_Backend_0.csv
│   ⋮
│   ├── audioData_Backend_N.csv
│   ├── Backend_Audio_0.wav
│   ⋮
│   └── Backend_Audio_N.wav
├── Fundamental algorithms
│   ├── CSV2Heartrate_Cleaned.py
│   ├── CSV2Heartrate.py
│   ├── sampleData.py
│   ├── sound_analyze.py
│   ├── UDP_Audio_CSV.py
│   ├── UDP_Audio.py
│   ├── UDP_CSV.py
│   ├── UDP_FFT.py
│   ├── UDP_Plot.py
│   ├── UDP_Print.py
│   └── UDP_send_test.py
├── CSV_EMG.py
└── Server_Processing_Script.py
```