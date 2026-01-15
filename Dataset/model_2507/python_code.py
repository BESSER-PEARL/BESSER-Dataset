from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class visualinher_N(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class N:

    pass
class visualinher_C:

    pass
class A:

    pass
class visualinher_E(A):

    pass
class visualinher_D(A):

    pass
class visualinher_I(A):

    pass
class I:

    pass
class visualinher_B(I):

    pass
class visualinher_R(N):

    pass
class visualinher_A(N):

    pass
class visualinher_S:

    pass