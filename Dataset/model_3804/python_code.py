from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class A_A3:

    pass
class A_A2:

    def __init__(self, f: str, A_A2: "A_A1" = None):
        self.f = f
        self.A_A2 = A_A2
        
    @property
    def f(self) -> str:
        return self.__f

    @f.setter
    def f(self, f: str):
        self.__f = f

    @property
    def A_A2(self):
        return self.__A_A2

    @A_A2.setter
    def A_A2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A_A2__A_A2", None)
        self.__A_A2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "A_A1"):
                opp_val = getattr(old_value, "A_A1", None)
                if opp_val == self:
                    setattr(old_value, "A_A1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "A_A1"):
                opp_val = getattr(value, "A_A1", None)
                setattr(value, "A_A1", self)

class A_A1:

    pass