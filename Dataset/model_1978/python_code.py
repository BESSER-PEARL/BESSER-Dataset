from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ParameterType(Enum):
    source = "source"
    target = "target"
    used = "used"


############################################
# Definition of Classes
############################################

class traces_EObject:

    pass
class traces_TraceElement:

    def __init__(self, traceType: str, value: str, typeName: str, traces_TraceElement: "traces_Trace" = None, traces_TraceElement6: "traces_EObject" = None):
        self.traceType = traceType
        self.value = value
        self.typeName = typeName
        self.traces_TraceElement = traces_TraceElement
        self.traces_TraceElement6 = traces_TraceElement6
        
    @property
    def typeName(self) -> str:
        return self.__typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self.__typeName = typeName

    @property
    def traceType(self) -> str:
        return self.__traceType

    @traceType.setter
    def traceType(self, traceType: str):
        self.__traceType = traceType

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def traces_TraceElement6(self):
        return self.__traces_TraceElement6

    @traces_TraceElement6.setter
    def traces_TraceElement6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traces_TraceElement__traces_TraceElement6", None)
        self.__traces_TraceElement6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traces_EObject"):
                opp_val = getattr(old_value, "traces_EObject", None)
                if opp_val == self:
                    setattr(old_value, "traces_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traces_EObject"):
                opp_val = getattr(value, "traces_EObject", None)
                setattr(value, "traces_EObject", self)

    @property
    def traces_TraceElement(self):
        return self.__traces_TraceElement

    @traces_TraceElement.setter
    def traces_TraceElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traces_TraceElement__traces_TraceElement", None)
        self.__traces_TraceElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traces_Trace4"):
                opp_val = getattr(old_value, "traces_Trace4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traces_Trace4"):
                opp_val = getattr(value, "traces_Trace4", None)
                if opp_val is None:
                    setattr(value, "traces_Trace4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class traces_TraceRecord:

    def __init__(self, name: str, traces_TraceRecord: set["traces_Trace"] = None, traces_TraceRecord2: set["traces_Model"] = None):
        self.name = name
        self.traces_TraceRecord = traces_TraceRecord if traces_TraceRecord is not None else set()
        self.traces_TraceRecord2 = traces_TraceRecord2 if traces_TraceRecord2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def traces_TraceRecord2(self):
        return self.__traces_TraceRecord2

    @traces_TraceRecord2.setter
    def traces_TraceRecord2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traces_TraceRecord__traces_TraceRecord2", None)
        self.__traces_TraceRecord2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "traces_Model"):
                    opp_val = getattr(item, "traces_Model", None)
                    
                    if opp_val == self:
                        setattr(item, "traces_Model", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "traces_Model"):
                    opp_val = getattr(item, "traces_Model", None)
                    
                    setattr(item, "traces_Model", self)
                    

    @property
    def traces_TraceRecord(self):
        return self.__traces_TraceRecord

    @traces_TraceRecord.setter
    def traces_TraceRecord(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traces_TraceRecord__traces_TraceRecord", None)
        self.__traces_TraceRecord = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "traces_Trace"):
                    opp_val = getattr(item, "traces_Trace", None)
                    
                    if opp_val == self:
                        setattr(item, "traces_Trace", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "traces_Trace"):
                    opp_val = getattr(item, "traces_Trace", None)
                    
                    setattr(item, "traces_Trace", self)
                    

class traces_Model:

    def __init__(self, uriModel: str, traces_Model: "traces_TraceRecord" = None, traces_Model8: "traces_EObject" = None):
        self.uriModel = uriModel
        self.traces_Model = traces_Model
        self.traces_Model8 = traces_Model8
        
    @property
    def uriModel(self) -> str:
        return self.__uriModel

    @uriModel.setter
    def uriModel(self, uriModel: str):
        self.__uriModel = uriModel

    @property
    def traces_Model(self):
        return self.__traces_Model

    @traces_Model.setter
    def traces_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traces_Model__traces_Model", None)
        self.__traces_Model = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traces_TraceRecord2"):
                opp_val = getattr(old_value, "traces_TraceRecord2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traces_TraceRecord2"):
                opp_val = getattr(value, "traces_TraceRecord2", None)
                if opp_val is None:
                    setattr(value, "traces_TraceRecord2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def traces_Model8(self):
        return self.__traces_Model8

    @traces_Model8.setter
    def traces_Model8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traces_Model__traces_Model8", None)
        self.__traces_Model8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traces_EObject9"):
                opp_val = getattr(old_value, "traces_EObject9", None)
                if opp_val == self:
                    setattr(old_value, "traces_EObject9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traces_EObject9"):
                opp_val = getattr(value, "traces_EObject9", None)
                setattr(value, "traces_EObject9", self)

class traces_Trace:

    def __init__(self, timestamp: str, ruleName: str, ruleInfo: str, traces_Trace: "traces_TraceRecord" = None, traces_Trace4: set["traces_TraceElement"] = None):
        self.timestamp = timestamp
        self.ruleName = ruleName
        self.ruleInfo = ruleInfo
        self.traces_Trace = traces_Trace
        self.traces_Trace4 = traces_Trace4 if traces_Trace4 is not None else set()
        
    @property
    def timestamp(self) -> str:
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, timestamp: str):
        self.__timestamp = timestamp

    @property
    def ruleName(self) -> str:
        return self.__ruleName

    @ruleName.setter
    def ruleName(self, ruleName: str):
        self.__ruleName = ruleName

    @property
    def ruleInfo(self) -> str:
        return self.__ruleInfo

    @ruleInfo.setter
    def ruleInfo(self, ruleInfo: str):
        self.__ruleInfo = ruleInfo

    @property
    def traces_Trace4(self):
        return self.__traces_Trace4

    @traces_Trace4.setter
    def traces_Trace4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traces_Trace__traces_Trace4", None)
        self.__traces_Trace4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "traces_TraceElement"):
                    opp_val = getattr(item, "traces_TraceElement", None)
                    
                    if opp_val == self:
                        setattr(item, "traces_TraceElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "traces_TraceElement"):
                    opp_val = getattr(item, "traces_TraceElement", None)
                    
                    setattr(item, "traces_TraceElement", self)
                    

    @property
    def traces_Trace(self):
        return self.__traces_Trace

    @traces_Trace.setter
    def traces_Trace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traces_Trace__traces_Trace", None)
        self.__traces_Trace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traces_TraceRecord"):
                opp_val = getattr(old_value, "traces_TraceRecord", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traces_TraceRecord"):
                opp_val = getattr(value, "traces_TraceRecord", None)
                if opp_val is None:
                    setattr(value, "traces_TraceRecord", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
