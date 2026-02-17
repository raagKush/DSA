# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 11:57:58 2025

@author: INAKUSHW
"""

# prices = [3,2,1,4]
prices = [5,4,3,7,6,5,4,3,4,3,7]

#initital logic (only counting pairs and longest descent, not subsequent descents)
def smoothDescent(prices):
    numSD = 0
    c = 0
    SD = []
    for i in range(len(prices)-1):
        SD.append(prices[i])
        # print(prices[i],prices[i+1])
        if ((prices[i]-prices[i+1]) == 1):
            numSD +=1
            SD.append((prices[i],prices[i+1]))
            c +=1
        else:
            if (c>1):
                numSD +=1
                SD.append((prices[i-c:i+1]))
                c=0
    SD.append(prices[-1])
    return(SD)
    
SD = smoothDescent(prices)
result = len(SD)
        
#correct
numSD = 0
c = 1
for i in range(len(prices)-1):

    if ((prices[i]-prices[i+1]) == 1):
        print(prices[i],prices[i+1])
        c +=1
    else:
        print(prices[i],prices[i+1])
        c = 1
    
    numSD += c
