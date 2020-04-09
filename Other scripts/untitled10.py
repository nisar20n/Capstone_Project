import tkinter
import tkinter as tk

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np


class Application(tk.Frame):
    def say_hi(self):
        print("hi there, everyone!")
        
    def __init__(self, frame):

        # Matplotlib ##################

#        self.fig = plt.figure(figsize=(8.0, 8.0))
        self.haga=1
        self.gaga=1
        if self.haga==1:
            self.fig = Figure(figsize=(5, 4), dpi=100)
            self.fig.add_subplot(111).plot(t, Ry)
            self.root = master
            self.fig.clear
            self.root.protocol("WM_DELETE_WINDOW", self.on_tl_close)
            self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
            self.canvas.get_tk_widget().pack(fill="both", expand=True)
            toolbar = NavigationToolbar2Tk(self.canvas, self.root)
            toolbar.update()
            self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
            self.canvas.draw()
            
        if self.gaga==1:
            self.root.protocol("WM_DELETE_WINDOW", self.on_tl_close)
            self.root.update
            self.fig = Figure(figsize=(5, 4), dpi=100)
            self.fig.add_subplot(141).plot(t, Ry)
            self.root = master
            
            self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
            self.canvas.get_tk_widget().pack(fill="both", expand=True)
            toolbar = NavigationToolbar2Tk(self.canvas, self.root)
            toolbar.update()
            self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
            self.canvas.draw()
    def on_tl_close(self, *args):
        self.root.destroy()
#        self.root= None
root = tk.Tk()
root.wm_title("Embedding in Tk")
var=IntVar()
rd1=Radiobutton(root,text="Lp",variable=var,value=1)
rd2=Radiobutton(root,text="Hp",variable=var,value=2)
rd1.pack(side=tkinter.TOP)
rd2.pack(side=tkinter.TOP)
label1=Label(root,text="Cut off Frequency")
label2=Label(root,text="Filter Type")
button = tkinter.Button(master=root, text="Quit", command=show_data)
button.pack(side=tkinter.BOTTOM)
entry=Entry(root)
entry.pack(side=tkinter.BOTTOM)
label1.pack(side=tkinter.TOP)
label2.pack(side=tkinter.TOP)
app = Application(root)
root.mainloop()
        