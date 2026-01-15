from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Exp:

    pass
class exp_Add(Exp):

    pass
class exp_Lit(Exp):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class exp_Exp(ABC):

    pass