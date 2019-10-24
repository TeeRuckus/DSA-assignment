from FileInterface import *
from DSAGraph import *
from Errors import *

def main():
    testUI = userInterface()
    userOp = testUI.mainMenu()

    print(userOp)

class userInterface:
    def mainMenu(self):
        stop = False

        while(not(stop)):
            print(
            '''
            1) Load Network
            2) Set probabilities
            3) find, insert or delete a person
            4) like, follow, add and remove
            5) New post
            6) Display network
            7) Display  statistics
            8) Update (run a timestep)
            9) Save network 
            10) Exit ''')

            userInput = input('Enter an option: ')
            
            stop = self._validateMainMenu(userInput)

        return userInput
    
    def executeOptions(self, userOp):
        if int(userOp) == 1:
            fileName = self.loadNetworkMenu()
            loadData = FileInterface() 
            network = loadData.createGraph(fileName)
        else if int(userOp) == 2:
            setProbabilityMenu()
        else if int(userOp) == 3:
            self.nodeOpMenu()
        else if int(userOp) == 4:
            self.edgeOpMenu()
        else if int(userOp) == 5:
            self.postMenu()
        else if int(userOp) == 6:
            
        else if int(userOp) == 7:
        else if int(userOp) == 8:
        else if int(userOp) == 9:
        else if int(userOp) == 10:
            retValue = None

        return retValue

    def nodeOpMenu(self):
        stop = False

        while(not(stop)):
            print(
            '''
            1) find a person
            2) Insert a new person
            3) delete a person ''')

            userInput = input('Enter an option: ')

            stop = self._validateNodeOpMenu(userInput)

    def edgeOpMenu(self):
        stop = False

        while(not(stop)):
            print('''
            1) like a persons post
            2) follow a person 
            3) add a person
            4) remove a person
            ''')

            userInput = input('Enter an option: ')

            stop = self._validateEdgeOpMenu(userInput)
        
        return valid

    def displayStatsMenu(self): 
        stop = False

        while(not(stop)): 
            print('''
            1) view order of popularity
            2) view people in order of popularity
            3) view a person's record
            ''')

            userInput = input('Enter an option: ')
            stop = self._validateStatsMenu(userInput)

        return userInput

    def saveNetworkMenu(self):
        pass

    def usageMenu(self):
        pass
        #print(
    
    def  _validateMainMenu(self, userOp):
        valid = False
        userOp = int(userOp)

        if (userOp == 1 or userOp == 2 or userOp == 3 or \
        userOp == 4 or userOp == 5 or userOp == 6 or \
        userOp == 7 or userOp  == 8 or userOp == 9 or \
        userOp == 10):
            valid = True  
        else:
            print('ERROR: Please enter one of the options given above')

        return valid

    def _validateNodeOpMenu(self, userOp):
        valid = False

        userOp = int(userOp)

        if (userOp == 1 or userOp == 2 or userOp = 3)
            valid = True
        else
            print('ERROR: enter option as shown above')
        
    
        return valid

    def _validateEdgeOpMenu(self, userOp):
        valid = False
        userOp = int(userOp)

        if(userOp == 1 or userOp == 2 or userOp == 3 or userOp == 4):
            valid = True
        else:
            print('ERROR: enter options given above')

    def _validateStatsMenu(self, userOP):
        valid = False
        userOp = int(userOP)

        if(userOp == 1 or userOp == 2 or userOp == 3):
            valid = True
        else: 
            print('ERROR: enter option given above')

        return valid 

    def usage(self):
        pass


if __name__ == '__main__':
    main()
