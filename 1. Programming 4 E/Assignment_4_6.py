# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 20:01:06 2019

@author: dk
"""

hrs = input("Enter Hours:")
rate = input("Enter rate:")

h = float(hrs)
r=float(rate)

def computepay(h,r):
    if h > 40:
        req = r * h
        otp = (h-40) * (r * 0.5)
        pay = req + otp
    else :
        pay= r * h
    return pay

print(computepay(h,r))