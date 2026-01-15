from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class LHS_B:

    def __init__(self, name: str, LHS_B: "LHS_A" = None):
        self.name = name
        self.LHS_B = LHS_B
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def LHS_B(self):
        return self.__LHS_B

    @LHS_B.setter
    def LHS_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LHS_B__LHS_B", None)
        self.__LHS_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LHS_A"):
                opp_val = getattr(old_value, "LHS_A", None)
                if opp_val == self:
                    setattr(old_value, "LHS_A", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LHS_A"):
                opp_val = getattr(value, "LHS_A", None)
                setattr(value, "LHS_A", self)

class LHS_A:

    def __init__(self, name: str, LHS_A: "LHS_B" = None):
        self.name = name
        self.LHS_A = LHS_A
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def LHS_A(self):
        return self.__LHS_A

    @LHS_A.setter
    def LHS_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LHS_A__LHS_A", None)
        self.__LHS_A = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LHS_B"):
                opp_val = getattr(old_value, "LHS_B", None)
                if opp_val == self:
                    setattr(old_value, "LHS_B", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LHS_B"):
                opp_val = getattr(value, "LHS_B", None)
                setattr(value, "LHS_B", self)
