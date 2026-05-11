from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class PortB:

    pass
class TypeB_PortB(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class TypeB_OutPortB(PortB):

    pass
class TypeB_InPortB(PortB):

    pass
class TypeB_BlockB:

    pass