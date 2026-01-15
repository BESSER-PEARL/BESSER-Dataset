from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class greetings_Greeting:

    def __init__(self, name: str, greetings_Greeting: "greetings_Model" = None):
        self.name = name
        self.greetings_Greeting = greetings_Greeting
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def greetings_Greeting(self):
        return self.__greetings_Greeting

    @greetings_Greeting.setter
    def greetings_Greeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_greetings_Greeting__greetings_Greeting", None)
        self.__greetings_Greeting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "greetings_Model"):
                opp_val = getattr(old_value, "greetings_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "greetings_Model"):
                opp_val = getattr(value, "greetings_Model", None)
                if opp_val is None:
                    setattr(value, "greetings_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class greetings_Model:

    pass