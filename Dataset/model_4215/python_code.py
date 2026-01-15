from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class helloworld2_Person:

    def __init__(self, name: str, helloworld2_Person: "helloworld2_Greeting" = None):
        self.name = name
        self.helloworld2_Person = helloworld2_Person
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def helloworld2_Person(self):
        return self.__helloworld2_Person

    @helloworld2_Person.setter
    def helloworld2_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld2_Person__helloworld2_Person", None)
        self.__helloworld2_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloworld2_Greeting2"):
                opp_val = getattr(old_value, "helloworld2_Greeting2", None)
                if opp_val == self:
                    setattr(old_value, "helloworld2_Greeting2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloworld2_Greeting2"):
                opp_val = getattr(value, "helloworld2_Greeting2", None)
                setattr(value, "helloworld2_Greeting2", self)

class helloworld2_GreetingMessage:

    def __init__(self, text: str, helloworld2_GreetingMessage: "helloworld2_Greeting" = None):
        self.text = text
        self.helloworld2_GreetingMessage = helloworld2_GreetingMessage
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def helloworld2_GreetingMessage(self):
        return self.__helloworld2_GreetingMessage

    @helloworld2_GreetingMessage.setter
    def helloworld2_GreetingMessage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloworld2_GreetingMessage__helloworld2_GreetingMessage", None)
        self.__helloworld2_GreetingMessage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloworld2_Greeting"):
                opp_val = getattr(old_value, "helloworld2_Greeting", None)
                if opp_val == self:
                    setattr(old_value, "helloworld2_Greeting", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloworld2_Greeting"):
                opp_val = getattr(value, "helloworld2_Greeting", None)
                setattr(value, "helloworld2_Greeting", self)

class helloworld2_Greeting:

    pass