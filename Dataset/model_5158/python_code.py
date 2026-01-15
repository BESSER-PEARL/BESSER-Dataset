from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class astrans_B:

    pass
class astrans_A:

    def __init__(self, ra: str, astrans_A: "astrans_B" = None, astrans_A2: "astrans_B" = None, astrans_A6: "astrans_A" = None, astrans_A4: "astrans_A" = None):
        self.ra = ra
        self.astrans_A = astrans_A
        self.astrans_A2 = astrans_A2
        self.astrans_A6 = astrans_A6
        self.astrans_A4 = astrans_A4
        
    @property
    def ra(self) -> str:
        return self.__ra

    @ra.setter
    def ra(self, ra: str):
        self.__ra = ra

    @property
    def astrans_A(self):
        return self.__astrans_A

    @astrans_A.setter
    def astrans_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astrans_A__astrans_A", None)
        self.__astrans_A = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astrans_B"):
                opp_val = getattr(old_value, "astrans_B", None)
                if opp_val == self:
                    setattr(old_value, "astrans_B", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astrans_B"):
                opp_val = getattr(value, "astrans_B", None)
                setattr(value, "astrans_B", self)

    @property
    def astrans_A6(self):
        return self.__astrans_A6

    @astrans_A6.setter
    def astrans_A6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astrans_A__astrans_A6", None)
        self.__astrans_A6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astrans_A4"):
                opp_val = getattr(old_value, "astrans_A4", None)
                if opp_val == self:
                    setattr(old_value, "astrans_A4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astrans_A4"):
                opp_val = getattr(value, "astrans_A4", None)
                setattr(value, "astrans_A4", self)

    @property
    def astrans_A2(self):
        return self.__astrans_A2

    @astrans_A2.setter
    def astrans_A2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astrans_A__astrans_A2", None)
        self.__astrans_A2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astrans_B3"):
                opp_val = getattr(old_value, "astrans_B3", None)
                if opp_val == self:
                    setattr(old_value, "astrans_B3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astrans_B3"):
                opp_val = getattr(value, "astrans_B3", None)
                setattr(value, "astrans_B3", self)

    @property
    def astrans_A4(self):
        return self.__astrans_A4

    @astrans_A4.setter
    def astrans_A4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astrans_A__astrans_A4", None)
        self.__astrans_A4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astrans_A6"):
                opp_val = getattr(old_value, "astrans_A6", None)
                if opp_val == self:
                    setattr(old_value, "astrans_A6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astrans_A6"):
                opp_val = getattr(value, "astrans_A6", None)
                setattr(value, "astrans_A6", self)
