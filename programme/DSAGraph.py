################################################################################
# AUTHOR: Tawana David Kwaramba                                                #
# STUDENT: NUMBER: 19476700                                                    #
# PURPOSE: 
#         
# LAST MODIFIED: 
################################################################################
from Errors import *
from DSALinkList import DSALinkList 
from DSAsorts import selectionSort
import numpy  as np

class DSAGraph:
    def __init__(self):
        self._vertices = DSALinkList()
        self._verticesCount  = 0
        self._edgeCount = 0 

    #ASSERT: returns the count of the verticesCount class field
    def getVerticeCount(self):
        return self._verticesCount

    def getEdgeCount(self):
        return self._edgeCount
    
    #ASSERTS: returns true if the DSAGraph has a vertex correspondig to inLabel 
    def hasVertex(self, inLabel):
        myIter = iter(self._vertices)
        found = False
        stop = False
        while (not(stop) and not(found)):
            #when the iterator reaches the end of the object, I am expecting a
            #StopIteration exception
            try:
                value = next(myIter).getValue()
                if str(value) == str(inLabel):
                    found = True
            except StopIteration:
                stop = True

        return found

    def getVertex(self, inLabel):
        if(self.hasVertex(inLabel)):
#            myIter = iter(self._vertices)
#            stop = False 
#
#            while not(stop):
#                value = next(myIter)
#                if str(value) == inLabel:
#                    stop = True
#                    foundVert = value
            foundVert = self._findVertex(inLabel)
        else:
            raise VertexError("ERROR: vertex doesn't exitst")

        return  foundVert 

    def getVertexLabel(self, inLabel):
        return getVertex._label

    def getEdge(self, vertexFromLabel, vertexToLabel):
        if(self.hasEdge(vertexFromLabel, vertexToLabel)):
            myIter = iter(self._edges)
            stop = False

            while not(stop):
                value = next(myIter).getValue()
                if(value._vertexOne == vertexFrom):
                    if(value._vertexTwo == vertexTo):
                        stop = True
                        foundEdge = value
        else:
            raise EdgeError("ERROR: edge connection doesn't exist")
        
        return foundEdge
           
    def isAdjacent(self, inLabelOne, inLabelTwo):
        mainVertex = self.getVertex(inLabelOne)
        isAdjacent = False
        stop = False
        myIter = iter(mainVertex._links)
        while(not(stop)):
            try:
                value = next(myIter).getValue()
                if str(value) == inLabelTwo:
                    isAdjacent = True
            except StopIteration:
                stop = True
        return isAdjacent
    
    #PURPOSE: to find the inLabel in the vertices linked list and to export its
    #adjacent list otherwise, abort.
    def getAdjacent(self, inLabel):
        #don't need to check if the label exist or not as getVertex handles that
        adjList = self.getVertex(inLabel)
        return adjList._getAdjacent()
    
    #PURPOSE: to return if the inLabel vertex has been visted, if the vertex
    #doesn't exist abort
    def hasVisited(self, inLabel):
        #don't need to abort here as getVertex handles that
        visted = self.getVertex(inLabel)
        return visted.getVisted()
    

    #PURPOSE: to create a vertex object which has the inputted label, and to add
    #the vertex object to the classes linked list
    def addVertex(self, inLabel):
        newVertex = _DSAGraphVertices(inLabel)
        self._vertices.insertLast(newVertex)
        self._verticesCount += 1

    def removeVertex(self, inLabel):

        self._vertices.remove(inLabel)

        #we need to search every vertices adjaceny list and  remove the desired
        #label
        myIter = (self._vertices)

        stop = False
        
        #we not to make sure that we go through all the  vertices in the linked
        #list. Hence our stop condition is when the stop iteration error occurs
        while not(stop):
            try:
                value = next(myIter).getValue()
                value._links.remove(inLabel)            
            except StopIteration:
                stop = True
            except ListUnderFlowError:
                #we want to ignore this error as ito simply means the vertice
                #we are analysing 
                pass
            except ListNodeError:
                pass

    def  addEdge(self, labelOne, labelTwo):
        if not(self.hasVertex(labelOne)):
            self.addVertex(labelOne)

        if not(self.hasVertex(labelTwo)):
            self.addVertex(labelTwo)

        vertexMain = self.getVertex(labelOne)
        connectingVertex = self.getVertex(labelTwo)

        if not(vertexMain._hasEdge(labelTwo)):
            vertexMain._addEdge(labelTwo)

    def setVertexValue(self, inVertexLabel, inValue):
        vertex = self.getVertex(inVertexLabel)
        vertex._value = inValue

    #PURPOSE: to display the vertices class field as an adjaceny list
    def displayAsList(self):
        print(" | GRAPH ADJACENY LIST")
        print("-"*50)
        myIter = iter(self._vertices)
        value = next(myIter).getValue()
        sortedLabels = self._sortVertices()
        for value in self._vertices:
            print(value, end=": ")
            adjNode = value.getValue()
            adjVertices = adjNode._getAdjacent()
            for value in adjVertices:
                print(value, end=" ")
            print()

    #PURPOSE: to display the vertices class field as a matrix
    def displayAsMatrix(self):
        rowNum = 0
        columnNum = 0

        #creating a m x m 2-Dimensinal array to hold all my values
        #creating an extra space in my rows for the labels
        rows = self._verticesCount + 1
        graphMatrix = np.zeros(shape=(rows,rows), dtype=str)
        
        #iterators to be used to print labels onto the matrix
        rowsIter = iter(self._vertices)
        columnIter = iter(self._vertices)
        rowLabels = next(rowsIter).getValue()
        columnLabels = next(columnIter).getValue()
        sortededLabels = self._sortVertices()
        print(sortededLabels)

        #placing all the labels on the matrix
        for rowLabels in sortededLabels:
            graphMatrix[rowNum+1][0] = rowLabels
            rowNum += 1

        for columnLabels in sortededLabels:
            graphMatrix[0][columnNum+1] = columnLabels
            columnNum += 1
    

        print("   | GRAPH MATRIX")
        print("-"*50)
        
        for labels in self._vertices:
            adjList = labels.getValue()._getAdjacent()
            for adjLabel in adjList:
                rowLoc = (ord(adjLabel) - ord('A'))+1
                columnLoc = (ord(adjLabel) - ord('A'))+1
                graphMatrix[rowLoc][columnLoc] = '1'

        print(graphMatrix)
    #PURPOSE: is to sort single characters in alphabatical orders
    def _sortVertices(self):
        #making a dictonary, so the ASCII values of the characters can be
        #easily associated back to their right ful character
        charDict = {}
        ii = 0
        kk = 0
        verticesArr = np.zeros(self._vertices.getCount(), dtype=int)
        sortedArr = np.zeros(self._vertices.getCount(), dtype=str)
        myVerticeIter = iter(self._vertices)
        value = next(myVerticeIter).getValue()
        try:
            for value in self._vertices:
                charDict[ord(value.getValue()._getLabel())] = \
                value.getValue()._getLabel()
            values = charDict.keys()
            #filling up the array with the values, so the array can be sortede
            #numerically
            for value in values:
                verticesArr[ii] = value
                ii += 1

            selectionSort(verticesArr)
            for jj in verticesArr:
                sortedArr[kk] = charDict[jj]
                kk += 1
        except TypeError:
            sorterdArr = 0
        return sortedArr


    def setVisted(self):
        pass

    def clearVisted(self):
        pass


    def toString(self):
        pass

    #PURPOSE: to be able to iterate through the vertices linked list and return
    #the memory address of the list node corresponding to the vertex label
    def _findVertex(self, inLabel):
        foundVertex = None
        try:
            myIter = iter(self._vertices)
            stop = False
        
            while not(stop):
                #going through all the elements of the linked list
                value = next(myIter).getValue()
                if str(value) == str(inLabel):
                    foundVertex = value
        except StopIteration:
            #do nothing as this exception will get thrown if it's at the 
            #end of iterating through the adjacent list
            pass
        return foundVertex


class _DSAGraphVertices:
    def __init__(self, label):
        self._label = label
        self._links = DSALinkList()
        self._visted = False

    def __str__(self):
        return("%s" % self._label)           
    

    #ASSERT: returns the label of the DSAGraphVertices class field
    def _getLabel(self):
        return  self._label
    
    #PURPOSE: it will retrun it's adjaceny list, which is the self._links
    #class field
    def _getAdjacent(self):
        return  self._sortLinks()

    #ASSERTS: returns true if the edge exits in links 
    def _hasEdge(self, inLabel):
        myIter = iter(self._links)
        found = False
        stop = False
        while not(stop):
            #when the iterator reaches the end of the object, I am expecting a
            #StopIteration exception
            try:
                value = next(myIter).getValue()
                #a vertex cannot be connected to itself
                if str(value) == self._label or str(value) == inLabel:
                    found = True
                    stop = True
            except StopIteration:
                stop = True
        return found

    #ASSERT: adds vertex to the links class field
    def _addEdge(self, vertex):
        self._links.insertLast(vertex)

    def _getAdjacentEdge(self): 
        pass

    def _setValue(self, inValue):
        self.value = inValue

    #PURPOSE: is to sort single characters in alphabatical orders
    def _sortLinks(self):
        #making a dictonary, so the ASCII values of the characters can be
        #easily associated back to their right ful character
        charDict = {}
        ii = 0
        kk = 0
        linksArr = np.zeros(self._links.getCount(), dtype=int)
        sortedArr = np.zeros(self._links.getCount(), dtype=str)
        myLinkIter = iter(self._links)
        
        try:
            value = next(myLinkIter).getValue()
            for value in self._links:
                charDict[ord(value.getValue())] = value
            values = charDict.keys()
            #filling up the array with the values, so the array can be sortede
            #numerically
            for value in values:
                linksArr[ii] = value
                ii += 1

            selectionSort(linksArr)
            for jj in linksArr:
                sortedArr[kk] = charDict[jj]
                kk += 1
        except StopIteration:
            pass
        return sortedArr
    
    #ASSERT: returns the value of the visted calss field
    def _getVisted(self):
        return self._visted
    
    #ASSERT: visted clsas field will be changed to true
    def _setVisted(self):
        self._visted = True
    
    #ASSERT: visited class field will be changed to false
    def _clearVisted(self):
        self._visted = False 

class _DSAGraphEdge:
    def __init__(self,inVertexOne,  inVertexTwo, inLabel, inValue):
        self._label = self._validateLabel(inLabel)
        self._value = self._validateValue(inValue)
        self._vertexOne = self._validateVertex(inVertexOne)
        self._vertexTwo = self._validateVertex(inVertexTwo)

    def _getLabel(self):
        return self._label

    def _getValue(self):
        return  self._value
    
    #gets vertex from the begining of the edge
    def _getFrom(self):
        return self._vertexOne

    #gets vertex  to where the edge is pointing too
    def _getTo(self):
        return self._vertexTwo

    def _toString(self):
        return '%s = %s | %s -> %s' %(self._label, self._value, self._vertexOne\
        ,vertexTwo)

    def _validateVertex(self, inVertex):
        vertex = inVertex

        if(not(isinstance(vertex, _DSAGraphVertices))):
            raise VertexError('ERROR: value: %s is not a vertex object' % \
            (inVertex))

        return vertex

    def _validateLabel(self, inLabel): 
        label = inLabel

        if(not(isinstance(label, str))):
            raise TypeError('ERROR: label must be a string')

        return label

    def _validateValue(self, inValue):
        value = inValue

        if(not(isinstance(value, float))):
            raise TypeError('ERROR: value - %s be a real number')

        return value
