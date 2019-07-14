# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 17:08:25 2019

@author: dk
"""

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r=float(rate)
if h > 40:
    req = r * h
    otp = (h-40) * (r * 0.5)
    pay = req + otp
else :
    pay= r * h
print(pay)