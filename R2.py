# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 15:32:41 2023

@author: tossu
"""

import json

with open('catalog.json', 'r') as f:
    j = json.load(f)
    
price = []

for data in j:
    if data["name"] == "jacket":
        price.append(int(data["price"]))
        
print("jacketの個数:%d" %len(price))
print("jacketの最高価格:%d" %max(price))
print("jacketの最低価格:%d" %min(price))

        
    