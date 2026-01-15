from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class a_B:

    pass
class a_A:

    def __init__(self, m: int, a_A: set["a_B"] = None):
        self.m = m
        self.a_A = a_A if a_A is not None else set()
        
    @property
    def m(self) -> int:
        return self.__m

    @m.setter
    def m(self, m: int):
        self.__m = m

    @property
    def a_A(self):
        return self.__a_A

    @a_A.setter
    def a_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_a_A__a_A", None)
        self.__a_A = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "a_B"):
                    opp_val = getattr(item, "a_B", None)
                    
                    if opp_val == self:
                        setattr(item, "a_B", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "a_B"):
                    opp_val = getattr(item, "a_B", None)
                    
                    setattr(item, "a_B", self)
                    
