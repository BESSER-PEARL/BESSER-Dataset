from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class rhs_Y:

    def __init__(self, y: str, rhs_Y: "rhs_X" = None):
        self.y = y
        self.rhs_Y = rhs_Y
        
    @property
    def y(self) -> str:
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y

    @property
    def rhs_Y(self):
        return self.__rhs_Y

    @rhs_Y.setter
    def rhs_Y(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rhs_Y__rhs_Y", None)
        self.__rhs_Y = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rhs_X"):
                opp_val = getattr(old_value, "rhs_X", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rhs_X"):
                opp_val = getattr(value, "rhs_X", None)
                if opp_val is None:
                    setattr(value, "rhs_X", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rhs_X:

    def __init__(self, x: str, rhs_X: set["rhs_Y"] = None):
        self.x = x
        self.rhs_X = rhs_X if rhs_X is not None else set()
        
    @property
    def x(self) -> str:
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x

    @property
    def rhs_X(self):
        return self.__rhs_X

    @rhs_X.setter
    def rhs_X(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rhs_X__rhs_X", None)
        self.__rhs_X = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rhs_Y"):
                    opp_val = getattr(item, "rhs_Y", None)
                    
                    if opp_val == self:
                        setattr(item, "rhs_Y", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rhs_Y"):
                    opp_val = getattr(item, "rhs_Y", None)
                    
                    setattr(item, "rhs_Y", self)
                    
