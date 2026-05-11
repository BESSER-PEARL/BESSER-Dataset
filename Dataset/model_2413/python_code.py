from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Column:

    pass
class Schema:

    pass
class Table:

    pass
class Named:

    pass
class Relational_Table(Named):

    pass
class Relational_Column(Named):

    pass
class Relational_System(Named):

    pass
class Relational_Schema(Named):

    pass
class Relational_Named(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class Relational_Type(Named):

    pass
class Type:

    pass