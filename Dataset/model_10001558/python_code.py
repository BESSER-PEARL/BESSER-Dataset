from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class C3:

    def __init__(self, K: int):
        self.K = K
        
        pass
    @property
    def K(self):
        return self.__K
    @K.setter
    def K(self, K: int):
        self.__K = K



class C2(ABC):

    pass


class C1(ABC):

    def __init__(self, b: str):
        self.b = b
        
        pass
    @property
    def b(self):
        return self.__b
    @b.setter
    def b(self, b: str):
        self.__b = b



class S(ABC):

    def __init__(self, v1: str):
        self.v1 = v1
        
        pass
    @property
    def v1(self):
        return self.__v1
    @v1.setter
    def v1(self, v1: str):
        self.__v1 = v1



class I_Interface:

    pass
