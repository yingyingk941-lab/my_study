import numpy as np

numarray = np.zeros(10)
print('Enter ten numbers...')

for i in range(len(numarray)):
    print('Enter a number (', i, ')...')
    numarray[i] = int(input())

print('Total is ', numarray.sum())

