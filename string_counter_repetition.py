# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 10:17:41 2026

@author: INAKUSHW
"""

str1 = '1a2b3c5e'

# O/p = 'abbccceeeee'

s = ''
for i in range(len(str1)-1):
    # print(str1[i])
    try:
        int(str1[i])
        # print(str1[i], 'is an integer')
        for j in range(int(str1[i])):
            s+=str1[i+1]
    except:
        pass

#Multidigit
str1 = '12a2b3c5e'
s = ''
num = ''
for ch in str1:
    if ch.isdigit():
        num+=ch
    else:
        s += ch*int(num)
        num = ''
    