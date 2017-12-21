# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 17:09:35 2017

@author: Administrator
"""

def mytest(years,money):
    years=int(years)
    money=int(money)
    if years==1:
        lilv=1.1
    else:
        lilv=1.1**years
    return lilv*money
    
while True:
    num1=input("For years: ")
    if num1=='q':
        break
    num2=input("How much: ")
    if num2=='q':
        break
    else:
        print(mytest(num1,num2))