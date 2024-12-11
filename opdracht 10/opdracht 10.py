import numpy as np
import copy
import time

#input = np.loadtxt("input.txt")
file = open("input.txt","r")
content = file.read()
content = content.split("\n")[:-1]
content2 = np.zeros((len(content),len(content[0])),int)
for n,row in enumerate(content):
    for m,i in enumerate(row):
        content2[n,m] = int(i)

content2 = np.pad(content2, [(1,1),(1,1)], mode="constant",constant_values= -1)

trailheadsvalues = np.zeros_like(content2)
trailheadsvalues2 = np.zeros_like(content2)

def trail(x,y,array):
    value = array[x,y]
    if value == 9:
        return [[x],[y]]
    else:
        x2 = []
        y2 = []
        if array[x,y+1] == value + 1:
            result = trail(x,y+1,array)
            # print(result)
            x2.extend(result[0])
            y2.extend(result[1])
        if array[x,y-1] == value + 1:
            result = trail(x,y-1,array)
            # print(result)
            x2.extend(result[0])
            y2.extend(result[1])
        if array[x+1,y] == value + 1:
            result = trail(x+1,y,array)
            # print(result)
            x2.extend(result[0])
            y2.extend(result[1])
        if array[x-1,y] == value + 1:
            result = trail(x-1,y,array)
            # print(result)
            x2.extend(result[0])
            y2.extend(result[1])
    return [x2,y2]

# def unpacklists(nested):
#     result = []
#     for i in nested:
#         if isinstance(i, list):
#             result.

for x in range(len(content2)):
    for y in range(len(content2[0])):
        if content2[x,y] == 0:
            result = trail(x,y,content2)
            x2 = result[0]
            y2 = result[1]
            tops = list(zip(x2,y2))
            trailheadsvalues[x,y] =  len(set(tops))
            trailheadsvalues2[x,y] = len(x2)
print(sum(sum(trailheadsvalues)))
print(sum(sum(trailheadsvalues2)))