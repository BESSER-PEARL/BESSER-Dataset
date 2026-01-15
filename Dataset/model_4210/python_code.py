from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Element:

    pass
class myDsl_Greeting(Element):

    pass
class myDsl_Person(Element):

    def __init__(self, name: str, myDsl_Person: "myDsl_Greeting" = None):
        self.name = name
        self.myDsl_Person = myDsl_Person
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Person(self):
        return self.__myDsl_Person

    @myDsl_Person.setter
    def myDsl_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Person__myDsl_Person", None)
        self.__myDsl_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Greeting"):
                opp_val = getattr(old_value, "myDsl_Greeting", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Greeting", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Greeting"):
                opp_val = getattr(value, "myDsl_Greeting", None)
                setattr(value, "myDsl_Greeting", self)

class myDsl_Element:

    pass
class myDsl_Model:

    pass