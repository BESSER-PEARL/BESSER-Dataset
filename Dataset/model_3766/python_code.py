from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class C(Enum):
    X = "X"
    Y = "Y"
    Z = "Z"


############################################
# Definition of Classes
############################################

class fsm_Transition:

    def __init__(self, a: str, b: str, c: str):
        self.a = a
        self.b = b
        self.c = c
        
    @property
    def c(self) -> str:
        return self.__c

    @c.setter
    def c(self, c: str):
        self.__c = c

    @property
    def a(self) -> str:
        return self.__a

    @a.setter
    def a(self, a: str):
        self.__a = a

    @property
    def b(self) -> str:
        return self.__b

    @b.setter
    def b(self, b: str):
        self.__b = b

    def foo(self, arg1: str, arg2: str) -> str:
        # TODO: Implement foo method
        pass
