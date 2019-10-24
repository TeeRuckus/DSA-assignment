from Person import Person
from DSALinkList import *
from DSAStack import Stack
from FileInterface import *
from DSAGraph import *
from Errors import *
import random as r 
import numpy as np

MIN_RAND_NUM = 1
MAX_RAND_NUM = 100

def main():
#    print('TEST 1: ')
#    LinkedListTest()
#
#    print('TEST 2: ')
#    StackClassTest()

    print('Test 3: ')
    graghTest()
    
#    print('TEST 5: ')
#    personClassTest()

def LinkedListTest():
    testingHeader('Linked list Unit test')
    numTests = 0
    numPassed = 0

    #test 1: intialising the linked list
    numTests += 1 
    print("\nTEST 1:\n")

    dLinkList = DSALinkList()
    if(dLinkList.getHead() == None and dLinkList.getTail() == None):
        print("PASSED: creating a linked list\n")
        numPassed += 1
    else:
        print("FAILED: creating a linked list\n")

    #TESTING ALL ACCESSORS WITH EMPTY LINKED LIST

    #Test 2: isEmpty accessor
    numTests += 1
    print("\nTEST 2\n")
    if(dLinkList.isEmpty()):
        print("PASSED: isEmpty accessor")
        numPassed += 1 
    else:
        print("FAILED: isEmpty accessor")

    #test 3: peekFirst with an empty LinkedList 
    numTests += 1
    print("\nTEST 3\n")
    try:
        dLinkList.peekFirst()
        print("FAILED: peek first with an empty accessor\n")
    except ListUnderFlowError as err:
        print("PASSED: peek first with an empty accessor: " +str(err)+ "\n")
        numPassed += 1

    #test 4: peekLast with an empty LinkedList
    numTests += 1
    print("\nTEST 4\n")
    try:
        dLinkList.peekLast()
        print("FAILED: peeklast with an empty linked list\n")
    except ListUnderFlowError as err:
        print("PASSED: peeklast with an empty linked list: " +str(err)+"\n")
        numPassed += 1

    #test 5: removeLast with an empty dLinkList
    numTests += 1 
    print("\nTEST 5\n")
    try:
        dLinkList.removeLast()
        print("FAILED: removeLast with an empty dLinkList\n")
    except ListUnderFlowError as err:
        print("PASSED: removeLast with an empty dLinkList: "+str(err)+"\n")
        numPassed += 1

    #test 6: removeFirst with an empty link list
    numTests += 1
    print("\nTEST 6\n")
    try:
        dLinkList.removeFirst()
        print("FAILED: removeFirst with an empty dLinkList\n")
    except ListUnderFlowError as err:
        print("PASSED: removeFirst with an empty dLinkList: "+str(err)+"\n")
        numPassed += 1

    #test 7: insert first mutator
    numTests += 1
    print("\nTEST 7\n")
    #testNum is going to be used again to test the peak method
    lastNum = r.randint(MIN_RAND_NUM, MAX_RAND_NUM)
    print("Element added onto the list: %s" % lastNum)
    dLinkList.insertFirst(lastNum)

    if (dLinkList.isEmpty() and dLinkList.peekFirst() != lastNum):
        print("FAILED: insertFirst mutator\n")
    else:
        print("PASSED: insertFirst mutator\n")
        numPassed += 1

    #test 8: getTail accessor with one element
    numTests += 1
    print("\nTEST 8\n")
    if (dLinkList.getTail().getValue() == lastNum):
        print("PASSED: getTail accessor with one element\n")
        numPassed += 1
    else:
        print("FAILED: getTail accessor with one element\n")

    #test 9: peekLast accessor
    numTests += 1
    print("\nTEST 9\n")
    if(dLinkList.peekLast() == lastNum):
        print("PASSED: peek last accessor\n")
        numPassed += 1
    else: 
        print("FAILED: peek last accessor\n")

    #test 10: insertLast mutator with random amount of elements to list
    numTests += 1 
    print("\nTEST 10\n")
    print("\nElements added onto the linked list")
    for ii in range(r.randint(1,10)):
        lastNum = r.randint(MIN_RAND_NUM,MAX_RAND_NUM)
        dLinkList.insertLast(lastNum)
    
    if(dLinkList.peekLast() == lastNum):
        print("PASSED: insertLast mutator with random amount of elements\n")
        numPassed += 1
    else:
        print("FAILED: insertLast mutator with random amount of elements\n")

    #test 11: getTail accessor with various elements
    numTests += 1
    print("\nTEST 11\n")
    if (dLinkList.getTail().getValue() == lastNum):
        print("PASSED: getTail accessor with various elements\n")
        numPassed += 1
    else: 
        print("FAILED: getTail accessor with various elements\n")
        

    #test 12: removeLast mutator
    numTests += 1
    print("\nTEST 12\n")
    lastNum = r.randint(MIN_RAND_NUM,MAX_RAND_NUM)
    print("element added onto the linked list: %s" %lastNum)
    dLinkList.insertLast(lastNum)
    countBeforeDel = dLinkList.getCount()
    removedNum = dLinkList.removeLast()
    print("removed element: %s" % removedNum)
    countAfterDel = dLinkList.getCount()

    if(((countBeforeDel - countAfterDel) == 1) and (removedNum == lastNum)):
        print("PASSED: removeLast mutator\n")
        numPassed += 1
    else:
        print("FAILED: removeLast mutator\n")

    #test 13: removeFirst mutator
    numTests += 1
    print("\nTEST 13\n")
    lastNum = r.randint(MIN_RAND_NUM, MAX_RAND_NUM)
    dLinkList.insertFirst(lastNum)
    print("element inserted on the list: %s" % lastNum)
    countBeforeDel = dLinkList.getCount()
    removedNum = dLinkList.removeFirst()
    print("element removed from the linked list %d" % removedNum)
    countAfterDel = dLinkList.getCount()
    if(((countBeforeDel - countAfterDel) == 1) and (removedNum == lastNum)):
        print("PASSED: removeFirst mutator\n")
        numPassed += 1
    else:
        print("FAILED: removeFirst mutator\n")

    #test 14: inserting a bunch of objects
    numTests += 1
    print("\nTEST 14\n")
    print("elements being added:\n1\ntwo\n3\nfour\nheyyy....\nummm\nI can hanedle\
     objects too")
    dLinkList.insertFirst("1")
    dLinkList.insertFirst("two")
    dLinkList.insertFirst("3")
    dLinkList.insertFirst("four")
    dLinkList.insertLast("Heyyyy....")
    dLinkList.insertLast("ummm")

    #this will be used in the test harness later on
    lastString = "I can handle objects too"
    dLinkList.insertLast(lastString)

    if(dLinkList.peekLast() == "I can handle objects too"):
        print("PASSED: the insertion of objects")
        numPassed += 1
    else:
        print("FAILED: the insertion of objects")

    #test 15: testing if iterators are working
    print("\nTEST 15: this is a visual test, scroll up to see what has been added\n\
    this is the iterator\n")

    myIter = iter(dLinkList)
    value = next(myIter)

    print("*{",end="")
    for value in dLinkList:
        print(value, end=", ")
    print("}",end="")

    myIter = iter(dLinkList)
    value = next(myIter)

    #test 16: peek first with elements on the linked list
    numTests += 1
    print("\nTEST 16\n")

    if(dLinkList.peekFirst() == "four"):
        print("PASSED: peek first accessor with elements on the linked list") 
        numPassed += 1
    else:
        print("FAILED: peek first accessor with elements on the linked list") 
    
    print('displaying the list to a string')
    dLinkList.display()

    #Test 17 removing a list nod from the list
    numTests += 1
    dLinkList.insertLast(69)
    numItems = dLinkList.getCount()
    print(numItems)
    print("\nTEST 17\n")
    dLinkList.remove('four')
    print("removed \"four\" ")

    if((numItems - dLinkList.getCount()) == 1):
        print("PASSED: removed a string off the linked list")
        numPassed += 1
    else:
        print("FAILED: removed a string off the linked list")

    dLinkList.display()
    dLinkList.remove(69)
    print("removed \"69\"")
    numTests += 1
    if((numItems - dLinkList.getCount()) == 2):
        numPassed += 1
        print("PASSED: removing an integer of the list")
    else:
        print("FAILED: removing an integer of the list")
    

    dLinkList.display()
    dLinkList.remove('two')
    numTests += 1
    print("removed \"two\"")
    if((numItems - dLinkList.getCount()) == 3):
        numPassed += 1
        print("PASSED: removing an elment in betwenn")
    else:
        print("FAILED: removing an element in between")

    dLinkList.display()

    dLinkList.remove('Heyyyy....')
    numTests += 1
    print("remove \"Heyyyy....\"")
    if((numItems - dLinkList.getCount()) == 4):
        numPassed += 1
        print("PASSED: removing an elment in betwenn")
    else:
        print("FAILED: removing an element in between")

    dLinkList.display()

    #trying to remove an element which is not at the end or the start of a 
    #linked list


    #RESULTS
    percent = (numPassed / numTests) * 100
    print("\nRESULTS " +str(numPassed)+ "/" +str(numTests))
    print("%.2f" %percent+ "%")

def StackClassTest():
    testingHeader('STACK UNIT TEST')

    numPassed = 0
    numTest = 0

    #Test 1 - create stack 
    numTest += 1
    stackTest = Stack()

    if (stackTest.getCount() == 0):
        print("PASSED: created stack succesfully\n")
        numPassed += 1 
    else:
        print("FAILED: creation of stack\n")

    #Test 2 - isEmpty accessor with empty stack
    numTest += 1
    if(stackTest.isEmpty()):
        print("PASSED: isEmpty accessor with no elements\n")
        numPassed += 1
    else:
        print("FAILED: isEmpty accessor with no elements\n")

    #test 4  - push values on an empty stack
    numTest += 1
    stackTest.push(r.randint(1,1000))
    stackTest.push(r.randint(1,1000))
    numOfPushedElements = 2
    if (stackTest.getCount() == numOfPushedElements):
        print("PASSED: push mutator\n")
        numPassed += 1
    else:
        print("FAILED: push mutator\n")
        
    #test 5 - getCount accessor with elements on the stack 
    numTest += 1
    for ii in range(r.randint(1,7)):
        stackTest.push(r.randint(1,10000))
        numOfPushedElements += 1

    if (stackTest.getCount() == numOfPushedElements):
        print("PASSED: getCount accessor with elements on stack\n")
        numPassed += 1
    else:
        print("FAILED: getCount accessor with elements on stack\n")

    #test 6 - pop values
    numTest += 1
    #deleting all the elements on the stack 
    for ii in range(numOfPushedElements):
        stackTest.pop() 
        numOfPushedElements -= 1 


    if (stackTest.getCount() == 0):
        print("PASSED: popping all values on stack\n")
        numPassed += 1
    else:
        print("FAILED: popping all values on stack\n")

    #test 7 - pop empty stack
    numTest += 1
    try:
        stackTest.pop()
        print("FAILED: popped value from empty stack\n")
    except ListUnderFlowError as err:
    #except StackUnderFlowError as err: - not defined 
        print("PASSED: can't pop empty stack: "+str(err)+ "\n")
        numPassed += 1

    #test 8 - top accessor test
    numTest += 1
    lastElement = 49

    #reserving the very last element, so we will always know what the element is
    #for every set of randomly generated numbers  
    for ii in range(r.randint(4,9)):
        stackTest.push(r.randint(1,10000))

    stackTest.push(lastElement)
    if (stackTest.top() == lastElement):
        print("PASSED: access of last element\n")
        numPassed += 1
    else:
        print("FAILED: access of last element\n")

    #test 9 - isEmpty with elements on the stack
    numTest += 1
    if(stackTest.isEmpty()):
        print("FAILED: isEmpty with a full stack\n")
    else:
        print("PASSED: isEmpty with a full stack\n")
        numPassed += 1 

    #test 10 - isFull with a full stack
    numTest += 1
    try:
        stackTest.isFull()
        print("FAILED: isFull surport\n")
    except UnsupportredOperationError:
        print("PASSED: isFull surport\n")
        numPassed += 1

    #test 12 - pushing string objects onto the stack
    #numTest += 1
    listOfRandomStrings = []
    for ii in range(3):
        stackTest.pop()
    listOfRandomStrings = ["hey you", "ummmm... I forgot what I was saying",
                            "ohhh yeah I can handle objects"]
    for ii in listOfRandomStrings:
        stackTest.push(ii)


    #Results 
    percent = (numPassed / numTest) * 100
    print("\nRESULTS " +str(numPassed)+ "/" +str(numTest))
    print("%.2f" %percent+ "%")

def personClassTest():
    numTest = 0
    numPassed = 0 

    testingHeader('PERSON CLASS UNIT TEST')

    #CREATING A PERSON OBJECT
    print('Created a person called Tim: ', end='')
    numTest += 1
    Tim = Person('Mr', 'Tim')

    if(isinstance(Tim, Person)):
        print('PASSED')
        print(Tim)
        numPassed += 1
    else:
        print('FAILED')
    
    #TESTING GET TITLE & GET NAME ACCESSOR
    print('Get title accessor test: ',end='')
    if(Tim.getTitle() == 'Mr'):
        print('PASSED')
    else:
        print('FAILED')

    print('Get name accesor test: ', end='') 
    if(Tim.getName() == 'Tim'):
        print('PASSED')
    else:
        print('FAILED')

    likeStr = 'Tim Liked sarah\'s post | 10:00 am'

    Tim.addLiking(likeStr)

def graghTest():
    verticesArr = np.zeros(10, dtype=str)
    print("-"*75)
    print("| "+" "*31 +"DSAGRAPH TESTUNIT", end=" "*24 +"|\n")
    print("-"*75) 

    numPassed = 0
    numTests = 0

    vertexSeven = 'A'
    vertexSix = 'B'
    vertexFive = 'C'
    vertexFour = 'D'
    vertexThree = 'E'
    vertexTwo = 'F'
    vertexOne = 'G'

    for ii in range(len(verticesArr)):
        character = ord(vertexOne) + ii + 1
        verticesArr[ii] = chr(character)

    
    #TEST 1: creating the graph
    print("TEST 1 ", end=" ")
    numTests += 1
    myGraph = createGraphTest(numPassed)

    #TEST 2: adding a vertex test
    print("TEST 2 ", end=" ")
    addVertexTest(myGraph,numPassed, vertexOne,vertexTwo,vertexThree,\
                  vertexFour,vertexFive,vertexSix, vertexSeven)

    #TEST 3: testing display as list
    print("TEST 3 ", end=" ")
    displayTest(myGraph, numPassed)
    
    #test 4: testing has vertex
    print("TEST 4", end=" ") 
    hasVertexTest(myGraph, numPassed, numTests, vertexOne,vertexTwo,vertexThree,\
                  vertexFour,vertexFive,vertexSix,vertexSeven)

    #TEST 5: testing addEdge
    print("TEST 5 ", end=" ")
    addEdgeTest(myGraph, numPassed, vertexOne, vertexTwo)
    
    #adding more edge, seeing how the graph will scale with more input
    print('adding more edges onto the graph...')
    addEdgeTest(myGraph, numPassed, vertexSeven, verticesArr[1])
    addEdgeTest(myGraph, numPassed, vertexSix, verticesArr[1])
    addEdgeTest(myGraph, numPassed, vertexFive, verticesArr[2])
    addEdgeTest(myGraph, numPassed, vertexFour, verticesArr[3])

    for ii in range(len(verticesArr)):
        addEdgeTest(myGraph, numPassed, vertexFour, verticesArr[ii])
    

    #TEST 6: testing creating an edge from a file
    print("TEST 6: removing vertices from my network", end=" ")
    removeVerticeTest(myGraph, 'Q')
    removeVerticeTest(myGraph, 'I')
    removeVerticeTest(myGraph, 'F')
    removeVerticeTest(myGraph, 'O')


    print("TEST 7:", end="")
    createdGraphOne = createGraphFileTest('testNetwork1.txt')


def createGraphTest(numPassed):
    print("creating a graph object")
    myGraph = DSAGraph()
    #there's two things we're testing when we created the object
    numPassed += 2 
    if not(myGraph.getVerticeCount() == 0):
        print("FAILED: getCount must be initialised to 0")
        numPassed -= 1
    if not(myGraph.getEdgeCount() == 0):
        print("FAILED: getEdgeCount  must be initialised to 0")
        numPassed -= 1
    return myGraph

#PURPOSE: to test the display as list and display as a matrix methods
def displayTest(graph, numPassed):
    print("\nDisplaying my current graph as an adjaceny list and matrix\n")
    numPassed += 1
    graph.displayAsList()

    print("\nDisplaying my current graph as an adjacent list and matrix")
    graph.displayAsMatrix()

def addEdgeTest(graph, numPassed, mainLabel, secondLabel):
    print("addEdge test\n")
    print("edge connections been added: %s -> %s\n" %(mainLabel, secondLabel))
    
    graph.addEdge(mainLabel, secondLabel)
    if not(graph.hasVertex(mainLabel)):
        print("FAILED: the graph doesn't contain: " +label)

    if not(graph.hasVertex(secondLabel)):
        print("FAILED: the graph doesn't contain: " +label)

    graph.displayAsList()

    numPassed += 1

def addVertexTest(graph, numPassed, *args):
    print("AddVertexTest")
    #adding all the arguments passed through args into the graph
    for labels in args:
        graph.addVertex(labels)
    numPassed += 1 
    
    for labels in args:
        if not(graph.hasVertex(labels)):
            print("FAILED: the graph doesn't contain the added vertex")
            numPassed -= 1 

def hasVertexTest(graph, numPassed, numTest, *args):
    print("has vertex test")
    #testing and verfying if the labels are in the DSAGraph
    for label in args:
        numTest += 1
        if not(graph.hasVertex(label)):
            print("FAILED: the hasVertex didn't pick label: " +label)
        else:
            numPassed += 1 

def createGraphFileTest(inFileName):
    print("creating a graph from a file")
    fileInterface = FileInterface()
    createdGraph = fileInterface.createNetwork(inFileName)
    print("\nVerify from manual computations\n")
    createdGraph.displayAsList()

    return createdGraph

def isAdjacentTest(graph):
    print('is adjacent test')
    if(graph.isAdjacent('A', 'C')):
        print('PASSED: valid adjaceny')
    else:
        print('FAILED: valid adjaceny')

    if(graph.isAdjacent('A', 'B')):
        print('PASSED: valid adjaceny')
    else:
        print('FAILED: valid adjaceny')

    if(graph.isAdjacent('A', 'D')):
        print('PASSED: valid adjaceny')
    else:
        print('FAILED: valid adjaceny')

    if(graph.isAdjacent('D', 'F')):
        print('PASSED: valid adjaceny')
    else:
        print('FAILED: valid adjaceny')

    if(graph.isAdjacent('G', 'L')):
        print('FAILED: invalid adjaceny')
    else:
        print('PASSED: invalid adjaceny')

    if(graph.isAdjacent('A', 'M')):
        print('FAILED: invalid adjaceny')
    else:
        print('PASSED: invalid adjaceny')

def removeVerticeTest(inGraph, delVertice):
    print("remove vertex from graph test")
    print(" removing %s ..." % delVertice)
    
    inGraph.removeVertex(delVertice)

    if(not(inGraph.hasVertex(delVertice))):
        print("PASSED: removing a vertex")
    else:
        print("FAILEDL removing a vertex")

    inGraph.displayAsList()

     
def testingHeader(inHeader):
    print('-'*75)
    print('|'+' '*31 + inHeader, end=' '*24 +'|\n')
    print('-'*75)

if __name__ == '__main__':
    main()
