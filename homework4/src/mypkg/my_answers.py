#!/usr/bin/python

"""
Object Oriented Programming and Python Classes
"""

"""
QUESTION 1: 
========================================================================================================
Write a class with name WindowAverage which is initialized by a window size and returns an average of
a stream of integers over a window by calling a method next. 

Example:
===========================
    w = WindowAverage(3)
    w.next(2) = 2   
    w.next(4) = (2+4)/2   （2+4）/2
    w.next(3) = (4+3)/2    (2+4+3)/3
    w.next(5) = (2+3)/2    (4+3+5)/3
    
Hints: You should have __init__ and next methods and can use a data structure - double-ended queue
from collections module.    
"""

from collections import deque


class WindowAverage:
    def __init__(self, size):
        self.d = deque()
        self.size = size

    def next(self, v):
        if len(self.d) == self.size:
            self.d.popleft()
        self.d.append(v)
        sum = 0.0
        for i in self.d:
            sum += i
        return sum / len(self.d)








"""
QUESTION 2: 
========================================================================================================
Write a class with name AlternateIterator which is initialized by two lists v1 and v2
and returns the elements alternatively every time a method next is called and stops
iteration when both lists are exhausted

Example:
===========================
    Input: l1 = [1, 2, 3]
           l2 = [4, 5, 6, 7]
        
    Output: [1, 4, 2, 5, 3, 6, 7]
 
    Usage:
    iter = AlternateIterator(l1, l2)
    res = []
    while iter.has_next():
        res.append(iter.next())

Hints: You should have three methods: __init__, next, and has_next. 

size1
size2
index1
index2
value
switch=1
if sw==1
 index++ siz1

"""


class AlternateIterator():
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2
        if self.v1 >= self.v2:
            self.size = len(self.v2)
            self.v1.insert(0,self.v2[0])
            i = 2
            j = 1
            while i <= 2 * self.size - 2 and j <= self.size:

                self.v1.insert(i,self.v2[j])
                i = 2*i
                j += 1
            for num in range(0,2*self.size,2):
                self.v1[num],self.v1[num+1] = self.v1[num+1],self.v1[num]
        else:
            self.size = len(self.v1)
            self.v2.insert(0,self.v1[0])
            i = 2
            j = 1
            while i <= 2 * self.size - 2 and j <= self.size:

                self.v2.insert(i,self.v1[j])
                i = 2*i
                j += 1
        self.count = -1
    def has_next(self):

        if self.count + 1 < max(len(self.v1),len(self.v2)):
            return True
        else:
            return False

    def next(self):
        self.count += 1
        if len(self.v1) >= len(self.v2):
            return self.v1[self.count]
        else:
            return self.v2[self.count]










"""
QUESTION 3:
========================================================================================================
Write a class ModifiedIterator that inherits the class AlternateIterator you wrote in Q2 that overwrites
the method next so that it return twice of the value from l2.

Example:
===========================
    Input: l1 = [1, 2, 3]
           l2 = [4, 5, 6, 7]
        
    Output: [1, 8, 2, 10, 3, 12, 14]
    
    Usage:
    iter = ModifiedIterator(l1, l2)
    res = []
    while iter.has_next():
        res.append(iter.next())
"""
class ModifiedIterator():
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2
        newList = []
        for i in self.v2:
            newList.append(2*i)
        self.v2 = newList
        if self.v1 >= self.v2:
            self.size = len(self.v2)
            self.v1.insert(0,self.v2[0])
            i = 2
            j = 1
            while i <= 2 * self.size - 2 and j <= self.size:

                self.v1.insert(i,self.v2[j])
                i = 2*i
                j += 1
            for num in range(0,2*self.size,2):
                self.v1[num],self.v1[num+1] = self.v1[num+1],self.v1[num]
        else:
            self.size = len(self.v1)
            self.v2.insert(0,self.v1[0])
            i = 2
            j = 1
            while i <= 2 * self.size - 2 and j <= self.size:

                self.v2.insert(i,self.v1[j])
                i = 2*i
                j += 1
        self.count = -1
    def has_next(self):

        if self.count + 1 < max(len(self.v1),len(self.v2)):
            return True
        else:
            return False

    def next(self):
        self.count += 1
        if len(self.v1) >= len(self.v2):
            return self.v1[self.count]
        else:
            return self.v2[self.count]



