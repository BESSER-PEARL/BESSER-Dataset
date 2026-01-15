from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Arc:

    pass
class petrinet_Transition:

    def __init__(self, name: str, petrinet_Transition: "petrinet_Petrinet" = None, src13: set["petrinet_TPArc"] = None, Transition: "petrinet_PTArc" = None, trg10: set["petrinet_PTArc"] = None, Transition19: "petrinet_TPArc" = None):
        self.name = name
        self.petrinet_Transition = petrinet_Transition
        self.src13 = src13 if src13 is not None else set()
        self.Transition = Transition
        self.trg10 = trg10 if trg10 is not None else set()
        self.Transition19 = Transition19
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def Transition19(self):
        return self.__Transition19

    @Transition19.setter
    def Transition19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Transition__Transition19", None)
        self.__Transition19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "out18"):
                opp_val = getattr(old_value, "out18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "out18"):
                opp_val = getattr(value, "out18", None)
                if opp_val is None:
                    setattr(value, "out18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def trg10(self):
        return self.__trg10

    @trg10.setter
    def trg10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Transition__trg10", None)
        self.__trg10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PTArc11"):
                    opp_val = getattr(item, "PTArc11", None)
                    
                    if opp_val == self:
                        setattr(item, "PTArc11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PTArc11"):
                    opp_val = getattr(item, "PTArc11", None)
                    
                    setattr(item, "PTArc11", self)
                    

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "in"):
                opp_val = getattr(old_value, "in", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "in"):
                opp_val = getattr(value, "in", None)
                if opp_val is None:
                    setattr(value, "in", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def src13(self):
        return self.__src13

    @src13.setter
    def src13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Transition__src13", None)
        self.__src13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TPArc14"):
                    opp_val = getattr(item, "TPArc14", None)
                    
                    if opp_val == self:
                        setattr(item, "TPArc14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TPArc14"):
                    opp_val = getattr(item, "TPArc14", None)
                    
                    setattr(item, "TPArc14", self)
                    

class petrinet_Place:

    def __init__(self, name: str, petrinet_Place6: set["petrinet_Token"] = None, src: set["petrinet_PTArc"] = None, trg: set["petrinet_TPArc"] = None, petrinet_Place: "petrinet_Petrinet" = None, Place: "petrinet_PTArc" = None, Place22: "petrinet_TPArc" = None):
        self.name = name
        self.petrinet_Place6 = petrinet_Place6 if petrinet_Place6 is not None else set()
        self.src = src if src is not None else set()
        self.trg = trg if trg is not None else set()
        self.petrinet_Place = petrinet_Place
        self.Place = Place
        self.Place22 = Place22
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def trg(self):
        return self.__trg

    @trg.setter
    def trg(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__trg", None)
        self.__trg = value if value is not None else set()
        
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
    def src(self):
        return self.__src

    @src.setter
    def src(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__src", None)
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
    def Place22(self):
        return self.__Place22

    @Place22.setter
    def Place22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__Place22", None)
        self.__Place22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "in21"):
                opp_val = getattr(old_value, "in21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "in21"):
                opp_val = getattr(value, "in21", None)
                if opp_val is None:
                    setattr(value, "in21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Place(self):
        return self.__Place

    @Place.setter
    def Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__Place", None)
        self.__Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "out"):
                opp_val = getattr(old_value, "out", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "out"):
                opp_val = getattr(value, "out", None)
                if opp_val is None:
                    setattr(value, "out", set([self]))
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
                    

class petrinet_TPArc(Arc):

    pass
class petrinet_PTArc(Arc):

    pass
class petrinet_Token:

    pass
class petrinet_Arc:

    def __init__(self, weight: int, petrinet_Arc: "petrinet_Petrinet" = None):
        self.weight = weight
        self.petrinet_Arc = petrinet_Arc
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

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

class petrinet_Petrinet:

    def __init__(self, name: str, petrinet_Petrinet2: set["petrinet_Transition"] = None, petrinet_Petrinet4: set["petrinet_Arc"] = None, petrinet_Petrinet: set["petrinet_Place"] = None):
        self.name = name
        self.petrinet_Petrinet2 = petrinet_Petrinet2 if petrinet_Petrinet2 is not None else set()
        self.petrinet_Petrinet4 = petrinet_Petrinet4 if petrinet_Petrinet4 is not None else set()
        self.petrinet_Petrinet = petrinet_Petrinet if petrinet_Petrinet is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
                    
