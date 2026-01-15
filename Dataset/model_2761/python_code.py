from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class simpletest_X:

    pass
class N:

    pass
class simpletest_A(N):

    pass
class simpletest_N(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class simpletest_L(N):

    pass
class simpletest_B(N):

    pass