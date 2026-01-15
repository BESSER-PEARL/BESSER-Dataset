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
class PlaceToTransition:

    pass
class TransitionToPlace:

    pass
class PetriNet:

    pass
class Execution:

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
class NamedElement:

    pass
class PetriNet_Element(NamedElement):

    pass
class PetriNet_Arc(NamedElement):

    def __init__(self, weight: str, 023: "PetriNet" = None):
        self.weight = weight
        self.023 = 023
        
    @property
    def weight(self) -> str:
        return self.__weight

    @weight.setter
    def weight(self, weight: str):
        self.__weight = weight

    @property
    def 023(self):
        return self.__023

    @023.setter
    def 023(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Arc__023", None)
        self.__023 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#24"):
                opp_val = getattr(old_value, "#24", None)
                if opp_val == self:
                    setattr(old_value, "#24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#24"):
                opp_val = getattr(value, "#24", None)
                setattr(value, "#24", self)

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
