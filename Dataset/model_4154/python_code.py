from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class prolog_Greeting:

    def __init__(self, name: str, prolog_Greeting: "prolog_Model" = None):
        self.name = name
        self.prolog_Greeting = prolog_Greeting
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def prolog_Greeting(self):
        return self.__prolog_Greeting

    @prolog_Greeting.setter
    def prolog_Greeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prolog_Greeting__prolog_Greeting", None)
        self.__prolog_Greeting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "prolog_Model"):
                opp_val = getattr(old_value, "prolog_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "prolog_Model"):
                opp_val = getattr(value, "prolog_Model", None)
                if opp_val is None:
                    setattr(value, "prolog_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class prolog_Model:

    pass