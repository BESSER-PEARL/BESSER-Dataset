from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class AB_B:

    def __init__(self, name: str, AB_B: "AB_A" = None):
        self.name = name
        self.AB_B = AB_B
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def AB_B(self):
        return self.__AB_B

    @AB_B.setter
    def AB_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AB_B__AB_B", None)
        self.__AB_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AB_A"):
                opp_val = getattr(old_value, "AB_A", None)
                if opp_val == self:
                    setattr(old_value, "AB_A", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AB_A"):
                opp_val = getattr(value, "AB_A", None)
                setattr(value, "AB_A", self)

class AB_A:

    def __init__(self, i: int, AB_A: "AB_B" = None):
        self.i = i
        self.AB_A = AB_A
        
    @property
    def i(self) -> int:
        return self.__i

    @i.setter
    def i(self, i: int):
        self.__i = i

    @property
    def AB_A(self):
        return self.__AB_A

    @AB_A.setter
    def AB_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AB_A__AB_A", None)
        self.__AB_A = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AB_B"):
                opp_val = getattr(old_value, "AB_B", None)
                if opp_val == self:
                    setattr(old_value, "AB_B", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AB_B"):
                opp_val = getattr(value, "AB_B", None)
                setattr(value, "AB_B", self)
