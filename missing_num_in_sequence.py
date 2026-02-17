# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 09:54:06 2026

@author: INAKUSHW
"""

arr = [2,3,4,5,7,8,9,10]

total = sum(arr)
calculated_sum = ((len(arr)+1)*(arr[0]+arr[-1]))/2

missing_num = calculated_sum-total