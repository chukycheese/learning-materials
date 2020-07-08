#%%
import random

N = 10
lstNumbers = list(range(N))
random.shuffle(lstNumbers)

print(lstNumbers)

def performSelectionSort(lstNumbers):
    for itr1 in range(0, N):
        for itr2 in range(itr1 + 1, N):
            if lstNumbers[itr1] < lstNumbers[itr2]:
                lstNumbers[itr1], lstNumbers[itr2] =\
                    lstNumbers[itr2], lstNumbers[itr1]
    return lstNumbers

print(performSelectionSort(lstNumbers))