import numpy as np
import copy
import time
#input = np.loadtxt("input.txt")
file = open("input.txt","r")
content = file.read()
content = content.split("\n")[:-1]
answers = []
numbers = []
for row in content:
    answers.append(int(row.split(":")[0]))
    row2 = []
    for i in row.split(" ")[1:]:
        row2.append(int(i))
    numbers.append(row2)


def multiply(x,y):
    return x*y

def add(x,y):
    return x+y

def concat(x,y):
    return int(str(x) + str(y))

def completelist(x,numbers,answer):
    if len(numbers) == 0:
        if x == answer:
            return True
        else:
            return False
    y = copy.deepcopy(numbers[0])
    numbers2 = copy.deepcopy(numbers)
    del numbers2[0]
    # print(x,y, numbers)
    z1 = completelist(multiply(x, y),numbers2,answer)
    z2 = completelist(add(x, y),numbers2,answer)
    if z1 or z2:
        return True
    else:
        return False
    
total = 0
possible = 0
counter = 0
for i in range(len(answers)):
    answer = answers[i]
    if completelist(numbers[i][0],numbers[i][1:],answer):
        possible += answer
        counter += 1
print(possible)

#%%

def completelist2(x,numbers,answer):
    if len(numbers) == 0:
        if x == answer:
            return True
        else:
            return False
    y = copy.deepcopy(numbers[0])
    numbers2 = copy.deepcopy(numbers)
    del numbers2[0]
    # print(x,y, numbers)
    z1 = completelist2(multiply(x, y),numbers2,answer)
    z2 = completelist2(add(x, y),numbers2,answer)
    z3 = completelist2(concat(x, y),numbers2,answer)
    if z1 or z2 or z3:
        return True
    else:
        return False

total = 0
possible = 0
counter = 0
for i in range(len(answers)):
    answer = answers[i]
    if completelist2(numbers[i][0],numbers[i][1:],answer):
        possible += answer
        counter += 1
        #print(counter,i)
print(possible)