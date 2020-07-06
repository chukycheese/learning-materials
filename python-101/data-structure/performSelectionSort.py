#%%
import random

N = 10
firstNumbers = list(range(N))
random.shuffle(firstNumbers)

print(firstNumbers)

def performSelectionSort(firstNumbers):
    for i in range(len(firstNumbers) - 1):
        min_idx = i
        for j in range(i + 1, len(firstNumbers)):
            if firstNumbers[j] < firstNumbers[min_idx]:
                min_idx = j
        firstNumbers[i], firstNumbers[min_idx] = firstNumbers[min_idx], firstNumbers[i]
    return firstNumbers

print(performSelectionSort(firstNumbers))