from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class java_Model:

    pass
class java_Greeting:

    def __init__(self, name: str, java_Greeting: "java_Model" = None):
        self.name = name
        self.java_Greeting = java_Greeting
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def java_Greeting(self):
        return self.__java_Greeting

    @java_Greeting.setter
    def java_Greeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Greeting__java_Greeting", None)
        self.__java_Greeting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Model"):
                opp_val = getattr(old_value, "java_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Model"):
                opp_val = getattr(value, "java_Model", None)
                if opp_val is None:
                    setattr(value, "java_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
