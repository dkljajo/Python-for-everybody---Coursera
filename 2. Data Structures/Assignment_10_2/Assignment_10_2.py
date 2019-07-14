# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 13:54:27 2019

@author: dk

10.2 Write a program to read through the mbox-short.txt 
and figure out the distribution by hour of the day for each of the messages. 
You can pull the hour out from the 'From ' line by finding the time and 
then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, 
print out the counts, sorted by hour as shown below.
"""

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

di = dict()

for line in handle:
    line = line.rstrip()
    if not line.startswith ('From '):
        continue
    wds=line.split()
    time=wds[5]
    hours=time.split(':')
    hour=hours[0]
    if hour in di:
        di[hour]=di[hour]+1
    else:
        di[hour]=1
        
tmp = list()  

tmp= sorted(di.items())
    
for k,v in tmp:
    print(k,v)