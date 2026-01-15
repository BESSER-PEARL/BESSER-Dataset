from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class myDslA_Greeting:

    def __init__(self, name: str, myDslA_Greeting: "myDslA_Model" = None):
        self.name = name
        self.myDslA_Greeting = myDslA_Greeting
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDslA_Greeting(self):
        return self.__myDslA_Greeting

    @myDslA_Greeting.setter
    def myDslA_Greeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDslA_Greeting__myDslA_Greeting", None)
        self.__myDslA_Greeting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDslA_Model"):
                opp_val = getattr(old_value, "myDslA_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDslA_Model"):
                opp_val = getattr(value, "myDslA_Model", None)
                if opp_val is None:
                    setattr(value, "myDslA_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDslA_Model:

    pass