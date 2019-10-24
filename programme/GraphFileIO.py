import pickle
from DSAShufflingQueue import *
from DSALinkList import DSALinkList
from DSAGraph import *

class FileInterface:
    def createGraph(self, fileName):
        fileContents = self._readFile(fileName)
        newGraph = DSAGraph()

        while not fileContents.isEmpty():
            newGraph.addEdge(fileContents.removeFirst(), fileContents.removeFirst())

        return newGraph

    
    #PURPOSE: to read in the contents of file to be enbaled to create graph
    #objects from file contents
    def _readFile(self, fileName): 
        fileNameClean = self._validateName(fileName.strip())
        fileContents = DSALinkList()
        with open(fileNameClean, 'r') as inStrm:
            for line in inStrm:
                lines = self._processLine(line)

                for line in lines:
                    fileContents.insertLast(line)
        
        return fileContents

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
