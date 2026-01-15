from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class datavault_Greeting:

    def __init__(self, name: str, datavault_Greeting: "datavault_Model" = None):
        self.name = name
        self.datavault_Greeting = datavault_Greeting
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def datavault_Greeting(self):
        return self.__datavault_Greeting

    @datavault_Greeting.setter
    def datavault_Greeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datavault_Greeting__datavault_Greeting", None)
        self.__datavault_Greeting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datavault_Model"):
                opp_val = getattr(old_value, "datavault_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datavault_Model"):
                opp_val = getattr(value, "datavault_Model", None)
                if opp_val is None:
                    setattr(value, "datavault_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class datavault_Model:

    pass