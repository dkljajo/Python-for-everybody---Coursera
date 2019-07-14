# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 11:48:07 2019

@author: dk
"""

import urllib.request
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, "lxml")

# Retrieve all of the 'span' tags
tags = soup.findAll('span', { "class":"comments" })

count = 0
sum = 0
for tag in tags:
    # Look at the parts of a tag
    num = tag.text
    sum = sum + int(num)
    count += 1

print ('Count', count)
print ('Sum', sum)