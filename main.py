# python modules
import os

class A:
    def __init__(self):
        print("This is A")

class B(A):
    def __init__(self):
        super().__init__()
        print("this is from B")

class C(A):
    def __init__(self):
        super().__init__()
        print("This is from c")

class B1(B):
    def __init__(self):
        super().__init__()
        print("i am from B1")

class B2(B):
    def __init__(self):
        super().__init__()
        print("i am from B2")

class C1(C):
    def __init__(self):
        super().__init__()
        print("i am from C1")

class C2(C):
    def __init__(self):
        super().__init__()
        print("i am from C2")


class D(B1, B2):
    def __init__(self):
        super().__init__()
        print("class D")

class E(C1, C2):
    def __init__(self):
        super().__init__()
        print("class E")

class F(E, D):
    def __init__(self):
        super().__init__()
        print("Hey i am the last one")


person = F()
print(person)
print(F.__mro__)


