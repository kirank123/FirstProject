class Mainclass:
    def __init__(self, name):
        self.name = name

    def fun(self):
        print("Hi")


class Subclass(Mainclass):
    def __init__(self, num):
        self.num = num

    def fun1(self, abc):
        abc = abc *abc
        return print(abc)


M1 = Mainclass("Kiran")
S1 = Subclass(10)

M1.fun()
S1.fun()
S1.fun1(5)




A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
print(A0)
print(A1)
print(A2)
print(A3)
print(A4)
print(A5)
print(A6)


def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while n > 1:
            fact *= n
            n -= 1
        return fact


num = 5
fact = factorial(num)
print(f"Factorial of {num} is {fact}")




import pandas as pd

s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([2, 3, 5, 6, 8])
print("Items in series1 not present in series 2")
res = s1[~s1.isin(s2)]
print(res)


