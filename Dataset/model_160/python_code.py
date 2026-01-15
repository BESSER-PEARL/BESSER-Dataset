from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Petrinet_Transition:

    def __init__(self, name: str, Petrinet_Transition: "Petrinet_PetriNet" = None, Petrinet_Transition5: "Petrinet_Place" = None, Petrinet_Transition7: set["Petrinet_Place"] = None):
        self.name = name
        self.Petrinet_Transition = Petrinet_Transition
        self.Petrinet_Transition5 = Petrinet_Transition5
        self.Petrinet_Transition7 = Petrinet_Transition7 if Petrinet_Transition7 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Petrinet_Transition5(self):
        return self.__Petrinet_Transition5

    @Petrinet_Transition5.setter
    def Petrinet_Transition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Petrinet_Transition__Petrinet_Transition5", None)
        self.__Petrinet_Transition5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Petrinet_Place4"):
                opp_val = getattr(old_value, "Petrinet_Place4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Petrinet_Place4"):
                opp_val = getattr(value, "Petrinet_Place4", None)
                if opp_val is None:
                    setattr(value, "Petrinet_Place4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Petrinet_Transition7(self):
        return self.__Petrinet_Transition7

    @Petrinet_Transition7.setter
    def Petrinet_Transition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Petrinet_Transition__Petrinet_Transition7", None)
        self.__Petrinet_Transition7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Petrinet_Place8"):
                    opp_val = getattr(item, "Petrinet_Place8", None)
                    
                    if opp_val == self:
                        setattr(item, "Petrinet_Place8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Petrinet_Place8"):
                    opp_val = getattr(item, "Petrinet_Place8", None)
                    
                    setattr(item, "Petrinet_Place8", self)
                    

    @property
    def Petrinet_Transition(self):
        return self.__Petrinet_Transition

    @Petrinet_Transition.setter
    def Petrinet_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Petrinet_Transition__Petrinet_Transition", None)
        self.__Petrinet_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Petrinet_PetriNet2"):
                opp_val = getattr(old_value, "Petrinet_PetriNet2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Petrinet_PetriNet2"):
                opp_val = getattr(value, "Petrinet_PetriNet2", None)
                if opp_val is None:
                    setattr(value, "Petrinet_PetriNet2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Petrinet_Place:

    def __init__(self, name: str, tokens: int, Petrinet_Place: "Petrinet_PetriNet" = None, Petrinet_Place4: set["Petrinet_Transition"] = None, Petrinet_Place8: "Petrinet_Transition" = None):
        self.name = name
        self.tokens = tokens
        self.Petrinet_Place = Petrinet_Place
        self.Petrinet_Place4 = Petrinet_Place4 if Petrinet_Place4 is not None else set()
        self.Petrinet_Place8 = Petrinet_Place8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tokens(self) -> int:
        return self.__tokens

    @tokens.setter
    def tokens(self, tokens: int):
        self.__tokens = tokens

    @property
    def Petrinet_Place8(self):
        return self.__Petrinet_Place8

    @Petrinet_Place8.setter
    def Petrinet_Place8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Petrinet_Place__Petrinet_Place8", None)
        self.__Petrinet_Place8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Petrinet_Transition7"):
                opp_val = getattr(old_value, "Petrinet_Transition7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Petrinet_Transition7"):
                opp_val = getattr(value, "Petrinet_Transition7", None)
                if opp_val is None:
                    setattr(value, "Petrinet_Transition7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Petrinet_Place4(self):
        return self.__Petrinet_Place4

    @Petrinet_Place4.setter
    def Petrinet_Place4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Petrinet_Place__Petrinet_Place4", None)
        self.__Petrinet_Place4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Petrinet_Transition5"):
                    opp_val = getattr(item, "Petrinet_Transition5", None)
                    
                    if opp_val == self:
                        setattr(item, "Petrinet_Transition5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Petrinet_Transition5"):
                    opp_val = getattr(item, "Petrinet_Transition5", None)
                    
                    setattr(item, "Petrinet_Transition5", self)
                    

    @property
    def Petrinet_Place(self):
        return self.__Petrinet_Place

    @Petrinet_Place.setter
    def Petrinet_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Petrinet_Place__Petrinet_Place", None)
        self.__Petrinet_Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Petrinet_PetriNet"):
                opp_val = getattr(old_value, "Petrinet_PetriNet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Petrinet_PetriNet"):
                opp_val = getattr(value, "Petrinet_PetriNet", None)
                if opp_val is None:
                    setattr(value, "Petrinet_PetriNet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Petrinet_PetriNet:

    pass