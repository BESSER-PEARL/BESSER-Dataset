from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class TestA(Enum):
class TestB(Enum):


############################################
# Definition of Classes
############################################

class nonemf_A:

    pass
class nonemf_B:

    pass
class Serializable:

    pass
class nonemf_MySerializableClass(Serializable):

    def __init__(self, somethingInteresting: str):
        self.somethingInteresting = somethingInteresting
        
    @property
    def somethingInteresting(self) -> str:
        return self.__somethingInteresting

    @somethingInteresting.setter
    def somethingInteresting(self, somethingInteresting: str):
        self.__somethingInteresting = somethingInteresting

class nonemf_Serializable(ABC):

    pass