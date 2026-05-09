from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Modifiers(Enum):
    abstract = "abstract"
    annotation = "annotation"
    bridge = "bridge"
    default = "default"
    deprecated = "deprecated"
    enum = "enum"
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
class PostfixExpressionOperatorKind(Enum):
    increment = "increment"
    decrement = "decrement"
class InfixExpressionOperatorKind(Enum):
    less_equals = "less_equals"
    equals = "equals"
    not_equals = "not_equals"
    and_ = "and_"
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
    greater_equals = "greater_equals"
    or_ = "or_"
    right_shift_signed = "right_shift_signed"
    minus = "minus"
    xor = "xor"
class PrefixExpressionOperatorKind(Enum):
    minus = "minus"
    not_ = "not_"
    decrement = "decrement"
    complement = "complement"
    increment = "increment"
    plus = "plus"


############################################
# Definition of Classes
############################################

class Core_IJavaElement(ABC):

    def __init__(self, elementName: str):
        self.elementName = elementName
        
        pass
    @property
    def elementName(self):
        return self.__elementName

    @elementName.setter
    def elementName(self, elementName: str):
        self.__elementName = elementName


class IImportDeclaration:

    pass
class IType:

    pass
class ITypeRoot:

    pass
class Core_ICompilationUnit(ITypeRoot):

    pass
class ISourceReference:

    pass
class PrimitiveTypes_Core_Parameter:

    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class PrimitiveTypes_Core_ICompilationUnit(ITypeRoot):

    pass
class PrimitiveTypes_Core_ISourceRange:

    def __init__(self, length: str, offset: str):
        self.length = length
        self.offset = offset
        
        pass
    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length: str):
        self.__length = length


    @property
    def offset(self):
        return self.__offset

    @offset.setter
    def offset(self, offset: str):
        self.__offset = offset


class PrimitiveTypes_Core_ISourceReference(ABC):

    def __init__(self, source: str, PrimitiveTypes_Core_ISourceReference: "Core_ISourceRange" = None):
        self.source = source
        self.PrimitiveTypes_Core_ISourceReference = PrimitiveTypes_Core_ISourceReference
        
        pass
    @property
    def source(self):
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

class PrimitiveTypes_Core_IClassFile(ITypeRoot):

    def __init__(self, isClass: str, isInterface: str, PrimitiveTypes_Core_IClassFile: "Core_IType" = None):
        self.isClass = isClass
        self.isInterface = isInterface
        self.PrimitiveTypes_Core_IClassFile = PrimitiveTypes_Core_IClassFile
        
        pass
    @property
    def isInterface(self):
        return self.__isInterface

    @isInterface.setter
    def isInterface(self, isInterface: str):
        self.__isInterface = isInterface


    @property
    def isClass(self):
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
            if hasattr(old_value, "Core_IType448"):
                opp_val = getattr(old_value, "Core_IType448", None)
                if opp_val == self:
                    setattr(old_value, "Core_IType448", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Core_IType448"):
                opp_val = getattr(value, "Core_IType448", None)
                setattr(value, "Core_IType448", self)

class MemberValuePair:

    pass
class PrimitiveTypes_Core_PhysicalElement(ABC):

    def __init__(self, path: str, isReadOnly: str):
        self.path = path
        self.isReadOnly = isReadOnly
        
        pass
    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path


    @property
    def isReadOnly(self):
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: str):
        self.__isReadOnly = isReadOnly


class PrimitiveTypes_Core_IJavaElement(ABC):

    def __init__(self, elementName: str):
        self.elementName = elementName
        
        pass
    @property
    def elementName(self):
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
        
        pass
    @property
    def varargs(self):
        return self.__varargs

    @varargs.setter
    def varargs(self, varargs: str):
        self.__varargs = varargs


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
                    

class CatchClause:

    pass
class Statement:

    pass
class DOM_ExpressionStatement(Statement):

    pass
class DOM_SynchronizedStatement(Statement):

    pass
class DOM_ReturnStatement(Statement):

    pass
class DOM_EnhancedForStatement(Statement):

    pass
class DOM_ForStatement(Statement):

    pass
class DOM_LabeledStatement(Statement):

    pass
class DOM_IfStatement(Statement):

    pass
class DOM_EmptyStatement(Statement):

    pass
class DOM_ThrowStatement(Statement):

    pass
class DOM_SwitchCase(Statement):

    def __init__(self, default: str, DOM_SwitchCase: "Expression" = None, Statement: "DOM_Block" = None, Statement327: "DOM_IfStatement" = None, Statement295: "DOM_DoStatement" = None, Statement310: "DOM_ForStatement" = None, Statement321: "DOM_IfStatement" = None, Statement300: "DOM_EnhancedForStatement" = None, Statement329: "DOM_LabeledStatement" = None, Statement375: "DOM_WhileStatement" = None, Statement349: "DOM_SwitchStatement" = None):
        self.default = default
        self.DOM_SwitchCase = DOM_SwitchCase
        
        pass
    @property
    def default(self):
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

class DOM_TryStatement(Statement):

    pass
class DOM_SwitchStatement(Statement):

    pass
class DOM_TypeDeclarationStatement(Statement):

    pass
class DOM_WhileStatement(Statement):

    pass
class DOM_VariableDeclarationStatement(Statement):

    pass
class DOM_SuperConstructorInvocation(Statement):

    pass
class DOM_AssertStatement(Statement):

    pass
class DOM_DoStatement(Statement):

    pass
class DOM_ContinueStatement(Statement):

    pass
class DOM_ConstructorInvocation(Statement):

    pass
class DOM_BreakStatement(Statement):

    pass
class DOM_Block(Statement):

    pass
class ArrayType:

    pass
class ArrayInitializer:

    pass
class TagElement:

    pass
class TypeParameter:

    pass
class VariableDeclarationFragment:

    pass
class EnumConstantDeclaration:

    pass
class AnonymousClassDeclaration:

    pass
class Annotation:

    pass
class DOM_SingleMemberAnnotation(Annotation):

    pass
class DOM_NormalAnnotation(Annotation):

    pass
class DOM_MarkerAnnotation(Annotation):

    pass
class Expression:

    pass
class DOM_PrefixExpression(Expression):

    def __init__(self, operator: str, DOM_PrefixExpression: "Expression" = None, Expression336: "DOM_SuperConstructorInvocation" = None, Expression: "DOM_MemberValuePair" = None, Expression227: "DOM_InstanceofExpression" = None, Expression182: "DOM_Assignment" = None, Expression222: "DOM_InfixExpression" = None, Expression280: "DOM_AssertStatement" = None, Expression308: "DOM_ExpressionStatement" = None, Expression354: "DOM_SynchronizedStatement" = None, Expression250: "DOM_PrefixExpression" = None, Expression410: "DOM_SingleMemberAnnotation" = None, Expression206: "DOM_ConditionalExpression" = None, Expression313: "DOM_ForStatement" = None, Expression172: "DOM_ArrayAccess" = None, Expression334: "DOM_ReturnStatement" = None, Expression232: "DOM_MethodInvocation" = None, Expression212: "DOM_ConditionalExpression" = None, Expression356: "DOM_ThrowStatement" = None, Expression225: "DOM_InfixExpression" = None, Expression180: "DOM_ArrayInitializer" = None, Expression192: "DOM_ClassInstanceCreation" = None, Expression174: "DOM_ArrayCreation" = None, Expression346: "DOM_SwitchStatement" = None, Expression283: "DOM_AssertStatement" = None, Expression169: "DOM_ArrayAccess" = None, Expression198: "DOM_ClassInstanceCreation" = None, Expression185: "DOM_Assignment" = None, Expression257: "DOM_SuperMethodInvocation" = None, Expression214: "DOM_FieldAccess" = None, Expression246: "DOM_ParenthesizedExpression" = None, Expression114: "DOM_AnnotationTypeMemberDeclaration" = None, Expression303: "DOM_EnhancedForStatement" = None, Expression339: "DOM_SuperConstructorInvocation" = None, Expression378: "DOM_WhileStatement" = None, Expression316: "DOM_ForStatement" = None, Expression235: "DOM_MethodInvocation" = None, Expression319: "DOM_ForStatement" = None, Expression209: "DOM_ConditionalExpression" = None, Expression324: "DOM_IfStatement" = None, Expression219: "DOM_InfixExpression" = None, Expression187: "DOM_CastExpression" = None, Expression298: "DOM_DoStatement" = None, Expression122: "DOM_EnumConstantDeclaration" = None, Expression288: "DOM_ConstructorInvocation" = None, Expression104: "DOM_VariableDeclaration" = None, Expression248: "DOM_PostfixExpression" = None, Expression344: "DOM_SwitchCase" = None):
        self.operator = operator
        self.DOM_PrefixExpression = DOM_PrefixExpression
        
        pass
    @property
    def operator(self):
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

class DOM_NumberLiteral(Expression):

    def __init__(self, token: str, Expression336: "DOM_SuperConstructorInvocation" = None, Expression: "DOM_MemberValuePair" = None, Expression227: "DOM_InstanceofExpression" = None, Expression182: "DOM_Assignment" = None, Expression222: "DOM_InfixExpression" = None, Expression280: "DOM_AssertStatement" = None, Expression308: "DOM_ExpressionStatement" = None, Expression354: "DOM_SynchronizedStatement" = None, Expression250: "DOM_PrefixExpression" = None, Expression410: "DOM_SingleMemberAnnotation" = None, Expression206: "DOM_ConditionalExpression" = None, Expression313: "DOM_ForStatement" = None, Expression172: "DOM_ArrayAccess" = None, Expression334: "DOM_ReturnStatement" = None, Expression232: "DOM_MethodInvocation" = None, Expression212: "DOM_ConditionalExpression" = None, Expression356: "DOM_ThrowStatement" = None, Expression225: "DOM_InfixExpression" = None, Expression180: "DOM_ArrayInitializer" = None, Expression192: "DOM_ClassInstanceCreation" = None, Expression174: "DOM_ArrayCreation" = None, Expression346: "DOM_SwitchStatement" = None, Expression283: "DOM_AssertStatement" = None, Expression169: "DOM_ArrayAccess" = None, Expression198: "DOM_ClassInstanceCreation" = None, Expression185: "DOM_Assignment" = None, Expression257: "DOM_SuperMethodInvocation" = None, Expression214: "DOM_FieldAccess" = None, Expression246: "DOM_ParenthesizedExpression" = None, Expression114: "DOM_AnnotationTypeMemberDeclaration" = None, Expression303: "DOM_EnhancedForStatement" = None, Expression339: "DOM_SuperConstructorInvocation" = None, Expression378: "DOM_WhileStatement" = None, Expression316: "DOM_ForStatement" = None, Expression235: "DOM_MethodInvocation" = None, Expression319: "DOM_ForStatement" = None, Expression209: "DOM_ConditionalExpression" = None, Expression324: "DOM_IfStatement" = None, Expression219: "DOM_InfixExpression" = None, Expression187: "DOM_CastExpression" = None, Expression298: "DOM_DoStatement" = None, Expression122: "DOM_EnumConstantDeclaration" = None, Expression288: "DOM_ConstructorInvocation" = None, Expression104: "DOM_VariableDeclaration" = None, Expression248: "DOM_PostfixExpression" = None, Expression344: "DOM_SwitchCase" = None):
        self.token = token
        
        pass
    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self, token: str):
        self.__token = token


class DOM_InfixExpression(Expression):

    def __init__(self, operator: str, DOM_InfixExpression: set["Expression"] = None, DOM_InfixExpression221: "Expression" = None, DOM_InfixExpression224: "Expression" = None, Expression336: "DOM_SuperConstructorInvocation" = None, Expression: "DOM_MemberValuePair" = None, Expression227: "DOM_InstanceofExpression" = None, Expression182: "DOM_Assignment" = None, Expression222: "DOM_InfixExpression" = None, Expression280: "DOM_AssertStatement" = None, Expression308: "DOM_ExpressionStatement" = None, Expression354: "DOM_SynchronizedStatement" = None, Expression250: "DOM_PrefixExpression" = None, Expression410: "DOM_SingleMemberAnnotation" = None, Expression206: "DOM_ConditionalExpression" = None, Expression313: "DOM_ForStatement" = None, Expression172: "DOM_ArrayAccess" = None, Expression334: "DOM_ReturnStatement" = None, Expression232: "DOM_MethodInvocation" = None, Expression212: "DOM_ConditionalExpression" = None, Expression356: "DOM_ThrowStatement" = None, Expression225: "DOM_InfixExpression" = None, Expression180: "DOM_ArrayInitializer" = None, Expression192: "DOM_ClassInstanceCreation" = None, Expression174: "DOM_ArrayCreation" = None, Expression346: "DOM_SwitchStatement" = None, Expression283: "DOM_AssertStatement" = None, Expression169: "DOM_ArrayAccess" = None, Expression198: "DOM_ClassInstanceCreation" = None, Expression185: "DOM_Assignment" = None, Expression257: "DOM_SuperMethodInvocation" = None, Expression214: "DOM_FieldAccess" = None, Expression246: "DOM_ParenthesizedExpression" = None, Expression114: "DOM_AnnotationTypeMemberDeclaration" = None, Expression303: "DOM_EnhancedForStatement" = None, Expression339: "DOM_SuperConstructorInvocation" = None, Expression378: "DOM_WhileStatement" = None, Expression316: "DOM_ForStatement" = None, Expression235: "DOM_MethodInvocation" = None, Expression319: "DOM_ForStatement" = None, Expression209: "DOM_ConditionalExpression" = None, Expression324: "DOM_IfStatement" = None, Expression219: "DOM_InfixExpression" = None, Expression187: "DOM_CastExpression" = None, Expression298: "DOM_DoStatement" = None, Expression122: "DOM_EnumConstantDeclaration" = None, Expression288: "DOM_ConstructorInvocation" = None, Expression104: "DOM_VariableDeclaration" = None, Expression248: "DOM_PostfixExpression" = None, Expression344: "DOM_SwitchCase" = None):
        self.operator = operator
        self.DOM_InfixExpression = DOM_InfixExpression if DOM_InfixExpression is not None else set()
        self.DOM_InfixExpression221 = DOM_InfixExpression221
        self.DOM_InfixExpression224 = DOM_InfixExpression224
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


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
                    

class DOM_ArrayAccess(Expression):

    pass
class DOM_NullLiteral(Expression):

    pass
class DOM_MethodInvocation(Expression):

    pass
class DOM_CharacterLiteral(Expression):

    def __init__(self, charValue: str, escapedValue: str, Expression336: "DOM_SuperConstructorInvocation" = None, Expression: "DOM_MemberValuePair" = None, Expression227: "DOM_InstanceofExpression" = None, Expression182: "DOM_Assignment" = None, Expression222: "DOM_InfixExpression" = None, Expression280: "DOM_AssertStatement" = None, Expression308: "DOM_ExpressionStatement" = None, Expression354: "DOM_SynchronizedStatement" = None, Expression250: "DOM_PrefixExpression" = None, Expression410: "DOM_SingleMemberAnnotation" = None, Expression206: "DOM_ConditionalExpression" = None, Expression313: "DOM_ForStatement" = None, Expression172: "DOM_ArrayAccess" = None, Expression334: "DOM_ReturnStatement" = None, Expression232: "DOM_MethodInvocation" = None, Expression212: "DOM_ConditionalExpression" = None, Expression356: "DOM_ThrowStatement" = None, Expression225: "DOM_InfixExpression" = None, Expression180: "DOM_ArrayInitializer" = None, Expression192: "DOM_ClassInstanceCreation" = None, Expression174: "DOM_ArrayCreation" = None, Expression346: "DOM_SwitchStatement" = None, Expression283: "DOM_AssertStatement" = None, Expression169: "DOM_ArrayAccess" = None, Expression198: "DOM_ClassInstanceCreation" = None, Expression185: "DOM_Assignment" = None, Expression257: "DOM_SuperMethodInvocation" = None, Expression214: "DOM_FieldAccess" = None, Expression246: "DOM_ParenthesizedExpression" = None, Expression114: "DOM_AnnotationTypeMemberDeclaration" = None, Expression303: "DOM_EnhancedForStatement" = None, Expression339: "DOM_SuperConstructorInvocation" = None, Expression378: "DOM_WhileStatement" = None, Expression316: "DOM_ForStatement" = None, Expression235: "DOM_MethodInvocation" = None, Expression319: "DOM_ForStatement" = None, Expression209: "DOM_ConditionalExpression" = None, Expression324: "DOM_IfStatement" = None, Expression219: "DOM_InfixExpression" = None, Expression187: "DOM_CastExpression" = None, Expression298: "DOM_DoStatement" = None, Expression122: "DOM_EnumConstantDeclaration" = None, Expression288: "DOM_ConstructorInvocation" = None, Expression104: "DOM_VariableDeclaration" = None, Expression248: "DOM_PostfixExpression" = None, Expression344: "DOM_SwitchCase" = None):
        self.charValue = charValue
        self.escapedValue = escapedValue
        
        pass
    @property
    def escapedValue(self):
        return self.__escapedValue

    @escapedValue.setter
    def escapedValue(self, escapedValue: str):
        self.__escapedValue = escapedValue


    @property
    def charValue(self):
        return self.__charValue

    @charValue.setter
    def charValue(self, charValue: str):
        self.__charValue = charValue


class DOM_ConditionalExpression(Expression):

    pass
class DOM_ThisExpression(Expression):

    pass
class DOM_VariableDeclarationExpression(Expression):

    pass
class DOM_ClassInstanceCreation(Expression):

    pass
class DOM_InstanceofExpression(Expression):

    pass
class DOM_ArrayInitializer(Expression):

    pass
class DOM_SuperFieldAccess(Expression):

    pass
class DOM_TypeLiteral(Expression):

    pass
class DOM_Assignment(Expression):

    def __init__(self, operator: str, DOM_Assignment: "Expression" = None, DOM_Assignment184: "Expression" = None, Expression336: "DOM_SuperConstructorInvocation" = None, Expression: "DOM_MemberValuePair" = None, Expression227: "DOM_InstanceofExpression" = None, Expression182: "DOM_Assignment" = None, Expression222: "DOM_InfixExpression" = None, Expression280: "DOM_AssertStatement" = None, Expression308: "DOM_ExpressionStatement" = None, Expression354: "DOM_SynchronizedStatement" = None, Expression250: "DOM_PrefixExpression" = None, Expression410: "DOM_SingleMemberAnnotation" = None, Expression206: "DOM_ConditionalExpression" = None, Expression313: "DOM_ForStatement" = None, Expression172: "DOM_ArrayAccess" = None, Expression334: "DOM_ReturnStatement" = None, Expression232: "DOM_MethodInvocation" = None, Expression212: "DOM_ConditionalExpression" = None, Expression356: "DOM_ThrowStatement" = None, Expression225: "DOM_InfixExpression" = None, Expression180: "DOM_ArrayInitializer" = None, Expression192: "DOM_ClassInstanceCreation" = None, Expression174: "DOM_ArrayCreation" = None, Expression346: "DOM_SwitchStatement" = None, Expression283: "DOM_AssertStatement" = None, Expression169: "DOM_ArrayAccess" = None, Expression198: "DOM_ClassInstanceCreation" = None, Expression185: "DOM_Assignment" = None, Expression257: "DOM_SuperMethodInvocation" = None, Expression214: "DOM_FieldAccess" = None, Expression246: "DOM_ParenthesizedExpression" = None, Expression114: "DOM_AnnotationTypeMemberDeclaration" = None, Expression303: "DOM_EnhancedForStatement" = None, Expression339: "DOM_SuperConstructorInvocation" = None, Expression378: "DOM_WhileStatement" = None, Expression316: "DOM_ForStatement" = None, Expression235: "DOM_MethodInvocation" = None, Expression319: "DOM_ForStatement" = None, Expression209: "DOM_ConditionalExpression" = None, Expression324: "DOM_IfStatement" = None, Expression219: "DOM_InfixExpression" = None, Expression187: "DOM_CastExpression" = None, Expression298: "DOM_DoStatement" = None, Expression122: "DOM_EnumConstantDeclaration" = None, Expression288: "DOM_ConstructorInvocation" = None, Expression104: "DOM_VariableDeclaration" = None, Expression248: "DOM_PostfixExpression" = None, Expression344: "DOM_SwitchCase" = None):
        self.operator = operator
        self.DOM_Assignment = DOM_Assignment
        self.DOM_Assignment184 = DOM_Assignment184
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


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

class DOM_PostfixExpression(Expression):

    def __init__(self, operator: str, DOM_PostfixExpression: "Expression" = None, Expression336: "DOM_SuperConstructorInvocation" = None, Expression: "DOM_MemberValuePair" = None, Expression227: "DOM_InstanceofExpression" = None, Expression182: "DOM_Assignment" = None, Expression222: "DOM_InfixExpression" = None, Expression280: "DOM_AssertStatement" = None, Expression308: "DOM_ExpressionStatement" = None, Expression354: "DOM_SynchronizedStatement" = None, Expression250: "DOM_PrefixExpression" = None, Expression410: "DOM_SingleMemberAnnotation" = None, Expression206: "DOM_ConditionalExpression" = None, Expression313: "DOM_ForStatement" = None, Expression172: "DOM_ArrayAccess" = None, Expression334: "DOM_ReturnStatement" = None, Expression232: "DOM_MethodInvocation" = None, Expression212: "DOM_ConditionalExpression" = None, Expression356: "DOM_ThrowStatement" = None, Expression225: "DOM_InfixExpression" = None, Expression180: "DOM_ArrayInitializer" = None, Expression192: "DOM_ClassInstanceCreation" = None, Expression174: "DOM_ArrayCreation" = None, Expression346: "DOM_SwitchStatement" = None, Expression283: "DOM_AssertStatement" = None, Expression169: "DOM_ArrayAccess" = None, Expression198: "DOM_ClassInstanceCreation" = None, Expression185: "DOM_Assignment" = None, Expression257: "DOM_SuperMethodInvocation" = None, Expression214: "DOM_FieldAccess" = None, Expression246: "DOM_ParenthesizedExpression" = None, Expression114: "DOM_AnnotationTypeMemberDeclaration" = None, Expression303: "DOM_EnhancedForStatement" = None, Expression339: "DOM_SuperConstructorInvocation" = None, Expression378: "DOM_WhileStatement" = None, Expression316: "DOM_ForStatement" = None, Expression235: "DOM_MethodInvocation" = None, Expression319: "DOM_ForStatement" = None, Expression209: "DOM_ConditionalExpression" = None, Expression324: "DOM_IfStatement" = None, Expression219: "DOM_InfixExpression" = None, Expression187: "DOM_CastExpression" = None, Expression298: "DOM_DoStatement" = None, Expression122: "DOM_EnumConstantDeclaration" = None, Expression288: "DOM_ConstructorInvocation" = None, Expression104: "DOM_VariableDeclaration" = None, Expression248: "DOM_PostfixExpression" = None, Expression344: "DOM_SwitchCase" = None):
        self.operator = operator
        self.DOM_PostfixExpression = DOM_PostfixExpression
        
        pass
    @property
    def operator(self):
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

class DOM_ParenthesizedExpression(Expression):

    pass
class DOM_CastExpression(Expression):

    pass
class DOM_ArrayCreation(Expression):

    pass
class DOM_SuperMethodInvocation(Expression):

    pass
class DOM_StringLiteral(Expression):

    def __init__(self, escapedValue: str, literalValue: str, Expression336: "DOM_SuperConstructorInvocation" = None, Expression: "DOM_MemberValuePair" = None, Expression227: "DOM_InstanceofExpression" = None, Expression182: "DOM_Assignment" = None, Expression222: "DOM_InfixExpression" = None, Expression280: "DOM_AssertStatement" = None, Expression308: "DOM_ExpressionStatement" = None, Expression354: "DOM_SynchronizedStatement" = None, Expression250: "DOM_PrefixExpression" = None, Expression410: "DOM_SingleMemberAnnotation" = None, Expression206: "DOM_ConditionalExpression" = None, Expression313: "DOM_ForStatement" = None, Expression172: "DOM_ArrayAccess" = None, Expression334: "DOM_ReturnStatement" = None, Expression232: "DOM_MethodInvocation" = None, Expression212: "DOM_ConditionalExpression" = None, Expression356: "DOM_ThrowStatement" = None, Expression225: "DOM_InfixExpression" = None, Expression180: "DOM_ArrayInitializer" = None, Expression192: "DOM_ClassInstanceCreation" = None, Expression174: "DOM_ArrayCreation" = None, Expression346: "DOM_SwitchStatement" = None, Expression283: "DOM_AssertStatement" = None, Expression169: "DOM_ArrayAccess" = None, Expression198: "DOM_ClassInstanceCreation" = None, Expression185: "DOM_Assignment" = None, Expression257: "DOM_SuperMethodInvocation" = None, Expression214: "DOM_FieldAccess" = None, Expression246: "DOM_ParenthesizedExpression" = None, Expression114: "DOM_AnnotationTypeMemberDeclaration" = None, Expression303: "DOM_EnhancedForStatement" = None, Expression339: "DOM_SuperConstructorInvocation" = None, Expression378: "DOM_WhileStatement" = None, Expression316: "DOM_ForStatement" = None, Expression235: "DOM_MethodInvocation" = None, Expression319: "DOM_ForStatement" = None, Expression209: "DOM_ConditionalExpression" = None, Expression324: "DOM_IfStatement" = None, Expression219: "DOM_InfixExpression" = None, Expression187: "DOM_CastExpression" = None, Expression298: "DOM_DoStatement" = None, Expression122: "DOM_EnumConstantDeclaration" = None, Expression288: "DOM_ConstructorInvocation" = None, Expression104: "DOM_VariableDeclaration" = None, Expression248: "DOM_PostfixExpression" = None, Expression344: "DOM_SwitchCase" = None):
        self.escapedValue = escapedValue
        self.literalValue = literalValue
        
        pass
    @property
    def literalValue(self):
        return self.__literalValue

    @literalValue.setter
    def literalValue(self, literalValue: str):
        self.__literalValue = literalValue


    @property
    def escapedValue(self):
        return self.__escapedValue

    @escapedValue.setter
    def escapedValue(self, escapedValue: str):
        self.__escapedValue = escapedValue


class DOM_Name(Expression):

    def __init__(self, fullyQualifiedName: str, Expression336: "DOM_SuperConstructorInvocation" = None, Expression: "DOM_MemberValuePair" = None, Expression227: "DOM_InstanceofExpression" = None, Expression182: "DOM_Assignment" = None, Expression222: "DOM_InfixExpression" = None, Expression280: "DOM_AssertStatement" = None, Expression308: "DOM_ExpressionStatement" = None, Expression354: "DOM_SynchronizedStatement" = None, Expression250: "DOM_PrefixExpression" = None, Expression410: "DOM_SingleMemberAnnotation" = None, Expression206: "DOM_ConditionalExpression" = None, Expression313: "DOM_ForStatement" = None, Expression172: "DOM_ArrayAccess" = None, Expression334: "DOM_ReturnStatement" = None, Expression232: "DOM_MethodInvocation" = None, Expression212: "DOM_ConditionalExpression" = None, Expression356: "DOM_ThrowStatement" = None, Expression225: "DOM_InfixExpression" = None, Expression180: "DOM_ArrayInitializer" = None, Expression192: "DOM_ClassInstanceCreation" = None, Expression174: "DOM_ArrayCreation" = None, Expression346: "DOM_SwitchStatement" = None, Expression283: "DOM_AssertStatement" = None, Expression169: "DOM_ArrayAccess" = None, Expression198: "DOM_ClassInstanceCreation" = None, Expression185: "DOM_Assignment" = None, Expression257: "DOM_SuperMethodInvocation" = None, Expression214: "DOM_FieldAccess" = None, Expression246: "DOM_ParenthesizedExpression" = None, Expression114: "DOM_AnnotationTypeMemberDeclaration" = None, Expression303: "DOM_EnhancedForStatement" = None, Expression339: "DOM_SuperConstructorInvocation" = None, Expression378: "DOM_WhileStatement" = None, Expression316: "DOM_ForStatement" = None, Expression235: "DOM_MethodInvocation" = None, Expression319: "DOM_ForStatement" = None, Expression209: "DOM_ConditionalExpression" = None, Expression324: "DOM_IfStatement" = None, Expression219: "DOM_InfixExpression" = None, Expression187: "DOM_CastExpression" = None, Expression298: "DOM_DoStatement" = None, Expression122: "DOM_EnumConstantDeclaration" = None, Expression288: "DOM_ConstructorInvocation" = None, Expression104: "DOM_VariableDeclaration" = None, Expression248: "DOM_PostfixExpression" = None, Expression344: "DOM_SwitchCase" = None):
        self.fullyQualifiedName = fullyQualifiedName
        
        pass
    @property
    def fullyQualifiedName(self):
        return self.__fullyQualifiedName

    @fullyQualifiedName.setter
    def fullyQualifiedName(self, fullyQualifiedName: str):
        self.__fullyQualifiedName = fullyQualifiedName


class DOM_BooleanLiteral(Expression):

    def __init__(self, booleanValue: str, Expression336: "DOM_SuperConstructorInvocation" = None, Expression: "DOM_MemberValuePair" = None, Expression227: "DOM_InstanceofExpression" = None, Expression182: "DOM_Assignment" = None, Expression222: "DOM_InfixExpression" = None, Expression280: "DOM_AssertStatement" = None, Expression308: "DOM_ExpressionStatement" = None, Expression354: "DOM_SynchronizedStatement" = None, Expression250: "DOM_PrefixExpression" = None, Expression410: "DOM_SingleMemberAnnotation" = None, Expression206: "DOM_ConditionalExpression" = None, Expression313: "DOM_ForStatement" = None, Expression172: "DOM_ArrayAccess" = None, Expression334: "DOM_ReturnStatement" = None, Expression232: "DOM_MethodInvocation" = None, Expression212: "DOM_ConditionalExpression" = None, Expression356: "DOM_ThrowStatement" = None, Expression225: "DOM_InfixExpression" = None, Expression180: "DOM_ArrayInitializer" = None, Expression192: "DOM_ClassInstanceCreation" = None, Expression174: "DOM_ArrayCreation" = None, Expression346: "DOM_SwitchStatement" = None, Expression283: "DOM_AssertStatement" = None, Expression169: "DOM_ArrayAccess" = None, Expression198: "DOM_ClassInstanceCreation" = None, Expression185: "DOM_Assignment" = None, Expression257: "DOM_SuperMethodInvocation" = None, Expression214: "DOM_FieldAccess" = None, Expression246: "DOM_ParenthesizedExpression" = None, Expression114: "DOM_AnnotationTypeMemberDeclaration" = None, Expression303: "DOM_EnhancedForStatement" = None, Expression339: "DOM_SuperConstructorInvocation" = None, Expression378: "DOM_WhileStatement" = None, Expression316: "DOM_ForStatement" = None, Expression235: "DOM_MethodInvocation" = None, Expression319: "DOM_ForStatement" = None, Expression209: "DOM_ConditionalExpression" = None, Expression324: "DOM_IfStatement" = None, Expression219: "DOM_InfixExpression" = None, Expression187: "DOM_CastExpression" = None, Expression298: "DOM_DoStatement" = None, Expression122: "DOM_EnumConstantDeclaration" = None, Expression288: "DOM_ConstructorInvocation" = None, Expression104: "DOM_VariableDeclaration" = None, Expression248: "DOM_PostfixExpression" = None, Expression344: "DOM_SwitchCase" = None):
        self.booleanValue = booleanValue
        
        pass
    @property
    def booleanValue(self):
        return self.__booleanValue

    @booleanValue.setter
    def booleanValue(self, booleanValue: str):
        self.__booleanValue = booleanValue


class DOM_FieldAccess(Expression):

    pass
class SimpleName:

    pass
class Name:

    pass
class DOM_SimpleName(Name):

    def __init__(self, identifier: str, declaration: str, Name407: "DOM_QualifiedName" = None, Name263: "DOM_SuperMethodInvocation" = None, Name79: "DOM_MethodRef" = None, Name260: "DOM_SuperMethodInvocation" = None, Name268: "DOM_ThisExpression" = None, Name167: "DOM_Annotation" = None, Name: "DOM_ImportDeclaration" = None, Name395: "DOM_SimpleType" = None, Name92: "DOM_PackageDeclaration" = None, Name70: "DOM_MemberRef" = None, Name255: "DOM_SuperFieldAccess" = None, Name147: "DOM_MethodDeclaration" = None):
        self.identifier = identifier
        self.declaration = declaration
        
        pass
    @property
    def declaration(self):
        return self.__declaration

    @declaration.setter
    def declaration(self, declaration: str):
        self.__declaration = declaration


    @property
    def identifier(self):
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier


class DOM_QualifiedName(Name):

    pass
class AbstractTypeDeclaration:

    pass
class DOM_AnnotationTypeDeclaration(AbstractTypeDeclaration):

    pass
class DOM_TypeDeclaration(AbstractTypeDeclaration):

    def __init__(self, interface: str, DOM_TypeDeclaration: "Type" = None, DOM_TypeDeclaration160: set["Type"] = None, DOM_TypeDeclaration163: set["TypeParameter"] = None, AbstractTypeDeclaration: "DOM_CompilationUnit" = None, AbstractTypeDeclaration365: "DOM_TypeDeclarationStatement" = None):
        self.interface = interface
        self.DOM_TypeDeclaration = DOM_TypeDeclaration
        self.DOM_TypeDeclaration160 = DOM_TypeDeclaration160 if DOM_TypeDeclaration160 is not None else set()
        self.DOM_TypeDeclaration163 = DOM_TypeDeclaration163 if DOM_TypeDeclaration163 is not None else set()
        
        pass
    @property
    def interface(self):
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
                    

class DOM_EnumDeclaration(AbstractTypeDeclaration):

    pass
class ImportDeclaration:

    pass
class PackageDeclaration:

    pass
class Comment:

    pass
class DOM_BlockComment(Comment):

    pass
class DOM_Javadoc(Comment):

    pass
class DOM_LineComment(Comment):

    pass
class DOM_ExtendedModifier(ABC):

    pass
class Type:

    pass
class DOM_WildcardType(Type):

    def __init__(self, upperBound: str, DOM_WildcardType: "Type" = None, Type141: "DOM_MethodDeclaration" = None, Type383: "DOM_ArrayType" = None, Type385: "DOM_ParameterizedType" = None, Type204: "DOM_ClassInstanceCreation" = None, Type266: "DOM_SuperMethodInvocation" = None, Type120: "DOM_AnnotationTypeMemberDeclaration" = None, Type393: "DOM_QualifiedType" = None, Type131: "DOM_FieldDeclaration" = None, Type161: "DOM_TypeDeclaration" = None, Type388: "DOM_ParameterizedType" = None, Type201: "DOM_ClassInstanceCreation" = None, Type230: "DOM_InstanceofExpression" = None, Type373: "DOM_VariableDeclarationStatement" = None, Type190: "DOM_CastExpression" = None, Type241: "DOM_MethodInvocation" = None, Type291: "DOM_ConstructorInvocation" = None, Type278: "DOM_VariableDeclarationExpression" = None, Type158: "DOM_TypeDeclaration" = None, Type399: "DOM_SingleVariableDeclaration" = None, Type154: "DOM_EnumDeclaration" = None, Type380: "DOM_ArrayType" = None, Type102: "DOM_TypeParameter" = None, Type397: "DOM_WildcardType" = None, Type: "DOM_MethodRefParameter" = None, Type342: "DOM_SuperConstructorInvocation" = None, Type270: "DOM_TypeLiteral" = None):
        self.upperBound = upperBound
        self.DOM_WildcardType = DOM_WildcardType
        
        pass
    @property
    def upperBound(self):
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

class DOM_ArrayType(Type):

    def __init__(self, dimensions: str, DOM_ArrayType: "Type" = None, DOM_ArrayType382: "Type" = None, Type141: "DOM_MethodDeclaration" = None, Type383: "DOM_ArrayType" = None, Type385: "DOM_ParameterizedType" = None, Type204: "DOM_ClassInstanceCreation" = None, Type266: "DOM_SuperMethodInvocation" = None, Type120: "DOM_AnnotationTypeMemberDeclaration" = None, Type393: "DOM_QualifiedType" = None, Type131: "DOM_FieldDeclaration" = None, Type161: "DOM_TypeDeclaration" = None, Type388: "DOM_ParameterizedType" = None, Type201: "DOM_ClassInstanceCreation" = None, Type230: "DOM_InstanceofExpression" = None, Type373: "DOM_VariableDeclarationStatement" = None, Type190: "DOM_CastExpression" = None, Type241: "DOM_MethodInvocation" = None, Type291: "DOM_ConstructorInvocation" = None, Type278: "DOM_VariableDeclarationExpression" = None, Type158: "DOM_TypeDeclaration" = None, Type399: "DOM_SingleVariableDeclaration" = None, Type154: "DOM_EnumDeclaration" = None, Type380: "DOM_ArrayType" = None, Type102: "DOM_TypeParameter" = None, Type397: "DOM_WildcardType" = None, Type: "DOM_MethodRefParameter" = None, Type342: "DOM_SuperConstructorInvocation" = None, Type270: "DOM_TypeLiteral" = None):
        self.dimensions = dimensions
        self.DOM_ArrayType = DOM_ArrayType
        self.DOM_ArrayType382 = DOM_ArrayType382
        
        pass
    @property
    def dimensions(self):
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

class DOM_SimpleType(Type):

    pass
class DOM_QualifiedType(Type):

    pass
class DOM_ParameterizedType(Type):

    pass
class DOM_PrimitiveType(Type):

    def __init__(self, code: str, Type141: "DOM_MethodDeclaration" = None, Type383: "DOM_ArrayType" = None, Type385: "DOM_ParameterizedType" = None, Type204: "DOM_ClassInstanceCreation" = None, Type266: "DOM_SuperMethodInvocation" = None, Type120: "DOM_AnnotationTypeMemberDeclaration" = None, Type393: "DOM_QualifiedType" = None, Type131: "DOM_FieldDeclaration" = None, Type161: "DOM_TypeDeclaration" = None, Type388: "DOM_ParameterizedType" = None, Type201: "DOM_ClassInstanceCreation" = None, Type230: "DOM_InstanceofExpression" = None, Type373: "DOM_VariableDeclarationStatement" = None, Type190: "DOM_CastExpression" = None, Type241: "DOM_MethodInvocation" = None, Type291: "DOM_ConstructorInvocation" = None, Type278: "DOM_VariableDeclarationExpression" = None, Type158: "DOM_TypeDeclaration" = None, Type399: "DOM_SingleVariableDeclaration" = None, Type154: "DOM_EnumDeclaration" = None, Type380: "DOM_ArrayType" = None, Type102: "DOM_TypeParameter" = None, Type397: "DOM_WildcardType" = None, Type: "DOM_MethodRefParameter" = None, Type342: "DOM_SuperConstructorInvocation" = None, Type270: "DOM_TypeLiteral" = None):
        self.code = code
        
        pass
    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code


class MethodRefParameter:

    pass
class BodyDeclaration:

    pass
class DOM_AbstractTypeDeclaration(BodyDeclaration):

    def __init__(self, localTypeDeclaration: str, memberTypeDeclaration: str, packageMemberTypeDeclaration: str, DOM_AbstractTypeDeclaration: set["BodyDeclaration"] = None, DOM_AbstractTypeDeclaration111: "SimpleName" = None, BodyDeclaration: "DOM_AnonymousClassDeclaration" = None, BodyDeclaration109: "DOM_AbstractTypeDeclaration" = None):
        self.localTypeDeclaration = localTypeDeclaration
        self.memberTypeDeclaration = memberTypeDeclaration
        self.packageMemberTypeDeclaration = packageMemberTypeDeclaration
        self.DOM_AbstractTypeDeclaration = DOM_AbstractTypeDeclaration if DOM_AbstractTypeDeclaration is not None else set()
        self.DOM_AbstractTypeDeclaration111 = DOM_AbstractTypeDeclaration111
        
        pass
    @property
    def memberTypeDeclaration(self):
        return self.__memberTypeDeclaration

    @memberTypeDeclaration.setter
    def memberTypeDeclaration(self, memberTypeDeclaration: str):
        self.__memberTypeDeclaration = memberTypeDeclaration


    @property
    def localTypeDeclaration(self):
        return self.__localTypeDeclaration

    @localTypeDeclaration.setter
    def localTypeDeclaration(self, localTypeDeclaration: str):
        self.__localTypeDeclaration = localTypeDeclaration


    @property
    def packageMemberTypeDeclaration(self):
        return self.__packageMemberTypeDeclaration

    @packageMemberTypeDeclaration.setter
    def packageMemberTypeDeclaration(self, packageMemberTypeDeclaration: str):
        self.__packageMemberTypeDeclaration = packageMemberTypeDeclaration


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
                    

class DOM_Initializer(BodyDeclaration):

    pass
class DOM_FieldDeclaration(BodyDeclaration):

    pass
class DOM_EnumConstantDeclaration(BodyDeclaration):

    pass
class DOM_MethodDeclaration(BodyDeclaration):

    def __init__(self, extraDimensions: str, constructor: str, varargs: str, DOM_MethodDeclaration: "Block" = None, DOM_MethodDeclaration137: "SimpleName" = None, DOM_MethodDeclaration140: "Type" = None, DOM_MethodDeclaration143: set["SingleVariableDeclaration"] = None, DOM_MethodDeclaration146: set["Name"] = None, DOM_MethodDeclaration149: set["TypeParameter"] = None, DOM_MethodDeclaration151: "IMethod" = None, BodyDeclaration: "DOM_AnonymousClassDeclaration" = None, BodyDeclaration109: "DOM_AbstractTypeDeclaration" = None):
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
        
        pass
    @property
    def constructor(self):
        return self.__constructor

    @constructor.setter
    def constructor(self, constructor: str):
        self.__constructor = constructor


    @property
    def extraDimensions(self):
        return self.__extraDimensions

    @extraDimensions.setter
    def extraDimensions(self, extraDimensions: str):
        self.__extraDimensions = extraDimensions


    @property
    def varargs(self):
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

class DOM_AnnotationTypeMemberDeclaration(BodyDeclaration):

    pass
class DOM_ASTNode(ABC):

    pass
class ASTNode:

    pass
class DOM_MethodRef(ASTNode):

    pass
class DOM_TextElement(ASTNode):

    def __init__(self, text: str, ASTNode: "DOM_AST" = None, ASTNode56: "DOM_Comment" = None, ASTNode97: "DOM_TagElement" = None):
        self.text = text
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


class DOM_Type(ASTNode):

    pass
class DOM_TagElement(ASTNode):

    def __init__(self, tagName: str, nested: str, DOM_TagElement: set["ASTNode"] = None, ASTNode: "DOM_AST" = None, ASTNode56: "DOM_Comment" = None, ASTNode97: "DOM_TagElement" = None):
        self.tagName = tagName
        self.nested = nested
        self.DOM_TagElement = DOM_TagElement if DOM_TagElement is not None else set()
        
        pass
    @property
    def tagName(self):
        return self.__tagName

    @tagName.setter
    def tagName(self, tagName: str):
        self.__tagName = tagName


    @property
    def nested(self):
        return self.__nested

    @nested.setter
    def nested(self, nested: str):
        self.__nested = nested


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
                    

class DOM_CompilationUnit(ASTNode):

    pass
class DOM_PackageDeclaration(ASTNode):

    pass
class DOM_MemberValuePair(ASTNode):

    pass
class DOM_BodyDeclaration(ASTNode):

    pass
class DOM_MethodRefParameter(ASTNode):

    def __init__(self, varargs: str, DOM_MethodRefParameter: "SimpleName" = None, DOM_MethodRefParameter85: "Type" = None, ASTNode: "DOM_AST" = None, ASTNode56: "DOM_Comment" = None, ASTNode97: "DOM_TagElement" = None):
        self.varargs = varargs
        self.DOM_MethodRefParameter = DOM_MethodRefParameter
        self.DOM_MethodRefParameter85 = DOM_MethodRefParameter85
        
        pass
    @property
    def varargs(self):
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
            if hasattr(old_value, "SimpleName83"):
                opp_val = getattr(old_value, "SimpleName83", None)
                if opp_val == self:
                    setattr(old_value, "SimpleName83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleName83"):
                opp_val = getattr(value, "SimpleName83", None)
                setattr(value, "SimpleName83", self)

    @property
    def DOM_MethodRefParameter85(self):
        return self.__DOM_MethodRefParameter85

    @DOM_MethodRefParameter85.setter
    def DOM_MethodRefParameter85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOM_MethodRefParameter__DOM_MethodRefParameter85", None)
        self.__DOM_MethodRefParameter85 = value
        
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

class DOM_AnonymousClassDeclaration(ASTNode):

    pass
class DOM_TypeParameter(ASTNode):

    pass
class DOM_VariableDeclaration(ASTNode):

    def __init__(self, extraDimensions: str, DOM_VariableDeclaration: "Expression" = None, DOM_VariableDeclaration106: "SimpleName" = None, ASTNode: "DOM_AST" = None, ASTNode56: "DOM_Comment" = None, ASTNode97: "DOM_TagElement" = None):
        self.extraDimensions = extraDimensions
        self.DOM_VariableDeclaration = DOM_VariableDeclaration
        self.DOM_VariableDeclaration106 = DOM_VariableDeclaration106
        
        pass
    @property
    def extraDimensions(self):
        return self.__extraDimensions

    @extraDimensions.setter
    def extraDimensions(self, extraDimensions: str):
        self.__extraDimensions = extraDimensions


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

class DOM_MemberRef(ASTNode):

    pass
class DOM_Expression(ASTNode):

    def __init__(self, resolveBoxing: str, resolveUnboxing: str, DOM_Expression: "IType" = None, ASTNode: "DOM_AST" = None, ASTNode56: "DOM_Comment" = None, ASTNode97: "DOM_TagElement" = None):
        self.resolveBoxing = resolveBoxing
        self.resolveUnboxing = resolveUnboxing
        self.DOM_Expression = DOM_Expression
        
        pass
    @property
    def resolveUnboxing(self):
        return self.__resolveUnboxing

    @resolveUnboxing.setter
    def resolveUnboxing(self, resolveUnboxing: str):
        self.__resolveUnboxing = resolveUnboxing


    @property
    def resolveBoxing(self):
        return self.__resolveBoxing

    @resolveBoxing.setter
    def resolveBoxing(self, resolveBoxing: str):
        self.__resolveBoxing = resolveBoxing


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
            if hasattr(old_value, "IType65"):
                opp_val = getattr(old_value, "IType65", None)
                if opp_val == self:
                    setattr(old_value, "IType65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IType65"):
                opp_val = getattr(value, "IType65", None)
                setattr(value, "IType65", self)

class DOM_Statement(ASTNode):

    pass
class DOM_ImportDeclaration(ASTNode):

    def __init__(self, onDemand: str, static: str, DOM_ImportDeclaration: "Name" = None, ASTNode: "DOM_AST" = None, ASTNode56: "DOM_Comment" = None, ASTNode97: "DOM_TagElement" = None):
        self.onDemand = onDemand
        self.static = static
        self.DOM_ImportDeclaration = DOM_ImportDeclaration
        
        pass
    @property
    def onDemand(self):
        return self.__onDemand

    @onDemand.setter
    def onDemand(self, onDemand: str):
        self.__onDemand = onDemand


    @property
    def static(self):
        return self.__static

    @static.setter
    def static(self, static: str):
        self.__static = static


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

class DOM_AST:

    pass
class Core_Parameter:

    def __init__(self, name: str, type: str, Core_Parameter: "PrimitiveTypes_Core_IMethod" = None):
        self.name = name
        self.type = type
        self.Core_Parameter = Core_Parameter
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def name(self):
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
class DOM_Comment(ASTNode):

    pass
class SingleVariableDeclaration:

    pass
class Block:

    pass
class DOM_CatchClause(ASTNode):

    pass
class Javadoc:

    pass
class ExtendedModifier:

    pass
class DOM_Annotation(Expression, ExtendedModifier):

    pass
class DOM_Modifier(ASTNode, ExtendedModifier):

    def __init__(self, abstract: str, final: str, native: str, none: str, private: str, protected: str, public: str, static: str, strictfp: str, synchronized: str, transient: str, volatile: str, ExtendedModifier370: "DOM_VariableDeclarationStatement" = None, ExtendedModifier402: "DOM_SingleVariableDeclaration" = None, ExtendedModifier275: "DOM_VariableDeclarationExpression" = None, ExtendedModifier: "DOM_BodyDeclaration" = None, ASTNode: "DOM_AST" = None, ASTNode56: "DOM_Comment" = None, ASTNode97: "DOM_TagElement" = None):
        self.abstract = abstract
        self.final = final
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
        
        pass
    @property
    def private(self):
        return self.__private

    @private.setter
    def private(self, private: str):
        self.__private = private


    @property
    def volatile(self):
        return self.__volatile

    @volatile.setter
    def volatile(self, volatile: str):
        self.__volatile = volatile


    @property
    def synchronized(self):
        return self.__synchronized

    @synchronized.setter
    def synchronized(self, synchronized: str):
        self.__synchronized = synchronized


    @property
    def protected(self):
        return self.__protected

    @protected.setter
    def protected(self, protected: str):
        self.__protected = protected


    @property
    def native(self):
        return self.__native

    @native.setter
    def native(self, native: str):
        self.__native = native


    @property
    def static(self):
        return self.__static

    @static.setter
    def static(self, static: str):
        self.__static = static


    @property
    def strictfp(self):
        return self.__strictfp

    @strictfp.setter
    def strictfp(self, strictfp: str):
        self.__strictfp = strictfp


    @property
    def abstract(self):
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: str):
        self.__abstract = abstract


    @property
    def none(self):
        return self.__none

    @none.setter
    def none(self, none: str):
        self.__none = none


    @property
    def public(self):
        return self.__public

    @public.setter
    def public(self, public: str):
        self.__public = public


    @property
    def final(self):
        return self.__final

    @final.setter
    def final(self, final: str):
        self.__final = final


    @property
    def transient(self):
        return self.__transient

    @transient.setter
    def transient(self, transient: str):
        self.__transient = transient


class IMethod:

    pass
class IField:

    pass
class IInitializer:

    pass
class IMember:

    pass
class PrimitiveTypes_Core_IInitializer(IMember):

    pass
class PrimitiveTypes_Core_IMethod(IMember):

    def __init__(self, returnType: str, isConstructor: str, isMainMethod: str, exceptionTypes: str, PrimitiveTypes_Core_IMethod: set["Core_Parameter"] = None):
        self.returnType = returnType
        self.isConstructor = isConstructor
        self.isMainMethod = isMainMethod
        self.exceptionTypes = exceptionTypes
        self.PrimitiveTypes_Core_IMethod = PrimitiveTypes_Core_IMethod if PrimitiveTypes_Core_IMethod is not None else set()
        
        pass
    @property
    def isMainMethod(self):
        return self.__isMainMethod

    @isMainMethod.setter
    def isMainMethod(self, isMainMethod: str):
        self.__isMainMethod = isMainMethod


    @property
    def isConstructor(self):
        return self.__isConstructor

    @isConstructor.setter
    def isConstructor(self, isConstructor: str):
        self.__isConstructor = isConstructor


    @property
    def returnType(self):
        return self.__returnType

    @returnType.setter
    def returnType(self, returnType: str):
        self.__returnType = returnType


    @property
    def exceptionTypes(self):
        return self.__exceptionTypes

    @exceptionTypes.setter
    def exceptionTypes(self, exceptionTypes: str):
        self.__exceptionTypes = exceptionTypes


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
                    

class Core_IMethod(IMember):

    def __init__(self, returnType: str, isConstructor: str, isMainMethod: str, exceptionTypes: str, Core_IMethod: set["Parameter"] = None, Core_IMethod460: "PrimitiveTypes_Core_IType" = None):
        self.returnType = returnType
        self.isConstructor = isConstructor
        self.isMainMethod = isMainMethod
        self.exceptionTypes = exceptionTypes
        self.Core_IMethod = Core_IMethod if Core_IMethod is not None else set()
        self.Core_IMethod460 = Core_IMethod460
        
        pass
    @property
    def isConstructor(self):
        return self.__isConstructor

    @isConstructor.setter
    def isConstructor(self, isConstructor: str):
        self.__isConstructor = isConstructor


    @property
    def exceptionTypes(self):
        return self.__exceptionTypes

    @exceptionTypes.setter
    def exceptionTypes(self, exceptionTypes: str):
        self.__exceptionTypes = exceptionTypes


    @property
    def returnType(self):
        return self.__returnType

    @returnType.setter
    def returnType(self, returnType: str):
        self.__returnType = returnType


    @property
    def isMainMethod(self):
        return self.__isMainMethod

    @isMainMethod.setter
    def isMainMethod(self, isMainMethod: str):
        self.__isMainMethod = isMainMethod


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
    def Core_IMethod460(self):
        return self.__Core_IMethod460

    @Core_IMethod460.setter
    def Core_IMethod460(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IMethod__Core_IMethod460", None)
        self.__Core_IMethod460 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PrimitiveTypes_Core_IType459"):
                opp_val = getattr(old_value, "PrimitiveTypes_Core_IType459", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PrimitiveTypes_Core_IType459"):
                opp_val = getattr(value, "PrimitiveTypes_Core_IType459", None)
                if opp_val is None:
                    setattr(value, "PrimitiveTypes_Core_IType459", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PrimitiveTypes_Core_IField(IMember):

    def __init__(self, constant: str, isEnumConstant: str, typeSignature: str, isVolatile: str, isTransient: str):
        self.constant = constant
        self.isEnumConstant = isEnumConstant
        self.typeSignature = typeSignature
        self.isVolatile = isVolatile
        self.isTransient = isTransient
        
        pass
    @property
    def isEnumConstant(self):
        return self.__isEnumConstant

    @isEnumConstant.setter
    def isEnumConstant(self, isEnumConstant: str):
        self.__isEnumConstant = isEnumConstant


    @property
    def typeSignature(self):
        return self.__typeSignature

    @typeSignature.setter
    def typeSignature(self, typeSignature: str):
        self.__typeSignature = typeSignature


    @property
    def isTransient(self):
        return self.__isTransient

    @isTransient.setter
    def isTransient(self, isTransient: str):
        self.__isTransient = isTransient


    @property
    def constant(self):
        return self.__constant

    @constant.setter
    def constant(self, constant: str):
        self.__constant = constant


    @property
    def isVolatile(self):
        return self.__isVolatile

    @isVolatile.setter
    def isVolatile(self, isVolatile: str):
        self.__isVolatile = isVolatile


class PrimitiveTypes_Core_IType(IMember):

    def __init__(self, fullyQualifiedName: str, fullyQualifiedParametrizedName: str, PrimitiveTypes_Core_IType459: set["Core_IMethod"] = None, PrimitiveTypes_Core_IType462: set["Core_IType"] = None, PrimitiveTypes_Core_IType465: set["Core_ITypeParameter"] = None, PrimitiveTypes_Core_IType: set["Core_IInitializer"] = None, PrimitiveTypes_Core_IType457: set["Core_IField"] = None):
        self.fullyQualifiedName = fullyQualifiedName
        self.fullyQualifiedParametrizedName = fullyQualifiedParametrizedName
        self.PrimitiveTypes_Core_IType459 = PrimitiveTypes_Core_IType459 if PrimitiveTypes_Core_IType459 is not None else set()
        self.PrimitiveTypes_Core_IType462 = PrimitiveTypes_Core_IType462 if PrimitiveTypes_Core_IType462 is not None else set()
        self.PrimitiveTypes_Core_IType465 = PrimitiveTypes_Core_IType465 if PrimitiveTypes_Core_IType465 is not None else set()
        self.PrimitiveTypes_Core_IType = PrimitiveTypes_Core_IType if PrimitiveTypes_Core_IType is not None else set()
        self.PrimitiveTypes_Core_IType457 = PrimitiveTypes_Core_IType457 if PrimitiveTypes_Core_IType457 is not None else set()
        
        pass
    @property
    def fullyQualifiedParametrizedName(self):
        return self.__fullyQualifiedParametrizedName

    @fullyQualifiedParametrizedName.setter
    def fullyQualifiedParametrizedName(self, fullyQualifiedParametrizedName: str):
        self.__fullyQualifiedParametrizedName = fullyQualifiedParametrizedName


    @property
    def fullyQualifiedName(self):
        return self.__fullyQualifiedName

    @fullyQualifiedName.setter
    def fullyQualifiedName(self, fullyQualifiedName: str):
        self.__fullyQualifiedName = fullyQualifiedName


    @property
    def PrimitiveTypes_Core_IType462(self):
        return self.__PrimitiveTypes_Core_IType462

    @PrimitiveTypes_Core_IType462.setter
    def PrimitiveTypes_Core_IType462(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PrimitiveTypes_Core_IType__PrimitiveTypes_Core_IType462", None)
        self.__PrimitiveTypes_Core_IType462 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Core_IType463"):
                    opp_val = getattr(item, "Core_IType463", None)
                    
                    if opp_val == self:
                        setattr(item, "Core_IType463", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Core_IType463"):
                    opp_val = getattr(item, "Core_IType463", None)
                    
                    setattr(item, "Core_IType463", self)
                    

    @property
    def PrimitiveTypes_Core_IType459(self):
        return self.__PrimitiveTypes_Core_IType459

    @PrimitiveTypes_Core_IType459.setter
    def PrimitiveTypes_Core_IType459(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PrimitiveTypes_Core_IType__PrimitiveTypes_Core_IType459", None)
        self.__PrimitiveTypes_Core_IType459 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Core_IMethod460"):
                    opp_val = getattr(item, "Core_IMethod460", None)
                    
                    if opp_val == self:
                        setattr(item, "Core_IMethod460", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Core_IMethod460"):
                    opp_val = getattr(item, "Core_IMethod460", None)
                    
                    setattr(item, "Core_IMethod460", self)
                    

    @property
    def PrimitiveTypes_Core_IType457(self):
        return self.__PrimitiveTypes_Core_IType457

    @PrimitiveTypes_Core_IType457.setter
    def PrimitiveTypes_Core_IType457(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PrimitiveTypes_Core_IType__PrimitiveTypes_Core_IType457", None)
        self.__PrimitiveTypes_Core_IType457 = value if value is not None else set()
        
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
    def PrimitiveTypes_Core_IType465(self):
        return self.__PrimitiveTypes_Core_IType465

    @PrimitiveTypes_Core_IType465.setter
    def PrimitiveTypes_Core_IType465(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PrimitiveTypes_Core_IType__PrimitiveTypes_Core_IType465", None)
        self.__PrimitiveTypes_Core_IType465 = value if value is not None else set()
        
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
                    

class Core_IType(IMember):

    def __init__(self, fullyQualifiedName: str, fullyQualifiedParametrizedName: str, Core_IType: set["IInitializer"] = None, Core_IType38: set["IField"] = None, Core_IType40: set["IMethod"] = None, Core_IType42: set["IType"] = None, Core_IType45: set["ITypeParameter"] = None, Core_IType435: "PrimitiveTypes_Core_ICompilationUnit" = None, Core_IType440: "PrimitiveTypes_Core_ICompilationUnit" = None, Core_IType448: "PrimitiveTypes_Core_IClassFile" = None, Core_IType463: "PrimitiveTypes_Core_IType" = None):
        self.fullyQualifiedName = fullyQualifiedName
        self.fullyQualifiedParametrizedName = fullyQualifiedParametrizedName
        self.Core_IType = Core_IType if Core_IType is not None else set()
        self.Core_IType38 = Core_IType38 if Core_IType38 is not None else set()
        self.Core_IType40 = Core_IType40 if Core_IType40 is not None else set()
        self.Core_IType42 = Core_IType42 if Core_IType42 is not None else set()
        self.Core_IType45 = Core_IType45 if Core_IType45 is not None else set()
        self.Core_IType435 = Core_IType435
        self.Core_IType440 = Core_IType440
        self.Core_IType448 = Core_IType448
        self.Core_IType463 = Core_IType463
        
        pass
    @property
    def fullyQualifiedName(self):
        return self.__fullyQualifiedName

    @fullyQualifiedName.setter
    def fullyQualifiedName(self, fullyQualifiedName: str):
        self.__fullyQualifiedName = fullyQualifiedName


    @property
    def fullyQualifiedParametrizedName(self):
        return self.__fullyQualifiedParametrizedName

    @fullyQualifiedParametrizedName.setter
    def fullyQualifiedParametrizedName(self, fullyQualifiedParametrizedName: str):
        self.__fullyQualifiedParametrizedName = fullyQualifiedParametrizedName


    @property
    def Core_IType42(self):
        return self.__Core_IType42

    @Core_IType42.setter
    def Core_IType42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IType__Core_IType42", None)
        self.__Core_IType42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "IType43"):
                    opp_val = getattr(item, "IType43", None)
                    
                    if opp_val == self:
                        setattr(item, "IType43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IType43"):
                    opp_val = getattr(item, "IType43", None)
                    
                    setattr(item, "IType43", self)
                    

    @property
    def Core_IType440(self):
        return self.__Core_IType440

    @Core_IType440.setter
    def Core_IType440(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IType__Core_IType440", None)
        self.__Core_IType440 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PrimitiveTypes_Core_ICompilationUnit439"):
                opp_val = getattr(old_value, "PrimitiveTypes_Core_ICompilationUnit439", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PrimitiveTypes_Core_ICompilationUnit439"):
                opp_val = getattr(value, "PrimitiveTypes_Core_ICompilationUnit439", None)
                if opp_val is None:
                    setattr(value, "PrimitiveTypes_Core_ICompilationUnit439", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Core_IType45(self):
        return self.__Core_IType45

    @Core_IType45.setter
    def Core_IType45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IType__Core_IType45", None)
        self.__Core_IType45 = value if value is not None else set()
        
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
    def Core_IType38(self):
        return self.__Core_IType38

    @Core_IType38.setter
    def Core_IType38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IType__Core_IType38", None)
        self.__Core_IType38 = value if value is not None else set()
        
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
    def Core_IType448(self):
        return self.__Core_IType448

    @Core_IType448.setter
    def Core_IType448(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IType__Core_IType448", None)
        self.__Core_IType448 = value
        
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
    def Core_IType463(self):
        return self.__Core_IType463

    @Core_IType463.setter
    def Core_IType463(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IType__Core_IType463", None)
        self.__Core_IType463 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PrimitiveTypes_Core_IType462"):
                opp_val = getattr(old_value, "PrimitiveTypes_Core_IType462", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PrimitiveTypes_Core_IType462"):
                opp_val = getattr(value, "PrimitiveTypes_Core_IType462", None)
                if opp_val is None:
                    setattr(value, "PrimitiveTypes_Core_IType462", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Core_IType435(self):
        return self.__Core_IType435

    @Core_IType435.setter
    def Core_IType435(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IType__Core_IType435", None)
        self.__Core_IType435 = value
        
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
                    

    @property
    def Core_IType40(self):
        return self.__Core_IType40

    @Core_IType40.setter
    def Core_IType40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IType__Core_IType40", None)
        self.__Core_IType40 = value if value is not None else set()
        
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
                    

class Core_ISourceRange:

    def __init__(self, length: str, offset: str, Core_ISourceRange: "PrimitiveTypes_Core_ISourceReference" = None, Core_ISourceRange451: "PrimitiveTypes_Core_IMember" = None, Core_ISourceRange454: "PrimitiveTypes_Core_IMember" = None):
        self.length = length
        self.offset = offset
        self.Core_ISourceRange = Core_ISourceRange
        self.Core_ISourceRange451 = Core_ISourceRange451
        self.Core_ISourceRange454 = Core_ISourceRange454
        
        pass
    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length: str):
        self.__length = length


    @property
    def offset(self):
        return self.__offset

    @offset.setter
    def offset(self, offset: str):
        self.__offset = offset


    @property
    def Core_ISourceRange454(self):
        return self.__Core_ISourceRange454

    @Core_ISourceRange454.setter
    def Core_ISourceRange454(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_ISourceRange__Core_ISourceRange454", None)
        self.__Core_ISourceRange454 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PrimitiveTypes_Core_IMember453"):
                opp_val = getattr(old_value, "PrimitiveTypes_Core_IMember453", None)
                if opp_val == self:
                    setattr(old_value, "PrimitiveTypes_Core_IMember453", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PrimitiveTypes_Core_IMember453"):
                opp_val = getattr(value, "PrimitiveTypes_Core_IMember453", None)
                setattr(value, "PrimitiveTypes_Core_IMember453", self)

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
    def Core_ISourceRange451(self):
        return self.__Core_ISourceRange451

    @Core_ISourceRange451.setter
    def Core_ISourceRange451(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_ISourceRange__Core_ISourceRange451", None)
        self.__Core_ISourceRange451 = value
        
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

class ISourceRange:

    pass
class Core_ISourceReference(ABC):

    def __init__(self, source: str, Core_ISourceReference: "ISourceRange" = None):
        self.source = source
        self.Core_ISourceReference = Core_ISourceReference
        
        pass
    @property
    def source(self):
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

class PrimitiveTypes_Core_IMember(Core_IJavaElement, Core_ISourceReference):

    def __init__(self, elementName: str, source: str, PrimitiveTypes_Core_IMember: "Core_ISourceRange" = None, PrimitiveTypes_Core_IMember453: "Core_ISourceRange" = None, Core_ISourceReference: "ISourceRange" = None):
        super().__init__(elementName, source, Core_ISourceReference)
        self.PrimitiveTypes_Core_IMember = PrimitiveTypes_Core_IMember
        self.PrimitiveTypes_Core_IMember453 = PrimitiveTypes_Core_IMember453
        
        pass
    @property
    def PrimitiveTypes_Core_IMember453(self):
        return self.__PrimitiveTypes_Core_IMember453

    @PrimitiveTypes_Core_IMember453.setter
    def PrimitiveTypes_Core_IMember453(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PrimitiveTypes_Core_IMember__PrimitiveTypes_Core_IMember453", None)
        self.__PrimitiveTypes_Core_IMember453 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Core_ISourceRange454"):
                opp_val = getattr(old_value, "Core_ISourceRange454", None)
                if opp_val == self:
                    setattr(old_value, "Core_ISourceRange454", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Core_ISourceRange454"):
                opp_val = getattr(value, "Core_ISourceRange454", None)
                setattr(value, "Core_ISourceRange454", self)

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
            if hasattr(old_value, "Core_ISourceRange451"):
                opp_val = getattr(old_value, "Core_ISourceRange451", None)
                if opp_val == self:
                    setattr(old_value, "Core_ISourceRange451", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Core_ISourceRange451"):
                opp_val = getattr(value, "Core_ISourceRange451", None)
                setattr(value, "Core_ISourceRange451", self)

class PrimitiveTypes_Core_IImportDeclaration(Core_IJavaElement, Core_ISourceReference):

    def __init__(self, elementName: str, source: str, isOnDemand: str, isStatic: str, Core_ISourceReference: "ISourceRange" = None):
        super().__init__(elementName, source, Core_ISourceReference)
        self.isOnDemand = isOnDemand
        self.isStatic = isStatic
        
        pass
    @property
    def isOnDemand(self):
        return self.__isOnDemand

    @isOnDemand.setter
    def isOnDemand(self, isOnDemand: str):
        self.__isOnDemand = isOnDemand


    @property
    def isStatic(self):
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: str):
        self.__isStatic = isStatic


class PrimitiveTypes_Core_ITypeParameter(Core_IJavaElement, Core_ISourceReference):

    def __init__(self, elementName: str, source: str, bounds: str, Core_ISourceReference: "ISourceRange" = None):
        super().__init__(elementName, source, Core_ISourceReference)
        self.bounds = bounds
        
        pass
    @property
    def bounds(self):
        return self.__bounds

    @bounds.setter
    def bounds(self, bounds: str):
        self.__bounds = bounds


class Core_IClassFile(ITypeRoot):

    def __init__(self, isClass: str, isInterface: str, Core_IClassFile: "IType" = None, Core_IClassFile430: "PrimitiveTypes_Core_IPackageFragment" = None):
        self.isClass = isClass
        self.isInterface = isInterface
        self.Core_IClassFile = Core_IClassFile
        self.Core_IClassFile430 = Core_IClassFile430
        
        pass
    @property
    def isClass(self):
        return self.__isClass

    @isClass.setter
    def isClass(self, isClass: str):
        self.__isClass = isClass


    @property
    def isInterface(self):
        return self.__isInterface

    @isInterface.setter
    def isInterface(self, isInterface: str):
        self.__isInterface = isInterface


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
            if hasattr(old_value, "IType29"):
                opp_val = getattr(old_value, "IType29", None)
                if opp_val == self:
                    setattr(old_value, "IType29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IType29"):
                opp_val = getattr(value, "IType29", None)
                setattr(value, "IType29", self)

    @property
    def Core_IClassFile430(self):
        return self.__Core_IClassFile430

    @Core_IClassFile430.setter
    def Core_IClassFile430(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IClassFile__Core_IClassFile430", None)
        self.__Core_IClassFile430 = value
        
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

class CompilationUnit:

    pass
class Core_IField(IMember):

    def __init__(self, constant: str, isEnumConstant: str, typeSignature: str, isVolatile: str, isTransient: str, Core_IField: "PrimitiveTypes_Core_IType" = None):
        self.constant = constant
        self.isEnumConstant = isEnumConstant
        self.typeSignature = typeSignature
        self.isVolatile = isVolatile
        self.isTransient = isTransient
        self.Core_IField = Core_IField
        
        pass
    @property
    def constant(self):
        return self.__constant

    @constant.setter
    def constant(self, constant: str):
        self.__constant = constant


    @property
    def isTransient(self):
        return self.__isTransient

    @isTransient.setter
    def isTransient(self, isTransient: str):
        self.__isTransient = isTransient


    @property
    def isEnumConstant(self):
        return self.__isEnumConstant

    @isEnumConstant.setter
    def isEnumConstant(self, isEnumConstant: str):
        self.__isEnumConstant = isEnumConstant


    @property
    def typeSignature(self):
        return self.__typeSignature

    @typeSignature.setter
    def typeSignature(self, typeSignature: str):
        self.__typeSignature = typeSignature


    @property
    def isVolatile(self):
        return self.__isVolatile

    @isVolatile.setter
    def isVolatile(self, isVolatile: str):
        self.__isVolatile = isVolatile


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
            if hasattr(old_value, "PrimitiveTypes_Core_IType457"):
                opp_val = getattr(old_value, "PrimitiveTypes_Core_IType457", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PrimitiveTypes_Core_IType457"):
                opp_val = getattr(value, "PrimitiveTypes_Core_IType457", None)
                if opp_val is None:
                    setattr(value, "PrimitiveTypes_Core_IType457", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Core_IInitializer(IMember):

    pass
class ITypeParameter:

    pass
class ICompilationUnit:

    pass
class IClassFile:

    pass
class IPackageFragment:

    pass
class IJavaElement:

    pass
class Core_IMember(ISourceReference, IJavaElement):

    pass
class Core_ITypeParameter(ISourceReference, IJavaElement):

    def __init__(self, bounds: str, Core_ITypeParameter: "PrimitiveTypes_Core_IType" = None):
        self.bounds = bounds
        self.Core_ITypeParameter = Core_ITypeParameter
        
        pass
    @property
    def bounds(self):
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
            if hasattr(old_value, "PrimitiveTypes_Core_IType465"):
                opp_val = getattr(old_value, "PrimitiveTypes_Core_IType465", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PrimitiveTypes_Core_IType465"):
                opp_val = getattr(value, "PrimitiveTypes_Core_IType465", None)
                if opp_val is None:
                    setattr(value, "PrimitiveTypes_Core_IType465", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Core_IImportDeclaration(ISourceReference, IJavaElement):

    def __init__(self, isOnDemand: str, isStatic: str, Core_IImportDeclaration: "PrimitiveTypes_Core_ICompilationUnit" = None):
        self.isOnDemand = isOnDemand
        self.isStatic = isStatic
        self.Core_IImportDeclaration = Core_IImportDeclaration
        
        pass
    @property
    def isOnDemand(self):
        return self.__isOnDemand

    @isOnDemand.setter
    def isOnDemand(self, isOnDemand: str):
        self.__isOnDemand = isOnDemand


    @property
    def isStatic(self):
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: str):
        self.__isStatic = isStatic


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
            if hasattr(old_value, "PrimitiveTypes_Core_ICompilationUnit437"):
                opp_val = getattr(old_value, "PrimitiveTypes_Core_ICompilationUnit437", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PrimitiveTypes_Core_ICompilationUnit437"):
                opp_val = getattr(value, "PrimitiveTypes_Core_ICompilationUnit437", None)
                if opp_val is None:
                    setattr(value, "PrimitiveTypes_Core_ICompilationUnit437", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class IPackageFragmentRoot:

    pass
class Core_SourcePackageFragmentRoot(IPackageFragmentRoot):

    pass
class Core_BinaryPackageFragmentRoot(IPackageFragmentRoot):

    pass
class PrimitiveTypes_Core_BinaryPackageFragmentRoot(IPackageFragmentRoot):

    pass
class PrimitiveTypes_Core_SourcePackageFragmentRoot(IPackageFragmentRoot):

    pass
class IJavaProject:

    pass
class PhysicalElement:

    pass
class Core_ITypeRoot(PhysicalElement, ISourceReference, IJavaElement):

    pass
class PrimitiveTypes_Core_IJavaModel(PhysicalElement):

    pass
class Core_IPackageFragment(PhysicalElement, IJavaElement):

    def __init__(self, isDefaultPackage: str, Core_IPackageFragment16: set["ICompilationUnit"] = None, packageFragments: "IPackageFragmentRoot" = None, Core_IPackageFragment: set["IClassFile"] = None, IPackageFragment425: "PrimitiveTypes_Core_IPackageFragmentRoot" = None):
        self.isDefaultPackage = isDefaultPackage
        self.Core_IPackageFragment16 = Core_IPackageFragment16 if Core_IPackageFragment16 is not None else set()
        self.packageFragments = packageFragments
        self.Core_IPackageFragment = Core_IPackageFragment if Core_IPackageFragment is not None else set()
        self.IPackageFragment425 = IPackageFragment425
        
        pass
    @property
    def isDefaultPackage(self):
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
    def IPackageFragment425(self):
        return self.__IPackageFragment425

    @IPackageFragment425.setter
    def IPackageFragment425(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IPackageFragment__IPackageFragment425", None)
        self.__IPackageFragment425 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "packageFragmentRoot424"):
                opp_val = getattr(old_value, "packageFragmentRoot424", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "packageFragmentRoot424"):
                opp_val = getattr(value, "packageFragmentRoot424", None)
                if opp_val is None:
                    setattr(value, "packageFragmentRoot424", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Core_IPackageFragment16(self):
        return self.__Core_IPackageFragment16

    @Core_IPackageFragment16.setter
    def Core_IPackageFragment16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IPackageFragment__Core_IPackageFragment16", None)
        self.__Core_IPackageFragment16 = value if value is not None else set()
        
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
    def packageFragments(self):
        return self.__packageFragments

    @packageFragments.setter
    def packageFragments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IPackageFragment__packageFragments", None)
        self.__packageFragments = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IPackageFragmentRoot13"):
                opp_val = getattr(old_value, "IPackageFragmentRoot13", None)
                if opp_val == self:
                    setattr(old_value, "IPackageFragmentRoot13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IPackageFragmentRoot13"):
                opp_val = getattr(value, "IPackageFragmentRoot13", None)
                setattr(value, "IPackageFragmentRoot13", self)

class Core_IPackageFragmentRoot(PhysicalElement, IJavaElement):

    pass
class Core_IJavaProject(PhysicalElement, IJavaElement):

    pass
class Core_IJavaModel(PhysicalElement):

    pass
class Core_PhysicalElement(ABC):

    def __init__(self, path: str, isReadOnly: str):
        self.path = path
        self.isReadOnly = isReadOnly
        
        pass
    @property
    def isReadOnly(self):
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: str):
        self.__isReadOnly = isReadOnly


    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path


class PrimitiveTypes_Core_IPackageFragment(Core_IJavaElement, Core_PhysicalElement):

    def __init__(self, elementName: str, path: str, isReadOnly: str, isDefaultPackage: str, packageFragments427: "Core_IPackageFragmentRoot" = None, PrimitiveTypes_Core_IPackageFragment: set["Core_IClassFile"] = None, PrimitiveTypes_Core_IPackageFragment432: set["Core_ICompilationUnit"] = None):
        super().__init__(elementName, path, isReadOnly)
        self.isDefaultPackage = isDefaultPackage
        self.packageFragments427 = packageFragments427
        self.PrimitiveTypes_Core_IPackageFragment = PrimitiveTypes_Core_IPackageFragment if PrimitiveTypes_Core_IPackageFragment is not None else set()
        self.PrimitiveTypes_Core_IPackageFragment432 = PrimitiveTypes_Core_IPackageFragment432 if PrimitiveTypes_Core_IPackageFragment432 is not None else set()
        
        pass
    @property
    def isDefaultPackage(self):
        return self.__isDefaultPackage

    @isDefaultPackage.setter
    def isDefaultPackage(self, isDefaultPackage: str):
        self.__isDefaultPackage = isDefaultPackage


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
                if hasattr(item, "Core_IClassFile430"):
                    opp_val = getattr(item, "Core_IClassFile430", None)
                    
                    if opp_val == self:
                        setattr(item, "Core_IClassFile430", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Core_IClassFile430"):
                    opp_val = getattr(item, "Core_IClassFile430", None)
                    
                    setattr(item, "Core_IClassFile430", self)
                    

    @property
    def PrimitiveTypes_Core_IPackageFragment432(self):
        return self.__PrimitiveTypes_Core_IPackageFragment432

    @PrimitiveTypes_Core_IPackageFragment432.setter
    def PrimitiveTypes_Core_IPackageFragment432(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PrimitiveTypes_Core_IPackageFragment__PrimitiveTypes_Core_IPackageFragment432", None)
        self.__PrimitiveTypes_Core_IPackageFragment432 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Core_ICompilationUnit433"):
                    opp_val = getattr(item, "Core_ICompilationUnit433", None)
                    
                    if opp_val == self:
                        setattr(item, "Core_ICompilationUnit433", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Core_ICompilationUnit433"):
                    opp_val = getattr(item, "Core_ICompilationUnit433", None)
                    
                    setattr(item, "Core_ICompilationUnit433", self)
                    

    @property
    def packageFragments427(self):
        return self.__packageFragments427

    @packageFragments427.setter
    def packageFragments427(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PrimitiveTypes_Core_IPackageFragment__packageFragments427", None)
        self.__packageFragments427 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IPackageFragmentRoot428"):
                opp_val = getattr(old_value, "IPackageFragmentRoot428", None)
                if opp_val == self:
                    setattr(old_value, "IPackageFragmentRoot428", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IPackageFragmentRoot428"):
                opp_val = getattr(value, "IPackageFragmentRoot428", None)
                setattr(value, "IPackageFragmentRoot428", self)

class PrimitiveTypes_Core_ITypeRoot(Core_IJavaElement, Core_ISourceReference, Core_PhysicalElement):

    def __init__(self, elementName: str, path: str, isReadOnly: str, source: str, Core_ISourceReference: "ISourceRange" = None):
        super().__init__(elementName, path, isReadOnly, source, Core_ISourceReference)
        
        pass
class PrimitiveTypes_Core_IJavaProject(Core_IJavaElement, Core_PhysicalElement):

    def __init__(self, elementName: str, path: str, isReadOnly: str, PrimitiveTypes_Core_IJavaProject: set["Core_IPackageFragmentRoot"] = None, PrimitiveTypes_Core_IJavaProject418: set["Core_IPackageFragmentRoot"] = None, PrimitiveTypes_Core_IJavaProject421: set["Core_IJavaProject"] = None):
        super().__init__(elementName, path, isReadOnly)
        self.PrimitiveTypes_Core_IJavaProject = PrimitiveTypes_Core_IJavaProject if PrimitiveTypes_Core_IJavaProject is not None else set()
        self.PrimitiveTypes_Core_IJavaProject418 = PrimitiveTypes_Core_IJavaProject418 if PrimitiveTypes_Core_IJavaProject418 is not None else set()
        self.PrimitiveTypes_Core_IJavaProject421 = PrimitiveTypes_Core_IJavaProject421 if PrimitiveTypes_Core_IJavaProject421 is not None else set()
        
        pass
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
                    

class PrimitiveTypes_Core_IPackageFragmentRoot(Core_IJavaElement, Core_PhysicalElement):

    def __init__(self, elementName: str, path: str, isReadOnly: str, packageFragmentRoot424: set["Core_IPackageFragment"] = None):
        super().__init__(elementName, path, isReadOnly)
        self.packageFragmentRoot424 = packageFragmentRoot424 if packageFragmentRoot424 is not None else set()
        
        pass
    @property
    def packageFragmentRoot424(self):
        return self.__packageFragmentRoot424

    @packageFragmentRoot424.setter
    def packageFragmentRoot424(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PrimitiveTypes_Core_IPackageFragmentRoot__packageFragmentRoot424", None)
        self.__packageFragmentRoot424 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "IPackageFragment425"):
                    opp_val = getattr(item, "IPackageFragment425", None)
                    
                    if opp_val == self:
                        setattr(item, "IPackageFragment425", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IPackageFragment425"):
                    opp_val = getattr(item, "IPackageFragment425", None)
                    
                    setattr(item, "IPackageFragment425", self)
                    
