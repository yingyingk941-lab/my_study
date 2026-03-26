import numpy as np

numarray = np.zeros(10)
print('Enter ten numbers...')

for i in range(len(numarray)):
    print('Enter a number (', i, ')...')
    numarray[i] = int(input())

print('Total is ', numarray.sum())


import matplotlib.pyplot as plt

plt.title('Number Bar Chart')
plt.xlabel('Index')
plt.ylabel('Number')
plt.bar([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], numarray, 0.9, color='purple')
plt.show()

