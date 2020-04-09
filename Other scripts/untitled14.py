# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 03:41:39 2020

@author: Nazibul
"""

import tkinter as tk
from PIL import ImageTk, Image

#This creates the main window of an application
window = tk.Tk()



window.after(5000, lambda: window.destroy()) 
label_one = tk.Label(window, justify=tk.LEFT,
              padx = 10,text = 'Welcome to Acceleration Avionics Performance Analysis Tool')

label_two = tk.Label(window, justify=tk.LEFT,
              padx = 10,text = 'Developed by Mohammad Nazibul Hassan ')
label_one.pack(side=tk.TOP,anchor=N)
label_two.pack(side=tk.TOP,anchor=N)
geo=window.geometry
geo("1500x1000+0+0")
window['bg'] = 'gray85'
window.wm_title("Hola!")
label_one.config(font=("Courier", 30))
label_two.config(font=("Courier", 30))
path = "acc.jpg"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "bottom",after=label_one, expand = "yes")

#Start the GUI
window.mainloop()