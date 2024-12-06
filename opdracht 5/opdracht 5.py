import numpy as np
import copy
#input = np.loadtxt("input.txt")
file = open("input.txt","r")
content = file.read()
content = content.split("\n\n")
rules = content[0]

rules = rules.split("\n")
rulesarray = np.zeros((100,100))
for rule in rules:
    [x,y] = rule.split("|")
    x = int(x)
    y = int(y)
    rulesarray[x,y] = 1

updates = content[1]
updates = updates.split("\n")
updatesorder = []

for update in updates[:-1]:
    numbers = list(map(int,update.split(",")))
    numbers2 = copy.deepcopy(numbers)
    order = []
    for number in numbers:
        # print(number)
        # print(numbers2)
        dependencies = sum(rulesarray[numbers2,number])
        # print(rulesarray[numbers2,number])
        if dependencies == 0:
            order.append(number)
            numbers2.remove(number)
    # print(numbers2)
    if not numbers2: 
        updatesorder.append(order)

middlevalues = 0
for update in updatesorder:
    middlevalues += update[int((len(update)-1)/2)]
print(middlevalues)

#%%
updatesorder = []
for update in updates[:-1]:
    numbers = list(map(int,update.split(",")))
    numbers2 = copy.deepcopy(numbers)
    order = []
    for i in range(len(numbers)):
        for number in numbers2:
            dependencies = sum(rulesarray[numbers2,number])
            if dependencies == 0:
                order.append(number)
                numbers2.remove(number)
                break
    updatesorder.append(order)

middlevalues2 = 0
for update in updatesorder:
    middlevalues2 += update[int((len(update)-1)/2)]
print(middlevalues2)
middlevalues3 = middlevalues2 - middlevalues
print(middlevalues3)