class python:
    def __init__(self):
        self.a = 1
        self.__b = 1

    def display(self):
        return self.__b


obj = python()
print(obj.__b)