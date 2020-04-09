# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 00:34:38 2020

@author: Nazibul
"""
import scipy.signal
import scipy.fftpack
import numpy as np
import matplotlib.pyplot as plt
from scipy import pi
from scipy.fftpack import fft

timestep=1./1000.#Assume sampling at 50Hz. Change this accordingly.
N=9999#the number of samples
T=N*timestep
t = np.linspace(0,T,N)#needed only to generate xAcc_synthetic
#freq=2.#peak a frequency at 2Hz
#generate synthetic signal at 2Hz and add some noise to it
xAcc_synthetic = np.sin((2*np.pi)*freq*t)+np.random.rand(N)*0.2
sp_synthetic = np.fft.fft(Rx)/x
freq = np.fft.fftfreq(t.size,d=timestep)
#print max(abs(freq))==(1/timestep)/2.#simple check highest freq.
plt.plot(freq, abs(sp_synthetic))
plt.xlabel('Hz')