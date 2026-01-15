from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class EDirectionKind(Enum):
    IN = "IN"
    INOUT = "INOUT"
    OUT = "OUT"


############################################
# Definition of Classes
############################################

class MappingOperation:

    pass
class trace_EValue:

    def __init__(self, primitiveValue: str, oclObject: str, collectionType: str, trace_EValue26: "trace_EObject" = None, trace_EValue28: "trace_EObject" = None, trace_EValue32: "trace_EValue" = None, trace_EValue30: set["trace_EValue"] = None, trace_EValue: "trace_VarParameterValue" = None, trace_EValue34: "trace_ETuplePartValue" = None):
        self.primitiveValue = primitiveValue
        self.oclObject = oclObject
        self.collectionType = collectionType
        self.trace_EValue26 = trace_EValue26
        self.trace_EValue28 = trace_EValue28
        self.trace_EValue32 = trace_EValue32
        self.trace_EValue30 = trace_EValue30 if trace_EValue30 is not None else set()
        self.trace_EValue = trace_EValue
        self.trace_EValue34 = trace_EValue34
        
    @property
    def oclObject(self) -> str:
        return self.__oclObject

    @oclObject.setter
    def oclObject(self, oclObject: str):
        self.__oclObject = oclObject

    @property
    def collectionType(self) -> str:
        return self.__collectionType

    @collectionType.setter
    def collectionType(self, collectionType: str):
        self.__collectionType = collectionType

    @property
    def primitiveValue(self) -> str:
        return self.__primitiveValue

    @primitiveValue.setter
    def primitiveValue(self, primitiveValue: str):
        self.__primitiveValue = primitiveValue

    @property
    def trace_EValue30(self):
        return self.__trace_EValue30

    @trace_EValue30.setter
    def trace_EValue30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_EValue__trace_EValue30", None)
        self.__trace_EValue30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trace_EValue32"):
                    opp_val = getattr(item, "trace_EValue32", None)
                    
                    if opp_val == self:
                        setattr(item, "trace_EValue32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trace_EValue32"):
                    opp_val = getattr(item, "trace_EValue32", None)
                    
                    setattr(item, "trace_EValue32", self)
                    

    @property
    def trace_EValue(self):
        return self.__trace_EValue

    @trace_EValue.setter
    def trace_EValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_EValue__trace_EValue", None)
        self.__trace_EValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_VarParameterValue"):
                opp_val = getattr(old_value, "trace_VarParameterValue", None)
                if opp_val == self:
                    setattr(old_value, "trace_VarParameterValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_VarParameterValue"):
                opp_val = getattr(value, "trace_VarParameterValue", None)
                setattr(value, "trace_VarParameterValue", self)

    @property
    def trace_EValue28(self):
        return self.__trace_EValue28

    @trace_EValue28.setter
    def trace_EValue28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_EValue__trace_EValue28", None)
        self.__trace_EValue28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_EObject29"):
                opp_val = getattr(old_value, "trace_EObject29", None)
                if opp_val == self:
                    setattr(old_value, "trace_EObject29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_EObject29"):
                opp_val = getattr(value, "trace_EObject29", None)
                setattr(value, "trace_EObject29", self)

    @property
    def trace_EValue34(self):
        return self.__trace_EValue34

    @trace_EValue34.setter
    def trace_EValue34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_EValue__trace_EValue34", None)
        self.__trace_EValue34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_ETuplePartValue"):
                opp_val = getattr(old_value, "trace_ETuplePartValue", None)
                if opp_val == self:
                    setattr(old_value, "trace_ETuplePartValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_ETuplePartValue"):
                opp_val = getattr(value, "trace_ETuplePartValue", None)
                setattr(value, "trace_ETuplePartValue", self)

    @property
    def trace_EValue26(self):
        return self.__trace_EValue26

    @trace_EValue26.setter
    def trace_EValue26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_EValue__trace_EValue26", None)
        self.__trace_EValue26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_EObject"):
                opp_val = getattr(old_value, "trace_EObject", None)
                if opp_val == self:
                    setattr(old_value, "trace_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_EObject"):
                opp_val = getattr(value, "trace_EObject", None)
                setattr(value, "trace_EObject", self)

    @property
    def trace_EValue32(self):
        return self.__trace_EValue32

    @trace_EValue32.setter
    def trace_EValue32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_EValue__trace_EValue32", None)
        self.__trace_EValue32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_EValue30"):
                opp_val = getattr(old_value, "trace_EValue30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_EValue30"):
                opp_val = getattr(value, "trace_EValue30", None)
                if opp_val is None:
                    setattr(value, "trace_EValue30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class trace_VarParameterValue:

    def __init__(self, kind: str, name: str, type: str, trace_VarParameterValue: "trace_EValue" = None, trace_VarParameterValue37: "trace_EMappingContext" = None, trace_VarParameterValue40: "trace_EMappingParameters" = None, trace_VarParameterValue43: "trace_EMappingResults" = None):
        self.kind = kind
        self.name = name
        self.type = type
        self.trace_VarParameterValue = trace_VarParameterValue
        self.trace_VarParameterValue37 = trace_VarParameterValue37
        self.trace_VarParameterValue40 = trace_VarParameterValue40
        self.trace_VarParameterValue43 = trace_VarParameterValue43
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def trace_VarParameterValue40(self):
        return self.__trace_VarParameterValue40

    @trace_VarParameterValue40.setter
    def trace_VarParameterValue40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_VarParameterValue__trace_VarParameterValue40", None)
        self.__trace_VarParameterValue40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_EMappingParameters39"):
                opp_val = getattr(old_value, "trace_EMappingParameters39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_EMappingParameters39"):
                opp_val = getattr(value, "trace_EMappingParameters39", None)
                if opp_val is None:
                    setattr(value, "trace_EMappingParameters39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def trace_VarParameterValue43(self):
        return self.__trace_VarParameterValue43

    @trace_VarParameterValue43.setter
    def trace_VarParameterValue43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_VarParameterValue__trace_VarParameterValue43", None)
        self.__trace_VarParameterValue43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_EMappingResults42"):
                opp_val = getattr(old_value, "trace_EMappingResults42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_EMappingResults42"):
                opp_val = getattr(value, "trace_EMappingResults42", None)
                if opp_val is None:
                    setattr(value, "trace_EMappingResults42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def trace_VarParameterValue(self):
        return self.__trace_VarParameterValue

    @trace_VarParameterValue.setter
    def trace_VarParameterValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_VarParameterValue__trace_VarParameterValue", None)
        self.__trace_VarParameterValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_EValue"):
                opp_val = getattr(old_value, "trace_EValue", None)
                if opp_val == self:
                    setattr(old_value, "trace_EValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_EValue"):
                opp_val = getattr(value, "trace_EValue", None)
                setattr(value, "trace_EValue", self)

    @property
    def trace_VarParameterValue37(self):
        return self.__trace_VarParameterValue37

    @trace_VarParameterValue37.setter
    def trace_VarParameterValue37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_VarParameterValue__trace_VarParameterValue37", None)
        self.__trace_VarParameterValue37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_EMappingContext36"):
                opp_val = getattr(old_value, "trace_EMappingContext36", None)
                if opp_val == self:
                    setattr(old_value, "trace_EMappingContext36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_EMappingContext36"):
                opp_val = getattr(value, "trace_EMappingContext36", None)
                setattr(value, "trace_EMappingContext36", self)

class trace_EMappingResults:

    pass
class trace_EMappingParameters:

    pass
class trace_EMappingContext:

    pass
class trace_EMappingOperation:

    def __init__(self, name: str, package: str, module: str, trace_EMappingOperation23: "MappingOperation" = None, trace_EMappingOperation: "trace_TraceRecord" = None):
        self.name = name
        self.package = package
        self.module = module
        self.trace_EMappingOperation23 = trace_EMappingOperation23
        self.trace_EMappingOperation = trace_EMappingOperation
        
    @property
    def package(self) -> str:
        return self.__package

    @package.setter
    def package(self, package: str):
        self.__package = package

    @property
    def module(self) -> str:
        return self.__module

    @module.setter
    def module(self, module: str):
        self.__module = module

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def trace_EMappingOperation(self):
        return self.__trace_EMappingOperation

    @trace_EMappingOperation.setter
    def trace_EMappingOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_EMappingOperation__trace_EMappingOperation", None)
        self.__trace_EMappingOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_TraceRecord9"):
                opp_val = getattr(old_value, "trace_TraceRecord9", None)
                if opp_val == self:
                    setattr(old_value, "trace_TraceRecord9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_TraceRecord9"):
                opp_val = getattr(value, "trace_TraceRecord9", None)
                setattr(value, "trace_TraceRecord9", self)

    @property
    def trace_EMappingOperation23(self):
        return self.__trace_EMappingOperation23

    @trace_EMappingOperation23.setter
    def trace_EMappingOperation23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_EMappingOperation__trace_EMappingOperation23", None)
        self.__trace_EMappingOperation23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MappingOperation24"):
                opp_val = getattr(old_value, "MappingOperation24", None)
                if opp_val == self:
                    setattr(old_value, "MappingOperation24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MappingOperation24"):
                opp_val = getattr(value, "MappingOperation24", None)
                setattr(value, "MappingOperation24", self)

class EValue:

    pass
class trace_ETuplePartValue(EValue):

    def __init__(self, name: str, trace_ETuplePartValue: "trace_EValue" = None):
        self.name = name
        self.trace_ETuplePartValue = trace_ETuplePartValue
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def trace_ETuplePartValue(self):
        return self.__trace_ETuplePartValue

    @trace_ETuplePartValue.setter
    def trace_ETuplePartValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_ETuplePartValue__trace_ETuplePartValue", None)
        self.__trace_ETuplePartValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_EValue34"):
                opp_val = getattr(old_value, "trace_EValue34", None)
                if opp_val == self:
                    setattr(old_value, "trace_EValue34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_EValue34"):
                opp_val = getattr(value, "trace_EValue34", None)
                setattr(value, "trace_EValue34", self)

class trace_EObject:

    pass
class trace_Trace:

    def __init__(self, trace_Trace: set["trace_TraceRecord"] = None, trace_Trace2: set["trace_MappingOperationToTraceRecordMapEntry"] = None, trace_Trace4: set["trace_ObjectToTraceRecordMapEntry"] = None, trace_Trace6: set["trace_ObjectToTraceRecordMapEntry"] = None):
        self.trace_Trace = trace_Trace if trace_Trace is not None else set()
        self.trace_Trace2 = trace_Trace2 if trace_Trace2 is not None else set()
        self.trace_Trace4 = trace_Trace4 if trace_Trace4 is not None else set()
        self.trace_Trace6 = trace_Trace6 if trace_Trace6 is not None else set()
        
    @property
    def trace_Trace(self):
        return self.__trace_Trace

    @trace_Trace.setter
    def trace_Trace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Trace__trace_Trace", None)
        self.__trace_Trace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trace_TraceRecord"):
                    opp_val = getattr(item, "trace_TraceRecord", None)
                    
                    if opp_val == self:
                        setattr(item, "trace_TraceRecord", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trace_TraceRecord"):
                    opp_val = getattr(item, "trace_TraceRecord", None)
                    
                    setattr(item, "trace_TraceRecord", self)
                    

    @property
    def trace_Trace4(self):
        return self.__trace_Trace4

    @trace_Trace4.setter
    def trace_Trace4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Trace__trace_Trace4", None)
        self.__trace_Trace4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trace_ObjectToTraceRecordMapEntry"):
                    opp_val = getattr(item, "trace_ObjectToTraceRecordMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "trace_ObjectToTraceRecordMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trace_ObjectToTraceRecordMapEntry"):
                    opp_val = getattr(item, "trace_ObjectToTraceRecordMapEntry", None)
                    
                    setattr(item, "trace_ObjectToTraceRecordMapEntry", self)
                    

    @property
    def trace_Trace2(self):
        return self.__trace_Trace2

    @trace_Trace2.setter
    def trace_Trace2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Trace__trace_Trace2", None)
        self.__trace_Trace2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trace_MappingOperationToTraceRecordMapEntry"):
                    opp_val = getattr(item, "trace_MappingOperationToTraceRecordMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "trace_MappingOperationToTraceRecordMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trace_MappingOperationToTraceRecordMapEntry"):
                    opp_val = getattr(item, "trace_MappingOperationToTraceRecordMapEntry", None)
                    
                    setattr(item, "trace_MappingOperationToTraceRecordMapEntry", self)
                    

    @property
    def trace_Trace6(self):
        return self.__trace_Trace6

    @trace_Trace6.setter
    def trace_Trace6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Trace__trace_Trace6", None)
        self.__trace_Trace6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trace_ObjectToTraceRecordMapEntry7"):
                    opp_val = getattr(item, "trace_ObjectToTraceRecordMapEntry7", None)
                    
                    if opp_val == self:
                        setattr(item, "trace_ObjectToTraceRecordMapEntry7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trace_ObjectToTraceRecordMapEntry7"):
                    opp_val = getattr(item, "trace_ObjectToTraceRecordMapEntry7", None)
                    
                    setattr(item, "trace_ObjectToTraceRecordMapEntry7", self)
                    

    def addRecordBySource(self, trace: str, sourceObject: str, mapping: str):
        # TODO: Implement addRecordBySource method
        pass

    def getRecordBySource(self, mapping: str, sourceObject: str) -> str:
        # TODO: Implement getRecordBySource method
        pass

class trace_ObjectToTraceRecordMapEntry:

    def __init__(self, key: str, trace_ObjectToTraceRecordMapEntry: "trace_Trace" = None, trace_ObjectToTraceRecordMapEntry7: "trace_Trace" = None, trace_ObjectToTraceRecordMapEntry45: set["trace_TraceRecord"] = None):
        self.key = key
        self.trace_ObjectToTraceRecordMapEntry = trace_ObjectToTraceRecordMapEntry
        self.trace_ObjectToTraceRecordMapEntry7 = trace_ObjectToTraceRecordMapEntry7
        self.trace_ObjectToTraceRecordMapEntry45 = trace_ObjectToTraceRecordMapEntry45 if trace_ObjectToTraceRecordMapEntry45 is not None else set()
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def trace_ObjectToTraceRecordMapEntry(self):
        return self.__trace_ObjectToTraceRecordMapEntry

    @trace_ObjectToTraceRecordMapEntry.setter
    def trace_ObjectToTraceRecordMapEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_ObjectToTraceRecordMapEntry__trace_ObjectToTraceRecordMapEntry", None)
        self.__trace_ObjectToTraceRecordMapEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_Trace4"):
                opp_val = getattr(old_value, "trace_Trace4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_Trace4"):
                opp_val = getattr(value, "trace_Trace4", None)
                if opp_val is None:
                    setattr(value, "trace_Trace4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def trace_ObjectToTraceRecordMapEntry45(self):
        return self.__trace_ObjectToTraceRecordMapEntry45

    @trace_ObjectToTraceRecordMapEntry45.setter
    def trace_ObjectToTraceRecordMapEntry45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_ObjectToTraceRecordMapEntry__trace_ObjectToTraceRecordMapEntry45", None)
        self.__trace_ObjectToTraceRecordMapEntry45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trace_TraceRecord46"):
                    opp_val = getattr(item, "trace_TraceRecord46", None)
                    
                    if opp_val == self:
                        setattr(item, "trace_TraceRecord46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trace_TraceRecord46"):
                    opp_val = getattr(item, "trace_TraceRecord46", None)
                    
                    setattr(item, "trace_TraceRecord46", self)
                    

    @property
    def trace_ObjectToTraceRecordMapEntry7(self):
        return self.__trace_ObjectToTraceRecordMapEntry7

    @trace_ObjectToTraceRecordMapEntry7.setter
    def trace_ObjectToTraceRecordMapEntry7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_ObjectToTraceRecordMapEntry__trace_ObjectToTraceRecordMapEntry7", None)
        self.__trace_ObjectToTraceRecordMapEntry7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_Trace6"):
                opp_val = getattr(old_value, "trace_Trace6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_Trace6"):
                opp_val = getattr(value, "trace_Trace6", None)
                if opp_val is None:
                    setattr(value, "trace_Trace6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class trace_MappingOperationToTraceRecordMapEntry:

    pass
class trace_TraceRecord:

    pass