from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class LHS_D:

    def __init__(self, name: str, LHS_D: "LHS_B" = None):
        self.name = name
        self.LHS_D = LHS_D
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def LHS_D(self):
        return self.__LHS_D

    @LHS_D.setter
    def LHS_D(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LHS_D__LHS_D", None)
        self.__LHS_D = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LHS_B4"):
                opp_val = getattr(old_value, "LHS_B4", None)
                if opp_val == self:
                    setattr(old_value, "LHS_B4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LHS_B4"):
                opp_val = getattr(value, "LHS_B4", None)
                setattr(value, "LHS_B4", self)

class LHS_C:

    def __init__(self, name: str, LHS_C: "LHS_A" = None):
        self.name = name
        self.LHS_C = LHS_C
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def LHS_C(self):
        return self.__LHS_C

    @LHS_C.setter
    def LHS_C(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LHS_C__LHS_C", None)
        self.__LHS_C = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LHS_A2"):
                opp_val = getattr(old_value, "LHS_A2", None)
                if opp_val == self:
                    setattr(old_value, "LHS_A2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LHS_A2"):
                opp_val = getattr(value, "LHS_A2", None)
                setattr(value, "LHS_A2", self)

class LHS_B:

    def __init__(self, name: str, LHS_B: "LHS_A" = None, LHS_B4: "LHS_D" = None):
        self.name = name
        self.LHS_B = LHS_B
        self.LHS_B4 = LHS_B4
        
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

    @property
    def LHS_B4(self):
        return self.__LHS_B4

    @LHS_B4.setter
    def LHS_B4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LHS_B__LHS_B4", None)
        self.__LHS_B4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LHS_D"):
                opp_val = getattr(old_value, "LHS_D", None)
                if opp_val == self:
                    setattr(old_value, "LHS_D", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LHS_D"):
                opp_val = getattr(value, "LHS_D", None)
                setattr(value, "LHS_D", self)

class LHS_A:

    def __init__(self, name: str, LHS_A: "LHS_B" = None, LHS_A2: "LHS_C" = None):
        self.name = name
        self.LHS_A = LHS_A
        self.LHS_A2 = LHS_A2
        
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

    @property
    def LHS_A2(self):
        return self.__LHS_A2

    @LHS_A2.setter
    def LHS_A2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LHS_A__LHS_A2", None)
        self.__LHS_A2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LHS_C"):
                opp_val = getattr(old_value, "LHS_C", None)
                if opp_val == self:
                    setattr(old_value, "LHS_C", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LHS_C"):
                opp_val = getattr(value, "LHS_C", None)
                setattr(value, "LHS_C", self)
