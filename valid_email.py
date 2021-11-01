# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 21:30:29 2021

@author: Tigran Boynagryan
"""


emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

emails1 = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]

def valid_email_checker(emails):
    res = set()
    for i in emails:
        loc,domain= i.split("@")[0],i.split("@")[1]
        loc = loc.split("+")[0].replace('.','')
        mail = loc+"@"+domain
        res.add(mail)
    return len(res)


print(valid_email_checker(emails))
print(valid_email_checker(emails1))
