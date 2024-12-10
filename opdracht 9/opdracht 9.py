import numpy as np
import copy
import time



#input = np.loadtxt("input.txt")
file = open("input.txt","r")
content = file.read()
content = content.split("\n")[0]
# content2 = []
locations = 0
for i in content:
    locations += int(i)
c = np.zeros(locations,int)
c[:] = -1
location = 0
numbers = 0
zeroes = 0
for n,i in enumerate(content):
    if n % 2 == 0:
        c[location:location+int(i)] = (n / 2) 
        numbers += int(i)
    else:
        zeroes += int(i)
    location += int(i)

xzeroes = np.where(c == -1)[0]
nzeroes = np.where(c != -1)[0]
c2 = copy.deepcopy(c)

n = 1
for i in range(numbers):
    if c2[i] == -1:
        c2[i] = c2[nzeroes[-n]]
        c2[nzeroes[-n]] = -1
        n += 1

total = np.int64(0)
for n,i in enumerate(c2):
    if i != -1:
        print(i, n)
        total += i*n