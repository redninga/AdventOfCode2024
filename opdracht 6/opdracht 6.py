import numpy as np
import copy
#input = np.loadtxt("input.txt")
file = open("input.txt","r")
content = file.read()
content = content.split("\n")[:-1]
# content2 = [[i] for i in [row for row in content]]
content2 = []
for row in content:
    # content2.append([0 if char == "" else 1 for char in row])
    content2.append([char for char in row])
content2 = np.array(content2)
[startx,starty] = np.where(content2 == "^")
x = startx[0]
y = starty[0]
direction = "up"

def updateDirection(direction):
    if direction == "up":
        return "right"
    elif direction == "right":
        return "down"
    elif direction == "down":
        return "left"
    elif direction == "left":
        return "up"

# def move(line):
    

# while True:
for i in range(3):
    if direction == "up":
        line = np.flip(content2[:x+1,y].flatten())
    elif direction == "right":
        line = content2[x,y:].flatten()
    elif direction == "down":
        line = content2[x:,y].flatten()
    elif direction == "left":
         line = np.flip(content2[x,:y+1].flatten())
    else:
        print("Error")
    distance = np.where(line == "#")[0]
    if distance.size == 0:
        
        break
    
    if direction == "up":
        content2[x-distance[0]+1:x+1,y] = "X"
        x = x-distance[0]+1
    elif direction == "right":
        content2[x,y:y+distance[0]] = "X"
        y = y + distance[0]
    elif direction == "down":
        content2[x:x+distance[0],y] = "X"
        x = x+distance[0]
    elif direction == "left":
        content2[x,:y+1] = "X"
    else:
        print("Error")
    direction = updateDirection(direction)
    
    
    
    
    # break