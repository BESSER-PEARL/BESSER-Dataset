from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class binDsl_L:

    pass
class binDsl_N:

    def __init__(self, cond: bool, binDsl_N2: "binDsl_L" = None, binDsl_N: "binDsl_L" = None):
        self.cond = cond
        self.binDsl_N2 = binDsl_N2
        self.binDsl_N = binDsl_N
        
    @property
    def cond(self) -> bool:
        return self.__cond

    @cond.setter
    def cond(self, cond: bool):
        self.__cond = cond

    @property
    def binDsl_N(self):
        return self.__binDsl_N

    @binDsl_N.setter
    def binDsl_N(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_binDsl_N__binDsl_N", None)
        self.__binDsl_N = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "binDsl_L"):
                opp_val = getattr(old_value, "binDsl_L", None)
                if opp_val == self:
                    setattr(old_value, "binDsl_L", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "binDsl_L"):
                opp_val = getattr(value, "binDsl_L", None)
                setattr(value, "binDsl_L", self)

    @property
    def binDsl_N2(self):
        return self.__binDsl_N2

    @binDsl_N2.setter
    def binDsl_N2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_binDsl_N__binDsl_N2", None)
        self.__binDsl_N2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "binDsl_L3"):
                opp_val = getattr(old_value, "binDsl_L3", None)
                if opp_val == self:
                    setattr(old_value, "binDsl_L3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "binDsl_L3"):
                opp_val = getattr(value, "binDsl_L3", None)
                setattr(value, "binDsl_L3", self)

class binDsl_B:

    def __init__(self, b: str, binDsl_B: "binDsl_L" = None):
        self.b = b
        self.binDsl_B = binDsl_B
        
    @property
    def b(self) -> str:
        return self.__b

    @b.setter
    def b(self, b: str):
        self.__b = b

    @property
    def binDsl_B(self):
        return self.__binDsl_B

    @binDsl_B.setter
    def binDsl_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_binDsl_B__binDsl_B", None)
        self.__binDsl_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "binDsl_L5"):
                opp_val = getattr(old_value, "binDsl_L5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "binDsl_L5"):
                opp_val = getattr(value, "binDsl_L5", None)
                if opp_val is None:
                    setattr(value, "binDsl_L5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
