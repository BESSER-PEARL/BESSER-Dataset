from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Arc:

    pass
class petrinet_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class petrinet_Arc(ABC):

    def __init__(self, weight: int):
        self.weight = weight
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

class petrinet_Token:

    pass
class petrinet_TPArc(Arc):

    pass
class petrinet_PTArc(Arc):

    pass
class petrinet_PetriNet:

    pass
class NamedElement:

    pass
class petrinet_Transition(NamedElement):

    pass
class petrinet_Place(NamedElement):

    pass