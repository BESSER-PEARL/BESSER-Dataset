from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class scribbleTraceDsl_Parameter:

    def __init__(self, type: str, value: str, scribbleTraceDsl_Parameter: "scribbleTraceDsl_Messagetransfer" = None):
        self.type = type
        self.value = value
        self.scribbleTraceDsl_Parameter = scribbleTraceDsl_Parameter
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def scribbleTraceDsl_Parameter(self):
        return self.__scribbleTraceDsl_Parameter

    @scribbleTraceDsl_Parameter.setter
    def scribbleTraceDsl_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scribbleTraceDsl_Parameter__scribbleTraceDsl_Parameter", None)
        self.__scribbleTraceDsl_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scribbleTraceDsl_Messagetransfer"):
                opp_val = getattr(old_value, "scribbleTraceDsl_Messagetransfer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scribbleTraceDsl_Messagetransfer"):
                opp_val = getattr(value, "scribbleTraceDsl_Messagetransfer", None)
                if opp_val is None:
                    setattr(value, "scribbleTraceDsl_Messagetransfer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Stepdefn:

    pass
class scribbleTraceDsl_Messagetransfer(Stepdefn):

    pass
class scribbleTraceDsl_Stepdefn:

    pass
class scribbleTraceDsl_Trace:

    def __init__(self, roles: str, scribbleTraceDsl_Trace: set["scribbleTraceDsl_Stepdefn"] = None):
        self.roles = roles
        self.scribbleTraceDsl_Trace = scribbleTraceDsl_Trace if scribbleTraceDsl_Trace is not None else set()
        
    @property
    def roles(self) -> str:
        return self.__roles

    @roles.setter
    def roles(self, roles: str):
        self.__roles = roles

    @property
    def scribbleTraceDsl_Trace(self):
        return self.__scribbleTraceDsl_Trace

    @scribbleTraceDsl_Trace.setter
    def scribbleTraceDsl_Trace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scribbleTraceDsl_Trace__scribbleTraceDsl_Trace", None)
        self.__scribbleTraceDsl_Trace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scribbleTraceDsl_Stepdefn"):
                    opp_val = getattr(item, "scribbleTraceDsl_Stepdefn", None)
                    
                    if opp_val == self:
                        setattr(item, "scribbleTraceDsl_Stepdefn", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scribbleTraceDsl_Stepdefn"):
                    opp_val = getattr(item, "scribbleTraceDsl_Stepdefn", None)
                    
                    setattr(item, "scribbleTraceDsl_Stepdefn", self)
                    
