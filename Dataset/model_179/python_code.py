from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Arc:

    pass
class petrinets_TPArc(Arc):

    pass
class petrinets_PTArc(Arc):

    pass
class petrinets_Place:

    def __init__(self, name: str, places: "petrinets_Net" = None, Place: "petrinets_Net" = None, dst: set["petrinets_TPArc"] = None, src: set["petrinets_PTArc"] = None, Place27: "petrinets_TPArc" = None, Place19: "petrinets_PTArc" = None):
        self.name = name
        self.places = places
        self.Place = Place
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
    def src(self):
        return self.__src

    @src.setter
    def src(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinets_Place__src", None)
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
        old_value = getattr(self, f"_petrinets_Place__dst", None)
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
    def places(self):
        return self.__places

    @places.setter
    def places(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinets_Place__places", None)
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
    def Place27(self):
        return self.__Place27

    @Place27.setter
    def Place27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinets_Place__Place27", None)
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
    def Place(self):
        return self.__Place

    @Place.setter
    def Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinets_Place__Place", None)
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
    def Place19(self):
        return self.__Place19

    @Place19.setter
    def Place19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinets_Place__Place19", None)
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

class petrinets_Net:

    pass
class petrinets_Arc(ABC):

    pass
class petrinets_Transition:

    def __init__(self, name: str, Transition: "petrinets_Net" = None, dst11: set["petrinets_PTArc"] = None, src14: set["petrinets_TPArc"] = None, transitions: "petrinets_Net" = None, Transition21: "petrinets_PTArc" = None, Transition24: "petrinets_TPArc" = None):
        self.name = name
        self.Transition = Transition
        self.dst11 = dst11 if dst11 is not None else set()
        self.src14 = src14 if src14 is not None else set()
        self.transitions = transitions
        self.Transition21 = Transition21
        self.Transition24 = Transition24
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Transition24(self):
        return self.__Transition24

    @Transition24.setter
    def Transition24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinets_Transition__Transition24", None)
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
    def dst11(self):
        return self.__dst11

    @dst11.setter
    def dst11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinets_Transition__dst11", None)
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
    def src14(self):
        return self.__src14

    @src14.setter
    def src14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinets_Transition__src14", None)
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
    def transitions(self):
        return self.__transitions

    @transitions.setter
    def transitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinets_Transition__transitions", None)
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
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinets_Transition__Transition", None)
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
        old_value = getattr(self, f"_petrinets_Transition__Transition21", None)
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
