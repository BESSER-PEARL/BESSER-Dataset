from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Element:

    pass
class PetriNet_Transition(Element):

    pass
class PetriNet_Place(Element):

    pass
class PetriNet_LocatedElement(ABC):

    def __init__(self, location: str):
        self.location = location
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

class NamedElement:

    pass
class PetriNet_Element(NamedElement):

    pass
class PetriNet_PetriNet(NamedElement):

    pass
class LocatedElement:

    pass
class PetriNet_NamedElement(LocatedElement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
