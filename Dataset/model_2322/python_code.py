from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Person:

    pass
class persons_Male(Person):

    pass
class persons_Person(ABC):

    def __init__(self, fullName: str):
        self.fullName = fullName
        
    @property
    def fullName(self) -> str:
        return self.__fullName

    @fullName.setter
    def fullName(self, fullName: str):
        self.__fullName = fullName

class persons_Female(Person):

    pass