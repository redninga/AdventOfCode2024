import numpy as np
import copy
import time
import re
import math

#input = np.loadtxt("input.txt")
file = open("input.txt","r")
content = file.read()
content = content.split("\n\n")
total = 0
for row in content:
    temp = row.split("\n")
    buta = temp[0]
    butb = temp[1]
    solution = temp[2]
    xa = int(buta[buta.find("X+") + 2:buta.find(", ")])
    ya = int(buta[buta.find("Y+") + 2:])
    xb = int(butb[butb.find("X+") + 2:butb.find(", ")])
    yb = int(butb[butb.find("Y+") + 2:])
    sx = int(solution[solution.find("X=") + 2:solution.find(", ")])
    sy = int(solution[solution.find("Y=") + 2:])
    
    gaus1 = ya/xa
    ya2 = ya-gaus1*xa
    yb2 = yb-gaus1*xb
    sy2 = sy-gaus1*sx
    b = round(sy2/yb2,0)
    a = round((sx - xb * b)/xa,0)
    # if a < 0 or a > 100 or b < 0 or b > 100:
    #     print("Error too big or small")
    if a * xa + b * xb == sx and a * ya + b * yb == sy:
        # print(a,b)
        total += a * 3 + b
    else:
        # print("error",a, b)
        pass
        
    
    a2 = (sx*yb-xb*sy)/(xa*yb-xb*ya)
    b2 = (xa*sy-sx*ya)/(xa*yb-xb*ya)
    # print(a2,b2)
print(total)

#%%
add = np.int64(10000000000000)

total = np.int64(0)
for row in content:
    temp = row.split("\n")
    buta = temp[0]
    butb = temp[1]
    solution = temp[2]
    xa = np.int64(buta[buta.find("X+") + 2:buta.find(", ")])
    ya = np.int64(buta[buta.find("Y+") + 2:])
    xb = np.int64(butb[butb.find("X+") + 2:butb.find(", ")])
    yb = np.int64(butb[butb.find("Y+") + 2:])
    sx = np.int64(solution[solution.find("X=") + 2:solution.find(", ")]) + add
    sy = np.int64(solution[solution.find("Y=") + 2:]) + add
    
    gaus1 = ya/xa
    ya2 = ya-gaus1*xa
    yb2 = yb-gaus1*xb
    sy2 = sy-gaus1*sx
    b = round(sy2/yb2,0)
    a = round((sx - xb * b)/xa,0)
        
    a2 = (sx*yb-xb*sy)/(xa*yb-xb*ya)
    b2 = (xa*sy-sx*ya)/(xa*yb-xb*ya)
    
    if a * xa + b * xb == sx and a * ya + b * yb == sy:
        print(a-a2,b-b2)
        total += int(a) * 3 + int(b)
        # if a < 0 or b < 0:
        #     print(a,b)
    else:
        # print("error",(sx - xb * b)/xa, sy2/yb2)
        pass
        


    # print(a2,b2)
print(total)