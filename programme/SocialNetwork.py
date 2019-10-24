from enum import Enum

class SocialNetwork:
    def follow(self, personOne, personTwo):
        personTwo.getVertexLabel().addFollower(personOne)
        personOne.addEdge(personTwo)       

    def like(self, personOne, personTwo):
        sendTo = personOne.getAdjacent()
        self._notifyFollowersOfLike(sendTo)
        personTwo.getVertexLabel().addLiker(personOne)
    
    def post(self, poster):
        sendTo = poster.getAdjacent()
        self._postInfo(sendTo)

    def post(self, personOne, personTwo, post):
        sendTo = personOne.getAdjacent()
        self._notifyFollowersOfPost(sendTo)

    def  _postInfo(self, listReceiptents):
        pass

    def _notifyFollowersOfLike(self, listOfReciptents):
        pass
    
    def _notifyFollowersOfPost(self, listOfReciptents):
        pass 

class _SocialInteraction(Enum):
    LIKE = 1
    FOLLOW = 2
    FOLLOWING = 3
