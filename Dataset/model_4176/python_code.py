from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class cherry1to2_Greeting:

    def __init__(self, name: str, cherry1to2_Greeting: "cherry1to2_Model" = None):
        self.name = name
        self.cherry1to2_Greeting = cherry1to2_Greeting
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cherry1to2_Greeting(self):
        return self.__cherry1to2_Greeting

    @cherry1to2_Greeting.setter
    def cherry1to2_Greeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cherry1to2_Greeting__cherry1to2_Greeting", None)
        self.__cherry1to2_Greeting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cherry1to2_Model"):
                opp_val = getattr(old_value, "cherry1to2_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cherry1to2_Model"):
                opp_val = getattr(value, "cherry1to2_Model", None)
                if opp_val is None:
                    setattr(value, "cherry1to2_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cherry1to2_Model:

    pass