from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class relationaldatabase_RelationalDatabase:

    pass
class NamedElement:

    pass
class relationaldatabase_Table(NamedElement):

    pass
class relationaldatabase_Column(NamedElement):

    pass
class relationaldatabase_ForeignKey(NamedElement):

    pass
class relationaldatabase_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
