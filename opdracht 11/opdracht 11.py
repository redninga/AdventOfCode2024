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

now = time.time()
stones = copy.deepcopy(content2)
for i in range(75):
    stones2 = []
    # print(i)
    for stone in stones:
        stones2.extend(rules(stone))
    stones = stones2
print(len(stones))
end = time.time()
print(now-end)