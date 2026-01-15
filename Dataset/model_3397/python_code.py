from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class StateMachine_Place:

    def __init__(self, tokens: int, name: str, StateMachine_Place: set["StateMachine_Arc"] = None):
        self.tokens = tokens
        self.name = name
        self.StateMachine_Place = StateMachine_Place if StateMachine_Place is not None else set()
        
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
    def StateMachine_Place(self):
        return self.__StateMachine_Place

    @StateMachine_Place.setter
    def StateMachine_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Place__StateMachine_Place", None)
        self.__StateMachine_Place = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StateMachine_Arc2"):
                    opp_val = getattr(item, "StateMachine_Arc2", None)
                    
                    if opp_val == self:
                        setattr(item, "StateMachine_Arc2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StateMachine_Arc2"):
                    opp_val = getattr(item, "StateMachine_Arc2", None)
                    
                    setattr(item, "StateMachine_Arc2", self)
                    

class StateMachine_PNTransition:

    pass
class StateMachine_Arc:

    def __init__(self, weight: int, toPlace: bool, StateMachine_Arc: "StateMachine_PNTransition" = None, StateMachine_Arc2: "StateMachine_Place" = None):
        self.weight = weight
        self.toPlace = toPlace
        self.StateMachine_Arc = StateMachine_Arc
        self.StateMachine_Arc2 = StateMachine_Arc2
        
    @property
    def toPlace(self) -> bool:
        return self.__toPlace

    @toPlace.setter
    def toPlace(self, toPlace: bool):
        self.__toPlace = toPlace

    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def StateMachine_Arc2(self):
        return self.__StateMachine_Arc2

    @StateMachine_Arc2.setter
    def StateMachine_Arc2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Arc__StateMachine_Arc2", None)
        self.__StateMachine_Arc2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine_Place"):
                opp_val = getattr(old_value, "StateMachine_Place", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine_Place"):
                opp_val = getattr(value, "StateMachine_Place", None)
                if opp_val is None:
                    setattr(value, "StateMachine_Place", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def StateMachine_Arc(self):
        return self.__StateMachine_Arc

    @StateMachine_Arc.setter
    def StateMachine_Arc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Arc__StateMachine_Arc", None)
        self.__StateMachine_Arc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine_PNTransition"):
                opp_val = getattr(old_value, "StateMachine_PNTransition", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine_PNTransition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine_PNTransition"):
                opp_val = getattr(value, "StateMachine_PNTransition", None)
                setattr(value, "StateMachine_PNTransition", self)
