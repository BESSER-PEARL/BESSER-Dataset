from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Level:

    pass
class Trace_Trace:

    def __init__(self, name: str, 0: set["Level"] = None):
        self.name = name
        self.0 = 0 if 0 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 0(self):
        return self.__0

    @0.setter
    def 0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Trace_Trace__0", None)
        self.__0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#"):
                    opp_val = getattr(item, "#", None)
                    
                    if opp_val == self:
                        setattr(item, "#", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#"):
                    opp_val = getattr(item, "#", None)
                    
                    setattr(item, "#", self)
                    

class Trace_Index:

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class Index:

    pass
class Trace_Call:

    def __init__(self, methodName: str, DBAccessesNumber: str, DBRowsNumber: str, CPUTime: str, 08: "Level" = None, Trace_Call: set["Index"] = None):
        self.methodName = methodName
        self.DBAccessesNumber = DBAccessesNumber
        self.DBRowsNumber = DBRowsNumber
        self.CPUTime = CPUTime
        self.08 = 08
        self.Trace_Call = Trace_Call if Trace_Call is not None else set()
        
    @property
    def DBRowsNumber(self) -> str:
        return self.__DBRowsNumber

    @DBRowsNumber.setter
    def DBRowsNumber(self, DBRowsNumber: str):
        self.__DBRowsNumber = DBRowsNumber

    @property
    def methodName(self) -> str:
        return self.__methodName

    @methodName.setter
    def methodName(self, methodName: str):
        self.__methodName = methodName

    @property
    def CPUTime(self) -> str:
        return self.__CPUTime

    @CPUTime.setter
    def CPUTime(self, CPUTime: str):
        self.__CPUTime = CPUTime

    @property
    def DBAccessesNumber(self) -> str:
        return self.__DBAccessesNumber

    @DBAccessesNumber.setter
    def DBAccessesNumber(self, DBAccessesNumber: str):
        self.__DBAccessesNumber = DBAccessesNumber

    @property
    def 08(self):
        return self.__08

    @08.setter
    def 08(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Trace_Call__08", None)
        self.__08 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#9"):
                opp_val = getattr(old_value, "#9", None)
                if opp_val == self:
                    setattr(old_value, "#9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#9"):
                opp_val = getattr(value, "#9", None)
                setattr(value, "#9", self)

    @property
    def Trace_Call(self):
        return self.__Trace_Call

    @Trace_Call.setter
    def Trace_Call(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Trace_Call__Trace_Call", None)
        self.__Trace_Call = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Index"):
                    opp_val = getattr(item, "Index", None)
                    
                    if opp_val == self:
                        setattr(item, "Index", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Index"):
                    opp_val = getattr(item, "Index", None)
                    
                    setattr(item, "Index", self)
                    

class Call:

    pass
class Trace:

    pass
class Trace_Level:

    pass