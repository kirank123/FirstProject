import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

ser = pd.Series(['mary', 'had', 'a', 'little', 'lamb'])
#print(ser)
ser = ser.map(lambda x: x.title())
#print(ser)

ser = ser.map(lambda a: len(a))
#print(ser)

x = np.arange(0,10,1)
y = np.arange(0,10,1)
#print(x)

#plt.plot(x,y)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("X vs Y")
#plt.show()

data = {"apple":50, "banana":20, "orange":30} names = list(data.keys())
values = list(data.values())
plt.bar(names, values)
plt.show()

