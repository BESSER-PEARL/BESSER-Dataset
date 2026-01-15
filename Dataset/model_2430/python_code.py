from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class NamedElement:

    pass
class necsis14_databaseschema_Column(NamedElement):

    pass
class necsis14_databaseschema_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class necsis14_databaseschema_Table(NamedElement):

    pass
class necsis14_databaseschema_DatabaseSchema:

    pass