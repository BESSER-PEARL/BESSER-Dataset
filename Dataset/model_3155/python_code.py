from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class SadlDataType(Enum):
    string = "string"
    boolean = "boolean"
    decimal = "decimal"
    int = "int"
    long = "long"
    float = "float"
    double = "double"
    duration = "duration"
    dateTime = "dateTime"
    gYearMonth = "gYearMonth"
    gYear = "gYear"
    gMonthDay = "gMonthDay"
    gDay = "gDay"
    gMonth = "gMonth"
    hexBinary = "hexBinary"
    base64Binary = "base64Binary"
    anyURI = "anyURI"
    integer = "integer"
    negativeInteger = "negativeInteger"
    nonNegativeInteger = "nonNegativeInteger"
    positiveInteger = "positiveInteger"
    nonPositiveInteger = "nonPositiveInteger"
    byte = "byte"
    unsignedByte = "unsignedByte"
    unsignedInt = "unsignedInt"
    anySimpleType = "anySimpleType"
    time = "time"
    date = "date"


############################################
# Definition of Classes
############################################

class SadlResource:

    pass
class sADL_Name(SadlResource):

    def __init__(self, function: bool, sADL_Name: set["sADL_Expression"] = None):
        self.function = function
        self.sADL_Name = sADL_Name if sADL_Name is not None else set()
        
    @property
    def function(self) -> bool:
        return self.__function

    @function.setter
    def function(self, function: bool):
        self.__function = function

    @property
    def sADL_Name(self):
        return self.__sADL_Name

    @sADL_Name.setter
    def sADL_Name(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_Name__sADL_Name", None)
        self.__sADL_Name = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sADL_Expression248"):
                    opp_val = getattr(item, "sADL_Expression248", None)
                    
                    if opp_val == self:
                        setattr(item, "sADL_Expression248", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sADL_Expression248"):
                    opp_val = getattr(item, "sADL_Expression248", None)
                    
                    setattr(item, "sADL_Expression248", self)
                    

class ExpressionScope:

    pass
class sADL_RuleStatement(ExpressionScope):

    pass
class sADL_QueryStatement(ExpressionScope):

    def __init__(self, start: str, sADL_QueryStatement: "sADL_SadlResource" = None, sADL_QueryStatement185: set["sADL_NamedStructureAnnotation"] = None, sADL_QueryStatement188: "sADL_Expression" = None):
        self.start = start
        self.sADL_QueryStatement = sADL_QueryStatement
        self.sADL_QueryStatement185 = sADL_QueryStatement185 if sADL_QueryStatement185 is not None else set()
        self.sADL_QueryStatement188 = sADL_QueryStatement188
        
    @property
    def start(self) -> str:
        return self.__start

    @start.setter
    def start(self, start: str):
        self.__start = start

    @property
    def sADL_QueryStatement185(self):
        return self.__sADL_QueryStatement185

    @sADL_QueryStatement185.setter
    def sADL_QueryStatement185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_QueryStatement__sADL_QueryStatement185", None)
        self.__sADL_QueryStatement185 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sADL_NamedStructureAnnotation186"):
                    opp_val = getattr(item, "sADL_NamedStructureAnnotation186", None)
                    
                    if opp_val == self:
                        setattr(item, "sADL_NamedStructureAnnotation186", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sADL_NamedStructureAnnotation186"):
                    opp_val = getattr(item, "sADL_NamedStructureAnnotation186", None)
                    
                    setattr(item, "sADL_NamedStructureAnnotation186", self)
                    

    @property
    def sADL_QueryStatement188(self):
        return self.__sADL_QueryStatement188

    @sADL_QueryStatement188.setter
    def sADL_QueryStatement188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_QueryStatement__sADL_QueryStatement188", None)
        self.__sADL_QueryStatement188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_Expression189"):
                opp_val = getattr(old_value, "sADL_Expression189", None)
                if opp_val == self:
                    setattr(old_value, "sADL_Expression189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_Expression189"):
                opp_val = getattr(value, "sADL_Expression189", None)
                setattr(value, "sADL_Expression189", self)

    @property
    def sADL_QueryStatement(self):
        return self.__sADL_QueryStatement

    @sADL_QueryStatement.setter
    def sADL_QueryStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_QueryStatement__sADL_QueryStatement", None)
        self.__sADL_QueryStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_SadlResource183"):
                opp_val = getattr(old_value, "sADL_SadlResource183", None)
                if opp_val == self:
                    setattr(old_value, "sADL_SadlResource183", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_SadlResource183"):
                opp_val = getattr(value, "sADL_SadlResource183", None)
                setattr(value, "sADL_SadlResource183", self)

class sADL_TestStatement(ExpressionScope):

    pass
class sADL_ExpressionStatement(ExpressionScope):

    def __init__(self, evaluatesTo: str, sADL_ExpressionStatement: "sADL_Expression" = None):
        self.evaluatesTo = evaluatesTo
        self.sADL_ExpressionStatement = sADL_ExpressionStatement
        
    @property
    def evaluatesTo(self) -> str:
        return self.__evaluatesTo

    @evaluatesTo.setter
    def evaluatesTo(self, evaluatesTo: str):
        self.__evaluatesTo = evaluatesTo

    @property
    def sADL_ExpressionStatement(self):
        return self.__sADL_ExpressionStatement

    @sADL_ExpressionStatement.setter
    def sADL_ExpressionStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_ExpressionStatement__sADL_ExpressionStatement", None)
        self.__sADL_ExpressionStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_Expression170"):
                opp_val = getattr(old_value, "sADL_Expression170", None)
                if opp_val == self:
                    setattr(old_value, "sADL_Expression170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_Expression170"):
                opp_val = getattr(value, "sADL_Expression170", None)
                setattr(value, "sADL_Expression170", self)

class SadlInstance:

    pass
class sADL_SadlNestedInstance(SadlInstance):

    def __init__(self, article: str):
        self.article = article
        
    @property
    def article(self) -> str:
        return self.__article

    @article.setter
    def article(self, article: str):
        self.__article = article

class sADL_ValueRow:

    pass
class sADL_OrderElement:

    def __init__(self, desc: bool, sADL_OrderElement: "sADL_SadlResource" = None, sADL_OrderElement212: "sADL_SelectExpression" = None):
        self.desc = desc
        self.sADL_OrderElement = sADL_OrderElement
        self.sADL_OrderElement212 = sADL_OrderElement212
        
    @property
    def desc(self) -> bool:
        return self.__desc

    @desc.setter
    def desc(self, desc: bool):
        self.__desc = desc

    @property
    def sADL_OrderElement(self):
        return self.__sADL_OrderElement

    @sADL_OrderElement.setter
    def sADL_OrderElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_OrderElement__sADL_OrderElement", None)
        self.__sADL_OrderElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_SadlResource90"):
                opp_val = getattr(old_value, "sADL_SadlResource90", None)
                if opp_val == self:
                    setattr(old_value, "sADL_SadlResource90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_SadlResource90"):
                opp_val = getattr(value, "sADL_SadlResource90", None)
                setattr(value, "sADL_SadlResource90", self)

    @property
    def sADL_OrderElement212(self):
        return self.__sADL_OrderElement212

    @sADL_OrderElement212.setter
    def sADL_OrderElement212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_OrderElement__sADL_OrderElement212", None)
        self.__sADL_OrderElement212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_SelectExpression211"):
                opp_val = getattr(old_value, "sADL_SelectExpression211", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_SelectExpression211"):
                opp_val = getattr(value, "sADL_SelectExpression211", None)
                if opp_val is None:
                    setattr(value, "sADL_SelectExpression211", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sADL_NamedStructureAnnotation:

    pass
class SadlExplicitValue:

    pass
class sADL_SadlUnaryExpression(SadlExplicitValue):

    def __init__(self, operator: str, sADL_SadlUnaryExpression: "sADL_SadlExplicitValueLiteral" = None):
        self.operator = operator
        self.sADL_SadlUnaryExpression = sADL_SadlUnaryExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def sADL_SadlUnaryExpression(self):
        return self.__sADL_SadlUnaryExpression

    @sADL_SadlUnaryExpression.setter
    def sADL_SadlUnaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SadlUnaryExpression__sADL_SadlUnaryExpression", None)
        self.__sADL_SadlUnaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_SadlExplicitValueLiteral"):
                opp_val = getattr(old_value, "sADL_SadlExplicitValueLiteral", None)
                if opp_val == self:
                    setattr(old_value, "sADL_SadlExplicitValueLiteral", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_SadlExplicitValueLiteral"):
                opp_val = getattr(value, "sADL_SadlExplicitValueLiteral", None)
                setattr(value, "sADL_SadlExplicitValueLiteral", self)

class sADL_SadlExplicitValueLiteral(SadlExplicitValue):

    pass
class sADL_SadlExplicitValue:

    pass
class SadlCondition:

    pass
class sADL_SadlHasValueCondition(SadlCondition):

    pass
class sADL_SadlCardinalityCondition(SadlCondition):

    def __init__(self, operator: str, cardinality: str, sADL_SadlCardinalityCondition75: "sADL_SadlDataTypeFacet" = None, sADL_SadlCardinalityCondition: "sADL_SadlTypeReference" = None):
        self.operator = operator
        self.cardinality = cardinality
        self.sADL_SadlCardinalityCondition75 = sADL_SadlCardinalityCondition75
        self.sADL_SadlCardinalityCondition = sADL_SadlCardinalityCondition
        
    @property
    def cardinality(self) -> str:
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, cardinality: str):
        self.__cardinality = cardinality

    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def sADL_SadlCardinalityCondition75(self):
        return self.__sADL_SadlCardinalityCondition75

    @sADL_SadlCardinalityCondition75.setter
    def sADL_SadlCardinalityCondition75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SadlCardinalityCondition__sADL_SadlCardinalityCondition75", None)
        self.__sADL_SadlCardinalityCondition75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_SadlDataTypeFacet76"):
                opp_val = getattr(old_value, "sADL_SadlDataTypeFacet76", None)
                if opp_val == self:
                    setattr(old_value, "sADL_SadlDataTypeFacet76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_SadlDataTypeFacet76"):
                opp_val = getattr(value, "sADL_SadlDataTypeFacet76", None)
                setattr(value, "sADL_SadlDataTypeFacet76", self)

    @property
    def sADL_SadlCardinalityCondition(self):
        return self.__sADL_SadlCardinalityCondition

    @sADL_SadlCardinalityCondition.setter
    def sADL_SadlCardinalityCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SadlCardinalityCondition__sADL_SadlCardinalityCondition", None)
        self.__sADL_SadlCardinalityCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_SadlTypeReference73"):
                opp_val = getattr(old_value, "sADL_SadlTypeReference73", None)
                if opp_val == self:
                    setattr(old_value, "sADL_SadlTypeReference73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_SadlTypeReference73"):
                opp_val = getattr(value, "sADL_SadlTypeReference73", None)
                setattr(value, "sADL_SadlTypeReference73", self)

class sADL_SadlAllValuesCondition(SadlCondition):

    pass
class SadlPropertyRestriction:

    pass
class sADL_SadlIsFunctional(SadlPropertyRestriction):

    def __init__(self, inverse: bool):
        self.inverse = inverse
        
    @property
    def inverse(self) -> bool:
        return self.__inverse

    @inverse.setter
    def inverse(self, inverse: bool):
        self.__inverse = inverse

class sADL_SadlIsTransitive(SadlPropertyRestriction):

    pass
class sADL_SadlIsInverseOf(SadlPropertyRestriction):

    pass
class sADL_SadlRangeRestriction(SadlPropertyRestriction):

    def __init__(self, singleValued: bool, typeonly: str, sADL_SadlRangeRestriction: "sADL_SadlTypeReference" = None, sADL_SadlRangeRestriction158: "sADL_SadlDataTypeFacet" = None):
        self.singleValued = singleValued
        self.typeonly = typeonly
        self.sADL_SadlRangeRestriction = sADL_SadlRangeRestriction
        self.sADL_SadlRangeRestriction158 = sADL_SadlRangeRestriction158
        
    @property
    def singleValued(self) -> bool:
        return self.__singleValued

    @singleValued.setter
    def singleValued(self, singleValued: bool):
        self.__singleValued = singleValued

    @property
    def typeonly(self) -> str:
        return self.__typeonly

    @typeonly.setter
    def typeonly(self, typeonly: str):
        self.__typeonly = typeonly

    @property
    def sADL_SadlRangeRestriction(self):
        return self.__sADL_SadlRangeRestriction

    @sADL_SadlRangeRestriction.setter
    def sADL_SadlRangeRestriction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SadlRangeRestriction__sADL_SadlRangeRestriction", None)
        self.__sADL_SadlRangeRestriction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_SadlTypeReference156"):
                opp_val = getattr(old_value, "sADL_SadlTypeReference156", None)
                if opp_val == self:
                    setattr(old_value, "sADL_SadlTypeReference156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_SadlTypeReference156"):
                opp_val = getattr(value, "sADL_SadlTypeReference156", None)
                setattr(value, "sADL_SadlTypeReference156", self)

    @property
    def sADL_SadlRangeRestriction158(self):
        return self.__sADL_SadlRangeRestriction158

    @sADL_SadlRangeRestriction158.setter
    def sADL_SadlRangeRestriction158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SadlRangeRestriction__sADL_SadlRangeRestriction158", None)
        self.__sADL_SadlRangeRestriction158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_SadlDataTypeFacet159"):
                opp_val = getattr(old_value, "sADL_SadlDataTypeFacet159", None)
                if opp_val == self:
                    setattr(old_value, "sADL_SadlDataTypeFacet159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_SadlDataTypeFacet159"):
                opp_val = getattr(value, "sADL_SadlDataTypeFacet159", None)
                setattr(value, "sADL_SadlDataTypeFacet159", self)

class sADL_SadlDefaultValue(SadlPropertyRestriction):

    def __init__(self, level: int, sADL_SadlDefaultValue: "sADL_SadlExplicitValue" = None):
        self.level = level
        self.sADL_SadlDefaultValue = sADL_SadlDefaultValue
        
    @property
    def level(self) -> int:
        return self.__level

    @level.setter
    def level(self, level: int):
        self.__level = level

    @property
    def sADL_SadlDefaultValue(self):
        return self.__sADL_SadlDefaultValue

    @sADL_SadlDefaultValue.setter
    def sADL_SadlDefaultValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SadlDefaultValue__sADL_SadlDefaultValue", None)
        self.__sADL_SadlDefaultValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_SadlExplicitValue163"):
                opp_val = getattr(old_value, "sADL_SadlExplicitValue163", None)
                if opp_val == self:
                    setattr(old_value, "sADL_SadlExplicitValue163", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_SadlExplicitValue163"):
                opp_val = getattr(value, "sADL_SadlExplicitValue163", None)
                setattr(value, "sADL_SadlExplicitValue163", self)

class sADL_SadlTypeAssociation(SadlPropertyRestriction):

    pass
class sADL_SadlCanOnlyBeOneOf(SadlPropertyRestriction):

    pass
class sADL_SadlMustBeOneOf(SadlPropertyRestriction):

    pass
class sADL_SadlIsSymmetrical(SadlPropertyRestriction):

    pass
class sADL_SadlIsAnnotation(SadlPropertyRestriction):

    pass
class sADL_SadlPropertyRestriction:

    pass
class sADL_SadlDataTypeFacet:

    def __init__(self, minInclusive: bool, min: str, max: str, maxInclusive: bool, regex: str, len: str, minlen: str, maxlen: str, values: str, sADL_SadlDataTypeFacet: "sADL_SadlAllValuesCondition" = None, sADL_SadlDataTypeFacet76: "sADL_SadlCardinalityCondition" = None, sADL_SadlDataTypeFacet108: "sADL_SadlClassOrPropertyDeclaration" = None, sADL_SadlDataTypeFacet159: "sADL_SadlRangeRestriction" = None):
        self.minInclusive = minInclusive
        self.min = min
        self.max = max
        self.maxInclusive = maxInclusive
        self.regex = regex
        self.len = len
        self.minlen = minlen
        self.maxlen = maxlen
        self.values = values
        self.sADL_SadlDataTypeFacet = sADL_SadlDataTypeFacet
        self.sADL_SadlDataTypeFacet76 = sADL_SadlDataTypeFacet76
        self.sADL_SadlDataTypeFacet108 = sADL_SadlDataTypeFacet108
        self.sADL_SadlDataTypeFacet159 = sADL_SadlDataTypeFacet159
        
    @property
    def len(self) -> str:
        return self.__len

    @len.setter
    def len(self, len: str):
        self.__len = len

    @property
    def max(self) -> str:
        return self.__max

    @max.setter
    def max(self, max: str):
        self.__max = max

    @property
    def minInclusive(self) -> bool:
        return self.__minInclusive

    @minInclusive.setter
    def minInclusive(self, minInclusive: bool):
        self.__minInclusive = minInclusive

    @property
    def min(self) -> str:
        return self.__min

    @min.setter
    def min(self, min: str):
        self.__min = min

    @property
    def minlen(self) -> str:
        return self.__minlen

    @minlen.setter
    def minlen(self, minlen: str):
        self.__minlen = minlen

    @property
    def maxlen(self) -> str:
        return self.__maxlen

    @maxlen.setter
    def maxlen(self, maxlen: str):
        self.__maxlen = maxlen

    @property
    def maxInclusive(self) -> bool:
        return self.__maxInclusive

    @maxInclusive.setter
    def maxInclusive(self, maxInclusive: bool):
        self.__maxInclusive = maxInclusive

    @property
    def regex(self) -> str:
        return self.__regex

    @regex.setter
    def regex(self, regex: str):
        self.__regex = regex

    @property
    def values(self) -> str:
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values

    @property
    def sADL_SadlDataTypeFacet108(self):
        return self.__sADL_SadlDataTypeFacet108

    @sADL_SadlDataTypeFacet108.setter
    def sADL_SadlDataTypeFacet108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SadlDataTypeFacet__sADL_SadlDataTypeFacet108", None)
        self.__sADL_SadlDataTypeFacet108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_SadlClassOrPropertyDeclaration107"):
                opp_val = getattr(old_value, "sADL_SadlClassOrPropertyDeclaration107", None)
                if opp_val == self:
                    setattr(old_value, "sADL_SadlClassOrPropertyDeclaration107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_SadlClassOrPropertyDeclaration107"):
                opp_val = getattr(value, "sADL_SadlClassOrPropertyDeclaration107", None)
                setattr(value, "sADL_SadlClassOrPropertyDeclaration107", self)

    @property
    def sADL_SadlDataTypeFacet76(self):
        return self.__sADL_SadlDataTypeFacet76

    @sADL_SadlDataTypeFacet76.setter
    def sADL_SadlDataTypeFacet76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SadlDataTypeFacet__sADL_SadlDataTypeFacet76", None)
        self.__sADL_SadlDataTypeFacet76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_SadlCardinalityCondition75"):
                opp_val = getattr(old_value, "sADL_SadlCardinalityCondition75", None)
                if opp_val == self:
                    setattr(old_value, "sADL_SadlCardinalityCondition75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_SadlCardinalityCondition75"):
                opp_val = getattr(value, "sADL_SadlCardinalityCondition75", None)
                setattr(value, "sADL_SadlCardinalityCondition75", self)

    @property
    def sADL_SadlDataTypeFacet159(self):
        return self.__sADL_SadlDataTypeFacet159

    @sADL_SadlDataTypeFacet159.setter
    def sADL_SadlDataTypeFacet159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SadlDataTypeFacet__sADL_SadlDataTypeFacet159", None)
        self.__sADL_SadlDataTypeFacet159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_SadlRangeRestriction158"):
                opp_val = getattr(old_value, "sADL_SadlRangeRestriction158", None)
                if opp_val == self:
                    setattr(old_value, "sADL_SadlRangeRestriction158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_SadlRangeRestriction158"):
                opp_val = getattr(value, "sADL_SadlRangeRestriction158", None)
                setattr(value, "sADL_SadlRangeRestriction158", self)

    @property
    def sADL_SadlDataTypeFacet(self):
        return self.__sADL_SadlDataTypeFacet

    @sADL_SadlDataTypeFacet.setter
    def sADL_SadlDataTypeFacet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SadlDataTypeFacet__sADL_SadlDataTypeFacet", None)
        self.__sADL_SadlDataTypeFacet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_SadlAllValuesCondition69"):
                opp_val = getattr(old_value, "sADL_SadlAllValuesCondition69", None)
                if opp_val == self:
                    setattr(old_value, "sADL_SadlAllValuesCondition69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_SadlAllValuesCondition69"):
                opp_val = getattr(value, "sADL_SadlAllValuesCondition69", None)
                setattr(value, "sADL_SadlAllValuesCondition69", self)

class sADL_SadlCondition(SadlPropertyRestriction):

    pass
class Expression:

    pass
class sADL_BinaryOperation(Expression):

    def __init__(self, op: str, sADL_BinaryOperation: "sADL_Expression" = None, sADL_BinaryOperation221: "sADL_Expression" = None):
        self.op = op
        self.sADL_BinaryOperation = sADL_BinaryOperation
        self.sADL_BinaryOperation221 = sADL_BinaryOperation221
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def sADL_BinaryOperation(self):
        return self.__sADL_BinaryOperation

    @sADL_BinaryOperation.setter
    def sADL_BinaryOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_BinaryOperation__sADL_BinaryOperation", None)
        self.__sADL_BinaryOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_Expression219"):
                opp_val = getattr(old_value, "sADL_Expression219", None)
                if opp_val == self:
                    setattr(old_value, "sADL_Expression219", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_Expression219"):
                opp_val = getattr(value, "sADL_Expression219", None)
                setattr(value, "sADL_Expression219", self)

    @property
    def sADL_BinaryOperation221(self):
        return self.__sADL_BinaryOperation221

    @sADL_BinaryOperation221.setter
    def sADL_BinaryOperation221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_BinaryOperation__sADL_BinaryOperation221", None)
        self.__sADL_BinaryOperation221 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_Expression222"):
                opp_val = getattr(old_value, "sADL_Expression222", None)
                if opp_val == self:
                    setattr(old_value, "sADL_Expression222", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_Expression222"):
                opp_val = getattr(value, "sADL_Expression222", None)
                setattr(value, "sADL_Expression222", self)

class sADL_ValueTable(Expression):

    pass
class sADL_Declaration(Expression):

    def __init__(self, ordinal: str, len: str, maxlen: str, article: str, sADL_Declaration: "sADL_SadlTypeReference" = None, sADL_Declaration245: set["sADL_Expression"] = None):
        self.ordinal = ordinal
        self.len = len
        self.maxlen = maxlen
        self.article = article
        self.sADL_Declaration = sADL_Declaration
        self.sADL_Declaration245 = sADL_Declaration245 if sADL_Declaration245 is not None else set()
        
    @property
    def maxlen(self) -> str:
        return self.__maxlen

    @maxlen.setter
    def maxlen(self, maxlen: str):
        self.__maxlen = maxlen

    @property
    def len(self) -> str:
        return self.__len

    @len.setter
    def len(self, len: str):
        self.__len = len

    @property
    def article(self) -> str:
        return self.__article

    @article.setter
    def article(self, article: str):
        self.__article = article

    @property
    def ordinal(self) -> str:
        return self.__ordinal

    @ordinal.setter
    def ordinal(self, ordinal: str):
        self.__ordinal = ordinal

    @property
    def sADL_Declaration245(self):
        return self.__sADL_Declaration245

    @sADL_Declaration245.setter
    def sADL_Declaration245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_Declaration__sADL_Declaration245", None)
        self.__sADL_Declaration245 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sADL_Expression246"):
                    opp_val = getattr(item, "sADL_Expression246", None)
                    
                    if opp_val == self:
                        setattr(item, "sADL_Expression246", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sADL_Expression246"):
                    opp_val = getattr(item, "sADL_Expression246", None)
                    
                    setattr(item, "sADL_Expression246", self)
                    

    @property
    def sADL_Declaration(self):
        return self.__sADL_Declaration

    @sADL_Declaration.setter
    def sADL_Declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_Declaration__sADL_Declaration", None)
        self.__sADL_Declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_SadlTypeReference243"):
                opp_val = getattr(old_value, "sADL_SadlTypeReference243", None)
                if opp_val == self:
                    setattr(old_value, "sADL_SadlTypeReference243", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_SadlTypeReference243"):
                opp_val = getattr(value, "sADL_SadlTypeReference243", None)
                setattr(value, "sADL_SadlTypeReference243", self)

class sADL_PropOfSubject(Expression):

    def __init__(self, of: str, sADL_PropOfSubject: "sADL_Expression" = None, sADL_PropOfSubject226: "sADL_Expression" = None):
        self.of = of
        self.sADL_PropOfSubject = sADL_PropOfSubject
        self.sADL_PropOfSubject226 = sADL_PropOfSubject226
        
    @property
    def of(self) -> str:
        return self.__of

    @of.setter
    def of(self, of: str):
        self.__of = of

    @property
    def sADL_PropOfSubject(self):
        return self.__sADL_PropOfSubject

    @sADL_PropOfSubject.setter
    def sADL_PropOfSubject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_PropOfSubject__sADL_PropOfSubject", None)
        self.__sADL_PropOfSubject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_Expression224"):
                opp_val = getattr(old_value, "sADL_Expression224", None)
                if opp_val == self:
                    setattr(old_value, "sADL_Expression224", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_Expression224"):
                opp_val = getattr(value, "sADL_Expression224", None)
                setattr(value, "sADL_Expression224", self)

    @property
    def sADL_PropOfSubject226(self):
        return self.__sADL_PropOfSubject226

    @sADL_PropOfSubject226.setter
    def sADL_PropOfSubject226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_PropOfSubject__sADL_PropOfSubject226", None)
        self.__sADL_PropOfSubject226 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_Expression227"):
                opp_val = getattr(old_value, "sADL_Expression227", None)
                if opp_val == self:
                    setattr(old_value, "sADL_Expression227", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_Expression227"):
                opp_val = getattr(value, "sADL_Expression227", None)
                setattr(value, "sADL_Expression227", self)

class sADL_StringLiteral(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class sADL_ElementInList(Expression):

    def __init__(self, before: bool, after: bool, sADL_ElementInList: "sADL_Expression" = None):
        self.before = before
        self.after = after
        self.sADL_ElementInList = sADL_ElementInList
        
    @property
    def after(self) -> bool:
        return self.__after

    @after.setter
    def after(self, after: bool):
        self.__after = after

    @property
    def before(self) -> bool:
        return self.__before

    @before.setter
    def before(self, before: bool):
        self.__before = before

    @property
    def sADL_ElementInList(self):
        return self.__sADL_ElementInList

    @sADL_ElementInList.setter
    def sADL_ElementInList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_ElementInList__sADL_ElementInList", None)
        self.__sADL_ElementInList = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_Expression237"):
                opp_val = getattr(old_value, "sADL_Expression237", None)
                if opp_val == self:
                    setattr(old_value, "sADL_Expression237", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_Expression237"):
                opp_val = getattr(value, "sADL_Expression237", None)
                setattr(value, "sADL_Expression237", self)

class sADL_Constant(Expression):

    def __init__(self, constant: str):
        self.constant = constant
        
    @property
    def constant(self) -> str:
        return self.__constant

    @constant.setter
    def constant(self, constant: str):
        self.__constant = constant

class sADL_AskExpression(Expression):

    pass
class sADL_UnaryExpression(Expression):

    def __init__(self, op: str, sADL_UnaryExpression: "sADL_Expression" = None):
        self.op = op
        self.sADL_UnaryExpression = sADL_UnaryExpression
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def sADL_UnaryExpression(self):
        return self.__sADL_UnaryExpression

    @sADL_UnaryExpression.setter
    def sADL_UnaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_UnaryExpression__sADL_UnaryExpression", None)
        self.__sADL_UnaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_Expression241"):
                opp_val = getattr(old_value, "sADL_Expression241", None)
                if opp_val == self:
                    setattr(old_value, "sADL_Expression241", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_Expression241"):
                opp_val = getattr(value, "sADL_Expression241", None)
                setattr(value, "sADL_Expression241", self)

class sADL_UnitExpression(Expression):

    def __init__(self, unit: str, sADL_UnitExpression: "sADL_Expression" = None):
        self.unit = unit
        self.sADL_UnitExpression = sADL_UnitExpression
        
    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

    @property
    def sADL_UnitExpression(self):
        return self.__sADL_UnitExpression

    @sADL_UnitExpression.setter
    def sADL_UnitExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_UnitExpression__sADL_UnitExpression", None)
        self.__sADL_UnitExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_Expression239"):
                opp_val = getattr(old_value, "sADL_Expression239", None)
                if opp_val == self:
                    setattr(old_value, "sADL_Expression239", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_Expression239"):
                opp_val = getattr(value, "sADL_Expression239", None)
                setattr(value, "sADL_Expression239", self)

class sADL_SubjHasProp(Expression):

    def __init__(self, comma: bool, sADL_SubjHasProp231: "sADL_SadlResource" = None, sADL_SubjHasProp234: "sADL_Expression" = None, sADL_SubjHasProp: "sADL_Expression" = None):
        self.comma = comma
        self.sADL_SubjHasProp231 = sADL_SubjHasProp231
        self.sADL_SubjHasProp234 = sADL_SubjHasProp234
        self.sADL_SubjHasProp = sADL_SubjHasProp
        
    @property
    def comma(self) -> bool:
        return self.__comma

    @comma.setter
    def comma(self, comma: bool):
        self.__comma = comma

    @property
    def sADL_SubjHasProp(self):
        return self.__sADL_SubjHasProp

    @sADL_SubjHasProp.setter
    def sADL_SubjHasProp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SubjHasProp__sADL_SubjHasProp", None)
        self.__sADL_SubjHasProp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_Expression229"):
                opp_val = getattr(old_value, "sADL_Expression229", None)
                if opp_val == self:
                    setattr(old_value, "sADL_Expression229", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_Expression229"):
                opp_val = getattr(value, "sADL_Expression229", None)
                setattr(value, "sADL_Expression229", self)

    @property
    def sADL_SubjHasProp234(self):
        return self.__sADL_SubjHasProp234

    @sADL_SubjHasProp234.setter
    def sADL_SubjHasProp234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SubjHasProp__sADL_SubjHasProp234", None)
        self.__sADL_SubjHasProp234 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_Expression235"):
                opp_val = getattr(old_value, "sADL_Expression235", None)
                if opp_val == self:
                    setattr(old_value, "sADL_Expression235", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_Expression235"):
                opp_val = getattr(value, "sADL_Expression235", None)
                setattr(value, "sADL_Expression235", self)

    @property
    def sADL_SubjHasProp231(self):
        return self.__sADL_SubjHasProp231

    @sADL_SubjHasProp231.setter
    def sADL_SubjHasProp231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SubjHasProp__sADL_SubjHasProp231", None)
        self.__sADL_SubjHasProp231 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_SadlResource232"):
                opp_val = getattr(old_value, "sADL_SadlResource232", None)
                if opp_val == self:
                    setattr(old_value, "sADL_SadlResource232", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_SadlResource232"):
                opp_val = getattr(value, "sADL_SadlResource232", None)
                setattr(value, "sADL_SadlResource232", self)

class sADL_Sublist(Expression):

    pass
class sADL_BooleanLiteral(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class sADL_NumberLiteral(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class sADL_SelectExpression(Expression):

    def __init__(self, distinct: bool, orderby: str, sADL_SelectExpression: set["sADL_SadlResource"] = None, sADL_SelectExpression208: "sADL_Expression" = None, sADL_SelectExpression211: set["sADL_OrderElement"] = None):
        self.distinct = distinct
        self.orderby = orderby
        self.sADL_SelectExpression = sADL_SelectExpression if sADL_SelectExpression is not None else set()
        self.sADL_SelectExpression208 = sADL_SelectExpression208
        self.sADL_SelectExpression211 = sADL_SelectExpression211 if sADL_SelectExpression211 is not None else set()
        
    @property
    def distinct(self) -> bool:
        return self.__distinct

    @distinct.setter
    def distinct(self, distinct: bool):
        self.__distinct = distinct

    @property
    def orderby(self) -> str:
        return self.__orderby

    @orderby.setter
    def orderby(self, orderby: str):
        self.__orderby = orderby

    @property
    def sADL_SelectExpression(self):
        return self.__sADL_SelectExpression

    @sADL_SelectExpression.setter
    def sADL_SelectExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SelectExpression__sADL_SelectExpression", None)
        self.__sADL_SelectExpression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sADL_SadlResource206"):
                    opp_val = getattr(item, "sADL_SadlResource206", None)
                    
                    if opp_val == self:
                        setattr(item, "sADL_SadlResource206", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sADL_SadlResource206"):
                    opp_val = getattr(item, "sADL_SadlResource206", None)
                    
                    setattr(item, "sADL_SadlResource206", self)
                    

    @property
    def sADL_SelectExpression208(self):
        return self.__sADL_SelectExpression208

    @sADL_SelectExpression208.setter
    def sADL_SelectExpression208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SelectExpression__sADL_SelectExpression208", None)
        self.__sADL_SelectExpression208 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_Expression209"):
                opp_val = getattr(old_value, "sADL_Expression209", None)
                if opp_val == self:
                    setattr(old_value, "sADL_Expression209", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_Expression209"):
                opp_val = getattr(value, "sADL_Expression209", None)
                setattr(value, "sADL_Expression209", self)

    @property
    def sADL_SelectExpression211(self):
        return self.__sADL_SelectExpression211

    @sADL_SelectExpression211.setter
    def sADL_SelectExpression211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SelectExpression__sADL_SelectExpression211", None)
        self.__sADL_SelectExpression211 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sADL_OrderElement212"):
                    opp_val = getattr(item, "sADL_OrderElement212", None)
                    
                    if opp_val == self:
                        setattr(item, "sADL_OrderElement212", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sADL_OrderElement212"):
                    opp_val = getattr(item, "sADL_OrderElement212", None)
                    
                    setattr(item, "sADL_OrderElement212", self)
                    

class sADL_ConstructExpression(Expression):

    pass
class SadlExplicitValueLiteral:

    pass
class sADL_SadlNumberLiteral(SadlExplicitValueLiteral):

    def __init__(self, literalNumber: str, unit: str):
        self.literalNumber = literalNumber
        self.unit = unit
        
    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

    @property
    def literalNumber(self) -> str:
        return self.__literalNumber

    @literalNumber.setter
    def literalNumber(self, literalNumber: str):
        self.__literalNumber = literalNumber

class sADL_SadlStringLiteral(SadlExplicitValueLiteral):

    def __init__(self, literalString: str):
        self.literalString = literalString
        
    @property
    def literalString(self) -> str:
        return self.__literalString

    @literalString.setter
    def literalString(self, literalString: str):
        self.__literalString = literalString

class sADL_SadlBooleanLiteral(SadlExplicitValueLiteral):

    def __init__(self, truethy: bool):
        self.truethy = truethy
        
    @property
    def truethy(self) -> bool:
        return self.__truethy

    @truethy.setter
    def truethy(self, truethy: bool):
        self.__truethy = truethy

class sADL_SadlConstantLiteral(SadlExplicitValueLiteral):

    def __init__(self, term: str):
        self.term = term
        
    @property
    def term(self) -> str:
        return self.__term

    @term.setter
    def term(self, term: str):
        self.__term = term

class sADL_SadlValueList(SadlExplicitValueLiteral):

    pass
class SadlStatement:

    pass
class sADL_SadlDisjointClasses(SadlStatement):

    pass
class sADL_SadlProperty(SadlStatement):

    def __init__(self, primaryDeclaration: bool, sADL_SadlProperty: "sADL_SadlResource" = None, sADL_SadlProperty53: set["sADL_SadlPropertyRestriction"] = None, sADL_SadlProperty58: "sADL_SadlTypeReference" = None, sADL_SadlProperty61: "sADL_SadlResource" = None, sADL_SadlProperty64: set["sADL_SadlResource"] = None, sADL_SadlProperty55: "sADL_SadlTypeReference" = None, sADL_SadlProperty111: "sADL_SadlClassOrPropertyDeclaration" = None):
        self.primaryDeclaration = primaryDeclaration
        self.sADL_SadlProperty = sADL_SadlProperty
        self.sADL_SadlProperty53 = sADL_SadlProperty53 if sADL_SadlProperty53 is not None else set()
        self.sADL_SadlProperty58 = sADL_SadlProperty58
        self.sADL_SadlProperty61 = sADL_SadlProperty61
        self.sADL_SadlProperty64 = sADL_SadlProperty64 if sADL_SadlProperty64 is not None else set()
        self.sADL_SadlProperty55 = sADL_SadlProperty55
        self.sADL_SadlProperty111 = sADL_SadlProperty111
        
    @property
    def primaryDeclaration(self) -> bool:
        return self.__primaryDeclaration

    @primaryDeclaration.setter
    def primaryDeclaration(self, primaryDeclaration: bool):
        self.__primaryDeclaration = primaryDeclaration

    @property
    def sADL_SadlProperty111(self):
        return self.__sADL_SadlProperty111

    @sADL_SadlProperty111.setter
    def sADL_SadlProperty111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SadlProperty__sADL_SadlProperty111", None)
        self.__sADL_SadlProperty111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_SadlClassOrPropertyDeclaration110"):
                opp_val = getattr(old_value, "sADL_SadlClassOrPropertyDeclaration110", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_SadlClassOrPropertyDeclaration110"):
                opp_val = getattr(value, "sADL_SadlClassOrPropertyDeclaration110", None)
                if opp_val is None:
                    setattr(value, "sADL_SadlClassOrPropertyDeclaration110", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sADL_SadlProperty58(self):
        return self.__sADL_SadlProperty58

    @sADL_SadlProperty58.setter
    def sADL_SadlProperty58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SadlProperty__sADL_SadlProperty58", None)
        self.__sADL_SadlProperty58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_SadlTypeReference59"):
                opp_val = getattr(old_value, "sADL_SadlTypeReference59", None)
                if opp_val == self:
                    setattr(old_value, "sADL_SadlTypeReference59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_SadlTypeReference59"):
                opp_val = getattr(value, "sADL_SadlTypeReference59", None)
                setattr(value, "sADL_SadlTypeReference59", self)

    @property
    def sADL_SadlProperty55(self):
        return self.__sADL_SadlProperty55

    @sADL_SadlProperty55.setter
    def sADL_SadlProperty55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SadlProperty__sADL_SadlProperty55", None)
        self.__sADL_SadlProperty55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_SadlTypeReference56"):
                opp_val = getattr(old_value, "sADL_SadlTypeReference56", None)
                if opp_val == self:
                    setattr(old_value, "sADL_SadlTypeReference56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_SadlTypeReference56"):
                opp_val = getattr(value, "sADL_SadlTypeReference56", None)
                setattr(value, "sADL_SadlTypeReference56", self)

    @property
    def sADL_SadlProperty61(self):
        return self.__sADL_SadlProperty61

    @sADL_SadlProperty61.setter
    def sADL_SadlProperty61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SadlProperty__sADL_SadlProperty61", None)
        self.__sADL_SadlProperty61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_SadlResource62"):
                opp_val = getattr(old_value, "sADL_SadlResource62", None)
                if opp_val == self:
                    setattr(old_value, "sADL_SadlResource62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_SadlResource62"):
                opp_val = getattr(value, "sADL_SadlResource62", None)
                setattr(value, "sADL_SadlResource62", self)

    @property
    def sADL_SadlProperty(self):
        return self.__sADL_SadlProperty

    @sADL_SadlProperty.setter
    def sADL_SadlProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SadlProperty__sADL_SadlProperty", None)
        self.__sADL_SadlProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_SadlResource51"):
                opp_val = getattr(old_value, "sADL_SadlResource51", None)
                if opp_val == self:
                    setattr(old_value, "sADL_SadlResource51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_SadlResource51"):
                opp_val = getattr(value, "sADL_SadlResource51", None)
                setattr(value, "sADL_SadlResource51", self)

    @property
    def sADL_SadlProperty64(self):
        return self.__sADL_SadlProperty64

    @sADL_SadlProperty64.setter
    def sADL_SadlProperty64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SadlProperty__sADL_SadlProperty64", None)
        self.__sADL_SadlProperty64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sADL_SadlResource65"):
                    opp_val = getattr(item, "sADL_SadlResource65", None)
                    
                    if opp_val == self:
                        setattr(item, "sADL_SadlResource65", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sADL_SadlResource65"):
                    opp_val = getattr(item, "sADL_SadlResource65", None)
                    
                    setattr(item, "sADL_SadlResource65", self)
                    

    @property
    def sADL_SadlProperty53(self):
        return self.__sADL_SadlProperty53

    @sADL_SadlProperty53.setter
    def sADL_SadlProperty53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SadlProperty__sADL_SadlProperty53", None)
        self.__sADL_SadlProperty53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sADL_SadlPropertyRestriction"):
                    opp_val = getattr(item, "sADL_SadlPropertyRestriction", None)
                    
                    if opp_val == self:
                        setattr(item, "sADL_SadlPropertyRestriction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sADL_SadlPropertyRestriction"):
                    opp_val = getattr(item, "sADL_SadlPropertyRestriction", None)
                    
                    setattr(item, "sADL_SadlPropertyRestriction", self)
                    

class sADL_SadlNecessaryAndSufficient(SadlStatement):

    pass
class sADL_SadlSameAs(SadlStatement):

    def __init__(self, complement: bool, sADL_SadlSameAs: "sADL_SadlResource" = None, sADL_SadlSameAs118: "sADL_SadlTypeReference" = None):
        self.complement = complement
        self.sADL_SadlSameAs = sADL_SadlSameAs
        self.sADL_SadlSameAs118 = sADL_SadlSameAs118
        
    @property
    def complement(self) -> bool:
        return self.__complement

    @complement.setter
    def complement(self, complement: bool):
        self.__complement = complement

    @property
    def sADL_SadlSameAs(self):
        return self.__sADL_SadlSameAs

    @sADL_SadlSameAs.setter
    def sADL_SadlSameAs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SadlSameAs__sADL_SadlSameAs", None)
        self.__sADL_SadlSameAs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_SadlResource116"):
                opp_val = getattr(old_value, "sADL_SadlResource116", None)
                if opp_val == self:
                    setattr(old_value, "sADL_SadlResource116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_SadlResource116"):
                opp_val = getattr(value, "sADL_SadlResource116", None)
                setattr(value, "sADL_SadlResource116", self)

    @property
    def sADL_SadlSameAs118(self):
        return self.__sADL_SadlSameAs118

    @sADL_SadlSameAs118.setter
    def sADL_SadlSameAs118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SadlSameAs__sADL_SadlSameAs118", None)
        self.__sADL_SadlSameAs118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_SadlTypeReference119"):
                opp_val = getattr(old_value, "sADL_SadlTypeReference119", None)
                if opp_val == self:
                    setattr(old_value, "sADL_SadlTypeReference119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_SadlTypeReference119"):
                opp_val = getattr(value, "sADL_SadlTypeReference119", None)
                setattr(value, "sADL_SadlTypeReference119", self)

class sADL_SadlClassOrPropertyDeclaration(SadlStatement):

    pass
class sADL_SadlDifferentFrom(SadlStatement):

    def __init__(self, complement: bool, sADL_SadlDifferentFrom123: "sADL_SadlTypeReference" = None, sADL_SadlDifferentFrom126: set["sADL_SadlClassOrPropertyDeclaration"] = None, sADL_SadlDifferentFrom: "sADL_SadlResource" = None):
        self.complement = complement
        self.sADL_SadlDifferentFrom123 = sADL_SadlDifferentFrom123
        self.sADL_SadlDifferentFrom126 = sADL_SadlDifferentFrom126 if sADL_SadlDifferentFrom126 is not None else set()
        self.sADL_SadlDifferentFrom = sADL_SadlDifferentFrom
        
    @property
    def complement(self) -> bool:
        return self.__complement

    @complement.setter
    def complement(self, complement: bool):
        self.__complement = complement

    @property
    def sADL_SadlDifferentFrom(self):
        return self.__sADL_SadlDifferentFrom

    @sADL_SadlDifferentFrom.setter
    def sADL_SadlDifferentFrom(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SadlDifferentFrom__sADL_SadlDifferentFrom", None)
        self.__sADL_SadlDifferentFrom = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_SadlResource121"):
                opp_val = getattr(old_value, "sADL_SadlResource121", None)
                if opp_val == self:
                    setattr(old_value, "sADL_SadlResource121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_SadlResource121"):
                opp_val = getattr(value, "sADL_SadlResource121", None)
                setattr(value, "sADL_SadlResource121", self)

    @property
    def sADL_SadlDifferentFrom126(self):
        return self.__sADL_SadlDifferentFrom126

    @sADL_SadlDifferentFrom126.setter
    def sADL_SadlDifferentFrom126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SadlDifferentFrom__sADL_SadlDifferentFrom126", None)
        self.__sADL_SadlDifferentFrom126 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sADL_SadlClassOrPropertyDeclaration127"):
                    opp_val = getattr(item, "sADL_SadlClassOrPropertyDeclaration127", None)
                    
                    if opp_val == self:
                        setattr(item, "sADL_SadlClassOrPropertyDeclaration127", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sADL_SadlClassOrPropertyDeclaration127"):
                    opp_val = getattr(item, "sADL_SadlClassOrPropertyDeclaration127", None)
                    
                    setattr(item, "sADL_SadlClassOrPropertyDeclaration127", self)
                    

    @property
    def sADL_SadlDifferentFrom123(self):
        return self.__sADL_SadlDifferentFrom123

    @sADL_SadlDifferentFrom123.setter
    def sADL_SadlDifferentFrom123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SadlDifferentFrom__sADL_SadlDifferentFrom123", None)
        self.__sADL_SadlDifferentFrom123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_SadlTypeReference124"):
                opp_val = getattr(old_value, "sADL_SadlTypeReference124", None)
                if opp_val == self:
                    setattr(old_value, "sADL_SadlTypeReference124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_SadlTypeReference124"):
                opp_val = getattr(value, "sADL_SadlTypeReference124", None)
                setattr(value, "sADL_SadlTypeReference124", self)

class sADL_SadlInstance(SadlStatement):

    pass
class sADL_EObject:

    pass
class sADL_SadlPropertyInitializer:

    pass
class SadlTypeReference:

    pass
class sADL_SadlIntersectionType(SadlTypeReference):

    pass
class sADL_SadlSimpleTypeReference(SadlTypeReference):

    def __init__(self, list: bool, sADL_SadlSimpleTypeReference: "sADL_SadlResource" = None):
        self.list = list
        self.sADL_SadlSimpleTypeReference = sADL_SadlSimpleTypeReference
        
    @property
    def list(self) -> bool:
        return self.__list

    @list.setter
    def list(self, list: bool):
        self.__list = list

    @property
    def sADL_SadlSimpleTypeReference(self):
        return self.__sADL_SadlSimpleTypeReference

    @sADL_SadlSimpleTypeReference.setter
    def sADL_SadlSimpleTypeReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SadlSimpleTypeReference__sADL_SadlSimpleTypeReference", None)
        self.__sADL_SadlSimpleTypeReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_SadlResource152"):
                opp_val = getattr(old_value, "sADL_SadlResource152", None)
                if opp_val == self:
                    setattr(old_value, "sADL_SadlResource152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_SadlResource152"):
                opp_val = getattr(value, "sADL_SadlResource152", None)
                setattr(value, "sADL_SadlResource152", self)

class sADL_SadlUnionType(SadlTypeReference):

    pass
class sADL_SadlPrimitiveDataType(SadlTypeReference):

    def __init__(self, primitiveType: str, list: bool):
        self.primitiveType = primitiveType
        self.list = list
        
    @property
    def list(self) -> bool:
        return self.__list

    @list.setter
    def list(self, list: bool):
        self.__list = list

    @property
    def primitiveType(self) -> str:
        return self.__primitiveType

    @primitiveType.setter
    def primitiveType(self, primitiveType: str):
        self.__primitiveType = primitiveType

class sADL_SadlPropertyCondition(SadlTypeReference):

    pass
class sADL_SadlTypeReference(SadlStatement):

    pass
class sADL_SadlParameterDeclaration:

    def __init__(self, unknown: str, ellipsis: str, sADL_SadlParameterDeclaration: "sADL_AbstractSadlEquation" = None, sADL_SadlParameterDeclaration15: "sADL_SadlTypeReference" = None, sADL_SadlParameterDeclaration18: "sADL_SadlResource" = None):
        self.unknown = unknown
        self.ellipsis = ellipsis
        self.sADL_SadlParameterDeclaration = sADL_SadlParameterDeclaration
        self.sADL_SadlParameterDeclaration15 = sADL_SadlParameterDeclaration15
        self.sADL_SadlParameterDeclaration18 = sADL_SadlParameterDeclaration18
        
    @property
    def ellipsis(self) -> str:
        return self.__ellipsis

    @ellipsis.setter
    def ellipsis(self, ellipsis: str):
        self.__ellipsis = ellipsis

    @property
    def unknown(self) -> str:
        return self.__unknown

    @unknown.setter
    def unknown(self, unknown: str):
        self.__unknown = unknown

    @property
    def sADL_SadlParameterDeclaration15(self):
        return self.__sADL_SadlParameterDeclaration15

    @sADL_SadlParameterDeclaration15.setter
    def sADL_SadlParameterDeclaration15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SadlParameterDeclaration__sADL_SadlParameterDeclaration15", None)
        self.__sADL_SadlParameterDeclaration15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_SadlTypeReference16"):
                opp_val = getattr(old_value, "sADL_SadlTypeReference16", None)
                if opp_val == self:
                    setattr(old_value, "sADL_SadlTypeReference16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_SadlTypeReference16"):
                opp_val = getattr(value, "sADL_SadlTypeReference16", None)
                setattr(value, "sADL_SadlTypeReference16", self)

    @property
    def sADL_SadlParameterDeclaration18(self):
        return self.__sADL_SadlParameterDeclaration18

    @sADL_SadlParameterDeclaration18.setter
    def sADL_SadlParameterDeclaration18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SadlParameterDeclaration__sADL_SadlParameterDeclaration18", None)
        self.__sADL_SadlParameterDeclaration18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_SadlResource19"):
                opp_val = getattr(old_value, "sADL_SadlResource19", None)
                if opp_val == self:
                    setattr(old_value, "sADL_SadlResource19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_SadlResource19"):
                opp_val = getattr(value, "sADL_SadlResource19", None)
                setattr(value, "sADL_SadlResource19", self)

    @property
    def sADL_SadlParameterDeclaration(self):
        return self.__sADL_SadlParameterDeclaration

    @sADL_SadlParameterDeclaration.setter
    def sADL_SadlParameterDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SadlParameterDeclaration__sADL_SadlParameterDeclaration", None)
        self.__sADL_SadlParameterDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_AbstractSadlEquation11"):
                opp_val = getattr(old_value, "sADL_AbstractSadlEquation11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_AbstractSadlEquation11"):
                opp_val = getattr(value, "sADL_AbstractSadlEquation11", None)
                if opp_val is None:
                    setattr(value, "sADL_AbstractSadlEquation11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sADL_SadlResource(SadlStatement, SadlExplicitValueLiteral, Expression):

    pass
class sADL_AbstractSadlEquation:

    def __init__(self, unknown: str, sADL_AbstractSadlEquation: "sADL_SadlResource" = None, sADL_AbstractSadlEquation11: set["sADL_SadlParameterDeclaration"] = None, sADL_AbstractSadlEquation13: "sADL_SadlTypeReference" = None):
        self.unknown = unknown
        self.sADL_AbstractSadlEquation = sADL_AbstractSadlEquation
        self.sADL_AbstractSadlEquation11 = sADL_AbstractSadlEquation11 if sADL_AbstractSadlEquation11 is not None else set()
        self.sADL_AbstractSadlEquation13 = sADL_AbstractSadlEquation13
        
    @property
    def unknown(self) -> str:
        return self.__unknown

    @unknown.setter
    def unknown(self, unknown: str):
        self.__unknown = unknown

    @property
    def sADL_AbstractSadlEquation11(self):
        return self.__sADL_AbstractSadlEquation11

    @sADL_AbstractSadlEquation11.setter
    def sADL_AbstractSadlEquation11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_AbstractSadlEquation__sADL_AbstractSadlEquation11", None)
        self.__sADL_AbstractSadlEquation11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sADL_SadlParameterDeclaration"):
                    opp_val = getattr(item, "sADL_SadlParameterDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "sADL_SadlParameterDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sADL_SadlParameterDeclaration"):
                    opp_val = getattr(item, "sADL_SadlParameterDeclaration", None)
                    
                    setattr(item, "sADL_SadlParameterDeclaration", self)
                    

    @property
    def sADL_AbstractSadlEquation13(self):
        return self.__sADL_AbstractSadlEquation13

    @sADL_AbstractSadlEquation13.setter
    def sADL_AbstractSadlEquation13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_AbstractSadlEquation__sADL_AbstractSadlEquation13", None)
        self.__sADL_AbstractSadlEquation13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_SadlTypeReference"):
                opp_val = getattr(old_value, "sADL_SadlTypeReference", None)
                if opp_val == self:
                    setattr(old_value, "sADL_SadlTypeReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_SadlTypeReference"):
                opp_val = getattr(value, "sADL_SadlTypeReference", None)
                setattr(value, "sADL_SadlTypeReference", self)

    @property
    def sADL_AbstractSadlEquation(self):
        return self.__sADL_AbstractSadlEquation

    @sADL_AbstractSadlEquation.setter
    def sADL_AbstractSadlEquation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_AbstractSadlEquation__sADL_AbstractSadlEquation", None)
        self.__sADL_AbstractSadlEquation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_SadlResource"):
                opp_val = getattr(old_value, "sADL_SadlResource", None)
                if opp_val == self:
                    setattr(old_value, "sADL_SadlResource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_SadlResource"):
                opp_val = getattr(value, "sADL_SadlResource", None)
                setattr(value, "sADL_SadlResource", self)

class sADL_SadlModel:

    def __init__(self, baseUri: str, alias: str, version: str, sADL_SadlModel: set["sADL_SadlAnnotation"] = None, sADL_SadlModel2: set["sADL_SadlImport"] = None, sADL_SadlModel4: set["sADL_SadlModelElement"] = None, sADL_SadlModel7: "sADL_SadlImport" = None):
        self.baseUri = baseUri
        self.alias = alias
        self.version = version
        self.sADL_SadlModel = sADL_SadlModel if sADL_SadlModel is not None else set()
        self.sADL_SadlModel2 = sADL_SadlModel2 if sADL_SadlModel2 is not None else set()
        self.sADL_SadlModel4 = sADL_SadlModel4 if sADL_SadlModel4 is not None else set()
        self.sADL_SadlModel7 = sADL_SadlModel7
        
    @property
    def baseUri(self) -> str:
        return self.__baseUri

    @baseUri.setter
    def baseUri(self, baseUri: str):
        self.__baseUri = baseUri

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def sADL_SadlModel(self):
        return self.__sADL_SadlModel

    @sADL_SadlModel.setter
    def sADL_SadlModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SadlModel__sADL_SadlModel", None)
        self.__sADL_SadlModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sADL_SadlAnnotation"):
                    opp_val = getattr(item, "sADL_SadlAnnotation", None)
                    
                    if opp_val == self:
                        setattr(item, "sADL_SadlAnnotation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sADL_SadlAnnotation"):
                    opp_val = getattr(item, "sADL_SadlAnnotation", None)
                    
                    setattr(item, "sADL_SadlAnnotation", self)
                    

    @property
    def sADL_SadlModel7(self):
        return self.__sADL_SadlModel7

    @sADL_SadlModel7.setter
    def sADL_SadlModel7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SadlModel__sADL_SadlModel7", None)
        self.__sADL_SadlModel7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_SadlImport6"):
                opp_val = getattr(old_value, "sADL_SadlImport6", None)
                if opp_val == self:
                    setattr(old_value, "sADL_SadlImport6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_SadlImport6"):
                opp_val = getattr(value, "sADL_SadlImport6", None)
                setattr(value, "sADL_SadlImport6", self)

    @property
    def sADL_SadlModel2(self):
        return self.__sADL_SadlModel2

    @sADL_SadlModel2.setter
    def sADL_SadlModel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SadlModel__sADL_SadlModel2", None)
        self.__sADL_SadlModel2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sADL_SadlImport"):
                    opp_val = getattr(item, "sADL_SadlImport", None)
                    
                    if opp_val == self:
                        setattr(item, "sADL_SadlImport", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sADL_SadlImport"):
                    opp_val = getattr(item, "sADL_SadlImport", None)
                    
                    setattr(item, "sADL_SadlImport", self)
                    

    @property
    def sADL_SadlModel4(self):
        return self.__sADL_SadlModel4

    @sADL_SadlModel4.setter
    def sADL_SadlModel4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SadlModel__sADL_SadlModel4", None)
        self.__sADL_SadlModel4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sADL_SadlModelElement"):
                    opp_val = getattr(item, "sADL_SadlModelElement", None)
                    
                    if opp_val == self:
                        setattr(item, "sADL_SadlModelElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sADL_SadlModelElement"):
                    opp_val = getattr(item, "sADL_SadlModelElement", None)
                    
                    setattr(item, "sADL_SadlModelElement", self)
                    

class sADL_Expression:

    pass
class AbstractSadlEquation:

    pass
class SadlModelElement:

    pass
class sADL_PrintStatement(SadlModelElement):

    def __init__(self, displayString: str, model: str):
        self.displayString = displayString
        self.model = model
        
    @property
    def model(self) -> str:
        return self.__model

    @model.setter
    def model(self, model: str):
        self.__model = model

    @property
    def displayString(self) -> str:
        return self.__displayString

    @displayString.setter
    def displayString(self, displayString: str):
        self.__displayString = displayString

class sADL_ExpressionScope(SadlModelElement):

    pass
class sADL_ExplainStatement(SadlModelElement):

    pass
class sADL_SadlStatement(SadlModelElement):

    pass
class sADL_ReadStatement(SadlModelElement):

    def __init__(self, filename: str, templateFilename: str):
        self.filename = filename
        self.templateFilename = templateFilename
        
    @property
    def templateFilename(self) -> str:
        return self.__templateFilename

    @templateFilename.setter
    def templateFilename(self, templateFilename: str):
        self.__templateFilename = templateFilename

    @property
    def filename(self) -> str:
        return self.__filename

    @filename.setter
    def filename(self, filename: str):
        self.__filename = filename

class sADL_StartWriteStatement(SadlModelElement):

    def __init__(self, write: str, dataOnly: str):
        self.write = write
        self.dataOnly = dataOnly
        
    @property
    def write(self) -> str:
        return self.__write

    @write.setter
    def write(self, write: str):
        self.__write = write

    @property
    def dataOnly(self) -> str:
        return self.__dataOnly

    @dataOnly.setter
    def dataOnly(self, dataOnly: str):
        self.__dataOnly = dataOnly

class sADL_EndWriteStatement(SadlModelElement):

    def __init__(self, filename: str):
        self.filename = filename
        
    @property
    def filename(self) -> str:
        return self.__filename

    @filename.setter
    def filename(self, filename: str):
        self.__filename = filename

class sADL_ExternalEquationStatement(AbstractSadlEquation, SadlModelElement):

    def __init__(self, uri: str, location: str):
        self.uri = uri
        self.location = location
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

class sADL_EquationStatement(AbstractSadlEquation, SadlModelElement):

    pass
class sADL_SadlModelElement:

    pass
class sADL_SadlImport:

    def __init__(self, alias: str, sADL_SadlImport: "sADL_SadlModel" = None, sADL_SadlImport6: "sADL_SadlModel" = None):
        self.alias = alias
        self.sADL_SadlImport = sADL_SadlImport
        self.sADL_SadlImport6 = sADL_SadlImport6
        
    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def sADL_SadlImport6(self):
        return self.__sADL_SadlImport6

    @sADL_SadlImport6.setter
    def sADL_SadlImport6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SadlImport__sADL_SadlImport6", None)
        self.__sADL_SadlImport6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_SadlModel7"):
                opp_val = getattr(old_value, "sADL_SadlModel7", None)
                if opp_val == self:
                    setattr(old_value, "sADL_SadlModel7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_SadlModel7"):
                opp_val = getattr(value, "sADL_SadlModel7", None)
                setattr(value, "sADL_SadlModel7", self)

    @property
    def sADL_SadlImport(self):
        return self.__sADL_SadlImport

    @sADL_SadlImport.setter
    def sADL_SadlImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SadlImport__sADL_SadlImport", None)
        self.__sADL_SadlImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_SadlModel2"):
                opp_val = getattr(old_value, "sADL_SadlModel2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_SadlModel2"):
                opp_val = getattr(value, "sADL_SadlModel2", None)
                if opp_val is None:
                    setattr(value, "sADL_SadlModel2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sADL_SadlAnnotation:

    def __init__(self, type: str, contents: str, sADL_SadlAnnotation: "sADL_SadlModel" = None, sADL_SadlAnnotation49: "sADL_SadlResource" = None):
        self.type = type
        self.contents = contents
        self.sADL_SadlAnnotation = sADL_SadlAnnotation
        self.sADL_SadlAnnotation49 = sADL_SadlAnnotation49
        
    @property
    def contents(self) -> str:
        return self.__contents

    @contents.setter
    def contents(self, contents: str):
        self.__contents = contents

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def sADL_SadlAnnotation49(self):
        return self.__sADL_SadlAnnotation49

    @sADL_SadlAnnotation49.setter
    def sADL_SadlAnnotation49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SadlAnnotation__sADL_SadlAnnotation49", None)
        self.__sADL_SadlAnnotation49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_SadlResource48"):
                opp_val = getattr(old_value, "sADL_SadlResource48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_SadlResource48"):
                opp_val = getattr(value, "sADL_SadlResource48", None)
                if opp_val is None:
                    setattr(value, "sADL_SadlResource48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sADL_SadlAnnotation(self):
        return self.__sADL_SadlAnnotation

    @sADL_SadlAnnotation.setter
    def sADL_SadlAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sADL_SadlAnnotation__sADL_SadlAnnotation", None)
        self.__sADL_SadlAnnotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sADL_SadlModel"):
                opp_val = getattr(old_value, "sADL_SadlModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sADL_SadlModel"):
                opp_val = getattr(value, "sADL_SadlModel", None)
                if opp_val is None:
                    setattr(value, "sADL_SadlModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
