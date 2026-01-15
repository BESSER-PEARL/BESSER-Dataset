from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class RHS_Y:

    def __init__(self, name: str, RHS_Y: "RHS_X" = None):
        self.name = name
        self.RHS_Y = RHS_Y
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def RHS_Y(self):
        return self.__RHS_Y

    @RHS_Y.setter
    def RHS_Y(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RHS_Y__RHS_Y", None)
        self.__RHS_Y = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RHS_X"):
                opp_val = getattr(old_value, "RHS_X", None)
                if opp_val == self:
                    setattr(old_value, "RHS_X", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RHS_X"):
                opp_val = getattr(value, "RHS_X", None)
                setattr(value, "RHS_X", self)

class RHS_X:

    def __init__(self, name: str, RHS_X: "RHS_Y" = None):
        self.name = name
        self.RHS_X = RHS_X
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def RHS_X(self):
        return self.__RHS_X

    @RHS_X.setter
    def RHS_X(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RHS_X__RHS_X", None)
        self.__RHS_X = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RHS_Y"):
                opp_val = getattr(old_value, "RHS_Y", None)
                if opp_val == self:
                    setattr(old_value, "RHS_Y", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RHS_Y"):
                opp_val = getattr(value, "RHS_Y", None)
                setattr(value, "RHS_Y", self)
