import numpy as np
import copy
#input = np.loadtxt("input.txt")
reports = []
file = open("input.txt","r")
content = file.read()
reports = content.splitlines()
reports2 = []
for report in reports:
    report2 = report.split(" ")
    reports2.append([int(i) for i in report2])
file.close()
safe = 0
errors = []
for n,report in enumerate(reports2):
    difference = np.subtract(report[1:], report[:-1]) 
    if all(num in (1, 2, 3) for num in difference) or all(num in (-1, -2, -3) for num in difference):
        safe += 1
    else:
        errors.append(n)
print(safe)
#%%%        
for n in errors:
    for m,temp in enumerate(reports2[n]):
        tempreport = copy.deepcopy(reports2[n])
        tempreport.pop(m)
        difference = np.subtract(tempreport[1:], tempreport[:-1]) 
        if all(num in (1, 2, 3) for num in difference) or all(num in (-1, -2, -3) for num in difference):
            safe += 1
            #print(difference,tempreport,n)
            break
print(safe)

