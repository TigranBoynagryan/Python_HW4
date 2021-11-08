# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 22:10:34 2021

@author: Tigran Boynagryan
"""
def findAndReplacePattern(words, pattern):
    result = []
    ls = {}
    def convert(c):
        if c not in ls:
            ls[c] = chr(97 + len(ls))
        return ls[c]
    
    def compare(word):
        ls.clear()
        for i in range(len(word)):
            if convert(word[i]) != puzzle[i]:
                return
        result.append(word)
    puzzle = [convert(c) for c in pattern]
    
    for word in words:
        compare(word)
    return result

words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"
print(findAndReplacePattern(words, pattern))