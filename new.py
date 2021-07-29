name = "kirankrishnan"
dup = []
np = []



def dup_check(name):
    for i in name:
        if i not in dup:
            dup.append(i)
        elif i not in np:
            np.append(i)
    return np, dup


print(list(dup_check(name)))

for i in name:
    if not name.count(i) >= 2:
        print(i)


ddp = [x for x in name if not name.count(x) >= 2]
print(list(x for x in name if not name.count(x) >= 2))

import numpy as np
import pandas as pd

a = np.zeros((5,5))
print(a)

a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.sum((a,b), axis=0))
print(np.sum((a,b), axis=1))


x = np.array([12, 24, 45, 11, 9, 66, 89, 3, 99])
print(x[np.argsort(x)])
print(np.argsort(x)[-2:][::-1])
print(x[np.argsort(x)[-2:][::-1]])

l1 = [1,2,3,4]
data1 = pd.DataFrame(l1)
print(data1)
dt1 = {'fruit_name':['apple', 'mango', 'orange'], 'count':[12, 24, 36]}

data2 = pd.DataFrame(dt1)
print(data2)

# printing prime numbers from 1 to 100
for i in range(0, 101):
    if i > 1:
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
            print(i)