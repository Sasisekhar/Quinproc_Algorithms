# Quinproc Algorithms
This repository contains all the algorithms pertaining to the Wireless Maternal Monitoring device/ Medical Data Acquisition Unit (MDAQ) and the basic python scripts that helped develop the same.

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

## EMG Testing
This folder contains the script, [Serial2txt.py](https://github.com/Sasisekhar/Quinproc_Algorithms/blob/main/EMG%20testing/Serial2txt.py), to collect EMG data from MDAQ when programmed with the firmware serialEMG.ino provided [here](https://github.com/Sasisekhar/serialEMG.git). This script collects the serial EMG data (ensure the serial port is selected correctly) and saves the same as a CSV file, whose name iterates from 0 to N. Further, a date and time stamp is also recorded in the CSV file.

## Heartrate_testing
This folder contains the script, [UDP2BPM_CSV_WAV.py](https://github.com/Sasisekhar/Quinproc_Algorithms/blob/main/Heartrate_Testing/UDP2BPM_CSV_WAV.py), to collect the microphone data from MDAQ when programmed with the firmware provided [here](https://github.com/Sasisekhar/Quinproc_QCU_Firmware.git). Currently (as of 12th June 2023) this script only supports data collection from **ONE** microphone. This script collects UDP data packets while listening to a pre-defined IP address and Port. The script initially provides 5 seconds of raw audio which can be used to ensure optimal positioning of the microphone. Once, confirmed, the script records data for one minute, calculates the BPM, plots various relevant graphs and updates the same in the cloud. Along with this, the raw data is stored as a CSV and the final filtered audio is saved as a WAV file.