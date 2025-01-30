#!/usr/bin/python3
from random import randint


def bubbleSort(inputArray):
    """
    Sorts in ascending order an array of integers using bubble sort

    :param inputArray: an array of positive integers
    :return: an array of integers sorted in ascending order
    """

    # Copy the array so we are not messing up any data
    workingArray = inputArray.copy()
    length = len(inputArray)

    for i in range(length -1):
        for j in range(length -1 - i):
            leftN = workingArray[j]
            rightN = workingArray[j+1]

            if(leftN > rightN):
                workingArray[j] = rightN
                workingArray[j+1] = leftN

    return workingArray

def insertionSort(inputArray):
    """
    Sorts in ascending order an array of integers using insertion sort

    :param inputArray: an array of positive integers
    :return: an array of integers sorted in ascending order
    """
    
    length = len(inputArray)
    workingArray = inputArray.copy()
    

    for i in range(1, length):

        current = workingArray[i]

        j = i - 1

        while (j >= 0) and (workingArray[j] > current):
            workingArray[j+1] = workingArray[j]
            j = j - 1

        
        workingArray[j + 1] = current


    return workingArray

def mergeSort(inputArray):
    """
    Sorts in ascending order an array of integers using merge sort

    :param inputArray: an array of positive integers
    :return: an array of integers sorted in ascending order
    """

    if (len(inputArray) <= 1):
        return inputArray
    
    else:
        # Split the arrays
        mid = len(inputArray) // 2
        arr1 = mergeSort(inputArray[:mid])
        arr2 = mergeSort(inputArray[mid:])

    return merge(arr1, arr2)

def merge(arr1, arr2):
    """
    merges two arrays of integers to be in ascending order. This is used by the mergeSort() function

    :param arr1: an array of positive integers
    :param arr2: an array of positive integers
    :return: an array of integers sorted in ascending order
    """
    len1 = len(arr1)
    len2 = len(arr2)

    sortedArray = []
    i = j = 0

    while i < len1 and j < len2:

        if(arr1[i] <= arr2[j]):
            sortedArray.append(arr1[i])
            i = i + 1
        elif(arr1[i] >= arr2[j]):
            sortedArray.append(arr2[j])
            j = j + 1

    sortedArray.extend(arr1[i:])
    sortedArray.extend(arr2[j:])

    return sortedArray

def countSortSlow(inputArray):
    '''
    Sorts in ascending order an array of positive integers using countSort

    :param inputArray: an array of positive integers
    :return: an array of integers sorted in ascending order
    '''

    #Find the max number
    maxNum = max(inputArray)
    inputLen = len(inputArray)

    #Generate Arrays we will be using
    tallyArray = [0] * (maxNum + 1)
    tallyLen = len(tallyArray)
    sortedArray = [0] * len(inputArray)

    #Builds a tally of each numbers occurancy in the array 
    for i in range(tallyLen):
        count = 0
        for j in range(inputLen):
            if inputArray[j] == i:
                count += 1
        tallyArray[i] = count

    #Sums the occurances
    count = 0
    for i in range(tallyLen):
        count += tallyArray[i]
        tallyArray[i] = count

    #Shift the array contents one to the right
    tempPosition = 0
    for i in range(tallyLen):
        tallyArray[i], tempPosition = tempPosition, tallyArray[i]

    #Begin building the sorted Array
    sortposition = 0
    for i in range(tallyLen):

        sortedArray[tallyArray[i]] = i

        if i < tallyLen-1:
            if tallyArray[i] < tallyArray[i+1] - 1:
                sortposition = tallyArray[i]
                count = 1
                while sortposition < tallyArray[i+1]:
                    sortedArray[tallyArray[i] + count] = i
                    count += 1
                    sortposition += 1



    return sortedArray

def countSort(inputArray):
    '''
    Sorts in ascending order an array of positive integers using countSort

    :param inputArray: an array of positive integers
    :return: an array of integers sorted in ascending order
    '''


    #Find the max number
    maxNum = max(inputArray)

    #Generate Arrays we will be using
    tallyArray = [0] * (maxNum + 1)
    sortedArray = [0] * len(inputArray)

    #Construct tallyArray
    for num in inputArray:
        tallyArray[num] += 1

    #Sums the occurances
    for i in range(1, len(tallyArray)):
        tallyArray[i] = tallyArray[i - 1]

    #Place elements into their correct positions in the sorted array
    for num in reversed(inputArray):
        position = tallyArray[num] - 1
        sortedArray[position] = num
        tallyArray[num] -= 1

    return sortedArray

def quickSort(inputArray):
    '''
    Sorts in ascending order an array of postive integers using quickSort

    :param inputArray: an array of positive integers
    :return: an array of integers sorted in ascending order
    '''
    
    #Best case scenario and the array is of size 1
    if len(inputArray) <= 1:
        return inputArray
    
    #Get the pivot
    pivotPosition = randint(0, (len(inputArray)-1))
    pivot = inputArray[pivotPosition]

    #Begin sorting around the pivot
    left = []
    right = []

    for i in range(len(inputArray)):

        if i == pivotPosition:
            pass
        elif inputArray[i] > pivot:
            right.append(inputArray[i])
        elif inputArray[i] <= pivot:
            left.append(inputArray[i])

    inputArray = quickSort(left) + [pivot] + quickSort(right)

    return inputArray



def heapify(inputArray, idx, size):

    largest = idx
    left = 2 * idx + 1
    right = 2 * idx + 2

    if left < size and inputArray[left] > inputArray[largest]:
        largest = left

    if right < size and inputArray[right] > inputArray[largest]:
        largest = right

    if largest != idx:
        inputArray[idx], inputArray[largest] = inputArray[largest], inputArray[idx]


        heapify(inputArray, largest, size)

    
def buildHeap(inputArray):

    size = len(inputArray)
    startIdx = size//2 -1


    for i in range(startIdx, -1, -1):
        heapify(inputArray, i, size)

    return inputArray


def heapSort(inputArray):
    '''
    Sorts in ascending order an array of postive integers using heapSort

    :param inputArray: an array of positive integers
    :return: an array of integers sorted in ascending order
    '''

    #Build heap
    inputArray = buildHeap(inputArray)

    length = len(inputArray)

    for i in range(length-1, 0, -1):
        
        inputArray[0], inputArray[i] = inputArray[i], inputArray[0]

        heapify(inputArray, 0, i)
    
    return inputArray






























