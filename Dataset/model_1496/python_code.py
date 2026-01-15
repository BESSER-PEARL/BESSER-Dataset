from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Element:

    pass
class PetriNet_Place(Element):

    def __init__(self, Tokens: int):
        self.Tokens = Tokens
        
    @property
    def Tokens(self) -> int:
        return self.__Tokens

    @Tokens.setter
    def Tokens(self, Tokens: int):
        self.__Tokens = Tokens

class PetriNet_Arc:

    pass
class PetriNet_Transition(Element):

    def __init__(self, minTime: int, maxTime: int):
        self.minTime = minTime
        self.maxTime = maxTime
        
    @property
    def minTime(self) -> int:
        return self.__minTime

    @minTime.setter
    def minTime(self, minTime: int):
        self.__minTime = minTime

    @property
    def maxTime(self) -> int:
        return self.__maxTime

    @maxTime.setter
    def maxTime(self, maxTime: int):
        self.__maxTime = maxTime

class PetriNet_Element(ABC):

    def __init__(self, name: str, PetriNet_Element5: "PetriNet_Arc" = None, PetriNet_Element8: "PetriNet_Arc" = None, PetriNet_Element: "PetriNet_PetriNetRoot" = None):
        self.name = name
        self.PetriNet_Element5 = PetriNet_Element5
        self.PetriNet_Element8 = PetriNet_Element8
        self.PetriNet_Element = PetriNet_Element
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PetriNet_Element8(self):
        return self.__PetriNet_Element8

    @PetriNet_Element8.setter
    def PetriNet_Element8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Element__PetriNet_Element8", None)
        self.__PetriNet_Element8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet_Arc7"):
                opp_val = getattr(old_value, "PetriNet_Arc7", None)
                if opp_val == self:
                    setattr(old_value, "PetriNet_Arc7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet_Arc7"):
                opp_val = getattr(value, "PetriNet_Arc7", None)
                setattr(value, "PetriNet_Arc7", self)

    @property
    def PetriNet_Element(self):
        return self.__PetriNet_Element

    @PetriNet_Element.setter
    def PetriNet_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Element__PetriNet_Element", None)
        self.__PetriNet_Element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet_PetriNetRoot"):
                opp_val = getattr(old_value, "PetriNet_PetriNetRoot", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet_PetriNetRoot"):
                opp_val = getattr(value, "PetriNet_PetriNetRoot", None)
                if opp_val is None:
                    setattr(value, "PetriNet_PetriNetRoot", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PetriNet_Element5(self):
        return self.__PetriNet_Element5

    @PetriNet_Element5.setter
    def PetriNet_Element5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Element__PetriNet_Element5", None)
        self.__PetriNet_Element5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet_Arc4"):
                opp_val = getattr(old_value, "PetriNet_Arc4", None)
                if opp_val == self:
                    setattr(old_value, "PetriNet_Arc4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet_Arc4"):
                opp_val = getattr(value, "PetriNet_Arc4", None)
                setattr(value, "PetriNet_Arc4", self)

class PetriNet_PetriNetRoot:

    pass