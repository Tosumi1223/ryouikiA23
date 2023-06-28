# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 16:08:35 2023

@author: tossu
"""

import json
import tkinter as tk

root = tk.Tk()
root.geometry("1920x1080")

canvas = tk.Canvas(root, bg = "white")
canvas.pack(fill = tk.BOTH, expand = True)

with open("./kabeposter/kabeposter/kabeposter_000000000000_keypoints.json","r") as f:
    j = json.load(f)
    
x1 = []
x2 = []
y1 = []
y2 = []
c1 = []
c2 = []

for i in range(0,75,3):
    x1.append(j['people'][0]["pose_keypoints_2d"][i])
    x2.append(j['people'][1]["pose_keypoints_2d"][i])
for i in range(1,75,3):
    y1.append(j['people'][0]["pose_keypoints_2d"][i])
    y2.append(j['people'][1]["pose_keypoints_2d"][i])
for i in range(2,75,3):
    c1.append(j['people'][0]["pose_keypoints_2d"][i])
    c2.append(j['people'][1]["pose_keypoints_2d"][i])
    
canvas.create_line(x1[1], y1[1], x1[2], y1[2], width = 3, tag = "person")
canvas.create_line(x1[1], y1[1], x1[5], y1[5], width = 3, tag = "person")
canvas.create_line(x2[1], y2[1], x2[2], y2[2], width = 3, tag = "person")
canvas.create_line(x2[1], y2[1], x2[5], y2[5], width = 3, tag = "person")



root.mainloop()