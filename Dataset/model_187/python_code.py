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
        
        pass
    @property
    def weight(self):
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
class Transition:

    pass
class Place:

    pass
class Element:

    pass
class PetriNet_Transition(Element):

    pass
class PetriNet_Place(Element):

    def __init__(self, name: str, target: set["TransToPlaceArc"] = None, source: set["PlaceToTransArc"] = None, places: "PetriNet" = None):
        self.name = name
        self.target = target if target is not None else set()
        self.source = source if source is not None else set()
        self.places = places
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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
    def places(self):
        return self.__places

    @places.setter
    def places(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Place__places", None)
        self.__places = value
        
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

    pass
class PetriNet_Element(ABC):

    pass
class PetriNet_TransToPlaceArc(Arc):

    pass