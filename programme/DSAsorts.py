################################################################################
#Modified by Tawana Kwaramba: 19476700                                         # 
# Data Structures and Algorithms COMP1002                                      # 
# Python file to hold all sorting methods                                      # 
#last dat to be modified:                                                      # 
#this programme is deisgned to run in python3                                  #
################################################################################
def bubbleSort(A):
    sort = False 

    while not sort:
        sort = True
        for ii in range(len(A) - 1):
            #if the first index is smaller than the next. Swap them
            if A[ii] > A[ii+1]:
                A = swap(A, ii)
                sort = False
        
    return A 

def insertionSort(A):
    nn = 1
    for nn in range(len(A)):
        ii = nn
        
        while (( ii > 0) and (A[ii -1]) > A[ii]):
            temp = A[ii] 
            A[ii] = A[ii - 1]
            A[ii - 1] = temp 
            ii = ii - 1

    return A

def selectionSort(A):
    for nn in range(0,len(A) - 1, 1):
        #automatically setting the minimum variable as the first index
        minIndx = nn

        #moving to the next element in the array 
        #jj = ii + 1
        for jj in range(nn + 1, len(A), 1): 

            #if any element is smaller than the previouse set minumum value
            #set that value to the new minimum value 
            if (A[jj] < A[minIndx]):
                minIndx = jj

        temp = A[minIndx]
        A[minIndx] = A[nn]
        A[nn] = temp

    return A 

def mergeSort(A):
    pass
    """ mergeSort - front-end for kick-starting the recursive algorithm
    """
    pass

def mergeSortRecurse(A, leftIdx, rightIdx):
    pass

def merge(A, leftIdx, midIdx, rightIdx):
    pass

def quickSort(A):
    pass
    """ quickSort - front-end for kick-starting the recursive algorithm
    """

def quickSortRecurse(A, leftIdx, rightIdx):
    pass

def doPartitioning(A, leftIdx, rightIdx, pivotIdx):
    pass

#this function is responsible for swapping around adjacent array indexs for the
#various sorting algorithms availble 
def swap(array, index):
    tempVar = array[index]
    array[index] = array[index + 1]
    array[index + 1] = tempVar

    return array
