from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class sql_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class NamedElement:

    pass
class sql_Column(NamedElement):

    pass
class sql_Table(NamedElement):

    pass
class sql_SelectQuery:

    pass
class sql_Model:

    pass