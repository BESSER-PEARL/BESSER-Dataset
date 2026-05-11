from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class OutPortB:

    pass
class typeB_OutType1(OutPortB):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class PortB:

    pass
class typeB_PortB(ABC):

    def __init__(self, id: int):
        self.id = id
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id


class typeB_OutPortB(PortB):

    pass
class typeB_InPortB(PortB):

    pass
class typeB_BlockB:

    pass