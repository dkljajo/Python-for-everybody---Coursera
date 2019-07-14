# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 19:11:51 2019

@author: dk

Assignment 6.5
"""

text = "X-DSPAM-Confidence:    0.8475";
ipos= text.find(':')
piece= text[ipos+1:]
value=float(piece)
print(value)