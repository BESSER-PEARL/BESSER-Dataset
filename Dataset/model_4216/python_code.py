from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class helloworldext_Greeting:

    pass
class helloworldext_Person:

    def __init__(self, name: str, helloworldext_Person: "helloworldext_Greeting" = None):
        self.name = name
        self.helloworldext_Person = helloworldext_Person
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def helloworldext_Person(self):
        return self.__helloworldext_Person

    @helloworldext_Person.setter
    def helloworldext_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworldext_Person__helloworldext_Person", None)
        self.__helloworldext_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloworldext_Greeting2"):
                opp_val = getattr(old_value, "helloworldext_Greeting2", None)
                if opp_val == self:
                    setattr(old_value, "helloworldext_Greeting2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloworldext_Greeting2"):
                opp_val = getattr(value, "helloworldext_Greeting2", None)
                setattr(value, "helloworldext_Greeting2", self)

class helloworldext_GreetingMessage:

    def __init__(self, text: str, helloworldext_GreetingMessage: "helloworldext_Greeting" = None):
        self.text = text
        self.helloworldext_GreetingMessage = helloworldext_GreetingMessage
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def helloworldext_GreetingMessage(self):
        return self.__helloworldext_GreetingMessage

    @helloworldext_GreetingMessage.setter
    def helloworldext_GreetingMessage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworldext_GreetingMessage__helloworldext_GreetingMessage", None)
        self.__helloworldext_GreetingMessage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloworldext_Greeting"):
                opp_val = getattr(old_value, "helloworldext_Greeting", None)
                if opp_val == self:
                    setattr(old_value, "helloworldext_Greeting", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloworldext_Greeting"):
                opp_val = getattr(value, "helloworldext_Greeting", None)
                setattr(value, "helloworldext_Greeting", self)
