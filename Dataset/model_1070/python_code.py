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
class PetriNet_Arc(NamedElement):

    def __init__(self, weight: str, Arc: "PetriNet_PetriNet" = None, arcs: "PetriNet_PetriNet" = None):
        self.weight = weight
        self.Arc = Arc
        self.arcs = arcs
        
    @property
    def weight(self) -> str:
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
            if hasattr(old_value, "PetriNet13"):
                opp_val = getattr(old_value, "PetriNet13", None)
                if opp_val == self:
                    setattr(old_value, "PetriNet13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet13"):
                opp_val = getattr(value, "PetriNet13", None)
                setattr(value, "PetriNet13", self)

    @property
    def Arc(self):
        return self.__Arc

    @Arc.setter
    def Arc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Arc__Arc", None)
        self.__Arc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "net2"):
                opp_val = getattr(old_value, "net2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "net2"):
                opp_val = getattr(value, "net2", None)
                if opp_val is None:
                    setattr(value, "net2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PetriNet_Element(NamedElement):

    pass