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
class Namespace(Enum):
    any = "any"
    other = "other"
    list = "list"
class Visibility(Enum):
    _ = "_"
    Outdated = "Outdated"
    Draft = "Draft"
    DoNotShow = "DoNotShow"
class RegistrationStatus(Enum):
    NO_STATUS = "NO_STATUS"
    PROVISIONALLY_REGISTERED = "PROVISIONALLY_REGISTERED"
    REGISTERED = "REGISTERED"
    OBSOLETE = "OBSOLETE"
class Aggregation(Enum):
    NONE = "NONE"
    COMPOSITE = "COMPOSITE"
    SHARED = "SHARED"


############################################
# Definition of Classes
############################################

class MessageSet:

    pass
class ISO20022_SWIFTSolution(MessageSet):

    def __init__(self, serviceName: str):
        self.serviceName = serviceName
        
    @property
    def serviceName(self) -> str:
        return self.__serviceName

    @serviceName.setter
    def serviceName(self, serviceName: str):
        self.__serviceName = serviceName

class AbstractTimeConcept:

    pass
class ISO20022_XSDYear(AbstractTimeConcept):

    pass
class ISO20022_XSDDuration(AbstractTimeConcept):

    pass
class ISO20022_XSDDateTime(AbstractTimeConcept):

    pass
class ISO20022_XSDMonthDay(AbstractTimeConcept):

    pass
class ISO20022_XSDYearMonth(AbstractTimeConcept):

    pass
class ISO20022_XSDMonth(AbstractTimeConcept):

    pass
class ISO20022_XSDDay(AbstractTimeConcept):

    pass
class ISO20022_XSDTime(AbstractTimeConcept):

    pass
class ISO20022_XSDDate(AbstractTimeConcept):

    pass
class MessageDefinition:

    pass
class ISO20022_ApplicationHeader(MessageDefinition):

    pass
class XSDDecimal:

    pass
class ISO20022_Quantity(XSDDecimal):

    def __init__(self, unitCode: str):
        self.unitCode = unitCode
        
    @property
    def unitCode(self) -> str:
        return self.__unitCode

    @unitCode.setter
    def unitCode(self, unitCode: str):
        self.__unitCode = unitCode

class ISO20022_Amount(XSDDecimal):

    pass
class ISO20022_Rate(XSDDecimal):

    def __init__(self, baseUnitCode: str, baseValue: str):
        self.baseUnitCode = baseUnitCode
        self.baseValue = baseValue
        
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

class XSDBoolean:

    pass
class ISO20022_Indicator(XSDBoolean):

    def __init__(self, meaningWhenTrue: str, meaningWhenFalse: str, pattern: str):
        self.meaningWhenTrue = meaningWhenTrue
        self.meaningWhenFalse = meaningWhenFalse
        self.pattern = pattern
        
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

    @property
    def pattern(self) -> str:
        return self.__pattern

    @pattern.setter
    def pattern(self, pattern: str):
        self.__pattern = pattern

class DataType:

    pass
class ISO20022_XSDBoolean(DataType):

    pass
class ISO20022_AbstractTimeConcept(DataType):

    def __init__(self, minExclusive: str, maxInclusive: str, maxExclusive: str, minInclusive: str, pattern: str):
        self.minExclusive = minExclusive
        self.maxInclusive = maxInclusive
        self.maxExclusive = maxExclusive
        self.minInclusive = minInclusive
        self.pattern = pattern
        
    @property
    def minInclusive(self) -> str:
        return self.__minInclusive

    @minInclusive.setter
    def minInclusive(self, minInclusive: str):
        self.__minInclusive = minInclusive

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

class ISO20022_XSDBinary(DataType):

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

class ISO20022_XSDDecimal(DataType):

    def __init__(self, minInclusive: str, minExclusive: str, maxInclusive: str, maxExclusive: str, totalDigits: str, fractionDigits: str, pattern: str):
        self.minInclusive = minInclusive
        self.minExclusive = minExclusive
        self.maxInclusive = maxInclusive
        self.maxExclusive = maxExclusive
        self.totalDigits = totalDigits
        self.fractionDigits = fractionDigits
        self.pattern = pattern
        
    @property
    def totalDigits(self) -> str:
        return self.__totalDigits

    @totalDigits.setter
    def totalDigits(self, totalDigits: str):
        self.__totalDigits = totalDigits

    @property
    def maxExclusive(self) -> str:
        return self.__maxExclusive

    @maxExclusive.setter
    def maxExclusive(self, maxExclusive: str):
        self.__maxExclusive = maxExclusive

    @property
    def minInclusive(self) -> str:
        return self.__minInclusive

    @minInclusive.setter
    def minInclusive(self, minInclusive: str):
        self.__minInclusive = minInclusive

    @property
    def pattern(self) -> str:
        return self.__pattern

    @pattern.setter
    def pattern(self, pattern: str):
        self.__pattern = pattern

    @property
    def fractionDigits(self) -> str:
        return self.__fractionDigits

    @fractionDigits.setter
    def fractionDigits(self, fractionDigits: str):
        self.__fractionDigits = fractionDigits

    @property
    def minExclusive(self) -> str:
        return self.__minExclusive

    @minExclusive.setter
    def minExclusive(self, minExclusive: str):
        self.__minExclusive = minExclusive

    @property
    def maxInclusive(self) -> str:
        return self.__maxInclusive

    @maxInclusive.setter
    def maxInclusive(self, maxInclusive: str):
        self.__maxInclusive = maxInclusive

class ISO20022_XSDString(DataType):

    def __init__(self, minLength: str, maxLength: str, length: str, pattern: str):
        self.minLength = minLength
        self.maxLength = maxLength
        self.length = length
        self.pattern = pattern
        
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

    @property
    def minLength(self) -> str:
        return self.__minLength

    @minLength.setter
    def minLength(self, minLength: str):
        self.__minLength = minLength

class XSDString:

    pass
class ISO20022_CodeSet(XSDString):

    def __init__(self, identificationScheme: str, CodeSet: "ISO20022_Code" = None, CodeSet159: "ISO20022_CodeSet" = None, derivation158: "ISO20022_CodeSet" = None, CodeSet163: "ISO20022_CodeSet" = None, trace162: set["ISO20022_CodeSet"] = None, owner165: set["ISO20022_Code"] = None):
        self.identificationScheme = identificationScheme
        self.CodeSet = CodeSet
        self.CodeSet159 = CodeSet159
        self.derivation158 = derivation158
        self.CodeSet163 = CodeSet163
        self.trace162 = trace162 if trace162 is not None else set()
        self.owner165 = owner165 if owner165 is not None else set()
        
    @property
    def identificationScheme(self) -> str:
        return self.__identificationScheme

    @identificationScheme.setter
    def identificationScheme(self, identificationScheme: str):
        self.__identificationScheme = identificationScheme

    @property
    def CodeSet163(self):
        return self.__CodeSet163

    @CodeSet163.setter
    def CodeSet163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_CodeSet__CodeSet163", None)
        self.__CodeSet163 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace162"):
                opp_val = getattr(old_value, "trace162", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace162"):
                opp_val = getattr(value, "trace162", None)
                if opp_val is None:
                    setattr(value, "trace162", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def owner165(self):
        return self.__owner165

    @owner165.setter
    def owner165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_CodeSet__owner165", None)
        self.__owner165 = value if value is not None else set()
        
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
    def CodeSet159(self):
        return self.__CodeSet159

    @CodeSet159.setter
    def CodeSet159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_CodeSet__CodeSet159", None)
        self.__CodeSet159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "derivation158"):
                opp_val = getattr(old_value, "derivation158", None)
                if opp_val == self:
                    setattr(old_value, "derivation158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "derivation158"):
                opp_val = getattr(value, "derivation158", None)
                setattr(value, "derivation158", self)

    @property
    def derivation158(self):
        return self.__derivation158

    @derivation158.setter
    def derivation158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_CodeSet__derivation158", None)
        self.__derivation158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CodeSet159"):
                opp_val = getattr(old_value, "CodeSet159", None)
                if opp_val == self:
                    setattr(old_value, "CodeSet159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CodeSet159"):
                opp_val = getattr(value, "CodeSet159", None)
                setattr(value, "CodeSet159", self)

    @property
    def CodeSet(self):
        return self.__CodeSet

    @CodeSet.setter
    def CodeSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_CodeSet__CodeSet", None)
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

    @property
    def trace162(self):
        return self.__trace162

    @trace162.setter
    def trace162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_CodeSet__trace162", None)
        self.__trace162 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CodeSet163"):
                    opp_val = getattr(item, "CodeSet163", None)
                    
                    if opp_val == self:
                        setattr(item, "CodeSet163", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CodeSet163"):
                    opp_val = getattr(item, "CodeSet163", None)
                    
                    setattr(item, "CodeSet163", self)
                    

class ISO20022_XSDID(XSDString):

    pass
class ISO20022_Text(XSDString):

    pass
class ISO20022_IdentifierSet(XSDString):

    def __init__(self, identificationScheme: str, ISO20022_IdentifierSet: "ISO20022_Amount" = None):
        self.identificationScheme = identificationScheme
        self.ISO20022_IdentifierSet = ISO20022_IdentifierSet
        
    @property
    def identificationScheme(self) -> str:
        return self.__identificationScheme

    @identificationScheme.setter
    def identificationScheme(self, identificationScheme: str):
        self.__identificationScheme = identificationScheme

    @property
    def ISO20022_IdentifierSet(self):
        return self.__ISO20022_IdentifierSet

    @ISO20022_IdentifierSet.setter
    def ISO20022_IdentifierSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_IdentifierSet__ISO20022_IdentifierSet", None)
        self.__ISO20022_IdentifierSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ISO20022_Amount"):
                opp_val = getattr(old_value, "ISO20022_Amount", None)
                if opp_val == self:
                    setattr(old_value, "ISO20022_Amount", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ISO20022_Amount"):
                opp_val = getattr(value, "ISO20022_Amount", None)
                setattr(value, "ISO20022_Amount", self)

class MessageElementContainer:

    pass
class ISO20022_ChoiceComponent(MessageElementContainer):

    def __init__(self):
        
    def AtLeastOneProperty(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement AtLeastOneProperty method
        pass

class ISO20022_MessageComponent(MessageElementContainer):

    pass
class ISO20022_MessageDefinitionIdentifier:

    def __init__(self, businessArea: str, messageFunctionality: str, flavour: str, version: str, ISO20022_MessageDefinitionIdentifier: "ISO20022_MessageDefinition" = None):
        self.businessArea = businessArea
        self.messageFunctionality = messageFunctionality
        self.flavour = flavour
        self.version = version
        self.ISO20022_MessageDefinitionIdentifier = ISO20022_MessageDefinitionIdentifier
        
    @property
    def messageFunctionality(self) -> str:
        return self.__messageFunctionality

    @messageFunctionality.setter
    def messageFunctionality(self, messageFunctionality: str):
        self.__messageFunctionality = messageFunctionality

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
    def businessArea(self) -> str:
        return self.__businessArea

    @businessArea.setter
    def businessArea(self, businessArea: str):
        self.__businessArea = businessArea

    @property
    def ISO20022_MessageDefinitionIdentifier(self):
        return self.__ISO20022_MessageDefinitionIdentifier

    @ISO20022_MessageDefinitionIdentifier.setter
    def ISO20022_MessageDefinitionIdentifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageDefinitionIdentifier__ISO20022_MessageDefinitionIdentifier", None)
        self.__ISO20022_MessageDefinitionIdentifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ISO20022_MessageDefinition110"):
                opp_val = getattr(old_value, "ISO20022_MessageDefinition110", None)
                if opp_val == self:
                    setattr(old_value, "ISO20022_MessageDefinition110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ISO20022_MessageDefinition110"):
                opp_val = getattr(value, "ISO20022_MessageDefinition110", None)
                setattr(value, "ISO20022_MessageDefinition110", self)

class TopLevelCatalogueEntry:

    pass
class ISO20022_SyntaxMessageScheme(TopLevelCatalogueEntry):

    pass
class ISO20022_BusinessArea(TopLevelCatalogueEntry):

    def __init__(self, code: str, BusinessArea: "ISO20022_MessageDefinition" = None, businessArea: set["ISO20022_MessageDefinition"] = None):
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
    def BusinessArea(self):
        return self.__BusinessArea

    @BusinessArea.setter
    def BusinessArea(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_BusinessArea__BusinessArea", None)
        self.__BusinessArea = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "messageDefinition"):
                opp_val = getattr(old_value, "messageDefinition", None)
                if opp_val == self:
                    setattr(old_value, "messageDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "messageDefinition"):
                opp_val = getattr(value, "messageDefinition", None)
                setattr(value, "messageDefinition", self)

    @property
    def businessArea(self):
        return self.__businessArea

    @businessArea.setter
    def businessArea(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_BusinessArea__businessArea", None)
        self.__businessArea = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MessageDefinition115"):
                    opp_val = getattr(item, "MessageDefinition115", None)
                    
                    if opp_val == self:
                        setattr(item, "MessageDefinition115", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MessageDefinition115"):
                    opp_val = getattr(item, "MessageDefinition115", None)
                    
                    setattr(item, "MessageDefinition115", self)
                    

class ISO20022_MessageChoreography(TopLevelCatalogueEntry):

    pass
class ISO20022_MessageSet(TopLevelCatalogueEntry):

    def __init__(self, MessageSet: "ISO20022_Encoding" = None, messageSet94: set["ISO20022_Encoding"] = None, messageSet: set["ISO20022_MessageDefinition"] = None, messageSet90: set["ISO20022_Interaction"] = None, generatedFor: set["ISO20022_Syntax"] = None, MessageSet113: "ISO20022_MessageDefinition" = None, MessageSet136: "ISO20022_Interaction" = None, MessageSet150: "ISO20022_Syntax" = None):
        self.MessageSet = MessageSet
        self.messageSet94 = messageSet94 if messageSet94 is not None else set()
        self.messageSet = messageSet if messageSet is not None else set()
        self.messageSet90 = messageSet90 if messageSet90 is not None else set()
        self.generatedFor = generatedFor if generatedFor is not None else set()
        self.MessageSet113 = MessageSet113
        self.MessageSet136 = MessageSet136
        self.MessageSet150 = MessageSet150
        
    @property
    def MessageSet(self):
        return self.__MessageSet

    @MessageSet.setter
    def MessageSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageSet__MessageSet", None)
        self.__MessageSet = value
        
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
    def MessageSet150(self):
        return self.__MessageSet150

    @MessageSet150.setter
    def MessageSet150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageSet__MessageSet150", None)
        self.__MessageSet150 = value
        
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
    def messageSet94(self):
        return self.__messageSet94

    @messageSet94.setter
    def messageSet94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageSet__messageSet94", None)
        self.__messageSet94 = value if value is not None else set()
        
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
    def messageSet90(self):
        return self.__messageSet90

    @messageSet90.setter
    def messageSet90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageSet__messageSet90", None)
        self.__messageSet90 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Interaction"):
                    opp_val = getattr(item, "Interaction", None)
                    
                    if opp_val == self:
                        setattr(item, "Interaction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Interaction"):
                    opp_val = getattr(item, "Interaction", None)
                    
                    setattr(item, "Interaction", self)
                    

    @property
    def MessageSet136(self):
        return self.__MessageSet136

    @MessageSet136.setter
    def MessageSet136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageSet__MessageSet136", None)
        self.__MessageSet136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "interactions"):
                opp_val = getattr(old_value, "interactions", None)
                if opp_val == self:
                    setattr(old_value, "interactions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "interactions"):
                opp_val = getattr(value, "interactions", None)
                setattr(value, "interactions", self)

    @property
    def MessageSet113(self):
        return self.__MessageSet113

    @MessageSet113.setter
    def MessageSet113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageSet__MessageSet113", None)
        self.__MessageSet113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "messageDefinition112"):
                opp_val = getattr(old_value, "messageDefinition112", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "messageDefinition112"):
                opp_val = getattr(value, "messageDefinition112", None)
                if opp_val is None:
                    setattr(value, "messageDefinition112", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def generatedFor(self):
        return self.__generatedFor

    @generatedFor.setter
    def generatedFor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageSet__generatedFor", None)
        self.__generatedFor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Syntax92"):
                    opp_val = getattr(item, "Syntax92", None)
                    
                    if opp_val == self:
                        setattr(item, "Syntax92", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Syntax92"):
                    opp_val = getattr(item, "Syntax92", None)
                    
                    setattr(item, "Syntax92", self)
                    

    @property
    def messageSet(self):
        return self.__messageSet

    @messageSet.setter
    def messageSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageSet__messageSet", None)
        self.__messageSet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MessageDefinition"):
                    opp_val = getattr(item, "MessageDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "MessageDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MessageDefinition"):
                    opp_val = getattr(item, "MessageDefinition", None)
                    
                    setattr(item, "MessageDefinition", self)
                    

    def GeneratedSyntaxDerivation(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement GeneratedSyntaxDerivation method
        pass

class MessageComponentType:

    pass
class ISO20022_ExternalSchema(MessageComponentType):

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

class ISO20022_UserDefined(MessageComponentType):

    def __init__(self, _: str, namespaceList: str, processContents: str):
        self._ = _
        self.namespaceList = namespaceList
        self.processContents = processContents
        
    @property
    def namespaceList(self) -> str:
        return self.__namespaceList

    @namespaceList.setter
    def namespaceList(self, namespaceList: str):
        self.__namespaceList = namespaceList

    @property
    def processContents(self) -> str:
        return self.__processContents

    @processContents.setter
    def processContents(self, processContents: str):
        self.__processContents = processContents

    @property
    def _(self) -> str:
        return self.___

    @_.setter
    def _(self, _: str):
        self.___ = _

class BusinessElement:

    pass
class ISO20022_BusinessAttribute(BusinessElement):

    def __init__(self, ISO20022_BusinessAttribute: "ISO20022_DataType" = None, ISO20022_BusinessAttribute154: "ISO20022_BusinessComponent" = None):
        self.ISO20022_BusinessAttribute = ISO20022_BusinessAttribute
        self.ISO20022_BusinessAttribute154 = ISO20022_BusinessAttribute154
        
    @property
    def ISO20022_BusinessAttribute154(self):
        return self.__ISO20022_BusinessAttribute154

    @ISO20022_BusinessAttribute154.setter
    def ISO20022_BusinessAttribute154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_BusinessAttribute__ISO20022_BusinessAttribute154", None)
        self.__ISO20022_BusinessAttribute154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ISO20022_BusinessComponent"):
                opp_val = getattr(old_value, "ISO20022_BusinessComponent", None)
                if opp_val == self:
                    setattr(old_value, "ISO20022_BusinessComponent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ISO20022_BusinessComponent"):
                opp_val = getattr(value, "ISO20022_BusinessComponent", None)
                setattr(value, "ISO20022_BusinessComponent", self)

    @property
    def ISO20022_BusinessAttribute(self):
        return self.__ISO20022_BusinessAttribute

    @ISO20022_BusinessAttribute.setter
    def ISO20022_BusinessAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_BusinessAttribute__ISO20022_BusinessAttribute", None)
        self.__ISO20022_BusinessAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ISO20022_DataType152"):
                opp_val = getattr(old_value, "ISO20022_DataType152", None)
                if opp_val == self:
                    setattr(old_value, "ISO20022_DataType152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ISO20022_DataType152"):
                opp_val = getattr(value, "ISO20022_DataType152", None)
                setattr(value, "ISO20022_DataType152", self)

    def NoDerivingCodeSetType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement NoDerivingCodeSetType method
        pass

    def BusinessAttributeHasExactlyOneType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement BusinessAttributeHasExactlyOneType method
        pass

class LogicalType:

    pass
class ISO20022_BusinessAssociationEnd(BusinessElement):

    def __init__(self, aggregation: str, BusinessAssociationEnd: "ISO20022_BusinessComponent" = None, ISO20022_BusinessAssociationEnd: "ISO20022_BusinessAssociationEnd" = None, ISO20022_BusinessAssociationEnd75: "ISO20022_BusinessAssociationEnd" = None, associationDomain: "ISO20022_BusinessComponent" = None):
        self.aggregation = aggregation
        self.BusinessAssociationEnd = BusinessAssociationEnd
        self.ISO20022_BusinessAssociationEnd = ISO20022_BusinessAssociationEnd
        self.ISO20022_BusinessAssociationEnd75 = ISO20022_BusinessAssociationEnd75
        self.associationDomain = associationDomain
        
    @property
    def aggregation(self) -> str:
        return self.__aggregation

    @aggregation.setter
    def aggregation(self, aggregation: str):
        self.__aggregation = aggregation

    @property
    def ISO20022_BusinessAssociationEnd75(self):
        return self.__ISO20022_BusinessAssociationEnd75

    @ISO20022_BusinessAssociationEnd75.setter
    def ISO20022_BusinessAssociationEnd75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_BusinessAssociationEnd__ISO20022_BusinessAssociationEnd75", None)
        self.__ISO20022_BusinessAssociationEnd75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ISO20022_BusinessAssociationEnd"):
                opp_val = getattr(old_value, "ISO20022_BusinessAssociationEnd", None)
                if opp_val == self:
                    setattr(old_value, "ISO20022_BusinessAssociationEnd", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ISO20022_BusinessAssociationEnd"):
                opp_val = getattr(value, "ISO20022_BusinessAssociationEnd", None)
                setattr(value, "ISO20022_BusinessAssociationEnd", self)

    @property
    def ISO20022_BusinessAssociationEnd(self):
        return self.__ISO20022_BusinessAssociationEnd

    @ISO20022_BusinessAssociationEnd.setter
    def ISO20022_BusinessAssociationEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_BusinessAssociationEnd__ISO20022_BusinessAssociationEnd", None)
        self.__ISO20022_BusinessAssociationEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ISO20022_BusinessAssociationEnd75"):
                opp_val = getattr(old_value, "ISO20022_BusinessAssociationEnd75", None)
                if opp_val == self:
                    setattr(old_value, "ISO20022_BusinessAssociationEnd75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ISO20022_BusinessAssociationEnd75"):
                opp_val = getattr(value, "ISO20022_BusinessAssociationEnd75", None)
                setattr(value, "ISO20022_BusinessAssociationEnd75", self)

    @property
    def BusinessAssociationEnd(self):
        return self.__BusinessAssociationEnd

    @BusinessAssociationEnd.setter
    def BusinessAssociationEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_BusinessAssociationEnd__BusinessAssociationEnd", None)
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
    def associationDomain(self):
        return self.__associationDomain

    @associationDomain.setter
    def associationDomain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_BusinessAssociationEnd__associationDomain", None)
        self.__associationDomain = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BusinessComponent78"):
                opp_val = getattr(old_value, "BusinessComponent78", None)
                if opp_val == self:
                    setattr(old_value, "BusinessComponent78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BusinessComponent78"):
                opp_val = getattr(value, "BusinessComponent78", None)
                setattr(value, "BusinessComponent78", self)

    def ContextConsistentWithType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ContextConsistentWithType method
        pass

    def AtMostOneAggregatedEnd(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement AtMostOneAggregatedEnd method
        pass

class BusinessConcept:

    pass
class TopLevelDictionaryEntry:

    pass
class ISO20022_EndPointCategory(TopLevelDictionaryEntry):

    pass
class BusinessElementType:

    pass
class ISO20022_DataType(BusinessElementType, TopLevelDictionaryEntry, LogicalType):

    pass
class Type:

    pass
class ISO20022_MessageDefinition(Type):

    def __init__(self, xmlTag: str, previousVersionDocumentation: str, urn: str, xmlName: str, rootElement: str, visibility: str, MessageDefinition: "ISO20022_MessageSet" = None, MessageDefinition97: "ISO20022_MessageDefinition" = None, subsets: "ISO20022_MessageDefinition" = None, MessageDefinition100: "ISO20022_MessageDefinition" = None, master: set["ISO20022_MessageDefinition"] = None, messageDefinition108: set["ISO20022_MessageChoreography"] = None, messageDefinition: "ISO20022_BusinessArea" = None, messageDefinition103: set["ISO20022_Xor"] = None, ISO20022_MessageDefinition: set["ISO20022_MessageBuildingBlock"] = None, messageDefinitionTrace: set["ISO20022_SyntaxMessageScheme"] = None, ISO20022_MessageDefinition110: "ISO20022_MessageDefinitionIdentifier" = None, messageDefinition112: set["ISO20022_MessageSet"] = None, MessageDefinition115: "ISO20022_BusinessArea" = None, MessageDefinition123: "ISO20022_Xor" = None, MessageDefinition128: "ISO20022_SyntaxMessageScheme" = None, MessageDefinition130: "ISO20022_MessageChoreography" = None):
        self.xmlTag = xmlTag
        self.previousVersionDocumentation = previousVersionDocumentation
        self.urn = urn
        self.xmlName = xmlName
        self.rootElement = rootElement
        self.visibility = visibility
        self.MessageDefinition = MessageDefinition
        self.MessageDefinition97 = MessageDefinition97
        self.subsets = subsets
        self.MessageDefinition100 = MessageDefinition100
        self.master = master if master is not None else set()
        self.messageDefinition108 = messageDefinition108 if messageDefinition108 is not None else set()
        self.messageDefinition = messageDefinition
        self.messageDefinition103 = messageDefinition103 if messageDefinition103 is not None else set()
        self.ISO20022_MessageDefinition = ISO20022_MessageDefinition if ISO20022_MessageDefinition is not None else set()
        self.messageDefinitionTrace = messageDefinitionTrace if messageDefinitionTrace is not None else set()
        self.ISO20022_MessageDefinition110 = ISO20022_MessageDefinition110
        self.messageDefinition112 = messageDefinition112 if messageDefinition112 is not None else set()
        self.MessageDefinition115 = MessageDefinition115
        self.MessageDefinition123 = MessageDefinition123
        self.MessageDefinition128 = MessageDefinition128
        self.MessageDefinition130 = MessageDefinition130
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def xmlTag(self) -> str:
        return self.__xmlTag

    @xmlTag.setter
    def xmlTag(self, xmlTag: str):
        self.__xmlTag = xmlTag

    @property
    def rootElement(self) -> str:
        return self.__rootElement

    @rootElement.setter
    def rootElement(self, rootElement: str):
        self.__rootElement = rootElement

    @property
    def xmlName(self) -> str:
        return self.__xmlName

    @xmlName.setter
    def xmlName(self, xmlName: str):
        self.__xmlName = xmlName

    @property
    def previousVersionDocumentation(self) -> str:
        return self.__previousVersionDocumentation

    @previousVersionDocumentation.setter
    def previousVersionDocumentation(self, previousVersionDocumentation: str):
        self.__previousVersionDocumentation = previousVersionDocumentation

    @property
    def urn(self) -> str:
        return self.__urn

    @urn.setter
    def urn(self, urn: str):
        self.__urn = urn

    @property
    def messageDefinition(self):
        return self.__messageDefinition

    @messageDefinition.setter
    def messageDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageDefinition__messageDefinition", None)
        self.__messageDefinition = value
        
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
    def MessageDefinition100(self):
        return self.__MessageDefinition100

    @MessageDefinition100.setter
    def MessageDefinition100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageDefinition__MessageDefinition100", None)
        self.__MessageDefinition100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "master"):
                opp_val = getattr(old_value, "master", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "master"):
                opp_val = getattr(value, "master", None)
                if opp_val is None:
                    setattr(value, "master", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MessageDefinition128(self):
        return self.__MessageDefinition128

    @MessageDefinition128.setter
    def MessageDefinition128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageDefinition__MessageDefinition128", None)
        self.__MessageDefinition128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "derivation127"):
                opp_val = getattr(old_value, "derivation127", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "derivation127"):
                opp_val = getattr(value, "derivation127", None)
                if opp_val is None:
                    setattr(value, "derivation127", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MessageDefinition130(self):
        return self.__MessageDefinition130

    @MessageDefinition130.setter
    def MessageDefinition130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageDefinition__MessageDefinition130", None)
        self.__MessageDefinition130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "messageChoreography"):
                opp_val = getattr(old_value, "messageChoreography", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "messageChoreography"):
                opp_val = getattr(value, "messageChoreography", None)
                if opp_val is None:
                    setattr(value, "messageChoreography", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def subsets(self):
        return self.__subsets

    @subsets.setter
    def subsets(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageDefinition__subsets", None)
        self.__subsets = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MessageDefinition97"):
                opp_val = getattr(old_value, "MessageDefinition97", None)
                if opp_val == self:
                    setattr(old_value, "MessageDefinition97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MessageDefinition97"):
                opp_val = getattr(value, "MessageDefinition97", None)
                setattr(value, "MessageDefinition97", self)

    @property
    def ISO20022_MessageDefinition110(self):
        return self.__ISO20022_MessageDefinition110

    @ISO20022_MessageDefinition110.setter
    def ISO20022_MessageDefinition110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageDefinition__ISO20022_MessageDefinition110", None)
        self.__ISO20022_MessageDefinition110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ISO20022_MessageDefinitionIdentifier"):
                opp_val = getattr(old_value, "ISO20022_MessageDefinitionIdentifier", None)
                if opp_val == self:
                    setattr(old_value, "ISO20022_MessageDefinitionIdentifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ISO20022_MessageDefinitionIdentifier"):
                opp_val = getattr(value, "ISO20022_MessageDefinitionIdentifier", None)
                setattr(value, "ISO20022_MessageDefinitionIdentifier", self)

    @property
    def messageDefinition103(self):
        return self.__messageDefinition103

    @messageDefinition103.setter
    def messageDefinition103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageDefinition__messageDefinition103", None)
        self.__messageDefinition103 = value if value is not None else set()
        
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
    def master(self):
        return self.__master

    @master.setter
    def master(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageDefinition__master", None)
        self.__master = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MessageDefinition100"):
                    opp_val = getattr(item, "MessageDefinition100", None)
                    
                    if opp_val == self:
                        setattr(item, "MessageDefinition100", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MessageDefinition100"):
                    opp_val = getattr(item, "MessageDefinition100", None)
                    
                    setattr(item, "MessageDefinition100", self)
                    

    @property
    def MessageDefinition97(self):
        return self.__MessageDefinition97

    @MessageDefinition97.setter
    def MessageDefinition97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageDefinition__MessageDefinition97", None)
        self.__MessageDefinition97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subsets"):
                opp_val = getattr(old_value, "subsets", None)
                if opp_val == self:
                    setattr(old_value, "subsets", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subsets"):
                opp_val = getattr(value, "subsets", None)
                setattr(value, "subsets", self)

    @property
    def MessageDefinition123(self):
        return self.__MessageDefinition123

    @MessageDefinition123.setter
    def MessageDefinition123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageDefinition__MessageDefinition123", None)
        self.__MessageDefinition123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xors122"):
                opp_val = getattr(old_value, "xors122", None)
                if opp_val == self:
                    setattr(old_value, "xors122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xors122"):
                opp_val = getattr(value, "xors122", None)
                setattr(value, "xors122", self)

    @property
    def MessageDefinition(self):
        return self.__MessageDefinition

    @MessageDefinition.setter
    def MessageDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageDefinition__MessageDefinition", None)
        self.__MessageDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "messageSet"):
                opp_val = getattr(old_value, "messageSet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "messageSet"):
                opp_val = getattr(value, "messageSet", None)
                if opp_val is None:
                    setattr(value, "messageSet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def messageDefinition108(self):
        return self.__messageDefinition108

    @messageDefinition108.setter
    def messageDefinition108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageDefinition__messageDefinition108", None)
        self.__messageDefinition108 = value if value is not None else set()
        
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
    def messageDefinitionTrace(self):
        return self.__messageDefinitionTrace

    @messageDefinitionTrace.setter
    def messageDefinitionTrace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageDefinition__messageDefinitionTrace", None)
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
    def ISO20022_MessageDefinition(self):
        return self.__ISO20022_MessageDefinition

    @ISO20022_MessageDefinition.setter
    def ISO20022_MessageDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageDefinition__ISO20022_MessageDefinition", None)
        self.__ISO20022_MessageDefinition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ISO20022_MessageBuildingBlock105"):
                    opp_val = getattr(item, "ISO20022_MessageBuildingBlock105", None)
                    
                    if opp_val == self:
                        setattr(item, "ISO20022_MessageBuildingBlock105", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ISO20022_MessageBuildingBlock105"):
                    opp_val = getattr(item, "ISO20022_MessageBuildingBlock105", None)
                    
                    setattr(item, "ISO20022_MessageBuildingBlock105", self)
                    

    @property
    def MessageDefinition115(self):
        return self.__MessageDefinition115

    @MessageDefinition115.setter
    def MessageDefinition115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageDefinition__MessageDefinition115", None)
        self.__MessageDefinition115 = value
        
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
    def messageDefinition112(self):
        return self.__messageDefinition112

    @messageDefinition112.setter
    def messageDefinition112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageDefinition__messageDefinition112", None)
        self.__messageDefinition112 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MessageSet113"):
                    opp_val = getattr(item, "MessageSet113", None)
                    
                    if opp_val == self:
                        setattr(item, "MessageSet113", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MessageSet113"):
                    opp_val = getattr(item, "MessageSet113", None)
                    
                    setattr(item, "MessageSet113", self)
                    

    def BusinessAreaNameMatch(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement BusinessAreaNameMatch method
        pass

class ISO20022_BusinessElementType(Type):

    pass
class ISO20022_MultiplicityEntity(ABC):

    def __init__(self, maxOccurs: str, minOccurs: str):
        self.maxOccurs = maxOccurs
        self.minOccurs = minOccurs
        
    @property
    def minOccurs(self) -> str:
        return self.__minOccurs

    @minOccurs.setter
    def minOccurs(self, minOccurs: str):
        self.__minOccurs = minOccurs

    @property
    def maxOccurs(self) -> str:
        return self.__maxOccurs

    @maxOccurs.setter
    def maxOccurs(self, maxOccurs: str):
        self.__maxOccurs = maxOccurs

class MultiplicityEntity:

    pass
class RepositoryConcept:

    pass
class ISO20022_Xor(RepositoryConcept):

    pass
class ISO20022_BusinessRole(RepositoryConcept):

    pass
class ISO20022_Diagram(RepositoryConcept):

    def __init__(self, content: str, location: str, Diagram: "ISO20022_Repository" = None, diagrams: "ISO20022_Repository" = None, ISO20022_Diagram: "ISO20022_Interaction" = None):
        self.content = content
        self.location = location
        self.Diagram = Diagram
        self.diagrams = diagrams
        self.ISO20022_Diagram = ISO20022_Diagram
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def diagrams(self):
        return self.__diagrams

    @diagrams.setter
    def diagrams(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_Diagram__diagrams", None)
        self.__diagrams = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Repository61"):
                opp_val = getattr(old_value, "Repository61", None)
                if opp_val == self:
                    setattr(old_value, "Repository61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Repository61"):
                opp_val = getattr(value, "Repository61", None)
                setattr(value, "Repository61", self)

    @property
    def Diagram(self):
        return self.__Diagram

    @Diagram.setter
    def Diagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_Diagram__Diagram", None)
        self.__Diagram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository50"):
                opp_val = getattr(old_value, "repository50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository50"):
                opp_val = getattr(value, "repository50", None)
                if opp_val is None:
                    setattr(value, "repository50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ISO20022_Diagram(self):
        return self.__ISO20022_Diagram

    @ISO20022_Diagram.setter
    def ISO20022_Diagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_Diagram__ISO20022_Diagram", None)
        self.__ISO20022_Diagram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ISO20022_Interaction"):
                opp_val = getattr(old_value, "ISO20022_Interaction", None)
                if opp_val == self:
                    setattr(old_value, "ISO20022_Interaction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ISO20022_Interaction"):
                opp_val = getattr(value, "ISO20022_Interaction", None)
                setattr(value, "ISO20022_Interaction", self)

class ISO20022_Interaction(RepositoryConcept):

    def __init__(self, location: str, Interaction: "ISO20022_MessageSet" = None, interaction133: set["ISO20022_InteractionMessage"] = None, interaction: set["ISO20022_InteractionActor"] = None, Interaction139: "ISO20022_InteractionActor" = None, ISO20022_Interaction: "ISO20022_Diagram" = None, interactions: "ISO20022_MessageSet" = None, Interaction146: "ISO20022_InteractionMessage" = None):
        self.location = location
        self.Interaction = Interaction
        self.interaction133 = interaction133 if interaction133 is not None else set()
        self.interaction = interaction if interaction is not None else set()
        self.Interaction139 = Interaction139
        self.ISO20022_Interaction = ISO20022_Interaction
        self.interactions = interactions
        self.Interaction146 = Interaction146
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def Interaction(self):
        return self.__Interaction

    @Interaction.setter
    def Interaction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_Interaction__Interaction", None)
        self.__Interaction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "messageSet90"):
                opp_val = getattr(old_value, "messageSet90", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "messageSet90"):
                opp_val = getattr(value, "messageSet90", None)
                if opp_val is None:
                    setattr(value, "messageSet90", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def interactions(self):
        return self.__interactions

    @interactions.setter
    def interactions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_Interaction__interactions", None)
        self.__interactions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MessageSet136"):
                opp_val = getattr(old_value, "MessageSet136", None)
                if opp_val == self:
                    setattr(old_value, "MessageSet136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MessageSet136"):
                opp_val = getattr(value, "MessageSet136", None)
                setattr(value, "MessageSet136", self)

    @property
    def interaction(self):
        return self.__interaction

    @interaction.setter
    def interaction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_Interaction__interaction", None)
        self.__interaction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InteractionActor"):
                    opp_val = getattr(item, "InteractionActor", None)
                    
                    if opp_val == self:
                        setattr(item, "InteractionActor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InteractionActor"):
                    opp_val = getattr(item, "InteractionActor", None)
                    
                    setattr(item, "InteractionActor", self)
                    

    @property
    def interaction133(self):
        return self.__interaction133

    @interaction133.setter
    def interaction133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_Interaction__interaction133", None)
        self.__interaction133 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InteractionMessage"):
                    opp_val = getattr(item, "InteractionMessage", None)
                    
                    if opp_val == self:
                        setattr(item, "InteractionMessage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InteractionMessage"):
                    opp_val = getattr(item, "InteractionMessage", None)
                    
                    setattr(item, "InteractionMessage", self)
                    

    @property
    def Interaction139(self):
        return self.__Interaction139

    @Interaction139.setter
    def Interaction139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_Interaction__Interaction139", None)
        self.__Interaction139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "actors"):
                opp_val = getattr(old_value, "actors", None)
                if opp_val == self:
                    setattr(old_value, "actors", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "actors"):
                opp_val = getattr(value, "actors", None)
                setattr(value, "actors", self)

    @property
    def ISO20022_Interaction(self):
        return self.__ISO20022_Interaction

    @ISO20022_Interaction.setter
    def ISO20022_Interaction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_Interaction__ISO20022_Interaction", None)
        self.__ISO20022_Interaction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ISO20022_Diagram"):
                opp_val = getattr(old_value, "ISO20022_Diagram", None)
                if opp_val == self:
                    setattr(old_value, "ISO20022_Diagram", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ISO20022_Diagram"):
                opp_val = getattr(value, "ISO20022_Diagram", None)
                setattr(value, "ISO20022_Diagram", self)

    @property
    def Interaction146(self):
        return self.__Interaction146

    @Interaction146.setter
    def Interaction146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_Interaction__Interaction146", None)
        self.__Interaction146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "messages"):
                opp_val = getattr(old_value, "messages", None)
                if opp_val == self:
                    setattr(old_value, "messages", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "messages"):
                opp_val = getattr(value, "messages", None)
                setattr(value, "messages", self)

class ISO20022_IsAnAlternativeFor(RepositoryConcept):

    pass
class ISO20022_TopLevelCatalogueEntry(RepositoryConcept):

    pass
class ISO20022_Code(RepositoryConcept):

    def __init__(self, codeName: str, code: "ISO20022_CodeSet" = None, Code: "ISO20022_CodeSet" = None):
        self.codeName = codeName
        self.code = code
        self.Code = Code
        
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
        old_value = getattr(self, f"_ISO20022_Code__Code", None)
        self.__Code = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner165"):
                opp_val = getattr(old_value, "owner165", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner165"):
                opp_val = getattr(value, "owner165", None)
                if opp_val is None:
                    setattr(value, "owner165", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_Code__code", None)
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

class ISO20022_InteractionActor(RepositoryConcept):

    pass
class ISO20022_Type(RepositoryConcept):

    pass
class ISO20022_TopLevelDictionaryEntry(RepositoryConcept):

    pass
class ISO20022_InteractionMessage(RepositoryConcept):

    pass
class ISO20022_Member(RepositoryConcept, MultiplicityEntity):

    pass
class ISO20022_LogicalType(Type):

    pass
class Member:

    pass
class ISO20022_XMLMember(Member):

    def __init__(self, xmlTag: str, typedXMLMember: "ISO20022_LogicalType" = None, XMLMember: "ISO20022_LogicalType" = None):
        self.xmlTag = xmlTag
        self.typedXMLMember = typedXMLMember
        self.XMLMember = XMLMember
        
    @property
    def xmlTag(self) -> str:
        return self.__xmlTag

    @xmlTag.setter
    def xmlTag(self, xmlTag: str):
        self.__xmlTag = xmlTag

    @property
    def typedXMLMember(self):
        return self.__typedXMLMember

    @typedXMLMember.setter
    def typedXMLMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_XMLMember__typedXMLMember", None)
        self.__typedXMLMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LogicalType"):
                opp_val = getattr(old_value, "LogicalType", None)
                if opp_val == self:
                    setattr(old_value, "LogicalType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LogicalType"):
                opp_val = getattr(value, "LogicalType", None)
                setattr(value, "LogicalType", self)

    @property
    def XMLMember(self):
        return self.__XMLMember

    @XMLMember.setter
    def XMLMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_XMLMember__XMLMember", None)
        self.__XMLMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xmlMemberType"):
                opp_val = getattr(old_value, "xmlMemberType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xmlMemberType"):
                opp_val = getattr(value, "xmlMemberType", None)
                if opp_val is None:
                    setattr(value, "xmlMemberType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ISO20022_MessageElementContainer(MessageComponentType):

    def __init__(self, MessageElementContainer: "ISO20022_MessageElement" = None, componentContext: set["ISO20022_MessageElement"] = None, ISO20022_MessageElementContainer: "ISO20022_EndPointCategory" = None):
        self.MessageElementContainer = MessageElementContainer
        self.componentContext = componentContext if componentContext is not None else set()
        self.ISO20022_MessageElementContainer = ISO20022_MessageElementContainer
        
    @property
    def componentContext(self):
        return self.__componentContext

    @componentContext.setter
    def componentContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageElementContainer__componentContext", None)
        self.__componentContext = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MessageElement80"):
                    opp_val = getattr(item, "MessageElement80", None)
                    
                    if opp_val == self:
                        setattr(item, "MessageElement80", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MessageElement80"):
                    opp_val = getattr(item, "MessageElement80", None)
                    
                    setattr(item, "MessageElement80", self)
                    

    @property
    def ISO20022_MessageElementContainer(self):
        return self.__ISO20022_MessageElementContainer

    @ISO20022_MessageElementContainer.setter
    def ISO20022_MessageElementContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageElementContainer__ISO20022_MessageElementContainer", None)
        self.__ISO20022_MessageElementContainer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ISO20022_EndPointCategory"):
                opp_val = getattr(old_value, "ISO20022_EndPointCategory", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ISO20022_EndPointCategory"):
                opp_val = getattr(value, "ISO20022_EndPointCategory", None)
                if opp_val is None:
                    setattr(value, "ISO20022_EndPointCategory", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MessageElementContainer(self):
        return self.__MessageElementContainer

    @MessageElementContainer.setter
    def MessageElementContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageElementContainer__MessageElementContainer", None)
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

    def technicalElement(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement technicalElement method
        pass

    def MessageElementsHaveUniqueNames(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement MessageElementsHaveUniqueNames method
        pass

class ISO20022_BusinessElement(BusinessConcept, Member):

    def __init__(self, isDerived: bool, BusinessElement: "ISO20022_MessageElement" = None, BusinessElement40: "ISO20022_BusinessComponent" = None, businessElementTrace: set["ISO20022_MessageElement"] = None, ISO20022_BusinessElement: "ISO20022_BusinessElementType" = None, element: "ISO20022_BusinessComponent" = None):
        self.isDerived = isDerived
        self.BusinessElement = BusinessElement
        self.BusinessElement40 = BusinessElement40
        self.businessElementTrace = businessElementTrace if businessElementTrace is not None else set()
        self.ISO20022_BusinessElement = ISO20022_BusinessElement
        self.element = element
        
    @property
    def isDerived(self) -> bool:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: bool):
        self.__isDerived = isDerived

    @property
    def element(self):
        return self.__element

    @element.setter
    def element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_BusinessElement__element", None)
        self.__element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BusinessComponent66"):
                opp_val = getattr(old_value, "BusinessComponent66", None)
                if opp_val == self:
                    setattr(old_value, "BusinessComponent66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BusinessComponent66"):
                opp_val = getattr(value, "BusinessComponent66", None)
                setattr(value, "BusinessComponent66", self)

    @property
    def ISO20022_BusinessElement(self):
        return self.__ISO20022_BusinessElement

    @ISO20022_BusinessElement.setter
    def ISO20022_BusinessElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_BusinessElement__ISO20022_BusinessElement", None)
        self.__ISO20022_BusinessElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ISO20022_BusinessElementType"):
                opp_val = getattr(old_value, "ISO20022_BusinessElementType", None)
                if opp_val == self:
                    setattr(old_value, "ISO20022_BusinessElementType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ISO20022_BusinessElementType"):
                opp_val = getattr(value, "ISO20022_BusinessElementType", None)
                setattr(value, "ISO20022_BusinessElementType", self)

    @property
    def BusinessElement40(self):
        return self.__BusinessElement40

    @BusinessElement40.setter
    def BusinessElement40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_BusinessElement__BusinessElement40", None)
        self.__BusinessElement40 = value
        
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

    @property
    def BusinessElement(self):
        return self.__BusinessElement

    @BusinessElement.setter
    def BusinessElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_BusinessElement__BusinessElement", None)
        self.__BusinessElement = value
        
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
    def businessElementTrace(self):
        return self.__businessElementTrace

    @businessElementTrace.setter
    def businessElementTrace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_BusinessElement__businessElementTrace", None)
        self.__businessElementTrace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MessageElement63"):
                    opp_val = getattr(item, "MessageElement63", None)
                    
                    if opp_val == self:
                        setattr(item, "MessageElement63", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MessageElement63"):
                    opp_val = getattr(item, "MessageElement63", None)
                    
                    setattr(item, "MessageElement63", self)
                    

class ISO20022_BusinessComponent(BusinessConcept, TopLevelDictionaryEntry, BusinessElementType):

    def __init__(self, previousVersionDocumentation: str, BusinessComponent: "ISO20022_MessageElement" = None, BusinessComponent35: "ISO20022_BusinessComponent" = None, superType: set["ISO20022_BusinessComponent"] = None, BusinessComponent38: "ISO20022_BusinessComponent" = None, subType: "ISO20022_BusinessComponent" = None, elementContext: set["ISO20022_BusinessElement"] = None, trace: set["ISO20022_MessageComponentType"] = None, type: set["ISO20022_BusinessAssociationEnd"] = None, businessComponentTrace: set["ISO20022_MessageElement"] = None, BusinessComponent69: "ISO20022_MessageComponentType" = None, BusinessComponent66: "ISO20022_BusinessElement" = None, BusinessComponent78: "ISO20022_BusinessAssociationEnd" = None, ISO20022_BusinessComponent: "ISO20022_BusinessAttribute" = None):
        self.previousVersionDocumentation = previousVersionDocumentation
        self.BusinessComponent = BusinessComponent
        self.BusinessComponent35 = BusinessComponent35
        self.superType = superType if superType is not None else set()
        self.BusinessComponent38 = BusinessComponent38
        self.subType = subType
        self.elementContext = elementContext if elementContext is not None else set()
        self.trace = trace if trace is not None else set()
        self.type = type if type is not None else set()
        self.businessComponentTrace = businessComponentTrace if businessComponentTrace is not None else set()
        self.BusinessComponent69 = BusinessComponent69
        self.BusinessComponent66 = BusinessComponent66
        self.BusinessComponent78 = BusinessComponent78
        self.ISO20022_BusinessComponent = ISO20022_BusinessComponent
        
    @property
    def previousVersionDocumentation(self) -> str:
        return self.__previousVersionDocumentation

    @previousVersionDocumentation.setter
    def previousVersionDocumentation(self, previousVersionDocumentation: str):
        self.__previousVersionDocumentation = previousVersionDocumentation

    @property
    def BusinessComponent35(self):
        return self.__BusinessComponent35

    @BusinessComponent35.setter
    def BusinessComponent35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_BusinessComponent__BusinessComponent35", None)
        self.__BusinessComponent35 = value
        
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
    def elementContext(self):
        return self.__elementContext

    @elementContext.setter
    def elementContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_BusinessComponent__elementContext", None)
        self.__elementContext = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BusinessElement40"):
                    opp_val = getattr(item, "BusinessElement40", None)
                    
                    if opp_val == self:
                        setattr(item, "BusinessElement40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BusinessElement40"):
                    opp_val = getattr(item, "BusinessElement40", None)
                    
                    setattr(item, "BusinessElement40", self)
                    

    @property
    def ISO20022_BusinessComponent(self):
        return self.__ISO20022_BusinessComponent

    @ISO20022_BusinessComponent.setter
    def ISO20022_BusinessComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_BusinessComponent__ISO20022_BusinessComponent", None)
        self.__ISO20022_BusinessComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ISO20022_BusinessAttribute154"):
                opp_val = getattr(old_value, "ISO20022_BusinessAttribute154", None)
                if opp_val == self:
                    setattr(old_value, "ISO20022_BusinessAttribute154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ISO20022_BusinessAttribute154"):
                opp_val = getattr(value, "ISO20022_BusinessAttribute154", None)
                setattr(value, "ISO20022_BusinessAttribute154", self)

    @property
    def BusinessComponent66(self):
        return self.__BusinessComponent66

    @BusinessComponent66.setter
    def BusinessComponent66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_BusinessComponent__BusinessComponent66", None)
        self.__BusinessComponent66 = value
        
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
    def subType(self):
        return self.__subType

    @subType.setter
    def subType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_BusinessComponent__subType", None)
        self.__subType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BusinessComponent38"):
                opp_val = getattr(old_value, "BusinessComponent38", None)
                if opp_val == self:
                    setattr(old_value, "BusinessComponent38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BusinessComponent38"):
                opp_val = getattr(value, "BusinessComponent38", None)
                setattr(value, "BusinessComponent38", self)

    @property
    def BusinessComponent38(self):
        return self.__BusinessComponent38

    @BusinessComponent38.setter
    def BusinessComponent38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_BusinessComponent__BusinessComponent38", None)
        self.__BusinessComponent38 = value
        
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
    def BusinessComponent78(self):
        return self.__BusinessComponent78

    @BusinessComponent78.setter
    def BusinessComponent78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_BusinessComponent__BusinessComponent78", None)
        self.__BusinessComponent78 = value
        
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
    def BusinessComponent69(self):
        return self.__BusinessComponent69

    @BusinessComponent69.setter
    def BusinessComponent69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_BusinessComponent__BusinessComponent69", None)
        self.__BusinessComponent69 = value
        
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
    def businessComponentTrace(self):
        return self.__businessComponentTrace

    @businessComponentTrace.setter
    def businessComponentTrace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_BusinessComponent__businessComponentTrace", None)
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
                    

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_BusinessComponent__type", None)
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
    def BusinessComponent(self):
        return self.__BusinessComponent

    @BusinessComponent.setter
    def BusinessComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_BusinessComponent__BusinessComponent", None)
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
    def superType(self):
        return self.__superType

    @superType.setter
    def superType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_BusinessComponent__superType", None)
        self.__superType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BusinessComponent35"):
                    opp_val = getattr(item, "BusinessComponent35", None)
                    
                    if opp_val == self:
                        setattr(item, "BusinessComponent35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BusinessComponent35"):
                    opp_val = getattr(item, "BusinessComponent35", None)
                    
                    setattr(item, "BusinessComponent35", self)
                    

    @property
    def trace(self):
        return self.__trace

    @trace.setter
    def trace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_BusinessComponent__trace", None)
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
                    

    def BusinessElementsHaveUniqueNames(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement BusinessElementsHaveUniqueNames method
        pass

class MessageConcept:

    pass
class XMLMember:

    pass
class ISO20022_MessageBuildingBlock(XMLMember):

    def __init__(self, MessageBuildingBlock: "ISO20022_MessageComponentType" = None, ISO20022_MessageBuildingBlock: "ISO20022_DataType" = None, messageBuildingBlock: "ISO20022_MessageComponentType" = None, ISO20022_MessageBuildingBlock105: "ISO20022_MessageDefinition" = None, ISO20022_MessageBuildingBlock120: "ISO20022_Xor" = None):
        self.MessageBuildingBlock = MessageBuildingBlock
        self.ISO20022_MessageBuildingBlock = ISO20022_MessageBuildingBlock
        self.messageBuildingBlock = messageBuildingBlock
        self.ISO20022_MessageBuildingBlock105 = ISO20022_MessageBuildingBlock105
        self.ISO20022_MessageBuildingBlock120 = ISO20022_MessageBuildingBlock120
        
    @property
    def messageBuildingBlock(self):
        return self.__messageBuildingBlock

    @messageBuildingBlock.setter
    def messageBuildingBlock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageBuildingBlock__messageBuildingBlock", None)
        self.__messageBuildingBlock = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MessageComponentType72"):
                opp_val = getattr(old_value, "MessageComponentType72", None)
                if opp_val == self:
                    setattr(old_value, "MessageComponentType72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MessageComponentType72"):
                opp_val = getattr(value, "MessageComponentType72", None)
                setattr(value, "MessageComponentType72", self)

    @property
    def ISO20022_MessageBuildingBlock(self):
        return self.__ISO20022_MessageBuildingBlock

    @ISO20022_MessageBuildingBlock.setter
    def ISO20022_MessageBuildingBlock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageBuildingBlock__ISO20022_MessageBuildingBlock", None)
        self.__ISO20022_MessageBuildingBlock = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ISO20022_DataType"):
                opp_val = getattr(old_value, "ISO20022_DataType", None)
                if opp_val == self:
                    setattr(old_value, "ISO20022_DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ISO20022_DataType"):
                opp_val = getattr(value, "ISO20022_DataType", None)
                setattr(value, "ISO20022_DataType", self)

    @property
    def MessageBuildingBlock(self):
        return self.__MessageBuildingBlock

    @MessageBuildingBlock.setter
    def MessageBuildingBlock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageBuildingBlock__MessageBuildingBlock", None)
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
    def ISO20022_MessageBuildingBlock105(self):
        return self.__ISO20022_MessageBuildingBlock105

    @ISO20022_MessageBuildingBlock105.setter
    def ISO20022_MessageBuildingBlock105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageBuildingBlock__ISO20022_MessageBuildingBlock105", None)
        self.__ISO20022_MessageBuildingBlock105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ISO20022_MessageDefinition"):
                opp_val = getattr(old_value, "ISO20022_MessageDefinition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ISO20022_MessageDefinition"):
                opp_val = getattr(value, "ISO20022_MessageDefinition", None)
                if opp_val is None:
                    setattr(value, "ISO20022_MessageDefinition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ISO20022_MessageBuildingBlock120(self):
        return self.__ISO20022_MessageBuildingBlock120

    @ISO20022_MessageBuildingBlock120.setter
    def ISO20022_MessageBuildingBlock120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageBuildingBlock__ISO20022_MessageBuildingBlock120", None)
        self.__ISO20022_MessageBuildingBlock120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ISO20022_Xor119"):
                opp_val = getattr(old_value, "ISO20022_Xor119", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ISO20022_Xor119"):
                opp_val = getattr(value, "ISO20022_Xor119", None)
                if opp_val is None:
                    setattr(value, "ISO20022_Xor119", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def MessageBuildingBlockHasExactlyOneType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement MessageBuildingBlockHasExactlyOneType method
        pass

class ISO20022_MessageElement(XMLMember, MessageConcept):

    def __init__(self, isTechnical: bool, tracePath: str, isDerived: bool, derivationElement: "ISO20022_BusinessComponent" = None, derivation: "ISO20022_BusinessElement" = None, messageElement: "ISO20022_MessageElementContainer" = None, MessageElement: "ISO20022_BusinessComponent" = None, MessageElement63: "ISO20022_BusinessElement" = None, MessageElement80: "ISO20022_MessageElementContainer" = None, ISO20022_MessageElement: "ISO20022_Xor" = None):
        self.isTechnical = isTechnical
        self.tracePath = tracePath
        self.isDerived = isDerived
        self.derivationElement = derivationElement
        self.derivation = derivation
        self.messageElement = messageElement
        self.MessageElement = MessageElement
        self.MessageElement63 = MessageElement63
        self.MessageElement80 = MessageElement80
        self.ISO20022_MessageElement = ISO20022_MessageElement
        
    @property
    def isTechnical(self) -> bool:
        return self.__isTechnical

    @isTechnical.setter
    def isTechnical(self, isTechnical: bool):
        self.__isTechnical = isTechnical

    @property
    def tracePath(self) -> str:
        return self.__tracePath

    @tracePath.setter
    def tracePath(self, tracePath: str):
        self.__tracePath = tracePath

    @property
    def isDerived(self) -> bool:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: bool):
        self.__isDerived = isDerived

    @property
    def messageElement(self):
        return self.__messageElement

    @messageElement.setter
    def messageElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageElement__messageElement", None)
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
    def derivation(self):
        return self.__derivation

    @derivation.setter
    def derivation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageElement__derivation", None)
        self.__derivation = value
        
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
    def ISO20022_MessageElement(self):
        return self.__ISO20022_MessageElement

    @ISO20022_MessageElement.setter
    def ISO20022_MessageElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageElement__ISO20022_MessageElement", None)
        self.__ISO20022_MessageElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ISO20022_Xor"):
                opp_val = getattr(old_value, "ISO20022_Xor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ISO20022_Xor"):
                opp_val = getattr(value, "ISO20022_Xor", None)
                if opp_val is None:
                    setattr(value, "ISO20022_Xor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def derivationElement(self):
        return self.__derivationElement

    @derivationElement.setter
    def derivationElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageElement__derivationElement", None)
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
    def MessageElement(self):
        return self.__MessageElement

    @MessageElement.setter
    def MessageElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageElement__MessageElement", None)
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
    def MessageElement80(self):
        return self.__MessageElement80

    @MessageElement80.setter
    def MessageElement80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageElement__MessageElement80", None)
        self.__MessageElement80 = value
        
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
    def MessageElement63(self):
        return self.__MessageElement63

    @MessageElement63.setter
    def MessageElement63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageElement__MessageElement63", None)
        self.__MessageElement63 = value
        
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

    def NoMoreThanOneTrace(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement NoMoreThanOneTrace method
        pass

    def CardinalityAlignment(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement CardinalityAlignment method
        pass

class ISO20022_MessageComponentType(TopLevelDictionaryEntry, LogicalType, MessageConcept):

    def __init__(self, isTechnical: bool, tracePath: str, ISO20022_MessageComponentType: "ISO20022_MessageAssociationEnd" = None, MessageComponentType: "ISO20022_BusinessComponent" = None, derivationComponent: "ISO20022_BusinessComponent" = None, complexType: set["ISO20022_MessageBuildingBlock"] = None, MessageComponentType72: "ISO20022_MessageBuildingBlock" = None, ISO20022_MessageComponentType85: "ISO20022_MessageAttribute" = None):
        self.isTechnical = isTechnical
        self.tracePath = tracePath
        self.ISO20022_MessageComponentType = ISO20022_MessageComponentType
        self.MessageComponentType = MessageComponentType
        self.derivationComponent = derivationComponent
        self.complexType = complexType if complexType is not None else set()
        self.MessageComponentType72 = MessageComponentType72
        self.ISO20022_MessageComponentType85 = ISO20022_MessageComponentType85
        
    @property
    def tracePath(self) -> str:
        return self.__tracePath

    @tracePath.setter
    def tracePath(self, tracePath: str):
        self.__tracePath = tracePath

    @property
    def isTechnical(self) -> bool:
        return self.__isTechnical

    @isTechnical.setter
    def isTechnical(self, isTechnical: bool):
        self.__isTechnical = isTechnical

    @property
    def complexType(self):
        return self.__complexType

    @complexType.setter
    def complexType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageComponentType__complexType", None)
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
        old_value = getattr(self, f"_ISO20022_MessageComponentType__derivationComponent", None)
        self.__derivationComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BusinessComponent69"):
                opp_val = getattr(old_value, "BusinessComponent69", None)
                if opp_val == self:
                    setattr(old_value, "BusinessComponent69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BusinessComponent69"):
                opp_val = getattr(value, "BusinessComponent69", None)
                setattr(value, "BusinessComponent69", self)

    @property
    def MessageComponentType(self):
        return self.__MessageComponentType

    @MessageComponentType.setter
    def MessageComponentType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageComponentType__MessageComponentType", None)
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
    def ISO20022_MessageComponentType85(self):
        return self.__ISO20022_MessageComponentType85

    @ISO20022_MessageComponentType85.setter
    def ISO20022_MessageComponentType85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageComponentType__ISO20022_MessageComponentType85", None)
        self.__ISO20022_MessageComponentType85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ISO20022_MessageAttribute84"):
                opp_val = getattr(old_value, "ISO20022_MessageAttribute84", None)
                if opp_val == self:
                    setattr(old_value, "ISO20022_MessageAttribute84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ISO20022_MessageAttribute84"):
                opp_val = getattr(value, "ISO20022_MessageAttribute84", None)
                setattr(value, "ISO20022_MessageAttribute84", self)

    @property
    def ISO20022_MessageComponentType(self):
        return self.__ISO20022_MessageComponentType

    @ISO20022_MessageComponentType.setter
    def ISO20022_MessageComponentType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageComponentType__ISO20022_MessageComponentType", None)
        self.__ISO20022_MessageComponentType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ISO20022_MessageAssociationEnd"):
                opp_val = getattr(old_value, "ISO20022_MessageAssociationEnd", None)
                if opp_val == self:
                    setattr(old_value, "ISO20022_MessageAssociationEnd", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ISO20022_MessageAssociationEnd"):
                opp_val = getattr(value, "ISO20022_MessageAssociationEnd", None)
                setattr(value, "ISO20022_MessageAssociationEnd", self)

    @property
    def MessageComponentType72(self):
        return self.__MessageComponentType72

    @MessageComponentType72.setter
    def MessageComponentType72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageComponentType__MessageComponentType72", None)
        self.__MessageComponentType72 = value
        
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

class MessageElement:

    pass
class ISO20022_MessageAttribute(MessageElement):

    def __init__(self, ISO20022_MessageAttribute: "ISO20022_DataType" = None, ISO20022_MessageAttribute84: "ISO20022_MessageComponentType" = None):
        self.ISO20022_MessageAttribute = ISO20022_MessageAttribute
        self.ISO20022_MessageAttribute84 = ISO20022_MessageAttribute84
        
    @property
    def ISO20022_MessageAttribute84(self):
        return self.__ISO20022_MessageAttribute84

    @ISO20022_MessageAttribute84.setter
    def ISO20022_MessageAttribute84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageAttribute__ISO20022_MessageAttribute84", None)
        self.__ISO20022_MessageAttribute84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ISO20022_MessageComponentType85"):
                opp_val = getattr(old_value, "ISO20022_MessageComponentType85", None)
                if opp_val == self:
                    setattr(old_value, "ISO20022_MessageComponentType85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ISO20022_MessageComponentType85"):
                opp_val = getattr(value, "ISO20022_MessageComponentType85", None)
                setattr(value, "ISO20022_MessageComponentType85", self)

    @property
    def ISO20022_MessageAttribute(self):
        return self.__ISO20022_MessageAttribute

    @ISO20022_MessageAttribute.setter
    def ISO20022_MessageAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageAttribute__ISO20022_MessageAttribute", None)
        self.__ISO20022_MessageAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ISO20022_DataType82"):
                opp_val = getattr(old_value, "ISO20022_DataType82", None)
                if opp_val == self:
                    setattr(old_value, "ISO20022_DataType82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ISO20022_DataType82"):
                opp_val = getattr(value, "ISO20022_DataType82", None)
                setattr(value, "ISO20022_DataType82", self)

    def MessageAttributeHasExactlyOneType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement MessageAttributeHasExactlyOneType method
        pass

class ISO20022_MessageAssociationEnd(MessageElement):

    def __init__(self, isComposite: bool, ISO20022_MessageAssociationEnd: "ISO20022_MessageComponentType" = None, ISO20022_MessageAssociationEnd15: "ISO20022_MessageAssociationEnd" = None, ISO20022_MessageAssociationEnd13: "ISO20022_MessageAssociationEnd" = None):
        self.isComposite = isComposite
        self.ISO20022_MessageAssociationEnd = ISO20022_MessageAssociationEnd
        self.ISO20022_MessageAssociationEnd15 = ISO20022_MessageAssociationEnd15
        self.ISO20022_MessageAssociationEnd13 = ISO20022_MessageAssociationEnd13
        
    @property
    def isComposite(self) -> bool:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: bool):
        self.__isComposite = isComposite

    @property
    def ISO20022_MessageAssociationEnd15(self):
        return self.__ISO20022_MessageAssociationEnd15

    @ISO20022_MessageAssociationEnd15.setter
    def ISO20022_MessageAssociationEnd15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageAssociationEnd__ISO20022_MessageAssociationEnd15", None)
        self.__ISO20022_MessageAssociationEnd15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ISO20022_MessageAssociationEnd13"):
                opp_val = getattr(old_value, "ISO20022_MessageAssociationEnd13", None)
                if opp_val == self:
                    setattr(old_value, "ISO20022_MessageAssociationEnd13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ISO20022_MessageAssociationEnd13"):
                opp_val = getattr(value, "ISO20022_MessageAssociationEnd13", None)
                setattr(value, "ISO20022_MessageAssociationEnd13", self)

    @property
    def ISO20022_MessageAssociationEnd13(self):
        return self.__ISO20022_MessageAssociationEnd13

    @ISO20022_MessageAssociationEnd13.setter
    def ISO20022_MessageAssociationEnd13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageAssociationEnd__ISO20022_MessageAssociationEnd13", None)
        self.__ISO20022_MessageAssociationEnd13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ISO20022_MessageAssociationEnd15"):
                opp_val = getattr(old_value, "ISO20022_MessageAssociationEnd15", None)
                if opp_val == self:
                    setattr(old_value, "ISO20022_MessageAssociationEnd15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ISO20022_MessageAssociationEnd15"):
                opp_val = getattr(value, "ISO20022_MessageAssociationEnd15", None)
                setattr(value, "ISO20022_MessageAssociationEnd15", self)

    @property
    def ISO20022_MessageAssociationEnd(self):
        return self.__ISO20022_MessageAssociationEnd

    @ISO20022_MessageAssociationEnd.setter
    def ISO20022_MessageAssociationEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_MessageAssociationEnd__ISO20022_MessageAssociationEnd", None)
        self.__ISO20022_MessageAssociationEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ISO20022_MessageComponentType"):
                opp_val = getattr(old_value, "ISO20022_MessageComponentType", None)
                if opp_val == self:
                    setattr(old_value, "ISO20022_MessageComponentType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ISO20022_MessageComponentType"):
                opp_val = getattr(value, "ISO20022_MessageComponentType", None)
                setattr(value, "ISO20022_MessageComponentType", self)

class ISO20022_ModelEntity(ABC):

    def __init__(self, objectIdentifier: str, ModelEntity: "ISO20022_ModelEntity" = None, previousVersion: set["ISO20022_ModelEntity"] = None, ModelEntity9: "ISO20022_ModelEntity" = None, nextVersions: "ISO20022_ModelEntity" = None):
        self.objectIdentifier = objectIdentifier
        self.ModelEntity = ModelEntity
        self.previousVersion = previousVersion if previousVersion is not None else set()
        self.ModelEntity9 = ModelEntity9
        self.nextVersions = nextVersions
        
    @property
    def objectIdentifier(self) -> str:
        return self.__objectIdentifier

    @objectIdentifier.setter
    def objectIdentifier(self, objectIdentifier: str):
        self.__objectIdentifier = objectIdentifier

    @property
    def previousVersion(self):
        return self.__previousVersion

    @previousVersion.setter
    def previousVersion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_ModelEntity__previousVersion", None)
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
    def ModelEntity(self):
        return self.__ModelEntity

    @ModelEntity.setter
    def ModelEntity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_ModelEntity__ModelEntity", None)
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
    def ModelEntity9(self):
        return self.__ModelEntity9

    @ModelEntity9.setter
    def ModelEntity9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_ModelEntity__ModelEntity9", None)
        self.__ModelEntity9 = value
        
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
    def nextVersions(self):
        return self.__nextVersions

    @nextVersions.setter
    def nextVersions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_ModelEntity__nextVersions", None)
        self.__nextVersions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelEntity9"):
                opp_val = getattr(old_value, "ModelEntity9", None)
                if opp_val == self:
                    setattr(old_value, "ModelEntity9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelEntity9"):
                opp_val = getattr(value, "ModelEntity9", None)
                setattr(value, "ModelEntity9", self)

class ModelEntity:

    pass
class ISO20022_BusinessConcept(ModelEntity):

    pass
class ISO20022_BusinessProcessCatalogue(ModelEntity):

    def __init__(self, BusinessProcessCatalogue: "ISO20022_Repository" = None, businessProcessCatalogue: set["ISO20022_TopLevelCatalogueEntry"] = None, businessProcessCatalogue56: "ISO20022_Repository" = None, BusinessProcessCatalogue59: "ISO20022_TopLevelCatalogueEntry" = None):
        self.BusinessProcessCatalogue = BusinessProcessCatalogue
        self.businessProcessCatalogue = businessProcessCatalogue if businessProcessCatalogue is not None else set()
        self.businessProcessCatalogue56 = businessProcessCatalogue56
        self.BusinessProcessCatalogue59 = BusinessProcessCatalogue59
        
    @property
    def BusinessProcessCatalogue(self):
        return self.__BusinessProcessCatalogue

    @BusinessProcessCatalogue.setter
    def BusinessProcessCatalogue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_BusinessProcessCatalogue__BusinessProcessCatalogue", None)
        self.__BusinessProcessCatalogue = value
        
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
    def BusinessProcessCatalogue59(self):
        return self.__BusinessProcessCatalogue59

    @BusinessProcessCatalogue59.setter
    def BusinessProcessCatalogue59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_BusinessProcessCatalogue__BusinessProcessCatalogue59", None)
        self.__BusinessProcessCatalogue59 = value
        
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
        old_value = getattr(self, f"_ISO20022_BusinessProcessCatalogue__businessProcessCatalogue", None)
        self.__businessProcessCatalogue = value if value is not None else set()
        
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
    def businessProcessCatalogue56(self):
        return self.__businessProcessCatalogue56

    @businessProcessCatalogue56.setter
    def businessProcessCatalogue56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_BusinessProcessCatalogue__businessProcessCatalogue56", None)
        self.__businessProcessCatalogue56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Repository57"):
                opp_val = getattr(old_value, "Repository57", None)
                if opp_val == self:
                    setattr(old_value, "Repository57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Repository57"):
                opp_val = getattr(value, "Repository57", None)
                setattr(value, "Repository57", self)

    def EntriesHaveUniqueName(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement EntriesHaveUniqueName method
        pass

class ISO20022_Facet(ModelEntity):

    def __init__(self, name: str, value: str, ISO20022_Facet: "ISO20022_DataType" = None):
        self.name = name
        self.value = value
        self.ISO20022_Facet = ISO20022_Facet
        
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
    def ISO20022_Facet(self):
        return self.__ISO20022_Facet

    @ISO20022_Facet.setter
    def ISO20022_Facet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_Facet__ISO20022_Facet", None)
        self.__ISO20022_Facet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ISO20022_DataType74"):
                opp_val = getattr(old_value, "ISO20022_DataType74", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ISO20022_DataType74"):
                opp_val = getattr(value, "ISO20022_DataType74", None)
                if opp_val is None:
                    setattr(value, "ISO20022_DataType74", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ISO20022_SemanticMarkupElement(ModelEntity):

    def __init__(self, name: str, value: str, ISO20022_SemanticMarkupElement: "ISO20022_SemanticMarkup" = None):
        self.name = name
        self.value = value
        self.ISO20022_SemanticMarkupElement = ISO20022_SemanticMarkupElement
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ISO20022_SemanticMarkupElement(self):
        return self.__ISO20022_SemanticMarkupElement

    @ISO20022_SemanticMarkupElement.setter
    def ISO20022_SemanticMarkupElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_SemanticMarkupElement__ISO20022_SemanticMarkupElement", None)
        self.__ISO20022_SemanticMarkupElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ISO20022_SemanticMarkup11"):
                opp_val = getattr(old_value, "ISO20022_SemanticMarkup11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ISO20022_SemanticMarkup11"):
                opp_val = getattr(value, "ISO20022_SemanticMarkup11", None)
                if opp_val is None:
                    setattr(value, "ISO20022_SemanticMarkup11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ISO20022_Repository(ModelEntity):

    pass
class ISO20022_Doclet(ModelEntity):

    def __init__(self, type: str, content: str, ISO20022_Doclet: "ISO20022_RepositoryConcept" = None):
        self.type = type
        self.content = content
        self.ISO20022_Doclet = ISO20022_Doclet
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def ISO20022_Doclet(self):
        return self.__ISO20022_Doclet

    @ISO20022_Doclet.setter
    def ISO20022_Doclet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_Doclet__ISO20022_Doclet", None)
        self.__ISO20022_Doclet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ISO20022_RepositoryConcept3"):
                opp_val = getattr(old_value, "ISO20022_RepositoryConcept3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ISO20022_RepositoryConcept3"):
                opp_val = getattr(value, "ISO20022_RepositoryConcept3", None)
                if opp_val is None:
                    setattr(value, "ISO20022_RepositoryConcept3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ISO20022_MessageConcept(ModelEntity):

    pass
class ISO20022_Syntax(ModelEntity):

    def __init__(self, Syntax: "ISO20022_Encoding" = None, Syntax92: "ISO20022_MessageSet" = None, syntax: set["ISO20022_Encoding"] = None, generatedSyntax: set["ISO20022_MessageSet"] = None):
        self.Syntax = Syntax
        self.Syntax92 = Syntax92
        self.syntax = syntax if syntax is not None else set()
        self.generatedSyntax = generatedSyntax if generatedSyntax is not None else set()
        
    @property
    def syntax(self):
        return self.__syntax

    @syntax.setter
    def syntax(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_Syntax__syntax", None)
        self.__syntax = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Encoding148"):
                    opp_val = getattr(item, "Encoding148", None)
                    
                    if opp_val == self:
                        setattr(item, "Encoding148", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Encoding148"):
                    opp_val = getattr(item, "Encoding148", None)
                    
                    setattr(item, "Encoding148", self)
                    

    @property
    def generatedSyntax(self):
        return self.__generatedSyntax

    @generatedSyntax.setter
    def generatedSyntax(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_Syntax__generatedSyntax", None)
        self.__generatedSyntax = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MessageSet150"):
                    opp_val = getattr(item, "MessageSet150", None)
                    
                    if opp_val == self:
                        setattr(item, "MessageSet150", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MessageSet150"):
                    opp_val = getattr(item, "MessageSet150", None)
                    
                    setattr(item, "MessageSet150", self)
                    

    @property
    def Syntax92(self):
        return self.__Syntax92

    @Syntax92.setter
    def Syntax92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_Syntax__Syntax92", None)
        self.__Syntax92 = value
        
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
    def Syntax(self):
        return self.__Syntax

    @Syntax.setter
    def Syntax(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_Syntax__Syntax", None)
        self.__Syntax = value
        
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

    def GeneratedForDerivation(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement GeneratedForDerivation method
        pass

class ISO20022_DataDictionary(ModelEntity):

    def __init__(self, DataDictionary: "ISO20022_TopLevelDictionaryEntry" = None, dataDictionary: "ISO20022_Repository" = None, dataDictionary47: set["ISO20022_TopLevelDictionaryEntry"] = None, DataDictionary53: "ISO20022_Repository" = None):
        self.DataDictionary = DataDictionary
        self.dataDictionary = dataDictionary
        self.dataDictionary47 = dataDictionary47 if dataDictionary47 is not None else set()
        self.DataDictionary53 = DataDictionary53
        
    @property
    def DataDictionary53(self):
        return self.__DataDictionary53

    @DataDictionary53.setter
    def DataDictionary53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_DataDictionary__DataDictionary53", None)
        self.__DataDictionary53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository52"):
                opp_val = getattr(old_value, "repository52", None)
                if opp_val == self:
                    setattr(old_value, "repository52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository52"):
                opp_val = getattr(value, "repository52", None)
                setattr(value, "repository52", self)

    @property
    def dataDictionary(self):
        return self.__dataDictionary

    @dataDictionary.setter
    def dataDictionary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_DataDictionary__dataDictionary", None)
        self.__dataDictionary = value
        
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
    def dataDictionary47(self):
        return self.__dataDictionary47

    @dataDictionary47.setter
    def dataDictionary47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_DataDictionary__dataDictionary47", None)
        self.__dataDictionary47 = value if value is not None else set()
        
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
                    

    @property
    def DataDictionary(self):
        return self.__DataDictionary

    @DataDictionary.setter
    def DataDictionary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_DataDictionary__DataDictionary", None)
        self.__DataDictionary = value
        
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

    def EntriesHaveUniqueName(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement EntriesHaveUniqueName method
        pass

class ISO20022_Encoding(ModelEntity):

    pass
class ISO20022_SemanticMarkup(ModelEntity):

    def __init__(self, type: str, ISO20022_SemanticMarkup: "ISO20022_RepositoryConcept" = None, ISO20022_SemanticMarkup11: set["ISO20022_SemanticMarkupElement"] = None):
        self.type = type
        self.ISO20022_SemanticMarkup = ISO20022_SemanticMarkup
        self.ISO20022_SemanticMarkup11 = ISO20022_SemanticMarkup11 if ISO20022_SemanticMarkup11 is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def ISO20022_SemanticMarkup(self):
        return self.__ISO20022_SemanticMarkup

    @ISO20022_SemanticMarkup.setter
    def ISO20022_SemanticMarkup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_SemanticMarkup__ISO20022_SemanticMarkup", None)
        self.__ISO20022_SemanticMarkup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ISO20022_RepositoryConcept"):
                opp_val = getattr(old_value, "ISO20022_RepositoryConcept", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ISO20022_RepositoryConcept"):
                opp_val = getattr(value, "ISO20022_RepositoryConcept", None)
                if opp_val is None:
                    setattr(value, "ISO20022_RepositoryConcept", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ISO20022_SemanticMarkup11(self):
        return self.__ISO20022_SemanticMarkup11

    @ISO20022_SemanticMarkup11.setter
    def ISO20022_SemanticMarkup11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_SemanticMarkup__ISO20022_SemanticMarkup11", None)
        self.__ISO20022_SemanticMarkup11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ISO20022_SemanticMarkupElement"):
                    opp_val = getattr(item, "ISO20022_SemanticMarkupElement", None)
                    
                    if opp_val == self:
                        setattr(item, "ISO20022_SemanticMarkupElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ISO20022_SemanticMarkupElement"):
                    opp_val = getattr(item, "ISO20022_SemanticMarkupElement", None)
                    
                    setattr(item, "ISO20022_SemanticMarkupElement", self)
                    

class ISO20022_RepositoryConcept(ModelEntity):

    def __init__(self, name: str, definition: str, example: str, swiftRegistrationStatus: str, swiftRemovalDate: date, registrationStatus: str, removalDate: date, RepositoryConcept: "ISO20022_Constraint" = None, ISO20022_RepositoryConcept: set["ISO20022_SemanticMarkup"] = None, ISO20022_RepositoryConcept3: set["ISO20022_Doclet"] = None, owner: set["ISO20022_Constraint"] = None):
        self.name = name
        self.definition = definition
        self.example = example
        self.swiftRegistrationStatus = swiftRegistrationStatus
        self.swiftRemovalDate = swiftRemovalDate
        self.registrationStatus = registrationStatus
        self.removalDate = removalDate
        self.RepositoryConcept = RepositoryConcept
        self.ISO20022_RepositoryConcept = ISO20022_RepositoryConcept if ISO20022_RepositoryConcept is not None else set()
        self.ISO20022_RepositoryConcept3 = ISO20022_RepositoryConcept3 if ISO20022_RepositoryConcept3 is not None else set()
        self.owner = owner if owner is not None else set()
        
    @property
    def removalDate(self) -> date:
        return self.__removalDate

    @removalDate.setter
    def removalDate(self, removalDate: date):
        self.__removalDate = removalDate

    @property
    def swiftRemovalDate(self) -> date:
        return self.__swiftRemovalDate

    @swiftRemovalDate.setter
    def swiftRemovalDate(self, swiftRemovalDate: date):
        self.__swiftRemovalDate = swiftRemovalDate

    @property
    def swiftRegistrationStatus(self) -> str:
        return self.__swiftRegistrationStatus

    @swiftRegistrationStatus.setter
    def swiftRegistrationStatus(self, swiftRegistrationStatus: str):
        self.__swiftRegistrationStatus = swiftRegistrationStatus

    @property
    def example(self) -> str:
        return self.__example

    @example.setter
    def example(self, example: str):
        self.__example = example

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def registrationStatus(self) -> str:
        return self.__registrationStatus

    @registrationStatus.setter
    def registrationStatus(self, registrationStatus: str):
        self.__registrationStatus = registrationStatus

    @property
    def definition(self) -> str:
        return self.__definition

    @definition.setter
    def definition(self, definition: str):
        self.__definition = definition

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_RepositoryConcept__owner", None)
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
    def RepositoryConcept(self):
        return self.__RepositoryConcept

    @RepositoryConcept.setter
    def RepositoryConcept(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_RepositoryConcept__RepositoryConcept", None)
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
    def ISO20022_RepositoryConcept3(self):
        return self.__ISO20022_RepositoryConcept3

    @ISO20022_RepositoryConcept3.setter
    def ISO20022_RepositoryConcept3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_RepositoryConcept__ISO20022_RepositoryConcept3", None)
        self.__ISO20022_RepositoryConcept3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ISO20022_Doclet"):
                    opp_val = getattr(item, "ISO20022_Doclet", None)
                    
                    if opp_val == self:
                        setattr(item, "ISO20022_Doclet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ISO20022_Doclet"):
                    opp_val = getattr(item, "ISO20022_Doclet", None)
                    
                    setattr(item, "ISO20022_Doclet", self)
                    

    @property
    def ISO20022_RepositoryConcept(self):
        return self.__ISO20022_RepositoryConcept

    @ISO20022_RepositoryConcept.setter
    def ISO20022_RepositoryConcept(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_RepositoryConcept__ISO20022_RepositoryConcept", None)
        self.__ISO20022_RepositoryConcept = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ISO20022_SemanticMarkup"):
                    opp_val = getattr(item, "ISO20022_SemanticMarkup", None)
                    
                    if opp_val == self:
                        setattr(item, "ISO20022_SemanticMarkup", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ISO20022_SemanticMarkup"):
                    opp_val = getattr(item, "ISO20022_SemanticMarkup", None)
                    
                    setattr(item, "ISO20022_SemanticMarkup", self)
                    

    def RemovalDateRegistrationStatus(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement RemovalDateRegistrationStatus method
        pass

class ISO20022_Constraint:

    def __init__(self, injected: bool, errorCode: str, errorText: str, kind: str, expression: str, expressionLanguage: str, constraint: "ISO20022_RepositoryConcept" = None, Constraint: "ISO20022_RepositoryConcept" = None):
        self.injected = injected
        self.errorCode = errorCode
        self.errorText = errorText
        self.kind = kind
        self.expression = expression
        self.expressionLanguage = expressionLanguage
        self.constraint = constraint
        self.Constraint = Constraint
        
    @property
    def errorCode(self) -> str:
        return self.__errorCode

    @errorCode.setter
    def errorCode(self, errorCode: str):
        self.__errorCode = errorCode

    @property
    def errorText(self) -> str:
        return self.__errorText

    @errorText.setter
    def errorText(self, errorText: str):
        self.__errorText = errorText

    @property
    def expressionLanguage(self) -> str:
        return self.__expressionLanguage

    @expressionLanguage.setter
    def expressionLanguage(self, expressionLanguage: str):
        self.__expressionLanguage = expressionLanguage

    @property
    def injected(self) -> bool:
        return self.__injected

    @injected.setter
    def injected(self, injected: bool):
        self.__injected = injected

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def Constraint(self):
        return self.__Constraint

    @Constraint.setter
    def Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_Constraint__Constraint", None)
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

    @property
    def constraint(self):
        return self.__constraint

    @constraint.setter
    def constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ISO20022_Constraint__constraint", None)
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
