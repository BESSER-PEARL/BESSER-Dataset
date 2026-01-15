from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Arc:

    pass
class petrinet_PTArc(Arc):

    pass
class petrinet_TPArc(Arc):

    pass
class petrinet_Arc:

    def __init__(self, weight: int):
        self.weight = weight
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

class petrinet_Transition:

    def __init__(self, name: str, petrinet_Transition: "petrinet_PetriNet" = None, source: set["petrinet_TPArc"] = None, petrinet_Transition7: "petrinet_PTArc" = None, Transition: "petrinet_TPArc" = None):
        self.name = name
        self.petrinet_Transition = petrinet_Transition
        self.source = source if source is not None else set()
        self.petrinet_Transition7 = petrinet_Transition7
        self.Transition = Transition
        
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
            if hasattr(old_value, "petrinet_PetriNet2"):
                opp_val = getattr(old_value, "petrinet_PetriNet2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_PetriNet2"):
                opp_val = getattr(value, "petrinet_PetriNet2", None)
                if opp_val is None:
                    setattr(value, "petrinet_PetriNet2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Transition__source", None)
        self.__source = value if value is not None else set()
        
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
    def petrinet_Transition7(self):
        return self.__petrinet_Transition7

    @petrinet_Transition7.setter
    def petrinet_Transition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Transition__petrinet_Transition7", None)
        self.__petrinet_Transition7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_PTArc"):
                opp_val = getattr(old_value, "petrinet_PTArc", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_PTArc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_PTArc"):
                opp_val = getattr(value, "petrinet_PTArc", None)
                setattr(value, "petrinet_PTArc", self)

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
            if hasattr(old_value, "outgoing12"):
                opp_val = getattr(old_value, "outgoing12", None)
                if opp_val == self:
                    setattr(old_value, "outgoing12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoing12"):
                opp_val = getattr(value, "outgoing12", None)
                setattr(value, "outgoing12", self)

class petrinet_Place:

    def __init__(self, name: str, token: int, petrinet_Place: "petrinet_PetriNet" = None, source5: set["petrinet_PTArc"] = None, Place: "petrinet_PTArc" = None, petrinet_Place10: "petrinet_TPArc" = None):
        self.name = name
        self.token = token
        self.petrinet_Place = petrinet_Place
        self.source5 = source5 if source5 is not None else set()
        self.Place = Place
        self.petrinet_Place10 = petrinet_Place10
        
    @property
    def token(self) -> int:
        return self.__token

    @token.setter
    def token(self, token: int):
        self.__token = token

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "petrinet_TPArc"):
                opp_val = getattr(old_value, "petrinet_TPArc", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_TPArc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_TPArc"):
                opp_val = getattr(value, "petrinet_TPArc", None)
                setattr(value, "petrinet_TPArc", self)

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
            if hasattr(old_value, "outgoing"):
                opp_val = getattr(old_value, "outgoing", None)
                if opp_val == self:
                    setattr(old_value, "outgoing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoing"):
                opp_val = getattr(value, "outgoing", None)
                setattr(value, "outgoing", self)

    @property
    def source5(self):
        return self.__source5

    @source5.setter
    def source5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__source5", None)
        self.__source5 = value if value is not None else set()
        
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
    def petrinet_Place(self):
        return self.__petrinet_Place

    @petrinet_Place.setter
    def petrinet_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__petrinet_Place", None)
        self.__petrinet_Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_PetriNet"):
                opp_val = getattr(old_value, "petrinet_PetriNet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_PetriNet"):
                opp_val = getattr(value, "petrinet_PetriNet", None)
                if opp_val is None:
                    setattr(value, "petrinet_PetriNet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class petrinet_PetriNet:

    pass