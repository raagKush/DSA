# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 08:52:17 2026

@author: INAKUSHW
"""

inputs =  [[1,3],[3,4],[5,7],[2,6],[8,10],[15,18]]

ip = sorted(inputs, key = lambda x:x[0])

op = [ip[0]]

j = 1

while j< len(ip):
    if(op[-1][1]>=ip[j][0]):
        print('overlap detected')
        
        op[-1] = [op[-1][0],max(ip[j][1],op[-1][1])]
        
    else:
        op.append(ip[j])
    
    j+=1
