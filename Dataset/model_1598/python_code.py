from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class petrinet2_Transition:

    def __init__(self, name: str, petrinet2_Transition: "petrinet2_Net" = None, petrinet2_Transition4: set["petrinet2_Place"] = None, petrinet2_Transition7: set["petrinet2_Place"] = None):
        self.name = name
        self.petrinet2_Transition = petrinet2_Transition
        self.petrinet2_Transition4 = petrinet2_Transition4 if petrinet2_Transition4 is not None else set()
        self.petrinet2_Transition7 = petrinet2_Transition7 if petrinet2_Transition7 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petrinet2_Transition4(self):
        return self.__petrinet2_Transition4

    @petrinet2_Transition4.setter
    def petrinet2_Transition4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet2_Transition__petrinet2_Transition4", None)
        self.__petrinet2_Transition4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinet2_Place5"):
                    opp_val = getattr(item, "petrinet2_Place5", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet2_Place5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet2_Place5"):
                    opp_val = getattr(item, "petrinet2_Place5", None)
                    
                    setattr(item, "petrinet2_Place5", self)
                    

    @property
    def petrinet2_Transition(self):
        return self.__petrinet2_Transition

    @petrinet2_Transition.setter
    def petrinet2_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet2_Transition__petrinet2_Transition", None)
        self.__petrinet2_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet2_Net2"):
                opp_val = getattr(old_value, "petrinet2_Net2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet2_Net2"):
                opp_val = getattr(value, "petrinet2_Net2", None)
                if opp_val is None:
                    setattr(value, "petrinet2_Net2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinet2_Transition7(self):
        return self.__petrinet2_Transition7

    @petrinet2_Transition7.setter
    def petrinet2_Transition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet2_Transition__petrinet2_Transition7", None)
        self.__petrinet2_Transition7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinet2_Place8"):
                    opp_val = getattr(item, "petrinet2_Place8", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet2_Place8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet2_Place8"):
                    opp_val = getattr(item, "petrinet2_Place8", None)
                    
                    setattr(item, "petrinet2_Place8", self)
                    

class petrinet2_Place:

    def __init__(self, name: str, petrinet2_Place: "petrinet2_Net" = None, petrinet2_Place5: "petrinet2_Transition" = None, petrinet2_Place8: "petrinet2_Transition" = None):
        self.name = name
        self.petrinet2_Place = petrinet2_Place
        self.petrinet2_Place5 = petrinet2_Place5
        self.petrinet2_Place8 = petrinet2_Place8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petrinet2_Place5(self):
        return self.__petrinet2_Place5

    @petrinet2_Place5.setter
    def petrinet2_Place5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet2_Place__petrinet2_Place5", None)
        self.__petrinet2_Place5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet2_Transition4"):
                opp_val = getattr(old_value, "petrinet2_Transition4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet2_Transition4"):
                opp_val = getattr(value, "petrinet2_Transition4", None)
                if opp_val is None:
                    setattr(value, "petrinet2_Transition4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinet2_Place8(self):
        return self.__petrinet2_Place8

    @petrinet2_Place8.setter
    def petrinet2_Place8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet2_Place__petrinet2_Place8", None)
        self.__petrinet2_Place8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet2_Transition7"):
                opp_val = getattr(old_value, "petrinet2_Transition7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet2_Transition7"):
                opp_val = getattr(value, "petrinet2_Transition7", None)
                if opp_val is None:
                    setattr(value, "petrinet2_Transition7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinet2_Place(self):
        return self.__petrinet2_Place

    @petrinet2_Place.setter
    def petrinet2_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet2_Place__petrinet2_Place", None)
        self.__petrinet2_Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet2_Net"):
                opp_val = getattr(old_value, "petrinet2_Net", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet2_Net"):
                opp_val = getattr(value, "petrinet2_Net", None)
                if opp_val is None:
                    setattr(value, "petrinet2_Net", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class petrinet2_Net:

    def __init__(self, name: str, petrinet2_Net: set["petrinet2_Place"] = None, petrinet2_Net2: set["petrinet2_Transition"] = None):
        self.name = name
        self.petrinet2_Net = petrinet2_Net if petrinet2_Net is not None else set()
        self.petrinet2_Net2 = petrinet2_Net2 if petrinet2_Net2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petrinet2_Net(self):
        return self.__petrinet2_Net

    @petrinet2_Net.setter
    def petrinet2_Net(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet2_Net__petrinet2_Net", None)
        self.__petrinet2_Net = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinet2_Place"):
                    opp_val = getattr(item, "petrinet2_Place", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet2_Place", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet2_Place"):
                    opp_val = getattr(item, "petrinet2_Place", None)
                    
                    setattr(item, "petrinet2_Place", self)
                    

    @property
    def petrinet2_Net2(self):
        return self.__petrinet2_Net2

    @petrinet2_Net2.setter
    def petrinet2_Net2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet2_Net__petrinet2_Net2", None)
        self.__petrinet2_Net2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinet2_Transition"):
                    opp_val = getattr(item, "petrinet2_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet2_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet2_Transition"):
                    opp_val = getattr(item, "petrinet2_Transition", None)
                    
                    setattr(item, "petrinet2_Transition", self)
                    
