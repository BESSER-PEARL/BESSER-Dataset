from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class PetriNet:

    pass
class PlaceToTransArc:

    pass
class TransToPlaceArc:

    pass
class Arc:

    pass
class Transition:

    pass
class Place:

    pass
class Element:

    pass
class PetriNet_Transition(Element):

    def __init__(self, name: str, target8: set["PlaceToTransArc"] = None, source11: set["TransToPlaceArc"] = None):
        self.name = name
        self.target8 = target8 if target8 is not None else set()
        self.source11 = source11 if source11 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def source11(self):
        return self.__source11

    @source11.setter
    def source11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Transition__source11", None)
        self.__source11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TransToPlaceArc12"):
                    opp_val = getattr(item, "TransToPlaceArc12", None)
                    
                    if opp_val == self:
                        setattr(item, "TransToPlaceArc12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TransToPlaceArc12"):
                    opp_val = getattr(item, "TransToPlaceArc12", None)
                    
                    setattr(item, "TransToPlaceArc12", self)
                    

    @property
    def target8(self):
        return self.__target8

    @target8.setter
    def target8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Transition__target8", None)
        self.__target8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PlaceToTransArc9"):
                    opp_val = getattr(item, "PlaceToTransArc9", None)
                    
                    if opp_val == self:
                        setattr(item, "PlaceToTransArc9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PlaceToTransArc9"):
                    opp_val = getattr(item, "PlaceToTransArc9", None)
                    
                    setattr(item, "PlaceToTransArc9", self)
                    

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
                    

class PetriNet_PetriNet(Element):

    def __init__(self, name: str, net: set["Place"] = None, PetriNet_PetriNet: set["Transition"] = None, PetriNet_PetriNet3: set["Arc"] = None):
        self.name = name
        self.net = net if net is not None else set()
        self.PetriNet_PetriNet = PetriNet_PetriNet if PetriNet_PetriNet is not None else set()
        self.PetriNet_PetriNet3 = PetriNet_PetriNet3 if PetriNet_PetriNet3 is not None else set()
        
        pass
    @property
    def name(self):
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
    def net(self):
        return self.__net

    @net.setter
    def net(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_PetriNet__net", None)
        self.__net = value if value is not None else set()
        
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
class PetriNet_TransToPlaceArc(Arc):

    pass
class PetriNet_PlaceToTransArc(Arc):

    pass
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

