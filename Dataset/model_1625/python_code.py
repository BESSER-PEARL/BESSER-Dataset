from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class petrinetv3_Token:

    pass
class petrinetv3_Transition:

    def __init__(self, clock: int, name: str, tmin: int, tmax: int, petrinetv3_Transition: set["petrinetv3_Place"] = None, Transition: "petrinetv3_Net" = None, transitions: "petrinetv3_Net" = None, petrinetv3_Transition5: set["petrinetv3_Place"] = None):
        self.clock = clock
        self.name = name
        self.tmin = tmin
        self.tmax = tmax
        self.petrinetv3_Transition = petrinetv3_Transition if petrinetv3_Transition is not None else set()
        self.Transition = Transition
        self.transitions = transitions
        self.petrinetv3_Transition5 = petrinetv3_Transition5 if petrinetv3_Transition5 is not None else set()
        
    @property
    def tmax(self) -> int:
        return self.__tmax

    @tmax.setter
    def tmax(self, tmax: int):
        self.__tmax = tmax

    @property
    def clock(self) -> int:
        return self.__clock

    @clock.setter
    def clock(self, clock: int):
        self.__clock = clock

    @property
    def tmin(self) -> int:
        return self.__tmin

    @tmin.setter
    def tmin(self, tmin: int):
        self.__tmin = tmin

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petrinetv3_Transition5(self):
        return self.__petrinetv3_Transition5

    @petrinetv3_Transition5.setter
    def petrinetv3_Transition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetv3_Transition__petrinetv3_Transition5", None)
        self.__petrinetv3_Transition5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinetv3_Place6"):
                    opp_val = getattr(item, "petrinetv3_Place6", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinetv3_Place6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinetv3_Place6"):
                    opp_val = getattr(item, "petrinetv3_Place6", None)
                    
                    setattr(item, "petrinetv3_Place6", self)
                    

    @property
    def transitions(self):
        return self.__transitions

    @transitions.setter
    def transitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetv3_Transition__transitions", None)
        self.__transitions = value
        
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
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetv3_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parentNet"):
                opp_val = getattr(old_value, "parentNet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentNet"):
                opp_val = getattr(value, "parentNet", None)
                if opp_val is None:
                    setattr(value, "parentNet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinetv3_Transition(self):
        return self.__petrinetv3_Transition

    @petrinetv3_Transition.setter
    def petrinetv3_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetv3_Transition__petrinetv3_Transition", None)
        self.__petrinetv3_Transition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinetv3_Place3"):
                    opp_val = getattr(item, "petrinetv3_Place3", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinetv3_Place3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinetv3_Place3"):
                    opp_val = getattr(item, "petrinetv3_Place3", None)
                    
                    setattr(item, "petrinetv3_Place3", self)
                    

class petrinetv3_Place:

    def __init__(self, name: str, initialTokens: int, petrinetv3_Place3: "petrinetv3_Transition" = None, petrinetv3_Place: "petrinetv3_Net" = None, petrinetv3_Place6: "petrinetv3_Transition" = None, petrinetv3_Place9: set["petrinetv3_Token"] = None):
        self.name = name
        self.initialTokens = initialTokens
        self.petrinetv3_Place3 = petrinetv3_Place3
        self.petrinetv3_Place = petrinetv3_Place
        self.petrinetv3_Place6 = petrinetv3_Place6
        self.petrinetv3_Place9 = petrinetv3_Place9 if petrinetv3_Place9 is not None else set()
        
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
    def petrinetv3_Place6(self):
        return self.__petrinetv3_Place6

    @petrinetv3_Place6.setter
    def petrinetv3_Place6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetv3_Place__petrinetv3_Place6", None)
        self.__petrinetv3_Place6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinetv3_Transition5"):
                opp_val = getattr(old_value, "petrinetv3_Transition5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinetv3_Transition5"):
                opp_val = getattr(value, "petrinetv3_Transition5", None)
                if opp_val is None:
                    setattr(value, "petrinetv3_Transition5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinetv3_Place9(self):
        return self.__petrinetv3_Place9

    @petrinetv3_Place9.setter
    def petrinetv3_Place9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetv3_Place__petrinetv3_Place9", None)
        self.__petrinetv3_Place9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinetv3_Token"):
                    opp_val = getattr(item, "petrinetv3_Token", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinetv3_Token", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinetv3_Token"):
                    opp_val = getattr(item, "petrinetv3_Token", None)
                    
                    setattr(item, "petrinetv3_Token", self)
                    

    @property
    def petrinetv3_Place(self):
        return self.__petrinetv3_Place

    @petrinetv3_Place.setter
    def petrinetv3_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetv3_Place__petrinetv3_Place", None)
        self.__petrinetv3_Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinetv3_Net"):
                opp_val = getattr(old_value, "petrinetv3_Net", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinetv3_Net"):
                opp_val = getattr(value, "petrinetv3_Net", None)
                if opp_val is None:
                    setattr(value, "petrinetv3_Net", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinetv3_Place3(self):
        return self.__petrinetv3_Place3

    @petrinetv3_Place3.setter
    def petrinetv3_Place3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetv3_Place__petrinetv3_Place3", None)
        self.__petrinetv3_Place3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinetv3_Transition"):
                opp_val = getattr(old_value, "petrinetv3_Transition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinetv3_Transition"):
                opp_val = getattr(value, "petrinetv3_Transition", None)
                if opp_val is None:
                    setattr(value, "petrinetv3_Transition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class petrinetv3_Net:

    pass