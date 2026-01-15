from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Edge:

    pass
class petrinet_InputEdge(Edge):

    pass
class petrinet_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class petrinet_ReadEdge(Edge):

    pass
class petrinet_InhibitorEdge(Edge):

    pass
class petrinet_OutputEdge(Edge):

    pass
class NamedElement:

    pass
class petrinet_Place(NamedElement):

    def __init__(self, tokens: int, place: set["petrinet_Edge"] = None, petrinet_Place: "petrinet_PetriNet" = None, Place: "petrinet_Edge" = None):
        self.tokens = tokens
        self.place = place if place is not None else set()
        self.petrinet_Place = petrinet_Place
        self.Place = Place
        
    @property
    def tokens(self) -> int:
        return self.__tokens

    @tokens.setter
    def tokens(self, tokens: int):
        self.__tokens = tokens

    @property
    def Place(self):
        return self.__Place

    @Place.setter
    def Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__Place", None)
        self.__Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edges"):
                opp_val = getattr(old_value, "edges", None)
                if opp_val == self:
                    setattr(old_value, "edges", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edges"):
                opp_val = getattr(value, "edges", None)
                setattr(value, "edges", self)

    @property
    def place(self):
        return self.__place

    @place.setter
    def place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__place", None)
        self.__place = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Edge"):
                    opp_val = getattr(item, "Edge", None)
                    
                    if opp_val == self:
                        setattr(item, "Edge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Edge"):
                    opp_val = getattr(item, "Edge", None)
                    
                    setattr(item, "Edge", self)
                    

    @property
    def petrinet_Place(self):
        return self.__petrinet_Place

    @petrinet_Place.setter
    def petrinet_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__petrinet_Place", None)
        self.__petrinet_Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_PetriNet"):
                opp_val = getattr(old_value, "petrinet_PetriNet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_PetriNet"):
                opp_val = getattr(value, "petrinet_PetriNet", None)
                if opp_val is None:
                    setattr(value, "petrinet_PetriNet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class petrinet_PetriNet(NamedElement):

    pass
class petrinet_Edge(NamedElement):

    pass
class petrinet_Transition(NamedElement):

    pass