import time
from concurrent.futures import ThreadPoolExecutor


def charnum(word, n=0, al=0):
    for i in word:
        if i.isdigit():
            n += 1
        if i.isalpha():
            al += 1

#    time.sleep(5)
    print(f" number of numbers in string is {n}")
    print(f" number of letter is {al}")
    print("#####")


str1 = "hello world! 123"
#charnum(str1)
str2 = "mallisseril213  !@$"
#charnum(str2)
str3 = "hello SFDSAFA 3432 5)a)(n){ibnPIU 9n)"
#charnum(str3)


def multiprocessing_tasks(tasks):
    with ThreadPoolExecutor() as executor:
        runnning_tasks = [executor.submit(task) for task in tasks]
        for runnning_task in runnning_tasks:
            runnning_task.result()


multiprocessing_tasks([
    lambda: charnum(str1),
    lambda: charnum(str2),
    lambda: charnum(str3)
])


def smart_divide(func):
    def inner(a, b):
        print(f"going to divide {a} and {b}")
        if b == 0:
            print("Division by 0 is not possible")
            return
        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)


divide(5,0)


mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


from abc import ABC, abstractmethod

class Polygon(ABC):

    @abstractmethod
    def sides(self):
        print("Abstract Base class")


class Triangle(Polygon):
    def sides(self):
        super().sides()
        print("3 sides")


t = Triangle()
t.sides()

print(issubclass(Triangle, Polygon))
print(isinstance(Triangle(), Polygon))


list1 = ['a', 'b', 'c']
str1 = ''.join(list1)
print(str1)
print("hello")
print(str(list1))

list = ["1", "4", "0", "6", "9"]
list = [int(i) for i in list]
#list = ','.join(list)
list.sort()
print(list)



A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
print(A0,A1,A2,A3,A4,A5,A6)

dict1 ={'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(dict1.keys())
print(dict1.values())
print([dict1[s] for s in dict1])


for i in range(-20, 20, 4):
    print(i)

String = 'GeeksForGeeks'
set1 = set(String)
print("\nSet with the use of an Object: " )
print(set1)



letters = set()
with open(r"C:\Users\kiran\OneDrive\Desktop\filewrite.txt") as countletter:
    count = 0
    text = countletter.read()
    for character in text:
        if character.isupper():
            count += 1
            letters.add(character)
print(count)


# Python code to sort a list without
# creating another list Use of sort()
def Sorting(lst):
    lst.sort(key=len)
    return lst


# Driver code
lst = ["rohan", "amy", "sapna", "muhammad", "aakash", "raunak", "chinmoy"]
print(Sorting(lst))


lst = ["rohan", "amy", "sapna", "muhammad", "aakash", "raunak", "chinmoy"]
print(lst)
lst = lst.sort(key=len)
print(lst.sort(key=len))


a =[1,4,6,3,34,7,3,2,74,32,311,322]
b = ["geeks", "code", "ide", "practice"]
print(a)
a.sort(reverse=True)
print(a)
print(b)
b.sort(key=len)
print(b)


def sortSecond(val):
    return val[1]
# list1 to demonstrate the use of sorting
# using using second key
list1 = [(1, 2), (3, 3), (1, 1)]
# sorts the array in ascending according to
# second element
list1.sort(key=sortSecond)
print(list1)
# sorts the array in descending according to
# second element
list1.sort(key=sortSecond, reverse=True)
print(list1)

# of list index() method

list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5]

# Will print the index of '4' in list1
print(list1.index(4))

list2 = ['cat', 'bat', 'mat', 'cat', 'pet']

# Will print the index of 'cat' in list2
print(list2.index('cat'))

list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5]

# Will print index of '4' in sublist
# having index from 4 to 8.
print("*********")
n =list1.index(4)
print(list1.index(4, n+1, len(list1)))
print("*********")


# Will print index of '1' in sublist
# having index from 1 to 7.
print(list1.index(1, 1, 7))
