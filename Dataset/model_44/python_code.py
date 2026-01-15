from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Arc:

    pass
class PetriNet_PlaceToTransArc(Arc):

    pass
class PetriNet_TransToPlaceArc(Arc):

    pass
class PetriNet_Element(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class PetriNet_Arc:

    def __init__(self, weight: int, PetriNet_Arc: "PetriNet_PetriNet" = None):
        self.weight = weight
        self.PetriNet_Arc = PetriNet_Arc
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def PetriNet_Arc(self):
        return self.__PetriNet_Arc

    @PetriNet_Arc.setter
    def PetriNet_Arc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Arc__PetriNet_Arc", None)
        self.__PetriNet_Arc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet_PetriNet4"):
                opp_val = getattr(old_value, "PetriNet_PetriNet4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet_PetriNet4"):
                opp_val = getattr(value, "PetriNet_PetriNet4", None)
                if opp_val is None:
                    setattr(value, "PetriNet_PetriNet4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Element:

    pass
class PetriNet_Place(Element):

    pass
class PetriNet_Transition(Element):

    pass
class PetriNet_PetriNet(Element):

    pass