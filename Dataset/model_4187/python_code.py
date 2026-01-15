from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class anyaBasic_Greeting:

    def __init__(self, name: str, anyaBasic_Greeting: "anyaBasic_Model" = None):
        self.name = name
        self.anyaBasic_Greeting = anyaBasic_Greeting
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def anyaBasic_Greeting(self):
        return self.__anyaBasic_Greeting

    @anyaBasic_Greeting.setter
    def anyaBasic_Greeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_anyaBasic_Greeting__anyaBasic_Greeting", None)
        self.__anyaBasic_Greeting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "anyaBasic_Model"):
                opp_val = getattr(old_value, "anyaBasic_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "anyaBasic_Model"):
                opp_val = getattr(value, "anyaBasic_Model", None)
                if opp_val is None:
                    setattr(value, "anyaBasic_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class anyaBasic_Model:

    pass