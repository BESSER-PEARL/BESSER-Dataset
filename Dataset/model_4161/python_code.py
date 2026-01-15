from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class dsl_Greeting:

    def __init__(self, name: str, dsl_Greeting: "dsl_Model" = None):
        self.name = name
        self.dsl_Greeting = dsl_Greeting
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_Greeting(self):
        return self.__dsl_Greeting

    @dsl_Greeting.setter
    def dsl_Greeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Greeting__dsl_Greeting", None)
        self.__dsl_Greeting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Model"):
                opp_val = getattr(old_value, "dsl_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Model"):
                opp_val = getattr(value, "dsl_Model", None)
                if opp_val is None:
                    setattr(value, "dsl_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dsl_Model:

    pass