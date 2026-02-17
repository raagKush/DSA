# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 11:33:25 2026

@author: INAKUSHW
"""

import heapq

nums = [4,4,4,6,6,7,7,7,7]
freq = {}
k = 2

for i in nums:
    if i in freq.keys():
        freq[i] +=1
    else:
        freq[i] = 1 

freqItems = [(-value,key) for key,value in freq.items()]    
heapq.heapify(freqItems)

print()

topK = []
for i in range(k):
    topK.append(heapq.heappop(freqItems)[1])
    
''' '''    ''''''''''''''''''''''''
    
import heapq

nums = [4,4,4,6,6,7,7,7,7]
freq = {}
k = 2

heap = []

for i in nums:
    if i in freq.keys():
        freq[i] +=1
    else:
        freq[i] = 1 
        
for (num, count ) in freq.items():
    heapq.heappush(heap, (count,num))
    
    if len(heap)>k:
        heapq.heappop(heap)
        
        
topK = [num for count,num in heap]