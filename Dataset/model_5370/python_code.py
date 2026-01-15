from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class hExample_1_RHS_Y:

    def __init__(self, label: str, hExample_1_RHS_Y: "hExample_1_RHS_X" = None):
        self.label = label
        self.hExample_1_RHS_Y = hExample_1_RHS_Y
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def hExample_1_RHS_Y(self):
        return self.__hExample_1_RHS_Y

    @hExample_1_RHS_Y.setter
    def hExample_1_RHS_Y(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hExample_1_RHS_Y__hExample_1_RHS_Y", None)
        self.__hExample_1_RHS_Y = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hExample_1_RHS_X"):
                opp_val = getattr(old_value, "hExample_1_RHS_X", None)
                if opp_val == self:
                    setattr(old_value, "hExample_1_RHS_X", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hExample_1_RHS_X"):
                opp_val = getattr(value, "hExample_1_RHS_X", None)
                setattr(value, "hExample_1_RHS_X", self)

class hExample_1_RHS_X:

    pass