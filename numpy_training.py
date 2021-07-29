import numpy as np
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
x = np.where(a == b)
print(x)

# import the pandas lib as pd
import pandas as pd

# create a dictionary
dict = {'A': 10, 'B': 20, 'C': 30}

# create a series
series = pd.Series(dict)

print(series)




import numpy as np
import pandas as pd
array = np.array([[1, 'a'], [2, 'b'], [3, 'c'], [4, 'd']])
df = pd.DataFrame(array)
print(df)


def fibonacci_sum(N):
    if N == 0:
        return 0
    Sum = 0
    a, b = 1, 1
    Sum += a
    while b <= N:
        Sum += b
        a, b = b, a + b
    return Sum

N=100
print(fibonacci_sum(N))


import re
def change_date_format(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{2,3})', '\\3-\\2-\\1', dt)
dt1 = "2026-01-223"
print("Original date in YYY-MM-DD Format: ",dt1)
print("New date in DD-MM-YYYY Format: ",change_date_format(dt1))