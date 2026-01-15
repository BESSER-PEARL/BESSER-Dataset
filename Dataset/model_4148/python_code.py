from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class myDsl_AbstractGreeting:

    def __init__(self, name: str, myDsl_AbstractGreeting2: "myDsl_GreetingReference" = None, myDsl_AbstractGreeting: "myDsl_Model" = None):
        self.name = name
        self.myDsl_AbstractGreeting2 = myDsl_AbstractGreeting2
        self.myDsl_AbstractGreeting = myDsl_AbstractGreeting
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_AbstractGreeting(self):
        return self.__myDsl_AbstractGreeting

    @myDsl_AbstractGreeting.setter
    def myDsl_AbstractGreeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_AbstractGreeting__myDsl_AbstractGreeting", None)
        self.__myDsl_AbstractGreeting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Model"):
                opp_val = getattr(old_value, "myDsl_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Model"):
                opp_val = getattr(value, "myDsl_Model", None)
                if opp_val is None:
                    setattr(value, "myDsl_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_AbstractGreeting2(self):
        return self.__myDsl_AbstractGreeting2

    @myDsl_AbstractGreeting2.setter
    def myDsl_AbstractGreeting2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_AbstractGreeting__myDsl_AbstractGreeting2", None)
        self.__myDsl_AbstractGreeting2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_GreetingReference"):
                opp_val = getattr(old_value, "myDsl_GreetingReference", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_GreetingReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_GreetingReference"):
                opp_val = getattr(value, "myDsl_GreetingReference", None)
                setattr(value, "myDsl_GreetingReference", self)

class myDsl_Model:

    pass
class AbstractGreeting:

    pass
class myDsl_GreetingReference(AbstractGreeting):

    pass
class myDsl_Greeting(AbstractGreeting):

    pass