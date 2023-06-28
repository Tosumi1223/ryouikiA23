# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 15:49:26 2023

@author: tossu
"""

import json

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

print("1人目の鼻のx座標:", x1[0])
print("1人目の鼻のy座標:", y1[0])
print("1人目の鼻の信頼度:", c1[0])
print("2人目の鼻のx座標:", x2[0])
print("2人目の鼻のy座標:", y2[0])
print("2人目の鼻の信頼度:", c2[0])
print("1人目の首のx座標:", x1[1])
print("1人目の首のy座標:", y1[1])
print("1人目の首の信頼度:", c1[1])
print("2人目の首のx座標:", x2[1])
print("2人目の首のy座標:", y2[1])
print("2人目の首の信頼度:", c2[1])
