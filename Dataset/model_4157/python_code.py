from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class myDsl2_Greeting:

    def __init__(self, name: str, myDsl2_Greeting: "myDsl2_Model" = None):
        self.name = name
        self.myDsl2_Greeting = myDsl2_Greeting
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl2_Greeting(self):
        return self.__myDsl2_Greeting

    @myDsl2_Greeting.setter
    def myDsl2_Greeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl2_Greeting__myDsl2_Greeting", None)
        self.__myDsl2_Greeting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl2_Model"):
                opp_val = getattr(old_value, "myDsl2_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl2_Model"):
                opp_val = getattr(value, "myDsl2_Model", None)
                if opp_val is None:
                    setattr(value, "myDsl2_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl2_Model:

    pass