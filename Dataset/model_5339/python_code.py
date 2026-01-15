from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class B_B1:

    def __init__(self, name: str, B_B1: set["B_B2"] = None):
        self.name = name
        self.B_B1 = B_B1 if B_B1 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def B_B1(self):
        return self.__B_B1

    @B_B1.setter
    def B_B1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B_B1__B_B1", None)
        self.__B_B1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "B_B2"):
                    opp_val = getattr(item, "B_B2", None)
                    
                    if opp_val == self:
                        setattr(item, "B_B2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "B_B2"):
                    opp_val = getattr(item, "B_B2", None)
                    
                    setattr(item, "B_B2", self)
                    

class B_B2:

    def __init__(self, name: str, B_B2: "B_B1" = None):
        self.name = name
        self.B_B2 = B_B2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def B_B2(self):
        return self.__B_B2

    @B_B2.setter
    def B_B2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B_B2__B_B2", None)
        self.__B_B2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "B_B1"):
                opp_val = getattr(old_value, "B_B1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "B_B1"):
                opp_val = getattr(value, "B_B1", None)
                if opp_val is None:
                    setattr(value, "B_B1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
