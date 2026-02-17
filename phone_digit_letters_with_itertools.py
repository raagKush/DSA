# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 10:29:44 2026

@author: INAKUSHW
"""

from itertools import product
digits = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz"
    }

ip = 8

ip = str(ip)
s = []
for i in range(len(ip)):
    s.append( digits[int(ip[i])])
    

values = ["".join(p) for p in product(*s)]