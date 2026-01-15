from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class NodeCS:

    pass
class kiamacs_PlusCS(NodeCS):

    pass
class kiamacs_NumCS(NodeCS):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class kiamacs_TopCS:

    pass
class kiamacs_NodeCS(ABC):

    pass