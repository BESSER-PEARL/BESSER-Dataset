from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class myDsl_Greeting:

    def __init__(self, name: str, myDsl_Greeting: "myDsl_Model" = None):
        self.name = name
        self.myDsl_Greeting = myDsl_Greeting
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "myDsl_Model6"):
                opp_val = getattr(old_value, "myDsl_Model6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Model6"):
                opp_val = getattr(value, "myDsl_Model6", None)
                if opp_val is None:
                    setattr(value, "myDsl_Model6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_Model:

    def __init__(self, name: str, myDsl_Model: "myDsl_Model" = None, myDsl_Model0: "myDsl_Model" = None, myDsl_Model4: "myDsl_Model" = None, myDsl_Model2: set["myDsl_Model"] = None, myDsl_Model6: set["myDsl_Greeting"] = None):
        self.name = name
        self.myDsl_Model = myDsl_Model
        self.myDsl_Model0 = myDsl_Model0
        self.myDsl_Model4 = myDsl_Model4
        self.myDsl_Model2 = myDsl_Model2 if myDsl_Model2 is not None else set()
        self.myDsl_Model6 = myDsl_Model6 if myDsl_Model6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Model0(self):
        return self.__myDsl_Model0

    @myDsl_Model0.setter
    def myDsl_Model0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Model__myDsl_Model0", None)
        self.__myDsl_Model0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Model"):
                opp_val = getattr(old_value, "myDsl_Model", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Model", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Model"):
                opp_val = getattr(value, "myDsl_Model", None)
                setattr(value, "myDsl_Model", self)

    @property
    def myDsl_Model2(self):
        return self.__myDsl_Model2

    @myDsl_Model2.setter
    def myDsl_Model2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Model__myDsl_Model2", None)
        self.__myDsl_Model2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_Model4"):
                    opp_val = getattr(item, "myDsl_Model4", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_Model4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_Model4"):
                    opp_val = getattr(item, "myDsl_Model4", None)
                    
                    setattr(item, "myDsl_Model4", self)
                    

    @property
    def myDsl_Model6(self):
        return self.__myDsl_Model6

    @myDsl_Model6.setter
    def myDsl_Model6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Model__myDsl_Model6", None)
        self.__myDsl_Model6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_Greeting"):
                    opp_val = getattr(item, "myDsl_Greeting", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_Greeting", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_Greeting"):
                    opp_val = getattr(item, "myDsl_Greeting", None)
                    
                    setattr(item, "myDsl_Greeting", self)
                    

    @property
    def myDsl_Model(self):
        return self.__myDsl_Model

    @myDsl_Model.setter
    def myDsl_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Model__myDsl_Model", None)
        self.__myDsl_Model = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Model0"):
                opp_val = getattr(old_value, "myDsl_Model0", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Model0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Model0"):
                opp_val = getattr(value, "myDsl_Model0", None)
                setattr(value, "myDsl_Model0", self)

    @property
    def myDsl_Model4(self):
        return self.__myDsl_Model4

    @myDsl_Model4.setter
    def myDsl_Model4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Model__myDsl_Model4", None)
        self.__myDsl_Model4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Model2"):
                opp_val = getattr(old_value, "myDsl_Model2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Model2"):
                opp_val = getattr(value, "myDsl_Model2", None)
                if opp_val is None:
                    setattr(value, "myDsl_Model2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
