# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 16:24:26 2021

@author: Royal
"""

# Python program to print positive Numbers in a List
  
# list of numbers
list1 = [22,-7,100,74,-14]
num = 0
  
# using while loop     
while(num < len(list1)):
      
    # checking condition
    if list1[num] >= 0:
        print(list1[num], end = " ")
      
    # increment num 
    num += 1
