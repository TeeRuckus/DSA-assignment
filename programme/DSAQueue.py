################################################################################
# AUTHOR: Tawana David Kwaramba                                                #
# STUDENT: NUMBER: 19476700                                                    #
# PURPOSE:  abstract class for all the queues.                                 #
#                                                                              # 
# LAST MODIFIED:  4/09/19 16:00                                                #
################################################################################


from abc import ABC, abstractmethod 
from DSALinkList import *

class Queue(ABC):

    def __init__(self):
        self.queue = DSALinkList()
        self.count = 0

    def getCount(self):
        return self.count

    def isEmpty(self):
        return self.count==0

    def isFull(self):
        raise UnsupportredOperationError("\nLinked list is dymically sizable\n")
        
    def peek(self):
        return self.queue.peekFirst()
    
    @abstractmethod
    def enqueue(self, value):
        return 0
    
    @abstractmethod
    def dequeue(self):
        return 0 
    
    def toString(self):
        print("the following elements are on the queue:\n")
        myIter = iter(self.queue)
        value = next(myIter)
        print("Start *{", end="")
        for value in self.queue:
            print(value, end = ", ")
        print("} *end")

    #PURPOSE: to return a string, whihc can be used to be  written to a CSV 
    #file 
    def toFileString(self):
        queueContents = DSADDELinkedList() 
        myIter = iter(self.queue)
        value = next(myIter)

        for value in self.queue:
            queueContents.insertLast(value)
        
        print(queueContents)
        return queueContents
