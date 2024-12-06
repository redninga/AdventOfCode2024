import numpy as np
import copy
#input = np.loadtxt("input.txt")
reports = []
file = open("input.txt","r")
content = file.read()
numbers = ['0','1','2','3','4','5','6','7','8','9']
start = "mul("
seperator = ","
end = ")"
content2 = content.split(start)

def numberlength(string):
    if string[0] in numbers:
        if string[1] in numbers:
            if string[2] in numbers:
                return 3
            else:
                return 2
        else:
            return 1
    return 0
        
total = 0
indexes = []
n1list = []
n2list = []
enabled = True
for n,i in enumerate(content2):
    if enabled:
        n1len = numberlength(i)
        if n1len != 0:
            n1 = int(i[:n1len])
            if i[n1len] == seperator:
                n2len = numberlength(i[n1len+1:])
                if n2len != 0:
                    if i[n1len+n2len+1] == end:
                        n2 = int(i[n1len+1:n1len+1+n2len])
                        total += n1 * n2
                        print(n,i[:n1len+1+n2len],n1,n2 , total)
                        indexes.append(n)
                        n1list.append(n1)
                        n2list.append(n2)
    if "do()" in i:
        enabled = True
    elif "don't()" in i:
        enabled = False
        

wrongindexes = [i for i in range(len(content2)) if i not in indexes]

#%%
# for i in wrongindexes:
#     print(content2[i])