from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class docl_Greeting:

    def __init__(self, name: str, docl_Greeting: "docl_Model" = None):
        self.name = name
        self.docl_Greeting = docl_Greeting
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def docl_Greeting(self):
        return self.__docl_Greeting

    @docl_Greeting.setter
    def docl_Greeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docl_Greeting__docl_Greeting", None)
        self.__docl_Greeting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docl_Model"):
                opp_val = getattr(old_value, "docl_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docl_Model"):
                opp_val = getattr(value, "docl_Model", None)
                if opp_val is None:
                    setattr(value, "docl_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class docl_Model:

    pass