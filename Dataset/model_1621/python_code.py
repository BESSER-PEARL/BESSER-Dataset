from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class petrinetv1_Transition:

    def __init__(self, name: str, petrinetv1_Transition4: set["petrinetv1_Place"] = None, petrinetv1_Transition: "petrinetv1_Net" = None, petrinetv1_Transition7: set["petrinetv1_Place"] = None):
        self.name = name
        self.petrinetv1_Transition4 = petrinetv1_Transition4 if petrinetv1_Transition4 is not None else set()
        self.petrinetv1_Transition = petrinetv1_Transition
        self.petrinetv1_Transition7 = petrinetv1_Transition7 if petrinetv1_Transition7 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petrinetv1_Transition(self):
        return self.__petrinetv1_Transition

    @petrinetv1_Transition.setter
    def petrinetv1_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetv1_Transition__petrinetv1_Transition", None)
        self.__petrinetv1_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinetv1_Net2"):
                opp_val = getattr(old_value, "petrinetv1_Net2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinetv1_Net2"):
                opp_val = getattr(value, "petrinetv1_Net2", None)
                if opp_val is None:
                    setattr(value, "petrinetv1_Net2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinetv1_Transition4(self):
        return self.__petrinetv1_Transition4

    @petrinetv1_Transition4.setter
    def petrinetv1_Transition4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetv1_Transition__petrinetv1_Transition4", None)
        self.__petrinetv1_Transition4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinetv1_Place5"):
                    opp_val = getattr(item, "petrinetv1_Place5", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinetv1_Place5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinetv1_Place5"):
                    opp_val = getattr(item, "petrinetv1_Place5", None)
                    
                    setattr(item, "petrinetv1_Place5", self)
                    

    @property
    def petrinetv1_Transition7(self):
        return self.__petrinetv1_Transition7

    @petrinetv1_Transition7.setter
    def petrinetv1_Transition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetv1_Transition__petrinetv1_Transition7", None)
        self.__petrinetv1_Transition7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinetv1_Place8"):
                    opp_val = getattr(item, "petrinetv1_Place8", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinetv1_Place8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinetv1_Place8"):
                    opp_val = getattr(item, "petrinetv1_Place8", None)
                    
                    setattr(item, "petrinetv1_Place8", self)
                    

class petrinetv1_Place:

    def __init__(self, name: str, initialTokens: int, tokens: int, petrinetv1_Place: "petrinetv1_Net" = None, petrinetv1_Place5: "petrinetv1_Transition" = None, petrinetv1_Place8: "petrinetv1_Transition" = None):
        self.name = name
        self.initialTokens = initialTokens
        self.tokens = tokens
        self.petrinetv1_Place = petrinetv1_Place
        self.petrinetv1_Place5 = petrinetv1_Place5
        self.petrinetv1_Place8 = petrinetv1_Place8
        
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
    def tokens(self) -> int:
        return self.__tokens

    @tokens.setter
    def tokens(self, tokens: int):
        self.__tokens = tokens

    @property
    def petrinetv1_Place8(self):
        return self.__petrinetv1_Place8

    @petrinetv1_Place8.setter
    def petrinetv1_Place8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetv1_Place__petrinetv1_Place8", None)
        self.__petrinetv1_Place8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinetv1_Transition7"):
                opp_val = getattr(old_value, "petrinetv1_Transition7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinetv1_Transition7"):
                opp_val = getattr(value, "petrinetv1_Transition7", None)
                if opp_val is None:
                    setattr(value, "petrinetv1_Transition7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinetv1_Place5(self):
        return self.__petrinetv1_Place5

    @petrinetv1_Place5.setter
    def petrinetv1_Place5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetv1_Place__petrinetv1_Place5", None)
        self.__petrinetv1_Place5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinetv1_Transition4"):
                opp_val = getattr(old_value, "petrinetv1_Transition4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinetv1_Transition4"):
                opp_val = getattr(value, "petrinetv1_Transition4", None)
                if opp_val is None:
                    setattr(value, "petrinetv1_Transition4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinetv1_Place(self):
        return self.__petrinetv1_Place

    @petrinetv1_Place.setter
    def petrinetv1_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetv1_Place__petrinetv1_Place", None)
        self.__petrinetv1_Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinetv1_Net"):
                opp_val = getattr(old_value, "petrinetv1_Net", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinetv1_Net"):
                opp_val = getattr(value, "petrinetv1_Net", None)
                if opp_val is None:
                    setattr(value, "petrinetv1_Net", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class petrinetv1_Net:

    pass