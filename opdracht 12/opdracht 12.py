import numpy as np
import copy
import time

#input = np.loadtxt("input.txt")
file = open("input.txt","r")
content = file.read()
content = content.split("\n")[:-1]
content2 = []
for row in content:
    content2.append([char for char in row])
content2 = np.array(content2)
content2 = np.pad(content2, [(1,1),(1,1)], mode="constant",constant_values= "#")
checked = np.zeros_like(content2,dtype= int)

def checkneighbors(x,y):
    area = 1
    perimiter = 0
    value = content2[x,y]
    checked[x,y] = 1
    if content2[x+1,y] == value:
        if checked[x+1,y] == 0:
            result = checkneighbors(x+1,y)
            # checked[x+1,y] = 1
            area += result[0]
            perimiter += result[1]
    else:
        perimiter += 1
    if content2[x-1,y] == value:
        if checked[x-1,y] == 0:
            result = checkneighbors(x-1,y)
            # checked[x-1,y] = 1
            area += result[0]
            perimiter += result[1]
    else:
        perimiter += 1
    if content2[x,y+1] == value:
        if checked[x,y+1] == 0:
            result = checkneighbors(x,y+1)
            # checked[x,y+1] = 1
            area += result[0]
            perimiter += result[1]
    else:
        perimiter += 1
    if content2[x,y-1] == value:
        if checked[x,y-1] == 0:
            result = checkneighbors(x,y-1)
            # checked[x,y-1] = 1
            area += result[0]
            perimiter += result[1]
    else:
        perimiter += 1
    return [area, perimiter]

total = 0
for x in range(len(content2)):
    for y in range(len(content2[0])):
        if checked[x,y] == 0:
            if content2[x,y] != "#":
                result = checkneighbors(x,y)
                area = result[0]
                perimiter = result[1]
                total += area * perimiter
print(total)
        
#%%

checked = np.zeros_like(content2,dtype= int)

def checkneighbors2(x,y):
    area = 1
    perimiter = 0
    x1 = [x]
    y1 = [y]
    value = content2[x,y]
    checked[x,y] = 1
    if content2[x+1,y] == value:
        if checked[x+1,y] == 0:
            result = checkneighbors2(x+1,y)
            # checked[x+1,y] = 1
            area += result[0]
            perimiter += result[1]
            x1.extend(result[2])
            y1.extend(result[3])
    else:
        perimiter += 1
    if content2[x-1,y] == value:
        if checked[x-1,y] == 0:
            result = checkneighbors2(x-1,y)
            # checked[x-1,y] = 1
            area += result[0]
            perimiter += result[1]
            x1.extend(result[2])
            y1.extend(result[3])
    else:
        perimiter += 1
    if content2[x,y+1] == value:
        if checked[x,y+1] == 0:
            result = checkneighbors2(x,y+1)
            # checked[x,y+1] = 1
            area += result[0]
            perimiter += result[1]
            x1.extend(result[2])
            y1.extend(result[3])
    else:
        perimiter += 1
    if content2[x,y-1] == value:
        if checked[x,y-1] == 0:
            result = checkneighbors2(x,y-1)
            # checked[x,y-1] = 1
            area += result[0]
            perimiter += result[1]
            x1.extend(result[2])
            y1.extend(result[3])
    else:
        perimiter += 1
    return [area, perimiter, x1, y1]

total = 0
for x in range(len(content2)):
    for y in range(len(content2[0])):
        if checked[x,y] == 0:
            if content2[x,y] != "#":
                result = checkneighbors2(x,y)
                area = result[0]
                perimiter = result[1]
                total += area * perimiter
                gardens = list(zip(result[2],result[3]))