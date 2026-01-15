from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Traces_EObject:

    pass
class Traces_Trace:

    def __init__(self, name: str, Traces_Trace: "Traces_EObject" = None, Traces_Trace2: "Traces_EObject" = None):
        self.name = name
        self.Traces_Trace = Traces_Trace
        self.Traces_Trace2 = Traces_Trace2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Traces_Trace2(self):
        return self.__Traces_Trace2

    @Traces_Trace2.setter
    def Traces_Trace2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Traces_Trace__Traces_Trace2", None)
        self.__Traces_Trace2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Traces_EObject3"):
                opp_val = getattr(old_value, "Traces_EObject3", None)
                if opp_val == self:
                    setattr(old_value, "Traces_EObject3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Traces_EObject3"):
                opp_val = getattr(value, "Traces_EObject3", None)
                setattr(value, "Traces_EObject3", self)

    @property
    def Traces_Trace(self):
        return self.__Traces_Trace

    @Traces_Trace.setter
    def Traces_Trace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Traces_Trace__Traces_Trace", None)
        self.__Traces_Trace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Traces_EObject"):
                opp_val = getattr(old_value, "Traces_EObject", None)
                if opp_val == self:
                    setattr(old_value, "Traces_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Traces_EObject"):
                opp_val = getattr(value, "Traces_EObject", None)
                setattr(value, "Traces_EObject", self)
