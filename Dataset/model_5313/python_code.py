from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class hExample_1_LHS_B:

    def __init__(self, name: str, hExample_1_LHS_B: "hExample_1_LHS_A" = None):
        self.name = name
        self.hExample_1_LHS_B = hExample_1_LHS_B
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def hExample_1_LHS_B(self):
        return self.__hExample_1_LHS_B

    @hExample_1_LHS_B.setter
    def hExample_1_LHS_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hExample_1_LHS_B__hExample_1_LHS_B", None)
        self.__hExample_1_LHS_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hExample_1_LHS_A"):
                opp_val = getattr(old_value, "hExample_1_LHS_A", None)
                if opp_val == self:
                    setattr(old_value, "hExample_1_LHS_A", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hExample_1_LHS_A"):
                opp_val = getattr(value, "hExample_1_LHS_A", None)
                setattr(value, "hExample_1_LHS_A", self)

class hExample_1_LHS_A:

    pass