from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class PetriNets_Token:

    pass
class PetriNets_Transition:

    def __init__(self, priority: float, trans: "PetriNets_PetriNet" = None, PetriNets_Transition: set["PetriNets_Place"] = None, PetriNets_Transition10: set["PetriNets_Place"] = None, PetriNets_Transition13: set["PetriNets_Place"] = None, PetriNets_Transition16: set["PetriNets_Place"] = None, Transition: "PetriNets_PetriNet" = None):
        self.priority = priority
        self.trans = trans
        self.PetriNets_Transition = PetriNets_Transition if PetriNets_Transition is not None else set()
        self.PetriNets_Transition10 = PetriNets_Transition10 if PetriNets_Transition10 is not None else set()
        self.PetriNets_Transition13 = PetriNets_Transition13 if PetriNets_Transition13 is not None else set()
        self.PetriNets_Transition16 = PetriNets_Transition16 if PetriNets_Transition16 is not None else set()
        self.Transition = Transition
        
    @property
    def priority(self) -> float:
        return self.__priority

    @priority.setter
    def priority(self, priority: float):
        self.__priority = priority

    @property
    def PetriNets_Transition13(self):
        return self.__PetriNets_Transition13

    @PetriNets_Transition13.setter
    def PetriNets_Transition13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Transition__PetriNets_Transition13", None)
        self.__PetriNets_Transition13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNets_Place14"):
                    opp_val = getattr(item, "PetriNets_Place14", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNets_Place14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNets_Place14"):
                    opp_val = getattr(item, "PetriNets_Place14", None)
                    
                    setattr(item, "PetriNets_Place14", self)
                    

    @property
    def PetriNets_Transition(self):
        return self.__PetriNets_Transition

    @PetriNets_Transition.setter
    def PetriNets_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Transition__PetriNets_Transition", None)
        self.__PetriNets_Transition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNets_Place8"):
                    opp_val = getattr(item, "PetriNets_Place8", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNets_Place8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNets_Place8"):
                    opp_val = getattr(item, "PetriNets_Place8", None)
                    
                    setattr(item, "PetriNets_Place8", self)
                    

    @property
    def PetriNets_Transition10(self):
        return self.__PetriNets_Transition10

    @PetriNets_Transition10.setter
    def PetriNets_Transition10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Transition__PetriNets_Transition10", None)
        self.__PetriNets_Transition10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNets_Place11"):
                    opp_val = getattr(item, "PetriNets_Place11", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNets_Place11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNets_Place11"):
                    opp_val = getattr(item, "PetriNets_Place11", None)
                    
                    setattr(item, "PetriNets_Place11", self)
                    

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
    def PetriNets_Transition16(self):
        return self.__PetriNets_Transition16

    @PetriNets_Transition16.setter
    def PetriNets_Transition16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Transition__PetriNets_Transition16", None)
        self.__PetriNets_Transition16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNets_Place17"):
                    opp_val = getattr(item, "PetriNets_Place17", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNets_Place17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNets_Place17"):
                    opp_val = getattr(item, "PetriNets_Place17", None)
                    
                    setattr(item, "PetriNets_Place17", self)
                    

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
            if hasattr(old_value, "PetriNet6"):
                opp_val = getattr(old_value, "PetriNet6", None)
                if opp_val == self:
                    setattr(old_value, "PetriNet6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet6"):
                opp_val = getattr(value, "PetriNet6", None)
                setattr(value, "PetriNet6", self)

class PetriNets_Place:

    def __init__(self, itokens: int, bound: int, Place: "PetriNets_PetriNet" = None, PetriNets_Place: set["PetriNets_Token"] = None, PetriNets_Place8: "PetriNets_Transition" = None, PetriNets_Place11: "PetriNets_Transition" = None, PetriNets_Place14: "PetriNets_Transition" = None, PetriNets_Place17: "PetriNets_Transition" = None, places: "PetriNets_PetriNet" = None):
        self.itokens = itokens
        self.bound = bound
        self.Place = Place
        self.PetriNets_Place = PetriNets_Place if PetriNets_Place is not None else set()
        self.PetriNets_Place8 = PetriNets_Place8
        self.PetriNets_Place11 = PetriNets_Place11
        self.PetriNets_Place14 = PetriNets_Place14
        self.PetriNets_Place17 = PetriNets_Place17
        self.places = places
        
    @property
    def itokens(self) -> int:
        return self.__itokens

    @itokens.setter
    def itokens(self, itokens: int):
        self.__itokens = itokens

    @property
    def bound(self) -> int:
        return self.__bound

    @bound.setter
    def bound(self, bound: int):
        self.__bound = bound

    @property
    def PetriNets_Place11(self):
        return self.__PetriNets_Place11

    @PetriNets_Place11.setter
    def PetriNets_Place11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Place__PetriNets_Place11", None)
        self.__PetriNets_Place11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNets_Transition10"):
                opp_val = getattr(old_value, "PetriNets_Transition10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNets_Transition10"):
                opp_val = getattr(value, "PetriNets_Transition10", None)
                if opp_val is None:
                    setattr(value, "PetriNets_Transition10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def PetriNets_Place17(self):
        return self.__PetriNets_Place17

    @PetriNets_Place17.setter
    def PetriNets_Place17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Place__PetriNets_Place17", None)
        self.__PetriNets_Place17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNets_Transition16"):
                opp_val = getattr(old_value, "PetriNets_Transition16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNets_Transition16"):
                opp_val = getattr(value, "PetriNets_Transition16", None)
                if opp_val is None:
                    setattr(value, "PetriNets_Transition16", set([self]))
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
    def PetriNets_Place8(self):
        return self.__PetriNets_Place8

    @PetriNets_Place8.setter
    def PetriNets_Place8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Place__PetriNets_Place8", None)
        self.__PetriNets_Place8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNets_Transition"):
                opp_val = getattr(old_value, "PetriNets_Transition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNets_Transition"):
                opp_val = getattr(value, "PetriNets_Transition", None)
                if opp_val is None:
                    setattr(value, "PetriNets_Transition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "PetriNets_Transition13"):
                opp_val = getattr(old_value, "PetriNets_Transition13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNets_Transition13"):
                opp_val = getattr(value, "PetriNets_Transition13", None)
                if opp_val is None:
                    setattr(value, "PetriNets_Transition13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def tokens(self) -> int:
        # TODO: Implement tokens method
        pass

class PetriNets_PetriNet:

    pass