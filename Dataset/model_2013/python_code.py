from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Trace_Index:

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class Index:

    pass
class Trace_Call:

    def __init__(self, methodName: str, DBAccessesNumber: str, DBRowsNumber: str, CPUTime: str, calls: "Level" = None, Trace_Call: set["Index"] = None):
        self.methodName = methodName
        self.DBAccessesNumber = DBAccessesNumber
        self.DBRowsNumber = DBRowsNumber
        self.CPUTime = CPUTime
        self.calls = calls
        self.Trace_Call = Trace_Call if Trace_Call is not None else set()
        
        pass
    @property
    def CPUTime(self):
        return self.__CPUTime

    @CPUTime.setter
    def CPUTime(self, CPUTime: str):
        self.__CPUTime = CPUTime


    @property
    def DBAccessesNumber(self):
        return self.__DBAccessesNumber

    @DBAccessesNumber.setter
    def DBAccessesNumber(self, DBAccessesNumber: str):
        self.__DBAccessesNumber = DBAccessesNumber


    @property
    def methodName(self):
        return self.__methodName

    @methodName.setter
    def methodName(self, methodName: str):
        self.__methodName = methodName


    @property
    def DBRowsNumber(self):
        return self.__DBRowsNumber

    @DBRowsNumber.setter
    def DBRowsNumber(self, DBRowsNumber: str):
        self.__DBRowsNumber = DBRowsNumber


    @property
    def calls(self):
        return self.__calls

    @calls.setter
    def calls(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Trace_Call__calls", None)
        self.__calls = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Level4"):
                opp_val = getattr(old_value, "Level4", None)
                if opp_val == self:
                    setattr(old_value, "Level4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Level4"):
                opp_val = getattr(value, "Level4", None)
                setattr(value, "Level4", self)

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
class Level:

    pass
class Trace_Trace:

    def __init__(self, name: str, trace: set["Level"] = None):
        self.name = name
        self.trace = trace if trace is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def trace(self):
        return self.__trace

    @trace.setter
    def trace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Trace_Trace__trace", None)
        self.__trace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Level"):
                    opp_val = getattr(item, "Level", None)
                    
                    if opp_val == self:
                        setattr(item, "Level", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Level"):
                    opp_val = getattr(item, "Level", None)
                    
                    setattr(item, "Level", self)
                    

class Trace:

    pass
class Trace_Level:

    pass