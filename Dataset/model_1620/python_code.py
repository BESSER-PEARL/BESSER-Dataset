from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Edge:

    pass
class pnw_PTEdge(Edge):

    pass
class pnw_TPEdge(Edge):

    pass
class NetElement:

    pass
class pnw_Edge(NetElement):

    def __init__(self, weight: int):
        self.weight = weight
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

class NamedElement:

    pass
class pnw_Transition(NetElement, NamedElement):

    pass
class pnw_Place(NetElement, NamedElement):

    def __init__(self, noOfTokens: int, fromPlace: set["pnw_PTEdge"] = None, toPlace: set["pnw_TPEdge"] = None, Place: "pnw_TPEdge" = None, Place11: "pnw_PTEdge" = None):
        self.noOfTokens = noOfTokens
        self.fromPlace = fromPlace if fromPlace is not None else set()
        self.toPlace = toPlace if toPlace is not None else set()
        self.Place = Place
        self.Place11 = Place11
        
    @property
    def noOfTokens(self) -> int:
        return self.__noOfTokens

    @noOfTokens.setter
    def noOfTokens(self, noOfTokens: int):
        self.__noOfTokens = noOfTokens

    @property
    def Place(self):
        return self.__Place

    @Place.setter
    def Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnw_Place__Place", None)
        self.__Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inTPEdges"):
                opp_val = getattr(old_value, "inTPEdges", None)
                if opp_val == self:
                    setattr(old_value, "inTPEdges", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inTPEdges"):
                opp_val = getattr(value, "inTPEdges", None)
                setattr(value, "inTPEdges", self)

    @property
    def Place11(self):
        return self.__Place11

    @Place11.setter
    def Place11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnw_Place__Place11", None)
        self.__Place11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outPTEdges"):
                opp_val = getattr(old_value, "outPTEdges", None)
                if opp_val == self:
                    setattr(old_value, "outPTEdges", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outPTEdges"):
                opp_val = getattr(value, "outPTEdges", None)
                setattr(value, "outPTEdges", self)

    @property
    def toPlace(self):
        return self.__toPlace

    @toPlace.setter
    def toPlace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnw_Place__toPlace", None)
        self.__toPlace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TPEdge7"):
                    opp_val = getattr(item, "TPEdge7", None)
                    
                    if opp_val == self:
                        setattr(item, "TPEdge7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TPEdge7"):
                    opp_val = getattr(item, "TPEdge7", None)
                    
                    setattr(item, "TPEdge7", self)
                    

    @property
    def fromPlace(self):
        return self.__fromPlace

    @fromPlace.setter
    def fromPlace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnw_Place__fromPlace", None)
        self.__fromPlace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PTEdge5"):
                    opp_val = getattr(item, "PTEdge5", None)
                    
                    if opp_val == self:
                        setattr(item, "PTEdge5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PTEdge5"):
                    opp_val = getattr(item, "PTEdge5", None)
                    
                    setattr(item, "PTEdge5", self)
                    

class pnw_Net(NamedElement):

    def __init__(self, incrementalID: str, net: set["pnw_NetElement"] = None, Net: "pnw_NetElement" = None):
        self.incrementalID = incrementalID
        self.net = net if net is not None else set()
        self.Net = Net
        
    @property
    def incrementalID(self) -> str:
        return self.__incrementalID

    @incrementalID.setter
    def incrementalID(self, incrementalID: str):
        self.__incrementalID = incrementalID

    @property
    def net(self):
        return self.__net

    @net.setter
    def net(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnw_Net__net", None)
        self.__net = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NetElement"):
                    opp_val = getattr(item, "NetElement", None)
                    
                    if opp_val == self:
                        setattr(item, "NetElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NetElement"):
                    opp_val = getattr(item, "NetElement", None)
                    
                    setattr(item, "NetElement", self)
                    

    @property
    def Net(self):
        return self.__Net

    @Net.setter
    def Net(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnw_Net__Net", None)
        self.__Net = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elements"):
                opp_val = getattr(old_value, "elements", None)
                if opp_val == self:
                    setattr(old_value, "elements", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elements"):
                opp_val = getattr(value, "elements", None)
                setattr(value, "elements", self)

class pnw_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class pnw_NetElement(ABC):

    pass