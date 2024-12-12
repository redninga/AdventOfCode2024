import numpy as np
import copy
import time

#input = np.loadtxt("input.txt")
file = open("input.txt","r")
content = file.read()
content = content.split("\n")[:-1]
content2 = [int(i) for i in content[0].split(" ")]

def rules(stone):
    if stone == 0:
        return rule1(stone)
    elif len(str(stone)) % 2 == 0:
        return rule2(stone)
    else:
        return rule3(stone)

def rule1(stone):
    return [1]

def rule2(stone):
    stone2 = str(stone)
    length = len(stone2)
    length2 = int(length/2)
    stones = [int(stone2[:length2]),int(stone2[length2:])]
    return stones

def rule3(stone):
    return [stone * 2024]

stones = copy.deepcopy(content2)


for i in range(25):
    stones2 = []
    # print(i)
    for stone in stones:
        stones2.extend(rules(stone))
    stones = stones2
print(len(stones))

# now = time.time()
# stones = copy.deepcopy(content2)
# for i in range(75):
#     stones2 = []
#     for stone in stones:
#         stones2.extend(rules(stone))
#     stones = stones2
#     print(i, len(stones))
# print(len(stones))
# end = time.time()
# print(now-end)

#%%

stones3 = {i:1 for i in content2}
for i in range(75):
    stones4 = {}
    for j in stones3:
        for k in rules(j):
            if k in stones4:
                stones4[k] += stones3[j]
            else:
                stones4[k] = stones3[j]
    stones3 = stones4

total = np.int64(0)
for i in stones3:
    total+= stones3[i]

# now = time.time()
# stones = copy.deepcopy(content2)
# stones = [stones[0]]
# for i in range(75):
#     stones2 = []
#     for stone in stones:
#         stones2.extend(rules(stone))
#     print(i,len(stones2)/len(stones), len(stones))
#     stones = stones2
# print(len(stones))
# end = time.time()
# print(now-end)