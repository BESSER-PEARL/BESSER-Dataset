from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class PetriNet:

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

class Transition:

    pass
class Place:

    pass
class Element:

    pass
class PetriNet_Transition(Element):

    def __init__(self, name: str, 014: set["PlaceToTransArc"] = None, 017: set["TransToPlaceArc"] = None):
        self.name = name
        self.014 = 014 if 014 is not None else set()
        self.017 = 017 if 017 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
                    

    @property
    def 017(self):
        return self.__017

    @017.setter
    def 017(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Transition__017", None)
        self.__017 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#18"):
                    opp_val = getattr(item, "#18", None)
                    
                    if opp_val == self:
                        setattr(item, "#18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#18"):
                    opp_val = getattr(item, "#18", None)
                    
                    setattr(item, "#18", self)
                    

class PlaceToTransArc:

    pass
class TransToPlaceArc:

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

class Arc:

    pass
class PetriNet_TransToPlaceArc(Arc):

    pass
class PetriNet_PlaceToTransArc(Arc):

    pass
class PetriNet_PetriNet(Element):

    def __init__(self, name: str, PetriNet_PetriNet: set["Transition"] = None, PetriNet_PetriNet3: set["Arc"] = None, 0: set["Place"] = None):
        self.name = name
        self.PetriNet_PetriNet = PetriNet_PetriNet if PetriNet_PetriNet is not None else set()
        self.PetriNet_PetriNet3 = PetriNet_PetriNet3 if PetriNet_PetriNet3 is not None else set()
        self.0 = 0 if 0 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PetriNet_PetriNet3(self):
        return self.__PetriNet_PetriNet3

    @PetriNet_PetriNet3.setter
    def PetriNet_PetriNet3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_PetriNet__PetriNet_PetriNet3", None)
        self.__PetriNet_PetriNet3 = value if value is not None else set()
        
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
    def 0(self):
        return self.__0

    @0.setter
    def 0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_PetriNet__0", None)
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
                    

class PetriNet_Element(ABC):

    pass