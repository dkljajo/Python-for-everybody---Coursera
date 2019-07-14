# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 19:22:02 2019

@author: dk
"""

score = input("Enter Score: ")
s=float(score)
if s >= 0.9:
    print("A")
elif s >= 0.8:
    print("B")
elif s >= 0.7:
    print("C")
elif s >= 0.6:
    print("D")
elif s < 0.6:
    print("F")
else:
    print("Error, your score is out of range!")
    quit()