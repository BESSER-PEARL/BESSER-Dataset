from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class petrinet_PetriNet:

    pass
class petrinet_Identifyable(ABC):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class Node:

    pass
class petrinet_Place(Node):

    pass
class petrinet_Transition(Node):

    pass
class Identifyable:

    pass
class petrinet_Arc(Identifyable):

    pass
class petrinet_Node(Identifyable):

    pass