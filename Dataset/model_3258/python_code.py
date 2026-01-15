from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ProcessContent(Enum):
    LAX = "LAX"
    SKIP = "SKIP"
    STRICT = "STRICT"
class MessageValidationLevel(Enum):
    NO_VALIDATION = "NO_VALIDATION"
    SYNTAX_VALID = "SYNTAX_VALID"
    SCHEMA_VALID = "SCHEMA_VALID"
    MESSAGE_VALID = "MESSAGE_VALID"
    RULE_VALID = "RULE_VALID"
    MARKET_PRACTICE_VALID = "MARKET_PRACTICE_VALID"
    BUSINESS_PROCESS_VALID = "BUSINESS_PROCESS_VALID"
    COMPLETELY_VALID = "COMPLETELY_VALID"
class MessageDeliveryOrder(Enum):
    EXPECTED_CAUSAL_ORDER = "EXPECTED_CAUSAL_ORDER"
    FIFO_ORDERED = "FIFO_ORDERED"
    UNORDERED = "UNORDERED"
class SchemaTypeKind(Enum):
    anySimpleType = "anySimpleType"
    anyURI = "anyURI"
    base64Binary = "base64Binary"
    boolean = "boolean"
    byte = "byte"
    date = "date"
    dateTime = "dateTime"
    decimal = "decimal"
    double = "double"
    duration = "duration"
    ENTITIES = "ENTITIES"
    ENTITY = "ENTITY"
    float = "float"
    gDay = "gDay"
    gMonth = "gMonth"
    gMonthDay = "gMonthDay"
    gYear = "gYear"
    gYearMonth = "gYearMonth"
    hexBinary = "hexBinary"
    ID = "ID"
    IDREF = "IDREF"
    IDREFS = "IDREFS"
    int = "int"
    integer = "integer"
    language = "language"
    long = "long"
    Name = "Name"
    NCName = "NCName"
    negativeInteger = "negativeInteger"
    NMTOKEN = "NMTOKEN"
    NMTOKENS = "NMTOKENS"
    nonNegativeInteger = "nonNegativeInteger"
    nonPositiveInteger = "nonPositiveInteger"
    normalizedString = "normalizedString"
    positiveInteger = "positiveInteger"
    QName = "QName"
    short = "short"
    string = "string"
    time = "time"
    token = "token"
    unsignedByte = "unsignedByte"
    unsignedInt = "unsignedInt"
    unsignedLong = "unsignedLong"
    unsignedShort = "unsignedShort"
class MessageValidationResults(Enum):
    REJECT = "REJECT"
    REJECT_AND_DELIVER = "REJECT_AND_DELIVER"
    DELIVER = "DELIVER"
class SenderAsynchronicity(Enum):
    ENDPOINT_SYNCHRONOUS = "ENDPOINT_SYNCHRONOUS"
    CONVERSATION_SYNCHRONOUS = "CONVERSATION_SYNCHRONOUS"
    ASYNCHRONOUS = "ASYNCHRONOUS"
class DeliveryAssurance(Enum):
    AT_LEAST_ONCE = "AT_LEAST_ONCE"
    EXACTLY_ONCE = "EXACTLY_ONCE"
    AT_MOST_ONCE = "AT_MOST_ONCE"
class MessageCasting(Enum):
    UNICAST = "UNICAST"
    MULTICAST = "MULTICAST"
    BROADCAST = "BROADCAST"
    ANYCAST = "ANYCAST"
class ISO20022Version(Enum):
    _2004 = "_2004"
    _2013 = "_2013"
class Aggregation(Enum):
    NONE = "NONE"
    COMPOSITE = "COMPOSITE"
    SHARED = "SHARED"
class MessageValidationOnOff(Enum):
    VALIDATION_ON = "VALIDATION_ON"
    VALIDATION_OFF = "VALIDATION_OFF"
class ReceiverAsynchronicity(Enum):
    ENDPOINT_SYNCHRONOUS = "ENDPOINT_SYNCHRONOUS"
    CONVERSATION_SYNCHRONOUS = "CONVERSATION_SYNCHRONOUS"
    ASYNCHRONOUS = "ASYNCHRONOUS"
class Durability(Enum):
    DURABLE = "DURABLE"
    PERSISTENT = "PERSISTENT"
    TRANSIENT = "TRANSIENT"
class Namespace(Enum):
    any = "any"
    other = "other"
    list = "list"
class RegistrationStatus(Enum):
    PROVISIONALLY_REGISTERED = "PROVISIONALLY_REGISTERED"
    REGISTERED = "REGISTERED"
    OBSOLETE = "OBSOLETE"


############################################
# Definition of Classes
############################################

class AbstractDateTimeConcept:

    pass
class iso20022_Year(AbstractDateTimeConcept):

    pass
class iso20022_YearMonth(AbstractDateTimeConcept):

    pass
class iso20022_Month(AbstractDateTimeConcept):

    pass
class iso20022_Time(AbstractDateTimeConcept):

    pass
class iso20022_Day(AbstractDateTimeConcept):

    pass
class iso20022_MonthDay(AbstractDateTimeConcept):

    pass
class iso20022_Duration(AbstractDateTimeConcept):

    pass
class iso20022_DateTime(AbstractDateTimeConcept):

    pass
class iso20022_Date(AbstractDateTimeConcept):

    pass
class IndustryMessageSet:

    pass
class iso20022_ISO15022MessageSet(IndustryMessageSet):

    pass
class Boolean:

    pass
class iso20022_Indicator(Boolean):

    def __init__(self, meaningWhenTrue: str, meaningWhenFalse: str):
        self.meaningWhenTrue = meaningWhenTrue
        self.meaningWhenFalse = meaningWhenFalse
        
    @property
    def meaningWhenFalse(self) -> str:
        return self.__meaningWhenFalse

    @meaningWhenFalse.setter
    def meaningWhenFalse(self, meaningWhenFalse: str):
        self.__meaningWhenFalse = meaningWhenFalse

    @property
    def meaningWhenTrue(self) -> str:
        return self.__meaningWhenTrue

    @meaningWhenTrue.setter
    def meaningWhenTrue(self, meaningWhenTrue: str):
        self.__meaningWhenTrue = meaningWhenTrue

class DataType:

    pass
class iso20022_Decimal(DataType):

    def __init__(self, minInclusive: str, minExclusive: str, maxInclusive: str, maxExclusive: str, totalDigits: str, fractionDigits: str, pattern: str):
        self.minInclusive = minInclusive
        self.minExclusive = minExclusive
        self.maxInclusive = maxInclusive
        self.maxExclusive = maxExclusive
        self.totalDigits = totalDigits
        self.fractionDigits = fractionDigits
        self.pattern = pattern
        
    @property
    def minInclusive(self) -> str:
        return self.__minInclusive

    @minInclusive.setter
    def minInclusive(self, minInclusive: str):
        self.__minInclusive = minInclusive

    @property
    def fractionDigits(self) -> str:
        return self.__fractionDigits

    @fractionDigits.setter
    def fractionDigits(self, fractionDigits: str):
        self.__fractionDigits = fractionDigits

    @property
    def maxExclusive(self) -> str:
        return self.__maxExclusive

    @maxExclusive.setter
    def maxExclusive(self, maxExclusive: str):
        self.__maxExclusive = maxExclusive

    @property
    def totalDigits(self) -> str:
        return self.__totalDigits

    @totalDigits.setter
    def totalDigits(self, totalDigits: str):
        self.__totalDigits = totalDigits

    @property
    def pattern(self) -> str:
        return self.__pattern

    @pattern.setter
    def pattern(self, pattern: str):
        self.__pattern = pattern

    @property
    def maxInclusive(self) -> str:
        return self.__maxInclusive

    @maxInclusive.setter
    def maxInclusive(self, maxInclusive: str):
        self.__maxInclusive = maxInclusive

    @property
    def minExclusive(self) -> str:
        return self.__minExclusive

    @minExclusive.setter
    def minExclusive(self, minExclusive: str):
        self.__minExclusive = minExclusive

class iso20022_Boolean(DataType):

    def __init__(self, pattern: str):
        self.pattern = pattern
        
    @property
    def pattern(self) -> str:
        return self.__pattern

    @pattern.setter
    def pattern(self, pattern: str):
        self.__pattern = pattern

class iso20022_SchemaType(DataType):

    def __init__(self, kind: str):
        self.kind = kind
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

class iso20022_AbstractDateTimeConcept(DataType):

    def __init__(self, minInclusive: str, minExclusive: str, maxInclusive: str, maxExclusive: str, pattern: str):
        self.minInclusive = minInclusive
        self.minExclusive = minExclusive
        self.maxInclusive = maxInclusive
        self.maxExclusive = maxExclusive
        self.pattern = pattern
        
    @property
    def maxInclusive(self) -> str:
        return self.__maxInclusive

    @maxInclusive.setter
    def maxInclusive(self, maxInclusive: str):
        self.__maxInclusive = maxInclusive

    @property
    def pattern(self) -> str:
        return self.__pattern

    @pattern.setter
    def pattern(self, pattern: str):
        self.__pattern = pattern

    @property
    def maxExclusive(self) -> str:
        return self.__maxExclusive

    @maxExclusive.setter
    def maxExclusive(self, maxExclusive: str):
        self.__maxExclusive = maxExclusive

    @property
    def minExclusive(self) -> str:
        return self.__minExclusive

    @minExclusive.setter
    def minExclusive(self, minExclusive: str):
        self.__minExclusive = minExclusive

    @property
    def minInclusive(self) -> str:
        return self.__minInclusive

    @minInclusive.setter
    def minInclusive(self, minInclusive: str):
        self.__minInclusive = minInclusive

class iso20022_Binary(DataType):

    def __init__(self, minLength: str, maxLength: str, length: str, pattern: str):
        self.minLength = minLength
        self.maxLength = maxLength
        self.length = length
        self.pattern = pattern
        
    @property
    def minLength(self) -> str:
        return self.__minLength

    @minLength.setter
    def minLength(self, minLength: str):
        self.__minLength = minLength

    @property
    def maxLength(self) -> str:
        return self.__maxLength

    @maxLength.setter
    def maxLength(self, maxLength: str):
        self.__maxLength = maxLength

    @property
    def length(self) -> str:
        return self.__length

    @length.setter
    def length(self, length: str):
        self.__length = length

    @property
    def pattern(self) -> str:
        return self.__pattern

    @pattern.setter
    def pattern(self, pattern: str):
        self.__pattern = pattern

class iso20022_String(DataType):

    def __init__(self, minLength: str, maxLength: str, length: str, pattern: str):
        self.minLength = minLength
        self.maxLength = maxLength
        self.length = length
        self.pattern = pattern
        
    @property
    def length(self) -> str:
        return self.__length

    @length.setter
    def length(self, length: str):
        self.__length = length

    @property
    def minLength(self) -> str:
        return self.__minLength

    @minLength.setter
    def minLength(self, minLength: str):
        self.__minLength = minLength

    @property
    def maxLength(self) -> str:
        return self.__maxLength

    @maxLength.setter
    def maxLength(self, maxLength: str):
        self.__maxLength = maxLength

    @property
    def pattern(self) -> str:
        return self.__pattern

    @pattern.setter
    def pattern(self, pattern: str):
        self.__pattern = pattern

class String:

    pass
class iso20022_CodeSet(String):

    def __init__(self, identificationScheme: str, owner208: set["iso20022_Code"] = None, CodeSet: "iso20022_Code" = None, CodeSet202: "iso20022_CodeSet" = None, derivation201: "iso20022_CodeSet" = None, CodeSet206: "iso20022_CodeSet" = None, trace205: set["iso20022_CodeSet"] = None):
        self.identificationScheme = identificationScheme
        self.owner208 = owner208 if owner208 is not None else set()
        self.CodeSet = CodeSet
        self.CodeSet202 = CodeSet202
        self.derivation201 = derivation201
        self.CodeSet206 = CodeSet206
        self.trace205 = trace205 if trace205 is not None else set()
        
    @property
    def identificationScheme(self) -> str:
        return self.__identificationScheme

    @identificationScheme.setter
    def identificationScheme(self, identificationScheme: str):
        self.__identificationScheme = identificationScheme

    @property
    def trace205(self):
        return self.__trace205

    @trace205.setter
    def trace205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_CodeSet__trace205", None)
        self.__trace205 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CodeSet206"):
                    opp_val = getattr(item, "CodeSet206", None)
                    
                    if opp_val == self:
                        setattr(item, "CodeSet206", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CodeSet206"):
                    opp_val = getattr(item, "CodeSet206", None)
                    
                    setattr(item, "CodeSet206", self)
                    

    @property
    def CodeSet202(self):
        return self.__CodeSet202

    @CodeSet202.setter
    def CodeSet202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_CodeSet__CodeSet202", None)
        self.__CodeSet202 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "derivation201"):
                opp_val = getattr(old_value, "derivation201", None)
                if opp_val == self:
                    setattr(old_value, "derivation201", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "derivation201"):
                opp_val = getattr(value, "derivation201", None)
                setattr(value, "derivation201", self)

    @property
    def derivation201(self):
        return self.__derivation201

    @derivation201.setter
    def derivation201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_CodeSet__derivation201", None)
        self.__derivation201 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CodeSet202"):
                opp_val = getattr(old_value, "CodeSet202", None)
                if opp_val == self:
                    setattr(old_value, "CodeSet202", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CodeSet202"):
                opp_val = getattr(value, "CodeSet202", None)
                setattr(value, "CodeSet202", self)

    @property
    def CodeSet206(self):
        return self.__CodeSet206

    @CodeSet206.setter
    def CodeSet206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_CodeSet__CodeSet206", None)
        self.__CodeSet206 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace205"):
                opp_val = getattr(old_value, "trace205", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace205"):
                opp_val = getattr(value, "trace205", None)
                if opp_val is None:
                    setattr(value, "trace205", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def owner208(self):
        return self.__owner208

    @owner208.setter
    def owner208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_CodeSet__owner208", None)
        self.__owner208 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Code"):
                    opp_val = getattr(item, "Code", None)
                    
                    if opp_val == self:
                        setattr(item, "Code", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Code"):
                    opp_val = getattr(item, "Code", None)
                    
                    setattr(item, "Code", self)
                    

    @property
    def CodeSet(self):
        return self.__CodeSet

    @CodeSet.setter
    def CodeSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_CodeSet__CodeSet", None)
        self.__CodeSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "code"):
                opp_val = getattr(old_value, "code", None)
                if opp_val == self:
                    setattr(old_value, "code", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "code"):
                opp_val = getattr(value, "code", None)
                setattr(value, "code", self)

class iso20022_IdentifierSet(String):

    def __init__(self, identificationScheme: str):
        self.identificationScheme = identificationScheme
        
    @property
    def identificationScheme(self) -> str:
        return self.__identificationScheme

    @identificationScheme.setter
    def identificationScheme(self, identificationScheme: str):
        self.__identificationScheme = identificationScheme

class iso20022_Text(String):

    pass
class Decimal:

    pass
class iso20022_Quantity(Decimal):

    def __init__(self, unitCode: str):
        self.unitCode = unitCode
        
    @property
    def unitCode(self) -> str:
        return self.__unitCode

    @unitCode.setter
    def unitCode(self, unitCode: str):
        self.__unitCode = unitCode

class iso20022_Amount(Decimal):

    pass
class iso20022_Rate(Decimal):

    def __init__(self, baseValue: str, baseUnitCode: str):
        self.baseValue = baseValue
        self.baseUnitCode = baseUnitCode
        
    @property
    def baseUnitCode(self) -> str:
        return self.__baseUnitCode

    @baseUnitCode.setter
    def baseUnitCode(self, baseUnitCode: str):
        self.__baseUnitCode = baseUnitCode

    @property
    def baseValue(self) -> str:
        return self.__baseValue

    @baseValue.setter
    def baseValue(self, baseValue: str):
        self.__baseValue = baseValue

class MessageElement:

    pass
class iso20022_MessageAttribute(MessageElement):

    def __init__(self, iso20022_MessageAttribute: "iso20022_DataType" = None, iso20022_MessageAttribute192: "iso20022_MessageComponentType" = None):
        self.iso20022_MessageAttribute = iso20022_MessageAttribute
        self.iso20022_MessageAttribute192 = iso20022_MessageAttribute192
        
    @property
    def iso20022_MessageAttribute192(self):
        return self.__iso20022_MessageAttribute192

    @iso20022_MessageAttribute192.setter
    def iso20022_MessageAttribute192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageAttribute__iso20022_MessageAttribute192", None)
        self.__iso20022_MessageAttribute192 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iso20022_MessageComponentType193"):
                opp_val = getattr(old_value, "iso20022_MessageComponentType193", None)
                if opp_val == self:
                    setattr(old_value, "iso20022_MessageComponentType193", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iso20022_MessageComponentType193"):
                opp_val = getattr(value, "iso20022_MessageComponentType193", None)
                setattr(value, "iso20022_MessageComponentType193", self)

    @property
    def iso20022_MessageAttribute(self):
        return self.__iso20022_MessageAttribute

    @iso20022_MessageAttribute.setter
    def iso20022_MessageAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageAttribute__iso20022_MessageAttribute", None)
        self.__iso20022_MessageAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iso20022_DataType190"):
                opp_val = getattr(old_value, "iso20022_DataType190", None)
                if opp_val == self:
                    setattr(old_value, "iso20022_DataType190", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iso20022_DataType190"):
                opp_val = getattr(value, "iso20022_DataType190", None)
                setattr(value, "iso20022_DataType190", self)

    def MessageAttributeHasExactlyOneType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement MessageAttributeHasExactlyOneType method
        pass

class iso20022_MessageAssociationEnd(MessageElement):

    def __init__(self, isComposite: bool, iso20022_MessageAssociationEnd: "iso20022_MessageComponentType" = None):
        self.isComposite = isComposite
        self.iso20022_MessageAssociationEnd = iso20022_MessageAssociationEnd
        
    @property
    def isComposite(self) -> bool:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: bool):
        self.__isComposite = isComposite

    @property
    def iso20022_MessageAssociationEnd(self):
        return self.__iso20022_MessageAssociationEnd

    @iso20022_MessageAssociationEnd.setter
    def iso20022_MessageAssociationEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageAssociationEnd__iso20022_MessageAssociationEnd", None)
        self.__iso20022_MessageAssociationEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iso20022_MessageComponentType"):
                opp_val = getattr(old_value, "iso20022_MessageComponentType", None)
                if opp_val == self:
                    setattr(old_value, "iso20022_MessageComponentType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iso20022_MessageComponentType"):
                opp_val = getattr(value, "iso20022_MessageComponentType", None)
                setattr(value, "iso20022_MessageComponentType", self)

class MessageElementContainer:

    pass
class iso20022_ChoiceComponent(MessageElementContainer):

    def __init__(self):
        
    def AtLeastOneProperty(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement AtLeastOneProperty method
        pass

class MessageComponentType:

    pass
class iso20022_UserDefined(MessageComponentType):

    def __init__(self, namespace: str, namespaceList: str, processContents: str):
        self.namespace = namespace
        self.namespaceList = namespaceList
        self.processContents = processContents
        
    @property
    def namespaceList(self) -> str:
        return self.__namespaceList

    @namespaceList.setter
    def namespaceList(self, namespaceList: str):
        self.__namespaceList = namespaceList

    @property
    def namespace(self) -> str:
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace

    @property
    def processContents(self) -> str:
        return self.__processContents

    @processContents.setter
    def processContents(self, processContents: str):
        self.__processContents = processContents

class iso20022_ExternalSchema(MessageComponentType):

    def __init__(self, namespaceList: str, processContent: str):
        self.namespaceList = namespaceList
        self.processContent = processContent
        
    @property
    def namespaceList(self) -> str:
        return self.__namespaceList

    @namespaceList.setter
    def namespaceList(self, namespaceList: str):
        self.__namespaceList = namespaceList

    @property
    def processContent(self) -> str:
        return self.__processContent

    @processContent.setter
    def processContent(self, processContent: str):
        self.__processContent = processContent

class BusinessElement:

    pass
class iso20022_BusinessAttribute(BusinessElement):

    def __init__(self, iso20022_BusinessAttribute: "iso20022_DataType" = None, iso20022_BusinessAttribute197: "iso20022_BusinessComponent" = None):
        self.iso20022_BusinessAttribute = iso20022_BusinessAttribute
        self.iso20022_BusinessAttribute197 = iso20022_BusinessAttribute197
        
    @property
    def iso20022_BusinessAttribute(self):
        return self.__iso20022_BusinessAttribute

    @iso20022_BusinessAttribute.setter
    def iso20022_BusinessAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessAttribute__iso20022_BusinessAttribute", None)
        self.__iso20022_BusinessAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iso20022_DataType195"):
                opp_val = getattr(old_value, "iso20022_DataType195", None)
                if opp_val == self:
                    setattr(old_value, "iso20022_DataType195", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iso20022_DataType195"):
                opp_val = getattr(value, "iso20022_DataType195", None)
                setattr(value, "iso20022_DataType195", self)

    @property
    def iso20022_BusinessAttribute197(self):
        return self.__iso20022_BusinessAttribute197

    @iso20022_BusinessAttribute197.setter
    def iso20022_BusinessAttribute197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessAttribute__iso20022_BusinessAttribute197", None)
        self.__iso20022_BusinessAttribute197 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iso20022_BusinessComponent"):
                opp_val = getattr(old_value, "iso20022_BusinessComponent", None)
                if opp_val == self:
                    setattr(old_value, "iso20022_BusinessComponent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iso20022_BusinessComponent"):
                opp_val = getattr(value, "iso20022_BusinessComponent", None)
                setattr(value, "iso20022_BusinessComponent", self)

    def BusinessAttributeHasExactlyOneType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement BusinessAttributeHasExactlyOneType method
        pass

    def NoDerivingCodeSetType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement NoDerivingCodeSetType method
        pass

class LogicalType:

    pass
class iso20022_BusinessAssociationEnd(BusinessElement):

    def __init__(self, aggregation: str, BusinessAssociationEnd: "iso20022_BusinessComponent" = None, iso20022_BusinessAssociationEnd: "iso20022_BusinessAssociationEnd" = None, iso20022_BusinessAssociationEnd112: "iso20022_BusinessAssociationEnd" = None, associationDomain: "iso20022_BusinessComponent" = None):
        self.aggregation = aggregation
        self.BusinessAssociationEnd = BusinessAssociationEnd
        self.iso20022_BusinessAssociationEnd = iso20022_BusinessAssociationEnd
        self.iso20022_BusinessAssociationEnd112 = iso20022_BusinessAssociationEnd112
        self.associationDomain = associationDomain
        
    @property
    def aggregation(self) -> str:
        return self.__aggregation

    @aggregation.setter
    def aggregation(self, aggregation: str):
        self.__aggregation = aggregation

    @property
    def associationDomain(self):
        return self.__associationDomain

    @associationDomain.setter
    def associationDomain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessAssociationEnd__associationDomain", None)
        self.__associationDomain = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BusinessComponent115"):
                opp_val = getattr(old_value, "BusinessComponent115", None)
                if opp_val == self:
                    setattr(old_value, "BusinessComponent115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BusinessComponent115"):
                opp_val = getattr(value, "BusinessComponent115", None)
                setattr(value, "BusinessComponent115", self)

    @property
    def BusinessAssociationEnd(self):
        return self.__BusinessAssociationEnd

    @BusinessAssociationEnd.setter
    def BusinessAssociationEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessAssociationEnd__BusinessAssociationEnd", None)
        self.__BusinessAssociationEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type"):
                opp_val = getattr(old_value, "type", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type"):
                opp_val = getattr(value, "type", None)
                if opp_val is None:
                    setattr(value, "type", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iso20022_BusinessAssociationEnd(self):
        return self.__iso20022_BusinessAssociationEnd

    @iso20022_BusinessAssociationEnd.setter
    def iso20022_BusinessAssociationEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessAssociationEnd__iso20022_BusinessAssociationEnd", None)
        self.__iso20022_BusinessAssociationEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iso20022_BusinessAssociationEnd112"):
                opp_val = getattr(old_value, "iso20022_BusinessAssociationEnd112", None)
                if opp_val == self:
                    setattr(old_value, "iso20022_BusinessAssociationEnd112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iso20022_BusinessAssociationEnd112"):
                opp_val = getattr(value, "iso20022_BusinessAssociationEnd112", None)
                setattr(value, "iso20022_BusinessAssociationEnd112", self)

    @property
    def iso20022_BusinessAssociationEnd112(self):
        return self.__iso20022_BusinessAssociationEnd112

    @iso20022_BusinessAssociationEnd112.setter
    def iso20022_BusinessAssociationEnd112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessAssociationEnd__iso20022_BusinessAssociationEnd112", None)
        self.__iso20022_BusinessAssociationEnd112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iso20022_BusinessAssociationEnd"):
                opp_val = getattr(old_value, "iso20022_BusinessAssociationEnd", None)
                if opp_val == self:
                    setattr(old_value, "iso20022_BusinessAssociationEnd", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iso20022_BusinessAssociationEnd"):
                opp_val = getattr(value, "iso20022_BusinessAssociationEnd", None)
                setattr(value, "iso20022_BusinessAssociationEnd", self)

    def AtMostOneAggregatedEnd(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement AtMostOneAggregatedEnd method
        pass

    def ContextConsistentWithType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement ContextConsistentWithType method
        pass

class BusinessConcept:

    pass
class BusinessElementType:

    pass
class TopLevelDictionaryEntry:

    pass
class iso20022_EndPointCategory(TopLevelDictionaryEntry):

    pass
class iso20022_DataType(BusinessElementType, TopLevelDictionaryEntry, LogicalType):

    pass
class iso20022_MultiplicityEntity(ABC):

    def __init__(self, maxOccurs: str, minOccurs: str):
        self.maxOccurs = maxOccurs
        self.minOccurs = minOccurs
        
    @property
    def maxOccurs(self) -> str:
        return self.__maxOccurs

    @maxOccurs.setter
    def maxOccurs(self, maxOccurs: str):
        self.__maxOccurs = maxOccurs

    @property
    def minOccurs(self) -> str:
        return self.__minOccurs

    @minOccurs.setter
    def minOccurs(self, minOccurs: str):
        self.__minOccurs = minOccurs

class MultiplicityEntity:

    pass
class Construct:

    pass
class iso20022_MessageConstruct(Construct):

    def __init__(self, xmlTag: str, iso20022_MessageConstruct: "iso20022_LogicalType" = None):
        self.xmlTag = xmlTag
        self.iso20022_MessageConstruct = iso20022_MessageConstruct
        
    @property
    def xmlTag(self) -> str:
        return self.__xmlTag

    @xmlTag.setter
    def xmlTag(self, xmlTag: str):
        self.__xmlTag = xmlTag

    @property
    def iso20022_MessageConstruct(self):
        return self.__iso20022_MessageConstruct

    @iso20022_MessageConstruct.setter
    def iso20022_MessageConstruct(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageConstruct__iso20022_MessageConstruct", None)
        self.__iso20022_MessageConstruct = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iso20022_LogicalType"):
                opp_val = getattr(old_value, "iso20022_LogicalType", None)
                if opp_val == self:
                    setattr(old_value, "iso20022_LogicalType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iso20022_LogicalType"):
                opp_val = getattr(value, "iso20022_LogicalType", None)
                setattr(value, "iso20022_LogicalType", self)

class iso20022_MessageElementContainer(MessageComponentType):

    def __init__(self, MessageElementContainer: "iso20022_MessageElement" = None, componentContext: set["iso20022_MessageElement"] = None, iso20022_MessageElementContainer: "iso20022_EndPointCategory" = None):
        self.MessageElementContainer = MessageElementContainer
        self.componentContext = componentContext if componentContext is not None else set()
        self.iso20022_MessageElementContainer = iso20022_MessageElementContainer
        
    @property
    def MessageElementContainer(self):
        return self.__MessageElementContainer

    @MessageElementContainer.setter
    def MessageElementContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageElementContainer__MessageElementContainer", None)
        self.__MessageElementContainer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "messageElement"):
                opp_val = getattr(old_value, "messageElement", None)
                if opp_val == self:
                    setattr(old_value, "messageElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "messageElement"):
                opp_val = getattr(value, "messageElement", None)
                setattr(value, "messageElement", self)

    @property
    def iso20022_MessageElementContainer(self):
        return self.__iso20022_MessageElementContainer

    @iso20022_MessageElementContainer.setter
    def iso20022_MessageElementContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageElementContainer__iso20022_MessageElementContainer", None)
        self.__iso20022_MessageElementContainer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iso20022_EndPointCategory"):
                opp_val = getattr(old_value, "iso20022_EndPointCategory", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iso20022_EndPointCategory"):
                opp_val = getattr(value, "iso20022_EndPointCategory", None)
                if opp_val is None:
                    setattr(value, "iso20022_EndPointCategory", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def componentContext(self):
        return self.__componentContext

    @componentContext.setter
    def componentContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageElementContainer__componentContext", None)
        self.__componentContext = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MessageElement117"):
                    opp_val = getattr(item, "MessageElement117", None)
                    
                    if opp_val == self:
                        setattr(item, "MessageElement117", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MessageElement117"):
                    opp_val = getattr(item, "MessageElement117", None)
                    
                    setattr(item, "MessageElement117", self)
                    

    def technicalElement(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement technicalElement method
        pass

    def MessageElementsHaveUniqueNames(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement MessageElementsHaveUniqueNames method
        pass

class iso20022_BusinessElement(Construct, BusinessConcept):

    def __init__(self, isDerived: bool, BusinessElement: "iso20022_MessageElement" = None, BusinessElement96: "iso20022_BusinessComponent" = None, element: "iso20022_BusinessComponent" = None, businessElementTrace: set["iso20022_MessageElement"] = None, iso20022_BusinessElement: "iso20022_BusinessElementType" = None):
        self.isDerived = isDerived
        self.BusinessElement = BusinessElement
        self.BusinessElement96 = BusinessElement96
        self.element = element
        self.businessElementTrace = businessElementTrace if businessElementTrace is not None else set()
        self.iso20022_BusinessElement = iso20022_BusinessElement
        
    @property
    def isDerived(self) -> bool:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: bool):
        self.__isDerived = isDerived

    @property
    def BusinessElement(self):
        return self.__BusinessElement

    @BusinessElement.setter
    def BusinessElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessElement__BusinessElement", None)
        self.__BusinessElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "derivation85"):
                opp_val = getattr(old_value, "derivation85", None)
                if opp_val == self:
                    setattr(old_value, "derivation85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "derivation85"):
                opp_val = getattr(value, "derivation85", None)
                setattr(value, "derivation85", self)

    @property
    def businessElementTrace(self):
        return self.__businessElementTrace

    @businessElementTrace.setter
    def businessElementTrace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessElement__businessElementTrace", None)
        self.__businessElementTrace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MessageElement101"):
                    opp_val = getattr(item, "MessageElement101", None)
                    
                    if opp_val == self:
                        setattr(item, "MessageElement101", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MessageElement101"):
                    opp_val = getattr(item, "MessageElement101", None)
                    
                    setattr(item, "MessageElement101", self)
                    

    @property
    def element(self):
        return self.__element

    @element.setter
    def element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessElement__element", None)
        self.__element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BusinessComponent104"):
                opp_val = getattr(old_value, "BusinessComponent104", None)
                if opp_val == self:
                    setattr(old_value, "BusinessComponent104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BusinessComponent104"):
                opp_val = getattr(value, "BusinessComponent104", None)
                setattr(value, "BusinessComponent104", self)

    @property
    def iso20022_BusinessElement(self):
        return self.__iso20022_BusinessElement

    @iso20022_BusinessElement.setter
    def iso20022_BusinessElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessElement__iso20022_BusinessElement", None)
        self.__iso20022_BusinessElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iso20022_BusinessElementType"):
                opp_val = getattr(old_value, "iso20022_BusinessElementType", None)
                if opp_val == self:
                    setattr(old_value, "iso20022_BusinessElementType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iso20022_BusinessElementType"):
                opp_val = getattr(value, "iso20022_BusinessElementType", None)
                setattr(value, "iso20022_BusinessElementType", self)

    @property
    def BusinessElement96(self):
        return self.__BusinessElement96

    @BusinessElement96.setter
    def BusinessElement96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessElement__BusinessElement96", None)
        self.__BusinessElement96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elementContext"):
                opp_val = getattr(old_value, "elementContext", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elementContext"):
                opp_val = getattr(value, "elementContext", None)
                if opp_val is None:
                    setattr(value, "elementContext", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class iso20022_BusinessComponent(TopLevelDictionaryEntry, BusinessConcept, BusinessElementType):

    def __init__(self, BusinessComponent: "iso20022_MessageElement" = None, BusinessComponent91: "iso20022_BusinessComponent" = None, superType: set["iso20022_BusinessComponent"] = None, BusinessComponent94: "iso20022_BusinessComponent" = None, subType: "iso20022_BusinessComponent" = None, elementContext: set["iso20022_BusinessElement"] = None, trace: set["iso20022_MessageComponentType"] = None, type: set["iso20022_BusinessAssociationEnd"] = None, businessComponentTrace: set["iso20022_MessageElement"] = None, BusinessComponent104: "iso20022_BusinessElement" = None, BusinessComponent107: "iso20022_MessageComponentType" = None, BusinessComponent115: "iso20022_BusinessAssociationEnd" = None, iso20022_BusinessComponent: "iso20022_BusinessAttribute" = None):
        self.BusinessComponent = BusinessComponent
        self.BusinessComponent91 = BusinessComponent91
        self.superType = superType if superType is not None else set()
        self.BusinessComponent94 = BusinessComponent94
        self.subType = subType
        self.elementContext = elementContext if elementContext is not None else set()
        self.trace = trace if trace is not None else set()
        self.type = type if type is not None else set()
        self.businessComponentTrace = businessComponentTrace if businessComponentTrace is not None else set()
        self.BusinessComponent104 = BusinessComponent104
        self.BusinessComponent107 = BusinessComponent107
        self.BusinessComponent115 = BusinessComponent115
        self.iso20022_BusinessComponent = iso20022_BusinessComponent
        
    @property
    def trace(self):
        return self.__trace

    @trace.setter
    def trace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessComponent__trace", None)
        self.__trace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MessageComponentType"):
                    opp_val = getattr(item, "MessageComponentType", None)
                    
                    if opp_val == self:
                        setattr(item, "MessageComponentType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MessageComponentType"):
                    opp_val = getattr(item, "MessageComponentType", None)
                    
                    setattr(item, "MessageComponentType", self)
                    

    @property
    def elementContext(self):
        return self.__elementContext

    @elementContext.setter
    def elementContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessComponent__elementContext", None)
        self.__elementContext = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BusinessElement96"):
                    opp_val = getattr(item, "BusinessElement96", None)
                    
                    if opp_val == self:
                        setattr(item, "BusinessElement96", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BusinessElement96"):
                    opp_val = getattr(item, "BusinessElement96", None)
                    
                    setattr(item, "BusinessElement96", self)
                    

    @property
    def BusinessComponent94(self):
        return self.__BusinessComponent94

    @BusinessComponent94.setter
    def BusinessComponent94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessComponent__BusinessComponent94", None)
        self.__BusinessComponent94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subType"):
                opp_val = getattr(old_value, "subType", None)
                if opp_val == self:
                    setattr(old_value, "subType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subType"):
                opp_val = getattr(value, "subType", None)
                setattr(value, "subType", self)

    @property
    def superType(self):
        return self.__superType

    @superType.setter
    def superType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessComponent__superType", None)
        self.__superType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BusinessComponent91"):
                    opp_val = getattr(item, "BusinessComponent91", None)
                    
                    if opp_val == self:
                        setattr(item, "BusinessComponent91", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BusinessComponent91"):
                    opp_val = getattr(item, "BusinessComponent91", None)
                    
                    setattr(item, "BusinessComponent91", self)
                    

    @property
    def BusinessComponent115(self):
        return self.__BusinessComponent115

    @BusinessComponent115.setter
    def BusinessComponent115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessComponent__BusinessComponent115", None)
        self.__BusinessComponent115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "associationDomain"):
                opp_val = getattr(old_value, "associationDomain", None)
                if opp_val == self:
                    setattr(old_value, "associationDomain", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "associationDomain"):
                opp_val = getattr(value, "associationDomain", None)
                setattr(value, "associationDomain", self)

    @property
    def subType(self):
        return self.__subType

    @subType.setter
    def subType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessComponent__subType", None)
        self.__subType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BusinessComponent94"):
                opp_val = getattr(old_value, "BusinessComponent94", None)
                if opp_val == self:
                    setattr(old_value, "BusinessComponent94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BusinessComponent94"):
                opp_val = getattr(value, "BusinessComponent94", None)
                setattr(value, "BusinessComponent94", self)

    @property
    def BusinessComponent91(self):
        return self.__BusinessComponent91

    @BusinessComponent91.setter
    def BusinessComponent91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessComponent__BusinessComponent91", None)
        self.__BusinessComponent91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "superType"):
                opp_val = getattr(old_value, "superType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "superType"):
                opp_val = getattr(value, "superType", None)
                if opp_val is None:
                    setattr(value, "superType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BusinessComponent(self):
        return self.__BusinessComponent

    @BusinessComponent.setter
    def BusinessComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessComponent__BusinessComponent", None)
        self.__BusinessComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "derivationElement"):
                opp_val = getattr(old_value, "derivationElement", None)
                if opp_val == self:
                    setattr(old_value, "derivationElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "derivationElement"):
                opp_val = getattr(value, "derivationElement", None)
                setattr(value, "derivationElement", self)

    @property
    def BusinessComponent104(self):
        return self.__BusinessComponent104

    @BusinessComponent104.setter
    def BusinessComponent104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessComponent__BusinessComponent104", None)
        self.__BusinessComponent104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "element"):
                opp_val = getattr(old_value, "element", None)
                if opp_val == self:
                    setattr(old_value, "element", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "element"):
                opp_val = getattr(value, "element", None)
                setattr(value, "element", self)

    @property
    def iso20022_BusinessComponent(self):
        return self.__iso20022_BusinessComponent

    @iso20022_BusinessComponent.setter
    def iso20022_BusinessComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessComponent__iso20022_BusinessComponent", None)
        self.__iso20022_BusinessComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iso20022_BusinessAttribute197"):
                opp_val = getattr(old_value, "iso20022_BusinessAttribute197", None)
                if opp_val == self:
                    setattr(old_value, "iso20022_BusinessAttribute197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iso20022_BusinessAttribute197"):
                opp_val = getattr(value, "iso20022_BusinessAttribute197", None)
                setattr(value, "iso20022_BusinessAttribute197", self)

    @property
    def BusinessComponent107(self):
        return self.__BusinessComponent107

    @BusinessComponent107.setter
    def BusinessComponent107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessComponent__BusinessComponent107", None)
        self.__BusinessComponent107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "derivationComponent"):
                opp_val = getattr(old_value, "derivationComponent", None)
                if opp_val == self:
                    setattr(old_value, "derivationComponent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "derivationComponent"):
                opp_val = getattr(value, "derivationComponent", None)
                setattr(value, "derivationComponent", self)

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessComponent__type", None)
        self.__type = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BusinessAssociationEnd"):
                    opp_val = getattr(item, "BusinessAssociationEnd", None)
                    
                    if opp_val == self:
                        setattr(item, "BusinessAssociationEnd", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BusinessAssociationEnd"):
                    opp_val = getattr(item, "BusinessAssociationEnd", None)
                    
                    setattr(item, "BusinessAssociationEnd", self)
                    

    @property
    def businessComponentTrace(self):
        return self.__businessComponentTrace

    @businessComponentTrace.setter
    def businessComponentTrace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessComponent__businessComponentTrace", None)
        self.__businessComponentTrace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MessageElement"):
                    opp_val = getattr(item, "MessageElement", None)
                    
                    if opp_val == self:
                        setattr(item, "MessageElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MessageElement"):
                    opp_val = getattr(item, "MessageElement", None)
                    
                    setattr(item, "MessageElement", self)
                    

    def BusinessElementsHaveUniqueNames(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement BusinessElementsHaveUniqueNames method
        pass

class MessageConcept:

    pass
class iso20022_MessageComponentType(TopLevelDictionaryEntry, MessageConcept, LogicalType):

    def __init__(self, isTechnical: bool, MessageComponentType: "iso20022_BusinessComponent" = None, complexType: set["iso20022_MessageBuildingBlock"] = None, derivationComponent: "iso20022_BusinessComponent" = None, MessageComponentType111: "iso20022_MessageBuildingBlock" = None, iso20022_MessageComponentType: "iso20022_MessageAssociationEnd" = None, iso20022_MessageComponentType193: "iso20022_MessageAttribute" = None):
        self.isTechnical = isTechnical
        self.MessageComponentType = MessageComponentType
        self.complexType = complexType if complexType is not None else set()
        self.derivationComponent = derivationComponent
        self.MessageComponentType111 = MessageComponentType111
        self.iso20022_MessageComponentType = iso20022_MessageComponentType
        self.iso20022_MessageComponentType193 = iso20022_MessageComponentType193
        
    @property
    def isTechnical(self) -> bool:
        return self.__isTechnical

    @isTechnical.setter
    def isTechnical(self, isTechnical: bool):
        self.__isTechnical = isTechnical

    @property
    def iso20022_MessageComponentType(self):
        return self.__iso20022_MessageComponentType

    @iso20022_MessageComponentType.setter
    def iso20022_MessageComponentType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageComponentType__iso20022_MessageComponentType", None)
        self.__iso20022_MessageComponentType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iso20022_MessageAssociationEnd"):
                opp_val = getattr(old_value, "iso20022_MessageAssociationEnd", None)
                if opp_val == self:
                    setattr(old_value, "iso20022_MessageAssociationEnd", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iso20022_MessageAssociationEnd"):
                opp_val = getattr(value, "iso20022_MessageAssociationEnd", None)
                setattr(value, "iso20022_MessageAssociationEnd", self)

    @property
    def MessageComponentType111(self):
        return self.__MessageComponentType111

    @MessageComponentType111.setter
    def MessageComponentType111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageComponentType__MessageComponentType111", None)
        self.__MessageComponentType111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "messageBuildingBlock"):
                opp_val = getattr(old_value, "messageBuildingBlock", None)
                if opp_val == self:
                    setattr(old_value, "messageBuildingBlock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "messageBuildingBlock"):
                opp_val = getattr(value, "messageBuildingBlock", None)
                setattr(value, "messageBuildingBlock", self)

    @property
    def iso20022_MessageComponentType193(self):
        return self.__iso20022_MessageComponentType193

    @iso20022_MessageComponentType193.setter
    def iso20022_MessageComponentType193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageComponentType__iso20022_MessageComponentType193", None)
        self.__iso20022_MessageComponentType193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iso20022_MessageAttribute192"):
                opp_val = getattr(old_value, "iso20022_MessageAttribute192", None)
                if opp_val == self:
                    setattr(old_value, "iso20022_MessageAttribute192", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iso20022_MessageAttribute192"):
                opp_val = getattr(value, "iso20022_MessageAttribute192", None)
                setattr(value, "iso20022_MessageAttribute192", self)

    @property
    def MessageComponentType(self):
        return self.__MessageComponentType

    @MessageComponentType.setter
    def MessageComponentType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageComponentType__MessageComponentType", None)
        self.__MessageComponentType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace"):
                opp_val = getattr(old_value, "trace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace"):
                opp_val = getattr(value, "trace", None)
                if opp_val is None:
                    setattr(value, "trace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def complexType(self):
        return self.__complexType

    @complexType.setter
    def complexType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageComponentType__complexType", None)
        self.__complexType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MessageBuildingBlock"):
                    opp_val = getattr(item, "MessageBuildingBlock", None)
                    
                    if opp_val == self:
                        setattr(item, "MessageBuildingBlock", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MessageBuildingBlock"):
                    opp_val = getattr(item, "MessageBuildingBlock", None)
                    
                    setattr(item, "MessageBuildingBlock", self)
                    

    @property
    def derivationComponent(self):
        return self.__derivationComponent

    @derivationComponent.setter
    def derivationComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageComponentType__derivationComponent", None)
        self.__derivationComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BusinessComponent107"):
                opp_val = getattr(old_value, "BusinessComponent107", None)
                if opp_val == self:
                    setattr(old_value, "BusinessComponent107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BusinessComponent107"):
                opp_val = getattr(value, "BusinessComponent107", None)
                setattr(value, "BusinessComponent107", self)

class MessageConstruct:

    pass
class iso20022_MessageComponent(MessageElementContainer):

    pass
class iso20022_MessageElement(MessageConstruct, MessageConcept):

    def __init__(self, isTechnical: bool, isDerived: bool, iso20022_MessageElement: "iso20022_Xor" = None, derivationElement: "iso20022_BusinessComponent" = None, derivation85: "iso20022_BusinessElement" = None, messageElement: "iso20022_MessageElementContainer" = None, MessageElement: "iso20022_BusinessComponent" = None, MessageElement101: "iso20022_BusinessElement" = None, MessageElement117: "iso20022_MessageElementContainer" = None):
        self.isTechnical = isTechnical
        self.isDerived = isDerived
        self.iso20022_MessageElement = iso20022_MessageElement
        self.derivationElement = derivationElement
        self.derivation85 = derivation85
        self.messageElement = messageElement
        self.MessageElement = MessageElement
        self.MessageElement101 = MessageElement101
        self.MessageElement117 = MessageElement117
        
    @property
    def isTechnical(self) -> bool:
        return self.__isTechnical

    @isTechnical.setter
    def isTechnical(self, isTechnical: bool):
        self.__isTechnical = isTechnical

    @property
    def isDerived(self) -> bool:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: bool):
        self.__isDerived = isDerived

    @property
    def MessageElement117(self):
        return self.__MessageElement117

    @MessageElement117.setter
    def MessageElement117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageElement__MessageElement117", None)
        self.__MessageElement117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentContext"):
                opp_val = getattr(old_value, "componentContext", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentContext"):
                opp_val = getattr(value, "componentContext", None)
                if opp_val is None:
                    setattr(value, "componentContext", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def messageElement(self):
        return self.__messageElement

    @messageElement.setter
    def messageElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageElement__messageElement", None)
        self.__messageElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MessageElementContainer"):
                opp_val = getattr(old_value, "MessageElementContainer", None)
                if opp_val == self:
                    setattr(old_value, "MessageElementContainer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MessageElementContainer"):
                opp_val = getattr(value, "MessageElementContainer", None)
                setattr(value, "MessageElementContainer", self)

    @property
    def derivation85(self):
        return self.__derivation85

    @derivation85.setter
    def derivation85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageElement__derivation85", None)
        self.__derivation85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BusinessElement"):
                opp_val = getattr(old_value, "BusinessElement", None)
                if opp_val == self:
                    setattr(old_value, "BusinessElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BusinessElement"):
                opp_val = getattr(value, "BusinessElement", None)
                setattr(value, "BusinessElement", self)

    @property
    def MessageElement(self):
        return self.__MessageElement

    @MessageElement.setter
    def MessageElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageElement__MessageElement", None)
        self.__MessageElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "businessComponentTrace"):
                opp_val = getattr(old_value, "businessComponentTrace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "businessComponentTrace"):
                opp_val = getattr(value, "businessComponentTrace", None)
                if opp_val is None:
                    setattr(value, "businessComponentTrace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MessageElement101(self):
        return self.__MessageElement101

    @MessageElement101.setter
    def MessageElement101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageElement__MessageElement101", None)
        self.__MessageElement101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "businessElementTrace"):
                opp_val = getattr(old_value, "businessElementTrace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "businessElementTrace"):
                opp_val = getattr(value, "businessElementTrace", None)
                if opp_val is None:
                    setattr(value, "businessElementTrace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def derivationElement(self):
        return self.__derivationElement

    @derivationElement.setter
    def derivationElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageElement__derivationElement", None)
        self.__derivationElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BusinessComponent"):
                opp_val = getattr(old_value, "BusinessComponent", None)
                if opp_val == self:
                    setattr(old_value, "BusinessComponent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BusinessComponent"):
                opp_val = getattr(value, "BusinessComponent", None)
                setattr(value, "BusinessComponent", self)

    @property
    def iso20022_MessageElement(self):
        return self.__iso20022_MessageElement

    @iso20022_MessageElement.setter
    def iso20022_MessageElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageElement__iso20022_MessageElement", None)
        self.__iso20022_MessageElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iso20022_Xor"):
                opp_val = getattr(old_value, "iso20022_Xor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iso20022_Xor"):
                opp_val = getattr(value, "iso20022_Xor", None)
                if opp_val is None:
                    setattr(value, "iso20022_Xor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def CardinalityAlignment(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement CardinalityAlignment method
        pass

    def NoMoreThanOneTrace(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement NoMoreThanOneTrace method
        pass

class iso20022_MessageBuildingBlock(MessageConstruct):

    def __init__(self, iso20022_MessageBuildingBlock: "iso20022_MessageDefinition" = None, iso20022_MessageBuildingBlock79: "iso20022_Xor" = None, MessageBuildingBlock: "iso20022_MessageComponentType" = None, iso20022_MessageBuildingBlock109: "iso20022_DataType" = None, messageBuildingBlock: "iso20022_MessageComponentType" = None):
        self.iso20022_MessageBuildingBlock = iso20022_MessageBuildingBlock
        self.iso20022_MessageBuildingBlock79 = iso20022_MessageBuildingBlock79
        self.MessageBuildingBlock = MessageBuildingBlock
        self.iso20022_MessageBuildingBlock109 = iso20022_MessageBuildingBlock109
        self.messageBuildingBlock = messageBuildingBlock
        
    @property
    def iso20022_MessageBuildingBlock79(self):
        return self.__iso20022_MessageBuildingBlock79

    @iso20022_MessageBuildingBlock79.setter
    def iso20022_MessageBuildingBlock79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageBuildingBlock__iso20022_MessageBuildingBlock79", None)
        self.__iso20022_MessageBuildingBlock79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iso20022_Xor78"):
                opp_val = getattr(old_value, "iso20022_Xor78", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iso20022_Xor78"):
                opp_val = getattr(value, "iso20022_Xor78", None)
                if opp_val is None:
                    setattr(value, "iso20022_Xor78", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MessageBuildingBlock(self):
        return self.__MessageBuildingBlock

    @MessageBuildingBlock.setter
    def MessageBuildingBlock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageBuildingBlock__MessageBuildingBlock", None)
        self.__MessageBuildingBlock = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "complexType"):
                opp_val = getattr(old_value, "complexType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "complexType"):
                opp_val = getattr(value, "complexType", None)
                if opp_val is None:
                    setattr(value, "complexType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iso20022_MessageBuildingBlock109(self):
        return self.__iso20022_MessageBuildingBlock109

    @iso20022_MessageBuildingBlock109.setter
    def iso20022_MessageBuildingBlock109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageBuildingBlock__iso20022_MessageBuildingBlock109", None)
        self.__iso20022_MessageBuildingBlock109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iso20022_DataType"):
                opp_val = getattr(old_value, "iso20022_DataType", None)
                if opp_val == self:
                    setattr(old_value, "iso20022_DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iso20022_DataType"):
                opp_val = getattr(value, "iso20022_DataType", None)
                setattr(value, "iso20022_DataType", self)

    @property
    def messageBuildingBlock(self):
        return self.__messageBuildingBlock

    @messageBuildingBlock.setter
    def messageBuildingBlock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageBuildingBlock__messageBuildingBlock", None)
        self.__messageBuildingBlock = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MessageComponentType111"):
                opp_val = getattr(old_value, "MessageComponentType111", None)
                if opp_val == self:
                    setattr(old_value, "MessageComponentType111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MessageComponentType111"):
                opp_val = getattr(value, "MessageComponentType111", None)
                setattr(value, "MessageComponentType111", self)

    @property
    def iso20022_MessageBuildingBlock(self):
        return self.__iso20022_MessageBuildingBlock

    @iso20022_MessageBuildingBlock.setter
    def iso20022_MessageBuildingBlock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageBuildingBlock__iso20022_MessageBuildingBlock", None)
        self.__iso20022_MessageBuildingBlock = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iso20022_MessageDefinition"):
                opp_val = getattr(old_value, "iso20022_MessageDefinition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iso20022_MessageDefinition"):
                opp_val = getattr(value, "iso20022_MessageDefinition", None)
                if opp_val is None:
                    setattr(value, "iso20022_MessageDefinition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def MessageBuildingBlockHasExactlyOneType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement MessageBuildingBlockHasExactlyOneType method
        pass

class RepositoryType:

    pass
class iso20022_LogicalType(RepositoryType):

    pass
class iso20022_BusinessElementType(RepositoryType):

    pass
class RepositoryConcept:

    pass
class iso20022_Code(RepositoryConcept):

    def __init__(self, codeName: str, Code: "iso20022_CodeSet" = None, code: "iso20022_CodeSet" = None):
        self.codeName = codeName
        self.Code = Code
        self.code = code
        
    @property
    def codeName(self) -> str:
        return self.__codeName

    @codeName.setter
    def codeName(self, codeName: str):
        self.__codeName = codeName

    @property
    def Code(self):
        return self.__Code

    @Code.setter
    def Code(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_Code__Code", None)
        self.__Code = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner208"):
                opp_val = getattr(old_value, "owner208", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner208"):
                opp_val = getattr(value, "owner208", None)
                if opp_val is None:
                    setattr(value, "owner208", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_Code__code", None)
        self.__code = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CodeSet"):
                opp_val = getattr(old_value, "CodeSet", None)
                if opp_val == self:
                    setattr(old_value, "CodeSet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CodeSet"):
                opp_val = getattr(value, "CodeSet", None)
                setattr(value, "CodeSet", self)

class iso20022_Constraint(RepositoryConcept):

    def __init__(self, expression: str, expressionLanguage: str, Constraint: "iso20022_RepositoryConcept" = None, constraint: "iso20022_RepositoryConcept" = None):
        self.expression = expression
        self.expressionLanguage = expressionLanguage
        self.Constraint = Constraint
        self.constraint = constraint
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def expressionLanguage(self) -> str:
        return self.__expressionLanguage

    @expressionLanguage.setter
    def expressionLanguage(self, expressionLanguage: str):
        self.__expressionLanguage = expressionLanguage

    @property
    def constraint(self):
        return self.__constraint

    @constraint.setter
    def constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_Constraint__constraint", None)
        self.__constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RepositoryConcept"):
                opp_val = getattr(old_value, "RepositoryConcept", None)
                if opp_val == self:
                    setattr(old_value, "RepositoryConcept", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RepositoryConcept"):
                opp_val = getattr(value, "RepositoryConcept", None)
                setattr(value, "RepositoryConcept", self)

    @property
    def Constraint(self):
        return self.__Constraint

    @Constraint.setter
    def Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_Constraint__Constraint", None)
        self.__Constraint = value
        
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

class iso20022_Construct(MultiplicityEntity, RepositoryConcept):

    pass
class iso20022_TopLevelDictionaryEntry(RepositoryConcept):

    pass
class iso20022_Participant(MultiplicityEntity, RepositoryConcept):

    pass
class iso20022_RepositoryType(RepositoryConcept):

    pass
class iso20022_Xor(RepositoryConcept):

    pass
class iso20022_MessageTransmission(RepositoryConcept):

    def __init__(self, messageTypeDescription: str, MessageTransmission: "iso20022_MessageDefinition" = None, MessageTransmission128: "iso20022_BusinessTransaction" = None, MessageTransmission169: "iso20022_Receive" = None, transmission: "iso20022_BusinessTransaction" = None, trace175: set["iso20022_MessageDefinition"] = None, messageTransmission: "iso20022_Send" = None, messageTransmission180: set["iso20022_Receive"] = None, MessageTransmission185: "iso20022_Send" = None):
        self.messageTypeDescription = messageTypeDescription
        self.MessageTransmission = MessageTransmission
        self.MessageTransmission128 = MessageTransmission128
        self.MessageTransmission169 = MessageTransmission169
        self.transmission = transmission
        self.trace175 = trace175 if trace175 is not None else set()
        self.messageTransmission = messageTransmission
        self.messageTransmission180 = messageTransmission180 if messageTransmission180 is not None else set()
        self.MessageTransmission185 = MessageTransmission185
        
    @property
    def messageTypeDescription(self) -> str:
        return self.__messageTypeDescription

    @messageTypeDescription.setter
    def messageTypeDescription(self, messageTypeDescription: str):
        self.__messageTypeDescription = messageTypeDescription

    @property
    def messageTransmission(self):
        return self.__messageTransmission

    @messageTransmission.setter
    def messageTransmission(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageTransmission__messageTransmission", None)
        self.__messageTransmission = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Send178"):
                opp_val = getattr(old_value, "Send178", None)
                if opp_val == self:
                    setattr(old_value, "Send178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Send178"):
                opp_val = getattr(value, "Send178", None)
                setattr(value, "Send178", self)

    @property
    def MessageTransmission(self):
        return self.__MessageTransmission

    @MessageTransmission.setter
    def MessageTransmission(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageTransmission__MessageTransmission", None)
        self.__MessageTransmission = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "derivation56"):
                opp_val = getattr(old_value, "derivation56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "derivation56"):
                opp_val = getattr(value, "derivation56", None)
                if opp_val is None:
                    setattr(value, "derivation56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MessageTransmission128(self):
        return self.__MessageTransmission128

    @MessageTransmission128.setter
    def MessageTransmission128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageTransmission__MessageTransmission128", None)
        self.__MessageTransmission128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "businessTransaction127"):
                opp_val = getattr(old_value, "businessTransaction127", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "businessTransaction127"):
                opp_val = getattr(value, "businessTransaction127", None)
                if opp_val is None:
                    setattr(value, "businessTransaction127", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def messageTransmission180(self):
        return self.__messageTransmission180

    @messageTransmission180.setter
    def messageTransmission180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageTransmission__messageTransmission180", None)
        self.__messageTransmission180 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Receive181"):
                    opp_val = getattr(item, "Receive181", None)
                    
                    if opp_val == self:
                        setattr(item, "Receive181", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Receive181"):
                    opp_val = getattr(item, "Receive181", None)
                    
                    setattr(item, "Receive181", self)
                    

    @property
    def MessageTransmission185(self):
        return self.__MessageTransmission185

    @MessageTransmission185.setter
    def MessageTransmission185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageTransmission__MessageTransmission185", None)
        self.__MessageTransmission185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "send"):
                opp_val = getattr(old_value, "send", None)
                if opp_val == self:
                    setattr(old_value, "send", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "send"):
                opp_val = getattr(value, "send", None)
                setattr(value, "send", self)

    @property
    def transmission(self):
        return self.__transmission

    @transmission.setter
    def transmission(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageTransmission__transmission", None)
        self.__transmission = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BusinessTransaction173"):
                opp_val = getattr(old_value, "BusinessTransaction173", None)
                if opp_val == self:
                    setattr(old_value, "BusinessTransaction173", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BusinessTransaction173"):
                opp_val = getattr(value, "BusinessTransaction173", None)
                setattr(value, "BusinessTransaction173", self)

    @property
    def trace175(self):
        return self.__trace175

    @trace175.setter
    def trace175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageTransmission__trace175", None)
        self.__trace175 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MessageDefinition176"):
                    opp_val = getattr(item, "MessageDefinition176", None)
                    
                    if opp_val == self:
                        setattr(item, "MessageDefinition176", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MessageDefinition176"):
                    opp_val = getattr(item, "MessageDefinition176", None)
                    
                    setattr(item, "MessageDefinition176", self)
                    

    @property
    def MessageTransmission169(self):
        return self.__MessageTransmission169

    @MessageTransmission169.setter
    def MessageTransmission169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageTransmission__MessageTransmission169", None)
        self.__MessageTransmission169 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "receive"):
                opp_val = getattr(old_value, "receive", None)
                if opp_val == self:
                    setattr(old_value, "receive", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "receive"):
                opp_val = getattr(value, "receive", None)
                setattr(value, "receive", self)

class iso20022_BusinessRole(RepositoryConcept):

    pass
class iso20022_TopLevelCatalogueEntry(RepositoryConcept):

    pass
class iso20022_MessageDefinition(RepositoryType):

    def __init__(self, xmlName: str, xmlTag: str, rootElement: str, MessageDefinition: "iso20022_SyntaxMessageScheme" = None, messageDefinition: set["iso20022_MessageSet"] = None, messageDefinition49: "iso20022_BusinessArea" = None, messageDefinition51: set["iso20022_Xor"] = None, iso20022_MessageDefinition: set["iso20022_MessageBuildingBlock"] = None, messageDefinition54: set["iso20022_MessageChoreography"] = None, derivation56: set["iso20022_MessageTransmission"] = None, iso20022_MessageDefinition58: "iso20022_MessageDefinitionIdentifier" = None, messageDefinitionTrace: set["iso20022_SyntaxMessageScheme"] = None, MessageDefinition64: "iso20022_MessageSet" = None, MessageDefinition74: "iso20022_BusinessArea" = None, MessageDefinition82: "iso20022_Xor" = None, MessageDefinition123: "iso20022_MessageChoreography" = None, MessageDefinition176: "iso20022_MessageTransmission" = None):
        self.xmlName = xmlName
        self.xmlTag = xmlTag
        self.rootElement = rootElement
        self.MessageDefinition = MessageDefinition
        self.messageDefinition = messageDefinition if messageDefinition is not None else set()
        self.messageDefinition49 = messageDefinition49
        self.messageDefinition51 = messageDefinition51 if messageDefinition51 is not None else set()
        self.iso20022_MessageDefinition = iso20022_MessageDefinition if iso20022_MessageDefinition is not None else set()
        self.messageDefinition54 = messageDefinition54 if messageDefinition54 is not None else set()
        self.derivation56 = derivation56 if derivation56 is not None else set()
        self.iso20022_MessageDefinition58 = iso20022_MessageDefinition58
        self.messageDefinitionTrace = messageDefinitionTrace if messageDefinitionTrace is not None else set()
        self.MessageDefinition64 = MessageDefinition64
        self.MessageDefinition74 = MessageDefinition74
        self.MessageDefinition82 = MessageDefinition82
        self.MessageDefinition123 = MessageDefinition123
        self.MessageDefinition176 = MessageDefinition176
        
    @property
    def xmlTag(self) -> str:
        return self.__xmlTag

    @xmlTag.setter
    def xmlTag(self, xmlTag: str):
        self.__xmlTag = xmlTag

    @property
    def xmlName(self) -> str:
        return self.__xmlName

    @xmlName.setter
    def xmlName(self, xmlName: str):
        self.__xmlName = xmlName

    @property
    def rootElement(self) -> str:
        return self.__rootElement

    @rootElement.setter
    def rootElement(self, rootElement: str):
        self.__rootElement = rootElement

    @property
    def messageDefinition54(self):
        return self.__messageDefinition54

    @messageDefinition54.setter
    def messageDefinition54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageDefinition__messageDefinition54", None)
        self.__messageDefinition54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MessageChoreography"):
                    opp_val = getattr(item, "MessageChoreography", None)
                    
                    if opp_val == self:
                        setattr(item, "MessageChoreography", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MessageChoreography"):
                    opp_val = getattr(item, "MessageChoreography", None)
                    
                    setattr(item, "MessageChoreography", self)
                    

    @property
    def iso20022_MessageDefinition(self):
        return self.__iso20022_MessageDefinition

    @iso20022_MessageDefinition.setter
    def iso20022_MessageDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageDefinition__iso20022_MessageDefinition", None)
        self.__iso20022_MessageDefinition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iso20022_MessageBuildingBlock"):
                    opp_val = getattr(item, "iso20022_MessageBuildingBlock", None)
                    
                    if opp_val == self:
                        setattr(item, "iso20022_MessageBuildingBlock", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iso20022_MessageBuildingBlock"):
                    opp_val = getattr(item, "iso20022_MessageBuildingBlock", None)
                    
                    setattr(item, "iso20022_MessageBuildingBlock", self)
                    

    @property
    def MessageDefinition64(self):
        return self.__MessageDefinition64

    @MessageDefinition64.setter
    def MessageDefinition64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageDefinition__MessageDefinition64", None)
        self.__MessageDefinition64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "messageSet63"):
                opp_val = getattr(old_value, "messageSet63", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "messageSet63"):
                opp_val = getattr(value, "messageSet63", None)
                if opp_val is None:
                    setattr(value, "messageSet63", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def messageDefinition49(self):
        return self.__messageDefinition49

    @messageDefinition49.setter
    def messageDefinition49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageDefinition__messageDefinition49", None)
        self.__messageDefinition49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BusinessArea"):
                opp_val = getattr(old_value, "BusinessArea", None)
                if opp_val == self:
                    setattr(old_value, "BusinessArea", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BusinessArea"):
                opp_val = getattr(value, "BusinessArea", None)
                setattr(value, "BusinessArea", self)

    @property
    def messageDefinitionTrace(self):
        return self.__messageDefinitionTrace

    @messageDefinitionTrace.setter
    def messageDefinitionTrace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageDefinition__messageDefinitionTrace", None)
        self.__messageDefinitionTrace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SyntaxMessageScheme"):
                    opp_val = getattr(item, "SyntaxMessageScheme", None)
                    
                    if opp_val == self:
                        setattr(item, "SyntaxMessageScheme", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SyntaxMessageScheme"):
                    opp_val = getattr(item, "SyntaxMessageScheme", None)
                    
                    setattr(item, "SyntaxMessageScheme", self)
                    

    @property
    def MessageDefinition(self):
        return self.__MessageDefinition

    @MessageDefinition.setter
    def MessageDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageDefinition__MessageDefinition", None)
        self.__MessageDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "derivation"):
                opp_val = getattr(old_value, "derivation", None)
                if opp_val == self:
                    setattr(old_value, "derivation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "derivation"):
                opp_val = getattr(value, "derivation", None)
                setattr(value, "derivation", self)

    @property
    def MessageDefinition82(self):
        return self.__MessageDefinition82

    @MessageDefinition82.setter
    def MessageDefinition82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageDefinition__MessageDefinition82", None)
        self.__MessageDefinition82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xors81"):
                opp_val = getattr(old_value, "xors81", None)
                if opp_val == self:
                    setattr(old_value, "xors81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xors81"):
                opp_val = getattr(value, "xors81", None)
                setattr(value, "xors81", self)

    @property
    def iso20022_MessageDefinition58(self):
        return self.__iso20022_MessageDefinition58

    @iso20022_MessageDefinition58.setter
    def iso20022_MessageDefinition58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageDefinition__iso20022_MessageDefinition58", None)
        self.__iso20022_MessageDefinition58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iso20022_MessageDefinitionIdentifier"):
                opp_val = getattr(old_value, "iso20022_MessageDefinitionIdentifier", None)
                if opp_val == self:
                    setattr(old_value, "iso20022_MessageDefinitionIdentifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iso20022_MessageDefinitionIdentifier"):
                opp_val = getattr(value, "iso20022_MessageDefinitionIdentifier", None)
                setattr(value, "iso20022_MessageDefinitionIdentifier", self)

    @property
    def messageDefinition(self):
        return self.__messageDefinition

    @messageDefinition.setter
    def messageDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageDefinition__messageDefinition", None)
        self.__messageDefinition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MessageSet"):
                    opp_val = getattr(item, "MessageSet", None)
                    
                    if opp_val == self:
                        setattr(item, "MessageSet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MessageSet"):
                    opp_val = getattr(item, "MessageSet", None)
                    
                    setattr(item, "MessageSet", self)
                    

    @property
    def messageDefinition51(self):
        return self.__messageDefinition51

    @messageDefinition51.setter
    def messageDefinition51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageDefinition__messageDefinition51", None)
        self.__messageDefinition51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Xor"):
                    opp_val = getattr(item, "Xor", None)
                    
                    if opp_val == self:
                        setattr(item, "Xor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Xor"):
                    opp_val = getattr(item, "Xor", None)
                    
                    setattr(item, "Xor", self)
                    

    @property
    def MessageDefinition123(self):
        return self.__MessageDefinition123

    @MessageDefinition123.setter
    def MessageDefinition123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageDefinition__MessageDefinition123", None)
        self.__MessageDefinition123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "choreography"):
                opp_val = getattr(old_value, "choreography", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "choreography"):
                opp_val = getattr(value, "choreography", None)
                if opp_val is None:
                    setattr(value, "choreography", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MessageDefinition176(self):
        return self.__MessageDefinition176

    @MessageDefinition176.setter
    def MessageDefinition176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageDefinition__MessageDefinition176", None)
        self.__MessageDefinition176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace175"):
                opp_val = getattr(old_value, "trace175", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace175"):
                opp_val = getattr(value, "trace175", None)
                if opp_val is None:
                    setattr(value, "trace175", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MessageDefinition74(self):
        return self.__MessageDefinition74

    @MessageDefinition74.setter
    def MessageDefinition74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageDefinition__MessageDefinition74", None)
        self.__MessageDefinition74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "businessArea"):
                opp_val = getattr(old_value, "businessArea", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "businessArea"):
                opp_val = getattr(value, "businessArea", None)
                if opp_val is None:
                    setattr(value, "businessArea", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def derivation56(self):
        return self.__derivation56

    @derivation56.setter
    def derivation56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageDefinition__derivation56", None)
        self.__derivation56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MessageTransmission"):
                    opp_val = getattr(item, "MessageTransmission", None)
                    
                    if opp_val == self:
                        setattr(item, "MessageTransmission", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MessageTransmission"):
                    opp_val = getattr(item, "MessageTransmission", None)
                    
                    setattr(item, "MessageTransmission", self)
                    

    def BusinessAreaNameMatch(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement BusinessAreaNameMatch method
        pass

class TopLevelCatalogueEntry:

    pass
class iso20022_MessageChoreography(TopLevelCatalogueEntry):

    pass
class iso20022_ConvergenceDocumentation(TopLevelCatalogueEntry):

    pass
class iso20022_MessageTransportMode(TopLevelCatalogueEntry):

    def __init__(self, boundedCommunicationDelay: str, maximumClockVariation: str, maximumMessageSize: str, messageDeliveryWindow: str, messageSendingWindow: str, deliveryAssurance: str, durability: str, messageCasting: str, messageDeliveryOrder: str, messageValidationLevel: str, messageValidationOnOff: str, messageValidationResults: str, receiverAsynchronicity: str, senderAsynchronicity: str, MessageTransportMode: "iso20022_BusinessTransaction" = None, messageTransportMode: set["iso20022_BusinessTransaction"] = None):
        self.boundedCommunicationDelay = boundedCommunicationDelay
        self.maximumClockVariation = maximumClockVariation
        self.maximumMessageSize = maximumMessageSize
        self.messageDeliveryWindow = messageDeliveryWindow
        self.messageSendingWindow = messageSendingWindow
        self.deliveryAssurance = deliveryAssurance
        self.durability = durability
        self.messageCasting = messageCasting
        self.messageDeliveryOrder = messageDeliveryOrder
        self.messageValidationLevel = messageValidationLevel
        self.messageValidationOnOff = messageValidationOnOff
        self.messageValidationResults = messageValidationResults
        self.receiverAsynchronicity = receiverAsynchronicity
        self.senderAsynchronicity = senderAsynchronicity
        self.MessageTransportMode = MessageTransportMode
        self.messageTransportMode = messageTransportMode if messageTransportMode is not None else set()
        
    @property
    def messageDeliveryWindow(self) -> str:
        return self.__messageDeliveryWindow

    @messageDeliveryWindow.setter
    def messageDeliveryWindow(self, messageDeliveryWindow: str):
        self.__messageDeliveryWindow = messageDeliveryWindow

    @property
    def deliveryAssurance(self) -> str:
        return self.__deliveryAssurance

    @deliveryAssurance.setter
    def deliveryAssurance(self, deliveryAssurance: str):
        self.__deliveryAssurance = deliveryAssurance

    @property
    def boundedCommunicationDelay(self) -> str:
        return self.__boundedCommunicationDelay

    @boundedCommunicationDelay.setter
    def boundedCommunicationDelay(self, boundedCommunicationDelay: str):
        self.__boundedCommunicationDelay = boundedCommunicationDelay

    @property
    def maximumMessageSize(self) -> str:
        return self.__maximumMessageSize

    @maximumMessageSize.setter
    def maximumMessageSize(self, maximumMessageSize: str):
        self.__maximumMessageSize = maximumMessageSize

    @property
    def messageValidationLevel(self) -> str:
        return self.__messageValidationLevel

    @messageValidationLevel.setter
    def messageValidationLevel(self, messageValidationLevel: str):
        self.__messageValidationLevel = messageValidationLevel

    @property
    def messageValidationOnOff(self) -> str:
        return self.__messageValidationOnOff

    @messageValidationOnOff.setter
    def messageValidationOnOff(self, messageValidationOnOff: str):
        self.__messageValidationOnOff = messageValidationOnOff

    @property
    def maximumClockVariation(self) -> str:
        return self.__maximumClockVariation

    @maximumClockVariation.setter
    def maximumClockVariation(self, maximumClockVariation: str):
        self.__maximumClockVariation = maximumClockVariation

    @property
    def messageDeliveryOrder(self) -> str:
        return self.__messageDeliveryOrder

    @messageDeliveryOrder.setter
    def messageDeliveryOrder(self, messageDeliveryOrder: str):
        self.__messageDeliveryOrder = messageDeliveryOrder

    @property
    def messageValidationResults(self) -> str:
        return self.__messageValidationResults

    @messageValidationResults.setter
    def messageValidationResults(self, messageValidationResults: str):
        self.__messageValidationResults = messageValidationResults

    @property
    def senderAsynchronicity(self) -> str:
        return self.__senderAsynchronicity

    @senderAsynchronicity.setter
    def senderAsynchronicity(self, senderAsynchronicity: str):
        self.__senderAsynchronicity = senderAsynchronicity

    @property
    def durability(self) -> str:
        return self.__durability

    @durability.setter
    def durability(self, durability: str):
        self.__durability = durability

    @property
    def messageCasting(self) -> str:
        return self.__messageCasting

    @messageCasting.setter
    def messageCasting(self, messageCasting: str):
        self.__messageCasting = messageCasting

    @property
    def messageSendingWindow(self) -> str:
        return self.__messageSendingWindow

    @messageSendingWindow.setter
    def messageSendingWindow(self, messageSendingWindow: str):
        self.__messageSendingWindow = messageSendingWindow

    @property
    def receiverAsynchronicity(self) -> str:
        return self.__receiverAsynchronicity

    @receiverAsynchronicity.setter
    def receiverAsynchronicity(self, receiverAsynchronicity: str):
        self.__receiverAsynchronicity = receiverAsynchronicity

    @property
    def messageTransportMode(self):
        return self.__messageTransportMode

    @messageTransportMode.setter
    def messageTransportMode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageTransportMode__messageTransportMode", None)
        self.__messageTransportMode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BusinessTransaction187"):
                    opp_val = getattr(item, "BusinessTransaction187", None)
                    
                    if opp_val == self:
                        setattr(item, "BusinessTransaction187", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BusinessTransaction187"):
                    opp_val = getattr(item, "BusinessTransaction187", None)
                    
                    setattr(item, "BusinessTransaction187", self)
                    

    @property
    def MessageTransportMode(self):
        return self.__MessageTransportMode

    @MessageTransportMode.setter
    def MessageTransportMode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageTransportMode__MessageTransportMode", None)
        self.__MessageTransportMode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "businessTransaction130"):
                opp_val = getattr(old_value, "businessTransaction130", None)
                if opp_val == self:
                    setattr(old_value, "businessTransaction130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "businessTransaction130"):
                opp_val = getattr(value, "businessTransaction130", None)
                setattr(value, "businessTransaction130", self)

class iso20022_BusinessArea(TopLevelCatalogueEntry):

    def __init__(self, code: str, BusinessArea: "iso20022_MessageDefinition" = None, businessArea: set["iso20022_MessageDefinition"] = None):
        self.code = code
        self.BusinessArea = BusinessArea
        self.businessArea = businessArea if businessArea is not None else set()
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def businessArea(self):
        return self.__businessArea

    @businessArea.setter
    def businessArea(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessArea__businessArea", None)
        self.__businessArea = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MessageDefinition74"):
                    opp_val = getattr(item, "MessageDefinition74", None)
                    
                    if opp_val == self:
                        setattr(item, "MessageDefinition74", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MessageDefinition74"):
                    opp_val = getattr(item, "MessageDefinition74", None)
                    
                    setattr(item, "MessageDefinition74", self)
                    

    @property
    def BusinessArea(self):
        return self.__BusinessArea

    @BusinessArea.setter
    def BusinessArea(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessArea__BusinessArea", None)
        self.__BusinessArea = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "messageDefinition49"):
                opp_val = getattr(old_value, "messageDefinition49", None)
                if opp_val == self:
                    setattr(old_value, "messageDefinition49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "messageDefinition49"):
                opp_val = getattr(value, "messageDefinition49", None)
                setattr(value, "messageDefinition49", self)

class iso20022_BusinessProcess(TopLevelCatalogueEntry):

    pass
class iso20022_IndustryMessageSet(TopLevelCatalogueEntry):

    pass
class iso20022_MessageSet(TopLevelCatalogueEntry):

    def __init__(self, MessageSet: "iso20022_MessageDefinition" = None, generatedFor: set["iso20022_Syntax"] = None, messageSet: set["iso20022_Encoding"] = None, messageSet63: set["iso20022_MessageDefinition"] = None, MessageSet68: "iso20022_Syntax" = None, MessageSet70: "iso20022_Encoding" = None):
        self.MessageSet = MessageSet
        self.generatedFor = generatedFor if generatedFor is not None else set()
        self.messageSet = messageSet if messageSet is not None else set()
        self.messageSet63 = messageSet63 if messageSet63 is not None else set()
        self.MessageSet68 = MessageSet68
        self.MessageSet70 = MessageSet70
        
    @property
    def MessageSet(self):
        return self.__MessageSet

    @MessageSet.setter
    def MessageSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageSet__MessageSet", None)
        self.__MessageSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "messageDefinition"):
                opp_val = getattr(old_value, "messageDefinition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "messageDefinition"):
                opp_val = getattr(value, "messageDefinition", None)
                if opp_val is None:
                    setattr(value, "messageDefinition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def messageSet63(self):
        return self.__messageSet63

    @messageSet63.setter
    def messageSet63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageSet__messageSet63", None)
        self.__messageSet63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MessageDefinition64"):
                    opp_val = getattr(item, "MessageDefinition64", None)
                    
                    if opp_val == self:
                        setattr(item, "MessageDefinition64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MessageDefinition64"):
                    opp_val = getattr(item, "MessageDefinition64", None)
                    
                    setattr(item, "MessageDefinition64", self)
                    

    @property
    def messageSet(self):
        return self.__messageSet

    @messageSet.setter
    def messageSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageSet__messageSet", None)
        self.__messageSet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Encoding"):
                    opp_val = getattr(item, "Encoding", None)
                    
                    if opp_val == self:
                        setattr(item, "Encoding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Encoding"):
                    opp_val = getattr(item, "Encoding", None)
                    
                    setattr(item, "Encoding", self)
                    

    @property
    def MessageSet70(self):
        return self.__MessageSet70

    @MessageSet70.setter
    def MessageSet70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageSet__MessageSet70", None)
        self.__MessageSet70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "validEncoding"):
                opp_val = getattr(old_value, "validEncoding", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "validEncoding"):
                opp_val = getattr(value, "validEncoding", None)
                if opp_val is None:
                    setattr(value, "validEncoding", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MessageSet68(self):
        return self.__MessageSet68

    @MessageSet68.setter
    def MessageSet68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageSet__MessageSet68", None)
        self.__MessageSet68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generatedSyntax"):
                opp_val = getattr(old_value, "generatedSyntax", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generatedSyntax"):
                opp_val = getattr(value, "generatedSyntax", None)
                if opp_val is None:
                    setattr(value, "generatedSyntax", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def generatedFor(self):
        return self.__generatedFor

    @generatedFor.setter
    def generatedFor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageSet__generatedFor", None)
        self.__generatedFor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Syntax"):
                    opp_val = getattr(item, "Syntax", None)
                    
                    if opp_val == self:
                        setattr(item, "Syntax", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Syntax"):
                    opp_val = getattr(item, "Syntax", None)
                    
                    setattr(item, "Syntax", self)
                    

    def GeneratedSyntaxDerivation(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement GeneratedSyntaxDerivation method
        pass

class iso20022_BusinessTransaction(TopLevelCatalogueEntry):

    def __init__(self, BusinessTransaction: "iso20022_MessageChoreography" = None, businessProcessTrace: "iso20022_BusinessProcess" = None, businessTransaction: set["iso20022_Participant"] = None, businessTransaction127: set["iso20022_MessageTransmission"] = None, businessTransaction130: "iso20022_MessageTransportMode" = None, BusinessTransaction133: "iso20022_BusinessTransaction" = None, parentTransaction: set["iso20022_BusinessTransaction"] = None, BusinessTransaction136: "iso20022_BusinessTransaction" = None, subTransaction: "iso20022_BusinessTransaction" = None, businessTransactionTrace: set["iso20022_MessageChoreography"] = None, BusinessTransaction154: "iso20022_BusinessProcess" = None, BusinessTransaction160: "iso20022_Participant" = None, BusinessTransaction173: "iso20022_MessageTransmission" = None, BusinessTransaction187: "iso20022_MessageTransportMode" = None):
        self.BusinessTransaction = BusinessTransaction
        self.businessProcessTrace = businessProcessTrace
        self.businessTransaction = businessTransaction if businessTransaction is not None else set()
        self.businessTransaction127 = businessTransaction127 if businessTransaction127 is not None else set()
        self.businessTransaction130 = businessTransaction130
        self.BusinessTransaction133 = BusinessTransaction133
        self.parentTransaction = parentTransaction if parentTransaction is not None else set()
        self.BusinessTransaction136 = BusinessTransaction136
        self.subTransaction = subTransaction
        self.businessTransactionTrace = businessTransactionTrace if businessTransactionTrace is not None else set()
        self.BusinessTransaction154 = BusinessTransaction154
        self.BusinessTransaction160 = BusinessTransaction160
        self.BusinessTransaction173 = BusinessTransaction173
        self.BusinessTransaction187 = BusinessTransaction187
        
    @property
    def businessProcessTrace(self):
        return self.__businessProcessTrace

    @businessProcessTrace.setter
    def businessProcessTrace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessTransaction__businessProcessTrace", None)
        self.__businessProcessTrace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BusinessProcess"):
                opp_val = getattr(old_value, "BusinessProcess", None)
                if opp_val == self:
                    setattr(old_value, "BusinessProcess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BusinessProcess"):
                opp_val = getattr(value, "BusinessProcess", None)
                setattr(value, "BusinessProcess", self)

    @property
    def businessTransaction(self):
        return self.__businessTransaction

    @businessTransaction.setter
    def businessTransaction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessTransaction__businessTransaction", None)
        self.__businessTransaction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Participant"):
                    opp_val = getattr(item, "Participant", None)
                    
                    if opp_val == self:
                        setattr(item, "Participant", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Participant"):
                    opp_val = getattr(item, "Participant", None)
                    
                    setattr(item, "Participant", self)
                    

    @property
    def BusinessTransaction173(self):
        return self.__BusinessTransaction173

    @BusinessTransaction173.setter
    def BusinessTransaction173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessTransaction__BusinessTransaction173", None)
        self.__BusinessTransaction173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transmission"):
                opp_val = getattr(old_value, "transmission", None)
                if opp_val == self:
                    setattr(old_value, "transmission", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transmission"):
                opp_val = getattr(value, "transmission", None)
                setattr(value, "transmission", self)

    @property
    def BusinessTransaction154(self):
        return self.__BusinessTransaction154

    @BusinessTransaction154.setter
    def BusinessTransaction154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessTransaction__BusinessTransaction154", None)
        self.__BusinessTransaction154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "businessProcessTrace153"):
                opp_val = getattr(old_value, "businessProcessTrace153", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "businessProcessTrace153"):
                opp_val = getattr(value, "businessProcessTrace153", None)
                if opp_val is None:
                    setattr(value, "businessProcessTrace153", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def businessTransaction130(self):
        return self.__businessTransaction130

    @businessTransaction130.setter
    def businessTransaction130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessTransaction__businessTransaction130", None)
        self.__businessTransaction130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MessageTransportMode"):
                opp_val = getattr(old_value, "MessageTransportMode", None)
                if opp_val == self:
                    setattr(old_value, "MessageTransportMode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MessageTransportMode"):
                opp_val = getattr(value, "MessageTransportMode", None)
                setattr(value, "MessageTransportMode", self)

    @property
    def BusinessTransaction(self):
        return self.__BusinessTransaction

    @BusinessTransaction.setter
    def BusinessTransaction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessTransaction__BusinessTransaction", None)
        self.__BusinessTransaction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace121"):
                opp_val = getattr(old_value, "trace121", None)
                if opp_val == self:
                    setattr(old_value, "trace121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace121"):
                opp_val = getattr(value, "trace121", None)
                setattr(value, "trace121", self)

    @property
    def BusinessTransaction133(self):
        return self.__BusinessTransaction133

    @BusinessTransaction133.setter
    def BusinessTransaction133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessTransaction__BusinessTransaction133", None)
        self.__BusinessTransaction133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parentTransaction"):
                opp_val = getattr(old_value, "parentTransaction", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentTransaction"):
                opp_val = getattr(value, "parentTransaction", None)
                if opp_val is None:
                    setattr(value, "parentTransaction", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BusinessTransaction187(self):
        return self.__BusinessTransaction187

    @BusinessTransaction187.setter
    def BusinessTransaction187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessTransaction__BusinessTransaction187", None)
        self.__BusinessTransaction187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "messageTransportMode"):
                opp_val = getattr(old_value, "messageTransportMode", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "messageTransportMode"):
                opp_val = getattr(value, "messageTransportMode", None)
                if opp_val is None:
                    setattr(value, "messageTransportMode", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BusinessTransaction160(self):
        return self.__BusinessTransaction160

    @BusinessTransaction160.setter
    def BusinessTransaction160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessTransaction__BusinessTransaction160", None)
        self.__BusinessTransaction160 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "participant"):
                opp_val = getattr(old_value, "participant", None)
                if opp_val == self:
                    setattr(old_value, "participant", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "participant"):
                opp_val = getattr(value, "participant", None)
                setattr(value, "participant", self)

    @property
    def BusinessTransaction136(self):
        return self.__BusinessTransaction136

    @BusinessTransaction136.setter
    def BusinessTransaction136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessTransaction__BusinessTransaction136", None)
        self.__BusinessTransaction136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subTransaction"):
                opp_val = getattr(old_value, "subTransaction", None)
                if opp_val == self:
                    setattr(old_value, "subTransaction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subTransaction"):
                opp_val = getattr(value, "subTransaction", None)
                setattr(value, "subTransaction", self)

    @property
    def subTransaction(self):
        return self.__subTransaction

    @subTransaction.setter
    def subTransaction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessTransaction__subTransaction", None)
        self.__subTransaction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BusinessTransaction136"):
                opp_val = getattr(old_value, "BusinessTransaction136", None)
                if opp_val == self:
                    setattr(old_value, "BusinessTransaction136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BusinessTransaction136"):
                opp_val = getattr(value, "BusinessTransaction136", None)
                setattr(value, "BusinessTransaction136", self)

    @property
    def businessTransaction127(self):
        return self.__businessTransaction127

    @businessTransaction127.setter
    def businessTransaction127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessTransaction__businessTransaction127", None)
        self.__businessTransaction127 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MessageTransmission128"):
                    opp_val = getattr(item, "MessageTransmission128", None)
                    
                    if opp_val == self:
                        setattr(item, "MessageTransmission128", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MessageTransmission128"):
                    opp_val = getattr(item, "MessageTransmission128", None)
                    
                    setattr(item, "MessageTransmission128", self)
                    

    @property
    def businessTransactionTrace(self):
        return self.__businessTransactionTrace

    @businessTransactionTrace.setter
    def businessTransactionTrace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessTransaction__businessTransactionTrace", None)
        self.__businessTransactionTrace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MessageChoreography138"):
                    opp_val = getattr(item, "MessageChoreography138", None)
                    
                    if opp_val == self:
                        setattr(item, "MessageChoreography138", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MessageChoreography138"):
                    opp_val = getattr(item, "MessageChoreography138", None)
                    
                    setattr(item, "MessageChoreography138", self)
                    

    @property
    def parentTransaction(self):
        return self.__parentTransaction

    @parentTransaction.setter
    def parentTransaction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessTransaction__parentTransaction", None)
        self.__parentTransaction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BusinessTransaction133"):
                    opp_val = getattr(item, "BusinessTransaction133", None)
                    
                    if opp_val == self:
                        setattr(item, "BusinessTransaction133", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BusinessTransaction133"):
                    opp_val = getattr(item, "BusinessTransaction133", None)
                    
                    setattr(item, "BusinessTransaction133", self)
                    

    def MessageTransmissionsHaveUniqueNames(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement MessageTransmissionsHaveUniqueNames method
        pass

    def ParticipantsHaveUniqueNames(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ParticipantsHaveUniqueNames method
        pass

class iso20022_SyntaxMessageScheme(TopLevelCatalogueEntry):

    pass
class iso20022_ModelEntity(ABC):

    def __init__(self, objectIdentifier: str, ModelEntity: "iso20022_ModelEntity" = None, previousVersion: set["iso20022_ModelEntity"] = None, ModelEntity6: "iso20022_ModelEntity" = None, nextVersions: "iso20022_ModelEntity" = None):
        self.objectIdentifier = objectIdentifier
        self.ModelEntity = ModelEntity
        self.previousVersion = previousVersion if previousVersion is not None else set()
        self.ModelEntity6 = ModelEntity6
        self.nextVersions = nextVersions
        
    @property
    def objectIdentifier(self) -> str:
        return self.__objectIdentifier

    @objectIdentifier.setter
    def objectIdentifier(self, objectIdentifier: str):
        self.__objectIdentifier = objectIdentifier

    @property
    def ModelEntity(self):
        return self.__ModelEntity

    @ModelEntity.setter
    def ModelEntity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_ModelEntity__ModelEntity", None)
        self.__ModelEntity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "previousVersion"):
                opp_val = getattr(old_value, "previousVersion", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "previousVersion"):
                opp_val = getattr(value, "previousVersion", None)
                if opp_val is None:
                    setattr(value, "previousVersion", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ModelEntity6(self):
        return self.__ModelEntity6

    @ModelEntity6.setter
    def ModelEntity6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_ModelEntity__ModelEntity6", None)
        self.__ModelEntity6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nextVersions"):
                opp_val = getattr(old_value, "nextVersions", None)
                if opp_val == self:
                    setattr(old_value, "nextVersions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nextVersions"):
                opp_val = getattr(value, "nextVersions", None)
                setattr(value, "nextVersions", self)

    @property
    def previousVersion(self):
        return self.__previousVersion

    @previousVersion.setter
    def previousVersion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_ModelEntity__previousVersion", None)
        self.__previousVersion = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelEntity"):
                    opp_val = getattr(item, "ModelEntity", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelEntity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelEntity"):
                    opp_val = getattr(item, "ModelEntity", None)
                    
                    setattr(item, "ModelEntity", self)
                    

    @property
    def nextVersions(self):
        return self.__nextVersions

    @nextVersions.setter
    def nextVersions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_ModelEntity__nextVersions", None)
        self.__nextVersions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelEntity6"):
                opp_val = getattr(old_value, "ModelEntity6", None)
                if opp_val == self:
                    setattr(old_value, "ModelEntity6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelEntity6"):
                opp_val = getattr(value, "ModelEntity6", None)
                setattr(value, "ModelEntity6", self)

class ModelEntity:

    pass
class iso20022_MessageConcept(ModelEntity):

    pass
class iso20022_Syntax(ModelEntity):

    def __init__(self, syntax: set["iso20022_Encoding"] = None, generatedSyntax: set["iso20022_MessageSet"] = None, Syntax72: "iso20022_Encoding" = None, Syntax: "iso20022_MessageSet" = None):
        self.syntax = syntax if syntax is not None else set()
        self.generatedSyntax = generatedSyntax if generatedSyntax is not None else set()
        self.Syntax72 = Syntax72
        self.Syntax = Syntax
        
    @property
    def syntax(self):
        return self.__syntax

    @syntax.setter
    def syntax(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_Syntax__syntax", None)
        self.__syntax = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Encoding66"):
                    opp_val = getattr(item, "Encoding66", None)
                    
                    if opp_val == self:
                        setattr(item, "Encoding66", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Encoding66"):
                    opp_val = getattr(item, "Encoding66", None)
                    
                    setattr(item, "Encoding66", self)
                    

    @property
    def Syntax(self):
        return self.__Syntax

    @Syntax.setter
    def Syntax(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_Syntax__Syntax", None)
        self.__Syntax = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generatedFor"):
                opp_val = getattr(old_value, "generatedFor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generatedFor"):
                opp_val = getattr(value, "generatedFor", None)
                if opp_val is None:
                    setattr(value, "generatedFor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Syntax72(self):
        return self.__Syntax72

    @Syntax72.setter
    def Syntax72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_Syntax__Syntax72", None)
        self.__Syntax72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "possibleEncodings"):
                opp_val = getattr(old_value, "possibleEncodings", None)
                if opp_val == self:
                    setattr(old_value, "possibleEncodings", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "possibleEncodings"):
                opp_val = getattr(value, "possibleEncodings", None)
                setattr(value, "possibleEncodings", self)

    @property
    def generatedSyntax(self):
        return self.__generatedSyntax

    @generatedSyntax.setter
    def generatedSyntax(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_Syntax__generatedSyntax", None)
        self.__generatedSyntax = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MessageSet68"):
                    opp_val = getattr(item, "MessageSet68", None)
                    
                    if opp_val == self:
                        setattr(item, "MessageSet68", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MessageSet68"):
                    opp_val = getattr(item, "MessageSet68", None)
                    
                    setattr(item, "MessageSet68", self)
                    

    def GeneratedForDerivation(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement GeneratedForDerivation method
        pass

class iso20022_Receive(ModelEntity):

    pass
class iso20022_DataDictionary(ModelEntity):

    def __init__(self, DataDictionary: "iso20022_Repository" = None, dataDictionary: set["iso20022_TopLevelDictionaryEntry"] = None, dataDictionary43: "iso20022_Repository" = None, DataDictionary46: "iso20022_TopLevelDictionaryEntry" = None):
        self.DataDictionary = DataDictionary
        self.dataDictionary = dataDictionary if dataDictionary is not None else set()
        self.dataDictionary43 = dataDictionary43
        self.DataDictionary46 = DataDictionary46
        
    @property
    def DataDictionary46(self):
        return self.__DataDictionary46

    @DataDictionary46.setter
    def DataDictionary46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_DataDictionary__DataDictionary46", None)
        self.__DataDictionary46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "topLevelDictionaryEntry"):
                opp_val = getattr(old_value, "topLevelDictionaryEntry", None)
                if opp_val == self:
                    setattr(old_value, "topLevelDictionaryEntry", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "topLevelDictionaryEntry"):
                opp_val = getattr(value, "topLevelDictionaryEntry", None)
                setattr(value, "topLevelDictionaryEntry", self)

    @property
    def DataDictionary(self):
        return self.__DataDictionary

    @DataDictionary.setter
    def DataDictionary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_DataDictionary__DataDictionary", None)
        self.__DataDictionary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository"):
                opp_val = getattr(old_value, "repository", None)
                if opp_val == self:
                    setattr(old_value, "repository", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository"):
                opp_val = getattr(value, "repository", None)
                setattr(value, "repository", self)

    @property
    def dataDictionary43(self):
        return self.__dataDictionary43

    @dataDictionary43.setter
    def dataDictionary43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_DataDictionary__dataDictionary43", None)
        self.__dataDictionary43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Repository44"):
                opp_val = getattr(old_value, "Repository44", None)
                if opp_val == self:
                    setattr(old_value, "Repository44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Repository44"):
                opp_val = getattr(value, "Repository44", None)
                setattr(value, "Repository44", self)

    @property
    def dataDictionary(self):
        return self.__dataDictionary

    @dataDictionary.setter
    def dataDictionary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_DataDictionary__dataDictionary", None)
        self.__dataDictionary = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TopLevelDictionaryEntry"):
                    opp_val = getattr(item, "TopLevelDictionaryEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "TopLevelDictionaryEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TopLevelDictionaryEntry"):
                    opp_val = getattr(item, "TopLevelDictionaryEntry", None)
                    
                    setattr(item, "TopLevelDictionaryEntry", self)
                    

    def EntriesHaveUniqueName(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement EntriesHaveUniqueName method
        pass

class iso20022_BusinessConcept(ModelEntity):

    pass
class iso20022_Conversation(ModelEntity):

    pass
class iso20022_TransportMessage(ModelEntity):

    def __init__(self, TransportMessage11: "iso20022_MessagingEndpoint" = None, sentMessage: "iso20022_MessagingEndpoint" = None, transportMessage: "iso20022_MessageInstance" = None, receivedMessage: set["iso20022_MessagingEndpoint"] = None, TransportMessage: "iso20022_MessagingEndpoint" = None, TransportMessage24: "iso20022_MessageInstance" = None):
        self.TransportMessage11 = TransportMessage11
        self.sentMessage = sentMessage
        self.transportMessage = transportMessage
        self.receivedMessage = receivedMessage if receivedMessage is not None else set()
        self.TransportMessage = TransportMessage
        self.TransportMessage24 = TransportMessage24
        
    @property
    def sentMessage(self):
        return self.__sentMessage

    @sentMessage.setter
    def sentMessage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_TransportMessage__sentMessage", None)
        self.__sentMessage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MessagingEndpoint18"):
                opp_val = getattr(old_value, "MessagingEndpoint18", None)
                if opp_val == self:
                    setattr(old_value, "MessagingEndpoint18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MessagingEndpoint18"):
                opp_val = getattr(value, "MessagingEndpoint18", None)
                setattr(value, "MessagingEndpoint18", self)

    @property
    def TransportMessage11(self):
        return self.__TransportMessage11

    @TransportMessage11.setter
    def TransportMessage11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_TransportMessage__TransportMessage11", None)
        self.__TransportMessage11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sender"):
                opp_val = getattr(old_value, "sender", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sender"):
                opp_val = getattr(value, "sender", None)
                if opp_val is None:
                    setattr(value, "sender", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TransportMessage24(self):
        return self.__TransportMessage24

    @TransportMessage24.setter
    def TransportMessage24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_TransportMessage__TransportMessage24", None)
        self.__TransportMessage24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "messageInstance"):
                opp_val = getattr(old_value, "messageInstance", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "messageInstance"):
                opp_val = getattr(value, "messageInstance", None)
                if opp_val is None:
                    setattr(value, "messageInstance", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def transportMessage(self):
        return self.__transportMessage

    @transportMessage.setter
    def transportMessage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_TransportMessage__transportMessage", None)
        self.__transportMessage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MessageInstance"):
                opp_val = getattr(old_value, "MessageInstance", None)
                if opp_val == self:
                    setattr(old_value, "MessageInstance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MessageInstance"):
                opp_val = getattr(value, "MessageInstance", None)
                setattr(value, "MessageInstance", self)

    @property
    def TransportMessage(self):
        return self.__TransportMessage

    @TransportMessage.setter
    def TransportMessage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_TransportMessage__TransportMessage", None)
        self.__TransportMessage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "receiver"):
                opp_val = getattr(old_value, "receiver", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "receiver"):
                opp_val = getattr(value, "receiver", None)
                if opp_val is None:
                    setattr(value, "receiver", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def receivedMessage(self):
        return self.__receivedMessage

    @receivedMessage.setter
    def receivedMessage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_TransportMessage__receivedMessage", None)
        self.__receivedMessage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MessagingEndpoint21"):
                    opp_val = getattr(item, "MessagingEndpoint21", None)
                    
                    if opp_val == self:
                        setattr(item, "MessagingEndpoint21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MessagingEndpoint21"):
                    opp_val = getattr(item, "MessagingEndpoint21", None)
                    
                    setattr(item, "MessagingEndpoint21", self)
                    

    def sameMessageTransportSystem(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement sameMessageTransportSystem method
        pass

class iso20022_Send(ModelEntity):

    pass
class iso20022_MessageTransportSystem(ModelEntity):

    pass
class iso20022_MessagingEndpoint(ModelEntity):

    pass
class iso20022_SemanticMarkup(ModelEntity):

    def __init__(self, type: str, iso20022_SemanticMarkup32: set["iso20022_SemanticMarkupElement"] = None, iso20022_SemanticMarkup: "iso20022_RepositoryConcept" = None):
        self.type = type
        self.iso20022_SemanticMarkup32 = iso20022_SemanticMarkup32 if iso20022_SemanticMarkup32 is not None else set()
        self.iso20022_SemanticMarkup = iso20022_SemanticMarkup
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def iso20022_SemanticMarkup32(self):
        return self.__iso20022_SemanticMarkup32

    @iso20022_SemanticMarkup32.setter
    def iso20022_SemanticMarkup32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_SemanticMarkup__iso20022_SemanticMarkup32", None)
        self.__iso20022_SemanticMarkup32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iso20022_SemanticMarkupElement"):
                    opp_val = getattr(item, "iso20022_SemanticMarkupElement", None)
                    
                    if opp_val == self:
                        setattr(item, "iso20022_SemanticMarkupElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iso20022_SemanticMarkupElement"):
                    opp_val = getattr(item, "iso20022_SemanticMarkupElement", None)
                    
                    setattr(item, "iso20022_SemanticMarkupElement", self)
                    

    @property
    def iso20022_SemanticMarkup(self):
        return self.__iso20022_SemanticMarkup

    @iso20022_SemanticMarkup.setter
    def iso20022_SemanticMarkup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_SemanticMarkup__iso20022_SemanticMarkup", None)
        self.__iso20022_SemanticMarkup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iso20022_RepositoryConcept"):
                opp_val = getattr(old_value, "iso20022_RepositoryConcept", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iso20022_RepositoryConcept"):
                opp_val = getattr(value, "iso20022_RepositoryConcept", None)
                if opp_val is None:
                    setattr(value, "iso20022_RepositoryConcept", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class iso20022_Doclet(ModelEntity):

    def __init__(self, type: str, content: str, iso20022_Doclet: "iso20022_RepositoryConcept" = None):
        self.type = type
        self.content = content
        self.iso20022_Doclet = iso20022_Doclet
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def iso20022_Doclet(self):
        return self.__iso20022_Doclet

    @iso20022_Doclet.setter
    def iso20022_Doclet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_Doclet__iso20022_Doclet", None)
        self.__iso20022_Doclet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iso20022_RepositoryConcept29"):
                opp_val = getattr(old_value, "iso20022_RepositoryConcept29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iso20022_RepositoryConcept29"):
                opp_val = getattr(value, "iso20022_RepositoryConcept29", None)
                if opp_val is None:
                    setattr(value, "iso20022_RepositoryConcept29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class iso20022_RepositoryConcept(ModelEntity):

    def __init__(self, name: str, definition: str, example: str, registrationStatus: str, removalDate: date, iso20022_RepositoryConcept29: set["iso20022_Doclet"] = None, owner: set["iso20022_Constraint"] = None, iso20022_RepositoryConcept: set["iso20022_SemanticMarkup"] = None, RepositoryConcept: "iso20022_Constraint" = None):
        self.name = name
        self.definition = definition
        self.example = example
        self.registrationStatus = registrationStatus
        self.removalDate = removalDate
        self.iso20022_RepositoryConcept29 = iso20022_RepositoryConcept29 if iso20022_RepositoryConcept29 is not None else set()
        self.owner = owner if owner is not None else set()
        self.iso20022_RepositoryConcept = iso20022_RepositoryConcept if iso20022_RepositoryConcept is not None else set()
        self.RepositoryConcept = RepositoryConcept
        
    @property
    def registrationStatus(self) -> str:
        return self.__registrationStatus

    @registrationStatus.setter
    def registrationStatus(self, registrationStatus: str):
        self.__registrationStatus = registrationStatus

    @property
    def removalDate(self) -> date:
        return self.__removalDate

    @removalDate.setter
    def removalDate(self, removalDate: date):
        self.__removalDate = removalDate

    @property
    def definition(self) -> str:
        return self.__definition

    @definition.setter
    def definition(self, definition: str):
        self.__definition = definition

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def example(self) -> str:
        return self.__example

    @example.setter
    def example(self, example: str):
        self.__example = example

    @property
    def iso20022_RepositoryConcept(self):
        return self.__iso20022_RepositoryConcept

    @iso20022_RepositoryConcept.setter
    def iso20022_RepositoryConcept(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_RepositoryConcept__iso20022_RepositoryConcept", None)
        self.__iso20022_RepositoryConcept = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iso20022_SemanticMarkup"):
                    opp_val = getattr(item, "iso20022_SemanticMarkup", None)
                    
                    if opp_val == self:
                        setattr(item, "iso20022_SemanticMarkup", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iso20022_SemanticMarkup"):
                    opp_val = getattr(item, "iso20022_SemanticMarkup", None)
                    
                    setattr(item, "iso20022_SemanticMarkup", self)
                    

    @property
    def RepositoryConcept(self):
        return self.__RepositoryConcept

    @RepositoryConcept.setter
    def RepositoryConcept(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_RepositoryConcept__RepositoryConcept", None)
        self.__RepositoryConcept = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "constraint"):
                opp_val = getattr(old_value, "constraint", None)
                if opp_val == self:
                    setattr(old_value, "constraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "constraint"):
                opp_val = getattr(value, "constraint", None)
                setattr(value, "constraint", self)

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_RepositoryConcept__owner", None)
        self.__owner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Constraint"):
                    opp_val = getattr(item, "Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Constraint"):
                    opp_val = getattr(item, "Constraint", None)
                    
                    setattr(item, "Constraint", self)
                    

    @property
    def iso20022_RepositoryConcept29(self):
        return self.__iso20022_RepositoryConcept29

    @iso20022_RepositoryConcept29.setter
    def iso20022_RepositoryConcept29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_RepositoryConcept__iso20022_RepositoryConcept29", None)
        self.__iso20022_RepositoryConcept29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iso20022_Doclet"):
                    opp_val = getattr(item, "iso20022_Doclet", None)
                    
                    if opp_val == self:
                        setattr(item, "iso20022_Doclet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iso20022_Doclet"):
                    opp_val = getattr(item, "iso20022_Doclet", None)
                    
                    setattr(item, "iso20022_Doclet", self)
                    

    def RemovalDateRegistrationStatus(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement RemovalDateRegistrationStatus method
        pass

    def NameFirstLetterUppercase(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement NameFirstLetterUppercase method
        pass

class iso20022_Repository(ModelEntity):

    pass
class iso20022_MessageDefinitionIdentifier(ModelEntity):

    def __init__(self, businessArea: str, messageFunctionality: str, flavour: str, version: str, iso20022_MessageDefinitionIdentifier: "iso20022_MessageDefinition" = None):
        self.businessArea = businessArea
        self.messageFunctionality = messageFunctionality
        self.flavour = flavour
        self.version = version
        self.iso20022_MessageDefinitionIdentifier = iso20022_MessageDefinitionIdentifier
        
    @property
    def flavour(self) -> str:
        return self.__flavour

    @flavour.setter
    def flavour(self, flavour: str):
        self.__flavour = flavour

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def messageFunctionality(self) -> str:
        return self.__messageFunctionality

    @messageFunctionality.setter
    def messageFunctionality(self, messageFunctionality: str):
        self.__messageFunctionality = messageFunctionality

    @property
    def businessArea(self) -> str:
        return self.__businessArea

    @businessArea.setter
    def businessArea(self, businessArea: str):
        self.__businessArea = businessArea

    @property
    def iso20022_MessageDefinitionIdentifier(self):
        return self.__iso20022_MessageDefinitionIdentifier

    @iso20022_MessageDefinitionIdentifier.setter
    def iso20022_MessageDefinitionIdentifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_MessageDefinitionIdentifier__iso20022_MessageDefinitionIdentifier", None)
        self.__iso20022_MessageDefinitionIdentifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iso20022_MessageDefinition58"):
                opp_val = getattr(old_value, "iso20022_MessageDefinition58", None)
                if opp_val == self:
                    setattr(old_value, "iso20022_MessageDefinition58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iso20022_MessageDefinition58"):
                opp_val = getattr(value, "iso20022_MessageDefinition58", None)
                setattr(value, "iso20022_MessageDefinition58", self)

class iso20022_BroadcastList(ModelEntity):

    pass
class iso20022_SemanticMarkupElement(ModelEntity):

    def __init__(self, name: str, value: str, iso20022_SemanticMarkupElement: "iso20022_SemanticMarkup" = None):
        self.name = name
        self.value = value
        self.iso20022_SemanticMarkupElement = iso20022_SemanticMarkupElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def iso20022_SemanticMarkupElement(self):
        return self.__iso20022_SemanticMarkupElement

    @iso20022_SemanticMarkupElement.setter
    def iso20022_SemanticMarkupElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_SemanticMarkupElement__iso20022_SemanticMarkupElement", None)
        self.__iso20022_SemanticMarkupElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iso20022_SemanticMarkup32"):
                opp_val = getattr(old_value, "iso20022_SemanticMarkup32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iso20022_SemanticMarkup32"):
                opp_val = getattr(value, "iso20022_SemanticMarkup32", None)
                if opp_val is None:
                    setattr(value, "iso20022_SemanticMarkup32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class iso20022_Encoding(ModelEntity):

    pass
class iso20022_MessageInstance(ModelEntity):

    pass
class iso20022_BusinessProcessCatalogue(ModelEntity):

    def __init__(self, BusinessProcessCatalogue: "iso20022_TopLevelCatalogueEntry" = None, businessProcessCatalogue: "iso20022_Repository" = None, businessProcessCatalogue36: set["iso20022_TopLevelCatalogueEntry"] = None, BusinessProcessCatalogue40: "iso20022_Repository" = None):
        self.BusinessProcessCatalogue = BusinessProcessCatalogue
        self.businessProcessCatalogue = businessProcessCatalogue
        self.businessProcessCatalogue36 = businessProcessCatalogue36 if businessProcessCatalogue36 is not None else set()
        self.BusinessProcessCatalogue40 = BusinessProcessCatalogue40
        
    @property
    def businessProcessCatalogue36(self):
        return self.__businessProcessCatalogue36

    @businessProcessCatalogue36.setter
    def businessProcessCatalogue36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessProcessCatalogue__businessProcessCatalogue36", None)
        self.__businessProcessCatalogue36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TopLevelCatalogueEntry"):
                    opp_val = getattr(item, "TopLevelCatalogueEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "TopLevelCatalogueEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TopLevelCatalogueEntry"):
                    opp_val = getattr(item, "TopLevelCatalogueEntry", None)
                    
                    setattr(item, "TopLevelCatalogueEntry", self)
                    

    @property
    def BusinessProcessCatalogue(self):
        return self.__BusinessProcessCatalogue

    @BusinessProcessCatalogue.setter
    def BusinessProcessCatalogue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessProcessCatalogue__BusinessProcessCatalogue", None)
        self.__BusinessProcessCatalogue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "topLevelCatalogueEntry"):
                opp_val = getattr(old_value, "topLevelCatalogueEntry", None)
                if opp_val == self:
                    setattr(old_value, "topLevelCatalogueEntry", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "topLevelCatalogueEntry"):
                opp_val = getattr(value, "topLevelCatalogueEntry", None)
                setattr(value, "topLevelCatalogueEntry", self)

    @property
    def businessProcessCatalogue(self):
        return self.__businessProcessCatalogue

    @businessProcessCatalogue.setter
    def businessProcessCatalogue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessProcessCatalogue__businessProcessCatalogue", None)
        self.__businessProcessCatalogue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Repository"):
                opp_val = getattr(old_value, "Repository", None)
                if opp_val == self:
                    setattr(old_value, "Repository", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Repository"):
                opp_val = getattr(value, "Repository", None)
                setattr(value, "Repository", self)

    @property
    def BusinessProcessCatalogue40(self):
        return self.__BusinessProcessCatalogue40

    @BusinessProcessCatalogue40.setter
    def BusinessProcessCatalogue40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iso20022_BusinessProcessCatalogue__BusinessProcessCatalogue40", None)
        self.__BusinessProcessCatalogue40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository39"):
                opp_val = getattr(old_value, "repository39", None)
                if opp_val == self:
                    setattr(old_value, "repository39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository39"):
                opp_val = getattr(value, "repository39", None)
                setattr(value, "repository39", self)

    def EntriesHaveUniqueName(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement EntriesHaveUniqueName method
        pass

class iso20022_Address(ModelEntity):

    pass