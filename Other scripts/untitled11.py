# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 04:20:21 2020

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
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter
import tkinter as tk
import numpy as np
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

class MyClass:
    def __init__(self, frame):
        self.frame = frame
        self.fig = Figure(figsize=(10, 6), dpi=100)
        self.haga=haga
        self.ax = self.fig.add_subplot(111)
#        self.ay = self.fig.add_subplot(211)
        self.canvas = FigureCanvasTkAgg(self.fig, self.frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tkinter.RIGHT)
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
        toolbar = NavigationToolbar2Tk(self.canvas, self.frame)
        toolbar.update()
        self.canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)
#        self.hello=int(pasa)
#        self.pl=(self.hello,2,haga)
#        self.filters(*self.pl)
        self.va = StringVar(root1, "0") 
        self.valuese = {"Time Plot" : "1", 
          "Frequency Plot" : "2", 
          "Filter Selection" : "3", 
          "Filtered Data" : "4", 
          "Complementary Filter" : "5"} 
        def ShowChoice():
            global poi
            poi =int(self.va.get())
            if poi==1:
                print(poi)
                self.plot_graph()
            if poi==2:
                print(poi)
                self.plot_graph1()
    
            
        for (text, value) in self.valuese.items(): 
            Radiobutton(root1, text = text, variable = self.va, command=ShowChoice,value = value, indicator = 0, background = "light blue").pack(side=tk.LEFT,before=toolbar,anchor=N)
        
#        self.button = tkinter.Button(self.frame, text="plot", command=self.plot_graph)
#        self.button.pack()
#    def filters(p,q,r):
#        global sos
#        global filtered
#        sos = signal.butter(p,q,r, fs=1024, output='sos')
#        filtered = signal.sosfilt(sos, Rx)
    def plot_graph(self):
        self.ax.cla()
        self.ax.plot(t,Rx)
#        self.ay.cla()
        self.ax.plot(t,filtered)
        self.canvas.draw()
        
    def plot_graph1(self):
        self.ax.cla()
        self.ax.plot(t, Ry)
        self.canvas.draw()
            
#        if pagu==1:
#            self.ax.cla()
#            self.ax.plot(t, Rz)
#            self.canvas.draw()

def show_data():
    print("hello")
    global pasa
    global haga
    global sos
    global filtered
    txt.delete('0.0','end')
    pasa=entry.get()
    haga=var.get()
    sos=0
    print(haga)
    if haga==1:
        haga='lp'
        melt="Low Pass Filter"
    else:
        haga='hp'
        melt="High Pass Filter"
    
    sentence="Hello,You have chosen a "+melt+" with a cut off frequency of "+pasa+" Hz.";
    txt.insert(0.0,sentence);
    hello=int(pasa)
  
    sos =signal.butter(10,hello,haga, fs=80, output='sos')
    filtered = signal.sosfilt(sos, Rx)
    
    

  
root1 = tkinter.Tk()
label1=tk.Label(root1,justify=tk.CENTER, text="Cut off Frequency")
#label2=tk.Label(root1,text="Filter Type")
entry=Entry(root1)
var=IntVar() 
rd1=Radiobutton(root1,text="Lp",variable=var,value=1)
rd2=Radiobutton(root1,text="Hp",variable=var,value=2)


label1.pack(side=tk.LEFT,padx=5,expand=True,anchor=N)
entry.pack(side=tk.LEFT,padx=5,expand=True,anchor=N)
rd1.place(relx=0, x=30, y=20, anchor=N)
rd2.place(relx=0, x=100, y=20, anchor=N)

btn=Button(root1,text="APPLY",bg="purple",fg="white",command=show_data)
btn.pack(side=tk.LEFT,padx=5,expand=True,anchor=N)

txt=Text(root1,width=25,height=10,wrap=WORD)
txt.place(relx=0, x=100, y=100, anchor=N)
global haga
global pasa
global filtered
haga=0
pasa=0

data=np.genfromtxt('angle_test2.txt',delimiter=',')
Rx=data[1:,0]
Ry=data[1:,1]
Rz=data[1:,2]
avg1=np.mean(Rx,0)
avg2=np.mean(Ry,0)
avg3=np.mean(Rz,0)
x=len(Rx)
t = np.arange(x) /1000
MyFrame = tkinter.Frame(root1)
MyClass(MyFrame)
MyFrame.pack()
root1.mainloop()