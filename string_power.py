# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 12:40:19 2021

@author: Tigran Boynagryan
"""

string = input()
power = int(input())

def negative(string,power):
    for i in range(len(string)+1):
        if string[:i]*abs(power) == string:
            return string[:i]
        else:
            continue
    else:
        return 'undefined'

if power >= 0:
    print(string*power)
else:
    print(negative(string, power))
