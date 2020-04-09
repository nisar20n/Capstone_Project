# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 06:11:54 2020

@author: Nazibul
"""


import numpy as np
import matplotlib.pyplot as plt
import decimal
import csv
import scipy.signal
from scipy import pi
from scipy.fftpack import fft
from mpl_toolkits.mplot3d import axes3d
import scipy.fftpack


sos = signal.butter(10, 1, 'lp', fs=1000, output='sos')
filtered = signal.sosfilt(sos, Rx)

sos = signal.butter(10, 1, 'lp', fs=1000, output='sos')
filtered1 = signal.sosfilt(sos, Ry)

sos = signal.butter(10, 1, 'lp', fs=1000, output='sos')
filtered2 = signal.sosfilt(sos, Rz)

#n_radii = 8
#n_angles = 36
#
## Make radii and angles spaces (radius r=0 omitted to eliminate duplication).
#radii = np.linspace(0.125, 1.0, n_radii)
#angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)
#
## Repeat all angles for each radius.
#angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
#X,Y,Z=[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]
## Convert polar (radii, angles) coords to cartesian (x, y) coords.


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.random.standard_normal(100)
y = np.random.standard_normal(100)
z = np.random.standard_normal(100)
c = np.random.standard_normal(100)

img = ax.scatter(t, filtered, filtered1, c=filtered2, cmap=plt.hot())
fig.colorbar(img)
plt.show()

plt.show()