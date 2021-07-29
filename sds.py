class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def fun(self):
        print(f"name is {self.name}")
        print(f"age is {self.age}")


person1 = Person("Kiran", 29)
person1.fun()
