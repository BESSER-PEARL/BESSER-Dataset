from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class PetriNet_Place:

    def __init__(self, name: str, PetriNet_Place: "PetriNet_PetriNet" = None, PetriNet_Place4: set["PetriNet_Token"] = None, PetriNet_Place7: "PetriNet_Transition" = None, PetriNet_Place10: "PetriNet_Transition" = None):
        self.name = name
        self.PetriNet_Place = PetriNet_Place
        self.PetriNet_Place4 = PetriNet_Place4 if PetriNet_Place4 is not None else set()
        self.PetriNet_Place7 = PetriNet_Place7
        self.PetriNet_Place10 = PetriNet_Place10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PetriNet_Place4(self):
        return self.__PetriNet_Place4

    @PetriNet_Place4.setter
    def PetriNet_Place4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Place__PetriNet_Place4", None)
        self.__PetriNet_Place4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNet_Token"):
                    opp_val = getattr(item, "PetriNet_Token", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNet_Token", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNet_Token"):
                    opp_val = getattr(item, "PetriNet_Token", None)
                    
                    setattr(item, "PetriNet_Token", self)
                    

    @property
    def PetriNet_Place7(self):
        return self.__PetriNet_Place7

    @PetriNet_Place7.setter
    def PetriNet_Place7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Place__PetriNet_Place7", None)
        self.__PetriNet_Place7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet_Transition6"):
                opp_val = getattr(old_value, "PetriNet_Transition6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet_Transition6"):
                opp_val = getattr(value, "PetriNet_Transition6", None)
                if opp_val is None:
                    setattr(value, "PetriNet_Transition6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PetriNet_Place(self):
        return self.__PetriNet_Place

    @PetriNet_Place.setter
    def PetriNet_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Place__PetriNet_Place", None)
        self.__PetriNet_Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet_PetriNet2"):
                opp_val = getattr(old_value, "PetriNet_PetriNet2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet_PetriNet2"):
                opp_val = getattr(value, "PetriNet_PetriNet2", None)
                if opp_val is None:
                    setattr(value, "PetriNet_PetriNet2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PetriNet_Place10(self):
        return self.__PetriNet_Place10

    @PetriNet_Place10.setter
    def PetriNet_Place10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Place__PetriNet_Place10", None)
        self.__PetriNet_Place10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet_Transition9"):
                opp_val = getattr(old_value, "PetriNet_Transition9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet_Transition9"):
                opp_val = getattr(value, "PetriNet_Transition9", None)
                if opp_val is None:
                    setattr(value, "PetriNet_Transition9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PetriNet_Transition:

    def __init__(self, name: str, PetriNet_Transition: "PetriNet_PetriNet" = None, PetriNet_Transition6: set["PetriNet_Place"] = None, PetriNet_Transition9: set["PetriNet_Place"] = None):
        self.name = name
        self.PetriNet_Transition = PetriNet_Transition
        self.PetriNet_Transition6 = PetriNet_Transition6 if PetriNet_Transition6 is not None else set()
        self.PetriNet_Transition9 = PetriNet_Transition9 if PetriNet_Transition9 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PetriNet_Transition9(self):
        return self.__PetriNet_Transition9

    @PetriNet_Transition9.setter
    def PetriNet_Transition9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Transition__PetriNet_Transition9", None)
        self.__PetriNet_Transition9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNet_Place10"):
                    opp_val = getattr(item, "PetriNet_Place10", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNet_Place10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNet_Place10"):
                    opp_val = getattr(item, "PetriNet_Place10", None)
                    
                    setattr(item, "PetriNet_Place10", self)
                    

    @property
    def PetriNet_Transition(self):
        return self.__PetriNet_Transition

    @PetriNet_Transition.setter
    def PetriNet_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Transition__PetriNet_Transition", None)
        self.__PetriNet_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet_PetriNet"):
                opp_val = getattr(old_value, "PetriNet_PetriNet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet_PetriNet"):
                opp_val = getattr(value, "PetriNet_PetriNet", None)
                if opp_val is None:
                    setattr(value, "PetriNet_PetriNet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PetriNet_Transition6(self):
        return self.__PetriNet_Transition6

    @PetriNet_Transition6.setter
    def PetriNet_Transition6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Transition__PetriNet_Transition6", None)
        self.__PetriNet_Transition6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNet_Place7"):
                    opp_val = getattr(item, "PetriNet_Place7", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNet_Place7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNet_Place7"):
                    opp_val = getattr(item, "PetriNet_Place7", None)
                    
                    setattr(item, "PetriNet_Place7", self)
                    

class PetriNet_PetriNet:

    pass
class PetriNet_Token:

    pass