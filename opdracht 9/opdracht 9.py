import numpy as np
import copy
import time



#input = np.loadtxt("input.txt")
file = open("input.txt","r")
content = file.read()
content = content.split("\n")[0]
# content2 = []
locations = 0
for i in content:
    locations += int(i)
c = np.zeros(locations,int)
c[:] = -1
location = 0
numbers = 0
zeroes = 0
for n,i in enumerate(content):
    if n % 2 == 0:
        c[location:location+int(i)] = (n / 2) 
        numbers += int(i)
    else:
        zeroes += int(i)
    location += int(i)

xzeroes = np.where(c == -1)[0]
nzeroes = np.where(c != -1)[0]
c2 = copy.deepcopy(c)

n = 1
for i in range(numbers):
    if c2[i] == -1:
        c2[i] = c2[nzeroes[-n]]
        c2[nzeroes[-n]] = -1
        n += 1

total = np.int64(0)
for n,i in enumerate(c2):
    if i != -1:
        # print(i, n)
        total += i*n

#%%
        
content2 = [i for i in content]
values = []
for n,i in enumerate(content2):
    if n % 2 == 0:
        values.append(int(n/2))
    else:
        values.append(-1)

values2 = copy.deepcopy(values)

# for n,i in enumerate(content2[::-1]):
#     if values[-(n+1)] != -1:
#         for m,j in enumerate(content2[:-(n+1)]):
#             if values[m] == -1:
#                 if j >= i:
#                     values[m] = values[-(n+1)]
#                     values[-(n+1)] = -1# nog overige delen berekenen en dan

# c3 = []
# for n in range(len(values)):
#     for i in range(int(content2[n])):
#         c3.append(values[n])
    
# total2 = np.int64(0)
# for n,i in enumerate(c3):
#     if i != -1:
#         # print(i, n)
#         total2 += i*n
#%%

def find_sequence(array, sequence):
    # Create a sliding window view of the array
    seq_len = len(sequence)
    windows = np.lib.stride_tricks.sliding_window_view(array, seq_len)
    
    # Compare each window with the sequence
    matches = np.all(windows == sequence, axis=1)
    
    # Get the starting indices of the matches
    indices = np.where(matches)[0]
    return indices

def numberlength(array,number):
    return len(np.where(array == number)[0])
    
def numberindexstart(array,number):
    return np.where(array == number)[0][0]

c3 = copy.deepcopy(c)



for i in range(9999,0,-1):
    length = numberlength(c3,i)
    position = numberindexstart(c3,i)
    sequence = [-1] * length
    newposition = find_sequence(c3[:position], sequence)
    if newposition.size != 0:
        c3[newposition[0]:newposition[0] + length] = i
        c3[position:position+length] = -1
    #print(newposition[0])
    #print(i, length, position)

total2 = np.int64(0)
for n,i in enumerate(c3):
    if i != -1:
        # print(i, n)
        total2 += i*n
print(total2)