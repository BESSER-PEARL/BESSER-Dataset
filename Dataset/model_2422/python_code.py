from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Relational_ERModel:

    pass
class Relational_FKey:

    pass
class Named:

    pass
class Relational_Type(Named):

    pass
class Relational_Column(Named):

    pass
class Relational_Table(Named):

    pass
class Relational_Named(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
