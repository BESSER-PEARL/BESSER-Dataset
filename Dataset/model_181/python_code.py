from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Arc:

    pass
class lit_petriNets_PTArc(Arc):

    pass
class lit_petriNets_TPArc(Arc):

    pass
class lit_petriNets_Arc(ABC):

    pass
class lit_petriNets_Transition:

    def __init__(self, name: str, transitions: "lit_petriNets_Net" = None, Transition: "lit_petriNets_Net" = None, Transition24: "lit_petriNets_TPArc" = None, dst10: set["lit_petriNets_PTArc"] = None, src13: set["lit_petriNets_TPArc"] = None, Transition21: "lit_petriNets_PTArc" = None):
        self.name = name
        self.transitions = transitions
        self.Transition = Transition
        self.Transition24 = Transition24
        self.dst10 = dst10 if dst10 is not None else set()
        self.src13 = src13 if src13 is not None else set()
        self.Transition21 = Transition21
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def transitions(self):
        return self.__transitions

    @transitions.setter
    def transitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lit_petriNets_Transition__transitions", None)
        self.__transitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Net8"):
                opp_val = getattr(old_value, "Net8", None)
                if opp_val == self:
                    setattr(old_value, "Net8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Net8"):
                opp_val = getattr(value, "Net8", None)
                setattr(value, "Net8", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lit_petriNets_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "net2"):
                opp_val = getattr(old_value, "net2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "net2"):
                opp_val = getattr(value, "net2", None)
                if opp_val is None:
                    setattr(value, "net2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition21(self):
        return self.__Transition21

    @Transition21.setter
    def Transition21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lit_petriNets_Transition__Transition21", None)
        self.__Transition21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "in"):
                opp_val = getattr(old_value, "in", None)
                if opp_val == self:
                    setattr(old_value, "in", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "in"):
                opp_val = getattr(value, "in", None)
                setattr(value, "in", self)

    @property
    def Transition24(self):
        return self.__Transition24

    @Transition24.setter
    def Transition24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lit_petriNets_Transition__Transition24", None)
        self.__Transition24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "out23"):
                opp_val = getattr(old_value, "out23", None)
                if opp_val == self:
                    setattr(old_value, "out23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "out23"):
                opp_val = getattr(value, "out23", None)
                setattr(value, "out23", self)

    @property
    def dst10(self):
        return self.__dst10

    @dst10.setter
    def dst10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lit_petriNets_Transition__dst10", None)
        self.__dst10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PTArc11"):
                    opp_val = getattr(item, "PTArc11", None)
                    
                    if opp_val == self:
                        setattr(item, "PTArc11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PTArc11"):
                    opp_val = getattr(item, "PTArc11", None)
                    
                    setattr(item, "PTArc11", self)
                    

    @property
    def src13(self):
        return self.__src13

    @src13.setter
    def src13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lit_petriNets_Transition__src13", None)
        self.__src13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TPArc14"):
                    opp_val = getattr(item, "TPArc14", None)
                    
                    if opp_val == self:
                        setattr(item, "TPArc14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TPArc14"):
                    opp_val = getattr(item, "TPArc14", None)
                    
                    setattr(item, "TPArc14", self)
                    

class lit_petriNets_Place:

    def __init__(self, name: str, Place: "lit_petriNets_Net" = None, places: "lit_petriNets_Net" = None, dst: set["lit_petriNets_TPArc"] = None, src: set["lit_petriNets_PTArc"] = None, Place27: "lit_petriNets_TPArc" = None, Place19: "lit_petriNets_PTArc" = None):
        self.name = name
        self.Place = Place
        self.places = places
        self.dst = dst if dst is not None else set()
        self.src = src if src is not None else set()
        self.Place27 = Place27
        self.Place19 = Place19
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Place27(self):
        return self.__Place27

    @Place27.setter
    def Place27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lit_petriNets_Place__Place27", None)
        self.__Place27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "in26"):
                opp_val = getattr(old_value, "in26", None)
                if opp_val == self:
                    setattr(old_value, "in26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "in26"):
                opp_val = getattr(value, "in26", None)
                setattr(value, "in26", self)

    @property
    def src(self):
        return self.__src

    @src.setter
    def src(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lit_petriNets_Place__src", None)
        self.__src = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PTArc"):
                    opp_val = getattr(item, "PTArc", None)
                    
                    if opp_val == self:
                        setattr(item, "PTArc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PTArc"):
                    opp_val = getattr(item, "PTArc", None)
                    
                    setattr(item, "PTArc", self)
                    

    @property
    def dst(self):
        return self.__dst

    @dst.setter
    def dst(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lit_petriNets_Place__dst", None)
        self.__dst = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TPArc"):
                    opp_val = getattr(item, "TPArc", None)
                    
                    if opp_val == self:
                        setattr(item, "TPArc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TPArc"):
                    opp_val = getattr(item, "TPArc", None)
                    
                    setattr(item, "TPArc", self)
                    

    @property
    def Place(self):
        return self.__Place

    @Place.setter
    def Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lit_petriNets_Place__Place", None)
        self.__Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "net"):
                opp_val = getattr(old_value, "net", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "net"):
                opp_val = getattr(value, "net", None)
                if opp_val is None:
                    setattr(value, "net", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def places(self):
        return self.__places

    @places.setter
    def places(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lit_petriNets_Place__places", None)
        self.__places = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Net"):
                opp_val = getattr(old_value, "Net", None)
                if opp_val == self:
                    setattr(old_value, "Net", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Net"):
                opp_val = getattr(value, "Net", None)
                setattr(value, "Net", self)

    @property
    def Place19(self):
        return self.__Place19

    @Place19.setter
    def Place19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lit_petriNets_Place__Place19", None)
        self.__Place19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "out"):
                opp_val = getattr(old_value, "out", None)
                if opp_val == self:
                    setattr(old_value, "out", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "out"):
                opp_val = getattr(value, "out", None)
                setattr(value, "out", self)

class lit_petriNets_Net:

    pass