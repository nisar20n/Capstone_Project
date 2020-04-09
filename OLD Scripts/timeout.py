# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:52:21 2020

@author: Nazibul
"""

import tkinter as tk

w = tk.Tk()
w.after(5000, lambda: w.destroy()) 
label_one = Label(w, justify=tk.LEFT,
              padx = 10,text = 'Welcome to Acceleration Avionics Performance Analysis Tool')

label_two = Label(w, justify=tk.LEFT,
              padx = 10,text = 'Developed by Mohammad Nazibul Hassan ')
label_one.grid(row=0)
label_two.grid(row=1)
geo=w.geometry
geo("1500x100+30+100")
w['bg'] = 'light sky blue'
w.wm_title("Hola!")

label_one.config(font=("Courier", 30))
label_two.config(font=("Courier", 30))
w.mainloop()