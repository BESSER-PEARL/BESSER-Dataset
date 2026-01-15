from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Arc:

    pass
class petriNetz_TPArc(Arc):

    pass
class petriNetz_Place:

    def __init__(self, name: str, petriNetz_Place6: set["petriNetz_Token"] = None, petriNetz_Place8: set["petriNetz_PTArc"] = None, petriNetz_Place: "petriNetz_Petrinet" = None, petriNetz_Place19: "petriNetz_PTArc" = None, petriNetz_Place10: set["petriNetz_TPArc"] = None, petriNetz_Place25: "petriNetz_TPArc" = None):
        self.name = name
        self.petriNetz_Place6 = petriNetz_Place6 if petriNetz_Place6 is not None else set()
        self.petriNetz_Place8 = petriNetz_Place8 if petriNetz_Place8 is not None else set()
        self.petriNetz_Place = petriNetz_Place
        self.petriNetz_Place19 = petriNetz_Place19
        self.petriNetz_Place10 = petriNetz_Place10 if petriNetz_Place10 is not None else set()
        self.petriNetz_Place25 = petriNetz_Place25
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petriNetz_Place(self):
        return self.__petriNetz_Place

    @petriNetz_Place.setter
    def petriNetz_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNetz_Place__petriNetz_Place", None)
        self.__petriNetz_Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petriNetz_Petrinet"):
                opp_val = getattr(old_value, "petriNetz_Petrinet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petriNetz_Petrinet"):
                opp_val = getattr(value, "petriNetz_Petrinet", None)
                if opp_val is None:
                    setattr(value, "petriNetz_Petrinet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petriNetz_Place8(self):
        return self.__petriNetz_Place8

    @petriNetz_Place8.setter
    def petriNetz_Place8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNetz_Place__petriNetz_Place8", None)
        self.__petriNetz_Place8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petriNetz_PTArc"):
                    opp_val = getattr(item, "petriNetz_PTArc", None)
                    
                    if opp_val == self:
                        setattr(item, "petriNetz_PTArc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petriNetz_PTArc"):
                    opp_val = getattr(item, "petriNetz_PTArc", None)
                    
                    setattr(item, "petriNetz_PTArc", self)
                    

    @property
    def petriNetz_Place10(self):
        return self.__petriNetz_Place10

    @petriNetz_Place10.setter
    def petriNetz_Place10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNetz_Place__petriNetz_Place10", None)
        self.__petriNetz_Place10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petriNetz_TPArc"):
                    opp_val = getattr(item, "petriNetz_TPArc", None)
                    
                    if opp_val == self:
                        setattr(item, "petriNetz_TPArc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petriNetz_TPArc"):
                    opp_val = getattr(item, "petriNetz_TPArc", None)
                    
                    setattr(item, "petriNetz_TPArc", self)
                    

    @property
    def petriNetz_Place6(self):
        return self.__petriNetz_Place6

    @petriNetz_Place6.setter
    def petriNetz_Place6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNetz_Place__petriNetz_Place6", None)
        self.__petriNetz_Place6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petriNetz_Token"):
                    opp_val = getattr(item, "petriNetz_Token", None)
                    
                    if opp_val == self:
                        setattr(item, "petriNetz_Token", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petriNetz_Token"):
                    opp_val = getattr(item, "petriNetz_Token", None)
                    
                    setattr(item, "petriNetz_Token", self)
                    

    @property
    def petriNetz_Place19(self):
        return self.__petriNetz_Place19

    @petriNetz_Place19.setter
    def petriNetz_Place19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNetz_Place__petriNetz_Place19", None)
        self.__petriNetz_Place19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petriNetz_PTArc18"):
                opp_val = getattr(old_value, "petriNetz_PTArc18", None)
                if opp_val == self:
                    setattr(old_value, "petriNetz_PTArc18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petriNetz_PTArc18"):
                opp_val = getattr(value, "petriNetz_PTArc18", None)
                setattr(value, "petriNetz_PTArc18", self)

    @property
    def petriNetz_Place25(self):
        return self.__petriNetz_Place25

    @petriNetz_Place25.setter
    def petriNetz_Place25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNetz_Place__petriNetz_Place25", None)
        self.__petriNetz_Place25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petriNetz_TPArc24"):
                opp_val = getattr(old_value, "petriNetz_TPArc24", None)
                if opp_val == self:
                    setattr(old_value, "petriNetz_TPArc24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petriNetz_TPArc24"):
                opp_val = getattr(value, "petriNetz_TPArc24", None)
                setattr(value, "petriNetz_TPArc24", self)

class petriNetz_PTArc(Arc):

    pass
class petriNetz_Token:

    pass
class petriNetz_Arc:

    def __init__(self, weight: int, petriNetz_Arc: "petriNetz_Petrinet" = None):
        self.weight = weight
        self.petriNetz_Arc = petriNetz_Arc
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def petriNetz_Arc(self):
        return self.__petriNetz_Arc

    @petriNetz_Arc.setter
    def petriNetz_Arc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNetz_Arc__petriNetz_Arc", None)
        self.__petriNetz_Arc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petriNetz_Petrinet4"):
                opp_val = getattr(old_value, "petriNetz_Petrinet4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petriNetz_Petrinet4"):
                opp_val = getattr(value, "petriNetz_Petrinet4", None)
                if opp_val is None:
                    setattr(value, "petriNetz_Petrinet4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class petriNetz_Transition:

    def __init__(self, name: str, petriNetz_Transition: "petriNetz_Petrinet" = None, petriNetz_Transition12: set["petriNetz_PTArc"] = None, petriNetz_Transition15: set["petriNetz_TPArc"] = None, petriNetz_Transition22: "petriNetz_PTArc" = None, petriNetz_Transition28: "petriNetz_TPArc" = None):
        self.name = name
        self.petriNetz_Transition = petriNetz_Transition
        self.petriNetz_Transition12 = petriNetz_Transition12 if petriNetz_Transition12 is not None else set()
        self.petriNetz_Transition15 = petriNetz_Transition15 if petriNetz_Transition15 is not None else set()
        self.petriNetz_Transition22 = petriNetz_Transition22
        self.petriNetz_Transition28 = petriNetz_Transition28
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petriNetz_Transition22(self):
        return self.__petriNetz_Transition22

    @petriNetz_Transition22.setter
    def petriNetz_Transition22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNetz_Transition__petriNetz_Transition22", None)
        self.__petriNetz_Transition22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petriNetz_PTArc21"):
                opp_val = getattr(old_value, "petriNetz_PTArc21", None)
                if opp_val == self:
                    setattr(old_value, "petriNetz_PTArc21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petriNetz_PTArc21"):
                opp_val = getattr(value, "petriNetz_PTArc21", None)
                setattr(value, "petriNetz_PTArc21", self)

    @property
    def petriNetz_Transition(self):
        return self.__petriNetz_Transition

    @petriNetz_Transition.setter
    def petriNetz_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNetz_Transition__petriNetz_Transition", None)
        self.__petriNetz_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petriNetz_Petrinet2"):
                opp_val = getattr(old_value, "petriNetz_Petrinet2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petriNetz_Petrinet2"):
                opp_val = getattr(value, "petriNetz_Petrinet2", None)
                if opp_val is None:
                    setattr(value, "petriNetz_Petrinet2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petriNetz_Transition15(self):
        return self.__petriNetz_Transition15

    @petriNetz_Transition15.setter
    def petriNetz_Transition15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNetz_Transition__petriNetz_Transition15", None)
        self.__petriNetz_Transition15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petriNetz_TPArc16"):
                    opp_val = getattr(item, "petriNetz_TPArc16", None)
                    
                    if opp_val == self:
                        setattr(item, "petriNetz_TPArc16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petriNetz_TPArc16"):
                    opp_val = getattr(item, "petriNetz_TPArc16", None)
                    
                    setattr(item, "petriNetz_TPArc16", self)
                    

    @property
    def petriNetz_Transition28(self):
        return self.__petriNetz_Transition28

    @petriNetz_Transition28.setter
    def petriNetz_Transition28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNetz_Transition__petriNetz_Transition28", None)
        self.__petriNetz_Transition28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petriNetz_TPArc27"):
                opp_val = getattr(old_value, "petriNetz_TPArc27", None)
                if opp_val == self:
                    setattr(old_value, "petriNetz_TPArc27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petriNetz_TPArc27"):
                opp_val = getattr(value, "petriNetz_TPArc27", None)
                setattr(value, "petriNetz_TPArc27", self)

    @property
    def petriNetz_Transition12(self):
        return self.__petriNetz_Transition12

    @petriNetz_Transition12.setter
    def petriNetz_Transition12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNetz_Transition__petriNetz_Transition12", None)
        self.__petriNetz_Transition12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petriNetz_PTArc13"):
                    opp_val = getattr(item, "petriNetz_PTArc13", None)
                    
                    if opp_val == self:
                        setattr(item, "petriNetz_PTArc13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petriNetz_PTArc13"):
                    opp_val = getattr(item, "petriNetz_PTArc13", None)
                    
                    setattr(item, "petriNetz_PTArc13", self)
                    

class petriNetz_Petrinet:

    def __init__(self, name: str, petriNetz_Petrinet2: set["petriNetz_Transition"] = None, petriNetz_Petrinet4: set["petriNetz_Arc"] = None, petriNetz_Petrinet: set["petriNetz_Place"] = None):
        self.name = name
        self.petriNetz_Petrinet2 = petriNetz_Petrinet2 if petriNetz_Petrinet2 is not None else set()
        self.petriNetz_Petrinet4 = petriNetz_Petrinet4 if petriNetz_Petrinet4 is not None else set()
        self.petriNetz_Petrinet = petriNetz_Petrinet if petriNetz_Petrinet is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petriNetz_Petrinet2(self):
        return self.__petriNetz_Petrinet2

    @petriNetz_Petrinet2.setter
    def petriNetz_Petrinet2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNetz_Petrinet__petriNetz_Petrinet2", None)
        self.__petriNetz_Petrinet2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petriNetz_Transition"):
                    opp_val = getattr(item, "petriNetz_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "petriNetz_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petriNetz_Transition"):
                    opp_val = getattr(item, "petriNetz_Transition", None)
                    
                    setattr(item, "petriNetz_Transition", self)
                    

    @property
    def petriNetz_Petrinet4(self):
        return self.__petriNetz_Petrinet4

    @petriNetz_Petrinet4.setter
    def petriNetz_Petrinet4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNetz_Petrinet__petriNetz_Petrinet4", None)
        self.__petriNetz_Petrinet4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petriNetz_Arc"):
                    opp_val = getattr(item, "petriNetz_Arc", None)
                    
                    if opp_val == self:
                        setattr(item, "petriNetz_Arc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petriNetz_Arc"):
                    opp_val = getattr(item, "petriNetz_Arc", None)
                    
                    setattr(item, "petriNetz_Arc", self)
                    

    @property
    def petriNetz_Petrinet(self):
        return self.__petriNetz_Petrinet

    @petriNetz_Petrinet.setter
    def petriNetz_Petrinet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNetz_Petrinet__petriNetz_Petrinet", None)
        self.__petriNetz_Petrinet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petriNetz_Place"):
                    opp_val = getattr(item, "petriNetz_Place", None)
                    
                    if opp_val == self:
                        setattr(item, "petriNetz_Place", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petriNetz_Place"):
                    opp_val = getattr(item, "petriNetz_Place", None)
                    
                    setattr(item, "petriNetz_Place", self)
                    
