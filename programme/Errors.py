#AUTHOR: Tawana Kwaramba
#PURPOSE: a file containg all defined exceptions
#DATE MODIFIED: 18 Aug 2019 2218
class Error(Exception):
    pass

class StackOverFlowError(Error):
    #exception raised if the stack is overfull
    def __init__(self, message):
        self.message = message

class StackUnderFlowError(Error):
    #exception raised if the stack is underful
    def __init__(self, message):
        self.message = message

class ListUnderFlowError(Error):
    def __init__(self, message):
        self.message = message

class UnsupportredOperationError(Error):
    def __init__(self, message):
        self.message = message

class VertexError(Error):
    def __init__(self, message):
        self.message = message

class EdgeError(Error):
    def __init__(self, message):
        self.message = message

class ListNodeError(Error):
    def __init__(self, message):
        self.message = message
