from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class myDsl1_Greeting:

    def __init__(self, name: str, myDsl1_Greeting: "myDsl1_Model" = None):
        self.name = name
        self.myDsl1_Greeting = myDsl1_Greeting
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl1_Greeting(self):
        return self.__myDsl1_Greeting

    @myDsl1_Greeting.setter
    def myDsl1_Greeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl1_Greeting__myDsl1_Greeting", None)
        self.__myDsl1_Greeting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl1_Model"):
                opp_val = getattr(old_value, "myDsl1_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl1_Model"):
                opp_val = getattr(value, "myDsl1_Model", None)
                if opp_val is None:
                    setattr(value, "myDsl1_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl1_Model:

    pass