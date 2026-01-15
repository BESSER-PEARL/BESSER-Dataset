from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class pascal_Greeting:

    def __init__(self, name: str, pascal_Greeting: "pascal_Model" = None):
        self.name = name
        self.pascal_Greeting = pascal_Greeting
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pascal_Greeting(self):
        return self.__pascal_Greeting

    @pascal_Greeting.setter
    def pascal_Greeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_Greeting__pascal_Greeting", None)
        self.__pascal_Greeting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_Model"):
                opp_val = getattr(old_value, "pascal_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_Model"):
                opp_val = getattr(value, "pascal_Model", None)
                if opp_val is None:
                    setattr(value, "pascal_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pascal_Model:

    pass