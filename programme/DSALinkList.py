################################################################################
# AUTHOR: Tawana David Kwaramba                                                #
# STUDENT: NUMBER: 19476700                                                    #
# PURPOSE:  this class defines a doubly linked list, and its surpporting       #
#           inner classes                                                      # 
# LAST MODIFIED:  4/09/19 16:00                                                #
################################################################################
from Errors import *

class DSALinkList:
    def __init__(self, head = None, tail = None):
        self._head = None
        self._tail = None
        self._count = 0

    #ACCESSORS
    def getCount(self):
        return self._count

    def getHead(self):
        return self._head

    def getTail(self):
        return self._tail

    def isEmpty(self):
        #return (self._head._getValue() == None and self._tail._getValue() == None)
        return self._count == 0

    def peekFirst(self):
        if self.isEmpty():
            raise ListUnderFlowError("ERROR: they is nothing attached to the list")
        else:
            nodeValue = self._head._value
        return nodeValue

    def peekLast(self):
        if self.isEmpty():
            raise ListUnderFlowError("ERROR: they is nothing attached to \
            the list")
        else:
            nodeValue = self._tail._value 
        return nodeValue

    def peek(self, value):
        raise UnsupportredOperationError("\nnot surporteded\n")

    def find(self, value):
        raise UnsupportredOperationError("\nnot surporteded\n")

    #MUTATORS

    def insertFirst(self, value):
        newNd = _ListNode(value)
        newNd._prevRef = None
        if(self.isEmpty()):
            self._tail = newNd
            self._head = newNd
        else:
            newNd._nextRef = self._head
            self._head._prevRef = newNd
            self._head = newNd
        self._count += 1


    def insertLast(self, value):
        newNd = _ListNode(value)
        newNd._prevRef = self._tail
        newNd._nextRef = None

        if(self.isEmpty()):
            self._head = newNd
        else:
            self._tail._nextRef = newNd

        self._tail = newNd
        self._count += 1

    def insertBefore(self, _value):
        raise UnsupportredOperationError("Operation is not supportded")

    def removeLast(self):
        if self.isEmpty():
            raise ListUnderFlowError("ERROR: they is nothing attached to the list")
        #elif (self._head._getNext() == None and self._head._getPrev() == None):

        lastNd  = self._tail
        nodeValue = lastNd._value

        if (self._count == 1):
            #the case if they is one node in the linked list
            self._head = None
            self._tail = None
        else:
            #case where they is multiple nodes in the linked list
            #assuming the tail is the last _value
            currNd = self._tail._prevRef
            self._tail = currNd
            self._tail._nextRef = None

        self._count -= 1

        return nodeValue

    def removeFirst(self):
        if self.isEmpty():
            raise ListUnderFlowError("ERROR: they is nothing attached to the list")

        firstNd = self._head
        nodeValue = firstNd._value

        if (self._count == 1):
            self._head = None
            self._tail = None
        else:
            currNd = self._head._nextRef
            self._head = currNd
            currNd._prevRef = None
            firstNd._nextRef = None

        self._count -= 1

        return nodeValue

        

    def __iter__(self):
        self._cur = self._head
        return self

    def __next__(self):
        curVal = None
        if self._cur == None:
            raise StopIteration
        else:
            #curVal = self._cur._value
            curVal = self._cur
            self._cur = self._cur._nextRef
        return curVal

    def display(self):
        if(self.isEmpty()):
            retStr = "Empty Stack"
        else:
           retStr = self._displayRec(self._head)

        return retStr

    def _displayRec(self, inNode):
        if(inNode != None):
            print('- %s' % inNode._value) 
            self._displayRec(inNode._nextRef)


    def remove(self, remove):
        stop = False
        myIter = iter(self)

        if self.isEmpty():
            raise ListUnderFlowError("ERROR: they is nothing attached to the list")

        while(not(stop)):   
            try:
                value = next(myIter)
                if str(value) == str(remove):
                    stop = True
                    nxtNd = value._nextRef
                    prevNd = value._prevRef
                    
                    if ((prevNd !=  None) and (nxtNd != None)):
                        prevNd._nextRef = nxtNd
                        nxtNd._prevRef = prevNd
                    elif prevNd == None:
                        self._head = nxtNd
                    elif nxtNd == None:
                        self._tail = prevNd
                        prevNd._nextRef = None
            except StopIteration:
                raise ListNodeError("ERORR: list node " + str(remove)+\
                " doesn't exist")
        self._count -= 1

        
class _ListNode:
    def __init__(self, value = None, nextRef = None, prevRef = None):
        self._value = value
        self._nextRef = nextRef
        self._prevRef = prevRef

    def __str__(self):
        return("%s" % self._value)

    #ACCESSORS
    def getValue(self):
        return self._value

    def getNext(self):
        return self._nextRef

    def getPrev(self):
        return self._prevRef

    #MUTATORS
    def setValue(self, inValue):
        self._value = inValue

    def setNext(self, newNxt):
        self._nextRef = newNxt

    def setPrev(self, newPrev):
        self._prevRef = newPrev

