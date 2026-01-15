from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class inherlink_T:

    pass
class inherlink_G:

    pass
class inherlink_P:

    pass
class R:

    pass
class inherlink_Y(R):

    pass
class L:

    pass
class inherlink_W(L):

    pass
class inherlink_A:

    pass
class inherlink_Named:

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
class inherlink_L(Named):

    pass
class inherlink_R(Named):

    pass
class inherlink_N(R):

    pass
class inherlink_X(L):

    pass
class inherlink_M(L):

    pass
class inherlink_K(R):

    pass
class inherlink_C:

    pass