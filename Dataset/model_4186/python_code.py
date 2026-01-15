from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class mDSL_Greeting:

    def __init__(self, name: str, mDSL_Greeting: "mDSL_Model" = None):
        self.name = name
        self.mDSL_Greeting = mDSL_Greeting
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mDSL_Greeting(self):
        return self.__mDSL_Greeting

    @mDSL_Greeting.setter
    def mDSL_Greeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mDSL_Greeting__mDSL_Greeting", None)
        self.__mDSL_Greeting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mDSL_Model"):
                opp_val = getattr(old_value, "mDSL_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mDSL_Model"):
                opp_val = getattr(value, "mDSL_Model", None)
                if opp_val is None:
                    setattr(value, "mDSL_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mDSL_Model:

    pass