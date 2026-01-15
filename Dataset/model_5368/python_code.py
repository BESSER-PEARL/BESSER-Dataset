from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class RHS_W:

    def __init__(self, name: str, RHS_W: "RHS_Y" = None):
        self.name = name
        self.RHS_W = RHS_W
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def RHS_W(self):
        return self.__RHS_W

    @RHS_W.setter
    def RHS_W(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RHS_W__RHS_W", None)
        self.__RHS_W = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RHS_Y4"):
                opp_val = getattr(old_value, "RHS_Y4", None)
                if opp_val == self:
                    setattr(old_value, "RHS_Y4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RHS_Y4"):
                opp_val = getattr(value, "RHS_Y4", None)
                setattr(value, "RHS_Y4", self)

class RHS_Y:

    def __init__(self, name: str, RHS_Y: "RHS_X" = None, RHS_Y4: "RHS_W" = None):
        self.name = name
        self.RHS_Y = RHS_Y
        self.RHS_Y4 = RHS_Y4
        
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
            if hasattr(old_value, "RHS_X2"):
                opp_val = getattr(old_value, "RHS_X2", None)
                if opp_val == self:
                    setattr(old_value, "RHS_X2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RHS_X2"):
                opp_val = getattr(value, "RHS_X2", None)
                setattr(value, "RHS_X2", self)

    @property
    def RHS_Y4(self):
        return self.__RHS_Y4

    @RHS_Y4.setter
    def RHS_Y4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RHS_Y__RHS_Y4", None)
        self.__RHS_Y4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RHS_W"):
                opp_val = getattr(old_value, "RHS_W", None)
                if opp_val == self:
                    setattr(old_value, "RHS_W", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RHS_W"):
                opp_val = getattr(value, "RHS_W", None)
                setattr(value, "RHS_W", self)

class RHS_V:

    def __init__(self, name: str, RHS_V: "RHS_X" = None):
        self.name = name
        self.RHS_V = RHS_V
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def RHS_V(self):
        return self.__RHS_V

    @RHS_V.setter
    def RHS_V(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RHS_V__RHS_V", None)
        self.__RHS_V = value
        
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

    def __init__(self, name: str, RHS_X: "RHS_V" = None, RHS_X2: "RHS_Y" = None):
        self.name = name
        self.RHS_X = RHS_X
        self.RHS_X2 = RHS_X2
        
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
            if hasattr(old_value, "RHS_V"):
                opp_val = getattr(old_value, "RHS_V", None)
                if opp_val == self:
                    setattr(old_value, "RHS_V", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RHS_V"):
                opp_val = getattr(value, "RHS_V", None)
                setattr(value, "RHS_V", self)

    @property
    def RHS_X2(self):
        return self.__RHS_X2

    @RHS_X2.setter
    def RHS_X2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RHS_X__RHS_X2", None)
        self.__RHS_X2 = value
        
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
