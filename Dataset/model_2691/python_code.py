from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class link_Named(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Named:

    pass
class link_M(Named):

    pass
class link_D(Named):

    pass
class link_K(Named):

    pass
class link_N99(Named):

    pass
class link_X(Named):

    pass
class link_W(Named):

    pass
class link_C(Named):

    pass
class link_B(Named):

    pass
class link_A(Named):

    pass