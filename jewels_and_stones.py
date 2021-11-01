# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 12:22:56 2021

@author: Tigran Boynagryan
"""

import re

jewels = input()
stones = input()

count = 0
for i in jewels:
    pattern = i
    if re.findall(i,stones):
        count += len(re.findall(i, stones))
    else:
        continue

print(count)
