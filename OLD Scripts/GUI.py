# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 17:42:50 2020

@author: Nazibul
"""
import scipy.signal
import scipy.fftpack
import numpy as np
import matplotlib.pyplot as plt
from scipy import pi
from scipy import signal
from scipy.fftpack import fft
from tkinter import *
import tkinter as tk
def show_data():
    global pasa
    global haga
    global kada
    txt.delete('0.0','end')
    pasa=entry.get()
    kada=entry1.get()
    haga=var.get()
    if haga==1:
        haga='lp'
        melt="Low Pass Filter"
    else:
        haga='hp'
        melt="High Pass Filter"
    
    sentence="Hello,You have chosen a "+melt+" with a cut off frequency of "+pasa+" Hz."+"with a order of" +kada;
    txt.insert(0.0,sentence);

global jhuta
jhuta='abnormal'   

if jhuta=='abnormal':
    root= Tk()
    jhuta=root.state()
root.geometry("300x350")
label1=tk.Label(root,justify=tk.LEFT,
              padx = 10, text="Cut off Frequency")
label2=Label(root,text="Filter Type")
entry=Entry(root)
entry1=Entry(root)

var=IntVar()
rd1=Radiobutton(root,text="Lp",variable=var,value=1)
rd2=Radiobutton(root,text="Hp",variable=var,value=2)

label1.grid(row=0)
label2.grid(row=1)
entry.grid(row=0,column=1)
entry1.grid(row=4,column=1)
rd1.grid(row=1,column=1,sticky=W)
rd2.grid(row=1,column=1,sticky=S)
btn=Button(root,text="APPLY",bg="purple",fg="white",command=show_data)
btn.grid(row=2,columnspan=2)
txt=Text(root,width=25,height=10,wrap=WORD)
txt.grid(row=3,columnspan=2,sticky=W)
#label1.pack()
#label2.pack()
root.mainloop()


data=np.genfromtxt('Data_4_Stationary.txt',delimiter=',')
Rx=data[1:,0]
Ry=data[1:,1]
Rz=data[1:,2]
avg1=np.mean(Rx,0)
avg2=np.mean(Ry,0)
avg3=np.mean(Rz,0)

x=len(Rx)
t = np.arange(x) /1024
#
#t = np.linspace(0, 1, 1000, False)  # 1 second
#sig = np.sin(2*np.pi*10*t) + np.sin(2*np.pi*20*t)
#fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
#ax1.plot(t, sig)
#ax1.set_title('10 Hz and 20 Hz sinusoids')
#ax1.axis([0, 1, -2, 2])

def filters(p,q,r):
    global sos
    global filtered
    sos = signal.butter(p,q,r, fs=1024, output='sos')
    filtered = signal.sosfilt(sos, Rx)

hello=int(pasa)
pl=(hello,2,haga)
filters(*pl)
#w=(10,100,'lp')
#filters(*w)


#frequency = np.linspace (0.0, 1, np.fix(x/2))*512
#
#freq_data = fft(Rx)
#ha=len(frequency)
#y = np.abs (freq_data [0:ha])/x

frequency = np.linspace(0, 1, np.fix(x/2))*512

freq_data = fft(filtered)
ha=len(frequency)
p= np.abs (freq_data [0:ha])/x


plt.figure(1)
plt.title('Rx Plot Before Filtering')
plt.plot(t,Rx,"b-*")
plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.minorticks_on()
plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.xlabel('time')
plt.ylabel('Rx')

plt.figure(2)
plt.title('Rx Plot AFter Filtering')
plt.plot(t,filtered,"b-*")
plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.minorticks_on()
plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.xlabel('time')
plt.ylabel('Rx')

#plt.figure(3)
#plt.plot(frequency, y)
#plt.title('Frequency domain Signal Before Filtering')
#plt.xlabel('Frequency in Hz')
#plt.ylabel('Amplitude')
#
#plt.figure(4)
#plt.plot(frequency, p)
#plt.title('Frequency domain Signal After Filtering')
#plt.xlabel('Frequency in Hz for Rx')
#plt.ylabel('Amplitude')

plt.show()
