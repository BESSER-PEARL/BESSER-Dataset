from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Trace_TraceLink:

    def __init__(self, targetType: str, description: str, sourceName: str, sourceType: str, targetName: str, Trace_TraceLink: "Trace_Trace" = None):
        self.targetType = targetType
        self.description = description
        self.sourceName = sourceName
        self.sourceType = sourceType
        self.targetName = targetName
        self.Trace_TraceLink = Trace_TraceLink
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def sourceType(self) -> str:
        return self.__sourceType

    @sourceType.setter
    def sourceType(self, sourceType: str):
        self.__sourceType = sourceType

    @property
    def sourceName(self) -> str:
        return self.__sourceName

    @sourceName.setter
    def sourceName(self, sourceName: str):
        self.__sourceName = sourceName

    @property
    def targetType(self) -> str:
        return self.__targetType

    @targetType.setter
    def targetType(self, targetType: str):
        self.__targetType = targetType

    @property
    def targetName(self) -> str:
        return self.__targetName

    @targetName.setter
    def targetName(self, targetName: str):
        self.__targetName = targetName

    @property
    def Trace_TraceLink(self):
        return self.__Trace_TraceLink

    @Trace_TraceLink.setter
    def Trace_TraceLink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Trace_TraceLink__Trace_TraceLink", None)
        self.__Trace_TraceLink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Trace_Trace"):
                opp_val = getattr(old_value, "Trace_Trace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Trace_Trace"):
                opp_val = getattr(value, "Trace_Trace", None)
                if opp_val is None:
                    setattr(value, "Trace_Trace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Trace_Trace:

    def __init__(self, description: str, Trace_Trace: set["Trace_TraceLink"] = None):
        self.description = description
        self.Trace_Trace = Trace_Trace if Trace_Trace is not None else set()
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def Trace_Trace(self):
        return self.__Trace_Trace

    @Trace_Trace.setter
    def Trace_Trace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Trace_Trace__Trace_Trace", None)
        self.__Trace_Trace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Trace_TraceLink"):
                    opp_val = getattr(item, "Trace_TraceLink", None)
                    
                    if opp_val == self:
                        setattr(item, "Trace_TraceLink", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Trace_TraceLink"):
                    opp_val = getattr(item, "Trace_TraceLink", None)
                    
                    setattr(item, "Trace_TraceLink", self)
                    
