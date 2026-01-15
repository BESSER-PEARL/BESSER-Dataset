from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class LogLevel(Enum):
    SEVERE = "SEVERE"
    WARNING = "WARNING"
    INFO = "INFO"
    CONFIG = "CONFIG"
    FINE = "FINE"
    FINER = "FINER"
    FINEST = "FINEST"


############################################
# Definition of Classes
############################################

class trace_Exception:

    def __init__(self, message: str, trace_Exception: "trace_Log" = None):
        self.message = message
        self.trace_Exception = trace_Exception
        
    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def trace_Exception(self):
        return self.__trace_Exception

    @trace_Exception.setter
    def trace_Exception(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Exception__trace_Exception", None)
        self.__trace_Exception = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_Log2"):
                opp_val = getattr(old_value, "trace_Log2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_Log2"):
                opp_val = getattr(value, "trace_Log2", None)
                if opp_val is None:
                    setattr(value, "trace_Log2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class trace_Log:

    def __init__(self, message: str, source: str, timestamp: date, level: str, trace_Log: "trace_Trace" = None, trace_Log2: set["trace_Exception"] = None):
        self.message = message
        self.source = source
        self.timestamp = timestamp
        self.level = level
        self.trace_Log = trace_Log
        self.trace_Log2 = trace_Log2 if trace_Log2 is not None else set()
        
    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def timestamp(self) -> date:
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, timestamp: date):
        self.__timestamp = timestamp

    @property
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level

    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def trace_Log2(self):
        return self.__trace_Log2

    @trace_Log2.setter
    def trace_Log2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Log__trace_Log2", None)
        self.__trace_Log2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trace_Exception"):
                    opp_val = getattr(item, "trace_Exception", None)
                    
                    if opp_val == self:
                        setattr(item, "trace_Exception", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trace_Exception"):
                    opp_val = getattr(item, "trace_Exception", None)
                    
                    setattr(item, "trace_Exception", self)
                    

    @property
    def trace_Log(self):
        return self.__trace_Log

    @trace_Log.setter
    def trace_Log(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Log__trace_Log", None)
        self.__trace_Log = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_Trace"):
                opp_val = getattr(old_value, "trace_Trace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_Trace"):
                opp_val = getattr(value, "trace_Trace", None)
                if opp_val is None:
                    setattr(value, "trace_Trace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class trace_Trace:

    pass