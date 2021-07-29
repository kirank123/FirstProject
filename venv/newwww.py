

class abc:
    def __init__(self, n):
        self.n = n
        print("base class")

    def __repr__(self):
        print("base class")

    def num(self, n):
        print("Class abc")
        self.n = n
        return n*n


class B(abc):
    def __init__(self, n):
        self.n = n
        super().__init__('B')

    def __repr__(self):
        print("Class B")


blc = B(5)
sqr = blc.num(5)
print(sqr)



