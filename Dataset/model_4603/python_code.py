from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Type(Enum):
    eEList = "eEList"
    eEnumerator = "eEnumerator"
    eFeatureMap = "eFeatureMap"
    eFeatureMapEntry = "eFeatureMapEntry"
    eFloat = "eFloat"
    eFloatObject = "eFloatObject"
    eInt = "eInt"
    eIntegerObject = "eIntegerObject"
    eTreeIterator = "eTreeIterator"
    eInvocationTargetException = "eInvocationTargetException"
    eJavaClass = "eJavaClass"
    eJavaObject = "eJavaObject"
    eLong = "eLong"
    eLongObject = "eLongObject"
    eMap = "eMap"
    eResource = "eResource"
    eResourceSet = "eResourceSet"
    eShort = "eShort"
    eShortObject = "eShortObject"
    eString = "eString"
    eBigDecimal = "eBigDecimal"
    eBigInteger = "eBigInteger"
    eBoolean = "eBoolean"
    eBooleanObject = "eBooleanObject"
    eByte = "eByte"
    eByteArray = "eByteArray"
    eByteObject = "eByteObject"
    eChar = "eChar"
    eCharacterObject = "eCharacterObject"
    eDate = "eDate"
    eDiagnosticChain = "eDiagnosticChain"
    eDouble = "eDouble"
    eDoubleObject = "eDoubleObject"


############################################
# Definition of Classes
############################################

class Expression:

    pass
class henshin_text_JavaClassValue(Expression):

    def __init__(self, value: str, henshin_text_JavaClassValue: set["henshin_text_Expression"] = None):
        self.value = value
        self.henshin_text_JavaClassValue = henshin_text_JavaClassValue if henshin_text_JavaClassValue is not None else set()
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def henshin_text_JavaClassValue(self):
        return self.__henshin_text_JavaClassValue

    @henshin_text_JavaClassValue.setter
    def henshin_text_JavaClassValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_text_JavaClassValue__henshin_text_JavaClassValue", None)
        self.__henshin_text_JavaClassValue = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "henshin_text_Expression153"):
                    opp_val = getattr(item, "henshin_text_Expression153", None)
                    
                    if opp_val == self:
                        setattr(item, "henshin_text_Expression153", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "henshin_text_Expression153"):
                    opp_val = getattr(item, "henshin_text_Expression153", None)
                    
                    setattr(item, "henshin_text_Expression153", self)
                    

class henshin_text_AndExpression(Expression):

    pass
class henshin_text_StringValue(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class henshin_text_NotExpression(Expression):

    pass
class henshin_text_ParameterValue(Expression):

    pass
class henshin_text_IntegerValue(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class henshin_text_MinusExpression(Expression):

    pass
class henshin_text_PlusExpression(Expression):

    pass
class henshin_text_BracketExpression(Expression):

    pass
class henshin_text_EqualityExpression(Expression):

    def __init__(self, op: str, henshin_text_EqualityExpression: "henshin_text_Expression" = None, henshin_text_EqualityExpression124: "henshin_text_Expression" = None):
        self.op = op
        self.henshin_text_EqualityExpression = henshin_text_EqualityExpression
        self.henshin_text_EqualityExpression124 = henshin_text_EqualityExpression124
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def henshin_text_EqualityExpression124(self):
        return self.__henshin_text_EqualityExpression124

    @henshin_text_EqualityExpression124.setter
    def henshin_text_EqualityExpression124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_text_EqualityExpression__henshin_text_EqualityExpression124", None)
        self.__henshin_text_EqualityExpression124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_text_Expression125"):
                opp_val = getattr(old_value, "henshin_text_Expression125", None)
                if opp_val == self:
                    setattr(old_value, "henshin_text_Expression125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_text_Expression125"):
                opp_val = getattr(value, "henshin_text_Expression125", None)
                setattr(value, "henshin_text_Expression125", self)

    @property
    def henshin_text_EqualityExpression(self):
        return self.__henshin_text_EqualityExpression

    @henshin_text_EqualityExpression.setter
    def henshin_text_EqualityExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_text_EqualityExpression__henshin_text_EqualityExpression", None)
        self.__henshin_text_EqualityExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_text_Expression122"):
                opp_val = getattr(old_value, "henshin_text_Expression122", None)
                if opp_val == self:
                    setattr(old_value, "henshin_text_Expression122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_text_Expression122"):
                opp_val = getattr(value, "henshin_text_Expression122", None)
                setattr(value, "henshin_text_Expression122", self)

class henshin_text_JavaAttributeValue(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class henshin_text_NumberValue(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class henshin_text_MulOrDivExpression(Expression):

    def __init__(self, op: str, henshin_text_MulOrDivExpression: "henshin_text_Expression" = None, henshin_text_MulOrDivExpression144: "henshin_text_Expression" = None):
        self.op = op
        self.henshin_text_MulOrDivExpression = henshin_text_MulOrDivExpression
        self.henshin_text_MulOrDivExpression144 = henshin_text_MulOrDivExpression144
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def henshin_text_MulOrDivExpression(self):
        return self.__henshin_text_MulOrDivExpression

    @henshin_text_MulOrDivExpression.setter
    def henshin_text_MulOrDivExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_text_MulOrDivExpression__henshin_text_MulOrDivExpression", None)
        self.__henshin_text_MulOrDivExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_text_Expression142"):
                opp_val = getattr(old_value, "henshin_text_Expression142", None)
                if opp_val == self:
                    setattr(old_value, "henshin_text_Expression142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_text_Expression142"):
                opp_val = getattr(value, "henshin_text_Expression142", None)
                setattr(value, "henshin_text_Expression142", self)

    @property
    def henshin_text_MulOrDivExpression144(self):
        return self.__henshin_text_MulOrDivExpression144

    @henshin_text_MulOrDivExpression144.setter
    def henshin_text_MulOrDivExpression144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_text_MulOrDivExpression__henshin_text_MulOrDivExpression144", None)
        self.__henshin_text_MulOrDivExpression144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_text_Expression145"):
                opp_val = getattr(old_value, "henshin_text_Expression145", None)
                if opp_val == self:
                    setattr(old_value, "henshin_text_Expression145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_text_Expression145"):
                opp_val = getattr(value, "henshin_text_Expression145", None)
                setattr(value, "henshin_text_Expression145", self)

class henshin_text_BoolValue(Expression):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class henshin_text_NaturalValue(Expression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class henshin_text_ComparisonExpression(Expression):

    def __init__(self, op: str, henshin_text_ComparisonExpression: "henshin_text_Expression" = None, henshin_text_ComparisonExpression129: "henshin_text_Expression" = None):
        self.op = op
        self.henshin_text_ComparisonExpression = henshin_text_ComparisonExpression
        self.henshin_text_ComparisonExpression129 = henshin_text_ComparisonExpression129
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def henshin_text_ComparisonExpression129(self):
        return self.__henshin_text_ComparisonExpression129

    @henshin_text_ComparisonExpression129.setter
    def henshin_text_ComparisonExpression129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_text_ComparisonExpression__henshin_text_ComparisonExpression129", None)
        self.__henshin_text_ComparisonExpression129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_text_Expression130"):
                opp_val = getattr(old_value, "henshin_text_Expression130", None)
                if opp_val == self:
                    setattr(old_value, "henshin_text_Expression130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_text_Expression130"):
                opp_val = getattr(value, "henshin_text_Expression130", None)
                setattr(value, "henshin_text_Expression130", self)

    @property
    def henshin_text_ComparisonExpression(self):
        return self.__henshin_text_ComparisonExpression

    @henshin_text_ComparisonExpression.setter
    def henshin_text_ComparisonExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_text_ComparisonExpression__henshin_text_ComparisonExpression", None)
        self.__henshin_text_ComparisonExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_text_Expression127"):
                opp_val = getattr(old_value, "henshin_text_Expression127", None)
                if opp_val == self:
                    setattr(old_value, "henshin_text_Expression127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_text_Expression127"):
                opp_val = getattr(value, "henshin_text_Expression127", None)
                setattr(value, "henshin_text_Expression127", self)

class henshin_text_OrExpression(Expression):

    pass
class henshin_text_ParameterType:

    def __init__(self, enumType: str, henshin_text_ParameterType: "henshin_text_Parameter" = None, henshin_text_ParameterType86: "henshin_text_EClass" = None):
        self.enumType = enumType
        self.henshin_text_ParameterType = henshin_text_ParameterType
        self.henshin_text_ParameterType86 = henshin_text_ParameterType86
        
    @property
    def enumType(self) -> str:
        return self.__enumType

    @enumType.setter
    def enumType(self, enumType: str):
        self.__enumType = enumType

    @property
    def henshin_text_ParameterType(self):
        return self.__henshin_text_ParameterType

    @henshin_text_ParameterType.setter
    def henshin_text_ParameterType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_text_ParameterType__henshin_text_ParameterType", None)
        self.__henshin_text_ParameterType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_text_Parameter84"):
                opp_val = getattr(old_value, "henshin_text_Parameter84", None)
                if opp_val == self:
                    setattr(old_value, "henshin_text_Parameter84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_text_Parameter84"):
                opp_val = getattr(value, "henshin_text_Parameter84", None)
                setattr(value, "henshin_text_Parameter84", self)

    @property
    def henshin_text_ParameterType86(self):
        return self.__henshin_text_ParameterType86

    @henshin_text_ParameterType86.setter
    def henshin_text_ParameterType86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_text_ParameterType__henshin_text_ParameterType86", None)
        self.__henshin_text_ParameterType86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_text_EClass87"):
                opp_val = getattr(old_value, "henshin_text_EClass87", None)
                if opp_val == self:
                    setattr(old_value, "henshin_text_EClass87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_text_EClass87"):
                opp_val = getattr(value, "henshin_text_EClass87", None)
                setattr(value, "henshin_text_EClass87", self)

class Logic:

    pass
class henshin_text_AND(Logic):

    pass
class henshin_text_Not(Logic):

    pass
class henshin_text_ConditionGraphRef(Logic):

    pass
class henshin_text_ORorXOR(Logic):

    def __init__(self, op: str, henshin_text_ORorXOR: "henshin_text_Logic" = None, henshin_text_ORorXOR95: "henshin_text_Logic" = None):
        self.op = op
        self.henshin_text_ORorXOR = henshin_text_ORorXOR
        self.henshin_text_ORorXOR95 = henshin_text_ORorXOR95
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def henshin_text_ORorXOR95(self):
        return self.__henshin_text_ORorXOR95

    @henshin_text_ORorXOR95.setter
    def henshin_text_ORorXOR95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_text_ORorXOR__henshin_text_ORorXOR95", None)
        self.__henshin_text_ORorXOR95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_text_Logic96"):
                opp_val = getattr(old_value, "henshin_text_Logic96", None)
                if opp_val == self:
                    setattr(old_value, "henshin_text_Logic96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_text_Logic96"):
                opp_val = getattr(value, "henshin_text_Logic96", None)
                setattr(value, "henshin_text_Logic96", self)

    @property
    def henshin_text_ORorXOR(self):
        return self.__henshin_text_ORorXOR

    @henshin_text_ORorXOR.setter
    def henshin_text_ORorXOR(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_text_ORorXOR__henshin_text_ORorXOR", None)
        self.__henshin_text_ORorXOR = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_text_Logic93"):
                opp_val = getattr(old_value, "henshin_text_Logic93", None)
                if opp_val == self:
                    setattr(old_value, "henshin_text_Logic93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_text_Logic93"):
                opp_val = getattr(value, "henshin_text_Logic93", None)
                setattr(value, "henshin_text_Logic93", self)

class ModelElement:

    pass
class henshin_text_Unit(ModelElement):

    pass
class henshin_text_Rule(ModelElement):

    pass
class henshin_text_ConditionNodeTypes:

    def __init__(self, name: str, henshin_text_ConditionNodeTypes50: "henshin_text_ConditionReuseNode" = None, henshin_text_ConditionNodeTypes: "henshin_text_ConditionEdge" = None, henshin_text_ConditionNodeTypes41: "henshin_text_ConditionEdge" = None):
        self.name = name
        self.henshin_text_ConditionNodeTypes50 = henshin_text_ConditionNodeTypes50
        self.henshin_text_ConditionNodeTypes = henshin_text_ConditionNodeTypes
        self.henshin_text_ConditionNodeTypes41 = henshin_text_ConditionNodeTypes41
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def henshin_text_ConditionNodeTypes(self):
        return self.__henshin_text_ConditionNodeTypes

    @henshin_text_ConditionNodeTypes.setter
    def henshin_text_ConditionNodeTypes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_text_ConditionNodeTypes__henshin_text_ConditionNodeTypes", None)
        self.__henshin_text_ConditionNodeTypes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_text_ConditionEdge38"):
                opp_val = getattr(old_value, "henshin_text_ConditionEdge38", None)
                if opp_val == self:
                    setattr(old_value, "henshin_text_ConditionEdge38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_text_ConditionEdge38"):
                opp_val = getattr(value, "henshin_text_ConditionEdge38", None)
                setattr(value, "henshin_text_ConditionEdge38", self)

    @property
    def henshin_text_ConditionNodeTypes50(self):
        return self.__henshin_text_ConditionNodeTypes50

    @henshin_text_ConditionNodeTypes50.setter
    def henshin_text_ConditionNodeTypes50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_text_ConditionNodeTypes__henshin_text_ConditionNodeTypes50", None)
        self.__henshin_text_ConditionNodeTypes50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_text_ConditionReuseNode"):
                opp_val = getattr(old_value, "henshin_text_ConditionReuseNode", None)
                if opp_val == self:
                    setattr(old_value, "henshin_text_ConditionReuseNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_text_ConditionReuseNode"):
                opp_val = getattr(value, "henshin_text_ConditionReuseNode", None)
                setattr(value, "henshin_text_ConditionReuseNode", self)

    @property
    def henshin_text_ConditionNodeTypes41(self):
        return self.__henshin_text_ConditionNodeTypes41

    @henshin_text_ConditionNodeTypes41.setter
    def henshin_text_ConditionNodeTypes41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_text_ConditionNodeTypes__henshin_text_ConditionNodeTypes41", None)
        self.__henshin_text_ConditionNodeTypes41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_text_ConditionEdge40"):
                opp_val = getattr(old_value, "henshin_text_ConditionEdge40", None)
                if opp_val == self:
                    setattr(old_value, "henshin_text_ConditionEdge40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_text_ConditionEdge40"):
                opp_val = getattr(value, "henshin_text_ConditionEdge40", None)
                setattr(value, "henshin_text_ConditionEdge40", self)

class henshin_text_ConditionEdge:

    pass
class henshin_text_ConditionGraphElements:

    pass
class henshin_text_ConditionGraph:

    def __init__(self, name: str, henshin_text_ConditionGraph: "henshin_text_Formula" = None, henshin_text_ConditionGraph35: set["henshin_text_ConditionGraphElements"] = None, henshin_text_ConditionGraph105: "henshin_text_ConditionGraphRef" = None):
        self.name = name
        self.henshin_text_ConditionGraph = henshin_text_ConditionGraph
        self.henshin_text_ConditionGraph35 = henshin_text_ConditionGraph35 if henshin_text_ConditionGraph35 is not None else set()
        self.henshin_text_ConditionGraph105 = henshin_text_ConditionGraph105
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def henshin_text_ConditionGraph(self):
        return self.__henshin_text_ConditionGraph

    @henshin_text_ConditionGraph.setter
    def henshin_text_ConditionGraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_text_ConditionGraph__henshin_text_ConditionGraph", None)
        self.__henshin_text_ConditionGraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_text_Formula33"):
                opp_val = getattr(old_value, "henshin_text_Formula33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_text_Formula33"):
                opp_val = getattr(value, "henshin_text_Formula33", None)
                if opp_val is None:
                    setattr(value, "henshin_text_Formula33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def henshin_text_ConditionGraph35(self):
        return self.__henshin_text_ConditionGraph35

    @henshin_text_ConditionGraph35.setter
    def henshin_text_ConditionGraph35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_text_ConditionGraph__henshin_text_ConditionGraph35", None)
        self.__henshin_text_ConditionGraph35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "henshin_text_ConditionGraphElements"):
                    opp_val = getattr(item, "henshin_text_ConditionGraphElements", None)
                    
                    if opp_val == self:
                        setattr(item, "henshin_text_ConditionGraphElements", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "henshin_text_ConditionGraphElements"):
                    opp_val = getattr(item, "henshin_text_ConditionGraphElements", None)
                    
                    setattr(item, "henshin_text_ConditionGraphElements", self)
                    

    @property
    def henshin_text_ConditionGraph105(self):
        return self.__henshin_text_ConditionGraph105

    @henshin_text_ConditionGraph105.setter
    def henshin_text_ConditionGraph105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_text_ConditionGraph__henshin_text_ConditionGraph105", None)
        self.__henshin_text_ConditionGraph105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_text_ConditionGraphRef"):
                opp_val = getattr(old_value, "henshin_text_ConditionGraphRef", None)
                if opp_val == self:
                    setattr(old_value, "henshin_text_ConditionGraphRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_text_ConditionGraphRef"):
                opp_val = getattr(value, "henshin_text_ConditionGraphRef", None)
                setattr(value, "henshin_text_ConditionGraphRef", self)

class henshin_text_List:

    pass
class SequentialProperties:

    pass
class henshin_text_Rollback(SequentialProperties):

    def __init__(self, rollback: bool):
        self.rollback = rollback
        
    @property
    def rollback(self) -> bool:
        return self.__rollback

    @rollback.setter
    def rollback(self, rollback: bool):
        self.__rollback = rollback

class henshin_text_Strict(SequentialProperties):

    def __init__(self, strict: bool):
        self.strict = strict
        
    @property
    def strict(self) -> bool:
        return self.__strict

    @strict.setter
    def strict(self, strict: bool):
        self.__strict = strict

class UnitElement:

    pass
class henshin_text_IteratedUnit(UnitElement):

    pass
class henshin_text_ConditionalUnit(UnitElement):

    pass
class henshin_text_PriorityUnit(UnitElement):

    pass
class henshin_text_Call(UnitElement):

    pass
class henshin_text_LoopUnit(UnitElement):

    pass
class henshin_text_IndependentUnit(UnitElement):

    pass
class henshin_text_SequentialProperties(UnitElement):

    pass
class henshin_text_UnitElement:

    pass
class henshin_text_Match:

    pass
class henshin_text_EReference:

    pass
class henshin_text_RuleNodeTypes:

    pass
class henshin_text_Edge:

    def __init__(self, actiontype: str, henshin_text_Edge: "henshin_text_Edges" = None, henshin_text_Edge11: "henshin_text_RuleNodeTypes" = None, henshin_text_Edge13: "henshin_text_RuleNodeTypes" = None, henshin_text_Edge16: "henshin_text_EReference" = None):
        self.actiontype = actiontype
        self.henshin_text_Edge = henshin_text_Edge
        self.henshin_text_Edge11 = henshin_text_Edge11
        self.henshin_text_Edge13 = henshin_text_Edge13
        self.henshin_text_Edge16 = henshin_text_Edge16
        
    @property
    def actiontype(self) -> str:
        return self.__actiontype

    @actiontype.setter
    def actiontype(self, actiontype: str):
        self.__actiontype = actiontype

    @property
    def henshin_text_Edge13(self):
        return self.__henshin_text_Edge13

    @henshin_text_Edge13.setter
    def henshin_text_Edge13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_text_Edge__henshin_text_Edge13", None)
        self.__henshin_text_Edge13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_text_RuleNodeTypes14"):
                opp_val = getattr(old_value, "henshin_text_RuleNodeTypes14", None)
                if opp_val == self:
                    setattr(old_value, "henshin_text_RuleNodeTypes14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_text_RuleNodeTypes14"):
                opp_val = getattr(value, "henshin_text_RuleNodeTypes14", None)
                setattr(value, "henshin_text_RuleNodeTypes14", self)

    @property
    def henshin_text_Edge16(self):
        return self.__henshin_text_Edge16

    @henshin_text_Edge16.setter
    def henshin_text_Edge16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_text_Edge__henshin_text_Edge16", None)
        self.__henshin_text_Edge16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_text_EReference"):
                opp_val = getattr(old_value, "henshin_text_EReference", None)
                if opp_val == self:
                    setattr(old_value, "henshin_text_EReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_text_EReference"):
                opp_val = getattr(value, "henshin_text_EReference", None)
                setattr(value, "henshin_text_EReference", self)

    @property
    def henshin_text_Edge11(self):
        return self.__henshin_text_Edge11

    @henshin_text_Edge11.setter
    def henshin_text_Edge11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_text_Edge__henshin_text_Edge11", None)
        self.__henshin_text_Edge11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_text_RuleNodeTypes"):
                opp_val = getattr(old_value, "henshin_text_RuleNodeTypes", None)
                if opp_val == self:
                    setattr(old_value, "henshin_text_RuleNodeTypes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_text_RuleNodeTypes"):
                opp_val = getattr(value, "henshin_text_RuleNodeTypes", None)
                setattr(value, "henshin_text_RuleNodeTypes", self)

    @property
    def henshin_text_Edge(self):
        return self.__henshin_text_Edge

    @henshin_text_Edge.setter
    def henshin_text_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_text_Edge__henshin_text_Edge", None)
        self.__henshin_text_Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_text_Edges"):
                opp_val = getattr(old_value, "henshin_text_Edges", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_text_Edges"):
                opp_val = getattr(value, "henshin_text_Edges", None)
                if opp_val is None:
                    setattr(value, "henshin_text_Edges", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class GraphElements:

    pass
class henshin_text_Edges(GraphElements):

    pass
class henshin_text_GraphElements:

    pass
class henshin_text_Expression:

    pass
class henshin_text_Logic:

    pass
class ConditionGraphElements:

    pass
class henshin_text_ConditionReuseNode(ConditionGraphElements):

    pass
class henshin_text_ConditionEdges(ConditionGraphElements):

    pass
class henshin_text_Formula(GraphElements, ConditionGraphElements):

    pass
class henshin_text_MultiRule(GraphElements):

    def __init__(self, name: str, henshin_text_MultiRule: set["henshin_text_RuleElement"] = None):
        self.name = name
        self.henshin_text_MultiRule = henshin_text_MultiRule if henshin_text_MultiRule is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def henshin_text_MultiRule(self):
        return self.__henshin_text_MultiRule

    @henshin_text_MultiRule.setter
    def henshin_text_MultiRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_text_MultiRule__henshin_text_MultiRule", None)
        self.__henshin_text_MultiRule = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "henshin_text_RuleElement"):
                    opp_val = getattr(item, "henshin_text_RuleElement", None)
                    
                    if opp_val == self:
                        setattr(item, "henshin_text_RuleElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "henshin_text_RuleElement"):
                    opp_val = getattr(item, "henshin_text_RuleElement", None)
                    
                    setattr(item, "henshin_text_RuleElement", self)
                    

class henshin_text_EAttribute:

    pass
class henshin_text_Attribute:

    def __init__(self, actiontype: str, update: str, henshin_text_Attribute: "henshin_text_Node" = None, henshin_text_Attribute24: "henshin_text_MultiRuleReuseNode" = None, henshin_text_Attribute26: "henshin_text_EAttribute" = None, henshin_text_Attribute28: "henshin_text_Expression" = None):
        self.actiontype = actiontype
        self.update = update
        self.henshin_text_Attribute = henshin_text_Attribute
        self.henshin_text_Attribute24 = henshin_text_Attribute24
        self.henshin_text_Attribute26 = henshin_text_Attribute26
        self.henshin_text_Attribute28 = henshin_text_Attribute28
        
    @property
    def update(self) -> str:
        return self.__update

    @update.setter
    def update(self, update: str):
        self.__update = update

    @property
    def actiontype(self) -> str:
        return self.__actiontype

    @actiontype.setter
    def actiontype(self, actiontype: str):
        self.__actiontype = actiontype

    @property
    def henshin_text_Attribute(self):
        return self.__henshin_text_Attribute

    @henshin_text_Attribute.setter
    def henshin_text_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_text_Attribute__henshin_text_Attribute", None)
        self.__henshin_text_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_text_Node19"):
                opp_val = getattr(old_value, "henshin_text_Node19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_text_Node19"):
                opp_val = getattr(value, "henshin_text_Node19", None)
                if opp_val is None:
                    setattr(value, "henshin_text_Node19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def henshin_text_Attribute24(self):
        return self.__henshin_text_Attribute24

    @henshin_text_Attribute24.setter
    def henshin_text_Attribute24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_text_Attribute__henshin_text_Attribute24", None)
        self.__henshin_text_Attribute24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_text_MultiRuleReuseNode23"):
                opp_val = getattr(old_value, "henshin_text_MultiRuleReuseNode23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_text_MultiRuleReuseNode23"):
                opp_val = getattr(value, "henshin_text_MultiRuleReuseNode23", None)
                if opp_val is None:
                    setattr(value, "henshin_text_MultiRuleReuseNode23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def henshin_text_Attribute28(self):
        return self.__henshin_text_Attribute28

    @henshin_text_Attribute28.setter
    def henshin_text_Attribute28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_text_Attribute__henshin_text_Attribute28", None)
        self.__henshin_text_Attribute28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_text_Expression29"):
                opp_val = getattr(old_value, "henshin_text_Expression29", None)
                if opp_val == self:
                    setattr(old_value, "henshin_text_Expression29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_text_Expression29"):
                opp_val = getattr(value, "henshin_text_Expression29", None)
                setattr(value, "henshin_text_Expression29", self)

    @property
    def henshin_text_Attribute26(self):
        return self.__henshin_text_Attribute26

    @henshin_text_Attribute26.setter
    def henshin_text_Attribute26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_text_Attribute__henshin_text_Attribute26", None)
        self.__henshin_text_Attribute26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_text_EAttribute"):
                opp_val = getattr(old_value, "henshin_text_EAttribute", None)
                if opp_val == self:
                    setattr(old_value, "henshin_text_EAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_text_EAttribute"):
                opp_val = getattr(value, "henshin_text_EAttribute", None)
                setattr(value, "henshin_text_EAttribute", self)

class henshin_text_EClass:

    pass
class ConditionNodeTypes:

    pass
class henshin_text_ConditionNode(ConditionNodeTypes, ConditionGraphElements):

    pass
class RuleNodeTypes:

    pass
class henshin_text_MultiRuleReuseNode(GraphElements, RuleNodeTypes):

    pass
class henshin_text_Node(ConditionNodeTypes, GraphElements, RuleNodeTypes):

    def __init__(self, actiontype: str, henshin_text_Node: "henshin_text_EClass" = None, henshin_text_Node19: set["henshin_text_Attribute"] = None, henshin_text_Node21: "henshin_text_MultiRuleReuseNode" = None):
        self.actiontype = actiontype
        self.henshin_text_Node = henshin_text_Node
        self.henshin_text_Node19 = henshin_text_Node19 if henshin_text_Node19 is not None else set()
        self.henshin_text_Node21 = henshin_text_Node21
        
    @property
    def actiontype(self) -> str:
        return self.__actiontype

    @actiontype.setter
    def actiontype(self, actiontype: str):
        self.__actiontype = actiontype

    @property
    def henshin_text_Node19(self):
        return self.__henshin_text_Node19

    @henshin_text_Node19.setter
    def henshin_text_Node19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_text_Node__henshin_text_Node19", None)
        self.__henshin_text_Node19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "henshin_text_Attribute"):
                    opp_val = getattr(item, "henshin_text_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "henshin_text_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "henshin_text_Attribute"):
                    opp_val = getattr(item, "henshin_text_Attribute", None)
                    
                    setattr(item, "henshin_text_Attribute", self)
                    

    @property
    def henshin_text_Node(self):
        return self.__henshin_text_Node

    @henshin_text_Node.setter
    def henshin_text_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_text_Node__henshin_text_Node", None)
        self.__henshin_text_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_text_EClass"):
                opp_val = getattr(old_value, "henshin_text_EClass", None)
                if opp_val == self:
                    setattr(old_value, "henshin_text_EClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_text_EClass"):
                opp_val = getattr(value, "henshin_text_EClass", None)
                setattr(value, "henshin_text_EClass", self)

    @property
    def henshin_text_Node21(self):
        return self.__henshin_text_Node21

    @henshin_text_Node21.setter
    def henshin_text_Node21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_text_Node__henshin_text_Node21", None)
        self.__henshin_text_Node21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_text_MultiRuleReuseNode"):
                opp_val = getattr(old_value, "henshin_text_MultiRuleReuseNode", None)
                if opp_val == self:
                    setattr(old_value, "henshin_text_MultiRuleReuseNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_text_MultiRuleReuseNode"):
                opp_val = getattr(value, "henshin_text_MultiRuleReuseNode", None)
                setattr(value, "henshin_text_MultiRuleReuseNode", self)

class RuleElement:

    pass
class henshin_text_InjectiveMatching(RuleElement):

    def __init__(self, injectiveMatching: bool):
        self.injectiveMatching = injectiveMatching
        
    @property
    def injectiveMatching(self) -> bool:
        return self.__injectiveMatching

    @injectiveMatching.setter
    def injectiveMatching(self, injectiveMatching: bool):
        self.__injectiveMatching = injectiveMatching

class henshin_text_CheckDangling(RuleElement):

    def __init__(self, checkDangling: bool):
        self.checkDangling = checkDangling
        
    @property
    def checkDangling(self) -> bool:
        return self.__checkDangling

    @checkDangling.setter
    def checkDangling(self, checkDangling: bool):
        self.__checkDangling = checkDangling

class henshin_text_Conditions(RuleElement):

    pass
class henshin_text_Graph(RuleElement):

    pass
class henshin_text_JavaImport(RuleElement):

    def __init__(self, packagename: str):
        self.packagename = packagename
        
    @property
    def packagename(self) -> str:
        return self.__packagename

    @packagename.setter
    def packagename(self, packagename: str):
        self.__packagename = packagename

class henshin_text_RuleElement:

    pass
class henshin_text_Parameter:

    def __init__(self, name: str, henshin_text_Parameter: "henshin_text_ModelElement" = None, henshin_text_Parameter84: "henshin_text_ParameterType" = None, henshin_text_Parameter110: "henshin_text_Call" = None, henshin_text_Parameter151: "henshin_text_ParameterValue" = None):
        self.name = name
        self.henshin_text_Parameter = henshin_text_Parameter
        self.henshin_text_Parameter84 = henshin_text_Parameter84
        self.henshin_text_Parameter110 = henshin_text_Parameter110
        self.henshin_text_Parameter151 = henshin_text_Parameter151
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def henshin_text_Parameter84(self):
        return self.__henshin_text_Parameter84

    @henshin_text_Parameter84.setter
    def henshin_text_Parameter84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_text_Parameter__henshin_text_Parameter84", None)
        self.__henshin_text_Parameter84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_text_ParameterType"):
                opp_val = getattr(old_value, "henshin_text_ParameterType", None)
                if opp_val == self:
                    setattr(old_value, "henshin_text_ParameterType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_text_ParameterType"):
                opp_val = getattr(value, "henshin_text_ParameterType", None)
                setattr(value, "henshin_text_ParameterType", self)

    @property
    def henshin_text_Parameter151(self):
        return self.__henshin_text_Parameter151

    @henshin_text_Parameter151.setter
    def henshin_text_Parameter151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_text_Parameter__henshin_text_Parameter151", None)
        self.__henshin_text_Parameter151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_text_ParameterValue"):
                opp_val = getattr(old_value, "henshin_text_ParameterValue", None)
                if opp_val == self:
                    setattr(old_value, "henshin_text_ParameterValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_text_ParameterValue"):
                opp_val = getattr(value, "henshin_text_ParameterValue", None)
                setattr(value, "henshin_text_ParameterValue", self)

    @property
    def henshin_text_Parameter110(self):
        return self.__henshin_text_Parameter110

    @henshin_text_Parameter110.setter
    def henshin_text_Parameter110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_text_Parameter__henshin_text_Parameter110", None)
        self.__henshin_text_Parameter110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_text_Call109"):
                opp_val = getattr(old_value, "henshin_text_Call109", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_text_Call109"):
                opp_val = getattr(value, "henshin_text_Call109", None)
                if opp_val is None:
                    setattr(value, "henshin_text_Call109", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def henshin_text_Parameter(self):
        return self.__henshin_text_Parameter

    @henshin_text_Parameter.setter
    def henshin_text_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_text_Parameter__henshin_text_Parameter", None)
        self.__henshin_text_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_text_ModelElement6"):
                opp_val = getattr(old_value, "henshin_text_ModelElement6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_text_ModelElement6"):
                opp_val = getattr(value, "henshin_text_ModelElement6", None)
                if opp_val is None:
                    setattr(value, "henshin_text_ModelElement6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class henshin_text_EPackage:

    pass
class henshin_text_ModelElement:

    def __init__(self, name: str, henshin_text_ModelElement: "henshin_text_Model" = None, henshin_text_ModelElement6: set["henshin_text_Parameter"] = None, henshin_text_ModelElement107: "henshin_text_Call" = None):
        self.name = name
        self.henshin_text_ModelElement = henshin_text_ModelElement
        self.henshin_text_ModelElement6 = henshin_text_ModelElement6 if henshin_text_ModelElement6 is not None else set()
        self.henshin_text_ModelElement107 = henshin_text_ModelElement107
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def henshin_text_ModelElement(self):
        return self.__henshin_text_ModelElement

    @henshin_text_ModelElement.setter
    def henshin_text_ModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_text_ModelElement__henshin_text_ModelElement", None)
        self.__henshin_text_ModelElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_text_Model2"):
                opp_val = getattr(old_value, "henshin_text_Model2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_text_Model2"):
                opp_val = getattr(value, "henshin_text_Model2", None)
                if opp_val is None:
                    setattr(value, "henshin_text_Model2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def henshin_text_ModelElement107(self):
        return self.__henshin_text_ModelElement107

    @henshin_text_ModelElement107.setter
    def henshin_text_ModelElement107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_text_ModelElement__henshin_text_ModelElement107", None)
        self.__henshin_text_ModelElement107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_text_Call"):
                opp_val = getattr(old_value, "henshin_text_Call", None)
                if opp_val == self:
                    setattr(old_value, "henshin_text_Call", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_text_Call"):
                opp_val = getattr(value, "henshin_text_Call", None)
                setattr(value, "henshin_text_Call", self)

    @property
    def henshin_text_ModelElement6(self):
        return self.__henshin_text_ModelElement6

    @henshin_text_ModelElement6.setter
    def henshin_text_ModelElement6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_text_ModelElement__henshin_text_ModelElement6", None)
        self.__henshin_text_ModelElement6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "henshin_text_Parameter"):
                    opp_val = getattr(item, "henshin_text_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "henshin_text_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "henshin_text_Parameter"):
                    opp_val = getattr(item, "henshin_text_Parameter", None)
                    
                    setattr(item, "henshin_text_Parameter", self)
                    

class henshin_text_EPackageImport:

    pass
class henshin_text_Model:

    pass