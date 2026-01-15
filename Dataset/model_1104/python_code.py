from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Transition:

    pass
class PlaceToTransition:

    pass
class TransitionToPlace:

    pass
class Place:

    pass
class Arc:

    pass
class evoPetrinet_TransitionToPlace(Arc):

    pass
class evoPetrinet_PlaceToTransition(Arc):

    pass
class evoPetrinet_PetriNetModel:

    pass
class Element:

    pass
class evoPetrinet_Place(Element):

    pass
class evoPetrinet_Arc(Element):

    def __init__(self, weight: str, #: "evoPetrinet_PetriNet"):
        self.weight = weight
        
    @property
    def weight(self) -> str:
        return self.__weight

    @weight.setter
    def weight(self, weight: str):
        self.__weight = weight

class evoPetrinet_Transition(Element):

    pass
class NamedElement:

    pass
class evoPetrinet_Element(NamedElement):

    pass
class evoPetrinet_PetriNet(NamedElement):

    pass
class LocatedElement:

    pass
class evoPetrinet_NamedElement(LocatedElement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class evoPetrinet_LocatedElement(ABC):

    def __init__(self, location: str):
        self.location = location
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

class PetriNet:

    pass