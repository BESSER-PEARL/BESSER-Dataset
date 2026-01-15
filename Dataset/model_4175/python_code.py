from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class activator_Greeting:

    def __init__(self, name: str, activator_Greeting: "activator_Model" = None):
        self.name = name
        self.activator_Greeting = activator_Greeting
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def activator_Greeting(self):
        return self.__activator_Greeting

    @activator_Greeting.setter
    def activator_Greeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activator_Greeting__activator_Greeting", None)
        self.__activator_Greeting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activator_Model"):
                opp_val = getattr(old_value, "activator_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activator_Model"):
                opp_val = getattr(value, "activator_Model", None)
                if opp_val is None:
                    setattr(value, "activator_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class activator_Model:

    pass