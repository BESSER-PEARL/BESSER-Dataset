from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class B_RootB:

    pass
class B_B:

    def __init__(self, b: int, bs: "B_RootB" = None, B: "B_RootB" = None):
        self.b = b
        self.bs = bs
        self.B = B
        
    @property
    def b(self) -> int:
        return self.__b

    @b.setter
    def b(self, b: int):
        self.__b = b

    @property
    def bs(self):
        return self.__bs

    @bs.setter
    def bs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B_B__bs", None)
        self.__bs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RootB"):
                opp_val = getattr(old_value, "RootB", None)
                if opp_val == self:
                    setattr(old_value, "RootB", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RootB"):
                opp_val = getattr(value, "RootB", None)
                setattr(value, "RootB", self)

    @property
    def B(self):
        return self.__B

    @B.setter
    def B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B_B__B", None)
        self.__B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "root"):
                opp_val = getattr(old_value, "root", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "root"):
                opp_val = getattr(value, "root", None)
                if opp_val is None:
                    setattr(value, "root", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
