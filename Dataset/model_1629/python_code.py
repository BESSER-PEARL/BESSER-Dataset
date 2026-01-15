from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class petri_RedPetri:

    pass
class petri_Transition:

    def __init__(self, name: str, petri_Transition: "petri_Place" = None, petri_Transition2: set["petri_Place"] = None, petri_Transition8: "petri_RedPetri" = None):
        self.name = name
        self.petri_Transition = petri_Transition
        self.petri_Transition2 = petri_Transition2 if petri_Transition2 is not None else set()
        self.petri_Transition8 = petri_Transition8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petri_Transition(self):
        return self.__petri_Transition

    @petri_Transition.setter
    def petri_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petri_Transition__petri_Transition", None)
        self.__petri_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petri_Place"):
                opp_val = getattr(old_value, "petri_Place", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petri_Place"):
                opp_val = getattr(value, "petri_Place", None)
                if opp_val is None:
                    setattr(value, "petri_Place", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petri_Transition2(self):
        return self.__petri_Transition2

    @petri_Transition2.setter
    def petri_Transition2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petri_Transition__petri_Transition2", None)
        self.__petri_Transition2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petri_Place3"):
                    opp_val = getattr(item, "petri_Place3", None)
                    
                    if opp_val == self:
                        setattr(item, "petri_Place3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petri_Place3"):
                    opp_val = getattr(item, "petri_Place3", None)
                    
                    setattr(item, "petri_Place3", self)
                    

    @property
    def petri_Transition8(self):
        return self.__petri_Transition8

    @petri_Transition8.setter
    def petri_Transition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petri_Transition__petri_Transition8", None)
        self.__petri_Transition8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petri_RedPetri7"):
                opp_val = getattr(old_value, "petri_RedPetri7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petri_RedPetri7"):
                opp_val = getattr(value, "petri_RedPetri7", None)
                if opp_val is None:
                    setattr(value, "petri_RedPetri7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class petri_Place:

    def __init__(self, name: str, tokens: int, petri_Place: set["petri_Transition"] = None, petri_Place3: "petri_Transition" = None, petri_Place5: "petri_RedPetri" = None):
        self.name = name
        self.tokens = tokens
        self.petri_Place = petri_Place if petri_Place is not None else set()
        self.petri_Place3 = petri_Place3
        self.petri_Place5 = petri_Place5
        
    @property
    def tokens(self) -> int:
        return self.__tokens

    @tokens.setter
    def tokens(self, tokens: int):
        self.__tokens = tokens

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petri_Place3(self):
        return self.__petri_Place3

    @petri_Place3.setter
    def petri_Place3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petri_Place__petri_Place3", None)
        self.__petri_Place3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petri_Transition2"):
                opp_val = getattr(old_value, "petri_Transition2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petri_Transition2"):
                opp_val = getattr(value, "petri_Transition2", None)
                if opp_val is None:
                    setattr(value, "petri_Transition2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petri_Place5(self):
        return self.__petri_Place5

    @petri_Place5.setter
    def petri_Place5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petri_Place__petri_Place5", None)
        self.__petri_Place5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petri_RedPetri"):
                opp_val = getattr(old_value, "petri_RedPetri", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petri_RedPetri"):
                opp_val = getattr(value, "petri_RedPetri", None)
                if opp_val is None:
                    setattr(value, "petri_RedPetri", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petri_Place(self):
        return self.__petri_Place

    @petri_Place.setter
    def petri_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petri_Place__petri_Place", None)
        self.__petri_Place = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petri_Transition"):
                    opp_val = getattr(item, "petri_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "petri_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petri_Transition"):
                    opp_val = getattr(item, "petri_Transition", None)
                    
                    setattr(item, "petri_Transition", self)
                    
