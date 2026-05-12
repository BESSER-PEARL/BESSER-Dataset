from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class CardValue(Enum):
    pass

############################################
# Definition of Classes
############################################










class Card:

    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: int):
        self.__value = value

