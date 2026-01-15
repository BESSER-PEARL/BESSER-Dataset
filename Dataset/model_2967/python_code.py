from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class EEnumOp(Enum):
    oneway = "oneway"
    notification = "notification"
    requestresponse = "requestresponse"
    solicitresponse = "solicitresponse"
class EEnumValueType(Enum):
    string = "string"
    date = "date"
    document = "document"
    int = "int"
    float = "float"
    double = "double"
class EEnumSubset(Enum):
    req = "req"
    pro = "pro"
    off = "off"
    exp = "exp"
class EEnumlogicalType(Enum):
    AND = "AND"
    OR = "OR"
class EEnumDimensionType(Enum):
    monotonic = "monotonic"
    antitonic = "antitonic"
class EEnumMes(Enum):
    input = "input"
    output = "output"
    fault = "fault"
class EEnumIntention(Enum):
    offering = "offering"
    expectation = "expectation"


############################################
# Definition of Classes
############################################

class InfoType:

    pass
class ASD_InfoTypeImported(InfoType):

    def __init__(self, url: str):
        self.url = url
        
    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

class ASD_Annotation:

    def __init__(self, value: str, key: str, Annotation: "ASD_NamedElement" = None, annotations: "ASD_NamedElement" = None):
        self.value = value
        self.key = key
        self.Annotation = Annotation
        self.annotations = annotations
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def annotations(self):
        return self.__annotations

    @annotations.setter
    def annotations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASD_Annotation__annotations", None)
        self.__annotations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NamedElement"):
                opp_val = getattr(old_value, "NamedElement", None)
                if opp_val == self:
                    setattr(old_value, "NamedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NamedElement"):
                opp_val = getattr(value, "NamedElement", None)
                setattr(value, "NamedElement", self)

    @property
    def Annotation(self):
        return self.__Annotation

    @Annotation.setter
    def Annotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASD_Annotation__Annotation", None)
        self.__Annotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner"):
                opp_val = getattr(old_value, "owner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner"):
                opp_val = getattr(value, "owner", None)
                if opp_val is None:
                    setattr(value, "owner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ASD_NamedElement(ABC):

    def __init__(self, name: str, owner: set["ASD_Annotation"] = None, NamedElement: "ASD_Annotation" = None):
        self.name = name
        self.owner = owner if owner is not None else set()
        self.NamedElement = NamedElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASD_NamedElement__owner", None)
        self.__owner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Annotation"):
                    opp_val = getattr(item, "Annotation", None)
                    
                    if opp_val == self:
                        setattr(item, "Annotation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Annotation"):
                    opp_val = getattr(item, "Annotation", None)
                    
                    setattr(item, "Annotation", self)
                    

    @property
    def NamedElement(self):
        return self.__NamedElement

    @NamedElement.setter
    def NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASD_NamedElement__NamedElement", None)
        self.__NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "annotations"):
                opp_val = getattr(old_value, "annotations", None)
                if opp_val == self:
                    setattr(old_value, "annotations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "annotations"):
                opp_val = getattr(value, "annotations", None)
                setattr(value, "annotations", self)

class NamedElement:

    pass
class ASD_Profile(NamedElement):

    pass
class ASD_Operation(NamedElement):

    def __init__(self, messagePattern: str, Operation: "ASD_ServiceDescription" = None, operation: set["ASD_Message"] = None, operations: "ASD_ServiceDescription" = None, Operation10: "ASD_Message" = None, ASD_Operation: "ASD_Profile" = None):
        self.messagePattern = messagePattern
        self.Operation = Operation
        self.operation = operation if operation is not None else set()
        self.operations = operations
        self.Operation10 = Operation10
        self.ASD_Operation = ASD_Operation
        
    @property
    def messagePattern(self) -> str:
        return self.__messagePattern

    @messagePattern.setter
    def messagePattern(self, messagePattern: str):
        self.__messagePattern = messagePattern

    @property
    def ASD_Operation(self):
        return self.__ASD_Operation

    @ASD_Operation.setter
    def ASD_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASD_Operation__ASD_Operation", None)
        self.__ASD_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ASD_Profile"):
                opp_val = getattr(old_value, "ASD_Profile", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ASD_Profile"):
                opp_val = getattr(value, "ASD_Profile", None)
                if opp_val is None:
                    setattr(value, "ASD_Profile", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def operation(self):
        return self.__operation

    @operation.setter
    def operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASD_Operation__operation", None)
        self.__operation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Message"):
                    opp_val = getattr(item, "Message", None)
                    
                    if opp_val == self:
                        setattr(item, "Message", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Message"):
                    opp_val = getattr(item, "Message", None)
                    
                    setattr(item, "Message", self)
                    

    @property
    def Operation10(self):
        return self.__Operation10

    @Operation10.setter
    def Operation10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASD_Operation__Operation10", None)
        self.__Operation10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contents"):
                opp_val = getattr(old_value, "contents", None)
                if opp_val == self:
                    setattr(old_value, "contents", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contents"):
                opp_val = getattr(value, "contents", None)
                setattr(value, "contents", self)

    @property
    def operations(self):
        return self.__operations

    @operations.setter
    def operations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASD_Operation__operations", None)
        self.__operations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ServiceDescription"):
                opp_val = getattr(old_value, "ServiceDescription", None)
                if opp_val == self:
                    setattr(old_value, "ServiceDescription", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ServiceDescription"):
                opp_val = getattr(value, "ServiceDescription", None)
                setattr(value, "ServiceDescription", self)

    @property
    def Operation(self):
        return self.__Operation

    @Operation.setter
    def Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASD_Operation__Operation", None)
        self.__Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "service"):
                opp_val = getattr(old_value, "service", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "service"):
                opp_val = getattr(value, "service", None)
                if opp_val is None:
                    setattr(value, "service", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ASD_Message(NamedElement):

    def __init__(self, role: str, subset: str, Message: "ASD_Operation" = None, message: set["ASD_InfoType"] = None, contents: "ASD_Operation" = None, Message17: "ASD_InfoType" = None):
        self.role = role
        self.subset = subset
        self.Message = Message
        self.message = message if message is not None else set()
        self.contents = contents
        self.Message17 = Message17
        
    @property
    def subset(self) -> str:
        return self.__subset

    @subset.setter
    def subset(self, subset: str):
        self.__subset = subset

    @property
    def role(self) -> str:
        return self.__role

    @role.setter
    def role(self, role: str):
        self.__role = role

    @property
    def Message17(self):
        return self.__Message17

    @Message17.setter
    def Message17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASD_Message__Message17", None)
        self.__Message17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "infoType"):
                opp_val = getattr(old_value, "infoType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "infoType"):
                opp_val = getattr(value, "infoType", None)
                if opp_val is None:
                    setattr(value, "infoType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Message(self):
        return self.__Message

    @Message.setter
    def Message(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASD_Message__Message", None)
        self.__Message = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operation"):
                opp_val = getattr(old_value, "operation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operation"):
                opp_val = getattr(value, "operation", None)
                if opp_val is None:
                    setattr(value, "operation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASD_Message__message", None)
        self.__message = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InfoType8"):
                    opp_val = getattr(item, "InfoType8", None)
                    
                    if opp_val == self:
                        setattr(item, "InfoType8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InfoType8"):
                    opp_val = getattr(item, "InfoType8", None)
                    
                    setattr(item, "InfoType8", self)
                    

    @property
    def contents(self):
        return self.__contents

    @contents.setter
    def contents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASD_Message__contents", None)
        self.__contents = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Operation10"):
                opp_val = getattr(old_value, "Operation10", None)
                if opp_val == self:
                    setattr(old_value, "Operation10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operation10"):
                opp_val = getattr(value, "Operation10", None)
                setattr(value, "Operation10", self)

class ASD_InfoType(NamedElement):

    def __init__(self, valueType: str, valueRange: str, subset: str, InfoType: "ASD_ServiceDescription" = None, InfoType8: "ASD_Message" = None, infoType: set["ASD_Message"] = None, infotypes: "ASD_ServiceDescription" = None, ASD_InfoType: "ASD_InfoType" = None, ASD_InfoType11: set["ASD_InfoType"] = None, ASD_InfoType15: "ASD_InfoType" = None, ASD_InfoType13: "ASD_InfoType" = None):
        self.valueType = valueType
        self.valueRange = valueRange
        self.subset = subset
        self.InfoType = InfoType
        self.InfoType8 = InfoType8
        self.infoType = infoType if infoType is not None else set()
        self.infotypes = infotypes
        self.ASD_InfoType = ASD_InfoType
        self.ASD_InfoType11 = ASD_InfoType11 if ASD_InfoType11 is not None else set()
        self.ASD_InfoType15 = ASD_InfoType15
        self.ASD_InfoType13 = ASD_InfoType13
        
    @property
    def subset(self) -> str:
        return self.__subset

    @subset.setter
    def subset(self, subset: str):
        self.__subset = subset

    @property
    def valueType(self) -> str:
        return self.__valueType

    @valueType.setter
    def valueType(self, valueType: str):
        self.__valueType = valueType

    @property
    def valueRange(self) -> str:
        return self.__valueRange

    @valueRange.setter
    def valueRange(self, valueRange: str):
        self.__valueRange = valueRange

    @property
    def InfoType(self):
        return self.__InfoType

    @InfoType.setter
    def InfoType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASD_InfoType__InfoType", None)
        self.__InfoType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "service2"):
                opp_val = getattr(old_value, "service2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "service2"):
                opp_val = getattr(value, "service2", None)
                if opp_val is None:
                    setattr(value, "service2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ASD_InfoType(self):
        return self.__ASD_InfoType

    @ASD_InfoType.setter
    def ASD_InfoType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASD_InfoType__ASD_InfoType", None)
        self.__ASD_InfoType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ASD_InfoType11"):
                opp_val = getattr(old_value, "ASD_InfoType11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ASD_InfoType11"):
                opp_val = getattr(value, "ASD_InfoType11", None)
                if opp_val is None:
                    setattr(value, "ASD_InfoType11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ASD_InfoType13(self):
        return self.__ASD_InfoType13

    @ASD_InfoType13.setter
    def ASD_InfoType13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASD_InfoType__ASD_InfoType13", None)
        self.__ASD_InfoType13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ASD_InfoType15"):
                opp_val = getattr(old_value, "ASD_InfoType15", None)
                if opp_val == self:
                    setattr(old_value, "ASD_InfoType15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ASD_InfoType15"):
                opp_val = getattr(value, "ASD_InfoType15", None)
                setattr(value, "ASD_InfoType15", self)

    @property
    def infotypes(self):
        return self.__infotypes

    @infotypes.setter
    def infotypes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASD_InfoType__infotypes", None)
        self.__infotypes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ServiceDescription19"):
                opp_val = getattr(old_value, "ServiceDescription19", None)
                if opp_val == self:
                    setattr(old_value, "ServiceDescription19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ServiceDescription19"):
                opp_val = getattr(value, "ServiceDescription19", None)
                setattr(value, "ServiceDescription19", self)

    @property
    def InfoType8(self):
        return self.__InfoType8

    @InfoType8.setter
    def InfoType8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASD_InfoType__InfoType8", None)
        self.__InfoType8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "message"):
                opp_val = getattr(old_value, "message", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "message"):
                opp_val = getattr(value, "message", None)
                if opp_val is None:
                    setattr(value, "message", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ASD_InfoType15(self):
        return self.__ASD_InfoType15

    @ASD_InfoType15.setter
    def ASD_InfoType15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASD_InfoType__ASD_InfoType15", None)
        self.__ASD_InfoType15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ASD_InfoType13"):
                opp_val = getattr(old_value, "ASD_InfoType13", None)
                if opp_val == self:
                    setattr(old_value, "ASD_InfoType13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ASD_InfoType13"):
                opp_val = getattr(value, "ASD_InfoType13", None)
                setattr(value, "ASD_InfoType13", self)

    @property
    def infoType(self):
        return self.__infoType

    @infoType.setter
    def infoType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASD_InfoType__infoType", None)
        self.__infoType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Message17"):
                    opp_val = getattr(item, "Message17", None)
                    
                    if opp_val == self:
                        setattr(item, "Message17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Message17"):
                    opp_val = getattr(item, "Message17", None)
                    
                    setattr(item, "Message17", self)
                    

    @property
    def ASD_InfoType11(self):
        return self.__ASD_InfoType11

    @ASD_InfoType11.setter
    def ASD_InfoType11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASD_InfoType__ASD_InfoType11", None)
        self.__ASD_InfoType11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ASD_InfoType"):
                    opp_val = getattr(item, "ASD_InfoType", None)
                    
                    if opp_val == self:
                        setattr(item, "ASD_InfoType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ASD_InfoType"):
                    opp_val = getattr(item, "ASD_InfoType", None)
                    
                    setattr(item, "ASD_InfoType", self)
                    

class ASD_Assertion(NamedElement):

    def __init__(self, dimensionType: str, role: str, minVal: float, maxVal: float, lType: str, subset: str, dimension: str, Assertion: "ASD_AssertionSet" = None, assertions: "ASD_AssertionSet" = None):
        self.dimensionType = dimensionType
        self.role = role
        self.minVal = minVal
        self.maxVal = maxVal
        self.lType = lType
        self.subset = subset
        self.dimension = dimension
        self.Assertion = Assertion
        self.assertions = assertions
        
    @property
    def dimension(self) -> str:
        return self.__dimension

    @dimension.setter
    def dimension(self, dimension: str):
        self.__dimension = dimension

    @property
    def role(self) -> str:
        return self.__role

    @role.setter
    def role(self, role: str):
        self.__role = role

    @property
    def minVal(self) -> float:
        return self.__minVal

    @minVal.setter
    def minVal(self, minVal: float):
        self.__minVal = minVal

    @property
    def lType(self) -> str:
        return self.__lType

    @lType.setter
    def lType(self, lType: str):
        self.__lType = lType

    @property
    def subset(self) -> str:
        return self.__subset

    @subset.setter
    def subset(self, subset: str):
        self.__subset = subset

    @property
    def dimensionType(self) -> str:
        return self.__dimensionType

    @dimensionType.setter
    def dimensionType(self, dimensionType: str):
        self.__dimensionType = dimensionType

    @property
    def maxVal(self) -> float:
        return self.__maxVal

    @maxVal.setter
    def maxVal(self, maxVal: float):
        self.__maxVal = maxVal

    @property
    def assertions(self):
        return self.__assertions

    @assertions.setter
    def assertions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASD_Assertion__assertions", None)
        self.__assertions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AssertionSet28"):
                opp_val = getattr(old_value, "AssertionSet28", None)
                if opp_val == self:
                    setattr(old_value, "AssertionSet28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AssertionSet28"):
                opp_val = getattr(value, "AssertionSet28", None)
                setattr(value, "AssertionSet28", self)

    @property
    def Assertion(self):
        return self.__Assertion

    @Assertion.setter
    def Assertion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASD_Assertion__Assertion", None)
        self.__Assertion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "set"):
                opp_val = getattr(old_value, "set", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "set"):
                opp_val = getattr(value, "set", None)
                if opp_val is None:
                    setattr(value, "set", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ASD_AssertionSet(NamedElement):

    def __init__(self, lType: str, AssertionSet: "ASD_Profile" = None, sets: "ASD_Profile" = None, set: set["ASD_Assertion"] = None, AssertionSet28: "ASD_Assertion" = None):
        self.lType = lType
        self.AssertionSet = AssertionSet
        self.sets = sets
        self.set = set if set is not None else set()
        self.AssertionSet28 = AssertionSet28
        
    @property
    def lType(self) -> str:
        return self.__lType

    @lType.setter
    def lType(self, lType: str):
        self.__lType = lType

    @property
    def AssertionSet(self):
        return self.__AssertionSet

    @AssertionSet.setter
    def AssertionSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASD_AssertionSet__AssertionSet", None)
        self.__AssertionSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile"):
                opp_val = getattr(old_value, "profile", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile"):
                opp_val = getattr(value, "profile", None)
                if opp_val is None:
                    setattr(value, "profile", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def AssertionSet28(self):
        return self.__AssertionSet28

    @AssertionSet28.setter
    def AssertionSet28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASD_AssertionSet__AssertionSet28", None)
        self.__AssertionSet28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assertions"):
                opp_val = getattr(old_value, "assertions", None)
                if opp_val == self:
                    setattr(old_value, "assertions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assertions"):
                opp_val = getattr(value, "assertions", None)
                setattr(value, "assertions", self)

    @property
    def sets(self):
        return self.__sets

    @sets.setter
    def sets(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASD_AssertionSet__sets", None)
        self.__sets = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Profile25"):
                opp_val = getattr(old_value, "Profile25", None)
                if opp_val == self:
                    setattr(old_value, "Profile25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Profile25"):
                opp_val = getattr(value, "Profile25", None)
                setattr(value, "Profile25", self)

    @property
    def set(self):
        return self.__set

    @set.setter
    def set(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ASD_AssertionSet__set", None)
        self.__set = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Assertion"):
                    opp_val = getattr(item, "Assertion", None)
                    
                    if opp_val == self:
                        setattr(item, "Assertion", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Assertion"):
                    opp_val = getattr(item, "Assertion", None)
                    
                    setattr(item, "Assertion", self)
                    

class ASD_ServiceDescription(NamedElement):

    pass