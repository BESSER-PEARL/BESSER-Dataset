from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Greeting:

    pass
class greetings_RefGreeting(Greeting):

    pass
class greetings_HelloGreeting(Greeting):

    def __init__(self, name: str, greetings_HelloGreeting: "greetings_HelloGreeting" = None, greetings_HelloGreeting1: "greetings_HelloGreeting" = None, greetings_HelloGreeting4: "greetings_RefGreeting" = None):
        self.name = name
        self.greetings_HelloGreeting = greetings_HelloGreeting
        self.greetings_HelloGreeting1 = greetings_HelloGreeting1
        self.greetings_HelloGreeting4 = greetings_HelloGreeting4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def greetings_HelloGreeting4(self):
        return self.__greetings_HelloGreeting4

    @greetings_HelloGreeting4.setter
    def greetings_HelloGreeting4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_greetings_HelloGreeting__greetings_HelloGreeting4", None)
        self.__greetings_HelloGreeting4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "greetings_RefGreeting"):
                opp_val = getattr(old_value, "greetings_RefGreeting", None)
                if opp_val == self:
                    setattr(old_value, "greetings_RefGreeting", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "greetings_RefGreeting"):
                opp_val = getattr(value, "greetings_RefGreeting", None)
                setattr(value, "greetings_RefGreeting", self)

    @property
    def greetings_HelloGreeting(self):
        return self.__greetings_HelloGreeting

    @greetings_HelloGreeting.setter
    def greetings_HelloGreeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_greetings_HelloGreeting__greetings_HelloGreeting", None)
        self.__greetings_HelloGreeting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "greetings_HelloGreeting1"):
                opp_val = getattr(old_value, "greetings_HelloGreeting1", None)
                if opp_val == self:
                    setattr(old_value, "greetings_HelloGreeting1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "greetings_HelloGreeting1"):
                opp_val = getattr(value, "greetings_HelloGreeting1", None)
                setattr(value, "greetings_HelloGreeting1", self)

    @property
    def greetings_HelloGreeting1(self):
        return self.__greetings_HelloGreeting1

    @greetings_HelloGreeting1.setter
    def greetings_HelloGreeting1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_greetings_HelloGreeting__greetings_HelloGreeting1", None)
        self.__greetings_HelloGreeting1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "greetings_HelloGreeting"):
                opp_val = getattr(old_value, "greetings_HelloGreeting", None)
                if opp_val == self:
                    setattr(old_value, "greetings_HelloGreeting", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "greetings_HelloGreeting"):
                opp_val = getattr(value, "greetings_HelloGreeting", None)
                setattr(value, "greetings_HelloGreeting", self)

class greetings_Greeting:

    pass
class greetings_Model:

    pass