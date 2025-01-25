#!/usr/bin/python3



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
        