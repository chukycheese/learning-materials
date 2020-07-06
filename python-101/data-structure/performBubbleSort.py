import random

N = 10
firstNumbers = list(range(N))
random.shuffle(firstNumbers)

print(firstNumbers)

def performBubbleSort(firstNumbers):
    for itr1 in range(len(firstNumbers)):
        for itr2 in range(itr1 + 1, N):
            if firstNumbers[itr1] < firstNumbers[itr2]:
                firstNumbers[itr1], firstNumbers[itr2] = \
                    firstNumbers[itr2], firstNumbers[itr1]

    return firstNumbers

print(performBubbleSort(firstNumbers))