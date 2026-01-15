from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class xSampleDsl_Greeting:

    def __init__(self, name: str, xSampleDsl_Greeting: "xSampleDsl_Model" = None):
        self.name = name
        self.xSampleDsl_Greeting = xSampleDsl_Greeting
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def xSampleDsl_Greeting(self):
        return self.__xSampleDsl_Greeting

    @xSampleDsl_Greeting.setter
    def xSampleDsl_Greeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xSampleDsl_Greeting__xSampleDsl_Greeting", None)
        self.__xSampleDsl_Greeting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xSampleDsl_Model"):
                opp_val = getattr(old_value, "xSampleDsl_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xSampleDsl_Model"):
                opp_val = getattr(value, "xSampleDsl_Model", None)
                if opp_val is None:
                    setattr(value, "xSampleDsl_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xSampleDsl_Model:

    pass