from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class comp_Greeting:

    def __init__(self, name: str, comp_Greeting: "comp_Model" = None):
        self.name = name
        self.comp_Greeting = comp_Greeting
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def comp_Greeting(self):
        return self.__comp_Greeting

    @comp_Greeting.setter
    def comp_Greeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_comp_Greeting__comp_Greeting", None)
        self.__comp_Greeting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "comp_Model"):
                opp_val = getattr(old_value, "comp_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "comp_Model"):
                opp_val = getattr(value, "comp_Model", None)
                if opp_val is None:
                    setattr(value, "comp_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class comp_Model:

    pass