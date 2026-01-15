from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Persons:

    pass
class Persons_Female(Persons):

    pass
class Persons_Male(Persons):

    pass
class Persons_Persons(ABC):

    def __init__(self, fullName: str):
        self.fullName = fullName
        
    @property
    def fullName(self) -> str:
        return self.__fullName

    @fullName.setter
    def fullName(self, fullName: str):
        self.__fullName = fullName
