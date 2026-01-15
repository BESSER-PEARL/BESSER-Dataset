from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Arc:

    pass
class PetriNets_ArcTP(Arc):

    pass
class PetriNets_ArcPT(Arc):

    pass
class PetriNets_Token:

    pass
class PetriNets_Arc(ABC):

    def __init__(self, weight: int, PetriNets_Arc: "PetriNets_PetriNet" = None):
        self.weight = weight
        self.PetriNets_Arc = PetriNets_Arc
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def PetriNets_Arc(self):
        return self.__PetriNets_Arc

    @PetriNets_Arc.setter
    def PetriNets_Arc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Arc__PetriNets_Arc", None)
        self.__PetriNets_Arc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNets_PetriNet"):
                opp_val = getattr(old_value, "PetriNets_PetriNet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNets_PetriNet"):
                opp_val = getattr(value, "PetriNets_PetriNet", None)
                if opp_val is None:
                    setattr(value, "PetriNets_PetriNet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PetriNets_Transition:

    def __init__(self, priority: float, Transition: "PetriNets_PetriNet" = None, PetriNets_Transition: "PetriNets_ArcPT" = None, trans: "PetriNets_PetriNet" = None, PetriNets_Transition18: set["PetriNets_Place"] = None, PetriNets_Transition21: set["PetriNets_Place"] = None, PetriNets_Transition24: set["PetriNets_Place"] = None, PetriNets_Transition11: "PetriNets_ArcTP" = None, PetriNets_Transition27: set["PetriNets_Place"] = None, PetriNets_Transition30: set["PetriNets_Place"] = None):
        self.priority = priority
        self.Transition = Transition
        self.PetriNets_Transition = PetriNets_Transition
        self.trans = trans
        self.PetriNets_Transition18 = PetriNets_Transition18 if PetriNets_Transition18 is not None else set()
        self.PetriNets_Transition21 = PetriNets_Transition21 if PetriNets_Transition21 is not None else set()
        self.PetriNets_Transition24 = PetriNets_Transition24 if PetriNets_Transition24 is not None else set()
        self.PetriNets_Transition11 = PetriNets_Transition11
        self.PetriNets_Transition27 = PetriNets_Transition27 if PetriNets_Transition27 is not None else set()
        self.PetriNets_Transition30 = PetriNets_Transition30 if PetriNets_Transition30 is not None else set()
        
    @property
    def priority(self) -> float:
        return self.__priority

    @priority.setter
    def priority(self, priority: float):
        self.__priority = priority

    @property
    def PetriNets_Transition(self):
        return self.__PetriNets_Transition

    @PetriNets_Transition.setter
    def PetriNets_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Transition__PetriNets_Transition", None)
        self.__PetriNets_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNets_ArcPT9"):
                opp_val = getattr(old_value, "PetriNets_ArcPT9", None)
                if opp_val == self:
                    setattr(old_value, "PetriNets_ArcPT9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNets_ArcPT9"):
                opp_val = getattr(value, "PetriNets_ArcPT9", None)
                setattr(value, "PetriNets_ArcPT9", self)

    @property
    def PetriNets_Transition21(self):
        return self.__PetriNets_Transition21

    @PetriNets_Transition21.setter
    def PetriNets_Transition21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Transition__PetriNets_Transition21", None)
        self.__PetriNets_Transition21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNets_Place22"):
                    opp_val = getattr(item, "PetriNets_Place22", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNets_Place22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNets_Place22"):
                    opp_val = getattr(item, "PetriNets_Place22", None)
                    
                    setattr(item, "PetriNets_Place22", self)
                    

    @property
    def trans(self):
        return self.__trans

    @trans.setter
    def trans(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Transition__trans", None)
        self.__trans = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet16"):
                opp_val = getattr(old_value, "PetriNet16", None)
                if opp_val == self:
                    setattr(old_value, "PetriNet16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet16"):
                opp_val = getattr(value, "PetriNet16", None)
                setattr(value, "PetriNet16", self)

    @property
    def PetriNets_Transition18(self):
        return self.__PetriNets_Transition18

    @PetriNets_Transition18.setter
    def PetriNets_Transition18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Transition__PetriNets_Transition18", None)
        self.__PetriNets_Transition18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNets_Place19"):
                    opp_val = getattr(item, "PetriNets_Place19", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNets_Place19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNets_Place19"):
                    opp_val = getattr(item, "PetriNets_Place19", None)
                    
                    setattr(item, "PetriNets_Place19", self)
                    

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Transition__Transition", None)
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
    def PetriNets_Transition30(self):
        return self.__PetriNets_Transition30

    @PetriNets_Transition30.setter
    def PetriNets_Transition30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Transition__PetriNets_Transition30", None)
        self.__PetriNets_Transition30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNets_Place31"):
                    opp_val = getattr(item, "PetriNets_Place31", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNets_Place31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNets_Place31"):
                    opp_val = getattr(item, "PetriNets_Place31", None)
                    
                    setattr(item, "PetriNets_Place31", self)
                    

    @property
    def PetriNets_Transition11(self):
        return self.__PetriNets_Transition11

    @PetriNets_Transition11.setter
    def PetriNets_Transition11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Transition__PetriNets_Transition11", None)
        self.__PetriNets_Transition11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNets_ArcTP"):
                opp_val = getattr(old_value, "PetriNets_ArcTP", None)
                if opp_val == self:
                    setattr(old_value, "PetriNets_ArcTP", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNets_ArcTP"):
                opp_val = getattr(value, "PetriNets_ArcTP", None)
                setattr(value, "PetriNets_ArcTP", self)

    @property
    def PetriNets_Transition27(self):
        return self.__PetriNets_Transition27

    @PetriNets_Transition27.setter
    def PetriNets_Transition27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Transition__PetriNets_Transition27", None)
        self.__PetriNets_Transition27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNets_Place28"):
                    opp_val = getattr(item, "PetriNets_Place28", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNets_Place28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNets_Place28"):
                    opp_val = getattr(item, "PetriNets_Place28", None)
                    
                    setattr(item, "PetriNets_Place28", self)
                    

    @property
    def PetriNets_Transition24(self):
        return self.__PetriNets_Transition24

    @PetriNets_Transition24.setter
    def PetriNets_Transition24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Transition__PetriNets_Transition24", None)
        self.__PetriNets_Transition24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNets_Place25"):
                    opp_val = getattr(item, "PetriNets_Place25", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNets_Place25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNets_Place25"):
                    opp_val = getattr(item, "PetriNets_Place25", None)
                    
                    setattr(item, "PetriNets_Place25", self)
                    

    def outputs(self) -> str:
        # TODO: Implement outputs method
        pass

    def inputs(self) -> str:
        # TODO: Implement inputs method
        pass

class PetriNets_Place:

    def __init__(self, itokens: int, bound: int, Place: "PetriNets_PetriNet" = None, PetriNets_Place: set["PetriNets_Token"] = None, PetriNets_Place7: "PetriNets_ArcPT" = None, places: "PetriNets_PetriNet" = None, PetriNets_Place19: "PetriNets_Transition" = None, PetriNets_Place22: "PetriNets_Transition" = None, PetriNets_Place25: "PetriNets_Transition" = None, PetriNets_Place14: "PetriNets_ArcTP" = None, PetriNets_Place28: "PetriNets_Transition" = None, PetriNets_Place31: "PetriNets_Transition" = None):
        self.itokens = itokens
        self.bound = bound
        self.Place = Place
        self.PetriNets_Place = PetriNets_Place if PetriNets_Place is not None else set()
        self.PetriNets_Place7 = PetriNets_Place7
        self.places = places
        self.PetriNets_Place19 = PetriNets_Place19
        self.PetriNets_Place22 = PetriNets_Place22
        self.PetriNets_Place25 = PetriNets_Place25
        self.PetriNets_Place14 = PetriNets_Place14
        self.PetriNets_Place28 = PetriNets_Place28
        self.PetriNets_Place31 = PetriNets_Place31
        
    @property
    def bound(self) -> int:
        return self.__bound

    @bound.setter
    def bound(self, bound: int):
        self.__bound = bound

    @property
    def itokens(self) -> int:
        return self.__itokens

    @itokens.setter
    def itokens(self, itokens: int):
        self.__itokens = itokens

    @property
    def PetriNets_Place25(self):
        return self.__PetriNets_Place25

    @PetriNets_Place25.setter
    def PetriNets_Place25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Place__PetriNets_Place25", None)
        self.__PetriNets_Place25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNets_Transition24"):
                opp_val = getattr(old_value, "PetriNets_Transition24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNets_Transition24"):
                opp_val = getattr(value, "PetriNets_Transition24", None)
                if opp_val is None:
                    setattr(value, "PetriNets_Transition24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PetriNets_Place22(self):
        return self.__PetriNets_Place22

    @PetriNets_Place22.setter
    def PetriNets_Place22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Place__PetriNets_Place22", None)
        self.__PetriNets_Place22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNets_Transition21"):
                opp_val = getattr(old_value, "PetriNets_Transition21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNets_Transition21"):
                opp_val = getattr(value, "PetriNets_Transition21", None)
                if opp_val is None:
                    setattr(value, "PetriNets_Transition21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def places(self):
        return self.__places

    @places.setter
    def places(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Place__places", None)
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
    def PetriNets_Place31(self):
        return self.__PetriNets_Place31

    @PetriNets_Place31.setter
    def PetriNets_Place31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Place__PetriNets_Place31", None)
        self.__PetriNets_Place31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNets_Transition30"):
                opp_val = getattr(old_value, "PetriNets_Transition30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNets_Transition30"):
                opp_val = getattr(value, "PetriNets_Transition30", None)
                if opp_val is None:
                    setattr(value, "PetriNets_Transition30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PetriNets_Place7(self):
        return self.__PetriNets_Place7

    @PetriNets_Place7.setter
    def PetriNets_Place7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Place__PetriNets_Place7", None)
        self.__PetriNets_Place7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNets_ArcPT"):
                opp_val = getattr(old_value, "PetriNets_ArcPT", None)
                if opp_val == self:
                    setattr(old_value, "PetriNets_ArcPT", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNets_ArcPT"):
                opp_val = getattr(value, "PetriNets_ArcPT", None)
                setattr(value, "PetriNets_ArcPT", self)

    @property
    def PetriNets_Place14(self):
        return self.__PetriNets_Place14

    @PetriNets_Place14.setter
    def PetriNets_Place14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Place__PetriNets_Place14", None)
        self.__PetriNets_Place14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNets_ArcTP13"):
                opp_val = getattr(old_value, "PetriNets_ArcTP13", None)
                if opp_val == self:
                    setattr(old_value, "PetriNets_ArcTP13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNets_ArcTP13"):
                opp_val = getattr(value, "PetriNets_ArcTP13", None)
                setattr(value, "PetriNets_ArcTP13", self)

    @property
    def PetriNets_Place28(self):
        return self.__PetriNets_Place28

    @PetriNets_Place28.setter
    def PetriNets_Place28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Place__PetriNets_Place28", None)
        self.__PetriNets_Place28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNets_Transition27"):
                opp_val = getattr(old_value, "PetriNets_Transition27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNets_Transition27"):
                opp_val = getattr(value, "PetriNets_Transition27", None)
                if opp_val is None:
                    setattr(value, "PetriNets_Transition27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PetriNets_Place(self):
        return self.__PetriNets_Place

    @PetriNets_Place.setter
    def PetriNets_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Place__PetriNets_Place", None)
        self.__PetriNets_Place = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNets_Token"):
                    opp_val = getattr(item, "PetriNets_Token", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNets_Token", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNets_Token"):
                    opp_val = getattr(item, "PetriNets_Token", None)
                    
                    setattr(item, "PetriNets_Token", self)
                    

    @property
    def Place(self):
        return self.__Place

    @Place.setter
    def Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Place__Place", None)
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
    def PetriNets_Place19(self):
        return self.__PetriNets_Place19

    @PetriNets_Place19.setter
    def PetriNets_Place19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Place__PetriNets_Place19", None)
        self.__PetriNets_Place19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNets_Transition18"):
                opp_val = getattr(old_value, "PetriNets_Transition18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNets_Transition18"):
                opp_val = getattr(value, "PetriNets_Transition18", None)
                if opp_val is None:
                    setattr(value, "PetriNets_Transition18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def tokens(self) -> int:
        # TODO: Implement tokens method
        pass

class PetriNets_PetriNet:

    pass