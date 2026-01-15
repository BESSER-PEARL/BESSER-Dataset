from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class NamedElement:

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

class PetriNet_LocatedElement(ABC):

    def __init__(self, location: str):
        self.location = location
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

class Transition:

    pass
class Place:

    pass
class PetriNet_Arc(NamedElement):

    def __init__(self, weight: int, 020: "PetriNet" = None):
        self.weight = weight
        self.020 = 020
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def 020(self):
        return self.__020

    @020.setter
    def 020(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Arc__020", None)
        self.__020 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "21"):
                opp_val = getattr(old_value, "21", None)
                if opp_val == self:
                    setattr(old_value, "21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "21"):
                opp_val = getattr(value, "21", None)
                setattr(value, "21", self)

class PlaceToTransition:

    pass
class TransitionToPlace:

    pass
class PetriNet:

    pass
class PetriNet_Element(NamedElement):

    pass
class Arc:

    pass
class PetriNet_PlaceToTransition(Arc):

    pass
class PetriNet_TransitionToPlace(Arc):

    pass
class Element:

    pass
class PetriNet_Transition(Element):

    pass
class PetriNet_Place(Element):

    pass