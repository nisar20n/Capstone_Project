# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 19:13:23 2020

@author: Nazibul
"""

import scipy.signal
import scipy.fftpack
import numpy as np
import matplotlib.pyplot as plt
from scipy import pi
from scipy.fftpack import fft


data=np.genfromtxt('Data 3.txt',delimiter=',')
Rx=data[1:,0]
Ry=data[1:,1]
Rz=data[1:,2]
avg1=np.mean(Rx,0)
avg2=np.mean(Ry,0)
avg3=np.mean(Rz,0)

x=len(Rz)
t = np.arange(x) /1024

#sample_rate = 18000
#N = sample_rate
#time = np.linspace(0, 1, N)

sample_rate = 1024
N = 2*sample_rate
time = np.linspace(0, 2, N)

freq1 = 60
magnitude1 = 25
freq2 = 270
magnitude2 = 2

waveform1 = magnitude1 * np.sin (2 * pi * freq1 * time)
waveform2 = magnitude2 * np.sin (2 * pi * freq2 * time)

noise = np.random.normal (0, 3, N)
time_data = waveform1 + waveform2 + noise

#plt.plot (t,Rz)
#plt.title ('Time Domain Signal')
#plt.xlabel ('Time')
#plt.ylabel ('Amplitude')
#plt.show ()

frequency = np.linspace (0.0, 1, np.fix(x/2))*512

freq_data = fft(Rz)
ha=len(frequency)
y = np.abs (freq_data [0:ha])/x
#frequency = np.linspace (0.0, 512, int (N/2))
#
#freq_data = fft(Rx)
#y = 2/N * np.abs (freq_data [0:np.int (N/2)])
plt.plot(frequency, y)
plt.title('Frequency domain Signal')
plt.xlabel('Frequency in Hz')
plt.ylabel('Amplitude')
plt.show()