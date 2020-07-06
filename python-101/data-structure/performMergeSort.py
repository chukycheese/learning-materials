import random

def performMergeSort(numList):
    if len(numList) == 1:
        return numList
    
    numSubList1 = []
    numSubList2 = []
    
    # Decomposition
    for itr in range(len(numList)):
        if len(numList) / 2 > itr:
            numSubList1.append(numList[itr])
        else:
            numSubList2.append(numList[itr])

    # Recursion
    numSubList1 = performMergeSort(numSubList1)
    numSubList2 = performMergeSort(numSubList2)

    # Aggregation
    idxCount1 = 0
    idxCount2 = 0

    for itr in range(len(numList)):
        if idxCount1 == len(numSubList1):
            numList[itr] = numSubList2[idxCount2]
            idxCount2 += 1
        elif idxCount2 == len(numSubList2):
            numList[itr] = numSubList1[idxCount1]
            idxCount1 += 1
        elif numSubList1[idxCount1] > numSubList2[idxCount2]:
            numList[itr] = numSubList2[idxCount2]
            idxCount2 += 1
        else:
            numList[itr] = numSubList1[idxCount1]
            idxCount1 += 1
    return numList

N = 10
numLists = list(range(N))
random.shuffle(numLists)
print(numLists)

numLists = performMergeSort(numLists)
print(numLists)