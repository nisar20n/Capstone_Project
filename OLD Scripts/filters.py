# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:43:18 2020

@author: Nazibul
"""
import scipy.signal
import scipy.fftpack
import numpy as np
import matplotlib.pyplot as plt
from scipy import pi
from scipy import signal
from scipy.fftpack import fft


#data=np.genfromtxt('Data 3.txt',delimiter=',')
#Rx=data[1:,0]
#Ry=data[1:,1]
#Rz=data[1:,2]
#avg1=np.mean(Rx,0)
#avg2=np.mean(Ry,0)
#avg3=np.mean(Rz,0)
#
#x=len(Rx)
#t = np.arange(x) /1000
#
#t = np.linspace(0, 1, 1000, False)  # 1 second
#sig = np.sin(2*np.pi*10*t) + np.sin(2*np.pi*20*t)
#fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
#ax1.plot(t, sig)
#ax1.set_title('10 Hz and 20 Hz sinusoids')
#ax1.axis([0, 1, -2, 2])

sos = signal.butter(10,5, 'lp', fs=1000, output='sos')
filtered = signal.sosfilt(sos, Rx)

sos1 = signal.butter(10, 5, 'lp', fs=1000, output='sos')
filtered1 = signal.sosfilt(sos1, Ry)

sos2 = signal.butter(10, 5, 'lp', fs=1000, output='sos')
filtered2 = signal.sosfilt(sos2, Rz)

frequency = np.linspace(0, 1, np.fix(x/2))*500
freq_data = fft(filtered)
ha=len(frequency)
k=np.abs (freq_data)/x
y = np.abs (freq_data [0:ha])/x

frequency1 = np.linspace(0, 1, np.fix(x/2))*500

freq_data1 = fft(filtered1)
ka=len(frequency1)
k=np.abs (freq_data1)/x
z = np.abs (freq_data1 [0:ka])/x
#
frequency2 = np.linspace(0, 1, np.fix(x/2))*500
freq_data2 = fft(filtered2)
la=len(frequency2)
k=np.abs (freq_data2)/x
m = np.abs (freq_data2 [0:la])/x

plt.figure(1)
plt.plot(t,Rx,"b-*",label='Unfiltered Data')
plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.minorticks_on()
plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.xlabel('time')
plt.ylabel('Rx')

plt.figure(2)
plt.plot(t,filtered,"b-*",label='Unfiltered Data')
plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.minorticks_on()
plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.xlabel('time')
plt.ylabel('Rx')



plt.figure(3)
plt.plot(t,Ry,"b-*")
plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.minorticks_on()
plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.xlabel('time')
plt.ylabel('Ry')

plt.figure(4)
plt.plot(t,filtered1,"b-*")
plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.minorticks_on()
plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.xlabel('time')
plt.ylabel('Ry')

plt.figure(5)
plt.plot(t,Rz,"b-*")
plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.minorticks_on()
plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.xlabel('time')
plt.ylabel('Rz')

plt.figure(6)
plt.plot(t,filtered2,"b-*")
plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.minorticks_on()
plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.xlabel('time')
plt.ylabel('Rz')

plt.figure(7)
plt.plot(frequency, y)
plt.title('Frequency domain Signal')
plt.xlabel('Frequency in Hz for Rx')
plt.ylabel('Amplitude')

plt.figure(8)
plt.plot(frequency1, z)
plt.title('Frequency domain Signal')
plt.xlabel('Frequency in Hz for Ry')
plt.ylabel('Amplitude')
#
plt.figure(9)
plt.plot(frequency1, m)
plt.title('Frequency domain Signal')
plt.xlabel('Frequency in Hz for Rz')
plt.ylabel('Amplitude')
plt.show()
#b, a = signal.butter(10, 100, 'low', analog=True)
#w, h = signal.freqs(b, a)
#plt.semilogx(w, 20 * np.log10(abs(h)))
#plt.title('Butterworth filter frequency response')
#plt.xlabel('Frequency [radians / second]')
#plt.ylabel('Amplitude [dB]')
#plt.margins(0, 0.1)
#plt.grid(which='both', axis='both')
#plt.axvline(100, color='green') # cutoff frequency
#plt.show()