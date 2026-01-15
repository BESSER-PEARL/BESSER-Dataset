from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class myDsl_Greeting:

    def __init__(self, name: str, myDsl_Greeting: "myDsl_Model" = None, myDsl_Greeting3: "myDsl_Greeting" = None, myDsl_Greeting1: "myDsl_Greeting" = None):
        self.name = name
        self.myDsl_Greeting = myDsl_Greeting
        self.myDsl_Greeting3 = myDsl_Greeting3
        self.myDsl_Greeting1 = myDsl_Greeting1
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Greeting1(self):
        return self.__myDsl_Greeting1

    @myDsl_Greeting1.setter
    def myDsl_Greeting1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Greeting__myDsl_Greeting1", None)
        self.__myDsl_Greeting1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Greeting3"):
                opp_val = getattr(old_value, "myDsl_Greeting3", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Greeting3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Greeting3"):
                opp_val = getattr(value, "myDsl_Greeting3", None)
                setattr(value, "myDsl_Greeting3", self)

    @property
    def myDsl_Greeting(self):
        return self.__myDsl_Greeting

    @myDsl_Greeting.setter
    def myDsl_Greeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Greeting__myDsl_Greeting", None)
        self.__myDsl_Greeting = value
        
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
    def myDsl_Greeting3(self):
        return self.__myDsl_Greeting3

    @myDsl_Greeting3.setter
    def myDsl_Greeting3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Greeting__myDsl_Greeting3", None)
        self.__myDsl_Greeting3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Greeting1"):
                opp_val = getattr(old_value, "myDsl_Greeting1", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Greeting1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Greeting1"):
                opp_val = getattr(value, "myDsl_Greeting1", None)
                setattr(value, "myDsl_Greeting1", self)

class myDsl_Model:

    pass