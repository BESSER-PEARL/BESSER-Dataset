from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class DatabaseElement:

    pass
class DB_Table(DatabaseElement):

    pass
class NamedElement:

    pass
class DB_Column(NamedElement):

    pass
class DB_DatabaseElement(NamedElement):

    pass
class DB_Database:

    pass
class DB_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class DB_ForeignKey(DatabaseElement):

    pass
class DB_Type(DatabaseElement):

    pass