from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class scheme_Greeting:

    def __init__(self, name: str, scheme_Greeting: "scheme_Model" = None):
        self.name = name
        self.scheme_Greeting = scheme_Greeting
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def scheme_Greeting(self):
        return self.__scheme_Greeting

    @scheme_Greeting.setter
    def scheme_Greeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scheme_Greeting__scheme_Greeting", None)
        self.__scheme_Greeting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scheme_Model"):
                opp_val = getattr(old_value, "scheme_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scheme_Model"):
                opp_val = getattr(value, "scheme_Model", None)
                if opp_val is None:
                    setattr(value, "scheme_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scheme_Model:

    pass