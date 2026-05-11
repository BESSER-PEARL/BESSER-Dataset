from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Person:

    pass
class persons_Female(Person):

    pass
class persons_Male(Person):

    pass
class persons_Person(ABC):

    def __init__(self, fullName: str):
        self.fullName = fullName
        
        pass
    @property
    def fullName(self):
        return self.__fullName

    @fullName.setter
    def fullName(self, fullName: str):
        self.__fullName = fullName

