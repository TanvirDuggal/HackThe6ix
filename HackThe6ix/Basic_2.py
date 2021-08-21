# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 22:26:11 2021

@author: Tanvy
"""

# Python 102
# Lets learn some real python stuff that makes it the best

# 1. List

a = [1,2,3,4,5,6,7,8,9]
# Accessing complete list
print("Accessing Complete List")
print(a)
# Accessing first element
print("Accessing first element")
print(a[0])
# Accessing last element
print("Accessing last element")
print(a[-1])
# Accessing All records from an index, REMEMBER LEFT/UPPER BOUND IS NOT INCLUDED BUT RIGHT/LOWER BOUND IS
print("Accessing all records from index")
print(a[1:])
print("Accessing all records before an index")
print(a[:-1])
print("Accessing records between two indexes")
print(a[2:5])

# LOOPING THROUGH LIST
print("Looping through FOR IN")
for i in a:
    print(i)

# LOOPING THROUGH FOR RANGE 
print("Looping through FOR RANGE loop")
for i in range(len(a)):
    print(a[i])
    
# ADDING ELEMENTS TO LIST
a.append(True)
a.append("Sup")
print(a)

# LIST COMPREHENSAION 
# CREATING AND ACCESSING LIST IN JUST SINGLE LINE

print("Creating list using list comprehension")
b = [x for x in range(2,10)]
print(b)

# EDITING LIST USING LIST COMPREHENSION
print("Editing list using list comprehension")
c = [x for x in b if type(x) == int]
print(c)

d = [x*2 for x in b]
print(d)


def changeNumToSomethingElse(num):
    if num%2 == 0:
        return "its even"
    else:
        return "its odd"
    
d = [changeNumToSomethingElse(x) for x in b]

print(d)