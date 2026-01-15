from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class petrinetv2_Token:

    pass
class petrinetv2_Transition:

    def __init__(self, name: str, petrinetv2_Transition4: set["petrinetv2_Place"] = None, petrinetv2_Transition7: set["petrinetv2_Place"] = None, petrinetv2_Transition: "petrinetv2_Net" = None):
        self.name = name
        self.petrinetv2_Transition4 = petrinetv2_Transition4 if petrinetv2_Transition4 is not None else set()
        self.petrinetv2_Transition7 = petrinetv2_Transition7 if petrinetv2_Transition7 is not None else set()
        self.petrinetv2_Transition = petrinetv2_Transition
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petrinetv2_Transition4(self):
        return self.__petrinetv2_Transition4

    @petrinetv2_Transition4.setter
    def petrinetv2_Transition4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetv2_Transition__petrinetv2_Transition4", None)
        self.__petrinetv2_Transition4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinetv2_Place5"):
                    opp_val = getattr(item, "petrinetv2_Place5", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinetv2_Place5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinetv2_Place5"):
                    opp_val = getattr(item, "petrinetv2_Place5", None)
                    
                    setattr(item, "petrinetv2_Place5", self)
                    

    @property
    def petrinetv2_Transition(self):
        return self.__petrinetv2_Transition

    @petrinetv2_Transition.setter
    def petrinetv2_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetv2_Transition__petrinetv2_Transition", None)
        self.__petrinetv2_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinetv2_Net2"):
                opp_val = getattr(old_value, "petrinetv2_Net2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinetv2_Net2"):
                opp_val = getattr(value, "petrinetv2_Net2", None)
                if opp_val is None:
                    setattr(value, "petrinetv2_Net2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinetv2_Transition7(self):
        return self.__petrinetv2_Transition7

    @petrinetv2_Transition7.setter
    def petrinetv2_Transition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetv2_Transition__petrinetv2_Transition7", None)
        self.__petrinetv2_Transition7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinetv2_Place8"):
                    opp_val = getattr(item, "petrinetv2_Place8", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinetv2_Place8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinetv2_Place8"):
                    opp_val = getattr(item, "petrinetv2_Place8", None)
                    
                    setattr(item, "petrinetv2_Place8", self)
                    

class petrinetv2_Place:

    def __init__(self, name: str, initialTokens: int, petrinetv2_Place5: "petrinetv2_Transition" = None, petrinetv2_Place8: "petrinetv2_Transition" = None, petrinetv2_Place: "petrinetv2_Net" = None, petrinetv2_Place10: set["petrinetv2_Token"] = None):
        self.name = name
        self.initialTokens = initialTokens
        self.petrinetv2_Place5 = petrinetv2_Place5
        self.petrinetv2_Place8 = petrinetv2_Place8
        self.petrinetv2_Place = petrinetv2_Place
        self.petrinetv2_Place10 = petrinetv2_Place10 if petrinetv2_Place10 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def initialTokens(self) -> int:
        return self.__initialTokens

    @initialTokens.setter
    def initialTokens(self, initialTokens: int):
        self.__initialTokens = initialTokens

    @property
    def petrinetv2_Place10(self):
        return self.__petrinetv2_Place10

    @petrinetv2_Place10.setter
    def petrinetv2_Place10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetv2_Place__petrinetv2_Place10", None)
        self.__petrinetv2_Place10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinetv2_Token"):
                    opp_val = getattr(item, "petrinetv2_Token", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinetv2_Token", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinetv2_Token"):
                    opp_val = getattr(item, "petrinetv2_Token", None)
                    
                    setattr(item, "petrinetv2_Token", self)
                    

    @property
    def petrinetv2_Place8(self):
        return self.__petrinetv2_Place8

    @petrinetv2_Place8.setter
    def petrinetv2_Place8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetv2_Place__petrinetv2_Place8", None)
        self.__petrinetv2_Place8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinetv2_Transition7"):
                opp_val = getattr(old_value, "petrinetv2_Transition7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinetv2_Transition7"):
                opp_val = getattr(value, "petrinetv2_Transition7", None)
                if opp_val is None:
                    setattr(value, "petrinetv2_Transition7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinetv2_Place5(self):
        return self.__petrinetv2_Place5

    @petrinetv2_Place5.setter
    def petrinetv2_Place5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetv2_Place__petrinetv2_Place5", None)
        self.__petrinetv2_Place5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinetv2_Transition4"):
                opp_val = getattr(old_value, "petrinetv2_Transition4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinetv2_Transition4"):
                opp_val = getattr(value, "petrinetv2_Transition4", None)
                if opp_val is None:
                    setattr(value, "petrinetv2_Transition4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinetv2_Place(self):
        return self.__petrinetv2_Place

    @petrinetv2_Place.setter
    def petrinetv2_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetv2_Place__petrinetv2_Place", None)
        self.__petrinetv2_Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinetv2_Net"):
                opp_val = getattr(old_value, "petrinetv2_Net", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinetv2_Net"):
                opp_val = getattr(value, "petrinetv2_Net", None)
                if opp_val is None:
                    setattr(value, "petrinetv2_Net", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class petrinetv2_Net:

    pass