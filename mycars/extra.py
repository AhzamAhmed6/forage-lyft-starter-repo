

from abc import ABC, abstractmethod
from lib2to3.pgen2 import driver
class A:
    def __init__(self, name):
        self.name=name
        self.age=12
        

class B(A):
    def __init__(self, name):
        super().__init__(name)

    def info(self):
        return self.name, self.age



print(B('ahzam').info())