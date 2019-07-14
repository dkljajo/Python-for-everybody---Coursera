# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 17:30:39 2019

@author: dk


"""

num=0
tot=0.0

while True:
    sval=input('Enter a number: ')
    if sval=='done':
        break
    try:
        fval=float(sval)
    except:
        print('Invalid input!')
    num=num+1
    tot=tot+fval
    
print (tot, num, tot/num)