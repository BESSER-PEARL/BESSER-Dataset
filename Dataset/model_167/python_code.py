from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class lit_petriNets_Transition:

    def __init__(self, name: str, Transition: "lit_petriNets_Net" = None, transitions: "lit_petriNets_Net" = None, dst11: set["lit_petriNets_Place"] = None, src14: set["lit_petriNets_Place"] = None, Transition5: "lit_petriNets_Place" = None, Transition7: "lit_petriNets_Place" = None):
        self.name = name
        self.Transition = Transition
        self.transitions = transitions
        self.dst11 = dst11 if dst11 is not None else set()
        self.src14 = src14 if src14 is not None else set()
        self.Transition5 = Transition5
        self.Transition7 = Transition7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
                    

class lit_petriNets_Place:

    def __init__(self, name: str, Place: "lit_petriNets_Net" = None, places: "lit_petriNets_Net" = None, Place12: "lit_petriNets_Transition" = None, Place15: "lit_petriNets_Transition" = None, dst: set["lit_petriNets_Transition"] = None, src: set["lit_petriNets_Transition"] = None):
        self.name = name
        self.Place = Place
        self.places = places
        self.Place12 = Place12
        self.Place15 = Place15
        self.dst = dst if dst is not None else set()
        self.src = src if src is not None else set()
        
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

class lit_petriNets_Net:

    def __init__(self, name: str, net: set["lit_petriNets_Place"] = None, net2: set["lit_petriNets_Transition"] = None, Net: "lit_petriNets_Place" = None, Net9: "lit_petriNets_Transition" = None):
        self.name = name
        self.net = net if net is not None else set()
        self.net2 = net2 if net2 is not None else set()
        self.Net = Net
        self.Net9 = Net9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def net(self):
        return self.__net

    @net.setter
    def net(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lit_petriNets_Net__net", None)
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
    def Net9(self):
        return self.__Net9

    @Net9.setter
    def Net9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lit_petriNets_Net__Net9", None)
        self.__Net9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transitions"):
                opp_val = getattr(old_value, "transitions", None)
                if opp_val == self:
                    setattr(old_value, "transitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transitions"):
                opp_val = getattr(value, "transitions", None)
                setattr(value, "transitions", self)

    @property
    def net2(self):
        return self.__net2

    @net2.setter
    def net2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lit_petriNets_Net__net2", None)
        self.__net2 = value if value is not None else set()
        
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
    def Net(self):
        return self.__Net

    @Net.setter
    def Net(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lit_petriNets_Net__Net", None)
        self.__Net = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "places"):
                opp_val = getattr(old_value, "places", None)
                if opp_val == self:
                    setattr(old_value, "places", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "places"):
                opp_val = getattr(value, "places", None)
                setattr(value, "places", self)
