from DSALinkList import DSALinkList
from DSAStack import Stack 

class Person:
    def __init__(self, inTitle, inName):
        self._name = self._validateName(inName)
        self._liking = Stack()
        self._likes = Stack()
        self._followers = Stack()
        self._following = Stack()
        self._posts = Stack()
        #hard coded probability for a person liking an given persons posts
        self._intialProb = 0.05

    def __str__(self):
        return ('%s %s | likes: %s | followers: %s | following: %s'% 
        (self._title, self._name, self.getLikes().getCount(), 
        self.getFollowers().getCount(), self.getFollowing().getCount()))
        #return ('%s %s' % (self._title, self._name))

    def _validateName(self, inName): 

        if(inName == None):
            raise ValueError('ERORR: a person has to have a name')

        return inName

    #ACCESSORS
    def getFollowers(self):
        return self._followers

    def getFollowing(self):
        return self._following

    def getLiking(self):
        return self._liking
    
    def getLikes(self):
        return self._likes

    def getTitle(self):
        return self._title 

    def getName(self):
        return self._name

    def getPosts(self):
        return self._posts

    def addLiker(self, inValue):
        self._likes.push(inValue)

    def addLiking(self, inValue):
        self._liking.push(inValue)

    def addFollower(self, inValue):
        self._followers.push(inValue)

    def addFollowinng(self, inValue):
        self._following.push(inValue)
    
