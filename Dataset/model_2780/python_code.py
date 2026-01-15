from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class p_C:

    pass
class p_B:

    pass
class p_A:

    def __init__(self, name: bool, p_A: "p_B" = None, p_A5: "p_C" = None):
        self.name = name
        self.p_A = p_A
        self.p_A5 = p_A5
        
    @property
    def name(self) -> bool:
        return self.__name

    @name.setter
    def name(self, name: bool):
        self.__name = name

    @property
    def p_A5(self):
        return self.__p_A5

    @p_A5.setter
    def p_A5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p_A__p_A5", None)
        self.__p_A5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p_C4"):
                opp_val = getattr(old_value, "p_C4", None)
                if opp_val == self:
                    setattr(old_value, "p_C4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p_C4"):
                opp_val = getattr(value, "p_C4", None)
                setattr(value, "p_C4", self)

    @property
    def p_A(self):
        return self.__p_A

    @p_A.setter
    def p_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_p_A__p_A", None)
        self.__p_A = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p_B"):
                opp_val = getattr(old_value, "p_B", None)
                if opp_val == self:
                    setattr(old_value, "p_B", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p_B"):
                opp_val = getattr(value, "p_B", None)
                setattr(value, "p_B", self)
