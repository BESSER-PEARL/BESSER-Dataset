from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class TraceItem:

    pass
class trace_M2CTraceItem(TraceItem):

    def __init__(self, targetFile: str, token: str):
        self.targetFile = targetFile
        self.token = token
        
    @property
    def token(self) -> str:
        return self.__token

    @token.setter
    def token(self, token: str):
        self.__token = token

    @property
    def targetFile(self) -> str:
        return self.__targetFile

    @targetFile.setter
    def targetFile(self, targetFile: str):
        self.__targetFile = targetFile

class trace_M2MTraceItem(TraceItem):

    pass
class trace_EObject:

    pass
class trace_TraceItem(ABC):

    def __init__(self, kind: str, trace_TraceItem: "trace_TraceList" = None, trace_TraceItem6: set["trace_EObject"] = None, trace_TraceItem12: "trace_TraceBySource" = None):
        self.kind = kind
        self.trace_TraceItem = trace_TraceItem
        self.trace_TraceItem6 = trace_TraceItem6 if trace_TraceItem6 is not None else set()
        self.trace_TraceItem12 = trace_TraceItem12
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def trace_TraceItem(self):
        return self.__trace_TraceItem

    @trace_TraceItem.setter
    def trace_TraceItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TraceItem__trace_TraceItem", None)
        self.__trace_TraceItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_TraceList4"):
                opp_val = getattr(old_value, "trace_TraceList4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_TraceList4"):
                opp_val = getattr(value, "trace_TraceList4", None)
                if opp_val is None:
                    setattr(value, "trace_TraceList4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def trace_TraceItem6(self):
        return self.__trace_TraceItem6

    @trace_TraceItem6.setter
    def trace_TraceItem6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TraceItem__trace_TraceItem6", None)
        self.__trace_TraceItem6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trace_EObject"):
                    opp_val = getattr(item, "trace_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "trace_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trace_EObject"):
                    opp_val = getattr(item, "trace_EObject", None)
                    
                    setattr(item, "trace_EObject", self)
                    

    @property
    def trace_TraceItem12(self):
        return self.__trace_TraceItem12

    @trace_TraceItem12.setter
    def trace_TraceItem12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TraceItem__trace_TraceItem12", None)
        self.__trace_TraceItem12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_TraceBySource11"):
                opp_val = getattr(old_value, "trace_TraceBySource11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_TraceBySource11"):
                opp_val = getattr(value, "trace_TraceBySource11", None)
                if opp_val is None:
                    setattr(value, "trace_TraceBySource11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class trace_TraceBySource:

    pass
class trace_TraceList:

    pass
class trace_Trace:

    pass