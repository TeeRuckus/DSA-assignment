def createNetwork( fileName):
    fileContents =readFile(fileName)
    newGraph = DSAGraph()

    while not fileContents.isEmpty():
        newGraph.addEdge(fileContents.removeFirst(), fileContents.removeFirst())

    return newGraph


#PURPOSE: to read in the contents of file to be enbaled to create graph
#objects from file contents
def readFile( fileName): 
    fileNameClean =validateName(fileName.strip())
    fileContents = DSALinkList()
    with open(fileNameClean, 'r') as inStrm:
        for line in inStrm:
            lines =processLine(line)

            for line in lines:
                fileContents.insertLast(line)
    
    return fileContents

def processLine( line): 
    lineContents = DSALinkList()
    contents = line.strip().split(" ")

    for vertice in contents:
        lineContents.insertLast(vertice)
    
    return lineContents

def validateName( inName):
    if inName == None:
        raise ValueError("ERROR: name cannot be nothing")
    
    return inName
