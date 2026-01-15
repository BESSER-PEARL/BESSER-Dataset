from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class lhs_B:

    def __init__(self, b: str, lhs_B: "lhs_A" = None):
        self.b = b
        self.lhs_B = lhs_B
        
    @property
    def b(self) -> str:
        return self.__b

    @b.setter
    def b(self, b: str):
        self.__b = b

    @property
    def lhs_B(self):
        return self.__lhs_B

    @lhs_B.setter
    def lhs_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lhs_B__lhs_B", None)
        self.__lhs_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lhs_A"):
                opp_val = getattr(old_value, "lhs_A", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lhs_A"):
                opp_val = getattr(value, "lhs_A", None)
                if opp_val is None:
                    setattr(value, "lhs_A", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class lhs_A:

    def __init__(self, a: str, lhs_A: set["lhs_B"] = None):
        self.a = a
        self.lhs_A = lhs_A if lhs_A is not None else set()
        
    @property
    def a(self) -> str:
        return self.__a

    @a.setter
    def a(self, a: str):
        self.__a = a

    @property
    def lhs_A(self):
        return self.__lhs_A

    @lhs_A.setter
    def lhs_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lhs_A__lhs_A", None)
        self.__lhs_A = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lhs_B"):
                    opp_val = getattr(item, "lhs_B", None)
                    
                    if opp_val == self:
                        setattr(item, "lhs_B", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lhs_B"):
                    opp_val = getattr(item, "lhs_B", None)
                    
                    setattr(item, "lhs_B", self)
                    
