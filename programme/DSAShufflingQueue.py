################################################################################
# AUTHOR: Tawana David Kwaramba                                                #
# STUDENT: NUMBER: 19476700                                                    #
# PURPOSE:  This class defines a shuffling queue which inherits from the       #
#           queue supper class                                                 # 
# LAST MODIFIED:  4/09/19 16:00                                                #
################################################################################


from DSAQueue import Queue
from Errors import StackOverFlowError
from Errors import StackUnderFlowError
import numpy as np 

class ShufflingQueue(Queue):
    def __init__(self):
        super().__init__()
    
    def dequeue(self):
        removedValue = self.queue.peekFirst()
        self.queue.removeFirst()
        self.count -=  1
        return removedValue

    def enqueue(self, value):
        self.count += 1 
        self.queue.insertLast(value)
