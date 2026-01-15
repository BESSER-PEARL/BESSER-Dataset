from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class graph_Edge:

    pass
class graph_HasName(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class graph_Root:

    pass
class HasName:

    pass
class graph_SubNode(HasName):

    pass
class graph_Node(HasName):

    pass