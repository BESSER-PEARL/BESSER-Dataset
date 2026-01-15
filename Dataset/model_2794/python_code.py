from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class HaxeAttributeProperty(Enum):
    default = "default"
    method = "method"
    null = "null"
    dynamic = "dynamic"
class HaxeTarget(Enum):
    neko = "neko"
    cpp = "cpp"
    java = "java"
    flash = "flash"
    cs = "cs"
    js = "js"
class HaxeInfixOperators(Enum):
    PLUS = "PLUS"
    TIMES = "TIMES"
    MINUS = "MINUS"
    DIVISION = "DIVISION"
    REMAINDER = "REMAINDER"
    SHIFT_RIGTH = "SHIFT_RIGTH"
    SHIFT_LEFT = "SHIFT_LEFT"
    SHIFT_ARITH = "SHIFT_ARITH"
    LESS_THAN = "LESS_THAN"
    GREATER_THAN = "GREATER_THAN"
    LESS_EQUALS = "LESS_EQUALS"
    GREATER_EQUALS = "GREATER_EQUALS"
    BITWISE_OR = "BITWISE_OR"
    BITWISE_AND = "BITWISE_AND"
    XOR = "XOR"
    EQ = "EQ"
    NEQ = "NEQ"
    OR = "OR"
    AND = "AND"
    RANGE = "RANGE"
class HaxePrefixOperators(Enum):
    NOT = "NOT"
    MINUS = "MINUS"
    PLUS = "PLUS"
    INCREMENT = "INCREMENT"
    DECREMENT = "DECREMENT"
    ONECOMPLEMENT = "ONECOMPLEMENT"
class HaxeAssignmentOperator(Enum):
    ASSIGN = "ASSIGN"
    PLUS_ASSIGN = "PLUS_ASSIGN"
    MINUS_ASSIGN = "MINUS_ASSIGN"
    DIVISION_ASSIGN = "DIVISION_ASSIGN"
    TIMES_ASSIGN = "TIMES_ASSIGN"
    SHIFT_LEFT_ASSIGN = "SHIFT_LEFT_ASSIGN"
    SHIFT_RIGTH_ASSIGN = "SHIFT_RIGTH_ASSIGN"
    SHIFT_ARITH_ASSIGN = "SHIFT_ARITH_ASSIGN"
    BITWISE_OR_ASSIGN = "BITWISE_OR_ASSIGN"
    BITWISE_AND_ASSIGN = "BITWISE_AND_ASSIGN"
    XOR_ASSIGN = "XOR_ASSIGN"
    REMAINDER_ASSIGN = "REMAINDER_ASSIGN"


############################################
# Definition of Classes
############################################

class HaxeDependencyDeclaration:

    pass
class haxe_HaxeUsingDeclaration(HaxeDependencyDeclaration):

    pass
class haxe_HaxeImportDeclaration(HaxeDependencyDeclaration):

    pass
class HaxeAbstractOperation:

    pass
class HaxeSingleVariableDeclaration:

    pass
class HaxeField:

    pass
class HaxeTypeAccess:

    pass
class haxe_HaxeFunctionTypeAccess(HaxeTypeAccess):

    pass
class HaxeClassifier:

    pass
class haxe_HaxeAbstract(HaxeClassifier):

    pass
class haxe_HaxeEnum(HaxeClassifier):

    pass
class HaxeFieldContainer:

    pass
class HaxeType:

    pass
class haxe_HaxeTypedef(HaxeType):

    pass
class haxe_HaxeTypeParameter(HaxeType):

    pass
class haxe_HaxeConstructor(HaxeField, HaxeAbstractOperation):

    pass
class haxe_HaxeAttribute(HaxeField, HaxeSingleVariableDeclaration):

    def __init__(self, getterProperty: str, setterProperty: str, haxe_HaxeAttribute: "haxe_HaxeClassifier" = None, haxe_HaxeAttribute203: "haxe_HaxeOperation" = None, haxe_HaxeAttribute206: "haxe_HaxeOperation" = None):
        self.getterProperty = getterProperty
        self.setterProperty = setterProperty
        self.haxe_HaxeAttribute = haxe_HaxeAttribute
        self.haxe_HaxeAttribute203 = haxe_HaxeAttribute203
        self.haxe_HaxeAttribute206 = haxe_HaxeAttribute206
        
    @property
    def setterProperty(self) -> str:
        return self.__setterProperty

    @setterProperty.setter
    def setterProperty(self, setterProperty: str):
        self.__setterProperty = setterProperty

    @property
    def getterProperty(self) -> str:
        return self.__getterProperty

    @getterProperty.setter
    def getterProperty(self, getterProperty: str):
        self.__getterProperty = getterProperty

    @property
    def haxe_HaxeAttribute203(self):
        return self.__haxe_HaxeAttribute203

    @haxe_HaxeAttribute203.setter
    def haxe_HaxeAttribute203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeAttribute__haxe_HaxeAttribute203", None)
        self.__haxe_HaxeAttribute203 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "haxe_HaxeOperation204"):
                opp_val = getattr(old_value, "haxe_HaxeOperation204", None)
                if opp_val == self:
                    setattr(old_value, "haxe_HaxeOperation204", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "haxe_HaxeOperation204"):
                opp_val = getattr(value, "haxe_HaxeOperation204", None)
                setattr(value, "haxe_HaxeOperation204", self)

    @property
    def haxe_HaxeAttribute(self):
        return self.__haxe_HaxeAttribute

    @haxe_HaxeAttribute.setter
    def haxe_HaxeAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeAttribute__haxe_HaxeAttribute", None)
        self.__haxe_HaxeAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "haxe_HaxeClassifier169"):
                opp_val = getattr(old_value, "haxe_HaxeClassifier169", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "haxe_HaxeClassifier169"):
                opp_val = getattr(value, "haxe_HaxeClassifier169", None)
                if opp_val is None:
                    setattr(value, "haxe_HaxeClassifier169", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def haxe_HaxeAttribute206(self):
        return self.__haxe_HaxeAttribute206

    @haxe_HaxeAttribute206.setter
    def haxe_HaxeAttribute206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeAttribute__haxe_HaxeAttribute206", None)
        self.__haxe_HaxeAttribute206 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "haxe_HaxeOperation207"):
                opp_val = getattr(old_value, "haxe_HaxeOperation207", None)
                if opp_val == self:
                    setattr(old_value, "haxe_HaxeOperation207", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "haxe_HaxeOperation207"):
                opp_val = getattr(value, "haxe_HaxeOperation207", None)
                setattr(value, "haxe_HaxeOperation207", self)

class HaxeMetadataContainer:

    pass
class haxe_HaxeClassifier(HaxeFieldContainer, HaxeType, HaxeMetadataContainer):

    pass
class HaxeVariableDeclaration:

    pass
class haxe_HaxeEnumConstructor(HaxeField, HaxeVariableDeclaration):

    pass
class haxe_HaxeVariableDeclarationFragment(HaxeVariableDeclaration):

    pass
class HaxePathReferentiable:

    pass
class HaxeAbstractMethodInvocation:

    pass
class HaxePathReference:

    pass
class haxe_HaxeClassifierAccess(HaxePathReference, HaxeTypeAccess):

    pass
class HaxeMethodInvocation:

    pass
class haxe_HaxeSuperConstructorInvocation(HaxeMethodInvocation):

    pass
class HaxeTypedElement:

    pass
class haxe_HaxeVariableDeclarationGroup(HaxeTypedElement):

    pass
class haxe_HaxeOperation(HaxeField, HaxeAbstractOperation, HaxeTypedElement):

    def __init__(self, macro: bool, haxe_HaxeOperation: "haxe_HaxeClassifier" = None, haxe_HaxeOperation204: "haxe_HaxeAttribute" = None, haxe_HaxeOperation207: "haxe_HaxeAttribute" = None):
        self.macro = macro
        self.haxe_HaxeOperation = haxe_HaxeOperation
        self.haxe_HaxeOperation204 = haxe_HaxeOperation204
        self.haxe_HaxeOperation207 = haxe_HaxeOperation207
        
    @property
    def macro(self) -> bool:
        return self.__macro

    @macro.setter
    def macro(self, macro: bool):
        self.__macro = macro

    @property
    def haxe_HaxeOperation204(self):
        return self.__haxe_HaxeOperation204

    @haxe_HaxeOperation204.setter
    def haxe_HaxeOperation204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeOperation__haxe_HaxeOperation204", None)
        self.__haxe_HaxeOperation204 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "haxe_HaxeAttribute203"):
                opp_val = getattr(old_value, "haxe_HaxeAttribute203", None)
                if opp_val == self:
                    setattr(old_value, "haxe_HaxeAttribute203", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "haxe_HaxeAttribute203"):
                opp_val = getattr(value, "haxe_HaxeAttribute203", None)
                setattr(value, "haxe_HaxeAttribute203", self)

    @property
    def haxe_HaxeOperation207(self):
        return self.__haxe_HaxeOperation207

    @haxe_HaxeOperation207.setter
    def haxe_HaxeOperation207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeOperation__haxe_HaxeOperation207", None)
        self.__haxe_HaxeOperation207 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "haxe_HaxeAttribute206"):
                opp_val = getattr(old_value, "haxe_HaxeAttribute206", None)
                if opp_val == self:
                    setattr(old_value, "haxe_HaxeAttribute206", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "haxe_HaxeAttribute206"):
                opp_val = getattr(value, "haxe_HaxeAttribute206", None)
                setattr(value, "haxe_HaxeAttribute206", self)

    @property
    def haxe_HaxeOperation(self):
        return self.__haxe_HaxeOperation

    @haxe_HaxeOperation.setter
    def haxe_HaxeOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeOperation__haxe_HaxeOperation", None)
        self.__haxe_HaxeOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "haxe_HaxeClassifier167"):
                opp_val = getattr(old_value, "haxe_HaxeClassifier167", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "haxe_HaxeClassifier167"):
                opp_val = getattr(value, "haxe_HaxeClassifier167", None)
                if opp_val is None:
                    setattr(value, "haxe_HaxeClassifier167", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class HaxeAbstractFunction:

    pass
class haxe_HaxeAbstractOperation(HaxeAbstractFunction):

    def __init__(self, isInline: bool, overrides: bool, haxe_HaxeAbstractOperation: "haxe_HaxeAbstractMethodInvocation" = None):
        self.isInline = isInline
        self.overrides = overrides
        self.haxe_HaxeAbstractOperation = haxe_HaxeAbstractOperation
        
    @property
    def overrides(self) -> bool:
        return self.__overrides

    @overrides.setter
    def overrides(self, overrides: bool):
        self.__overrides = overrides

    @property
    def isInline(self) -> bool:
        return self.__isInline

    @isInline.setter
    def isInline(self, isInline: bool):
        self.__isInline = isInline

    @property
    def haxe_HaxeAbstractOperation(self):
        return self.__haxe_HaxeAbstractOperation

    @haxe_HaxeAbstractOperation.setter
    def haxe_HaxeAbstractOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeAbstractOperation__haxe_HaxeAbstractOperation", None)
        self.__haxe_HaxeAbstractOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "haxe_HaxeAbstractMethodInvocation"):
                opp_val = getattr(old_value, "haxe_HaxeAbstractMethodInvocation", None)
                if opp_val == self:
                    setattr(old_value, "haxe_HaxeAbstractMethodInvocation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "haxe_HaxeAbstractMethodInvocation"):
                opp_val = getattr(value, "haxe_HaxeAbstractMethodInvocation", None)
                setattr(value, "haxe_HaxeAbstractMethodInvocation", self)

class HaxeConstant:

    pass
class haxe_HaxeNullLiteral(HaxeConstant):

    pass
class haxe_HaxeBooleanLiteral(HaxeConstant):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class haxe_HaxeStringLiteral(HaxeConstant):

    def __init__(self, escapedValue: str):
        self.escapedValue = escapedValue
        
    @property
    def escapedValue(self) -> str:
        return self.__escapedValue

    @escapedValue.setter
    def escapedValue(self, escapedValue: str):
        self.__escapedValue = escapedValue

class haxe_HaxeRegexLiteral(HaxeConstant):

    def __init__(self, pattern: str, options: str):
        self.pattern = pattern
        self.options = options
        
    @property
    def pattern(self) -> str:
        return self.__pattern

    @pattern.setter
    def pattern(self, pattern: str):
        self.__pattern = pattern

    @property
    def options(self) -> str:
        return self.__options

    @options.setter
    def options(self, options: str):
        self.__options = options

class haxe_HaxeIdentifierLiteral(HaxeConstant):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class haxe_HaxeNumberLiteral(HaxeConstant):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class HaxeBinaryExpression:

    pass
class haxe_HaxeAssignment(HaxeBinaryExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class haxe_HaxeInfixExpression(HaxeBinaryExpression):

    def __init__(self, operator: str, haxe_HaxeInfixExpression: set["haxe_HaxeExpression"] = None):
        self.operator = operator
        self.haxe_HaxeInfixExpression = haxe_HaxeInfixExpression if haxe_HaxeInfixExpression is not None else set()
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def haxe_HaxeInfixExpression(self):
        return self.__haxe_HaxeInfixExpression

    @haxe_HaxeInfixExpression.setter
    def haxe_HaxeInfixExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeInfixExpression__haxe_HaxeInfixExpression", None)
        self.__haxe_HaxeInfixExpression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "haxe_HaxeExpression46"):
                    opp_val = getattr(item, "haxe_HaxeExpression46", None)
                    
                    if opp_val == self:
                        setattr(item, "haxe_HaxeExpression46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "haxe_HaxeExpression46"):
                    opp_val = getattr(item, "haxe_HaxeExpression46", None)
                    
                    setattr(item, "haxe_HaxeExpression46", self)
                    

class HaxeUnaryExpression:

    pass
class haxe_HaxePrefixExpression(HaxeUnaryExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class HaxeExpressionStatement:

    pass
class haxe_HaxeThrowExpression(HaxeExpressionStatement):

    pass
class haxe_HaxeReturn(HaxeExpressionStatement):

    pass
class haxe_HaxePostfixExpression(HaxeUnaryExpression):

    def __init__(self, isIncrement: bool):
        self.isIncrement = isIncrement
        
    @property
    def isIncrement(self) -> bool:
        return self.__isIncrement

    @isIncrement.setter
    def isIncrement(self, isIncrement: bool):
        self.__isIncrement = isIncrement

class HaxeConditionalExpression:

    pass
class haxe_HaxeTernaryExpression(HaxeConditionalExpression):

    pass
class haxe_HaxeIfStatement(HaxeConditionalExpression):

    pass
class haxe_HaxeSingleVariableDeclaration(HaxeVariableDeclaration, HaxeTypedElement):

    def __init__(self, isOptional: bool, haxe_HaxeSingleVariableDeclaration: "haxe_HaxeForStatement" = None, haxe_HaxeSingleVariableDeclaration41: "haxe_HaxeInExpression" = None, HaxeSingleVariableDeclaration: "haxe_HaxeCatchClause" = None, exception: "haxe_HaxeCatchClause" = None, haxe_HaxeSingleVariableDeclaration209: "haxe_HaxeAbstractFunction" = None, haxe_HaxeSingleVariableDeclaration221: "haxe_HaxeEnumConstructor" = None):
        self.isOptional = isOptional
        self.haxe_HaxeSingleVariableDeclaration = haxe_HaxeSingleVariableDeclaration
        self.haxe_HaxeSingleVariableDeclaration41 = haxe_HaxeSingleVariableDeclaration41
        self.HaxeSingleVariableDeclaration = HaxeSingleVariableDeclaration
        self.exception = exception
        self.haxe_HaxeSingleVariableDeclaration209 = haxe_HaxeSingleVariableDeclaration209
        self.haxe_HaxeSingleVariableDeclaration221 = haxe_HaxeSingleVariableDeclaration221
        
    @property
    def isOptional(self) -> bool:
        return self.__isOptional

    @isOptional.setter
    def isOptional(self, isOptional: bool):
        self.__isOptional = isOptional

    @property
    def haxe_HaxeSingleVariableDeclaration(self):
        return self.__haxe_HaxeSingleVariableDeclaration

    @haxe_HaxeSingleVariableDeclaration.setter
    def haxe_HaxeSingleVariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeSingleVariableDeclaration__haxe_HaxeSingleVariableDeclaration", None)
        self.__haxe_HaxeSingleVariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "haxe_HaxeForStatement"):
                opp_val = getattr(old_value, "haxe_HaxeForStatement", None)
                if opp_val == self:
                    setattr(old_value, "haxe_HaxeForStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "haxe_HaxeForStatement"):
                opp_val = getattr(value, "haxe_HaxeForStatement", None)
                setattr(value, "haxe_HaxeForStatement", self)

    @property
    def exception(self):
        return self.__exception

    @exception.setter
    def exception(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeSingleVariableDeclaration__exception", None)
        self.__exception = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HaxeCatchClause"):
                opp_val = getattr(old_value, "HaxeCatchClause", None)
                if opp_val == self:
                    setattr(old_value, "HaxeCatchClause", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HaxeCatchClause"):
                opp_val = getattr(value, "HaxeCatchClause", None)
                setattr(value, "HaxeCatchClause", self)

    @property
    def haxe_HaxeSingleVariableDeclaration221(self):
        return self.__haxe_HaxeSingleVariableDeclaration221

    @haxe_HaxeSingleVariableDeclaration221.setter
    def haxe_HaxeSingleVariableDeclaration221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeSingleVariableDeclaration__haxe_HaxeSingleVariableDeclaration221", None)
        self.__haxe_HaxeSingleVariableDeclaration221 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "haxe_HaxeEnumConstructor220"):
                opp_val = getattr(old_value, "haxe_HaxeEnumConstructor220", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "haxe_HaxeEnumConstructor220"):
                opp_val = getattr(value, "haxe_HaxeEnumConstructor220", None)
                if opp_val is None:
                    setattr(value, "haxe_HaxeEnumConstructor220", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def haxe_HaxeSingleVariableDeclaration41(self):
        return self.__haxe_HaxeSingleVariableDeclaration41

    @haxe_HaxeSingleVariableDeclaration41.setter
    def haxe_HaxeSingleVariableDeclaration41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeSingleVariableDeclaration__haxe_HaxeSingleVariableDeclaration41", None)
        self.__haxe_HaxeSingleVariableDeclaration41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "haxe_HaxeInExpression"):
                opp_val = getattr(old_value, "haxe_HaxeInExpression", None)
                if opp_val == self:
                    setattr(old_value, "haxe_HaxeInExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "haxe_HaxeInExpression"):
                opp_val = getattr(value, "haxe_HaxeInExpression", None)
                setattr(value, "haxe_HaxeInExpression", self)

    @property
    def haxe_HaxeSingleVariableDeclaration209(self):
        return self.__haxe_HaxeSingleVariableDeclaration209

    @haxe_HaxeSingleVariableDeclaration209.setter
    def haxe_HaxeSingleVariableDeclaration209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeSingleVariableDeclaration__haxe_HaxeSingleVariableDeclaration209", None)
        self.__haxe_HaxeSingleVariableDeclaration209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "haxe_HaxeAbstractFunction"):
                opp_val = getattr(old_value, "haxe_HaxeAbstractFunction", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "haxe_HaxeAbstractFunction"):
                opp_val = getattr(value, "haxe_HaxeAbstractFunction", None)
                if opp_val is None:
                    setattr(value, "haxe_HaxeAbstractFunction", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def HaxeSingleVariableDeclaration(self):
        return self.__HaxeSingleVariableDeclaration

    @HaxeSingleVariableDeclaration.setter
    def HaxeSingleVariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeSingleVariableDeclaration__HaxeSingleVariableDeclaration", None)
        self.__HaxeSingleVariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "catchClause"):
                opp_val = getattr(old_value, "catchClause", None)
                if opp_val == self:
                    setattr(old_value, "catchClause", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "catchClause"):
                opp_val = getattr(value, "catchClause", None)
                setattr(value, "catchClause", self)

class HaxeLoopStatement:

    pass
class haxe_HaxeDoWhileStatement(HaxeLoopStatement):

    pass
class haxe_HaxeWhileStatement(HaxeLoopStatement):

    pass
class haxe_HaxeForStatement(HaxeLoopStatement):

    pass
class haxe_HaxePackage(HaxePathReferentiable):

    pass
class HaxeNamedElement:

    pass
class haxe_HaxeFieldDeclaration(HaxeTypedElement, HaxeNamedElement):

    pass
class haxe_HaxeVariableDeclaration(HaxeNamedElement):

    pass
class HaxeExpression:

    pass
class haxe_HaxeArrayAccess(HaxeExpression):

    pass
class haxe_HaxeMethodInvocation(HaxeExpression, HaxeAbstractMethodInvocation):

    pass
class haxe_HaxeTypeCheckExpression(HaxeExpression):

    pass
class haxe_HaxeUnsafeCastExpression(HaxeExpression):

    pass
class haxe_HaxeArrayCreation(HaxeExpression):

    pass
class haxe_HaxeUnaryExpression(HaxeExpression):

    pass
class haxe_HaxeTypeAccess(HaxeExpression):

    pass
class haxe_HaxeTryExpression(HaxeExpression):

    pass
class haxe_HaxeExpressionStatement(HaxeExpression):

    pass
class haxe_HaxeSuperMethodInvocation(HaxeExpression, HaxeAbstractMethodInvocation):

    pass
class haxe_HaxeSwitch(HaxeExpression):

    pass
class haxe_HaxeArrayInitializer(HaxeExpression):

    pass
class haxe_HaxeBinaryExpression(HaxeExpression):

    pass
class haxe_HaxeVariableDeclarationExpression(HaxeExpression):

    pass
class haxe_HaxeCastingExpression(HaxeExpression):

    pass
class haxe_HaxeConstant(HaxeExpression):

    pass
class haxe_HaxeObjectDeclaration(HaxeExpression):

    pass
class haxe_HaxeParenthizedExpression(HaxeExpression):

    pass
class haxe_HaxeFieldAccess(HaxeExpression):

    pass
class haxe_HaxeSingleVariableAccess(HaxeExpression):

    pass
class haxe_HaxeFunctionExpression(HaxeAbstractFunction, HaxeExpression):

    pass
class haxe_HaxeEmptyStatement(HaxeExpression):

    pass
class haxe_HaxeBreak(HaxeExpression):

    pass
class haxe_HaxeCatchClause(HaxeExpression):

    pass
class haxe_HaxeInExpression(HaxeExpression):

    pass
class haxe_HaxeCallExpression(HaxeExpression):

    pass
class haxe_HaxeBlock(HaxeExpression):

    def __init__(self, haxe_HaxeBlock: set["haxe_HaxeExpression"] = None):
        self.haxe_HaxeBlock = haxe_HaxeBlock if haxe_HaxeBlock is not None else set()
        
    @property
    def haxe_HaxeBlock(self):
        return self.__haxe_HaxeBlock

    @haxe_HaxeBlock.setter
    def haxe_HaxeBlock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeBlock__haxe_HaxeBlock", None)
        self.__haxe_HaxeBlock = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "haxe_HaxeExpression29"):
                    opp_val = getattr(item, "haxe_HaxeExpression29", None)
                    
                    if opp_val == self:
                        setattr(item, "haxe_HaxeExpression29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "haxe_HaxeExpression29"):
                    opp_val = getattr(item, "haxe_HaxeExpression29", None)
                    
                    setattr(item, "haxe_HaxeExpression29", self)
                    

    def isEmpty(self) -> bool:
        # TODO: Implement isEmpty method
        pass

class haxe_HaxeConditionalExpression(HaxeExpression):

    pass
class haxe_HaxeContinue(HaxeExpression):

    pass
class haxe_HaxeMetadata(HaxeExpression, HaxeNamedElement):

    def __init__(self, compilerMetadata: bool, HaxeMetadata: "haxe_HaxeMetadataContainer" = None, metadata: "haxe_HaxeMetadataContainer" = None, haxe_HaxeMetadata: set["haxe_HaxeExpression"] = None):
        self.compilerMetadata = compilerMetadata
        self.HaxeMetadata = HaxeMetadata
        self.metadata = metadata
        self.haxe_HaxeMetadata = haxe_HaxeMetadata if haxe_HaxeMetadata is not None else set()
        
    @property
    def compilerMetadata(self) -> bool:
        return self.__compilerMetadata

    @compilerMetadata.setter
    def compilerMetadata(self, compilerMetadata: bool):
        self.__compilerMetadata = compilerMetadata

    @property
    def haxe_HaxeMetadata(self):
        return self.__haxe_HaxeMetadata

    @haxe_HaxeMetadata.setter
    def haxe_HaxeMetadata(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeMetadata__haxe_HaxeMetadata", None)
        self.__haxe_HaxeMetadata = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "haxe_HaxeExpression227"):
                    opp_val = getattr(item, "haxe_HaxeExpression227", None)
                    
                    if opp_val == self:
                        setattr(item, "haxe_HaxeExpression227", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "haxe_HaxeExpression227"):
                    opp_val = getattr(item, "haxe_HaxeExpression227", None)
                    
                    setattr(item, "haxe_HaxeExpression227", self)
                    

    @property
    def metadata(self):
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeMetadata__metadata", None)
        self.__metadata = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HaxeMetadataContainer"):
                opp_val = getattr(old_value, "HaxeMetadataContainer", None)
                if opp_val == self:
                    setattr(old_value, "HaxeMetadataContainer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HaxeMetadataContainer"):
                opp_val = getattr(value, "HaxeMetadataContainer", None)
                setattr(value, "HaxeMetadataContainer", self)

    @property
    def HaxeMetadata(self):
        return self.__HaxeMetadata

    @HaxeMetadata.setter
    def HaxeMetadata(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeMetadata__HaxeMetadata", None)
        self.__HaxeMetadata = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usedIn"):
                opp_val = getattr(old_value, "usedIn", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usedIn"):
                opp_val = getattr(value, "usedIn", None)
                if opp_val is None:
                    setattr(value, "usedIn", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class haxe_HaxeThisExpression(HaxeExpression):

    pass
class haxe_HaxePackageAccess(HaxePathReference, HaxeExpression):

    pass
class haxe_HaxeCase(HaxeExpression):

    pass
class haxe_HaxeLoopStatement(HaxeExpression):

    pass
class haxe_HaxeField(HaxeMetadataContainer, HaxeNamedElement):

    def __init__(self, isStatic: bool, isPrivate: bool, HaxeField: "haxe_HaxeFieldContainer" = None, haxeFields: "haxe_HaxeFieldContainer" = None, haxe_HaxeField: "haxe_HaxeImportDeclaration" = None, haxe_HaxeField224: "haxe_HaxeUsingDeclaration" = None):
        self.isStatic = isStatic
        self.isPrivate = isPrivate
        self.HaxeField = HaxeField
        self.haxeFields = haxeFields
        self.haxe_HaxeField = haxe_HaxeField
        self.haxe_HaxeField224 = haxe_HaxeField224
        
    @property
    def isPrivate(self) -> bool:
        return self.__isPrivate

    @isPrivate.setter
    def isPrivate(self, isPrivate: bool):
        self.__isPrivate = isPrivate

    @property
    def isStatic(self) -> bool:
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: bool):
        self.__isStatic = isStatic

    @property
    def HaxeField(self):
        return self.__HaxeField

    @HaxeField.setter
    def HaxeField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeField__HaxeField", None)
        self.__HaxeField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fieldContainer"):
                opp_val = getattr(old_value, "fieldContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fieldContainer"):
                opp_val = getattr(value, "fieldContainer", None)
                if opp_val is None:
                    setattr(value, "fieldContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def haxe_HaxeField(self):
        return self.__haxe_HaxeField

    @haxe_HaxeField.setter
    def haxe_HaxeField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeField__haxe_HaxeField", None)
        self.__haxe_HaxeField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "haxe_HaxeImportDeclaration"):
                opp_val = getattr(old_value, "haxe_HaxeImportDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "haxe_HaxeImportDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "haxe_HaxeImportDeclaration"):
                opp_val = getattr(value, "haxe_HaxeImportDeclaration", None)
                setattr(value, "haxe_HaxeImportDeclaration", self)

    @property
    def haxe_HaxeField224(self):
        return self.__haxe_HaxeField224

    @haxe_HaxeField224.setter
    def haxe_HaxeField224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeField__haxe_HaxeField224", None)
        self.__haxe_HaxeField224 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "haxe_HaxeUsingDeclaration"):
                opp_val = getattr(old_value, "haxe_HaxeUsingDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "haxe_HaxeUsingDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "haxe_HaxeUsingDeclaration"):
                opp_val = getattr(value, "haxe_HaxeUsingDeclaration", None)
                setattr(value, "haxe_HaxeUsingDeclaration", self)

    @property
    def haxeFields(self):
        return self.__haxeFields

    @haxeFields.setter
    def haxeFields(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeField__haxeFields", None)
        self.__haxeFields = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HaxeFieldContainer"):
                opp_val = getattr(old_value, "HaxeFieldContainer", None)
                if opp_val == self:
                    setattr(old_value, "HaxeFieldContainer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HaxeFieldContainer"):
                opp_val = getattr(value, "HaxeFieldContainer", None)
                setattr(value, "HaxeFieldContainer", self)

class HaxeASTNode:

    pass
class haxe_HaxeTagElement(HaxeASTNode):

    def __init__(self, tagName: str, haxe_HaxeTagElement: "haxe_HaxeHaxedocComment" = None, haxe_HaxeTagElement11: set["haxe_HaxeASTNode"] = None):
        self.tagName = tagName
        self.haxe_HaxeTagElement = haxe_HaxeTagElement
        self.haxe_HaxeTagElement11 = haxe_HaxeTagElement11 if haxe_HaxeTagElement11 is not None else set()
        
    @property
    def tagName(self) -> str:
        return self.__tagName

    @tagName.setter
    def tagName(self, tagName: str):
        self.__tagName = tagName

    @property
    def haxe_HaxeTagElement(self):
        return self.__haxe_HaxeTagElement

    @haxe_HaxeTagElement.setter
    def haxe_HaxeTagElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeTagElement__haxe_HaxeTagElement", None)
        self.__haxe_HaxeTagElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "haxe_HaxeHaxedocComment"):
                opp_val = getattr(old_value, "haxe_HaxeHaxedocComment", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "haxe_HaxeHaxedocComment"):
                opp_val = getattr(value, "haxe_HaxeHaxedocComment", None)
                if opp_val is None:
                    setattr(value, "haxe_HaxeHaxedocComment", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def haxe_HaxeTagElement11(self):
        return self.__haxe_HaxeTagElement11

    @haxe_HaxeTagElement11.setter
    def haxe_HaxeTagElement11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeTagElement__haxe_HaxeTagElement11", None)
        self.__haxe_HaxeTagElement11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "haxe_HaxeASTNode12"):
                    opp_val = getattr(item, "haxe_HaxeASTNode12", None)
                    
                    if opp_val == self:
                        setattr(item, "haxe_HaxeASTNode12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "haxe_HaxeASTNode12"):
                    opp_val = getattr(item, "haxe_HaxeASTNode12", None)
                    
                    setattr(item, "haxe_HaxeASTNode12", self)
                    

class haxe_HaxeExpression(HaxeASTNode):

    pass
class haxe_HaxeType(HaxeASTNode, HaxePathReferentiable):

    def __init__(self, private: bool, extern: bool, HaxeType: "haxe_HaxeModule" = None, haxe_HaxeType: "haxe_HaxePackage" = None, theElements: "haxe_HaxeModule" = None, haxe_HaxeType157: set["haxe_HaxeComment"] = None, haxe_HaxeType160: set["haxe_HaxeComment"] = None, haxe_HaxeType163: set["haxe_HaxeTypeParameter"] = None):
        self.private = private
        self.extern = extern
        self.HaxeType = HaxeType
        self.haxe_HaxeType = haxe_HaxeType
        self.theElements = theElements
        self.haxe_HaxeType157 = haxe_HaxeType157 if haxe_HaxeType157 is not None else set()
        self.haxe_HaxeType160 = haxe_HaxeType160 if haxe_HaxeType160 is not None else set()
        self.haxe_HaxeType163 = haxe_HaxeType163 if haxe_HaxeType163 is not None else set()
        
    @property
    def private(self) -> bool:
        return self.__private

    @private.setter
    def private(self, private: bool):
        self.__private = private

    @property
    def extern(self) -> bool:
        return self.__extern

    @extern.setter
    def extern(self, extern: bool):
        self.__extern = extern

    @property
    def haxe_HaxeType160(self):
        return self.__haxe_HaxeType160

    @haxe_HaxeType160.setter
    def haxe_HaxeType160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeType__haxe_HaxeType160", None)
        self.__haxe_HaxeType160 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "haxe_HaxeComment161"):
                    opp_val = getattr(item, "haxe_HaxeComment161", None)
                    
                    if opp_val == self:
                        setattr(item, "haxe_HaxeComment161", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "haxe_HaxeComment161"):
                    opp_val = getattr(item, "haxe_HaxeComment161", None)
                    
                    setattr(item, "haxe_HaxeComment161", self)
                    

    @property
    def haxe_HaxeType(self):
        return self.__haxe_HaxeType

    @haxe_HaxeType.setter
    def haxe_HaxeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeType__haxe_HaxeType", None)
        self.__haxe_HaxeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "haxe_HaxePackage145"):
                opp_val = getattr(old_value, "haxe_HaxePackage145", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "haxe_HaxePackage145"):
                opp_val = getattr(value, "haxe_HaxePackage145", None)
                if opp_val is None:
                    setattr(value, "haxe_HaxePackage145", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def haxe_HaxeType157(self):
        return self.__haxe_HaxeType157

    @haxe_HaxeType157.setter
    def haxe_HaxeType157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeType__haxe_HaxeType157", None)
        self.__haxe_HaxeType157 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "haxe_HaxeComment158"):
                    opp_val = getattr(item, "haxe_HaxeComment158", None)
                    
                    if opp_val == self:
                        setattr(item, "haxe_HaxeComment158", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "haxe_HaxeComment158"):
                    opp_val = getattr(item, "haxe_HaxeComment158", None)
                    
                    setattr(item, "haxe_HaxeComment158", self)
                    

    @property
    def theElements(self):
        return self.__theElements

    @theElements.setter
    def theElements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeType__theElements", None)
        self.__theElements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HaxeModule"):
                opp_val = getattr(old_value, "HaxeModule", None)
                if opp_val == self:
                    setattr(old_value, "HaxeModule", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HaxeModule"):
                opp_val = getattr(value, "HaxeModule", None)
                setattr(value, "HaxeModule", self)

    @property
    def haxe_HaxeType163(self):
        return self.__haxe_HaxeType163

    @haxe_HaxeType163.setter
    def haxe_HaxeType163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeType__haxe_HaxeType163", None)
        self.__haxe_HaxeType163 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "haxe_HaxeTypeParameter"):
                    opp_val = getattr(item, "haxe_HaxeTypeParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "haxe_HaxeTypeParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "haxe_HaxeTypeParameter"):
                    opp_val = getattr(item, "haxe_HaxeTypeParameter", None)
                    
                    setattr(item, "haxe_HaxeTypeParameter", self)
                    

    @property
    def HaxeType(self):
        return self.__HaxeType

    @HaxeType.setter
    def HaxeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeType__HaxeType", None)
        self.__HaxeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containerModule"):
                opp_val = getattr(old_value, "containerModule", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containerModule"):
                opp_val = getattr(value, "containerModule", None)
                if opp_val is None:
                    setattr(value, "containerModule", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class haxe_HaxeDependencyDeclaration(HaxePathReference, HaxeASTNode):

    pass
class haxe_HaxeTextElement(HaxeASTNode):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class haxe_HaxeAbstractFunction(HaxeASTNode):

    pass
class haxe_HaxeAbstractMethodInvocation(HaxeASTNode):

    pass
class haxe_HaxeNamedElement(HaxeASTNode):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class haxe_HaxeComment(HaxeASTNode):

    def __init__(self, enclosedByParent: bool, prefixOfParent: bool, content: str, lineComment: bool, haxe_HaxeComment: "haxe_HaxeASTNode" = None, haxe_HaxeComment148: "haxe_HaxeModule" = None, haxe_HaxeComment158: "haxe_HaxeType" = None, haxe_HaxeComment161: "haxe_HaxeType" = None):
        self.enclosedByParent = enclosedByParent
        self.prefixOfParent = prefixOfParent
        self.content = content
        self.lineComment = lineComment
        self.haxe_HaxeComment = haxe_HaxeComment
        self.haxe_HaxeComment148 = haxe_HaxeComment148
        self.haxe_HaxeComment158 = haxe_HaxeComment158
        self.haxe_HaxeComment161 = haxe_HaxeComment161
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def lineComment(self) -> bool:
        return self.__lineComment

    @lineComment.setter
    def lineComment(self, lineComment: bool):
        self.__lineComment = lineComment

    @property
    def enclosedByParent(self) -> bool:
        return self.__enclosedByParent

    @enclosedByParent.setter
    def enclosedByParent(self, enclosedByParent: bool):
        self.__enclosedByParent = enclosedByParent

    @property
    def prefixOfParent(self) -> bool:
        return self.__prefixOfParent

    @prefixOfParent.setter
    def prefixOfParent(self, prefixOfParent: bool):
        self.__prefixOfParent = prefixOfParent

    @property
    def haxe_HaxeComment148(self):
        return self.__haxe_HaxeComment148

    @haxe_HaxeComment148.setter
    def haxe_HaxeComment148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeComment__haxe_HaxeComment148", None)
        self.__haxe_HaxeComment148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "haxe_HaxeModule147"):
                opp_val = getattr(old_value, "haxe_HaxeModule147", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "haxe_HaxeModule147"):
                opp_val = getattr(value, "haxe_HaxeModule147", None)
                if opp_val is None:
                    setattr(value, "haxe_HaxeModule147", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def haxe_HaxeComment158(self):
        return self.__haxe_HaxeComment158

    @haxe_HaxeComment158.setter
    def haxe_HaxeComment158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeComment__haxe_HaxeComment158", None)
        self.__haxe_HaxeComment158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "haxe_HaxeType157"):
                opp_val = getattr(old_value, "haxe_HaxeType157", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "haxe_HaxeType157"):
                opp_val = getattr(value, "haxe_HaxeType157", None)
                if opp_val is None:
                    setattr(value, "haxe_HaxeType157", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def haxe_HaxeComment(self):
        return self.__haxe_HaxeComment

    @haxe_HaxeComment.setter
    def haxe_HaxeComment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeComment__haxe_HaxeComment", None)
        self.__haxe_HaxeComment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "haxe_HaxeASTNode"):
                opp_val = getattr(old_value, "haxe_HaxeASTNode", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "haxe_HaxeASTNode"):
                opp_val = getattr(value, "haxe_HaxeASTNode", None)
                if opp_val is None:
                    setattr(value, "haxe_HaxeASTNode", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def haxe_HaxeComment161(self):
        return self.__haxe_HaxeComment161

    @haxe_HaxeComment161.setter
    def haxe_HaxeComment161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeComment__haxe_HaxeComment161", None)
        self.__haxe_HaxeComment161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "haxe_HaxeType160"):
                opp_val = getattr(old_value, "haxe_HaxeType160", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "haxe_HaxeType160"):
                opp_val = getattr(value, "haxe_HaxeType160", None)
                if opp_val is None:
                    setattr(value, "haxe_HaxeType160", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class HaxeModelElement:

    pass
class haxe_HaxeTypedElement(HaxeModelElement):

    pass
class haxe_HaxeMetadataContainer(HaxeModelElement):

    pass
class haxe_HaxeFieldContainer(HaxeModelElement):

    pass
class haxe_HaxePathReference(HaxeModelElement):

    pass
class haxe_HaxeASTNode(HaxeModelElement):

    pass
class HaxeComment:

    pass
class haxe_HaxeHaxedocComment(HaxeComment):

    pass
class haxe_HaxeModel:

    def __init__(self, target: str, name: str, sourceFolder: str, targetFolder: str, haxe_HaxeModel: "haxe_HaxeClass" = None, haxe_HaxeModel2: set["haxe_HaxePathReferentiable"] = None, haxe_HaxeModel4: set["haxe_HaxePathReferentiable"] = None, haxe_HaxeModel7: set["haxe_HaxeModule"] = None):
        self.target = target
        self.name = name
        self.sourceFolder = sourceFolder
        self.targetFolder = targetFolder
        self.haxe_HaxeModel = haxe_HaxeModel
        self.haxe_HaxeModel2 = haxe_HaxeModel2 if haxe_HaxeModel2 is not None else set()
        self.haxe_HaxeModel4 = haxe_HaxeModel4 if haxe_HaxeModel4 is not None else set()
        self.haxe_HaxeModel7 = haxe_HaxeModel7 if haxe_HaxeModel7 is not None else set()
        
    @property
    def sourceFolder(self) -> str:
        return self.__sourceFolder

    @sourceFolder.setter
    def sourceFolder(self, sourceFolder: str):
        self.__sourceFolder = sourceFolder

    @property
    def target(self) -> str:
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target

    @property
    def targetFolder(self) -> str:
        return self.__targetFolder

    @targetFolder.setter
    def targetFolder(self, targetFolder: str):
        self.__targetFolder = targetFolder

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def haxe_HaxeModel7(self):
        return self.__haxe_HaxeModel7

    @haxe_HaxeModel7.setter
    def haxe_HaxeModel7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeModel__haxe_HaxeModel7", None)
        self.__haxe_HaxeModel7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "haxe_HaxeModule"):
                    opp_val = getattr(item, "haxe_HaxeModule", None)
                    
                    if opp_val == self:
                        setattr(item, "haxe_HaxeModule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "haxe_HaxeModule"):
                    opp_val = getattr(item, "haxe_HaxeModule", None)
                    
                    setattr(item, "haxe_HaxeModule", self)
                    

    @property
    def haxe_HaxeModel2(self):
        return self.__haxe_HaxeModel2

    @haxe_HaxeModel2.setter
    def haxe_HaxeModel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeModel__haxe_HaxeModel2", None)
        self.__haxe_HaxeModel2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "haxe_HaxePathReferentiable"):
                    opp_val = getattr(item, "haxe_HaxePathReferentiable", None)
                    
                    if opp_val == self:
                        setattr(item, "haxe_HaxePathReferentiable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "haxe_HaxePathReferentiable"):
                    opp_val = getattr(item, "haxe_HaxePathReferentiable", None)
                    
                    setattr(item, "haxe_HaxePathReferentiable", self)
                    

    @property
    def haxe_HaxeModel4(self):
        return self.__haxe_HaxeModel4

    @haxe_HaxeModel4.setter
    def haxe_HaxeModel4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeModel__haxe_HaxeModel4", None)
        self.__haxe_HaxeModel4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "haxe_HaxePathReferentiable5"):
                    opp_val = getattr(item, "haxe_HaxePathReferentiable5", None)
                    
                    if opp_val == self:
                        setattr(item, "haxe_HaxePathReferentiable5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "haxe_HaxePathReferentiable5"):
                    opp_val = getattr(item, "haxe_HaxePathReferentiable5", None)
                    
                    setattr(item, "haxe_HaxePathReferentiable5", self)
                    

    @property
    def haxe_HaxeModel(self):
        return self.__haxe_HaxeModel

    @haxe_HaxeModel.setter
    def haxe_HaxeModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeModel__haxe_HaxeModel", None)
        self.__haxe_HaxeModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "haxe_HaxeClass"):
                opp_val = getattr(old_value, "haxe_HaxeClass", None)
                if opp_val == self:
                    setattr(old_value, "haxe_HaxeClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "haxe_HaxeClass"):
                opp_val = getattr(value, "haxe_HaxeClass", None)
                setattr(value, "haxe_HaxeClass", self)

class haxe_HaxeModelElement(ABC):

    pass
class haxe_HaxeModule(HaxeNamedElement):

    pass
class haxe_HaxePathReferentiable(HaxeNamedElement):

    pass
class haxe_HaxeClass(HaxeClassifier):

    def __init__(self, isInterface: bool, haxe_HaxeClass: "haxe_HaxeModel" = None, haxe_HaxeClass185: "haxe_HaxeClassifierAccess" = None, haxe_HaxeClass188: set["haxe_HaxeClassifierAccess"] = None, haxe_HaxeClass218: "haxe_HaxeConstructor" = None):
        self.isInterface = isInterface
        self.haxe_HaxeClass = haxe_HaxeClass
        self.haxe_HaxeClass185 = haxe_HaxeClass185
        self.haxe_HaxeClass188 = haxe_HaxeClass188 if haxe_HaxeClass188 is not None else set()
        self.haxe_HaxeClass218 = haxe_HaxeClass218
        
    @property
    def isInterface(self) -> bool:
        return self.__isInterface

    @isInterface.setter
    def isInterface(self, isInterface: bool):
        self.__isInterface = isInterface

    @property
    def haxe_HaxeClass188(self):
        return self.__haxe_HaxeClass188

    @haxe_HaxeClass188.setter
    def haxe_HaxeClass188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeClass__haxe_HaxeClass188", None)
        self.__haxe_HaxeClass188 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "haxe_HaxeClassifierAccess189"):
                    opp_val = getattr(item, "haxe_HaxeClassifierAccess189", None)
                    
                    if opp_val == self:
                        setattr(item, "haxe_HaxeClassifierAccess189", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "haxe_HaxeClassifierAccess189"):
                    opp_val = getattr(item, "haxe_HaxeClassifierAccess189", None)
                    
                    setattr(item, "haxe_HaxeClassifierAccess189", self)
                    

    @property
    def haxe_HaxeClass(self):
        return self.__haxe_HaxeClass

    @haxe_HaxeClass.setter
    def haxe_HaxeClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeClass__haxe_HaxeClass", None)
        self.__haxe_HaxeClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "haxe_HaxeModel"):
                opp_val = getattr(old_value, "haxe_HaxeModel", None)
                if opp_val == self:
                    setattr(old_value, "haxe_HaxeModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "haxe_HaxeModel"):
                opp_val = getattr(value, "haxe_HaxeModel", None)
                setattr(value, "haxe_HaxeModel", self)

    @property
    def haxe_HaxeClass218(self):
        return self.__haxe_HaxeClass218

    @haxe_HaxeClass218.setter
    def haxe_HaxeClass218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeClass__haxe_HaxeClass218", None)
        self.__haxe_HaxeClass218 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "haxe_HaxeConstructor217"):
                opp_val = getattr(old_value, "haxe_HaxeConstructor217", None)
                if opp_val == self:
                    setattr(old_value, "haxe_HaxeConstructor217", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "haxe_HaxeConstructor217"):
                opp_val = getattr(value, "haxe_HaxeConstructor217", None)
                setattr(value, "haxe_HaxeConstructor217", self)

    @property
    def haxe_HaxeClass185(self):
        return self.__haxe_HaxeClass185

    @haxe_HaxeClass185.setter
    def haxe_HaxeClass185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_haxe_HaxeClass__haxe_HaxeClass185", None)
        self.__haxe_HaxeClass185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "haxe_HaxeClassifierAccess186"):
                opp_val = getattr(old_value, "haxe_HaxeClassifierAccess186", None)
                if opp_val == self:
                    setattr(old_value, "haxe_HaxeClassifierAccess186", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "haxe_HaxeClassifierAccess186"):
                opp_val = getattr(value, "haxe_HaxeClassifierAccess186", None)
                setattr(value, "haxe_HaxeClassifierAccess186", self)
