from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Arc:

    pass
class evoPetrinet_TransitionToPlace(Arc):

    pass
class evoPetrinet_PlaceToTransition(Arc):

    pass
class PlaceToTransition:

    pass
class TransitionToPlace:

    pass
class Element:

    pass
class evoPetrinet_Arc(Element):

    def __init__(self, weight: str, Element: "evoPetrinet_PetriNet" = None):
        self.weight = weight
        
        pass
    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: str):
        self.__weight = weight


class evoPetrinet_Transition(Element):

    pass
class evoPetrinet_Place(Element):

    pass
class Transition:

    pass
class Place:

    pass
class LocatedElement:

    pass
class evoPetrinet_NamedElement(LocatedElement):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class evoPetrinet_LocatedElement(ABC):

    def __init__(self, location: str):
        self.location = location
        
        pass
    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


class PetriNet:

    pass
class evoPetrinet_PetriNetModel:

    pass
class NamedElement:

    pass
class evoPetrinet_Element(NamedElement):

    pass
class evoPetrinet_PetriNet(NamedElement):

    pass