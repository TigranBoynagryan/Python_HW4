# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 22:24:48 2021

@author: Tigran Boynagryan
"""

k = int(input())
logs = [[0,5],[1,2],[0,2],[0,5],[1,3]]

def findingUsersActiveMinutes(logs, k):
    res = [0] * k
    ls = {}
    for i, j in logs:
        if i not in ls:
            ls[i] = [j]
        elif i in ls and j not in ls[i]:
            ls[i].append(j)
    
    for keys,values in ls.items():
       
        res[len(values)-1] += 1
    return res

print(findingUsersActiveMinutes(logs, k))