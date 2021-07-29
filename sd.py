
def decor_divide(fun):
    def inner(a, b):
        if b == 0:
            print("Division by zero is not possible")
            return
        return fun(a*a, b*b)
    return inner




@decor_divide
def divide(a, b):
    print(a/b)

divide(5, 2)

stri="welcome"
print(stri)
nn = [x for x in stri]
print(nn)