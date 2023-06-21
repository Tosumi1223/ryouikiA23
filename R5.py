# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 15:23:05 2023

@author: tossu
"""

import tkinter as tk

root = tk.Tk()
root.geometry("1000x500")

canvas = tk.Canvas(root, bg = "white")
canvas.pack(fill = tk.BOTH, expand = True)

canvas.create_oval(100, 100, 200, 200, width = 3, tag = "person")
canvas.create_line(150, 200, 150, 300, width = 3, tag = "person")
canvas.create_line(150, 250, 75, 225, width = 3, tag = "person")
canvas.create_line(150, 250, 225, 225, width = 3, tag = "person")
canvas.create_line(150, 300, 75, 350, width = 3, tag = "person")
canvas.create_line(150, 300, 225, 350, width = 3, tag = "person")

def move():
    canvas.move("person",5, 0)
    canvas.after(100,move)
    
move()

root.mainloop()