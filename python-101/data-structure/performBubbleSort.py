import random

N = 10
lstNumbers = list(range(N))
random.shuffle(lstNumbers)

print(lstNumbers)

def performBubbleSort(lstNumbers):
    for itr1 in range(N):
        for itr2 in range(N - 1):
            if lstNumbers[itr2] > lstNumbers[itr2 + 1]:
                lstNumbers[itr2], lstNumbers[itr2 + 1] = \
                    lstNumbers[itr2 + 1], lstNumbers[itr2]
    return lstNumbers

print(performBubbleSort(lstNumbers))