from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class PetriNet_Movement:

    pass
class Token:

    pass
class PetriNet_Marking:

    pass
class PetriNet_Token:

    pass
class Movement:

    pass
class Marking:

    pass
class PetriNet_Execution:

    pass
class Transition:

    pass
class Place:

    pass
class PetriNet:

    pass
class Execution:

    pass
class Arc:

    pass
class PetriNet_TransitionToPlace(Arc):

    pass
class PetriNet_PlaceToTransition(Arc):

    pass
class Element:

    pass
class PetriNet_Place(Element):

    pass
class PetriNet_Transition(Element):

    pass
class NamedElement:

    pass
class PetriNet_Element(NamedElement):

    pass
class PetriNet_Arc(NamedElement):

    def __init__(self, weight: str, arcs: "PetriNet" = None):
        self.weight = weight
        self.arcs = arcs
        
        pass
    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: str):
        self.__weight = weight


    @property
    def arcs(self):
        return self.__arcs

    @arcs.setter
    def arcs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Arc__arcs", None)
        self.__arcs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet15"):
                opp_val = getattr(old_value, "PetriNet15", None)
                if opp_val == self:
                    setattr(old_value, "PetriNet15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet15"):
                opp_val = getattr(value, "PetriNet15", None)
                setattr(value, "PetriNet15", self)

class PetriNet_PetriNet(NamedElement):

    pass
class LocatedElement:

    pass
class PetriNet_NamedElement(LocatedElement):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class PetriNet_LocatedElement(ABC):

    def __init__(self, location: str):
        self.location = location
        
        pass
    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


class PlaceToTransition:

    pass
class TransitionToPlace:

    pass