# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 15:29:33 2023

@author: tossu
"""

from ultralytics import YOLO
import cv2
import numpy as np

cap = cv2.VideoCapture(r"sample.mp4")
totalframecount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

model = YOLO("yolov8x.pt")
results = model("sample.mp4", save=True, save_txt=True, save_conf=True)

rec = np.zeros(len(results[0].names))
output = {}

for i in range(totalframecount):
  boxes = results[i].boxes
  for box in boxes:
    if rec[int(box.data[0][5].item())] == 0:
      rec[int(box.data[0][5].item())] = 1

for j in range(len(rec)):
  if rec[j] == 1:
    output[j] = results[0].names[j]

print(output)