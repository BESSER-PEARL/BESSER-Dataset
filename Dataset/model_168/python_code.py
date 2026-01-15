from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class PetriNet_NonReferencedClass:

    pass
class PetriNet_Arc:

    def __init__(self, weight: str, name: str):
        self.weight = weight
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def weight(self) -> str:
        return self.__weight

    @weight.setter
    def weight(self, weight: str):
        self.__weight = weight

class Arc:

    pass
class PetriNet_TransToPlaceArc(Arc):

    pass
class PetriNet_WeightedArc(Arc):

    pass
class PetriNet_PlaceToTransArc(Arc):

    pass
class Transition:

    pass
class PetriNet:

    pass
class PlaceToTransArc:

    pass
class TransToPlaceArc:

    pass
class Place:

    pass
class Element:

    pass
class PetriNet_Transition(Element):

    def __init__(self, name: str, 011: set["PlaceToTransArc"] = None, 014: set["TransToPlaceArc"] = None):
        self.name = name
        self.011 = 011 if 011 is not None else set()
        self.014 = 014 if 014 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 011(self):
        return self.__011

    @011.setter
    def 011(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Transition__011", None)
        self.__011 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#12"):
                    opp_val = getattr(item, "#12", None)
                    
                    if opp_val == self:
                        setattr(item, "#12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#12"):
                    opp_val = getattr(item, "#12", None)
                    
                    setattr(item, "#12", self)
                    

    @property
    def 014(self):
        return self.__014

    @014.setter
    def 014(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Transition__014", None)
        self.__014 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#15"):
                    opp_val = getattr(item, "#15", None)
                    
                    if opp_val == self:
                        setattr(item, "#15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#15"):
                    opp_val = getattr(item, "#15", None)
                    
                    setattr(item, "#15", self)
                    

class PetriNet_Place(Element):

    def __init__(self, name: str, 0: set["TransToPlaceArc"] = None, 07: set["PlaceToTransArc"] = None, PetriNet_Place: "PetriNet" = None):
        self.name = name
        self.0 = 0 if 0 is not None else set()
        self.07 = 07 if 07 is not None else set()
        self.PetriNet_Place = PetriNet_Place
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 07(self):
        return self.__07

    @07.setter
    def 07(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Place__07", None)
        self.__07 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#8"):
                    opp_val = getattr(item, "#8", None)
                    
                    if opp_val == self:
                        setattr(item, "#8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#8"):
                    opp_val = getattr(item, "#8", None)
                    
                    setattr(item, "#8", self)
                    

    @property
    def 0(self):
        return self.__0

    @0.setter
    def 0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Place__0", None)
        self.__0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#"):
                    opp_val = getattr(item, "#", None)
                    
                    if opp_val == self:
                        setattr(item, "#", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#"):
                    opp_val = getattr(item, "#", None)
                    
                    setattr(item, "#", self)
                    

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
            if hasattr(old_value, "PetriNet"):
                opp_val = getattr(old_value, "PetriNet", None)
                if opp_val == self:
                    setattr(old_value, "PetriNet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet"):
                opp_val = getattr(value, "PetriNet", None)
                setattr(value, "PetriNet", self)

class PetriNet_PetriNet(Element):

    def __init__(self, name: str, PetriNet_PetriNet: set["Place"] = None, PetriNet_PetriNet2: set["Transition"] = None, PetriNet_PetriNet4: set["Arc"] = None):
        self.name = name
        self.PetriNet_PetriNet = PetriNet_PetriNet if PetriNet_PetriNet is not None else set()
        self.PetriNet_PetriNet2 = PetriNet_PetriNet2 if PetriNet_PetriNet2 is not None else set()
        self.PetriNet_PetriNet4 = PetriNet_PetriNet4 if PetriNet_PetriNet4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PetriNet_PetriNet4(self):
        return self.__PetriNet_PetriNet4

    @PetriNet_PetriNet4.setter
    def PetriNet_PetriNet4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_PetriNet__PetriNet_PetriNet4", None)
        self.__PetriNet_PetriNet4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arc"):
                    opp_val = getattr(item, "Arc", None)
                    
                    if opp_val == self:
                        setattr(item, "Arc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arc"):
                    opp_val = getattr(item, "Arc", None)
                    
                    setattr(item, "Arc", self)
                    

    @property
    def PetriNet_PetriNet2(self):
        return self.__PetriNet_PetriNet2

    @PetriNet_PetriNet2.setter
    def PetriNet_PetriNet2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_PetriNet__PetriNet_PetriNet2", None)
        self.__PetriNet_PetriNet2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    setattr(item, "Transition", self)
                    

    @property
    def PetriNet_PetriNet(self):
        return self.__PetriNet_PetriNet

    @PetriNet_PetriNet.setter
    def PetriNet_PetriNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_PetriNet__PetriNet_PetriNet", None)
        self.__PetriNet_PetriNet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Place"):
                    opp_val = getattr(item, "Place", None)
                    
                    if opp_val == self:
                        setattr(item, "Place", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Place"):
                    opp_val = getattr(item, "Place", None)
                    
                    setattr(item, "Place", self)
                    

class PetriNet_Element(ABC):

    pass