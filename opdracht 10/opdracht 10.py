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

trailheadsvalues = np.zeros_like(2)

def trail(x,y,array):
    value = x


for x in range(54):
    for y in range(54):
        if content2[x,y] == 0:
            