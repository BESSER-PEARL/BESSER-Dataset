from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class lexertrace_Greeting:

    def __init__(self, name: str, lexertrace_Greeting: "lexertrace_Model" = None):
        self.name = name
        self.lexertrace_Greeting = lexertrace_Greeting
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def lexertrace_Greeting(self):
        return self.__lexertrace_Greeting

    @lexertrace_Greeting.setter
    def lexertrace_Greeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lexertrace_Greeting__lexertrace_Greeting", None)
        self.__lexertrace_Greeting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lexertrace_Model"):
                opp_val = getattr(old_value, "lexertrace_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lexertrace_Model"):
                opp_val = getattr(value, "lexertrace_Model", None)
                if opp_val is None:
                    setattr(value, "lexertrace_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class lexertrace_Model:

    pass