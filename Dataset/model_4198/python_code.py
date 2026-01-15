from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class myDsl_Greeting:

    def __init__(self, name: str, myDsl_Greeting: "myDsl_Greeting" = None, myDsl_Greeting0: "myDsl_Greeting" = None):
        self.name = name
        self.myDsl_Greeting = myDsl_Greeting
        self.myDsl_Greeting0 = myDsl_Greeting0
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Greeting0(self):
        return self.__myDsl_Greeting0

    @myDsl_Greeting0.setter
    def myDsl_Greeting0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Greeting__myDsl_Greeting0", None)
        self.__myDsl_Greeting0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Greeting"):
                opp_val = getattr(old_value, "myDsl_Greeting", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Greeting", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Greeting"):
                opp_val = getattr(value, "myDsl_Greeting", None)
                setattr(value, "myDsl_Greeting", self)

    @property
    def myDsl_Greeting(self):
        return self.__myDsl_Greeting

    @myDsl_Greeting.setter
    def myDsl_Greeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Greeting__myDsl_Greeting", None)
        self.__myDsl_Greeting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Greeting0"):
                opp_val = getattr(old_value, "myDsl_Greeting0", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Greeting0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Greeting0"):
                opp_val = getattr(value, "myDsl_Greeting0", None)
                setattr(value, "myDsl_Greeting0", self)
