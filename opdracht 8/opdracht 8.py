import numpy as np
import copy
import time

def antinode(x,y):
    xnode = []
    ynode = []
    for n in range(len(x)-1):
        for m in range(n+1,len(x)):
            xnode.append(2*x[n]-x[m]) #abs(x[n]-x[m])
            ynode.append(2*y[n]-y[m]) 
            xnode.append(2*x[m]-x[n])
            ynode.append(2*y[m]-y[n]) 
            
    return [xnode,ynode]


#input = np.loadtxt("input.txt")
file = open("input.txt","r")
content = file.read()
content = content.split("\n")[:-1]
content2 = []
for row in content:
    # content2.append([0 if char == "" else 1 for char in row])
    content2.append([char for char in row])
content2 = np.array(content2)
antinodes = np.zeros_like(content2)
uniquevalues = list(set(str(i) for j in content2 for i in j))
del uniquevalues[uniquevalues.index(".")]
x = []
y = []
for value in uniquevalues:
    location = np.where(content2 == value)
    #print(location)
    if len(location[0]) >= 2:
        # print(location[0],location[1])
        antinodes = antinode(location[0],location[1])
        x.extend(antinodes[0])
        y.extend(antinodes[1])

antinodesarray = np.zeros_like(content2)
for n,i in enumerate(x):
    if x[n] < 0 or x[n] > 49 or y[n] < 0 or y[n] > 49:
        pass
    else:
        antinodesarray[x[n], y[n]] = 1
antinodesbounded = np.where(antinodesarray == "1")
print(len(antinodesbounded[0]))
            
#%%

def antinode2(x,y):
    xnode = []
    ynode = []
    for n in range(len(x)-1):
        for m in range(n+1,len(x)):
            for i in range(0,50):
                print(n,m,i)
                xnode.append(x[n] + i*(x[n]-x[m])) #abs(x[n]-x[m])
                ynode.append(y[n] + i*(y[n]-y[m])) 
                xnode.append(x[m] + i*(x[m]-x[n]))
                ynode.append(y[m] + i*(y[m]-y[n])) 
    return [xnode,ynode]

x = []
y = []
for value in uniquevalues:
    location = np.where(content2 == value)
    #print(location)
    if len(location[0]) >= 2:
        # print(location[0],location[1])
        antinodes = antinode2(location[0],location[1])
        x.extend(antinodes[0])
        y.extend(antinodes[1])

antinodesarray = np.zeros_like(content2)
for n,i in enumerate(x):
    if x[n] < 0 or x[n] > 49 or y[n] < 0 or y[n] > 49:
        pass
    else:
        antinodesarray[x[n], y[n]] = 1
antinodesbounded = np.where(antinodesarray == "1")
print(len(antinodesbounded[0]))