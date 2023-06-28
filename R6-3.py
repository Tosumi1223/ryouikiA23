# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 16:08:35 2023

@author: tossu
"""

import json
import tkinter as tk
import glob
import os
import time


root = tk.Tk()
root.geometry("1920x1080")

canvas = tk.Canvas(root, bg = "white")
canvas.pack(fill = tk.BOTH, expand = True)

path = "./kabeposter/kabeposter"
os.chdir(path)
filej = glob.glob("*.json")
link = [[0,15],[15,17],[0,16],[16,18],[0,1],[1,2],[2,3],[3,4],[1,5],[5,6],[6,7],[1,8],[8,9],[9,10],[10,11],[11,24],[11,22],[22,23],[8,12],[12,13],[13,14],[14,21],[14,19],[19,20]]

def draw(x,y):
    for l in link:
        if x[l[0]] != 0 and y[l[0]] != 0 and x[l[1]] != 0 and y[l[1]] != 0:       
            canvas.create_line(x[l[0]], y[l[0]], x[l[1]], y[l[1]], width = 3, tag = "person")

def move():
    canvas.delete("person")
    
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
    draw(x1, y1)
    draw(x2, y2)
    time.sleep(0.05)
    root.update()
   

for file in filej:
    with open(file,"r") as f:
        j = json.load(f)
        
    move()

root.mainloop()
