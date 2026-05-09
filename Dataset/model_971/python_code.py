from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class graph_Edge:

    pass
class graph_AbstractNamedObject(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class AbstractNamedObject:

    pass
class graph_Node(AbstractNamedObject):

    pass
class graph_Graph(AbstractNamedObject):

    pass