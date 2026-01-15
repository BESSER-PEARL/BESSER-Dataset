from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class resource_Greeting:

    def __init__(self, name: str, resource_Greeting: "resource_Model" = None):
        self.name = name
        self.resource_Greeting = resource_Greeting
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def resource_Greeting(self):
        return self.__resource_Greeting

    @resource_Greeting.setter
    def resource_Greeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_resource_Greeting__resource_Greeting", None)
        self.__resource_Greeting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resource_Model"):
                opp_val = getattr(old_value, "resource_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resource_Model"):
                opp_val = getattr(value, "resource_Model", None)
                if opp_val is None:
                    setattr(value, "resource_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class resource_Model:

    pass