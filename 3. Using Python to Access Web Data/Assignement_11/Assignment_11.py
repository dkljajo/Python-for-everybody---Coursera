# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 19:09:22 2019

@author: dk

The sum for the sample text above is 27486. 
The numbers can appear anywhere in the line. 
There can be any number of numbers in each line (including none).
Handling The Data
The basic outline of this problem is to read the file, 
look for integers using the re.findall(), looking for a 
regular expression of '[0-9]+' and then converting the extracted strings 
to integers and summing up the integers.
"""


import re


fname = input("Enter file name: ")
if len(fname) < 1 : fname = "regex_sum_42.txt"

fhandle = open(fname)

total = 0

for line in fhandle:
    listOfNums = re.findall('([0-9]+)', line.rstrip())
    for snum in listOfNums :
        total = total + int(snum)
print(total)
