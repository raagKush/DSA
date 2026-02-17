# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 09:55:41 2026

@author: INAKUSHW
"""

ip = ["tea","eat","ate","tan","ant","pan"]

from collections import defaultdict

def groupAnagram(s):
    op_dict = defaultdict(list)
    for s in ip:
        key = "".join(sorted(s))
        op_dict[key].append(s)
        
    return(list(op_dict.values()))
    
op = groupAnagram(ip)