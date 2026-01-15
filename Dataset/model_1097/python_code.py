from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class lit_petriNets_Transition:

    def __init__(self, name: str, transitions: "lit_petriNets_Net" = None, dst11: set["lit_petriNets_Place"] = None, src14: set["lit_petriNets_Place"] = None, Transition: "lit_petriNets_Net" = None, Transition5: "lit_petriNets_Place" = None, Transition7: "lit_petriNets_Place" = None):
        self.name = name
        self.transitions = transitions
        self.dst11 = dst11 if dst11 is not None else set()
        self.src14 = src14 if src14 is not None else set()
        self.Transition = Transition
        self.Transition5 = Transition5
        self.Transition7 = Transition7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
                if hasattr(item, "Place15"):
                    opp_val = getattr(item, "Place15", None)
                    
                    if opp_val == self:
                        setattr(item, "Place15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Place15"):
                    opp_val = getattr(item, "Place15", None)
                    
                    setattr(item, "Place15", self)
                    

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
                if hasattr(item, "Place12"):
                    opp_val = getattr(item, "Place12", None)
                    
                    if opp_val == self:
                        setattr(item, "Place12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Place12"):
                    opp_val = getattr(item, "Place12", None)
                    
                    setattr(item, "Place12", self)
                    

    @property
    def Transition7(self):
        return self.__Transition7

    @Transition7.setter
    def Transition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lit_petriNets_Transition__Transition7", None)
        self.__Transition7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "src"):
                opp_val = getattr(old_value, "src", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "src"):
                opp_val = getattr(value, "src", None)
                if opp_val is None:
                    setattr(value, "src", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def Transition5(self):
        return self.__Transition5

    @Transition5.setter
    def Transition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lit_petriNets_Transition__Transition5", None)
        self.__Transition5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dst"):
                opp_val = getattr(old_value, "dst", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dst"):
                opp_val = getattr(value, "dst", None)
                if opp_val is None:
                    setattr(value, "dst", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class lit_petriNets_Place:

    def __init__(self, name: str, Place: "lit_petriNets_Net" = None, Place12: "lit_petriNets_Transition" = None, Place15: "lit_petriNets_Transition" = None, places: "lit_petriNets_Net" = None, dst: set["lit_petriNets_Transition"] = None, src: set["lit_petriNets_Transition"] = None):
        self.name = name
        self.Place = Place
        self.Place12 = Place12
        self.Place15 = Place15
        self.places = places
        self.dst = dst if dst is not None else set()
        self.src = src if src is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
                if hasattr(item, "Transition5"):
                    opp_val = getattr(item, "Transition5", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition5"):
                    opp_val = getattr(item, "Transition5", None)
                    
                    setattr(item, "Transition5", self)
                    

    @property
    def Place12(self):
        return self.__Place12

    @Place12.setter
    def Place12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lit_petriNets_Place__Place12", None)
        self.__Place12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dst11"):
                opp_val = getattr(old_value, "dst11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dst11"):
                opp_val = getattr(value, "dst11", None)
                if opp_val is None:
                    setattr(value, "dst11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Place15(self):
        return self.__Place15

    @Place15.setter
    def Place15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lit_petriNets_Place__Place15", None)
        self.__Place15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "src14"):
                opp_val = getattr(old_value, "src14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "src14"):
                opp_val = getattr(value, "src14", None)
                if opp_val is None:
                    setattr(value, "src14", set([self]))
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
                    

class lit_petriNets_Net:

    pass