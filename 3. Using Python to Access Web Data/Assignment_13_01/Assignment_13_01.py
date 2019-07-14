# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 19:22:44 2019

@author: dk
"""

import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ')
data = urllib.request.urlopen(url).read()
info = json.loads(data)
info = info['comments']
print ('Retrieving', url, '\nRetrieved', len(data), 'characters', '\nCount:', len(info))
sum = 0
for item in info:
    sum += int(item['count'])
print ('Sum:', sum)