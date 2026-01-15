from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class PortB:

    pass
class typeB_PortB(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class typeB_OutPortB(PortB):

    pass
class typeB_InPortB(PortB):

    pass
class typeB_BlockB:

    pass