#AUTHOR: Tawana David Kwaramba
#STUDENT ID: 19476700
#PURPOSE: is to create an abstract data type of a _stack for the purposes in 
#implementing it in other children classes
#LAST DATE MODIFIED:

import numpy as np 
from Errors import *
from DSALinkList import *

class Stack():
    def __init__(self):
        self._stack = DSALinkList()

    #ACCESORS
    def getCount(self):
        return self._stack.getCount()

    def isEmpty(self):
        return self._stack.isEmpty()

    def isFull(self):
        raise UnsupportredOperationError("\nlist doesn't have maximum capacity\n")
    
    #MUTATORS 

    #place a new value on top of the _stack
    def push(self, value):
        self._stack.insertFirst(value)

    #remove the value from the start of the list, as the linked list has been
    #organised backwards
    def pop(self):
        topVal = self._stack.peekFirst()
        self._stack.removeFirst() 
        return topVal

    def top(self):
        return self._stack.peekFirst()

    def display(self):
        self._stack.display()
