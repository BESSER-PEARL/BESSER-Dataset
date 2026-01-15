from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Named:

    pass
class relational_Schema(Named):

    pass
class relational_Type(Named):

    pass
class relational_Column(Named):

    pass
class relational_Table(Named):

    pass
class relational_Named(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
