from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Arc:

    pass
class lit_petriNets_Arc(ABC):

    pass
class lit_petriNets_Transition:

    def __init__(self, name: str, transitions: "lit_petriNets_Net" = None, dst11: set["lit_petriNets_PTArc"] = None, Transition: "lit_petriNets_Net" = None, src14: set["lit_petriNets_TPArc"] = None, Transition19: "lit_petriNets_PTArc" = None, Transition22: "lit_petriNets_TPArc" = None):
        self.name = name
        self.transitions = transitions
        self.dst11 = dst11 if dst11 is not None else set()
        self.Transition = Transition
        self.src14 = src14 if src14 is not None else set()
        self.Transition19 = Transition19
        self.Transition22 = Transition22
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Transition22(self):
        return self.__Transition22

    @Transition22.setter
    def Transition22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lit_petriNets_Transition__Transition22", None)
        self.__Transition22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "out21"):
                opp_val = getattr(old_value, "out21", None)
                if opp_val == self:
                    setattr(old_value, "out21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "out21"):
                opp_val = getattr(value, "out21", None)
                setattr(value, "out21", self)

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
            if hasattr(old_value, "Net9"):
                opp_val = getattr(old_value, "Net9", None)
                if opp_val == self:
                    setattr(old_value, "Net9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Net9"):
                opp_val = getattr(value, "Net9", None)
                setattr(value, "Net9", self)

    @property
    def Transition19(self):
        return self.__Transition19

    @Transition19.setter
    def Transition19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lit_petriNets_Transition__Transition19", None)
        self.__Transition19 = value
        
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
    def src14(self):
        return self.__src14

    @src14.setter
    def src14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lit_petriNets_Transition__src14", None)
        self.__src14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TPArc15"):
                    opp_val = getattr(item, "TPArc15", None)
                    
                    if opp_val == self:
                        setattr(item, "TPArc15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TPArc15"):
                    opp_val = getattr(item, "TPArc15", None)
                    
                    setattr(item, "TPArc15", self)
                    

    @property
    def dst11(self):
        return self.__dst11

    @dst11.setter
    def dst11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lit_petriNets_Transition__dst11", None)
        self.__dst11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PTArc12"):
                    opp_val = getattr(item, "PTArc12", None)
                    
                    if opp_val == self:
                        setattr(item, "PTArc12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PTArc12"):
                    opp_val = getattr(item, "PTArc12", None)
                    
                    setattr(item, "PTArc12", self)
                    

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

class lit_petriNets_Place:

    def __init__(self, name: str, places: "lit_petriNets_Net" = None, src: set["lit_petriNets_PTArc"] = None, dst: set["lit_petriNets_TPArc"] = None, Place: "lit_petriNets_Net" = None, Place17: "lit_petriNets_PTArc" = None, Place25: "lit_petriNets_TPArc" = None):
        self.name = name
        self.places = places
        self.src = src if src is not None else set()
        self.dst = dst if dst is not None else set()
        self.Place = Place
        self.Place17 = Place17
        self.Place25 = Place25
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Place17(self):
        return self.__Place17

    @Place17.setter
    def Place17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lit_petriNets_Place__Place17", None)
        self.__Place17 = value
        
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
    def Place25(self):
        return self.__Place25

    @Place25.setter
    def Place25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lit_petriNets_Place__Place25", None)
        self.__Place25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "in24"):
                opp_val = getattr(old_value, "in24", None)
                if opp_val == self:
                    setattr(old_value, "in24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "in24"):
                opp_val = getattr(value, "in24", None)
                setattr(value, "in24", self)

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
                    

class lit_petriNets_TPArc(Arc):

    pass
class lit_petriNets_PTArc(Arc):

    pass
class lit_petriNets_Net:

    pass