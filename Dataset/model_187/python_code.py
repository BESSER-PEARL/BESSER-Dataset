from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class PetriNet_NonReferencedClass:

    pass
class PetriNet_Arc:

    def __init__(self, weight: str):
        self.weight = weight
        
    @property
    def weight(self) -> str:
        return self.__weight

    @weight.setter
    def weight(self, weight: str):
        self.__weight = weight

class PetriNet:

    pass
class PlaceToTransArc:

    pass
class TransToPlaceArc:

    pass
class Arc:

    pass
class PetriNet_PlaceToTransArc(Arc):

    pass
class PetriNet_TransToPlaceArc(Arc):

    pass
class Transition:

    pass
class Place:

    pass
class Element:

    pass
class PetriNet_Place(Element):

    def __init__(self, name: str, 05: set["TransToPlaceArc"] = None, 08: set["PlaceToTransArc"] = None, 011: "PetriNet" = None):
        self.name = name
        self.05 = 05 if 05 is not None else set()
        self.08 = 08 if 08 is not None else set()
        self.011 = 011
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 08(self):
        return self.__08

    @08.setter
    def 08(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Place__08", None)
        self.__08 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#9"):
                    opp_val = getattr(item, "#9", None)
                    
                    if opp_val == self:
                        setattr(item, "#9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#9"):
                    opp_val = getattr(item, "#9", None)
                    
                    setattr(item, "#9", self)
                    

    @property
    def 011(self):
        return self.__011

    @011.setter
    def 011(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Place__011", None)
        self.__011 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#12"):
                opp_val = getattr(old_value, "#12", None)
                if opp_val == self:
                    setattr(old_value, "#12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#12"):
                opp_val = getattr(value, "#12", None)
                setattr(value, "#12", self)

    @property
    def 05(self):
        return self.__05

    @05.setter
    def 05(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Place__05", None)
        self.__05 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#6"):
                    opp_val = getattr(item, "#6", None)
                    
                    if opp_val == self:
                        setattr(item, "#6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#6"):
                    opp_val = getattr(item, "#6", None)
                    
                    setattr(item, "#6", self)
                    

class PetriNet_Transition(Element):

    pass
class PetriNet_PetriNet(Element):

    pass
class PetriNet_Element(ABC):

    pass