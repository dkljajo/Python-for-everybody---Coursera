# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 21:04:02 2019

@author: dk

9.4 Write a program to read through the mbox-short.txt 
and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines 
as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address 
to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary 
using a maximum loop to find the most prolific committer.
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
    email=wds[1]
    if email in di:
        di[email]=di[email]+1
    else:
        di[email]=1
    
#find most common e-mail
theword=None
largest=-1
for k,v in di.items():
    if v>largest:
        largest=v
        theword=k
        
print(theword, largest)
