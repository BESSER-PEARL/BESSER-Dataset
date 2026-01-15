from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class PN_Transition:

    def __init__(self, input: str, Transition: "PN_Place" = None, Transition5: "PN_Place" = None, outgoing: set["PN_Place"] = None, incoming: set["PN_Place"] = None, PN_Transition: "PN_Net" = None):
        self.input = input
        self.Transition = Transition
        self.Transition5 = Transition5
        self.outgoing = outgoing if outgoing is not None else set()
        self.incoming = incoming if incoming is not None else set()
        self.PN_Transition = PN_Transition
        
    @property
    def input(self) -> str:
        return self.__input

    @input.setter
    def input(self, input: str):
        self.__input = input

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PN_Transition__outgoing", None)
        self.__outgoing = value if value is not None else set()
        
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
    def PN_Transition(self):
        return self.__PN_Transition

    @PN_Transition.setter
    def PN_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PN_Transition__PN_Transition", None)
        self.__PN_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PN_Net2"):
                opp_val = getattr(old_value, "PN_Net2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PN_Net2"):
                opp_val = getattr(value, "PN_Net2", None)
                if opp_val is None:
                    setattr(value, "PN_Net2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PN_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "to"):
                opp_val = getattr(old_value, "to", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "to"):
                opp_val = getattr(value, "to", None)
                if opp_val is None:
                    setattr(value, "to", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PN_Transition__incoming", None)
        self.__incoming = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Place8"):
                    opp_val = getattr(item, "Place8", None)
                    
                    if opp_val == self:
                        setattr(item, "Place8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Place8"):
                    opp_val = getattr(item, "Place8", None)
                    
                    setattr(item, "Place8", self)
                    

    @property
    def Transition5(self):
        return self.__Transition5

    @Transition5.setter
    def Transition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PN_Transition__Transition5", None)
        self.__Transition5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "from"):
                opp_val = getattr(old_value, "from", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "from"):
                opp_val = getattr(value, "from", None)
                if opp_val is None:
                    setattr(value, "from", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PN_Place:

    def __init__(self, name: str, to: set["PN_Transition"] = None, from: set["PN_Transition"] = None, Place: "PN_Transition" = None, Place8: "PN_Transition" = None, PN_Place: "PN_Net" = None):
        self.name = name
        self.to = to if to is not None else set()
        self.from = from if from is not None else set()
        self.Place = Place
        self.Place8 = Place8
        self.PN_Place = PN_Place
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Place8(self):
        return self.__Place8

    @Place8.setter
    def Place8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PN_Place__Place8", None)
        self.__Place8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incoming"):
                opp_val = getattr(old_value, "incoming", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incoming"):
                opp_val = getattr(value, "incoming", None)
                if opp_val is None:
                    setattr(value, "incoming", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def to(self):
        return self.__to

    @to.setter
    def to(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PN_Place__to", None)
        self.__to = value if value is not None else set()
        
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
    def PN_Place(self):
        return self.__PN_Place

    @PN_Place.setter
    def PN_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PN_Place__PN_Place", None)
        self.__PN_Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PN_Net"):
                opp_val = getattr(old_value, "PN_Net", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PN_Net"):
                opp_val = getattr(value, "PN_Net", None)
                if opp_val is None:
                    setattr(value, "PN_Net", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def from(self):
        return self.__from

    @from.setter
    def from(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PN_Place__from", None)
        self.__from = value if value is not None else set()
        
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
    def Place(self):
        return self.__Place

    @Place.setter
    def Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PN_Place__Place", None)
        self.__Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoing"):
                opp_val = getattr(old_value, "outgoing", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoing"):
                opp_val = getattr(value, "outgoing", None)
                if opp_val is None:
                    setattr(value, "outgoing", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PN_Net:

    def __init__(self, name: str, PN_Net: set["PN_Place"] = None, PN_Net2: set["PN_Transition"] = None):
        self.name = name
        self.PN_Net = PN_Net if PN_Net is not None else set()
        self.PN_Net2 = PN_Net2 if PN_Net2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PN_Net2(self):
        return self.__PN_Net2

    @PN_Net2.setter
    def PN_Net2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PN_Net__PN_Net2", None)
        self.__PN_Net2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PN_Transition"):
                    opp_val = getattr(item, "PN_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "PN_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PN_Transition"):
                    opp_val = getattr(item, "PN_Transition", None)
                    
                    setattr(item, "PN_Transition", self)
                    

    @property
    def PN_Net(self):
        return self.__PN_Net

    @PN_Net.setter
    def PN_Net(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PN_Net__PN_Net", None)
        self.__PN_Net = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PN_Place"):
                    opp_val = getattr(item, "PN_Place", None)
                    
                    if opp_val == self:
                        setattr(item, "PN_Place", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PN_Place"):
                    opp_val = getattr(item, "PN_Place", None)
                    
                    setattr(item, "PN_Place", self)
                    
