from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class noJdt_Greeting:

    def __init__(self, name: str, noJdt_Greeting: "noJdt_Model" = None, noJdt_Greeting3: "noJdt_Greeting" = None, noJdt_Greeting1: "noJdt_Greeting" = None):
        self.name = name
        self.noJdt_Greeting = noJdt_Greeting
        self.noJdt_Greeting3 = noJdt_Greeting3
        self.noJdt_Greeting1 = noJdt_Greeting1
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def noJdt_Greeting3(self):
        return self.__noJdt_Greeting3

    @noJdt_Greeting3.setter
    def noJdt_Greeting3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noJdt_Greeting__noJdt_Greeting3", None)
        self.__noJdt_Greeting3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "noJdt_Greeting1"):
                opp_val = getattr(old_value, "noJdt_Greeting1", None)
                if opp_val == self:
                    setattr(old_value, "noJdt_Greeting1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "noJdt_Greeting1"):
                opp_val = getattr(value, "noJdt_Greeting1", None)
                setattr(value, "noJdt_Greeting1", self)

    @property
    def noJdt_Greeting(self):
        return self.__noJdt_Greeting

    @noJdt_Greeting.setter
    def noJdt_Greeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noJdt_Greeting__noJdt_Greeting", None)
        self.__noJdt_Greeting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "noJdt_Model"):
                opp_val = getattr(old_value, "noJdt_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "noJdt_Model"):
                opp_val = getattr(value, "noJdt_Model", None)
                if opp_val is None:
                    setattr(value, "noJdt_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def noJdt_Greeting1(self):
        return self.__noJdt_Greeting1

    @noJdt_Greeting1.setter
    def noJdt_Greeting1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noJdt_Greeting__noJdt_Greeting1", None)
        self.__noJdt_Greeting1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "noJdt_Greeting3"):
                opp_val = getattr(old_value, "noJdt_Greeting3", None)
                if opp_val == self:
                    setattr(old_value, "noJdt_Greeting3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "noJdt_Greeting3"):
                opp_val = getattr(value, "noJdt_Greeting3", None)
                setattr(value, "noJdt_Greeting3", self)

class noJdt_Model:

    pass