from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class exp_Exp(ABC):

    pass
class Exp:

    pass
class exp_Add(Exp):

    pass
class exp_Lit(Exp):

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

