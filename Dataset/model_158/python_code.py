from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class petrinet_Token:

    pass
class petrinet_Arc:

    def __init__(self, name: str, weight: int, petrinet_Arc: "petrinet_Petrinet" = None):
        self.name = name
        self.weight = weight
        self.petrinet_Arc = petrinet_Arc
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petrinet_Arc(self):
        return self.__petrinet_Arc

    @petrinet_Arc.setter
    def petrinet_Arc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Arc__petrinet_Arc", None)
        self.__petrinet_Arc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Petrinet4"):
                opp_val = getattr(old_value, "petrinet_Petrinet4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Petrinet4"):
                opp_val = getattr(value, "petrinet_Petrinet4", None)
                if opp_val is None:
                    setattr(value, "petrinet_Petrinet4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Arc:

    pass
class petrinet_PTArc(Arc):

    pass
class petrinet_TPArc(Arc):

    pass
class petrinet_Transition:

    def __init__(self, name: str, petrinet_Transition: "petrinet_Petrinet" = None, petrinet_Transition12: set["petrinet_TPArc"] = None, petrinet_Transition15: set["petrinet_PTArc"] = None, petrinet_Transition22: "petrinet_PTArc" = None, petrinet_Transition25: "petrinet_TPArc" = None):
        self.name = name
        self.petrinet_Transition = petrinet_Transition
        self.petrinet_Transition12 = petrinet_Transition12 if petrinet_Transition12 is not None else set()
        self.petrinet_Transition15 = petrinet_Transition15 if petrinet_Transition15 is not None else set()
        self.petrinet_Transition22 = petrinet_Transition22
        self.petrinet_Transition25 = petrinet_Transition25
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petrinet_Transition12(self):
        return self.__petrinet_Transition12

    @petrinet_Transition12.setter
    def petrinet_Transition12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Transition__petrinet_Transition12", None)
        self.__petrinet_Transition12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinet_TPArc13"):
                    opp_val = getattr(item, "petrinet_TPArc13", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_TPArc13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_TPArc13"):
                    opp_val = getattr(item, "petrinet_TPArc13", None)
                    
                    setattr(item, "petrinet_TPArc13", self)
                    

    @property
    def petrinet_Transition25(self):
        return self.__petrinet_Transition25

    @petrinet_Transition25.setter
    def petrinet_Transition25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Transition__petrinet_Transition25", None)
        self.__petrinet_Transition25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_TPArc24"):
                opp_val = getattr(old_value, "petrinet_TPArc24", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_TPArc24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_TPArc24"):
                opp_val = getattr(value, "petrinet_TPArc24", None)
                setattr(value, "petrinet_TPArc24", self)

    @property
    def petrinet_Transition15(self):
        return self.__petrinet_Transition15

    @petrinet_Transition15.setter
    def petrinet_Transition15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Transition__petrinet_Transition15", None)
        self.__petrinet_Transition15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinet_PTArc16"):
                    opp_val = getattr(item, "petrinet_PTArc16", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_PTArc16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_PTArc16"):
                    opp_val = getattr(item, "petrinet_PTArc16", None)
                    
                    setattr(item, "petrinet_PTArc16", self)
                    

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
            if hasattr(old_value, "petrinet_Petrinet2"):
                opp_val = getattr(old_value, "petrinet_Petrinet2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Petrinet2"):
                opp_val = getattr(value, "petrinet_Petrinet2", None)
                if opp_val is None:
                    setattr(value, "petrinet_Petrinet2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinet_Transition22(self):
        return self.__petrinet_Transition22

    @petrinet_Transition22.setter
    def petrinet_Transition22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Transition__petrinet_Transition22", None)
        self.__petrinet_Transition22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_PTArc21"):
                opp_val = getattr(old_value, "petrinet_PTArc21", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_PTArc21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_PTArc21"):
                opp_val = getattr(value, "petrinet_PTArc21", None)
                setattr(value, "petrinet_PTArc21", self)

class petrinet_Place:

    def __init__(self, name: str, petrinet_Place: "petrinet_Petrinet" = None, petrinet_Place6: set["petrinet_Token"] = None, petrinet_Place8: set["petrinet_PTArc"] = None, petrinet_Place10: set["petrinet_TPArc"] = None, petrinet_Place19: "petrinet_PTArc" = None, petrinet_Place28: "petrinet_TPArc" = None):
        self.name = name
        self.petrinet_Place = petrinet_Place
        self.petrinet_Place6 = petrinet_Place6 if petrinet_Place6 is not None else set()
        self.petrinet_Place8 = petrinet_Place8 if petrinet_Place8 is not None else set()
        self.petrinet_Place10 = petrinet_Place10 if petrinet_Place10 is not None else set()
        self.petrinet_Place19 = petrinet_Place19
        self.petrinet_Place28 = petrinet_Place28
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petrinet_Place28(self):
        return self.__petrinet_Place28

    @petrinet_Place28.setter
    def petrinet_Place28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__petrinet_Place28", None)
        self.__petrinet_Place28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_TPArc27"):
                opp_val = getattr(old_value, "petrinet_TPArc27", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_TPArc27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_TPArc27"):
                opp_val = getattr(value, "petrinet_TPArc27", None)
                setattr(value, "petrinet_TPArc27", self)

    @property
    def petrinet_Place8(self):
        return self.__petrinet_Place8

    @petrinet_Place8.setter
    def petrinet_Place8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__petrinet_Place8", None)
        self.__petrinet_Place8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinet_PTArc"):
                    opp_val = getattr(item, "petrinet_PTArc", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_PTArc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_PTArc"):
                    opp_val = getattr(item, "petrinet_PTArc", None)
                    
                    setattr(item, "petrinet_PTArc", self)
                    

    @property
    def petrinet_Place19(self):
        return self.__petrinet_Place19

    @petrinet_Place19.setter
    def petrinet_Place19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__petrinet_Place19", None)
        self.__petrinet_Place19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_PTArc18"):
                opp_val = getattr(old_value, "petrinet_PTArc18", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_PTArc18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_PTArc18"):
                opp_val = getattr(value, "petrinet_PTArc18", None)
                setattr(value, "petrinet_PTArc18", self)

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
            if hasattr(old_value, "petrinet_Petrinet"):
                opp_val = getattr(old_value, "petrinet_Petrinet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Petrinet"):
                opp_val = getattr(value, "petrinet_Petrinet", None)
                if opp_val is None:
                    setattr(value, "petrinet_Petrinet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinet_Place6(self):
        return self.__petrinet_Place6

    @petrinet_Place6.setter
    def petrinet_Place6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__petrinet_Place6", None)
        self.__petrinet_Place6 = value if value is not None else set()
        
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
                    

    @property
    def petrinet_Place10(self):
        return self.__petrinet_Place10

    @petrinet_Place10.setter
    def petrinet_Place10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__petrinet_Place10", None)
        self.__petrinet_Place10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinet_TPArc"):
                    opp_val = getattr(item, "petrinet_TPArc", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_TPArc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_TPArc"):
                    opp_val = getattr(item, "petrinet_TPArc", None)
                    
                    setattr(item, "petrinet_TPArc", self)
                    

class petrinet_Petrinet:

    def __init__(self, name: str, petrinet_Petrinet: set["petrinet_Place"] = None, petrinet_Petrinet2: set["petrinet_Transition"] = None, petrinet_Petrinet4: set["petrinet_Arc"] = None):
        self.name = name
        self.petrinet_Petrinet = petrinet_Petrinet if petrinet_Petrinet is not None else set()
        self.petrinet_Petrinet2 = petrinet_Petrinet2 if petrinet_Petrinet2 is not None else set()
        self.petrinet_Petrinet4 = petrinet_Petrinet4 if petrinet_Petrinet4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petrinet_Petrinet(self):
        return self.__petrinet_Petrinet

    @petrinet_Petrinet.setter
    def petrinet_Petrinet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Petrinet__petrinet_Petrinet", None)
        self.__petrinet_Petrinet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinet_Place"):
                    opp_val = getattr(item, "petrinet_Place", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_Place", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_Place"):
                    opp_val = getattr(item, "petrinet_Place", None)
                    
                    setattr(item, "petrinet_Place", self)
                    

    @property
    def petrinet_Petrinet4(self):
        return self.__petrinet_Petrinet4

    @petrinet_Petrinet4.setter
    def petrinet_Petrinet4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Petrinet__petrinet_Petrinet4", None)
        self.__petrinet_Petrinet4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinet_Arc"):
                    opp_val = getattr(item, "petrinet_Arc", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_Arc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_Arc"):
                    opp_val = getattr(item, "petrinet_Arc", None)
                    
                    setattr(item, "petrinet_Arc", self)
                    

    @property
    def petrinet_Petrinet2(self):
        return self.__petrinet_Petrinet2

    @petrinet_Petrinet2.setter
    def petrinet_Petrinet2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Petrinet__petrinet_Petrinet2", None)
        self.__petrinet_Petrinet2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinet_Transition"):
                    opp_val = getattr(item, "petrinet_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_Transition"):
                    opp_val = getattr(item, "petrinet_Transition", None)
                    
                    setattr(item, "petrinet_Transition", self)
                    
