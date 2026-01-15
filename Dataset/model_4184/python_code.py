from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class kobold_Greeting:

    def __init__(self, name: str, kobold_Greeting: "kobold_Model" = None):
        self.name = name
        self.kobold_Greeting = kobold_Greeting
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def kobold_Greeting(self):
        return self.__kobold_Greeting

    @kobold_Greeting.setter
    def kobold_Greeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kobold_Greeting__kobold_Greeting", None)
        self.__kobold_Greeting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kobold_Model"):
                opp_val = getattr(old_value, "kobold_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kobold_Model"):
                opp_val = getattr(value, "kobold_Model", None)
                if opp_val is None:
                    setattr(value, "kobold_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class kobold_Model:

    pass