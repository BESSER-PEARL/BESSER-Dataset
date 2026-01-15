from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class mydsl_Greeting:

    def __init__(self, name: str, mydsl_Greeting: "mydsl_Model" = None):
        self.name = name
        self.mydsl_Greeting = mydsl_Greeting
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mydsl_Greeting(self):
        return self.__mydsl_Greeting

    @mydsl_Greeting.setter
    def mydsl_Greeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mydsl_Greeting__mydsl_Greeting", None)
        self.__mydsl_Greeting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mydsl_Model"):
                opp_val = getattr(old_value, "mydsl_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mydsl_Model"):
                opp_val = getattr(value, "mydsl_Model", None)
                if opp_val is None:
                    setattr(value, "mydsl_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mydsl_Model:

    pass