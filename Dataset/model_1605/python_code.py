from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class NetElement:

    pass
class pn_Transition(NetElement):

    pass
class NamedElement:

    pass
class pn_Place(NamedElement, NetElement):

    def __init__(self, noOfTokens: int, Place: "pn_Transition" = None, Place4: "pn_Transition" = None, srcP2T: set["pn_Transition"] = None, trgT2P: set["pn_Transition"] = None):
        self.noOfTokens = noOfTokens
        self.Place = Place
        self.Place4 = Place4
        self.srcP2T = srcP2T if srcP2T is not None else set()
        self.trgT2P = trgT2P if trgT2P is not None else set()
        
    @property
    def noOfTokens(self) -> int:
        return self.__noOfTokens

    @noOfTokens.setter
    def noOfTokens(self, noOfTokens: int):
        self.__noOfTokens = noOfTokens

    @property
    def Place4(self):
        return self.__Place4

    @Place4.setter
    def Place4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pn_Place__Place4", None)
        self.__Place4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trgP2T"):
                opp_val = getattr(old_value, "trgP2T", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trgP2T"):
                opp_val = getattr(value, "trgP2T", None)
                if opp_val is None:
                    setattr(value, "trgP2T", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def trgT2P(self):
        return self.__trgT2P

    @trgT2P.setter
    def trgT2P(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pn_Place__trgT2P", None)
        self.__trgT2P = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition7"):
                    opp_val = getattr(item, "Transition7", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition7"):
                    opp_val = getattr(item, "Transition7", None)
                    
                    setattr(item, "Transition7", self)
                    

    @property
    def srcP2T(self):
        return self.__srcP2T

    @srcP2T.setter
    def srcP2T(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pn_Place__srcP2T", None)
        self.__srcP2T = value if value is not None else set()
        
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
    def Place(self):
        return self.__Place

    @Place.setter
    def Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pn_Place__Place", None)
        self.__Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "srcT2P"):
                opp_val = getattr(old_value, "srcT2P", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "srcT2P"):
                opp_val = getattr(value, "srcT2P", None)
                if opp_val is None:
                    setattr(value, "srcT2P", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pn_NetElement(NamedElement):

    pass
class pn_Net(NamedElement):

    def __init__(self, incrementalID: str, net: set["pn_NetElement"] = None, Net: "pn_NetElement" = None):
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
    def Net(self):
        return self.__Net

    @Net.setter
    def Net(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pn_Net__Net", None)
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

    @property
    def net(self):
        return self.__net

    @net.setter
    def net(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pn_Net__net", None)
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
                    

class pn_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
