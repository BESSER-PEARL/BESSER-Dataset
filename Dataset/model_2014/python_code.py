from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class trace_DebugLocationData:

    def __init__(self, label: str, offset: int, length: int, lineNumber: int, endLineNumber: int, path: str, endOffset: int, trace_DebugLocationData: "trace_DebugTraceRegion" = None):
        self.label = label
        self.offset = offset
        self.length = length
        self.lineNumber = lineNumber
        self.endLineNumber = endLineNumber
        self.path = path
        self.endOffset = endOffset
        self.trace_DebugLocationData = trace_DebugLocationData
        
    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

    @property
    def lineNumber(self) -> int:
        return self.__lineNumber

    @lineNumber.setter
    def lineNumber(self, lineNumber: int):
        self.__lineNumber = lineNumber

    @property
    def endLineNumber(self) -> int:
        return self.__endLineNumber

    @endLineNumber.setter
    def endLineNumber(self, endLineNumber: int):
        self.__endLineNumber = endLineNumber

    @property
    def endOffset(self) -> int:
        return self.__endOffset

    @endOffset.setter
    def endOffset(self, endOffset: int):
        self.__endOffset = endOffset

    @property
    def offset(self) -> int:
        return self.__offset

    @offset.setter
    def offset(self, offset: int):
        self.__offset = offset

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def trace_DebugLocationData(self):
        return self.__trace_DebugLocationData

    @trace_DebugLocationData.setter
    def trace_DebugLocationData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_DebugLocationData__trace_DebugLocationData", None)
        self.__trace_DebugLocationData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_DebugTraceRegion3"):
                opp_val = getattr(old_value, "trace_DebugTraceRegion3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_DebugTraceRegion3"):
                opp_val = getattr(value, "trace_DebugTraceRegion3", None)
                if opp_val is None:
                    setattr(value, "trace_DebugTraceRegion3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class trace_DebugTraceRegion:

    def __init__(self, label: str, myOffset: int, myLength: int, myLineNumber: int, myEndLineNumber: int, myEndOffset: int, trace_DebugTraceRegion: "trace_DebugTraceRegion" = None, trace_DebugTraceRegion0: set["trace_DebugTraceRegion"] = None, trace_DebugTraceRegion3: set["trace_DebugLocationData"] = None):
        self.label = label
        self.myOffset = myOffset
        self.myLength = myLength
        self.myLineNumber = myLineNumber
        self.myEndLineNumber = myEndLineNumber
        self.myEndOffset = myEndOffset
        self.trace_DebugTraceRegion = trace_DebugTraceRegion
        self.trace_DebugTraceRegion0 = trace_DebugTraceRegion0 if trace_DebugTraceRegion0 is not None else set()
        self.trace_DebugTraceRegion3 = trace_DebugTraceRegion3 if trace_DebugTraceRegion3 is not None else set()
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def myEndOffset(self) -> int:
        return self.__myEndOffset

    @myEndOffset.setter
    def myEndOffset(self, myEndOffset: int):
        self.__myEndOffset = myEndOffset

    @property
    def myOffset(self) -> int:
        return self.__myOffset

    @myOffset.setter
    def myOffset(self, myOffset: int):
        self.__myOffset = myOffset

    @property
    def myLineNumber(self) -> int:
        return self.__myLineNumber

    @myLineNumber.setter
    def myLineNumber(self, myLineNumber: int):
        self.__myLineNumber = myLineNumber

    @property
    def myLength(self) -> int:
        return self.__myLength

    @myLength.setter
    def myLength(self, myLength: int):
        self.__myLength = myLength

    @property
    def myEndLineNumber(self) -> int:
        return self.__myEndLineNumber

    @myEndLineNumber.setter
    def myEndLineNumber(self, myEndLineNumber: int):
        self.__myEndLineNumber = myEndLineNumber

    @property
    def trace_DebugTraceRegion0(self):
        return self.__trace_DebugTraceRegion0

    @trace_DebugTraceRegion0.setter
    def trace_DebugTraceRegion0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_DebugTraceRegion__trace_DebugTraceRegion0", None)
        self.__trace_DebugTraceRegion0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trace_DebugTraceRegion"):
                    opp_val = getattr(item, "trace_DebugTraceRegion", None)
                    
                    if opp_val == self:
                        setattr(item, "trace_DebugTraceRegion", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trace_DebugTraceRegion"):
                    opp_val = getattr(item, "trace_DebugTraceRegion", None)
                    
                    setattr(item, "trace_DebugTraceRegion", self)
                    

    @property
    def trace_DebugTraceRegion3(self):
        return self.__trace_DebugTraceRegion3

    @trace_DebugTraceRegion3.setter
    def trace_DebugTraceRegion3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_DebugTraceRegion__trace_DebugTraceRegion3", None)
        self.__trace_DebugTraceRegion3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trace_DebugLocationData"):
                    opp_val = getattr(item, "trace_DebugLocationData", None)
                    
                    if opp_val == self:
                        setattr(item, "trace_DebugLocationData", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trace_DebugLocationData"):
                    opp_val = getattr(item, "trace_DebugLocationData", None)
                    
                    setattr(item, "trace_DebugLocationData", self)
                    

    @property
    def trace_DebugTraceRegion(self):
        return self.__trace_DebugTraceRegion

    @trace_DebugTraceRegion.setter
    def trace_DebugTraceRegion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_DebugTraceRegion__trace_DebugTraceRegion", None)
        self.__trace_DebugTraceRegion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_DebugTraceRegion0"):
                opp_val = getattr(old_value, "trace_DebugTraceRegion0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_DebugTraceRegion0"):
                opp_val = getattr(value, "trace_DebugTraceRegion0", None)
                if opp_val is None:
                    setattr(value, "trace_DebugTraceRegion0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
