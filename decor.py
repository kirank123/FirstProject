def caps(text):
    return text.upper()


def small(text):
    return text.lower()


def greet(func):
    greeting = func("My name is Kiran Krishnan")
    print(greeting)


greet(caps)
greet(small)


def create_adder(x):
    def adder(y):
        return x + y
    return adder


add_15 = create_adder(15)
print(add_15(10))


def hello_decorator(func):
    def inner1():
        print("Hello, this is before function execution")
        func()
        print("This is after function execution")
    return inner1


def function_to_be_used():
    print("This is inside the function !!")


function_to_be_used = hello_decorator(function_to_be_used)
function_to_be_used()
print("!!!!!!!!!!!!")


def hello_decorator(func):
    def inner1():
        print("Hello, this is before function execution")
        func()
        print("This is after function execution")
    return inner1


@hello_decorator
def function_to_be_used():
    print("This is inside the function !!")


function_to_be_used()


def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)


divide(2, 0)


def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@star
@percent
def printer(msg):
    print("hahahahhaha")
    print(msg)


printer("Hello")