import numpy as np
import copy
#input = np.loadtxt("input.txt")
file = open("input.txt","r")
content = file.read()
content = content.split("\n")
del content[-1]
colslen = len(content[0])
rowslen = len(content)
content = np.array(list("".join(content))).reshape((rowslen,colslen))
contenttransposed = content.transpose()
horizontal = ["".join(i) for i in np.transpose(content)]
vertical = ["".join(i) for i in content[:]]
diag1 = []
diag2 = []
for i in range(colslen):
    if i == 0:
        diag1.append("".join(np.diag(content,i)))
        diag2.append("".join(np.diag(contenttransposed,i)))
    else:
        diag1.append("".join(np.diag(content,i)))
        diag2.append("".join(np.diag(contenttransposed,i)))
        diag1.append("".join(np.diag(content,-i)))
        diag2.append("".join(np.diag(contenttransposed,-i)))
        
words = ["XMAS","SAMX"]
amount = 0
for word in words:
    for i in diag1:
        amount += i.count(word)
    for i in diag2:
        amount += i.count(word)
    for i in horizontal:
        amount += i.count(word)
    for i in vertical:
        amount += i.count(word)
print(amount)

# if  "MAS" == "".join(np.diag(content[n-1:n-4,m-1:m:-4])):
#     total+=1
# if  "MAS" == "".join(content[n,m-1:m-4]):
#     total+=1
# if  "MAS" == "".join(np.diag(content[n-1:n-4,m+1:m:+4])):
#     total+=1
# if  "MAS" == "".join(content[n,m+1:m+4]):
#     total+=1
# if  "MAS" == "".join(np.diag(content[n+1:n+4,m-1:m:-4])):
#     total+=1
# if  "MAS" == "".join(content[n-1:n-4,m]):
#     total+=1
# if  "MAS" == "".join(np.diag(content[n+1:n+4,m+1:m:+4])):
#     total+=1
# if  "MAS" == "".join(content[n-1:n-4,m]):
#     total+=1

total = 0
total2 = 0
sit = []
content2 = np.pad(content, [(3,3),(3,3)], mode="constant",constant_values=" ")
for n,row in enumerate(content2):
    for m,letter in enumerate(row):
        if letter == "X":
            if  "MAS" == "".join([content2[n-1,m-1],content2[n-2,m-2],content2[n-3,m-3]]):
                total+=1
                sit.append(1)
            if  "SAM" == "".join(content2[n,m-3:m]):
                total+=1
                sit.append(2)
            if  "MAS" == "".join([content2[n-1,m+1],content2[n-2,m+2],content2[n-3,m+3]]):
                total+=1
                sit.append(3)
            if  "MAS" == "".join(content2[n,m+1:m+4]):
                total+=1
                sit.append(4)
            if  "MAS" == "".join([content2[n+1,m-1],content2[n+2,m-2],content2[n+3,m-3]]):
                total+=1
                sit.append(5)
            if  "SAM" == "".join(content2[n-3:n,m]):
                total+=1
                sit.append(6)
            if  "MAS" == "".join([content2[n+1,m+1],content2[n+2,m+2],content2[n+3,m+3]]):
                total+=1
                sit.append(7)
            if  "MAS" == "".join(content2[n+1:n+4,m]):
                total+=1
                sit.append(8)
            if total2 < total:
                print(content2[n-3:n+4,m-3:m+4])
                print(n,m)
print(total)
# print(sit.count(1),sit.count(2),sit.count(3),sit.count(4),sit.count(5),sit.count(6),sit.count(7),sit.count(8))

total2 = 0
for n,row in enumerate(content2):
    for m,letter in enumerate(row):
        if letter == "A":
            if (content2[n-1,m-1] == "M" and content2[n+1,m+1] == "S") or (content2[n-1,m-1] == "S" and content2[n+1,m+1] == "M"):
                if (content2[n+1,m-1] == "M" and content2[n-1,m+1] == "S") or (content2[n+1,m-1] == "S" and content2[n-1,m+1] == "M"):
                    total2 +=1

            # if n >= 3:
            #     if n <= 136:
            #         if m >= 3:
            #             if m <= 136:

            #                     total+=1
            #             else:
            #                 if  "MAS" == "".join(np.diag(content[n-1:n-4,m-1:m:-4])):
            #                     total+=1
            #                 if  "MAS" == "".join(content[n,m-1:m-4]):
            #                     total+=1
            #                 if  "MAS" == "".join(np.diag(content[n+1:n+4,m-1:m:-4])):
            #                     total+=1
            #                 if  "MAS" == "".join(content[n-1:n-4,m]):
            #                     total+=1
            #                 if  "MAS" == "".join(content[n-1:n-4,m]):
            #                     total+=1
            #         else:
            #             if m <= 136:
            #                 if  "MAS" == "".join(np.diag(content[n-1:n-4,m+1:m:+4])):
            #                     total+=1
            #                 if  "MAS" == "".join(content[n,m+1:m+4]):
            #                     total+=1
            #                 if  "MAS" == "".join(content[n-1:n-4,m]):
            #                     total+=1
            #                 if  "MAS" == "".join(np.diag(content[n+1:n+4,m+1:m:+4])):
            #                     total+=1
            #                 if  "MAS" == "".join(content[n-1:n-4,m]):
            #                     total+=1
            #             else:
                            
            # elif n <= 136:
            #     if m >= 3:
            #         if m <= 136:
                
            #     else:
            #         if m <= 136:
            #     if  "MAS" == "".join(content[n-1:n-4,m]):
            #         total+=1
                
            #         if  "MAS" == "".join(np.diag(content[n-1:n-4,m-1:m:-4])):
            #             total+=1
            #         if  "MAS" == "".join(content[n,m-1:m-4]):
            #             total+=1
                
            #         if  "MAS" == "".join(np.diag(content[n-1:n-4,m+1:m:+4])):
            #             total+=1
            #         if  "MAS" == "".join(content[n,m+1:m+4]):
            #             total+=1
                
            
            #     if  "MAS" == "".join(content[n+1:n+4,m]):
            #         total+=1
            #     if m >= 3:
                
            #     if m <= 136:
                

                
                
            
           
# diag1 = ["".join(i) for i in ]
#content = content.view('S1').reshape((content.size, -1))
# contentvert = np.transpose(content)
# diag1 = []
# diag2 = []
# for row in range(rows+cols-1):
#     break