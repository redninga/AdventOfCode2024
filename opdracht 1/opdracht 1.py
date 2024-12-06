file = open("input.txt","r")
content =file.read()
file.close()

import numpy as np

file2 = np.loadtxt("input.txt")
array1 = file2[:,0]
array2 = file2[:,1]

array1 = np.sort(array1)
array2 = np.sort(array2)

difference = abs(array1-array2)
totaldif = sum(difference)
print(totaldif)

#%%
simularity = 0
for i in array1:
    simularity += i* sum(array2 == i)
print(simularity)