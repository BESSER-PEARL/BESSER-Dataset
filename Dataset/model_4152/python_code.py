from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Example_Greeting:

    def __init__(self, name: str, Example_Greeting: "Example_Model" = None):
        self.name = name
        self.Example_Greeting = Example_Greeting
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Example_Greeting(self):
        return self.__Example_Greeting

    @Example_Greeting.setter
    def Example_Greeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Example_Greeting__Example_Greeting", None)
        self.__Example_Greeting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Example_Model"):
                opp_val = getattr(old_value, "Example_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Example_Model"):
                opp_val = getattr(value, "Example_Model", None)
                if opp_val is None:
                    setattr(value, "Example_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Example_Model:

    pass