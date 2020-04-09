# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 15:09:59 2020

@author: Nazibul
"""

import time
import numpy as np
import matplotlib.pyplot as plt
import decimal
import csv
from scipy import pi
from scipy.fftpack import fft
import pandas as pd
import numpy as np

rotor_radius=9.8
rpm_data=np.genfromtxt('4G_rpm_test3.txt',delimiter=',')
rpm=rpm_data[0:,0]

p_rpm= rpm[rpm < 350]

rpm_x=len(p_rpm)
tx = np.arange(rpm_x) /82

gr=0.00001118*9.8*np.square(p_rpm)



#plt.figure(10)
#plt.plot(tx,p_rpm,"b-*")
#
#plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
#         linestyle='-',linewidth=2)
#plt.minorticks_on()
#plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
#         linestyle='-',linewidth=2)
#plt.xlabel('time')
#plt.ylabel('Rx')
#
#plt.figure(11)
#plt.plot(tx,gr,"b-*")
#
#plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
#         linestyle='-',linewidth=2)
#plt.minorticks_on()
#plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
#         linestyle='-',linewidth=2)
#plt.xlabel('time')
#plt.ylabel('Rx')
