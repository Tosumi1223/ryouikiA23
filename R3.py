# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 15:46:57 2023

@author: tossu
"""

import zipfile
import glob

with zipfile.ZipFile("sample.zip", "r") as zf:
    zf.extractall()
    
    files = glob.glob("./sample/*[13579]_*")
    sum = 0
    
    for file in files:
        with open(file,"r") as f:
            sum = sum + int(f.read())
            
    print(sum)
    