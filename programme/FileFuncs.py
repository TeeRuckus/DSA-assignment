################################################################################
# AUTHOR: Tawana David Kwaramba                                                #
# STUDENT: NUMBER: 19476700                                                    #
# PURPOSE:  this document is a container of all my functions which relate      #
#           to file input/ output                                              # 
# LAST MODIFIED:  4/09/19 16:00                                                #
################################################################################


import pickle

def fileMenu():
    valid = False
    userOp = 0 
    while not valid:
        valid = True

        userOp = input("""
1) Read a serialized file
2) display the list
3) write a serialized file

""")    
        #removing all white spaces from the user input
        userOpClean = userOp.strip()
        if ((userOpClean != "1") and (userOpClean != "2") and (userOpClean != "3")):
            print("\nPlease enter a valid option\n")
            valid = False

    return userOp

#code obtain from pratical submission one. The code is written by myself:
#Tawana Kwaramba 19476700
#PURPOSE: to read in the contents of a file
def readFile(fileName):
    fileContents = []
    
    with open(fileName, 'r') as inStrm:
        for line in inStrm:
            fileItems = inStrm.readlines()
            #fileContents = inStrm.read()

    for ii in range(len(fileItems)):
        fileContents.append(fileItems[ii].strip('\n'))

    return fileContents

#PURPOSE:t to write the contents of a file
def writeFile(fileName, inList):
    #fileLines = []
    document = open(fileName, 'a')
    for ii in range(len(inList)):
        document.write(inList)
    fileName.close()

    return 0
#end of code obtained from practical one

def loadObject(fileName):
    try:
        with open(fileName, 'rb') as dataFile:
            inObject = pickle.load(dataFile)
    except:
        print("ERORR: object file does not exist!")
    return inObject

def saveObject(fileName, inObjct):
    print("Saving object to file...")
    try:
        with open(fileName, 'wb') as dataFile:
            pickle.dump(inObjct, dataFile)
    except:
        print("ERROR: problem pickling object")
