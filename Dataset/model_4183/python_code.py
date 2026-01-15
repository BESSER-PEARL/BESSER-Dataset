from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class hello_Greeting:

    def __init__(self, name: str, hello_Greeting: "hello_Model" = None):
        self.name = name
        self.hello_Greeting = hello_Greeting
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def hello_Greeting(self):
        return self.__hello_Greeting

    @hello_Greeting.setter
    def hello_Greeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello_Greeting__hello_Greeting", None)
        self.__hello_Greeting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hello_Model"):
                opp_val = getattr(old_value, "hello_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hello_Model"):
                opp_val = getattr(value, "hello_Model", None)
                if opp_val is None:
                    setattr(value, "hello_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class hello_Model:

    pass