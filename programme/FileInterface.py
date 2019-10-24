import pickle
from DSAShufflingQueue import *
from DSALinkList import DSALinkList
from DSAGraph import *
from Person import Person

class FileInterface:
    def createNetwork(self, fileName):
        newGraph = DSAGraph()
        self._readNetwork(fileName, newGraph)

        #while not fileContents.isEmpty():
        #    newGraph.addVertex(fileContents.removeLast())

        return newGraph

    def simulateNetworkEvents(self, fileName):
        pass
    
    #PURPOSE: to read in the contents of file to be enbaled to create graph
    #objects from file contents
    def _readNetwork(self, fileName, inGraph): 
        fileNameClean = self._validateName(fileName.strip())
        with open(fileNameClean, 'r') as inStrm:
            for line in inStrm:
                lines = self._processLine(line)
                
                if lines.getCount() == 2:
                    inGraph.addEdge(lines.removeFirst(), lines.removeFirst())
                else:
                    inGraph.addVertex(lines.removeFirst())


#    def _readNetworkEvents(self, fileName): 
#        fileNameClean = self._validateName(fileName.strip())
#        fileContents = DSALinkList()
#
#        with open(fileNameClean, 'r') as inStrm:
#            for line in inStrm:

    def _processLine(self, line): 
        lineContents = DSALinkList()
        contents = line.strip().split(":")

        for vertice in contents:
            lineContents.insertLast(vertice)
        
        return lineContents

    def _validateName(self, inName):
        if inName == None:
            raise ValueError("ERROR: name cannot be nothing")
        
        return inName
