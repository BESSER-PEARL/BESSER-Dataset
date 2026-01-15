from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class petrinet_Transition:

    def __init__(self, name: str, petrinet_Transition6: set["petrinet_Place"] = None, petrinet_Transition9: set["petrinet_Place"] = None, petrinet_Transition: "petrinet_Net" = None):
        self.name = name
        self.petrinet_Transition6 = petrinet_Transition6 if petrinet_Transition6 is not None else set()
        self.petrinet_Transition9 = petrinet_Transition9 if petrinet_Transition9 is not None else set()
        self.petrinet_Transition = petrinet_Transition
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petrinet_Transition9(self):
        return self.__petrinet_Transition9

    @petrinet_Transition9.setter
    def petrinet_Transition9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Transition__petrinet_Transition9", None)
        self.__petrinet_Transition9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinet_Place10"):
                    opp_val = getattr(item, "petrinet_Place10", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_Place10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_Place10"):
                    opp_val = getattr(item, "petrinet_Place10", None)
                    
                    setattr(item, "petrinet_Place10", self)
                    

    @property
    def petrinet_Transition(self):
        return self.__petrinet_Transition

    @petrinet_Transition.setter
    def petrinet_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Transition__petrinet_Transition", None)
        self.__petrinet_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Net2"):
                opp_val = getattr(old_value, "petrinet_Net2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Net2"):
                opp_val = getattr(value, "petrinet_Net2", None)
                if opp_val is None:
                    setattr(value, "petrinet_Net2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinet_Transition6(self):
        return self.__petrinet_Transition6

    @petrinet_Transition6.setter
    def petrinet_Transition6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Transition__petrinet_Transition6", None)
        self.__petrinet_Transition6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinet_Place7"):
                    opp_val = getattr(item, "petrinet_Place7", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_Place7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_Place7"):
                    opp_val = getattr(item, "petrinet_Place7", None)
                    
                    setattr(item, "petrinet_Place7", self)
                    

class petrinet_Place:

    def __init__(self, name: str, initialTokens: int, petrinet_Place4: set["petrinet_Token"] = None, petrinet_Place7: "petrinet_Transition" = None, petrinet_Place10: "petrinet_Transition" = None, petrinet_Place: "petrinet_Net" = None):
        self.name = name
        self.initialTokens = initialTokens
        self.petrinet_Place4 = petrinet_Place4 if petrinet_Place4 is not None else set()
        self.petrinet_Place7 = petrinet_Place7
        self.petrinet_Place10 = petrinet_Place10
        self.petrinet_Place = petrinet_Place
        
    @property
    def initialTokens(self) -> int:
        return self.__initialTokens

    @initialTokens.setter
    def initialTokens(self, initialTokens: int):
        self.__initialTokens = initialTokens

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petrinet_Place7(self):
        return self.__petrinet_Place7

    @petrinet_Place7.setter
    def petrinet_Place7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__petrinet_Place7", None)
        self.__petrinet_Place7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Transition6"):
                opp_val = getattr(old_value, "petrinet_Transition6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Transition6"):
                opp_val = getattr(value, "petrinet_Transition6", None)
                if opp_val is None:
                    setattr(value, "petrinet_Transition6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinet_Place(self):
        return self.__petrinet_Place

    @petrinet_Place.setter
    def petrinet_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__petrinet_Place", None)
        self.__petrinet_Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Net"):
                opp_val = getattr(old_value, "petrinet_Net", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Net"):
                opp_val = getattr(value, "petrinet_Net", None)
                if opp_val is None:
                    setattr(value, "petrinet_Net", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinet_Place10(self):
        return self.__petrinet_Place10

    @petrinet_Place10.setter
    def petrinet_Place10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__petrinet_Place10", None)
        self.__petrinet_Place10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Transition9"):
                opp_val = getattr(old_value, "petrinet_Transition9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Transition9"):
                opp_val = getattr(value, "petrinet_Transition9", None)
                if opp_val is None:
                    setattr(value, "petrinet_Transition9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinet_Place4(self):
        return self.__petrinet_Place4

    @petrinet_Place4.setter
    def petrinet_Place4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__petrinet_Place4", None)
        self.__petrinet_Place4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinet_Token"):
                    opp_val = getattr(item, "petrinet_Token", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_Token", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_Token"):
                    opp_val = getattr(item, "petrinet_Token", None)
                    
                    setattr(item, "petrinet_Token", self)
                    

class petrinet_Net:

    pass
class petrinet_Token:

    pass