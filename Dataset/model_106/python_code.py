from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AssignmentOperatorKind(Enum):
    right_shift_signed_assign = "right_shift_signed_assign"
    bit_xor_assign = "bit_xor_assign"
    times_assign = "times_assign"
    divide_assign = "divide_assign"
    minus_assign = "minus_assign"
    bit_or_assign = "bit_or_assign"
    plus_assign = "plus_assign"
    assign = "assign"
    right_shift_unsigned_assign = "right_shift_unsigned_assign"
    remainder_assign = "remainder_assign"
    bit_and_assign = "bit_and_assign"
    left_shift_assign = "left_shift_assign"
class InfixExpressionOperatorKind(Enum):
    greater_equals = "greater_equals"
    or = "or"
    right_shift_signed = "right_shift_signed"
    minus = "minus"
    xor = "xor"
    less_equals = "less_equals"
    equals = "equals"
    not_equals = "not_equals"
    and = "and"
    plus = "plus"
    greater = "greater"
    conditional_or = "conditional_or"
    remainder = "remainder"
    less = "less"
    left_shift = "left_shift"
    right_shift_unsigned = "right_shift_unsigned"
    conditional_and = "conditional_and"
    times = "times"
    divide = "divide"
class Modifiers(Enum):
    final = "final"
    interface = "interface"
    native = "native"
    private = "private"
    protected = "protected"
    public = "public"
    static = "static"
    strictfp = "strictfp"
    super = "super"
    synchronized = "synchronized"
    synthetic = "synthetic"
    transient = "transient"
    varargs = "varargs"
    volatile = "volatile"
    abstract = "abstract"
    annotation = "annotation"
    bridge = "bridge"
    default = "default"
    deprecated = "deprecated"
    enum = "enum"
class PostfixExpressionOperatorKind(Enum):
    increment = "increment"
    decrement = "decrement"
class PrefixExpressionOperatorKind(Enum):
    minus = "minus"
    not = "not"
    decrement = "decrement"
    complement = "complement"
    increment = "increment"
    plus = "plus"


############################################
# Definition of Classes
############################################

class PrimitiveTypes_Core_Parameter:

    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class PrimitiveTypes_Core_ISourceReference(ABC):

    def __init__(self, source: str, PrimitiveTypes_Core_ISourceReference: "Core_ISourceRange" = None):
        self.source = source
        self.PrimitiveTypes_Core_ISourceReference = PrimitiveTypes_Core_ISourceReference
        
    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def PrimitiveTypes_Core_ISourceReference(self):
        return self.__PrimitiveTypes_Core_ISourceReference

    @PrimitiveTypes_Core_ISourceReference.setter
    def PrimitiveTypes_Core_ISourceReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PrimitiveTypes_Core_ISourceReference__PrimitiveTypes_Core_ISourceReference", None)
        self.__PrimitiveTypes_Core_ISourceReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Core_ISourceRange"):
                opp_val = getattr(old_value, "Core_ISourceRange", None)
                if opp_val == self:
                    setattr(old_value, "Core_ISourceRange", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Core_ISourceRange"):
                opp_val = getattr(value, "Core_ISourceRange", None)
                setattr(value, "Core_ISourceRange", self)

class PrimitiveTypes_Core_ISourceRange:

    def __init__(self, length: str, offset: str):
        self.length = length
        self.offset = offset
        
    @property
    def length(self) -> str:
        return self.__length

    @length.setter
    def length(self, length: str):
        self.__length = length

    @property
    def offset(self) -> str:
        return self.__offset

    @offset.setter
    def offset(self, offset: str):
        self.__offset = offset

class MemberValuePair:

    pass
class PrimitiveTypes_Core_PhysicalElement(ABC):

    def __init__(self, path: str, isReadOnly: str):
        self.path = path
        self.isReadOnly = isReadOnly
        
    @property
    def isReadOnly(self) -> str:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: str):
        self.__isReadOnly = isReadOnly

    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

class PrimitiveTypes_Core_IJavaElement(ABC):

    def __init__(self, elementName: str):
        self.elementName = elementName
        
    @property
    def elementName(self) -> str:
        return self.__elementName

    @elementName.setter
    def elementName(self, elementName: str):
        self.__elementName = elementName

class VariableDeclaration:

    pass
class DOM_VariableDeclarationFragment(VariableDeclaration):

    pass
class DOM_SingleVariableDeclaration(VariableDeclaration):

    def __init__(self, varargs: str, DOM_SingleVariableDeclaration: "Type" = None, DOM_SingleVariableDeclaration401: set["ExtendedModifier"] = None):
        self.varargs = varargs
        self.DOM_SingleVariableDeclaration = DOM_SingleVariableDeclaration
        self.DOM_SingleVariableDeclaration401 = DOM_SingleVariableDeclaration401 if DOM_SingleVariableDeclaration401 is not None else set()
        
    @property
    def varargs(self) -> str:
        return self.__varargs

    @varargs.setter
    def varargs(self, varargs: str):
        self.__varargs = varargs

    @property
    def DOM_SingleVariableDeclaration401(self):
        return self.__DOM_SingleVariableDeclaration401

    @DOM_SingleVariableDeclaration401.setter
    def DOM_SingleVariableDeclaration401(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_SingleVariableDeclaration__DOM_SingleVariableDeclaration401", None)
        self.__DOM_SingleVariableDeclaration401 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExtendedModifier402"):
                    opp_val = getattr(item, "ExtendedModifier402", None)
                    
                    if opp_val == self:
                        setattr(item, "ExtendedModifier402", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExtendedModifier402"):
                    opp_val = getattr(item, "ExtendedModifier402", None)
                    
                    setattr(item, "ExtendedModifier402", self)
                    

    @property
    def DOM_SingleVariableDeclaration(self):
        return self.__DOM_SingleVariableDeclaration

    @DOM_SingleVariableDeclaration.setter
    def DOM_SingleVariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_SingleVariableDeclaration__DOM_SingleVariableDeclaration", None)
        self.__DOM_SingleVariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type399"):
                opp_val = getattr(old_value, "Type399", None)
                if opp_val == self:
                    setattr(old_value, "Type399", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type399"):
                opp_val = getattr(value, "Type399", None)
                setattr(value, "Type399", self)

class CatchClause:

    pass
class Statement:

    pass
class DOM_SynchronizedStatement(Statement):

    pass
class DOM_ThrowStatement(Statement):

    pass
class DOM_EnhancedForStatement(Statement):

    pass
class DOM_ForStatement(Statement):

    pass
class DOM_SwitchStatement(Statement):

    pass
class DOM_TypeDeclarationStatement(Statement):

    pass
class DOM_IfStatement(Statement):

    pass
class DOM_ReturnStatement(Statement):

    pass
class DOM_SuperConstructorInvocation(Statement):

    pass
class DOM_ExpressionStatement(Statement):

    pass
class DOM_ContinueStatement(Statement):

    pass
class DOM_WhileStatement(Statement):

    pass
class DOM_LabeledStatement(Statement):

    pass
class DOM_SwitchCase(Statement):

    def __init__(self, default: str, DOM_SwitchCase: "Expression" = None, Statement310: "DOM_ForStatement", Statement329: "DOM_LabeledStatement", Statement327: "DOM_IfStatement", Statement321: "DOM_IfStatement", Statement375: "DOM_WhileStatement", Statement295: "DOM_DoStatement", Statement: "DOM_Block", Statement349: "DOM_SwitchStatement", Statement300: "DOM_EnhancedForStatement"):
        self.default = default
        self.DOM_SwitchCase = DOM_SwitchCase
        
    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def DOM_SwitchCase(self):
        return self.__DOM_SwitchCase

    @DOM_SwitchCase.setter
    def DOM_SwitchCase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_SwitchCase__DOM_SwitchCase", None)
        self.__DOM_SwitchCase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression344"):
                opp_val = getattr(old_value, "Expression344", None)
                if opp_val == self:
                    setattr(old_value, "Expression344", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression344"):
                opp_val = getattr(value, "Expression344", None)
                setattr(value, "Expression344", self)

class DOM_EmptyStatement(Statement):

    pass
class DOM_Block(Statement):

    pass
class DOM_DoStatement(Statement):

    pass
class DOM_BreakStatement(Statement):

    pass
class DOM_TryStatement(Statement):

    pass
class DOM_VariableDeclarationStatement(Statement):

    pass
class DOM_ConstructorInvocation(Statement):

    pass
class DOM_AssertStatement(Statement):

    pass
class ArrayType:

    pass
class ArrayInitializer:

    pass
class TagElement:

    pass
class EnumConstantDeclaration:

    pass
class TypeParameter:

    pass
class VariableDeclarationFragment:

    pass
class AnonymousClassDeclaration:

    pass
class Annotation:

    pass
class DOM_MarkerAnnotation(Annotation):

    pass
class DOM_SingleMemberAnnotation(Annotation):

    pass
class DOM_NormalAnnotation(Annotation):

    pass
class DOM_ExtendedModifier(ABC):

    pass
class Type:

    pass
class DOM_WildcardType(Type):

    def __init__(self, upperBound: str, DOM_WildcardType: "Type" = None, Type270: "DOM_TypeLiteral", Type342: "DOM_SuperConstructorInvocation", Type190: "DOM_CastExpression", Type388: "DOM_ParameterizedType", Type278: "DOM_VariableDeclarationExpression", Type291: "DOM_ConstructorInvocation", Type383: "DOM_ArrayType", Type158: "DOM_TypeDeclaration", Type204: "DOM_ClassInstanceCreation", Type266: "DOM_SuperMethodInvocation", Type241: "DOM_MethodInvocation", Type: "DOM_MethodRefParameter", Type380: "DOM_ArrayType", Type201: "DOM_ClassInstanceCreation", Type393: "DOM_QualifiedType", Type141: "DOM_MethodDeclaration", Type120: "DOM_AnnotationTypeMemberDeclaration", Type399: "DOM_SingleVariableDeclaration", Type373: "DOM_VariableDeclarationStatement", Type230: "DOM_InstanceofExpression", Type385: "DOM_ParameterizedType", Type102: "DOM_TypeParameter", Type161: "DOM_TypeDeclaration", Type154: "DOM_EnumDeclaration", Type397: "DOM_WildcardType", Type131: "DOM_FieldDeclaration"):
        self.upperBound = upperBound
        self.DOM_WildcardType = DOM_WildcardType
        
    @property
    def upperBound(self) -> str:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: str):
        self.__upperBound = upperBound

    @property
    def DOM_WildcardType(self):
        return self.__DOM_WildcardType

    @DOM_WildcardType.setter
    def DOM_WildcardType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_WildcardType__DOM_WildcardType", None)
        self.__DOM_WildcardType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type397"):
                opp_val = getattr(old_value, "Type397", None)
                if opp_val == self:
                    setattr(old_value, "Type397", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type397"):
                opp_val = getattr(value, "Type397", None)
                setattr(value, "Type397", self)

class DOM_PrimitiveType(Type):

    def __init__(self, code: str, Type270: "DOM_TypeLiteral", Type342: "DOM_SuperConstructorInvocation", Type190: "DOM_CastExpression", Type388: "DOM_ParameterizedType", Type278: "DOM_VariableDeclarationExpression", Type291: "DOM_ConstructorInvocation", Type383: "DOM_ArrayType", Type158: "DOM_TypeDeclaration", Type204: "DOM_ClassInstanceCreation", Type266: "DOM_SuperMethodInvocation", Type241: "DOM_MethodInvocation", Type: "DOM_MethodRefParameter", Type380: "DOM_ArrayType", Type201: "DOM_ClassInstanceCreation", Type393: "DOM_QualifiedType", Type141: "DOM_MethodDeclaration", Type120: "DOM_AnnotationTypeMemberDeclaration", Type399: "DOM_SingleVariableDeclaration", Type373: "DOM_VariableDeclarationStatement", Type230: "DOM_InstanceofExpression", Type385: "DOM_ParameterizedType", Type102: "DOM_TypeParameter", Type161: "DOM_TypeDeclaration", Type154: "DOM_EnumDeclaration", Type397: "DOM_WildcardType", Type131: "DOM_FieldDeclaration"):
        self.code = code
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

class DOM_SimpleType(Type):

    pass
class DOM_QualifiedType(Type):

    pass
class DOM_ParameterizedType(Type):

    pass
class DOM_ArrayType(Type):

    def __init__(self, dimensions: str, DOM_ArrayType: "Type" = None, DOM_ArrayType382: "Type" = None, Type270: "DOM_TypeLiteral", Type342: "DOM_SuperConstructorInvocation", Type190: "DOM_CastExpression", Type388: "DOM_ParameterizedType", Type278: "DOM_VariableDeclarationExpression", Type291: "DOM_ConstructorInvocation", Type383: "DOM_ArrayType", Type158: "DOM_TypeDeclaration", Type204: "DOM_ClassInstanceCreation", Type266: "DOM_SuperMethodInvocation", Type241: "DOM_MethodInvocation", Type: "DOM_MethodRefParameter", Type380: "DOM_ArrayType", Type201: "DOM_ClassInstanceCreation", Type393: "DOM_QualifiedType", Type141: "DOM_MethodDeclaration", Type120: "DOM_AnnotationTypeMemberDeclaration", Type399: "DOM_SingleVariableDeclaration", Type373: "DOM_VariableDeclarationStatement", Type230: "DOM_InstanceofExpression", Type385: "DOM_ParameterizedType", Type102: "DOM_TypeParameter", Type161: "DOM_TypeDeclaration", Type154: "DOM_EnumDeclaration", Type397: "DOM_WildcardType", Type131: "DOM_FieldDeclaration"):
        self.dimensions = dimensions
        self.DOM_ArrayType = DOM_ArrayType
        self.DOM_ArrayType382 = DOM_ArrayType382
        
    @property
    def dimensions(self) -> str:
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, dimensions: str):
        self.__dimensions = dimensions

    @property
    def DOM_ArrayType382(self):
        return self.__DOM_ArrayType382

    @DOM_ArrayType382.setter
    def DOM_ArrayType382(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_ArrayType__DOM_ArrayType382", None)
        self.__DOM_ArrayType382 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type383"):
                opp_val = getattr(old_value, "Type383", None)
                if opp_val == self:
                    setattr(old_value, "Type383", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type383"):
                opp_val = getattr(value, "Type383", None)
                setattr(value, "Type383", self)

    @property
    def DOM_ArrayType(self):
        return self.__DOM_ArrayType

    @DOM_ArrayType.setter
    def DOM_ArrayType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_ArrayType__DOM_ArrayType", None)
        self.__DOM_ArrayType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type380"):
                opp_val = getattr(old_value, "Type380", None)
                if opp_val == self:
                    setattr(old_value, "Type380", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type380"):
                opp_val = getattr(value, "Type380", None)
                setattr(value, "Type380", self)

class MethodRefParameter:

    pass
class Expression:

    pass
class DOM_MethodInvocation(Expression):

    pass
class DOM_VariableDeclarationExpression(Expression):

    pass
class DOM_SuperFieldAccess(Expression):

    pass
class DOM_InstanceofExpression(Expression):

    pass
class DOM_CharacterLiteral(Expression):

    def __init__(self, escapedValue: str, charValue: str, Expression225: "DOM_InfixExpression", Expression198: "DOM_ClassInstanceCreation", Expression235: "DOM_MethodInvocation", Expression257: "DOM_SuperMethodInvocation", Expression232: "DOM_MethodInvocation", Expression222: "DOM_InfixExpression", Expression339: "DOM_SuperConstructorInvocation", Expression172: "DOM_ArrayAccess", Expression319: "DOM_ForStatement", Expression182: "DOM_Assignment", Expression: "DOM_MemberValuePair", Expression187: "DOM_CastExpression", Expression280: "DOM_AssertStatement", Expression214: "DOM_FieldAccess", Expression378: "DOM_WhileStatement", Expression248: "DOM_PostfixExpression", Expression209: "DOM_ConditionalExpression", Expression104: "DOM_VariableDeclaration", Expression174: "DOM_ArrayCreation", Expression344: "DOM_SwitchCase", Expression346: "DOM_SwitchStatement", Expression288: "DOM_ConstructorInvocation", Expression169: "DOM_ArrayAccess", Expression122: "DOM_EnumConstantDeclaration", Expression334: "DOM_ReturnStatement", Expression227: "DOM_InstanceofExpression", Expression283: "DOM_AssertStatement", Expression185: "DOM_Assignment", Expression180: "DOM_ArrayInitializer", Expression206: "DOM_ConditionalExpression", Expression114: "DOM_AnnotationTypeMemberDeclaration", Expression324: "DOM_IfStatement", Expression354: "DOM_SynchronizedStatement", Expression212: "DOM_ConditionalExpression", Expression219: "DOM_InfixExpression", Expression250: "DOM_PrefixExpression", Expression313: "DOM_ForStatement", Expression303: "DOM_EnhancedForStatement", Expression192: "DOM_ClassInstanceCreation", Expression356: "DOM_ThrowStatement", Expression246: "DOM_ParenthesizedExpression", Expression308: "DOM_ExpressionStatement", Expression336: "DOM_SuperConstructorInvocation", Expression298: "DOM_DoStatement", Expression410: "DOM_SingleMemberAnnotation", Expression316: "DOM_ForStatement"):
        self.escapedValue = escapedValue
        self.charValue = charValue
        
    @property
    def charValue(self) -> str:
        return self.__charValue

    @charValue.setter
    def charValue(self, charValue: str):
        self.__charValue = charValue

    @property
    def escapedValue(self) -> str:
        return self.__escapedValue

    @escapedValue.setter
    def escapedValue(self, escapedValue: str):
        self.__escapedValue = escapedValue

class DOM_ConditionalExpression(Expression):

    pass
class DOM_ThisExpression(Expression):

    pass
class DOM_SuperMethodInvocation(Expression):

    pass
class DOM_InfixExpression(Expression):

    def __init__(self, operator: str, DOM_InfixExpression: set["Expression"] = None, DOM_InfixExpression221: "Expression" = None, DOM_InfixExpression224: "Expression" = None, Expression225: "DOM_InfixExpression", Expression198: "DOM_ClassInstanceCreation", Expression235: "DOM_MethodInvocation", Expression257: "DOM_SuperMethodInvocation", Expression232: "DOM_MethodInvocation", Expression222: "DOM_InfixExpression", Expression339: "DOM_SuperConstructorInvocation", Expression172: "DOM_ArrayAccess", Expression319: "DOM_ForStatement", Expression182: "DOM_Assignment", Expression: "DOM_MemberValuePair", Expression187: "DOM_CastExpression", Expression280: "DOM_AssertStatement", Expression214: "DOM_FieldAccess", Expression378: "DOM_WhileStatement", Expression248: "DOM_PostfixExpression", Expression209: "DOM_ConditionalExpression", Expression104: "DOM_VariableDeclaration", Expression174: "DOM_ArrayCreation", Expression344: "DOM_SwitchCase", Expression346: "DOM_SwitchStatement", Expression288: "DOM_ConstructorInvocation", Expression169: "DOM_ArrayAccess", Expression122: "DOM_EnumConstantDeclaration", Expression334: "DOM_ReturnStatement", Expression227: "DOM_InstanceofExpression", Expression283: "DOM_AssertStatement", Expression185: "DOM_Assignment", Expression180: "DOM_ArrayInitializer", Expression206: "DOM_ConditionalExpression", Expression114: "DOM_AnnotationTypeMemberDeclaration", Expression324: "DOM_IfStatement", Expression354: "DOM_SynchronizedStatement", Expression212: "DOM_ConditionalExpression", Expression219: "DOM_InfixExpression", Expression250: "DOM_PrefixExpression", Expression313: "DOM_ForStatement", Expression303: "DOM_EnhancedForStatement", Expression192: "DOM_ClassInstanceCreation", Expression356: "DOM_ThrowStatement", Expression246: "DOM_ParenthesizedExpression", Expression308: "DOM_ExpressionStatement", Expression336: "DOM_SuperConstructorInvocation", Expression298: "DOM_DoStatement", Expression410: "DOM_SingleMemberAnnotation", Expression316: "DOM_ForStatement"):
        self.operator = operator
        self.DOM_InfixExpression = DOM_InfixExpression if DOM_InfixExpression is not None else set()
        self.DOM_InfixExpression221 = DOM_InfixExpression221
        self.DOM_InfixExpression224 = DOM_InfixExpression224
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def DOM_InfixExpression(self):
        return self.__DOM_InfixExpression

    @DOM_InfixExpression.setter
    def DOM_InfixExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_InfixExpression__DOM_InfixExpression", None)
        self.__DOM_InfixExpression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Expression219"):
                    opp_val = getattr(item, "Expression219", None)
                    
                    if opp_val == self:
                        setattr(item, "Expression219", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Expression219"):
                    opp_val = getattr(item, "Expression219", None)
                    
                    setattr(item, "Expression219", self)
                    

    @property
    def DOM_InfixExpression221(self):
        return self.__DOM_InfixExpression221

    @DOM_InfixExpression221.setter
    def DOM_InfixExpression221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_InfixExpression__DOM_InfixExpression221", None)
        self.__DOM_InfixExpression221 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression222"):
                opp_val = getattr(old_value, "Expression222", None)
                if opp_val == self:
                    setattr(old_value, "Expression222", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression222"):
                opp_val = getattr(value, "Expression222", None)
                setattr(value, "Expression222", self)

    @property
    def DOM_InfixExpression224(self):
        return self.__DOM_InfixExpression224

    @DOM_InfixExpression224.setter
    def DOM_InfixExpression224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_InfixExpression__DOM_InfixExpression224", None)
        self.__DOM_InfixExpression224 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression225"):
                opp_val = getattr(old_value, "Expression225", None)
                if opp_val == self:
                    setattr(old_value, "Expression225", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression225"):
                opp_val = getattr(value, "Expression225", None)
                setattr(value, "Expression225", self)

class DOM_ArrayCreation(Expression):

    pass
class DOM_ParenthesizedExpression(Expression):

    pass
class DOM_BooleanLiteral(Expression):

    def __init__(self, booleanValue: str, Expression225: "DOM_InfixExpression", Expression198: "DOM_ClassInstanceCreation", Expression235: "DOM_MethodInvocation", Expression257: "DOM_SuperMethodInvocation", Expression232: "DOM_MethodInvocation", Expression222: "DOM_InfixExpression", Expression339: "DOM_SuperConstructorInvocation", Expression172: "DOM_ArrayAccess", Expression319: "DOM_ForStatement", Expression182: "DOM_Assignment", Expression: "DOM_MemberValuePair", Expression187: "DOM_CastExpression", Expression280: "DOM_AssertStatement", Expression214: "DOM_FieldAccess", Expression378: "DOM_WhileStatement", Expression248: "DOM_PostfixExpression", Expression209: "DOM_ConditionalExpression", Expression104: "DOM_VariableDeclaration", Expression174: "DOM_ArrayCreation", Expression344: "DOM_SwitchCase", Expression346: "DOM_SwitchStatement", Expression288: "DOM_ConstructorInvocation", Expression169: "DOM_ArrayAccess", Expression122: "DOM_EnumConstantDeclaration", Expression334: "DOM_ReturnStatement", Expression227: "DOM_InstanceofExpression", Expression283: "DOM_AssertStatement", Expression185: "DOM_Assignment", Expression180: "DOM_ArrayInitializer", Expression206: "DOM_ConditionalExpression", Expression114: "DOM_AnnotationTypeMemberDeclaration", Expression324: "DOM_IfStatement", Expression354: "DOM_SynchronizedStatement", Expression212: "DOM_ConditionalExpression", Expression219: "DOM_InfixExpression", Expression250: "DOM_PrefixExpression", Expression313: "DOM_ForStatement", Expression303: "DOM_EnhancedForStatement", Expression192: "DOM_ClassInstanceCreation", Expression356: "DOM_ThrowStatement", Expression246: "DOM_ParenthesizedExpression", Expression308: "DOM_ExpressionStatement", Expression336: "DOM_SuperConstructorInvocation", Expression298: "DOM_DoStatement", Expression410: "DOM_SingleMemberAnnotation", Expression316: "DOM_ForStatement"):
        self.booleanValue = booleanValue
        
    @property
    def booleanValue(self) -> str:
        return self.__booleanValue

    @booleanValue.setter
    def booleanValue(self, booleanValue: str):
        self.__booleanValue = booleanValue

class DOM_NumberLiteral(Expression):

    def __init__(self, token: str, Expression225: "DOM_InfixExpression", Expression198: "DOM_ClassInstanceCreation", Expression235: "DOM_MethodInvocation", Expression257: "DOM_SuperMethodInvocation", Expression232: "DOM_MethodInvocation", Expression222: "DOM_InfixExpression", Expression339: "DOM_SuperConstructorInvocation", Expression172: "DOM_ArrayAccess", Expression319: "DOM_ForStatement", Expression182: "DOM_Assignment", Expression: "DOM_MemberValuePair", Expression187: "DOM_CastExpression", Expression280: "DOM_AssertStatement", Expression214: "DOM_FieldAccess", Expression378: "DOM_WhileStatement", Expression248: "DOM_PostfixExpression", Expression209: "DOM_ConditionalExpression", Expression104: "DOM_VariableDeclaration", Expression174: "DOM_ArrayCreation", Expression344: "DOM_SwitchCase", Expression346: "DOM_SwitchStatement", Expression288: "DOM_ConstructorInvocation", Expression169: "DOM_ArrayAccess", Expression122: "DOM_EnumConstantDeclaration", Expression334: "DOM_ReturnStatement", Expression227: "DOM_InstanceofExpression", Expression283: "DOM_AssertStatement", Expression185: "DOM_Assignment", Expression180: "DOM_ArrayInitializer", Expression206: "DOM_ConditionalExpression", Expression114: "DOM_AnnotationTypeMemberDeclaration", Expression324: "DOM_IfStatement", Expression354: "DOM_SynchronizedStatement", Expression212: "DOM_ConditionalExpression", Expression219: "DOM_InfixExpression", Expression250: "DOM_PrefixExpression", Expression313: "DOM_ForStatement", Expression303: "DOM_EnhancedForStatement", Expression192: "DOM_ClassInstanceCreation", Expression356: "DOM_ThrowStatement", Expression246: "DOM_ParenthesizedExpression", Expression308: "DOM_ExpressionStatement", Expression336: "DOM_SuperConstructorInvocation", Expression298: "DOM_DoStatement", Expression410: "DOM_SingleMemberAnnotation", Expression316: "DOM_ForStatement"):
        self.token = token
        
    @property
    def token(self) -> str:
        return self.__token

    @token.setter
    def token(self, token: str):
        self.__token = token

class DOM_FieldAccess(Expression):

    pass
class DOM_ArrayAccess(Expression):

    pass
class DOM_Assignment(Expression):

    def __init__(self, operator: str, DOM_Assignment: "Expression" = None, DOM_Assignment184: "Expression" = None, Expression225: "DOM_InfixExpression", Expression198: "DOM_ClassInstanceCreation", Expression235: "DOM_MethodInvocation", Expression257: "DOM_SuperMethodInvocation", Expression232: "DOM_MethodInvocation", Expression222: "DOM_InfixExpression", Expression339: "DOM_SuperConstructorInvocation", Expression172: "DOM_ArrayAccess", Expression319: "DOM_ForStatement", Expression182: "DOM_Assignment", Expression: "DOM_MemberValuePair", Expression187: "DOM_CastExpression", Expression280: "DOM_AssertStatement", Expression214: "DOM_FieldAccess", Expression378: "DOM_WhileStatement", Expression248: "DOM_PostfixExpression", Expression209: "DOM_ConditionalExpression", Expression104: "DOM_VariableDeclaration", Expression174: "DOM_ArrayCreation", Expression344: "DOM_SwitchCase", Expression346: "DOM_SwitchStatement", Expression288: "DOM_ConstructorInvocation", Expression169: "DOM_ArrayAccess", Expression122: "DOM_EnumConstantDeclaration", Expression334: "DOM_ReturnStatement", Expression227: "DOM_InstanceofExpression", Expression283: "DOM_AssertStatement", Expression185: "DOM_Assignment", Expression180: "DOM_ArrayInitializer", Expression206: "DOM_ConditionalExpression", Expression114: "DOM_AnnotationTypeMemberDeclaration", Expression324: "DOM_IfStatement", Expression354: "DOM_SynchronizedStatement", Expression212: "DOM_ConditionalExpression", Expression219: "DOM_InfixExpression", Expression250: "DOM_PrefixExpression", Expression313: "DOM_ForStatement", Expression303: "DOM_EnhancedForStatement", Expression192: "DOM_ClassInstanceCreation", Expression356: "DOM_ThrowStatement", Expression246: "DOM_ParenthesizedExpression", Expression308: "DOM_ExpressionStatement", Expression336: "DOM_SuperConstructorInvocation", Expression298: "DOM_DoStatement", Expression410: "DOM_SingleMemberAnnotation", Expression316: "DOM_ForStatement"):
        self.operator = operator
        self.DOM_Assignment = DOM_Assignment
        self.DOM_Assignment184 = DOM_Assignment184
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def DOM_Assignment(self):
        return self.__DOM_Assignment

    @DOM_Assignment.setter
    def DOM_Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Assignment__DOM_Assignment", None)
        self.__DOM_Assignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression182"):
                opp_val = getattr(old_value, "Expression182", None)
                if opp_val == self:
                    setattr(old_value, "Expression182", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression182"):
                opp_val = getattr(value, "Expression182", None)
                setattr(value, "Expression182", self)

    @property
    def DOM_Assignment184(self):
        return self.__DOM_Assignment184

    @DOM_Assignment184.setter
    def DOM_Assignment184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Assignment__DOM_Assignment184", None)
        self.__DOM_Assignment184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression185"):
                opp_val = getattr(old_value, "Expression185", None)
                if opp_val == self:
                    setattr(old_value, "Expression185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression185"):
                opp_val = getattr(value, "Expression185", None)
                setattr(value, "Expression185", self)

class DOM_TypeLiteral(Expression):

    pass
class DOM_Name(Expression):

    def __init__(self, fullyQualifiedName: str, Expression225: "DOM_InfixExpression", Expression198: "DOM_ClassInstanceCreation", Expression235: "DOM_MethodInvocation", Expression257: "DOM_SuperMethodInvocation", Expression232: "DOM_MethodInvocation", Expression222: "DOM_InfixExpression", Expression339: "DOM_SuperConstructorInvocation", Expression172: "DOM_ArrayAccess", Expression319: "DOM_ForStatement", Expression182: "DOM_Assignment", Expression: "DOM_MemberValuePair", Expression187: "DOM_CastExpression", Expression280: "DOM_AssertStatement", Expression214: "DOM_FieldAccess", Expression378: "DOM_WhileStatement", Expression248: "DOM_PostfixExpression", Expression209: "DOM_ConditionalExpression", Expression104: "DOM_VariableDeclaration", Expression174: "DOM_ArrayCreation", Expression344: "DOM_SwitchCase", Expression346: "DOM_SwitchStatement", Expression288: "DOM_ConstructorInvocation", Expression169: "DOM_ArrayAccess", Expression122: "DOM_EnumConstantDeclaration", Expression334: "DOM_ReturnStatement", Expression227: "DOM_InstanceofExpression", Expression283: "DOM_AssertStatement", Expression185: "DOM_Assignment", Expression180: "DOM_ArrayInitializer", Expression206: "DOM_ConditionalExpression", Expression114: "DOM_AnnotationTypeMemberDeclaration", Expression324: "DOM_IfStatement", Expression354: "DOM_SynchronizedStatement", Expression212: "DOM_ConditionalExpression", Expression219: "DOM_InfixExpression", Expression250: "DOM_PrefixExpression", Expression313: "DOM_ForStatement", Expression303: "DOM_EnhancedForStatement", Expression192: "DOM_ClassInstanceCreation", Expression356: "DOM_ThrowStatement", Expression246: "DOM_ParenthesizedExpression", Expression308: "DOM_ExpressionStatement", Expression336: "DOM_SuperConstructorInvocation", Expression298: "DOM_DoStatement", Expression410: "DOM_SingleMemberAnnotation", Expression316: "DOM_ForStatement"):
        self.fullyQualifiedName = fullyQualifiedName
        
    @property
    def fullyQualifiedName(self) -> str:
        return self.__fullyQualifiedName

    @fullyQualifiedName.setter
    def fullyQualifiedName(self, fullyQualifiedName: str):
        self.__fullyQualifiedName = fullyQualifiedName

class DOM_CastExpression(Expression):

    pass
class DOM_PostfixExpression(Expression):

    def __init__(self, operator: str, DOM_PostfixExpression: "Expression" = None, Expression225: "DOM_InfixExpression", Expression198: "DOM_ClassInstanceCreation", Expression235: "DOM_MethodInvocation", Expression257: "DOM_SuperMethodInvocation", Expression232: "DOM_MethodInvocation", Expression222: "DOM_InfixExpression", Expression339: "DOM_SuperConstructorInvocation", Expression172: "DOM_ArrayAccess", Expression319: "DOM_ForStatement", Expression182: "DOM_Assignment", Expression: "DOM_MemberValuePair", Expression187: "DOM_CastExpression", Expression280: "DOM_AssertStatement", Expression214: "DOM_FieldAccess", Expression378: "DOM_WhileStatement", Expression248: "DOM_PostfixExpression", Expression209: "DOM_ConditionalExpression", Expression104: "DOM_VariableDeclaration", Expression174: "DOM_ArrayCreation", Expression344: "DOM_SwitchCase", Expression346: "DOM_SwitchStatement", Expression288: "DOM_ConstructorInvocation", Expression169: "DOM_ArrayAccess", Expression122: "DOM_EnumConstantDeclaration", Expression334: "DOM_ReturnStatement", Expression227: "DOM_InstanceofExpression", Expression283: "DOM_AssertStatement", Expression185: "DOM_Assignment", Expression180: "DOM_ArrayInitializer", Expression206: "DOM_ConditionalExpression", Expression114: "DOM_AnnotationTypeMemberDeclaration", Expression324: "DOM_IfStatement", Expression354: "DOM_SynchronizedStatement", Expression212: "DOM_ConditionalExpression", Expression219: "DOM_InfixExpression", Expression250: "DOM_PrefixExpression", Expression313: "DOM_ForStatement", Expression303: "DOM_EnhancedForStatement", Expression192: "DOM_ClassInstanceCreation", Expression356: "DOM_ThrowStatement", Expression246: "DOM_ParenthesizedExpression", Expression308: "DOM_ExpressionStatement", Expression336: "DOM_SuperConstructorInvocation", Expression298: "DOM_DoStatement", Expression410: "DOM_SingleMemberAnnotation", Expression316: "DOM_ForStatement"):
        self.operator = operator
        self.DOM_PostfixExpression = DOM_PostfixExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def DOM_PostfixExpression(self):
        return self.__DOM_PostfixExpression

    @DOM_PostfixExpression.setter
    def DOM_PostfixExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_PostfixExpression__DOM_PostfixExpression", None)
        self.__DOM_PostfixExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression248"):
                opp_val = getattr(old_value, "Expression248", None)
                if opp_val == self:
                    setattr(old_value, "Expression248", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression248"):
                opp_val = getattr(value, "Expression248", None)
                setattr(value, "Expression248", self)

class DOM_ArrayInitializer(Expression):

    pass
class DOM_StringLiteral(Expression):

    def __init__(self, literalValue: str, escapedValue: str, Expression225: "DOM_InfixExpression", Expression198: "DOM_ClassInstanceCreation", Expression235: "DOM_MethodInvocation", Expression257: "DOM_SuperMethodInvocation", Expression232: "DOM_MethodInvocation", Expression222: "DOM_InfixExpression", Expression339: "DOM_SuperConstructorInvocation", Expression172: "DOM_ArrayAccess", Expression319: "DOM_ForStatement", Expression182: "DOM_Assignment", Expression: "DOM_MemberValuePair", Expression187: "DOM_CastExpression", Expression280: "DOM_AssertStatement", Expression214: "DOM_FieldAccess", Expression378: "DOM_WhileStatement", Expression248: "DOM_PostfixExpression", Expression209: "DOM_ConditionalExpression", Expression104: "DOM_VariableDeclaration", Expression174: "DOM_ArrayCreation", Expression344: "DOM_SwitchCase", Expression346: "DOM_SwitchStatement", Expression288: "DOM_ConstructorInvocation", Expression169: "DOM_ArrayAccess", Expression122: "DOM_EnumConstantDeclaration", Expression334: "DOM_ReturnStatement", Expression227: "DOM_InstanceofExpression", Expression283: "DOM_AssertStatement", Expression185: "DOM_Assignment", Expression180: "DOM_ArrayInitializer", Expression206: "DOM_ConditionalExpression", Expression114: "DOM_AnnotationTypeMemberDeclaration", Expression324: "DOM_IfStatement", Expression354: "DOM_SynchronizedStatement", Expression212: "DOM_ConditionalExpression", Expression219: "DOM_InfixExpression", Expression250: "DOM_PrefixExpression", Expression313: "DOM_ForStatement", Expression303: "DOM_EnhancedForStatement", Expression192: "DOM_ClassInstanceCreation", Expression356: "DOM_ThrowStatement", Expression246: "DOM_ParenthesizedExpression", Expression308: "DOM_ExpressionStatement", Expression336: "DOM_SuperConstructorInvocation", Expression298: "DOM_DoStatement", Expression410: "DOM_SingleMemberAnnotation", Expression316: "DOM_ForStatement"):
        self.literalValue = literalValue
        self.escapedValue = escapedValue
        
    @property
    def escapedValue(self) -> str:
        return self.__escapedValue

    @escapedValue.setter
    def escapedValue(self, escapedValue: str):
        self.__escapedValue = escapedValue

    @property
    def literalValue(self) -> str:
        return self.__literalValue

    @literalValue.setter
    def literalValue(self, literalValue: str):
        self.__literalValue = literalValue

class DOM_PrefixExpression(Expression):

    def __init__(self, operator: str, DOM_PrefixExpression: "Expression" = None, Expression225: "DOM_InfixExpression", Expression198: "DOM_ClassInstanceCreation", Expression235: "DOM_MethodInvocation", Expression257: "DOM_SuperMethodInvocation", Expression232: "DOM_MethodInvocation", Expression222: "DOM_InfixExpression", Expression339: "DOM_SuperConstructorInvocation", Expression172: "DOM_ArrayAccess", Expression319: "DOM_ForStatement", Expression182: "DOM_Assignment", Expression: "DOM_MemberValuePair", Expression187: "DOM_CastExpression", Expression280: "DOM_AssertStatement", Expression214: "DOM_FieldAccess", Expression378: "DOM_WhileStatement", Expression248: "DOM_PostfixExpression", Expression209: "DOM_ConditionalExpression", Expression104: "DOM_VariableDeclaration", Expression174: "DOM_ArrayCreation", Expression344: "DOM_SwitchCase", Expression346: "DOM_SwitchStatement", Expression288: "DOM_ConstructorInvocation", Expression169: "DOM_ArrayAccess", Expression122: "DOM_EnumConstantDeclaration", Expression334: "DOM_ReturnStatement", Expression227: "DOM_InstanceofExpression", Expression283: "DOM_AssertStatement", Expression185: "DOM_Assignment", Expression180: "DOM_ArrayInitializer", Expression206: "DOM_ConditionalExpression", Expression114: "DOM_AnnotationTypeMemberDeclaration", Expression324: "DOM_IfStatement", Expression354: "DOM_SynchronizedStatement", Expression212: "DOM_ConditionalExpression", Expression219: "DOM_InfixExpression", Expression250: "DOM_PrefixExpression", Expression313: "DOM_ForStatement", Expression303: "DOM_EnhancedForStatement", Expression192: "DOM_ClassInstanceCreation", Expression356: "DOM_ThrowStatement", Expression246: "DOM_ParenthesizedExpression", Expression308: "DOM_ExpressionStatement", Expression336: "DOM_SuperConstructorInvocation", Expression298: "DOM_DoStatement", Expression410: "DOM_SingleMemberAnnotation", Expression316: "DOM_ForStatement"):
        self.operator = operator
        self.DOM_PrefixExpression = DOM_PrefixExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def DOM_PrefixExpression(self):
        return self.__DOM_PrefixExpression

    @DOM_PrefixExpression.setter
    def DOM_PrefixExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_PrefixExpression__DOM_PrefixExpression", None)
        self.__DOM_PrefixExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression250"):
                opp_val = getattr(old_value, "Expression250", None)
                if opp_val == self:
                    setattr(old_value, "Expression250", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression250"):
                opp_val = getattr(value, "Expression250", None)
                setattr(value, "Expression250", self)

class DOM_ClassInstanceCreation(Expression):

    pass
class DOM_NullLiteral(Expression):

    pass
class SimpleName:

    pass
class Name:

    pass
class DOM_SimpleName(Name):

    def __init__(self, identifier: str, declaration: str, Name407: "DOM_QualifiedName", Name255: "DOM_SuperFieldAccess", Name167: "DOM_Annotation", Name260: "DOM_SuperMethodInvocation", Name395: "DOM_SimpleType", Name80: "DOM_MethodRef", Name93: "DOM_PackageDeclaration", Name: "DOM_ImportDeclaration", Name71: "DOM_MemberRef", Name268: "DOM_ThisExpression", Name263: "DOM_SuperMethodInvocation", Name147: "DOM_MethodDeclaration"):
        self.identifier = identifier
        self.declaration = declaration
        
    @property
    def declaration(self) -> str:
        return self.__declaration

    @declaration.setter
    def declaration(self, declaration: str):
        self.__declaration = declaration

    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

class DOM_QualifiedName(Name):

    pass
class AbstractTypeDeclaration:

    pass
class DOM_EnumDeclaration(AbstractTypeDeclaration):

    pass
class DOM_TypeDeclaration(AbstractTypeDeclaration):

    def __init__(self, interface: str, DOM_TypeDeclaration: "Type" = None, DOM_TypeDeclaration160: set["Type"] = None, DOM_TypeDeclaration163: set["TypeParameter"] = None, AbstractTypeDeclaration365: "DOM_TypeDeclarationStatement", AbstractTypeDeclaration: "DOM_CompilationUnit"):
        self.interface = interface
        self.DOM_TypeDeclaration = DOM_TypeDeclaration
        self.DOM_TypeDeclaration160 = DOM_TypeDeclaration160 if DOM_TypeDeclaration160 is not None else set()
        self.DOM_TypeDeclaration163 = DOM_TypeDeclaration163 if DOM_TypeDeclaration163 is not None else set()
        
    @property
    def interface(self) -> str:
        return self.__interface

    @interface.setter
    def interface(self, interface: str):
        self.__interface = interface

    @property
    def DOM_TypeDeclaration160(self):
        return self.__DOM_TypeDeclaration160

    @DOM_TypeDeclaration160.setter
    def DOM_TypeDeclaration160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_TypeDeclaration__DOM_TypeDeclaration160", None)
        self.__DOM_TypeDeclaration160 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Type161"):
                    opp_val = getattr(item, "Type161", None)
                    
                    if opp_val == self:
                        setattr(item, "Type161", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Type161"):
                    opp_val = getattr(item, "Type161", None)
                    
                    setattr(item, "Type161", self)
                    

    @property
    def DOM_TypeDeclaration163(self):
        return self.__DOM_TypeDeclaration163

    @DOM_TypeDeclaration163.setter
    def DOM_TypeDeclaration163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_TypeDeclaration__DOM_TypeDeclaration163", None)
        self.__DOM_TypeDeclaration163 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypeParameter164"):
                    opp_val = getattr(item, "TypeParameter164", None)
                    
                    if opp_val == self:
                        setattr(item, "TypeParameter164", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypeParameter164"):
                    opp_val = getattr(item, "TypeParameter164", None)
                    
                    setattr(item, "TypeParameter164", self)
                    

    @property
    def DOM_TypeDeclaration(self):
        return self.__DOM_TypeDeclaration

    @DOM_TypeDeclaration.setter
    def DOM_TypeDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_TypeDeclaration__DOM_TypeDeclaration", None)
        self.__DOM_TypeDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type158"):
                opp_val = getattr(old_value, "Type158", None)
                if opp_val == self:
                    setattr(old_value, "Type158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type158"):
                opp_val = getattr(value, "Type158", None)
                setattr(value, "Type158", self)

class DOM_AnnotationTypeDeclaration(AbstractTypeDeclaration):

    pass
class ImportDeclaration:

    pass
class PackageDeclaration:

    pass
class SingleVariableDeclaration:

    pass
class Block:

    pass
class Javadoc:

    pass
class ExtendedModifier:

    pass
class DOM_Annotation(Expression, ExtendedModifier):

    pass
class Comment:

    pass
class DOM_Javadoc(Comment):

    pass
class DOM_BlockComment(Comment):

    pass
class DOM_LineComment(Comment):

    pass
class BodyDeclaration:

    pass
class DOM_Initializer(BodyDeclaration):

    pass
class DOM_EnumConstantDeclaration(BodyDeclaration):

    pass
class DOM_AnnotationTypeMemberDeclaration(BodyDeclaration):

    pass
class DOM_FieldDeclaration(BodyDeclaration):

    pass
class DOM_AbstractTypeDeclaration(BodyDeclaration):

    def __init__(self, localTypeDeclaration: str, memberTypeDeclaration: str, packageMemberTypeDeclaration: str, DOM_AbstractTypeDeclaration: set["BodyDeclaration"] = None, DOM_AbstractTypeDeclaration111: "SimpleName" = None, BodyDeclaration109: "DOM_AbstractTypeDeclaration", BodyDeclaration: "DOM_AnonymousClassDeclaration"):
        self.localTypeDeclaration = localTypeDeclaration
        self.memberTypeDeclaration = memberTypeDeclaration
        self.packageMemberTypeDeclaration = packageMemberTypeDeclaration
        self.DOM_AbstractTypeDeclaration = DOM_AbstractTypeDeclaration if DOM_AbstractTypeDeclaration is not None else set()
        self.DOM_AbstractTypeDeclaration111 = DOM_AbstractTypeDeclaration111
        
    @property
    def memberTypeDeclaration(self) -> str:
        return self.__memberTypeDeclaration

    @memberTypeDeclaration.setter
    def memberTypeDeclaration(self, memberTypeDeclaration: str):
        self.__memberTypeDeclaration = memberTypeDeclaration

    @property
    def packageMemberTypeDeclaration(self) -> str:
        return self.__packageMemberTypeDeclaration

    @packageMemberTypeDeclaration.setter
    def packageMemberTypeDeclaration(self, packageMemberTypeDeclaration: str):
        self.__packageMemberTypeDeclaration = packageMemberTypeDeclaration

    @property
    def localTypeDeclaration(self) -> str:
        return self.__localTypeDeclaration

    @localTypeDeclaration.setter
    def localTypeDeclaration(self, localTypeDeclaration: str):
        self.__localTypeDeclaration = localTypeDeclaration

    @property
    def DOM_AbstractTypeDeclaration111(self):
        return self.__DOM_AbstractTypeDeclaration111

    @DOM_AbstractTypeDeclaration111.setter
    def DOM_AbstractTypeDeclaration111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_AbstractTypeDeclaration__DOM_AbstractTypeDeclaration111", None)
        self.__DOM_AbstractTypeDeclaration111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleName112"):
                opp_val = getattr(old_value, "SimpleName112", None)
                if opp_val == self:
                    setattr(old_value, "SimpleName112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleName112"):
                opp_val = getattr(value, "SimpleName112", None)
                setattr(value, "SimpleName112", self)

    @property
    def DOM_AbstractTypeDeclaration(self):
        return self.__DOM_AbstractTypeDeclaration

    @DOM_AbstractTypeDeclaration.setter
    def DOM_AbstractTypeDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_AbstractTypeDeclaration__DOM_AbstractTypeDeclaration", None)
        self.__DOM_AbstractTypeDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BodyDeclaration109"):
                    opp_val = getattr(item, "BodyDeclaration109", None)
                    
                    if opp_val == self:
                        setattr(item, "BodyDeclaration109", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BodyDeclaration109"):
                    opp_val = getattr(item, "BodyDeclaration109", None)
                    
                    setattr(item, "BodyDeclaration109", self)
                    

class DOM_MethodDeclaration(BodyDeclaration):

    def __init__(self, extraDimensions: str, constructor: str, varargs: str, DOM_MethodDeclaration: "Block" = None, DOM_MethodDeclaration137: "SimpleName" = None, DOM_MethodDeclaration140: "Type" = None, DOM_MethodDeclaration143: set["SingleVariableDeclaration"] = None, DOM_MethodDeclaration146: set["Name"] = None, DOM_MethodDeclaration149: set["TypeParameter"] = None, DOM_MethodDeclaration151: "IMethod" = None, BodyDeclaration109: "DOM_AbstractTypeDeclaration", BodyDeclaration: "DOM_AnonymousClassDeclaration"):
        self.extraDimensions = extraDimensions
        self.constructor = constructor
        self.varargs = varargs
        self.DOM_MethodDeclaration = DOM_MethodDeclaration
        self.DOM_MethodDeclaration137 = DOM_MethodDeclaration137
        self.DOM_MethodDeclaration140 = DOM_MethodDeclaration140
        self.DOM_MethodDeclaration143 = DOM_MethodDeclaration143 if DOM_MethodDeclaration143 is not None else set()
        self.DOM_MethodDeclaration146 = DOM_MethodDeclaration146 if DOM_MethodDeclaration146 is not None else set()
        self.DOM_MethodDeclaration149 = DOM_MethodDeclaration149 if DOM_MethodDeclaration149 is not None else set()
        self.DOM_MethodDeclaration151 = DOM_MethodDeclaration151
        
    @property
    def extraDimensions(self) -> str:
        return self.__extraDimensions

    @extraDimensions.setter
    def extraDimensions(self, extraDimensions: str):
        self.__extraDimensions = extraDimensions

    @property
    def constructor(self) -> str:
        return self.__constructor

    @constructor.setter
    def constructor(self, constructor: str):
        self.__constructor = constructor

    @property
    def varargs(self) -> str:
        return self.__varargs

    @varargs.setter
    def varargs(self, varargs: str):
        self.__varargs = varargs

    @property
    def DOM_MethodDeclaration146(self):
        return self.__DOM_MethodDeclaration146

    @DOM_MethodDeclaration146.setter
    def DOM_MethodDeclaration146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_MethodDeclaration__DOM_MethodDeclaration146", None)
        self.__DOM_MethodDeclaration146 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Name147"):
                    opp_val = getattr(item, "Name147", None)
                    
                    if opp_val == self:
                        setattr(item, "Name147", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Name147"):
                    opp_val = getattr(item, "Name147", None)
                    
                    setattr(item, "Name147", self)
                    

    @property
    def DOM_MethodDeclaration140(self):
        return self.__DOM_MethodDeclaration140

    @DOM_MethodDeclaration140.setter
    def DOM_MethodDeclaration140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_MethodDeclaration__DOM_MethodDeclaration140", None)
        self.__DOM_MethodDeclaration140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type141"):
                opp_val = getattr(old_value, "Type141", None)
                if opp_val == self:
                    setattr(old_value, "Type141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type141"):
                opp_val = getattr(value, "Type141", None)
                setattr(value, "Type141", self)

    @property
    def DOM_MethodDeclaration143(self):
        return self.__DOM_MethodDeclaration143

    @DOM_MethodDeclaration143.setter
    def DOM_MethodDeclaration143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_MethodDeclaration__DOM_MethodDeclaration143", None)
        self.__DOM_MethodDeclaration143 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SingleVariableDeclaration144"):
                    opp_val = getattr(item, "SingleVariableDeclaration144", None)
                    
                    if opp_val == self:
                        setattr(item, "SingleVariableDeclaration144", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SingleVariableDeclaration144"):
                    opp_val = getattr(item, "SingleVariableDeclaration144", None)
                    
                    setattr(item, "SingleVariableDeclaration144", self)
                    

    @property
    def DOM_MethodDeclaration149(self):
        return self.__DOM_MethodDeclaration149

    @DOM_MethodDeclaration149.setter
    def DOM_MethodDeclaration149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_MethodDeclaration__DOM_MethodDeclaration149", None)
        self.__DOM_MethodDeclaration149 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypeParameter"):
                    opp_val = getattr(item, "TypeParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "TypeParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypeParameter"):
                    opp_val = getattr(item, "TypeParameter", None)
                    
                    setattr(item, "TypeParameter", self)
                    

    @property
    def DOM_MethodDeclaration137(self):
        return self.__DOM_MethodDeclaration137

    @DOM_MethodDeclaration137.setter
    def DOM_MethodDeclaration137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_MethodDeclaration__DOM_MethodDeclaration137", None)
        self.__DOM_MethodDeclaration137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleName138"):
                opp_val = getattr(old_value, "SimpleName138", None)
                if opp_val == self:
                    setattr(old_value, "SimpleName138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleName138"):
                opp_val = getattr(value, "SimpleName138", None)
                setattr(value, "SimpleName138", self)

    @property
    def DOM_MethodDeclaration151(self):
        return self.__DOM_MethodDeclaration151

    @DOM_MethodDeclaration151.setter
    def DOM_MethodDeclaration151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_MethodDeclaration__DOM_MethodDeclaration151", None)
        self.__DOM_MethodDeclaration151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IMethod152"):
                opp_val = getattr(old_value, "IMethod152", None)
                if opp_val == self:
                    setattr(old_value, "IMethod152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IMethod152"):
                opp_val = getattr(value, "IMethod152", None)
                setattr(value, "IMethod152", self)

    @property
    def DOM_MethodDeclaration(self):
        return self.__DOM_MethodDeclaration

    @DOM_MethodDeclaration.setter
    def DOM_MethodDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_MethodDeclaration__DOM_MethodDeclaration", None)
        self.__DOM_MethodDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Block135"):
                opp_val = getattr(old_value, "Block135", None)
                if opp_val == self:
                    setattr(old_value, "Block135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Block135"):
                opp_val = getattr(value, "Block135", None)
                setattr(value, "Block135", self)

class DOM_ASTNode(ABC):

    pass
class ASTNode:

    pass
class DOM_MemberValuePair(ASTNode):

    pass
class DOM_AnonymousClassDeclaration(ASTNode):

    pass
class DOM_Statement(ASTNode):

    pass
class DOM_PackageDeclaration(ASTNode):

    pass
class DOM_CatchClause(ASTNode):

    pass
class DOM_TagElement(ASTNode):

    def __init__(self, tagName: str, nested: str, DOM_TagElement: set["ASTNode"] = None, ASTNode97: "DOM_TagElement", ASTNode: "DOM_AST", ASTNode57: "DOM_Comment"):
        self.tagName = tagName
        self.nested = nested
        self.DOM_TagElement = DOM_TagElement if DOM_TagElement is not None else set()
        
    @property
    def nested(self) -> str:
        return self.__nested

    @nested.setter
    def nested(self, nested: str):
        self.__nested = nested

    @property
    def tagName(self) -> str:
        return self.__tagName

    @tagName.setter
    def tagName(self, tagName: str):
        self.__tagName = tagName

    @property
    def DOM_TagElement(self):
        return self.__DOM_TagElement

    @DOM_TagElement.setter
    def DOM_TagElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_TagElement__DOM_TagElement", None)
        self.__DOM_TagElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ASTNode97"):
                    opp_val = getattr(item, "ASTNode97", None)
                    
                    if opp_val == self:
                        setattr(item, "ASTNode97", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ASTNode97"):
                    opp_val = getattr(item, "ASTNode97", None)
                    
                    setattr(item, "ASTNode97", self)
                    

class DOM_Modifier(ExtendedModifier, ASTNode):

    def __init__(self, final: str, abstract: str, native: str, none: str, private: str, protected: str, public: str, static: str, strictfp: str, synchronized: str, transient: str, volatile: str, ASTNode97: "DOM_TagElement", ASTNode: "DOM_AST", ASTNode57: "DOM_Comment", ExtendedModifier370: "DOM_VariableDeclarationStatement", ExtendedModifier: "DOM_BodyDeclaration", ExtendedModifier402: "DOM_SingleVariableDeclaration", ExtendedModifier275: "DOM_VariableDeclarationExpression"):
        self.final = final
        self.abstract = abstract
        self.native = native
        self.none = none
        self.private = private
        self.protected = protected
        self.public = public
        self.static = static
        self.strictfp = strictfp
        self.synchronized = synchronized
        self.transient = transient
        self.volatile = volatile
        
    @property
    def native(self) -> str:
        return self.__native

    @native.setter
    def native(self, native: str):
        self.__native = native

    @property
    def final(self) -> str:
        return self.__final

    @final.setter
    def final(self, final: str):
        self.__final = final

    @property
    def transient(self) -> str:
        return self.__transient

    @transient.setter
    def transient(self, transient: str):
        self.__transient = transient

    @property
    def static(self) -> str:
        return self.__static

    @static.setter
    def static(self, static: str):
        self.__static = static

    @property
    def abstract(self) -> str:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: str):
        self.__abstract = abstract

    @property
    def public(self) -> str:
        return self.__public

    @public.setter
    def public(self, public: str):
        self.__public = public

    @property
    def protected(self) -> str:
        return self.__protected

    @protected.setter
    def protected(self, protected: str):
        self.__protected = protected

    @property
    def synchronized(self) -> str:
        return self.__synchronized

    @synchronized.setter
    def synchronized(self, synchronized: str):
        self.__synchronized = synchronized

    @property
    def volatile(self) -> str:
        return self.__volatile

    @volatile.setter
    def volatile(self, volatile: str):
        self.__volatile = volatile

    @property
    def none(self) -> str:
        return self.__none

    @none.setter
    def none(self, none: str):
        self.__none = none

    @property
    def strictfp(self) -> str:
        return self.__strictfp

    @strictfp.setter
    def strictfp(self, strictfp: str):
        self.__strictfp = strictfp

    @property
    def private(self) -> str:
        return self.__private

    @private.setter
    def private(self, private: str):
        self.__private = private

class DOM_MethodRef(ASTNode):

    pass
class DOM_MemberRef(ASTNode):

    pass
class DOM_MethodRefParameter(ASTNode):

    def __init__(self, varargs: str, DOM_MethodRefParameter: "SimpleName" = None, DOM_MethodRefParameter86: "Type" = None, ASTNode97: "DOM_TagElement", ASTNode: "DOM_AST", ASTNode57: "DOM_Comment"):
        self.varargs = varargs
        self.DOM_MethodRefParameter = DOM_MethodRefParameter
        self.DOM_MethodRefParameter86 = DOM_MethodRefParameter86
        
    @property
    def varargs(self) -> str:
        return self.__varargs

    @varargs.setter
    def varargs(self, varargs: str):
        self.__varargs = varargs

    @property
    def DOM_MethodRefParameter(self):
        return self.__DOM_MethodRefParameter

    @DOM_MethodRefParameter.setter
    def DOM_MethodRefParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_MethodRefParameter__DOM_MethodRefParameter", None)
        self.__DOM_MethodRefParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleName84"):
                opp_val = getattr(old_value, "SimpleName84", None)
                if opp_val == self:
                    setattr(old_value, "SimpleName84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleName84"):
                opp_val = getattr(value, "SimpleName84", None)
                setattr(value, "SimpleName84", self)

    @property
    def DOM_MethodRefParameter86(self):
        return self.__DOM_MethodRefParameter86

    @DOM_MethodRefParameter86.setter
    def DOM_MethodRefParameter86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_MethodRefParameter__DOM_MethodRefParameter86", None)
        self.__DOM_MethodRefParameter86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type"):
                opp_val = getattr(old_value, "Type", None)
                if opp_val == self:
                    setattr(old_value, "Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type"):
                opp_val = getattr(value, "Type", None)
                setattr(value, "Type", self)

class DOM_Comment(ASTNode):

    pass
class DOM_TypeParameter(ASTNode):

    pass
class DOM_ImportDeclaration(ASTNode):

    def __init__(self, static: str, onDemand: str, DOM_ImportDeclaration: "Name" = None, ASTNode97: "DOM_TagElement", ASTNode: "DOM_AST", ASTNode57: "DOM_Comment"):
        self.static = static
        self.onDemand = onDemand
        self.DOM_ImportDeclaration = DOM_ImportDeclaration
        
    @property
    def static(self) -> str:
        return self.__static

    @static.setter
    def static(self, static: str):
        self.__static = static

    @property
    def onDemand(self) -> str:
        return self.__onDemand

    @onDemand.setter
    def onDemand(self, onDemand: str):
        self.__onDemand = onDemand

    @property
    def DOM_ImportDeclaration(self):
        return self.__DOM_ImportDeclaration

    @DOM_ImportDeclaration.setter
    def DOM_ImportDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_ImportDeclaration__DOM_ImportDeclaration", None)
        self.__DOM_ImportDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Name"):
                opp_val = getattr(old_value, "Name", None)
                if opp_val == self:
                    setattr(old_value, "Name", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Name"):
                opp_val = getattr(value, "Name", None)
                setattr(value, "Name", self)

class DOM_Type(ASTNode):

    pass
class DOM_VariableDeclaration(ASTNode):

    def __init__(self, extraDimensions: str, DOM_VariableDeclaration: "Expression" = None, DOM_VariableDeclaration106: "SimpleName" = None, ASTNode97: "DOM_TagElement", ASTNode: "DOM_AST", ASTNode57: "DOM_Comment"):
        self.extraDimensions = extraDimensions
        self.DOM_VariableDeclaration = DOM_VariableDeclaration
        self.DOM_VariableDeclaration106 = DOM_VariableDeclaration106
        
    @property
    def extraDimensions(self) -> str:
        return self.__extraDimensions

    @extraDimensions.setter
    def extraDimensions(self, extraDimensions: str):
        self.__extraDimensions = extraDimensions

    @property
    def DOM_VariableDeclaration(self):
        return self.__DOM_VariableDeclaration

    @DOM_VariableDeclaration.setter
    def DOM_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_VariableDeclaration__DOM_VariableDeclaration", None)
        self.__DOM_VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression104"):
                opp_val = getattr(old_value, "Expression104", None)
                if opp_val == self:
                    setattr(old_value, "Expression104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression104"):
                opp_val = getattr(value, "Expression104", None)
                setattr(value, "Expression104", self)

    @property
    def DOM_VariableDeclaration106(self):
        return self.__DOM_VariableDeclaration106

    @DOM_VariableDeclaration106.setter
    def DOM_VariableDeclaration106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_VariableDeclaration__DOM_VariableDeclaration106", None)
        self.__DOM_VariableDeclaration106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleName107"):
                opp_val = getattr(old_value, "SimpleName107", None)
                if opp_val == self:
                    setattr(old_value, "SimpleName107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleName107"):
                opp_val = getattr(value, "SimpleName107", None)
                setattr(value, "SimpleName107", self)

class DOM_CompilationUnit(ASTNode):

    pass
class DOM_TextElement(ASTNode):

    def __init__(self, text: str, ASTNode97: "DOM_TagElement", ASTNode: "DOM_AST", ASTNode57: "DOM_Comment"):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class DOM_Expression(ASTNode):

    def __init__(self, resolveBoxing: str, resolveUnboxing: str, DOM_Expression: "IType" = None, ASTNode97: "DOM_TagElement", ASTNode: "DOM_AST", ASTNode57: "DOM_Comment"):
        self.resolveBoxing = resolveBoxing
        self.resolveUnboxing = resolveUnboxing
        self.DOM_Expression = DOM_Expression
        
    @property
    def resolveBoxing(self) -> str:
        return self.__resolveBoxing

    @resolveBoxing.setter
    def resolveBoxing(self, resolveBoxing: str):
        self.__resolveBoxing = resolveBoxing

    @property
    def resolveUnboxing(self) -> str:
        return self.__resolveUnboxing

    @resolveUnboxing.setter
    def resolveUnboxing(self, resolveUnboxing: str):
        self.__resolveUnboxing = resolveUnboxing

    @property
    def DOM_Expression(self):
        return self.__DOM_Expression

    @DOM_Expression.setter
    def DOM_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_Expression__DOM_Expression", None)
        self.__DOM_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IType66"):
                opp_val = getattr(old_value, "IType66", None)
                if opp_val == self:
                    setattr(old_value, "IType66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IType66"):
                opp_val = getattr(value, "IType66", None)
                setattr(value, "IType66", self)

class DOM_AST:

    pass
class DOM_BodyDeclaration(ASTNode):

    pass
class Core_Parameter:

    def __init__(self, name: str, type: str, Core_Parameter: "PrimitiveTypes_Core_IMethod" = None):
        self.name = name
        self.type = type
        self.Core_Parameter = Core_Parameter
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Core_Parameter(self):
        return self.__Core_Parameter

    @Core_Parameter.setter
    def Core_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_Parameter__Core_Parameter", None)
        self.__Core_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PrimitiveTypes_Core_IMethod"):
                opp_val = getattr(old_value, "PrimitiveTypes_Core_IMethod", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PrimitiveTypes_Core_IMethod"):
                opp_val = getattr(value, "PrimitiveTypes_Core_IMethod", None)
                if opp_val is None:
                    setattr(value, "PrimitiveTypes_Core_IMethod", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Parameter:

    pass
class ITypeParameter:

    pass
class ISourceRange:

    pass
class IMethod:

    pass
class IField:

    pass
class IInitializer:

    pass
class IMember:

    pass
class Core_IInitializer(IMember):

    pass
class PrimitiveTypes_Core_IField(IMember):

    def __init__(self, constant: str, isEnumConstant: str, typeSignature: str, isVolatile: str, isTransient: str):
        self.constant = constant
        self.isEnumConstant = isEnumConstant
        self.typeSignature = typeSignature
        self.isVolatile = isVolatile
        self.isTransient = isTransient
        
    @property
    def isTransient(self) -> str:
        return self.__isTransient

    @isTransient.setter
    def isTransient(self, isTransient: str):
        self.__isTransient = isTransient

    @property
    def constant(self) -> str:
        return self.__constant

    @constant.setter
    def constant(self, constant: str):
        self.__constant = constant

    @property
    def typeSignature(self) -> str:
        return self.__typeSignature

    @typeSignature.setter
    def typeSignature(self, typeSignature: str):
        self.__typeSignature = typeSignature

    @property
    def isEnumConstant(self) -> str:
        return self.__isEnumConstant

    @isEnumConstant.setter
    def isEnumConstant(self, isEnumConstant: str):
        self.__isEnumConstant = isEnumConstant

    @property
    def isVolatile(self) -> str:
        return self.__isVolatile

    @isVolatile.setter
    def isVolatile(self, isVolatile: str):
        self.__isVolatile = isVolatile

class PrimitiveTypes_Core_IMethod(IMember):

    def __init__(self, returnType: str, isConstructor: str, isMainMethod: str, exceptionTypes: str, PrimitiveTypes_Core_IMethod: set["Core_Parameter"] = None):
        self.returnType = returnType
        self.isConstructor = isConstructor
        self.isMainMethod = isMainMethod
        self.exceptionTypes = exceptionTypes
        self.PrimitiveTypes_Core_IMethod = PrimitiveTypes_Core_IMethod if PrimitiveTypes_Core_IMethod is not None else set()
        
    @property
    def isConstructor(self) -> str:
        return self.__isConstructor

    @isConstructor.setter
    def isConstructor(self, isConstructor: str):
        self.__isConstructor = isConstructor

    @property
    def exceptionTypes(self) -> str:
        return self.__exceptionTypes

    @exceptionTypes.setter
    def exceptionTypes(self, exceptionTypes: str):
        self.__exceptionTypes = exceptionTypes

    @property
    def isMainMethod(self) -> str:
        return self.__isMainMethod

    @isMainMethod.setter
    def isMainMethod(self, isMainMethod: str):
        self.__isMainMethod = isMainMethod

    @property
    def returnType(self) -> str:
        return self.__returnType

    @returnType.setter
    def returnType(self, returnType: str):
        self.__returnType = returnType

    @property
    def PrimitiveTypes_Core_IMethod(self):
        return self.__PrimitiveTypes_Core_IMethod

    @PrimitiveTypes_Core_IMethod.setter
    def PrimitiveTypes_Core_IMethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PrimitiveTypes_Core_IMethod__PrimitiveTypes_Core_IMethod", None)
        self.__PrimitiveTypes_Core_IMethod = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Core_Parameter"):
                    opp_val = getattr(item, "Core_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "Core_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Core_Parameter"):
                    opp_val = getattr(item, "Core_Parameter", None)
                    
                    setattr(item, "Core_Parameter", self)
                    

class PrimitiveTypes_Core_IInitializer(IMember):

    pass
class Core_IMethod(IMember):

    def __init__(self, returnType: str, isConstructor: str, isMainMethod: str, exceptionTypes: str, Core_IMethod: set["Parameter"] = None, Core_IMethod459: "PrimitiveTypes_Core_IType" = None):
        self.returnType = returnType
        self.isConstructor = isConstructor
        self.isMainMethod = isMainMethod
        self.exceptionTypes = exceptionTypes
        self.Core_IMethod = Core_IMethod if Core_IMethod is not None else set()
        self.Core_IMethod459 = Core_IMethod459
        
    @property
    def exceptionTypes(self) -> str:
        return self.__exceptionTypes

    @exceptionTypes.setter
    def exceptionTypes(self, exceptionTypes: str):
        self.__exceptionTypes = exceptionTypes

    @property
    def isMainMethod(self) -> str:
        return self.__isMainMethod

    @isMainMethod.setter
    def isMainMethod(self, isMainMethod: str):
        self.__isMainMethod = isMainMethod

    @property
    def returnType(self) -> str:
        return self.__returnType

    @returnType.setter
    def returnType(self, returnType: str):
        self.__returnType = returnType

    @property
    def isConstructor(self) -> str:
        return self.__isConstructor

    @isConstructor.setter
    def isConstructor(self, isConstructor: str):
        self.__isConstructor = isConstructor

    @property
    def Core_IMethod(self):
        return self.__Core_IMethod

    @Core_IMethod.setter
    def Core_IMethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IMethod__Core_IMethod", None)
        self.__Core_IMethod = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    setattr(item, "Parameter", self)
                    

    @property
    def Core_IMethod459(self):
        return self.__Core_IMethod459

    @Core_IMethod459.setter
    def Core_IMethod459(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IMethod__Core_IMethod459", None)
        self.__Core_IMethod459 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PrimitiveTypes_Core_IType458"):
                opp_val = getattr(old_value, "PrimitiveTypes_Core_IType458", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PrimitiveTypes_Core_IType458"):
                opp_val = getattr(value, "PrimitiveTypes_Core_IType458", None)
                if opp_val is None:
                    setattr(value, "PrimitiveTypes_Core_IType458", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Core_IField(IMember):

    def __init__(self, constant: str, isEnumConstant: str, typeSignature: str, isVolatile: str, isTransient: str, Core_IField: "PrimitiveTypes_Core_IType" = None):
        self.constant = constant
        self.isEnumConstant = isEnumConstant
        self.typeSignature = typeSignature
        self.isVolatile = isVolatile
        self.isTransient = isTransient
        self.Core_IField = Core_IField
        
    @property
    def typeSignature(self) -> str:
        return self.__typeSignature

    @typeSignature.setter
    def typeSignature(self, typeSignature: str):
        self.__typeSignature = typeSignature

    @property
    def isTransient(self) -> str:
        return self.__isTransient

    @isTransient.setter
    def isTransient(self, isTransient: str):
        self.__isTransient = isTransient

    @property
    def isEnumConstant(self) -> str:
        return self.__isEnumConstant

    @isEnumConstant.setter
    def isEnumConstant(self, isEnumConstant: str):
        self.__isEnumConstant = isEnumConstant

    @property
    def isVolatile(self) -> str:
        return self.__isVolatile

    @isVolatile.setter
    def isVolatile(self, isVolatile: str):
        self.__isVolatile = isVolatile

    @property
    def constant(self) -> str:
        return self.__constant

    @constant.setter
    def constant(self, constant: str):
        self.__constant = constant

    @property
    def Core_IField(self):
        return self.__Core_IField

    @Core_IField.setter
    def Core_IField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IField__Core_IField", None)
        self.__Core_IField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PrimitiveTypes_Core_IType456"):
                opp_val = getattr(old_value, "PrimitiveTypes_Core_IType456", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PrimitiveTypes_Core_IType456"):
                opp_val = getattr(value, "PrimitiveTypes_Core_IType456", None)
                if opp_val is None:
                    setattr(value, "PrimitiveTypes_Core_IType456", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PrimitiveTypes_Core_IType(IMember):

    def __init__(self, fullyQualifiedName: str, fullyQualifiedParametrizedName: str, PrimitiveTypes_Core_IType464: set["Core_ITypeParameter"] = None, PrimitiveTypes_Core_IType: set["Core_IInitializer"] = None, PrimitiveTypes_Core_IType456: set["Core_IField"] = None, PrimitiveTypes_Core_IType458: set["Core_IMethod"] = None, PrimitiveTypes_Core_IType461: set["Core_IType"] = None):
        self.fullyQualifiedName = fullyQualifiedName
        self.fullyQualifiedParametrizedName = fullyQualifiedParametrizedName
        self.PrimitiveTypes_Core_IType464 = PrimitiveTypes_Core_IType464 if PrimitiveTypes_Core_IType464 is not None else set()
        self.PrimitiveTypes_Core_IType = PrimitiveTypes_Core_IType if PrimitiveTypes_Core_IType is not None else set()
        self.PrimitiveTypes_Core_IType456 = PrimitiveTypes_Core_IType456 if PrimitiveTypes_Core_IType456 is not None else set()
        self.PrimitiveTypes_Core_IType458 = PrimitiveTypes_Core_IType458 if PrimitiveTypes_Core_IType458 is not None else set()
        self.PrimitiveTypes_Core_IType461 = PrimitiveTypes_Core_IType461 if PrimitiveTypes_Core_IType461 is not None else set()
        
    @property
    def fullyQualifiedName(self) -> str:
        return self.__fullyQualifiedName

    @fullyQualifiedName.setter
    def fullyQualifiedName(self, fullyQualifiedName: str):
        self.__fullyQualifiedName = fullyQualifiedName

    @property
    def fullyQualifiedParametrizedName(self) -> str:
        return self.__fullyQualifiedParametrizedName

    @fullyQualifiedParametrizedName.setter
    def fullyQualifiedParametrizedName(self, fullyQualifiedParametrizedName: str):
        self.__fullyQualifiedParametrizedName = fullyQualifiedParametrizedName

    @property
    def PrimitiveTypes_Core_IType458(self):
        return self.__PrimitiveTypes_Core_IType458

    @PrimitiveTypes_Core_IType458.setter
    def PrimitiveTypes_Core_IType458(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PrimitiveTypes_Core_IType__PrimitiveTypes_Core_IType458", None)
        self.__PrimitiveTypes_Core_IType458 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Core_IMethod459"):
                    opp_val = getattr(item, "Core_IMethod459", None)
                    
                    if opp_val == self:
                        setattr(item, "Core_IMethod459", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Core_IMethod459"):
                    opp_val = getattr(item, "Core_IMethod459", None)
                    
                    setattr(item, "Core_IMethod459", self)
                    

    @property
    def PrimitiveTypes_Core_IType456(self):
        return self.__PrimitiveTypes_Core_IType456

    @PrimitiveTypes_Core_IType456.setter
    def PrimitiveTypes_Core_IType456(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PrimitiveTypes_Core_IType__PrimitiveTypes_Core_IType456", None)
        self.__PrimitiveTypes_Core_IType456 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Core_IField"):
                    opp_val = getattr(item, "Core_IField", None)
                    
                    if opp_val == self:
                        setattr(item, "Core_IField", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Core_IField"):
                    opp_val = getattr(item, "Core_IField", None)
                    
                    setattr(item, "Core_IField", self)
                    

    @property
    def PrimitiveTypes_Core_IType464(self):
        return self.__PrimitiveTypes_Core_IType464

    @PrimitiveTypes_Core_IType464.setter
    def PrimitiveTypes_Core_IType464(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PrimitiveTypes_Core_IType__PrimitiveTypes_Core_IType464", None)
        self.__PrimitiveTypes_Core_IType464 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Core_ITypeParameter"):
                    opp_val = getattr(item, "Core_ITypeParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "Core_ITypeParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Core_ITypeParameter"):
                    opp_val = getattr(item, "Core_ITypeParameter", None)
                    
                    setattr(item, "Core_ITypeParameter", self)
                    

    @property
    def PrimitiveTypes_Core_IType(self):
        return self.__PrimitiveTypes_Core_IType

    @PrimitiveTypes_Core_IType.setter
    def PrimitiveTypes_Core_IType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PrimitiveTypes_Core_IType__PrimitiveTypes_Core_IType", None)
        self.__PrimitiveTypes_Core_IType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Core_IInitializer"):
                    opp_val = getattr(item, "Core_IInitializer", None)
                    
                    if opp_val == self:
                        setattr(item, "Core_IInitializer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Core_IInitializer"):
                    opp_val = getattr(item, "Core_IInitializer", None)
                    
                    setattr(item, "Core_IInitializer", self)
                    

    @property
    def PrimitiveTypes_Core_IType461(self):
        return self.__PrimitiveTypes_Core_IType461

    @PrimitiveTypes_Core_IType461.setter
    def PrimitiveTypes_Core_IType461(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PrimitiveTypes_Core_IType__PrimitiveTypes_Core_IType461", None)
        self.__PrimitiveTypes_Core_IType461 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Core_IType462"):
                    opp_val = getattr(item, "Core_IType462", None)
                    
                    if opp_val == self:
                        setattr(item, "Core_IType462", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Core_IType462"):
                    opp_val = getattr(item, "Core_IType462", None)
                    
                    setattr(item, "Core_IType462", self)
                    

class Core_IType(IMember):

    def __init__(self, fullyQualifiedName: str, fullyQualifiedParametrizedName: str, Core_IType: set["IInitializer"] = None, Core_IType39: set["IField"] = None, Core_IType43: set["IType"] = None, Core_IType46: set["ITypeParameter"] = None, Core_IType41: set["IMethod"] = None, Core_IType434: "PrimitiveTypes_Core_ICompilationUnit" = None, Core_IType439: "PrimitiveTypes_Core_ICompilationUnit" = None, Core_IType447: "PrimitiveTypes_Core_IClassFile" = None, Core_IType462: "PrimitiveTypes_Core_IType" = None):
        self.fullyQualifiedName = fullyQualifiedName
        self.fullyQualifiedParametrizedName = fullyQualifiedParametrizedName
        self.Core_IType = Core_IType if Core_IType is not None else set()
        self.Core_IType39 = Core_IType39 if Core_IType39 is not None else set()
        self.Core_IType43 = Core_IType43 if Core_IType43 is not None else set()
        self.Core_IType46 = Core_IType46 if Core_IType46 is not None else set()
        self.Core_IType41 = Core_IType41 if Core_IType41 is not None else set()
        self.Core_IType434 = Core_IType434
        self.Core_IType439 = Core_IType439
        self.Core_IType447 = Core_IType447
        self.Core_IType462 = Core_IType462
        
    @property
    def fullyQualifiedName(self) -> str:
        return self.__fullyQualifiedName

    @fullyQualifiedName.setter
    def fullyQualifiedName(self, fullyQualifiedName: str):
        self.__fullyQualifiedName = fullyQualifiedName

    @property
    def fullyQualifiedParametrizedName(self) -> str:
        return self.__fullyQualifiedParametrizedName

    @fullyQualifiedParametrizedName.setter
    def fullyQualifiedParametrizedName(self, fullyQualifiedParametrizedName: str):
        self.__fullyQualifiedParametrizedName = fullyQualifiedParametrizedName

    @property
    def Core_IType46(self):
        return self.__Core_IType46

    @Core_IType46.setter
    def Core_IType46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IType__Core_IType46", None)
        self.__Core_IType46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ITypeParameter"):
                    opp_val = getattr(item, "ITypeParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "ITypeParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ITypeParameter"):
                    opp_val = getattr(item, "ITypeParameter", None)
                    
                    setattr(item, "ITypeParameter", self)
                    

    @property
    def Core_IType39(self):
        return self.__Core_IType39

    @Core_IType39.setter
    def Core_IType39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IType__Core_IType39", None)
        self.__Core_IType39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "IField"):
                    opp_val = getattr(item, "IField", None)
                    
                    if opp_val == self:
                        setattr(item, "IField", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IField"):
                    opp_val = getattr(item, "IField", None)
                    
                    setattr(item, "IField", self)
                    

    @property
    def Core_IType439(self):
        return self.__Core_IType439

    @Core_IType439.setter
    def Core_IType439(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IType__Core_IType439", None)
        self.__Core_IType439 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PrimitiveTypes_Core_ICompilationUnit438"):
                opp_val = getattr(old_value, "PrimitiveTypes_Core_ICompilationUnit438", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PrimitiveTypes_Core_ICompilationUnit438"):
                opp_val = getattr(value, "PrimitiveTypes_Core_ICompilationUnit438", None)
                if opp_val is None:
                    setattr(value, "PrimitiveTypes_Core_ICompilationUnit438", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Core_IType434(self):
        return self.__Core_IType434

    @Core_IType434.setter
    def Core_IType434(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IType__Core_IType434", None)
        self.__Core_IType434 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PrimitiveTypes_Core_ICompilationUnit"):
                opp_val = getattr(old_value, "PrimitiveTypes_Core_ICompilationUnit", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PrimitiveTypes_Core_ICompilationUnit"):
                opp_val = getattr(value, "PrimitiveTypes_Core_ICompilationUnit", None)
                if opp_val is None:
                    setattr(value, "PrimitiveTypes_Core_ICompilationUnit", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Core_IType43(self):
        return self.__Core_IType43

    @Core_IType43.setter
    def Core_IType43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IType__Core_IType43", None)
        self.__Core_IType43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "IType44"):
                    opp_val = getattr(item, "IType44", None)
                    
                    if opp_val == self:
                        setattr(item, "IType44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IType44"):
                    opp_val = getattr(item, "IType44", None)
                    
                    setattr(item, "IType44", self)
                    

    @property
    def Core_IType447(self):
        return self.__Core_IType447

    @Core_IType447.setter
    def Core_IType447(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IType__Core_IType447", None)
        self.__Core_IType447 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PrimitiveTypes_Core_IClassFile"):
                opp_val = getattr(old_value, "PrimitiveTypes_Core_IClassFile", None)
                if opp_val == self:
                    setattr(old_value, "PrimitiveTypes_Core_IClassFile", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PrimitiveTypes_Core_IClassFile"):
                opp_val = getattr(value, "PrimitiveTypes_Core_IClassFile", None)
                setattr(value, "PrimitiveTypes_Core_IClassFile", self)

    @property
    def Core_IType41(self):
        return self.__Core_IType41

    @Core_IType41.setter
    def Core_IType41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IType__Core_IType41", None)
        self.__Core_IType41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "IMethod"):
                    opp_val = getattr(item, "IMethod", None)
                    
                    if opp_val == self:
                        setattr(item, "IMethod", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IMethod"):
                    opp_val = getattr(item, "IMethod", None)
                    
                    setattr(item, "IMethod", self)
                    

    @property
    def Core_IType462(self):
        return self.__Core_IType462

    @Core_IType462.setter
    def Core_IType462(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IType__Core_IType462", None)
        self.__Core_IType462 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PrimitiveTypes_Core_IType461"):
                opp_val = getattr(old_value, "PrimitiveTypes_Core_IType461", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PrimitiveTypes_Core_IType461"):
                opp_val = getattr(value, "PrimitiveTypes_Core_IType461", None)
                if opp_val is None:
                    setattr(value, "PrimitiveTypes_Core_IType461", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Core_IType(self):
        return self.__Core_IType

    @Core_IType.setter
    def Core_IType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IType__Core_IType", None)
        self.__Core_IType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "IInitializer"):
                    opp_val = getattr(item, "IInitializer", None)
                    
                    if opp_val == self:
                        setattr(item, "IInitializer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IInitializer"):
                    opp_val = getattr(item, "IInitializer", None)
                    
                    setattr(item, "IInitializer", self)
                    

class Core_ISourceRange:

    def __init__(self, length: str, offset: str, Core_ISourceRange: "PrimitiveTypes_Core_ISourceReference" = None, Core_ISourceRange450: "PrimitiveTypes_Core_IMember" = None, Core_ISourceRange453: "PrimitiveTypes_Core_IMember" = None):
        self.length = length
        self.offset = offset
        self.Core_ISourceRange = Core_ISourceRange
        self.Core_ISourceRange450 = Core_ISourceRange450
        self.Core_ISourceRange453 = Core_ISourceRange453
        
    @property
    def offset(self) -> str:
        return self.__offset

    @offset.setter
    def offset(self, offset: str):
        self.__offset = offset

    @property
    def length(self) -> str:
        return self.__length

    @length.setter
    def length(self, length: str):
        self.__length = length

    @property
    def Core_ISourceRange(self):
        return self.__Core_ISourceRange

    @Core_ISourceRange.setter
    def Core_ISourceRange(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_ISourceRange__Core_ISourceRange", None)
        self.__Core_ISourceRange = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PrimitiveTypes_Core_ISourceReference"):
                opp_val = getattr(old_value, "PrimitiveTypes_Core_ISourceReference", None)
                if opp_val == self:
                    setattr(old_value, "PrimitiveTypes_Core_ISourceReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PrimitiveTypes_Core_ISourceReference"):
                opp_val = getattr(value, "PrimitiveTypes_Core_ISourceReference", None)
                setattr(value, "PrimitiveTypes_Core_ISourceReference", self)

    @property
    def Core_ISourceRange453(self):
        return self.__Core_ISourceRange453

    @Core_ISourceRange453.setter
    def Core_ISourceRange453(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_ISourceRange__Core_ISourceRange453", None)
        self.__Core_ISourceRange453 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PrimitiveTypes_Core_IMember452"):
                opp_val = getattr(old_value, "PrimitiveTypes_Core_IMember452", None)
                if opp_val == self:
                    setattr(old_value, "PrimitiveTypes_Core_IMember452", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PrimitiveTypes_Core_IMember452"):
                opp_val = getattr(value, "PrimitiveTypes_Core_IMember452", None)
                setattr(value, "PrimitiveTypes_Core_IMember452", self)

    @property
    def Core_ISourceRange450(self):
        return self.__Core_ISourceRange450

    @Core_ISourceRange450.setter
    def Core_ISourceRange450(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_ISourceRange__Core_ISourceRange450", None)
        self.__Core_ISourceRange450 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PrimitiveTypes_Core_IMember"):
                opp_val = getattr(old_value, "PrimitiveTypes_Core_IMember", None)
                if opp_val == self:
                    setattr(old_value, "PrimitiveTypes_Core_IMember", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PrimitiveTypes_Core_IMember"):
                opp_val = getattr(value, "PrimitiveTypes_Core_IMember", None)
                setattr(value, "PrimitiveTypes_Core_IMember", self)

class Core_ISourceReference(ABC):

    def __init__(self, source: str, Core_ISourceReference: "ISourceRange" = None):
        self.source = source
        self.Core_ISourceReference = Core_ISourceReference
        
    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def Core_ISourceReference(self):
        return self.__Core_ISourceReference

    @Core_ISourceReference.setter
    def Core_ISourceReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_ISourceReference__Core_ISourceReference", None)
        self.__Core_ISourceReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ISourceRange"):
                opp_val = getattr(old_value, "ISourceRange", None)
                if opp_val == self:
                    setattr(old_value, "ISourceRange", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ISourceRange"):
                opp_val = getattr(value, "ISourceRange", None)
                setattr(value, "ISourceRange", self)

class CompilationUnit:

    pass
class IImportDeclaration:

    pass
class IType:

    pass
class ITypeRoot:

    pass
class PrimitiveTypes_Core_IClassFile(ITypeRoot):

    def __init__(self, isClass: str, isInterface: str, PrimitiveTypes_Core_IClassFile: "Core_IType" = None):
        self.isClass = isClass
        self.isInterface = isInterface
        self.PrimitiveTypes_Core_IClassFile = PrimitiveTypes_Core_IClassFile
        
    @property
    def isInterface(self) -> str:
        return self.__isInterface

    @isInterface.setter
    def isInterface(self, isInterface: str):
        self.__isInterface = isInterface

    @property
    def isClass(self) -> str:
        return self.__isClass

    @isClass.setter
    def isClass(self, isClass: str):
        self.__isClass = isClass

    @property
    def PrimitiveTypes_Core_IClassFile(self):
        return self.__PrimitiveTypes_Core_IClassFile

    @PrimitiveTypes_Core_IClassFile.setter
    def PrimitiveTypes_Core_IClassFile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PrimitiveTypes_Core_IClassFile__PrimitiveTypes_Core_IClassFile", None)
        self.__PrimitiveTypes_Core_IClassFile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Core_IType447"):
                opp_val = getattr(old_value, "Core_IType447", None)
                if opp_val == self:
                    setattr(old_value, "Core_IType447", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Core_IType447"):
                opp_val = getattr(value, "Core_IType447", None)
                setattr(value, "Core_IType447", self)

class PrimitiveTypes_Core_ICompilationUnit(ITypeRoot):

    pass
class Core_IClassFile(ITypeRoot):

    def __init__(self, isClass: str, isInterface: str, Core_IClassFile: "IType" = None, Core_IClassFile429: "PrimitiveTypes_Core_IPackageFragment" = None):
        self.isClass = isClass
        self.isInterface = isInterface
        self.Core_IClassFile = Core_IClassFile
        self.Core_IClassFile429 = Core_IClassFile429
        
    @property
    def isInterface(self) -> str:
        return self.__isInterface

    @isInterface.setter
    def isInterface(self, isInterface: str):
        self.__isInterface = isInterface

    @property
    def isClass(self) -> str:
        return self.__isClass

    @isClass.setter
    def isClass(self, isClass: str):
        self.__isClass = isClass

    @property
    def Core_IClassFile(self):
        return self.__Core_IClassFile

    @Core_IClassFile.setter
    def Core_IClassFile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IClassFile__Core_IClassFile", None)
        self.__Core_IClassFile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IType30"):
                opp_val = getattr(old_value, "IType30", None)
                if opp_val == self:
                    setattr(old_value, "IType30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IType30"):
                opp_val = getattr(value, "IType30", None)
                setattr(value, "IType30", self)

    @property
    def Core_IClassFile429(self):
        return self.__Core_IClassFile429

    @Core_IClassFile429.setter
    def Core_IClassFile429(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IClassFile__Core_IClassFile429", None)
        self.__Core_IClassFile429 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PrimitiveTypes_Core_IPackageFragment"):
                opp_val = getattr(old_value, "PrimitiveTypes_Core_IPackageFragment", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PrimitiveTypes_Core_IPackageFragment"):
                opp_val = getattr(value, "PrimitiveTypes_Core_IPackageFragment", None)
                if opp_val is None:
                    setattr(value, "PrimitiveTypes_Core_IPackageFragment", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Core_ICompilationUnit(ITypeRoot):

    pass
class ISourceReference:

    pass
class IClassFile:

    pass
class ICompilationUnit:

    pass
class IPackageFragment:

    pass
class IJavaElement:

    pass
class Core_IImportDeclaration(IJavaElement, ISourceReference):

    def __init__(self, isOnDemand: str, isStatic: str, Core_IImportDeclaration: "PrimitiveTypes_Core_ICompilationUnit" = None):
        self.isOnDemand = isOnDemand
        self.isStatic = isStatic
        self.Core_IImportDeclaration = Core_IImportDeclaration
        
    @property
    def isStatic(self) -> str:
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: str):
        self.__isStatic = isStatic

    @property
    def isOnDemand(self) -> str:
        return self.__isOnDemand

    @isOnDemand.setter
    def isOnDemand(self, isOnDemand: str):
        self.__isOnDemand = isOnDemand

    @property
    def Core_IImportDeclaration(self):
        return self.__Core_IImportDeclaration

    @Core_IImportDeclaration.setter
    def Core_IImportDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IImportDeclaration__Core_IImportDeclaration", None)
        self.__Core_IImportDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PrimitiveTypes_Core_ICompilationUnit436"):
                opp_val = getattr(old_value, "PrimitiveTypes_Core_ICompilationUnit436", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PrimitiveTypes_Core_ICompilationUnit436"):
                opp_val = getattr(value, "PrimitiveTypes_Core_ICompilationUnit436", None)
                if opp_val is None:
                    setattr(value, "PrimitiveTypes_Core_ICompilationUnit436", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Core_IMember(IJavaElement, ISourceReference):

    pass
class Core_ITypeParameter(IJavaElement, ISourceReference):

    def __init__(self, bounds: str, Core_ITypeParameter: "PrimitiveTypes_Core_IType" = None):
        self.bounds = bounds
        self.Core_ITypeParameter = Core_ITypeParameter
        
    @property
    def bounds(self) -> str:
        return self.__bounds

    @bounds.setter
    def bounds(self, bounds: str):
        self.__bounds = bounds

    @property
    def Core_ITypeParameter(self):
        return self.__Core_ITypeParameter

    @Core_ITypeParameter.setter
    def Core_ITypeParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_ITypeParameter__Core_ITypeParameter", None)
        self.__Core_ITypeParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PrimitiveTypes_Core_IType464"):
                opp_val = getattr(old_value, "PrimitiveTypes_Core_IType464", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PrimitiveTypes_Core_IType464"):
                opp_val = getattr(value, "PrimitiveTypes_Core_IType464", None)
                if opp_val is None:
                    setattr(value, "PrimitiveTypes_Core_IType464", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class IPackageFragmentRoot:

    pass
class Core_BinaryPackageFragmentRoot(IPackageFragmentRoot):

    pass
class PrimitiveTypes_Core_SourcePackageFragmentRoot(IPackageFragmentRoot):

    pass
class Core_SourcePackageFragmentRoot(IPackageFragmentRoot):

    pass
class PrimitiveTypes_Core_BinaryPackageFragmentRoot(IPackageFragmentRoot):

    pass
class IJavaProject:

    pass
class PhysicalElement:

    pass
class Core_IJavaProject(PhysicalElement, IJavaElement):

    pass
class Core_ITypeRoot(PhysicalElement, IJavaElement, ISourceReference):

    pass
class Core_IPackageFragmentRoot(PhysicalElement, IJavaElement):

    pass
class PrimitiveTypes_Core_IJavaModel(PhysicalElement):

    pass
class Core_IPackageFragment(PhysicalElement, IJavaElement):

    def __init__(self, isDefaultPackage: str, 013: "IPackageFragmentRoot" = None, Core_IPackageFragment17: set["ICompilationUnit"] = None, Core_IPackageFragment: set["IClassFile"] = None, #424: "PrimitiveTypes_Core_IPackageFragmentRoot" = None):
        self.isDefaultPackage = isDefaultPackage
        self.013 = 013
        self.Core_IPackageFragment17 = Core_IPackageFragment17 if Core_IPackageFragment17 is not None else set()
        self.Core_IPackageFragment = Core_IPackageFragment if Core_IPackageFragment is not None else set()
        self.#424 = #424
        
    @property
    def isDefaultPackage(self) -> str:
        return self.__isDefaultPackage

    @isDefaultPackage.setter
    def isDefaultPackage(self, isDefaultPackage: str):
        self.__isDefaultPackage = isDefaultPackage

    @property
    def Core_IPackageFragment(self):
        return self.__Core_IPackageFragment

    @Core_IPackageFragment.setter
    def Core_IPackageFragment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IPackageFragment__Core_IPackageFragment", None)
        self.__Core_IPackageFragment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "IClassFile"):
                    opp_val = getattr(item, "IClassFile", None)
                    
                    if opp_val == self:
                        setattr(item, "IClassFile", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IClassFile"):
                    opp_val = getattr(item, "IClassFile", None)
                    
                    setattr(item, "IClassFile", self)
                    

    @property
    def Core_IPackageFragment17(self):
        return self.__Core_IPackageFragment17

    @Core_IPackageFragment17.setter
    def Core_IPackageFragment17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IPackageFragment__Core_IPackageFragment17", None)
        self.__Core_IPackageFragment17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ICompilationUnit"):
                    opp_val = getattr(item, "ICompilationUnit", None)
                    
                    if opp_val == self:
                        setattr(item, "ICompilationUnit", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ICompilationUnit"):
                    opp_val = getattr(item, "ICompilationUnit", None)
                    
                    setattr(item, "ICompilationUnit", self)
                    

    @property
    def #424(self):
        return self.__#424

    @#424.setter
    def #424(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IPackageFragment__#424", None)
        self.__#424 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "2"):
                opp_val = getattr(old_value, "2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "2"):
                opp_val = getattr(value, "2", None)
                if opp_val is None:
                    setattr(value, "2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 013(self):
        return self.__013

    @013.setter
    def 013(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IPackageFragment__013", None)
        self.__013 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#14"):
                opp_val = getattr(old_value, "#14", None)
                if opp_val == self:
                    setattr(old_value, "#14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#14"):
                opp_val = getattr(value, "#14", None)
                setattr(value, "#14", self)

class Core_IJavaModel(PhysicalElement):

    pass
class Core_PhysicalElement(ABC):

    def __init__(self, path: str, isReadOnly: str):
        self.path = path
        self.isReadOnly = isReadOnly
        
    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def isReadOnly(self) -> str:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: str):
        self.__isReadOnly = isReadOnly

class Core_IJavaElement(ABC):

    def __init__(self, elementName: str):
        self.elementName = elementName
        
    @property
    def elementName(self) -> str:
        return self.__elementName

    @elementName.setter
    def elementName(self, elementName: str):
        self.__elementName = elementName

class PrimitiveTypes_Core_IImportDeclaration(Core_IJavaElement, Core_ISourceReference):

    def __init__(self, elementName: str, source: str, isOnDemand: str, isStatic: str, Core_ISourceReference: "ISourceRange"):
        super().__init__(elementName, source, Core_ISourceReference)
        self.isOnDemand = isOnDemand
        self.isStatic = isStatic
        
    @property
    def isOnDemand(self) -> str:
        return self.__isOnDemand

    @isOnDemand.setter
    def isOnDemand(self, isOnDemand: str):
        self.__isOnDemand = isOnDemand

    @property
    def isStatic(self) -> str:
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: str):
        self.__isStatic = isStatic

class PrimitiveTypes_Core_IPackageFragmentRoot(Core_IJavaElement, Core_PhysicalElement):

    def __init__(self, elementName: str, path: str, isReadOnly: str, 2: set["Core_IPackageFragment"] = None):
        super().__init__(elementName, path, isReadOnly)
        self.2 = 2 if 2 is not None else set()
        
    @property
    def 2(self):
        return self.__2

    @2.setter
    def 2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PrimitiveTypes_Core_IPackageFragmentRoot__2", None)
        self.__2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#424"):
                    opp_val = getattr(item, "#424", None)
                    
                    if opp_val == self:
                        setattr(item, "#424", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#424"):
                    opp_val = getattr(item, "#424", None)
                    
                    setattr(item, "#424", self)
                    

class PrimitiveTypes_Core_IJavaProject(Core_IJavaElement, Core_PhysicalElement):

    def __init__(self, elementName: str, path: str, isReadOnly: str, PrimitiveTypes_Core_IJavaProject: set["Core_IPackageFragmentRoot"] = None, PrimitiveTypes_Core_IJavaProject418: set["Core_IPackageFragmentRoot"] = None, PrimitiveTypes_Core_IJavaProject421: set["Core_IJavaProject"] = None):
        super().__init__(elementName, path, isReadOnly)
        self.PrimitiveTypes_Core_IJavaProject = PrimitiveTypes_Core_IJavaProject if PrimitiveTypes_Core_IJavaProject is not None else set()
        self.PrimitiveTypes_Core_IJavaProject418 = PrimitiveTypes_Core_IJavaProject418 if PrimitiveTypes_Core_IJavaProject418 is not None else set()
        self.PrimitiveTypes_Core_IJavaProject421 = PrimitiveTypes_Core_IJavaProject421 if PrimitiveTypes_Core_IJavaProject421 is not None else set()
        
    @property
    def PrimitiveTypes_Core_IJavaProject418(self):
        return self.__PrimitiveTypes_Core_IJavaProject418

    @PrimitiveTypes_Core_IJavaProject418.setter
    def PrimitiveTypes_Core_IJavaProject418(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PrimitiveTypes_Core_IJavaProject__PrimitiveTypes_Core_IJavaProject418", None)
        self.__PrimitiveTypes_Core_IJavaProject418 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Core_IPackageFragmentRoot419"):
                    opp_val = getattr(item, "Core_IPackageFragmentRoot419", None)
                    
                    if opp_val == self:
                        setattr(item, "Core_IPackageFragmentRoot419", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Core_IPackageFragmentRoot419"):
                    opp_val = getattr(item, "Core_IPackageFragmentRoot419", None)
                    
                    setattr(item, "Core_IPackageFragmentRoot419", self)
                    

    @property
    def PrimitiveTypes_Core_IJavaProject421(self):
        return self.__PrimitiveTypes_Core_IJavaProject421

    @PrimitiveTypes_Core_IJavaProject421.setter
    def PrimitiveTypes_Core_IJavaProject421(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PrimitiveTypes_Core_IJavaProject__PrimitiveTypes_Core_IJavaProject421", None)
        self.__PrimitiveTypes_Core_IJavaProject421 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Core_IJavaProject422"):
                    opp_val = getattr(item, "Core_IJavaProject422", None)
                    
                    if opp_val == self:
                        setattr(item, "Core_IJavaProject422", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Core_IJavaProject422"):
                    opp_val = getattr(item, "Core_IJavaProject422", None)
                    
                    setattr(item, "Core_IJavaProject422", self)
                    

    @property
    def PrimitiveTypes_Core_IJavaProject(self):
        return self.__PrimitiveTypes_Core_IJavaProject

    @PrimitiveTypes_Core_IJavaProject.setter
    def PrimitiveTypes_Core_IJavaProject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PrimitiveTypes_Core_IJavaProject__PrimitiveTypes_Core_IJavaProject", None)
        self.__PrimitiveTypes_Core_IJavaProject = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Core_IPackageFragmentRoot416"):
                    opp_val = getattr(item, "Core_IPackageFragmentRoot416", None)
                    
                    if opp_val == self:
                        setattr(item, "Core_IPackageFragmentRoot416", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Core_IPackageFragmentRoot416"):
                    opp_val = getattr(item, "Core_IPackageFragmentRoot416", None)
                    
                    setattr(item, "Core_IPackageFragmentRoot416", self)
                    

class PrimitiveTypes_Core_IMember(Core_IJavaElement, Core_ISourceReference):

    def __init__(self, elementName: str, source: str, PrimitiveTypes_Core_IMember: "Core_ISourceRange" = None, PrimitiveTypes_Core_IMember452: "Core_ISourceRange" = None, Core_ISourceReference: "ISourceRange"):
        super().__init__(elementName, source, Core_ISourceReference)
        self.PrimitiveTypes_Core_IMember = PrimitiveTypes_Core_IMember
        self.PrimitiveTypes_Core_IMember452 = PrimitiveTypes_Core_IMember452
        
    @property
    def PrimitiveTypes_Core_IMember452(self):
        return self.__PrimitiveTypes_Core_IMember452

    @PrimitiveTypes_Core_IMember452.setter
    def PrimitiveTypes_Core_IMember452(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PrimitiveTypes_Core_IMember__PrimitiveTypes_Core_IMember452", None)
        self.__PrimitiveTypes_Core_IMember452 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Core_ISourceRange453"):
                opp_val = getattr(old_value, "Core_ISourceRange453", None)
                if opp_val == self:
                    setattr(old_value, "Core_ISourceRange453", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Core_ISourceRange453"):
                opp_val = getattr(value, "Core_ISourceRange453", None)
                setattr(value, "Core_ISourceRange453", self)

    @property
    def PrimitiveTypes_Core_IMember(self):
        return self.__PrimitiveTypes_Core_IMember

    @PrimitiveTypes_Core_IMember.setter
    def PrimitiveTypes_Core_IMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PrimitiveTypes_Core_IMember__PrimitiveTypes_Core_IMember", None)
        self.__PrimitiveTypes_Core_IMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Core_ISourceRange450"):
                opp_val = getattr(old_value, "Core_ISourceRange450", None)
                if opp_val == self:
                    setattr(old_value, "Core_ISourceRange450", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Core_ISourceRange450"):
                opp_val = getattr(value, "Core_ISourceRange450", None)
                setattr(value, "Core_ISourceRange450", self)

class PrimitiveTypes_Core_ITypeParameter(Core_IJavaElement, Core_ISourceReference):

    def __init__(self, elementName: str, source: str, bounds: str, Core_ISourceReference: "ISourceRange"):
        super().__init__(elementName, source, Core_ISourceReference)
        self.bounds = bounds
        
    @property
    def bounds(self) -> str:
        return self.__bounds

    @bounds.setter
    def bounds(self, bounds: str):
        self.__bounds = bounds

class PrimitiveTypes_Core_IPackageFragment(Core_IJavaElement, Core_PhysicalElement):

    def __init__(self, elementName: str, path: str, isReadOnly: str, isDefaultPackage: str, 2426: "Core_IPackageFragmentRoot" = None, PrimitiveTypes_Core_IPackageFragment: set["Core_IClassFile"] = None, PrimitiveTypes_Core_IPackageFragment431: set["Core_ICompilationUnit"] = None):
        super().__init__(elementName, path, isReadOnly)
        self.isDefaultPackage = isDefaultPackage
        self.2426 = 2426
        self.PrimitiveTypes_Core_IPackageFragment = PrimitiveTypes_Core_IPackageFragment if PrimitiveTypes_Core_IPackageFragment is not None else set()
        self.PrimitiveTypes_Core_IPackageFragment431 = PrimitiveTypes_Core_IPackageFragment431 if PrimitiveTypes_Core_IPackageFragment431 is not None else set()
        
    @property
    def isDefaultPackage(self) -> str:
        return self.__isDefaultPackage

    @isDefaultPackage.setter
    def isDefaultPackage(self, isDefaultPackage: str):
        self.__isDefaultPackage = isDefaultPackage

    @property
    def PrimitiveTypes_Core_IPackageFragment431(self):
        return self.__PrimitiveTypes_Core_IPackageFragment431

    @PrimitiveTypes_Core_IPackageFragment431.setter
    def PrimitiveTypes_Core_IPackageFragment431(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PrimitiveTypes_Core_IPackageFragment__PrimitiveTypes_Core_IPackageFragment431", None)
        self.__PrimitiveTypes_Core_IPackageFragment431 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Core_ICompilationUnit432"):
                    opp_val = getattr(item, "Core_ICompilationUnit432", None)
                    
                    if opp_val == self:
                        setattr(item, "Core_ICompilationUnit432", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Core_ICompilationUnit432"):
                    opp_val = getattr(item, "Core_ICompilationUnit432", None)
                    
                    setattr(item, "Core_ICompilationUnit432", self)
                    

    @property
    def 2426(self):
        return self.__2426

    @2426.setter
    def 2426(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PrimitiveTypes_Core_IPackageFragment__2426", None)
        self.__2426 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#427"):
                opp_val = getattr(old_value, "#427", None)
                if opp_val == self:
                    setattr(old_value, "#427", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#427"):
                opp_val = getattr(value, "#427", None)
                setattr(value, "#427", self)

    @property
    def PrimitiveTypes_Core_IPackageFragment(self):
        return self.__PrimitiveTypes_Core_IPackageFragment

    @PrimitiveTypes_Core_IPackageFragment.setter
    def PrimitiveTypes_Core_IPackageFragment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PrimitiveTypes_Core_IPackageFragment__PrimitiveTypes_Core_IPackageFragment", None)
        self.__PrimitiveTypes_Core_IPackageFragment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Core_IClassFile429"):
                    opp_val = getattr(item, "Core_IClassFile429", None)
                    
                    if opp_val == self:
                        setattr(item, "Core_IClassFile429", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Core_IClassFile429"):
                    opp_val = getattr(item, "Core_IClassFile429", None)
                    
                    setattr(item, "Core_IClassFile429", self)
                    

class PrimitiveTypes_Core_ITypeRoot(Core_IJavaElement, Core_ISourceReference, Core_PhysicalElement):

    def __init__(self, elementName: str, path: str, isReadOnly: str, source: str, Core_ISourceReference: "ISourceRange"):
        super().__init__(elementName, path, isReadOnly, source, Core_ISourceReference)
        