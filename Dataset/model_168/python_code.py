from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class PetriNet_Arc:

    def __init__(self, weight: str, name: str):
        self.weight = weight
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: str):
        self.__weight = weight


class PetriNet_NonReferencedClass:

    pass
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
class PetriNet_WeightedArc(Arc):

    pass
class Transition:

    pass
class Place:

    pass
class Element:

    pass
class PetriNet_Transition(Element):

    def __init__(self, name: str, target9: set["PlaceToTransArc"] = None, source12: set["TransToPlaceArc"] = None):
        self.name = name
        self.target9 = target9 if target9 is not None else set()
        self.source12 = source12 if source12 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def source12(self):
        return self.__source12

    @source12.setter
    def source12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Transition__source12", None)
        self.__source12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TransToPlaceArc13"):
                    opp_val = getattr(item, "TransToPlaceArc13", None)
                    
                    if opp_val == self:
                        setattr(item, "TransToPlaceArc13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TransToPlaceArc13"):
                    opp_val = getattr(item, "TransToPlaceArc13", None)
                    
                    setattr(item, "TransToPlaceArc13", self)
                    

    @property
    def target9(self):
        return self.__target9

    @target9.setter
    def target9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Transition__target9", None)
        self.__target9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PlaceToTransArc10"):
                    opp_val = getattr(item, "PlaceToTransArc10", None)
                    
                    if opp_val == self:
                        setattr(item, "PlaceToTransArc10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PlaceToTransArc10"):
                    opp_val = getattr(item, "PlaceToTransArc10", None)
                    
                    setattr(item, "PlaceToTransArc10", self)
                    

class PetriNet_Place(Element):

    def __init__(self, name: str, target: set["TransToPlaceArc"] = None, source: set["PlaceToTransArc"] = None, PetriNet_Place: "PetriNet" = None):
        self.name = name
        self.target = target if target is not None else set()
        self.source = source if source is not None else set()
        self.PetriNet_Place = PetriNet_Place
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Place__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PlaceToTransArc"):
                    opp_val = getattr(item, "PlaceToTransArc", None)
                    
                    if opp_val == self:
                        setattr(item, "PlaceToTransArc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PlaceToTransArc"):
                    opp_val = getattr(item, "PlaceToTransArc", None)
                    
                    setattr(item, "PlaceToTransArc", self)
                    

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Place__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TransToPlaceArc"):
                    opp_val = getattr(item, "TransToPlaceArc", None)
                    
                    if opp_val == self:
                        setattr(item, "TransToPlaceArc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TransToPlaceArc"):
                    opp_val = getattr(item, "TransToPlaceArc", None)
                    
                    setattr(item, "TransToPlaceArc", self)
                    

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
        
        pass
    @property
    def name(self):
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