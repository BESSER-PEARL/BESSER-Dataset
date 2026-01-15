from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Arc:

    pass
class PetriNet_TransToPlaceArc(Arc):

    pass
class PetriNet_PlaceToTransArc(Arc):

    pass
class PetriNet_Transition:

    pass
class PetriNet_Place:

    def __init__(self, tokens: int, PetriNet_Place: "PetriNet_PetriNet" = None, PetriNet_Place6: "PetriNet_PlaceToTransArc" = None, PetriNet_Place14: "PetriNet_TransToPlaceArc" = None):
        self.tokens = tokens
        self.PetriNet_Place = PetriNet_Place
        self.PetriNet_Place6 = PetriNet_Place6
        self.PetriNet_Place14 = PetriNet_Place14
        
    @property
    def tokens(self) -> int:
        return self.__tokens

    @tokens.setter
    def tokens(self, tokens: int):
        self.__tokens = tokens

    @property
    def PetriNet_Place14(self):
        return self.__PetriNet_Place14

    @PetriNet_Place14.setter
    def PetriNet_Place14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Place__PetriNet_Place14", None)
        self.__PetriNet_Place14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet_TransToPlaceArc13"):
                opp_val = getattr(old_value, "PetriNet_TransToPlaceArc13", None)
                if opp_val == self:
                    setattr(old_value, "PetriNet_TransToPlaceArc13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet_TransToPlaceArc13"):
                opp_val = getattr(value, "PetriNet_TransToPlaceArc13", None)
                setattr(value, "PetriNet_TransToPlaceArc13", self)

    @property
    def PetriNet_Place(self):
        return self.__PetriNet_Place

    @PetriNet_Place.setter
    def PetriNet_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Place__PetriNet_Place", None)
        self.__PetriNet_Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet_PetriNet"):
                opp_val = getattr(old_value, "PetriNet_PetriNet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet_PetriNet"):
                opp_val = getattr(value, "PetriNet_PetriNet", None)
                if opp_val is None:
                    setattr(value, "PetriNet_PetriNet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PetriNet_Place6(self):
        return self.__PetriNet_Place6

    @PetriNet_Place6.setter
    def PetriNet_Place6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Place__PetriNet_Place6", None)
        self.__PetriNet_Place6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet_PlaceToTransArc"):
                opp_val = getattr(old_value, "PetriNet_PlaceToTransArc", None)
                if opp_val == self:
                    setattr(old_value, "PetriNet_PlaceToTransArc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet_PlaceToTransArc"):
                opp_val = getattr(value, "PetriNet_PlaceToTransArc", None)
                setattr(value, "PetriNet_PlaceToTransArc", self)

class PetriNet_PetriNet:

    pass
class PetriNet_Arc(ABC):

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
