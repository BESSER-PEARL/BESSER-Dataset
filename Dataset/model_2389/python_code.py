from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class simpleRDBMS_RDBMSModel:

    pass
class NamedElement:

    pass
class simpleRDBMS_Column(NamedElement):

    pass
class simpleRDBMS_Table(NamedElement):

    pass
class simpleRDBMS_Schema(NamedElement):

    pass
class simpleRDBMS_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class simpleRDBMS_Key(NamedElement):

    pass
class simpleRDBMS_ForeignKey(NamedElement):

    pass