# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 15:23:23 2023

@author: tossu
"""

with open('data.txt', 'r') as f:

    sum = 0

    for line in f:
        try:
            sum = sum + int(line)
        except ValueError:
            pass
          
    print(sum)