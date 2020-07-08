import random

N = 10
lstNumbers = list(range(N))
random.shuffle(lstNumbers)

print(lstNumbers)

def performInsertionSort(lstNumbers):
    for itr1 in range(1, N):
        key = lstNumbers[itr1]
        itr2 = itr1 - 1
        while itr2 >= 0 and lstNumbers[itr2] > key:
            lstNumbers[itr2 + 1] = lstNumbers[itr2]
            itr2 = itr2 - 1
            lstNumbers[itr2 + 1] = key
    return lstNumbers

print(performInsertionSort(lstNumbers))
