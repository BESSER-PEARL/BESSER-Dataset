from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class PortB:

    pass
class typeB_PortB(ABC):

    def __init__(self, id: int):
        self.id = id
        
    @property
    def id(self) -> int:
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