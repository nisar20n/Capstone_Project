import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np


root = tkinter.Tk()
root.wm_title("Embedding in Tk")
var=IntVar()
rd1=Radiobutton(root,text="Lp",variable=var,value=1)
rd2=Radiobutton(root,text="Hp",variable=var,value=2)
global jina
kappu=1
pappu=2
v = StringVar(root, "1") 
values = {"Time Plot" : "1", 
          "Frequency Plot" : "2", 
          "Filter Selection" : "3", 
          "Filtered Data" : "4", 
          "Complementary Filter" : "5"} 
def ShowChoice():
    global po
    po =int(v.get())
    if po==1:
        my_function()
    if po==2:
        my_function1()
    
            
for (text, value) in values.items(): 
        Radiobutton(root, text = text, variable = v, command=ShowChoice,value = value, indicator = 0, background = "light blue").pack(side=tkinter.TOP)

def my_function():
    jina=1
    jina=jina+1
    print(kappu)
    fig = Figure(figsize=(10, 5), dpi=100)
    fig.add_subplot(111).plot(t, Rx)
    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    toolbar.pack()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    
rd1.pack(side=tkinter.TOP)
rd2.pack(side=tkinter.TOP)
label1=Label(root,text="Cut off Frequency")
label2=Label(root,text="Filter Type")
button = tkinter.Button(master=root, text="Quit", command=my_function)
button.pack(side=tkinter.BOTTOM)
entry=Entry(root)
entry.pack(side=tkinter.BOTTOM)
label1.pack(side=tkinter.TOP)
label2.pack(side=tkinter.TOP)
guggu=var.get()
#if kappu==1:
#    my_function()
#if pappu==2:
#    my_function1()

fig = Figure(figsize=(5, 4), dpi=100)

fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))
#
canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
#canvas.draw()
#canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
#
#toolbar = NavigationToolbar2Tk(canvas, root)
#toolbar.update()
#canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)




def my_function1():
  print("Hello from a function")
  fig = Figure(figsize=(5, 4), dpi=100)
  fig.add_subplot(111).plot(t, Ry)
  canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea
  canvas.draw()
  canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
  toolbar = NavigationToolbar2Tk(canvas, root)
  toolbar.update()
  canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)
def show_data():
    global pasa
    global haga
    global fig
    pasa=entry.get()
    haga=var.get()
    
    print("Hello from a function")
    fig = Figure(figsize=(5, 4), dpi=100)
    ax=fig.add_subplot(111)
    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingAre
    canvas.draw()
    fig.canvas.get_tk_widget().update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
    if haga==1:
        ax.cla()
        ax.plot(t,Rx)
        canvas.draw()
    if haga==2:
        ax.cla()
        ax.plot(t,Ry)
        canvas.draw()
        
    
#   
#
def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


tkinter.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.