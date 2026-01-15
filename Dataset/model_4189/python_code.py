from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class evlDSL_Greeting:

    def __init__(self, name: str, evlDSL_Greeting: "evlDSL_Model" = None):
        self.name = name
        self.evlDSL_Greeting = evlDSL_Greeting
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def evlDSL_Greeting(self):
        return self.__evlDSL_Greeting

    @evlDSL_Greeting.setter
    def evlDSL_Greeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_evlDSL_Greeting__evlDSL_Greeting", None)
        self.__evlDSL_Greeting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "evlDSL_Model"):
                opp_val = getattr(old_value, "evlDSL_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "evlDSL_Model"):
                opp_val = getattr(value, "evlDSL_Model", None)
                if opp_val is None:
                    setattr(value, "evlDSL_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class evlDSL_Model:

    pass