from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class test_N(ABC):

    def __init__(self, n: str):
        self.n = n
        
    @property
    def n(self) -> str:
        return self.__n

    @n.setter
    def n(self, n: str):
        self.__n = n

class B:

    pass
class N:

    pass
class test_test2_B(N):

    def __init__(self, nb: int, nb2: int):
        self.nb = nb
        self.nb2 = nb2
        
    @property
    def nb(self) -> int:
        return self.__nb

    @nb.setter
    def nb(self, nb: int):
        self.__nb = nb

    @property
    def nb2(self) -> int:
        return self.__nb2

    @nb2.setter
    def nb2(self, nb2: int):
        self.__nb2 = nb2

class test_A(N):

    pass