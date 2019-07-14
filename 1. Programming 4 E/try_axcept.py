# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 17:04:14 2019

@author: dk
"""

rawstr = input('Enter a number:')
try:
    ival = int(rawstr)
except:
    ival=-1
if ival>0:
    print('Nice work')
else:
    print('Not a number')