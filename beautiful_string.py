# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 12:33:07 2021

@author: Tigran Boynagryan
"""

import re
n=int(input())
s = input()


pattern = '010'

occurs = re.findall(pattern,s)
print(len(occurs))
