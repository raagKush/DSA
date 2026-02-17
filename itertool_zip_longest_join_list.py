# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 08:43:29 2026

@author: INAKUSHW
"""

list1 = ['a','b','c','d','e']

list2 = [1,2,3]

list3 = ['f','g','h','i']

list4 = []

        
from itertools import zip_longest

for (a,b,c) in zip_longest(list1,list2,list3):
    print(a,b,c)
    
    s = ''
    
    if a is not None:
        s+=a
        
    if b is not None:
        s+=str(b)
        
    if c is not None:
        s+=c
        
    list4.append(s)
        