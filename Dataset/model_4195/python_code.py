from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class helloWorldDsl_Greeting:

    def __init__(self, name: str, helloWorldDsl_Greeting: "helloWorldDsl_Model" = None):
        self.name = name
        self.helloWorldDsl_Greeting = helloWorldDsl_Greeting
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def helloWorldDsl_Greeting(self):
        return self.__helloWorldDsl_Greeting

    @helloWorldDsl_Greeting.setter
    def helloWorldDsl_Greeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloWorldDsl_Greeting__helloWorldDsl_Greeting", None)
        self.__helloWorldDsl_Greeting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloWorldDsl_Model"):
                opp_val = getattr(old_value, "helloWorldDsl_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloWorldDsl_Model"):
                opp_val = getattr(value, "helloWorldDsl_Model", None)
                if opp_val is None:
                    setattr(value, "helloWorldDsl_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class helloWorldDsl_Model:

    pass