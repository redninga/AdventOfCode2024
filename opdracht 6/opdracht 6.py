import numpy as np
import copy
import time
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
direction = "u"
walk = True

def updateDirection(direction):
    if direction == "u":
        return "r"
    elif direction == "r":
        return "d"
    elif direction == "d":
        return "l"
    elif direction == "l":
        return "u"

def side(x,y):
    if x == 0 or x == 129 or y == 0 or y == 129:
        return False
    else:
        return True


while(walk):
    if direction == "u":
        x1 = x - 1
        y1 = y
    elif direction == "r":
        x1 = x 
        y1 = y + 1
    elif direction == "d":
        x1 = x + 1
        y1 = y
    elif direction == "l":
        x1 = x 
        y1 = y - 1
    if content2[x1,y1] == "#":
        direction = updateDirection(direction)
    else:
        content2[x,y] = "X"
        x = x1
        y = y1
    walk = side(x, y)
content2[x,y] = "X"

walkpos = np.where(content2 == "X")
print(len(walkpos[0]))

#%%
timer = time.time()
content2 = []
for row in content:
    # content2.append([0 if char == "" else 1 for char in row])
    content2.append([char for char in row])
content2 = np.array(content2)

counter = 0


for iy, ix in np.ndindex(content2.shape):
    if content2[ix,iy] == ".":
        x = startx[0]
        y = starty[0]
        direction = "u"
        walk = True
        content3 = copy.deepcopy(content2)
        content3[ix,iy] = "#"
        turns = []
        
        
        while(walk):
            if direction == "u":
                x1 = x - 1
                y1 = y
            elif direction == "r":
                x1 = x 
                y1 = y + 1
            elif direction == "d":
                x1 = x + 1
                y1 = y
            elif direction == "l":
                x1 = x 
                y1 = y - 1
            if content3[x1,y1] == "#":
                turn = str(x) + " " + str(y) + " " + direction
                if turn in turns:
                    counter += 1
                    break
                turns.append(str(x) + " " + str(y) + " " + direction)
                direction = updateDirection(direction)
            else:
                # content2[x,y] = "X"
                x = x1
                y = y1
            walk = side(x, y)
    # content2[x,y] = "X"
    
    # walkpos = np.where(content2 == "X")
    # print(len(walkpos[0]))
print(counter)

timer = time.time() - timer
print(timer)


# def move(line):
    

# # while True:
# for i in range(3):
#     if direction == "up":
#         line = np.flip(content2[:x+1,y].flatten())
#     elif direction == "right":
#         line = content2[x,y:].flatten()
#     elif direction == "down":
#         line = content2[x:,y].flatten()
#     elif direction == "left":
#          line = np.flip(content2[x,:y+1].flatten())
#     else:
#         print("Error")
#     distance = np.where(line == "#")[0]
#     if distance.size == 0:
        
#         break
    
#     if direction == "up":
#         content2[x-distance[0]+1:x+1,y] = "X"
#         x = x-distance[0]+1
#     elif direction == "right":
#         content2[x,y:y+distance[0]] = "X"
#         y = y + distance[0]
#     elif direction == "down":
#         content2[x:x+distance[0],y] = "X"
#         x = x+distance[0]
#     elif direction == "left":
#         content2[x,:y+1] = "X"
#     else:
#         print("Error")
#     direction = updateDirection(direction)
    
    
    
    
#     # break