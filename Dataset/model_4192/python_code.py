from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class helloBuck_Greeting:

    def __init__(self, name: str, helloBuck_Greeting: "helloBuck_Model" = None):
        self.name = name
        self.helloBuck_Greeting = helloBuck_Greeting
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def helloBuck_Greeting(self):
        return self.__helloBuck_Greeting

    @helloBuck_Greeting.setter
    def helloBuck_Greeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloBuck_Greeting__helloBuck_Greeting", None)
        self.__helloBuck_Greeting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloBuck_Model"):
                opp_val = getattr(old_value, "helloBuck_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloBuck_Model"):
                opp_val = getattr(value, "helloBuck_Model", None)
                if opp_val is None:
                    setattr(value, "helloBuck_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class helloBuck_Model:

    pass