from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class CppVarType(Enum):
    OBJECT = "OBJECT"
    REFERENCE = "REFERENCE"
    POINTER = "POINTER"
class CppAccessSpecifier(Enum):
    PRIVATE = "PRIVATE"
    PROTECTED = "PROTECTED"
    PUBLIC = "PUBLIC"
class CppStorageType(Enum):
    AUTO = "AUTO"
    REGISTER = "REGISTER"
    STATIC = "STATIC"
    EXTERN = "EXTERN"
    TYPEDEF = "TYPEDEF"
    THREAD_LOCAL = "THREAD_LOCAL"
    MUTABLE = "MUTABLE"
class CppPostfixOperator(Enum):
    DECREMENT = "DECREMENT"
    INCREMENT = "INCREMENT"
class CppQualifierType(Enum):
    CONST = "CONST"
    VOLATILE = "VOLATILE"
    RESTRICT = "RESTRICT"
    ATOMIC = "ATOMIC"
class CppLinkageSpecifier(Enum):
    STATIC = "STATIC"
    EXTERN = "EXTERN"
class CppAssignmentOperator(Enum):
    ASSIGN = "ASSIGN"
    TIMES_ASSIGN = "TIMES_ASSIGN"
    DIVISSION_ASSIGN = "DIVISSION_ASSIGN"
    MODULO_ASSIGN = "MODULO_ASSIGN"
    PLUS_ASSIGN = "PLUS_ASSIGN"
    MINUS_ASSIGN = "MINUS_ASSIGN"
    SHIFT_LEFT_ASSIGN = "SHIFT_LEFT_ASSIGN"
    SHIFT_RIGHT_ASSIGN = "SHIFT_RIGHT_ASSIGN"
    AND_ASSIGN = "AND_ASSIGN"
    XOR_ASSIGN = "XOR_ASSIGN"
    OR_ASSIGN = "OR_ASSIGN"
class CppOperator(Enum):
    TIMES = "TIMES"
    DIVISION = "DIVISION"
    SHIFT_LEFT = "SHIFT_LEFT"
    SHIFT_RIGHT = "SHIFT_RIGHT"
    XOR = "XOR"
    BIT_OR = "BIT_OR"
    REMAINDER = "REMAINDER"
    BIT_AND = "BIT_AND"
    GREATER_EQUALS = "GREATER_EQUALS"
    OR = "OR"
    MINUS = "MINUS"
    XOR_EQ = "XOR_EQ"
    LESS_EQUALS = "LESS_EQUALS"
    EQUALS = "EQUALS"
    NOT_EQUALS = "NOT_EQUALS"
    AND = "AND"
    PLUS = "PLUS"
    GREATER_THAN = "GREATER_THAN"
    LESS_THAN = "LESS_THAN"
class CppUnaryOperator(Enum):
    AMPERSAND = "AMPERSAND"
    ASTERISK = "ASTERISK"
    PLUS = "PLUS"
    MINUS = "MINUS"
    BIT_NOT = "BIT_NOT"
    NOT = "NOT"
    INCREMENT = "INCREMENT"
    DECREMENT = "DECREMENT"
class CppClassKey(Enum):
    CLASS = "CLASS"
    STRUCT = "STRUCT"
    UNION = "UNION"


############################################
# Definition of Classes
############################################

class CppBinaryExpression:

    pass
class Metamodelo_Cpp_CppAssignamentStatement(CppBinaryExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


class CppUnaryExpression:

    pass
class Metamodelo_Cpp_CppPrefixExpression(CppUnaryExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


class Metamodelo_Cpp_CppPostfixExpression(CppUnaryExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


class Metamodelo_Cpp_CppInfixExpression(CppBinaryExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


class CppSelectionStatement:

    pass
class Metamodelo_Cpp_CppIfElseStatement(CppSelectionStatement):

    def __init__(self, inLine: bool, Metamodelo_Cpp_CppIfElseStatement: "Metamodelo_Cpp_CppExpression" = None):
        self.inLine = inLine
        self.Metamodelo_Cpp_CppIfElseStatement = Metamodelo_Cpp_CppIfElseStatement
        
        pass
    @property
    def inLine(self):
        return self.__inLine

    @inLine.setter
    def inLine(self, inLine: bool):
        self.__inLine = inLine


    @property
    def Metamodelo_Cpp_CppIfElseStatement(self):
        return self.__Metamodelo_Cpp_CppIfElseStatement

    @Metamodelo_Cpp_CppIfElseStatement.setter
    def Metamodelo_Cpp_CppIfElseStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Metamodelo_Cpp_CppIfElseStatement__Metamodelo_Cpp_CppIfElseStatement", None)
        self.__Metamodelo_Cpp_CppIfElseStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Metamodelo_Cpp_CppExpression73"):
                opp_val = getattr(old_value, "Metamodelo_Cpp_CppExpression73", None)
                if opp_val == self:
                    setattr(old_value, "Metamodelo_Cpp_CppExpression73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Metamodelo_Cpp_CppExpression73"):
                opp_val = getattr(value, "Metamodelo_Cpp_CppExpression73", None)
                setattr(value, "Metamodelo_Cpp_CppExpression73", self)

class Metamodelo_Cpp_CppIfStatement(CppSelectionStatement):

    pass
class CppMethodInvocation:

    pass
class Metamodelo_Cpp_CppSuperConstructorInvocation(CppMethodInvocation):

    pass
class CppJumpStatement:

    pass
class Metamodelo_Cpp_CppReturnStatement(CppJumpStatement):

    pass
class Metamodelo_Cpp_CppGotoStatement(CppJumpStatement):

    pass
class Metamodelo_Cpp_CppContinueStatement(CppJumpStatement):

    pass
class Metamodelo_Cpp_CppBreakStatement(CppJumpStatement):

    pass
class CppIterationStatement:

    pass
class Metamodelo_Cpp_CppDoWhileStatement(CppIterationStatement):

    pass
class Metamodelo_Cpp_CppForStatement(CppIterationStatement):

    pass
class Metamodelo_Cpp_CppWhileStatement(CppIterationStatement):

    pass
class CppExpression:

    pass
class Metamodelo_Cpp_CppNullLiteral(CppExpression):

    pass
class Metamodelo_Cpp_CppBinaryExpression(CppExpression):

    pass
class Metamodelo_Cpp_CppFieldAccess(CppExpression):

    pass
class Metamodelo_Cpp_CppThisExpression(CppExpression):

    pass
class Metamodelo_Cpp_CppCharacterLiteral(CppExpression):

    def __init__(self, charValue: str):
        self.charValue = charValue
        
        pass
    @property
    def charValue(self):
        return self.__charValue

    @charValue.setter
    def charValue(self, charValue: str):
        self.__charValue = charValue


class Metamodelo_Cpp_CppStringLiteral(CppExpression):

    def __init__(self, literalValue: str):
        self.literalValue = literalValue
        
        pass
    @property
    def literalValue(self):
        return self.__literalValue

    @literalValue.setter
    def literalValue(self, literalValue: str):
        self.__literalValue = literalValue


class Metamodelo_Cpp_CppRegexLiteral(CppExpression):

    def __init__(self, pattern: str, options: str):
        self.pattern = pattern
        self.options = options
        
        pass
    @property
    def options(self):
        return self.__options

    @options.setter
    def options(self, options: str):
        self.__options = options


    @property
    def pattern(self):
        return self.__pattern

    @pattern.setter
    def pattern(self, pattern: str):
        self.__pattern = pattern


class Metamodelo_Cpp_CppSelectionStatement(CppExpression):

    pass
class Metamodelo_Cpp_CppNumberLiteral(CppExpression):

    def __init__(self, token: str):
        self.token = token
        
        pass
    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self, token: str):
        self.__token = token


class Metamodelo_Cpp_CppUnaryExpression(CppExpression):

    pass
class Metamodelo_Cpp_CppIterationStatement(CppExpression):

    pass
class Metamodelo_Cpp_CppDeclarationExpression(CppExpression):

    pass
class Metamodelo_Cpp_CppJumpStatement(CppExpression):

    pass
class Metamodelo_Cpp_CppCastExpression(CppExpression):

    pass
class Metamodelo_Cpp_CppArrayAccess(CppExpression):

    pass
class Metamodelo_Cpp_CppVariableAccess(CppExpression):

    pass
class Metamodelo_Cpp_CppParenthizedExpression(CppExpression):

    pass
class Metamodelo_Cpp_CppBlock(CppExpression):

    pass
class Metamodelo_Cpp_CppTryExpression(CppExpression):

    pass
class Metamodelo_Cpp_CppCatchClause(CppExpression):

    pass
class Metamodelo_Cpp_CppSwitchExpression(CppExpression):

    pass
class Metamodelo_Cpp_CppBooleanLiteral(CppExpression):

    def __init__(self, booleanValue: bool):
        self.booleanValue = booleanValue
        
        pass
    @property
    def booleanValue(self):
        return self.__booleanValue

    @booleanValue.setter
    def booleanValue(self, booleanValue: bool):
        self.__booleanValue = booleanValue


class Metamodelo_Cpp_CppThrowExpression(CppExpression):

    pass
class Metamodelo_Cpp_CppCase(CppExpression):

    pass
class Metamodelo_Cpp_CppArrayInitializer(CppExpression):

    pass
class CppTypedElement:

    pass
class Metamodelo_Cpp_CppVariableDeclarationGroup(CppTypedElement):

    pass
class CppField:

    pass
class CppVariableDeclaration:

    pass
class Metamodelo_Cpp_CppVariableDeclarationFragment(CppVariableDeclaration):

    pass
class Metamodelo_Cpp_CppSingleVariableDeclaration(CppTypedElement, CppVariableDeclaration):

    pass
class CppAbstractMethodInvocation:

    pass
class Metamodelo_Cpp_CppSuperMethodInvocation(CppAbstractMethodInvocation):

    pass
class Metamodelo_Cpp_CppMethodInvocation(CppAbstractMethodInvocation):

    pass
class Metamodelo_Cpp_CppAbstractMethodInvocation(CppExpression):

    pass
class CppMemberFunction:

    pass
class Metamodelo_Cpp_CppMethod(CppTypedElement, CppMemberFunction):

    def __init__(self, isFinal: bool, isConst: bool, isVirtual: bool, isPureVirtual: bool):
        self.isFinal = isFinal
        self.isConst = isConst
        self.isVirtual = isVirtual
        self.isPureVirtual = isPureVirtual
        
        pass
    @property
    def isVirtual(self):
        return self.__isVirtual

    @isVirtual.setter
    def isVirtual(self, isVirtual: bool):
        self.__isVirtual = isVirtual


    @property
    def isPureVirtual(self):
        return self.__isPureVirtual

    @isPureVirtual.setter
    def isPureVirtual(self, isPureVirtual: bool):
        self.__isPureVirtual = isPureVirtual


    @property
    def isFinal(self):
        return self.__isFinal

    @isFinal.setter
    def isFinal(self, isFinal: bool):
        self.__isFinal = isFinal


    @property
    def isConst(self):
        return self.__isConst

    @isConst.setter
    def isConst(self, isConst: bool):
        self.__isConst = isConst


class Metamodelo_Cpp_CppDestructor(CppMemberFunction):

    def __init__(self, isVirtual: bool):
        self.isVirtual = isVirtual
        
        pass
    @property
    def isVirtual(self):
        return self.__isVirtual

    @isVirtual.setter
    def isVirtual(self, isVirtual: bool):
        self.__isVirtual = isVirtual


class Metamodelo_Cpp_CppConstructor(CppMemberFunction):

    pass
class CppFunction:

    pass
class CppClassifier:

    pass
class CppPrimitiveType:

    pass
class Metamodelo_Cpp_CppVoidType(CppPrimitiveType):

    pass
class Metamodelo_Cpp_CppCharType(CppPrimitiveType):

    pass
class Metamodelo_Cpp_CppFloatType(CppPrimitiveType):

    pass
class Metamodelo_Cpp_CppShortType(CppPrimitiveType):

    pass
class Metamodelo_Cpp_CppUnsignedType(CppPrimitiveType):

    pass
class Metamodelo_Cpp_CppIntType(CppPrimitiveType):

    pass
class Metamodelo_Cpp_CppLongType(CppPrimitiveType):

    pass
class Metamodelo_Cpp_CppDoubleType(CppPrimitiveType):

    pass
class Metamodelo_Cpp_CppSignedType(CppPrimitiveType):

    pass
class Metamodelo_Cpp_CppBooleanType(CppPrimitiveType):

    pass
class CppType:

    pass
class Metamodelo_Cpp_CppPrimitiveType(CppType):

    pass
class Metamodelo_Cpp_CppTypeParameter(CppType):

    pass
class Metamodelo_Cpp_CppTypeAccess(CppExpression):

    pass
class Metamodelo_Cpp_CppModelElement(ABC):

    pass
class Metamodelo_Cpp_CppEnum(CppType):

    pass
class Metamodelo_Cpp_CppVariable(CppTypedElement, CppField, CppVariableDeclaration, CppType):

    def __init__(self, isConst: bool, storage: str, Metamodelo_Cpp_CppVariable: "Metamodelo_Cpp_CppClassifier" = None):
        self.isConst = isConst
        self.storage = storage
        self.Metamodelo_Cpp_CppVariable = Metamodelo_Cpp_CppVariable
        
        pass
    @property
    def storage(self):
        return self.__storage

    @storage.setter
    def storage(self, storage: str):
        self.__storage = storage


    @property
    def isConst(self):
        return self.__isConst

    @isConst.setter
    def isConst(self, isConst: bool):
        self.__isConst = isConst


    @property
    def Metamodelo_Cpp_CppVariable(self):
        return self.__Metamodelo_Cpp_CppVariable

    @Metamodelo_Cpp_CppVariable.setter
    def Metamodelo_Cpp_CppVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Metamodelo_Cpp_CppVariable__Metamodelo_Cpp_CppVariable", None)
        self.__Metamodelo_Cpp_CppVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Metamodelo_Cpp_CppClassifier35"):
                opp_val = getattr(old_value, "Metamodelo_Cpp_CppClassifier35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Metamodelo_Cpp_CppClassifier35"):
                opp_val = getattr(value, "Metamodelo_Cpp_CppClassifier35", None)
                if opp_val is None:
                    setattr(value, "Metamodelo_Cpp_CppClassifier35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Metamodelo_Cpp_CppMemberFunction(CppField, CppFunction):

    pass
class CppFieldContainer:

    pass
class Metamodelo_Cpp_CppClassifier(CppFieldContainer, CppType):

    pass
class Metamodelo_Cpp_CppClass(CppClassifier):

    def __init__(self, isAbstract: bool, classkey: str, isGeneric: bool, isFinal: bool, Metamodelo_Cpp_CppClass41: "Metamodelo_Cpp_CppClass" = None, Metamodelo_Cpp_CppClass39: set["Metamodelo_Cpp_CppClass"] = None, Metamodelo_Cpp_CppClass: "Metamodelo_Cpp_CppModel" = None):
        self.isAbstract = isAbstract
        self.classkey = classkey
        self.isGeneric = isGeneric
        self.isFinal = isFinal
        self.Metamodelo_Cpp_CppClass41 = Metamodelo_Cpp_CppClass41
        self.Metamodelo_Cpp_CppClass39 = Metamodelo_Cpp_CppClass39 if Metamodelo_Cpp_CppClass39 is not None else set()
        self.Metamodelo_Cpp_CppClass = Metamodelo_Cpp_CppClass
        
        pass
    @property
    def classkey(self):
        return self.__classkey

    @classkey.setter
    def classkey(self, classkey: str):
        self.__classkey = classkey


    @property
    def isFinal(self):
        return self.__isFinal

    @isFinal.setter
    def isFinal(self, isFinal: bool):
        self.__isFinal = isFinal


    @property
    def isGeneric(self):
        return self.__isGeneric

    @isGeneric.setter
    def isGeneric(self, isGeneric: bool):
        self.__isGeneric = isGeneric


    @property
    def isAbstract(self):
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract


    @property
    def Metamodelo_Cpp_CppClass(self):
        return self.__Metamodelo_Cpp_CppClass

    @Metamodelo_Cpp_CppClass.setter
    def Metamodelo_Cpp_CppClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Metamodelo_Cpp_CppClass__Metamodelo_Cpp_CppClass", None)
        self.__Metamodelo_Cpp_CppClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Metamodelo_Cpp_CppModel"):
                opp_val = getattr(old_value, "Metamodelo_Cpp_CppModel", None)
                if opp_val == self:
                    setattr(old_value, "Metamodelo_Cpp_CppModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Metamodelo_Cpp_CppModel"):
                opp_val = getattr(value, "Metamodelo_Cpp_CppModel", None)
                setattr(value, "Metamodelo_Cpp_CppModel", self)

    @property
    def Metamodelo_Cpp_CppClass41(self):
        return self.__Metamodelo_Cpp_CppClass41

    @Metamodelo_Cpp_CppClass41.setter
    def Metamodelo_Cpp_CppClass41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Metamodelo_Cpp_CppClass__Metamodelo_Cpp_CppClass41", None)
        self.__Metamodelo_Cpp_CppClass41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Metamodelo_Cpp_CppClass39"):
                opp_val = getattr(old_value, "Metamodelo_Cpp_CppClass39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Metamodelo_Cpp_CppClass39"):
                opp_val = getattr(value, "Metamodelo_Cpp_CppClass39", None)
                if opp_val is None:
                    setattr(value, "Metamodelo_Cpp_CppClass39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Metamodelo_Cpp_CppClass39(self):
        return self.__Metamodelo_Cpp_CppClass39

    @Metamodelo_Cpp_CppClass39.setter
    def Metamodelo_Cpp_CppClass39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Metamodelo_Cpp_CppClass__Metamodelo_Cpp_CppClass39", None)
        self.__Metamodelo_Cpp_CppClass39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Metamodelo_Cpp_CppClass41"):
                    opp_val = getattr(item, "Metamodelo_Cpp_CppClass41", None)
                    
                    if opp_val == self:
                        setattr(item, "Metamodelo_Cpp_CppClass41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Metamodelo_Cpp_CppClass41"):
                    opp_val = getattr(item, "Metamodelo_Cpp_CppClass41", None)
                    
                    setattr(item, "Metamodelo_Cpp_CppClass41", self)
                    

class Metamodelo_Cpp_CppModel:

    def __init__(self, name: str, sourceFolder: str, targetFolder: str, Metamodelo_Cpp_CppModel4: set["Metamodelo_Cpp_CppType"] = None, Metamodelo_Cpp_CppModel6: set["Metamodelo_Cpp_CppClassFile"] = None, Metamodelo_Cpp_CppModel: "Metamodelo_Cpp_CppClass" = None, Metamodelo_Cpp_CppModel2: set["Metamodelo_Cpp_CppPathReferentiable"] = None):
        self.name = name
        self.sourceFolder = sourceFolder
        self.targetFolder = targetFolder
        self.Metamodelo_Cpp_CppModel4 = Metamodelo_Cpp_CppModel4 if Metamodelo_Cpp_CppModel4 is not None else set()
        self.Metamodelo_Cpp_CppModel6 = Metamodelo_Cpp_CppModel6 if Metamodelo_Cpp_CppModel6 is not None else set()
        self.Metamodelo_Cpp_CppModel = Metamodelo_Cpp_CppModel
        self.Metamodelo_Cpp_CppModel2 = Metamodelo_Cpp_CppModel2 if Metamodelo_Cpp_CppModel2 is not None else set()
        
        pass
    @property
    def targetFolder(self):
        return self.__targetFolder

    @targetFolder.setter
    def targetFolder(self, targetFolder: str):
        self.__targetFolder = targetFolder


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def sourceFolder(self):
        return self.__sourceFolder

    @sourceFolder.setter
    def sourceFolder(self, sourceFolder: str):
        self.__sourceFolder = sourceFolder


    @property
    def Metamodelo_Cpp_CppModel4(self):
        return self.__Metamodelo_Cpp_CppModel4

    @Metamodelo_Cpp_CppModel4.setter
    def Metamodelo_Cpp_CppModel4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Metamodelo_Cpp_CppModel__Metamodelo_Cpp_CppModel4", None)
        self.__Metamodelo_Cpp_CppModel4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Metamodelo_Cpp_CppType"):
                    opp_val = getattr(item, "Metamodelo_Cpp_CppType", None)
                    
                    if opp_val == self:
                        setattr(item, "Metamodelo_Cpp_CppType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Metamodelo_Cpp_CppType"):
                    opp_val = getattr(item, "Metamodelo_Cpp_CppType", None)
                    
                    setattr(item, "Metamodelo_Cpp_CppType", self)
                    

    @property
    def Metamodelo_Cpp_CppModel2(self):
        return self.__Metamodelo_Cpp_CppModel2

    @Metamodelo_Cpp_CppModel2.setter
    def Metamodelo_Cpp_CppModel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Metamodelo_Cpp_CppModel__Metamodelo_Cpp_CppModel2", None)
        self.__Metamodelo_Cpp_CppModel2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Metamodelo_Cpp_CppPathReferentiable"):
                    opp_val = getattr(item, "Metamodelo_Cpp_CppPathReferentiable", None)
                    
                    if opp_val == self:
                        setattr(item, "Metamodelo_Cpp_CppPathReferentiable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Metamodelo_Cpp_CppPathReferentiable"):
                    opp_val = getattr(item, "Metamodelo_Cpp_CppPathReferentiable", None)
                    
                    setattr(item, "Metamodelo_Cpp_CppPathReferentiable", self)
                    

    @property
    def Metamodelo_Cpp_CppModel6(self):
        return self.__Metamodelo_Cpp_CppModel6

    @Metamodelo_Cpp_CppModel6.setter
    def Metamodelo_Cpp_CppModel6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Metamodelo_Cpp_CppModel__Metamodelo_Cpp_CppModel6", None)
        self.__Metamodelo_Cpp_CppModel6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Metamodelo_Cpp_CppClassFile"):
                    opp_val = getattr(item, "Metamodelo_Cpp_CppClassFile", None)
                    
                    if opp_val == self:
                        setattr(item, "Metamodelo_Cpp_CppClassFile", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Metamodelo_Cpp_CppClassFile"):
                    opp_val = getattr(item, "Metamodelo_Cpp_CppClassFile", None)
                    
                    setattr(item, "Metamodelo_Cpp_CppClassFile", self)
                    

    @property
    def Metamodelo_Cpp_CppModel(self):
        return self.__Metamodelo_Cpp_CppModel

    @Metamodelo_Cpp_CppModel.setter
    def Metamodelo_Cpp_CppModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Metamodelo_Cpp_CppModel__Metamodelo_Cpp_CppModel", None)
        self.__Metamodelo_Cpp_CppModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Metamodelo_Cpp_CppClass"):
                opp_val = getattr(old_value, "Metamodelo_Cpp_CppClass", None)
                if opp_val == self:
                    setattr(old_value, "Metamodelo_Cpp_CppClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Metamodelo_Cpp_CppClass"):
                opp_val = getattr(value, "Metamodelo_Cpp_CppClass", None)
                setattr(value, "Metamodelo_Cpp_CppClass", self)

class CppPathReferentiable:

    pass
class CppModelElement:

    pass
class Metamodelo_Cpp_CppImportDeclaration(CppModelElement):

    pass
class Metamodelo_Cpp_CppFunction(CppModelElement, CppType):

    def __init__(self, isVarArg: bool, linkage: str, isInline: bool, Metamodelo_Cpp_CppFunction: set["Metamodelo_Cpp_CppSingleVariableDeclaration"] = None, Metamodelo_Cpp_CppFunction51: "Metamodelo_Cpp_CppBlock" = None):
        self.isVarArg = isVarArg
        self.linkage = linkage
        self.isInline = isInline
        self.Metamodelo_Cpp_CppFunction = Metamodelo_Cpp_CppFunction if Metamodelo_Cpp_CppFunction is not None else set()
        self.Metamodelo_Cpp_CppFunction51 = Metamodelo_Cpp_CppFunction51
        
        pass
    @property
    def isVarArg(self):
        return self.__isVarArg

    @isVarArg.setter
    def isVarArg(self, isVarArg: bool):
        self.__isVarArg = isVarArg


    @property
    def linkage(self):
        return self.__linkage

    @linkage.setter
    def linkage(self, linkage: str):
        self.__linkage = linkage


    @property
    def isInline(self):
        return self.__isInline

    @isInline.setter
    def isInline(self, isInline: bool):
        self.__isInline = isInline


    @property
    def Metamodelo_Cpp_CppFunction(self):
        return self.__Metamodelo_Cpp_CppFunction

    @Metamodelo_Cpp_CppFunction.setter
    def Metamodelo_Cpp_CppFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Metamodelo_Cpp_CppFunction__Metamodelo_Cpp_CppFunction", None)
        self.__Metamodelo_Cpp_CppFunction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Metamodelo_Cpp_CppSingleVariableDeclaration"):
                    opp_val = getattr(item, "Metamodelo_Cpp_CppSingleVariableDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "Metamodelo_Cpp_CppSingleVariableDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Metamodelo_Cpp_CppSingleVariableDeclaration"):
                    opp_val = getattr(item, "Metamodelo_Cpp_CppSingleVariableDeclaration", None)
                    
                    setattr(item, "Metamodelo_Cpp_CppSingleVariableDeclaration", self)
                    

    @property
    def Metamodelo_Cpp_CppFunction51(self):
        return self.__Metamodelo_Cpp_CppFunction51

    @Metamodelo_Cpp_CppFunction51.setter
    def Metamodelo_Cpp_CppFunction51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Metamodelo_Cpp_CppFunction__Metamodelo_Cpp_CppFunction51", None)
        self.__Metamodelo_Cpp_CppFunction51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Metamodelo_Cpp_CppBlock"):
                opp_val = getattr(old_value, "Metamodelo_Cpp_CppBlock", None)
                if opp_val == self:
                    setattr(old_value, "Metamodelo_Cpp_CppBlock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Metamodelo_Cpp_CppBlock"):
                opp_val = getattr(value, "Metamodelo_Cpp_CppBlock", None)
                setattr(value, "Metamodelo_Cpp_CppBlock", self)

class Metamodelo_Cpp_CppExpression(CppModelElement):

    pass
class Metamodelo_Cpp_CppNamedElement(CppModelElement):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class Metamodelo_Cpp_CppFieldContainer(CppModelElement):

    pass
class Metamodelo_Cpp_CppComment(CppModelElement):

    def __init__(self, singleLine: bool, multiLine: bool, content: str):
        self.singleLine = singleLine
        self.multiLine = multiLine
        self.content = content
        
        pass
    @property
    def singleLine(self):
        return self.__singleLine

    @singleLine.setter
    def singleLine(self, singleLine: bool):
        self.__singleLine = singleLine


    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content


    @property
    def multiLine(self):
        return self.__multiLine

    @multiLine.setter
    def multiLine(self, multiLine: bool):
        self.__multiLine = multiLine


class Metamodelo_Cpp_CppTypedElement(CppModelElement):

    pass
class Metamodelo_Cpp_CppPathReference(CppModelElement):

    pass
class Metamodelo_Cpp_CppPackage(CppPathReferentiable):

    pass
class CppNamedElement:

    pass
class Metamodelo_Cpp_CppPathReferentiable(CppNamedElement):

    pass
class Metamodelo_Cpp_CppLabeledStatement(CppNamedElement, CppExpression):

    pass
class Metamodelo_Cpp_CppField(CppNamedElement):

    def __init__(self, accessSpecifier: str, CppField: "Metamodelo_Cpp_CppFieldContainer" = None, cppFields: "Metamodelo_Cpp_CppFieldContainer" = None):
        self.accessSpecifier = accessSpecifier
        self.CppField = CppField
        self.cppFields = cppFields
        
        pass
    @property
    def accessSpecifier(self):
        return self.__accessSpecifier

    @accessSpecifier.setter
    def accessSpecifier(self, accessSpecifier: str):
        self.__accessSpecifier = accessSpecifier


    @property
    def CppField(self):
        return self.__CppField

    @CppField.setter
    def CppField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Metamodelo_Cpp_CppField__CppField", None)
        self.__CppField = value
        
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
    def cppFields(self):
        return self.__cppFields

    @cppFields.setter
    def cppFields(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Metamodelo_Cpp_CppField__cppFields", None)
        self.__cppFields = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CppFieldContainer"):
                opp_val = getattr(old_value, "CppFieldContainer", None)
                if opp_val == self:
                    setattr(old_value, "CppFieldContainer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CppFieldContainer"):
                opp_val = getattr(value, "CppFieldContainer", None)
                setattr(value, "CppFieldContainer", self)

class Metamodelo_Cpp_CppEnumConstructor(CppNamedElement):

    pass
class Metamodelo_Cpp_CppConstantExpression(CppNamedElement, CppExpression):

    pass
class Metamodelo_Cpp_CppVariableDeclaration(CppNamedElement):

    def __init__(self, vartype: str, isArray: bool, Metamodelo_Cpp_CppVariableDeclaration140: set["Metamodelo_Cpp_CppExpression"] = None, CppVariableDeclaration: "Metamodelo_Cpp_CppVariableAccess" = None, variable: set["Metamodelo_Cpp_CppVariableAccess"] = None, Metamodelo_Cpp_CppVariableDeclaration: "Metamodelo_Cpp_CppExpression" = None):
        self.vartype = vartype
        self.isArray = isArray
        self.Metamodelo_Cpp_CppVariableDeclaration140 = Metamodelo_Cpp_CppVariableDeclaration140 if Metamodelo_Cpp_CppVariableDeclaration140 is not None else set()
        self.CppVariableDeclaration = CppVariableDeclaration
        self.variable = variable if variable is not None else set()
        self.Metamodelo_Cpp_CppVariableDeclaration = Metamodelo_Cpp_CppVariableDeclaration
        
        pass
    @property
    def vartype(self):
        return self.__vartype

    @vartype.setter
    def vartype(self, vartype: str):
        self.__vartype = vartype


    @property
    def isArray(self):
        return self.__isArray

    @isArray.setter
    def isArray(self, isArray: bool):
        self.__isArray = isArray


    @property
    def Metamodelo_Cpp_CppVariableDeclaration(self):
        return self.__Metamodelo_Cpp_CppVariableDeclaration

    @Metamodelo_Cpp_CppVariableDeclaration.setter
    def Metamodelo_Cpp_CppVariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Metamodelo_Cpp_CppVariableDeclaration__Metamodelo_Cpp_CppVariableDeclaration", None)
        self.__Metamodelo_Cpp_CppVariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Metamodelo_Cpp_CppExpression138"):
                opp_val = getattr(old_value, "Metamodelo_Cpp_CppExpression138", None)
                if opp_val == self:
                    setattr(old_value, "Metamodelo_Cpp_CppExpression138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Metamodelo_Cpp_CppExpression138"):
                opp_val = getattr(value, "Metamodelo_Cpp_CppExpression138", None)
                setattr(value, "Metamodelo_Cpp_CppExpression138", self)

    @property
    def variable(self):
        return self.__variable

    @variable.setter
    def variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Metamodelo_Cpp_CppVariableDeclaration__variable", None)
        self.__variable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CppVariableAccess"):
                    opp_val = getattr(item, "CppVariableAccess", None)
                    
                    if opp_val == self:
                        setattr(item, "CppVariableAccess", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CppVariableAccess"):
                    opp_val = getattr(item, "CppVariableAccess", None)
                    
                    setattr(item, "CppVariableAccess", self)
                    

    @property
    def CppVariableDeclaration(self):
        return self.__CppVariableDeclaration

    @CppVariableDeclaration.setter
    def CppVariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Metamodelo_Cpp_CppVariableDeclaration__CppVariableDeclaration", None)
        self.__CppVariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usageInVariableAccess"):
                opp_val = getattr(old_value, "usageInVariableAccess", None)
                if opp_val == self:
                    setattr(old_value, "usageInVariableAccess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usageInVariableAccess"):
                opp_val = getattr(value, "usageInVariableAccess", None)
                setattr(value, "usageInVariableAccess", self)

    @property
    def Metamodelo_Cpp_CppVariableDeclaration140(self):
        return self.__Metamodelo_Cpp_CppVariableDeclaration140

    @Metamodelo_Cpp_CppVariableDeclaration140.setter
    def Metamodelo_Cpp_CppVariableDeclaration140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Metamodelo_Cpp_CppVariableDeclaration__Metamodelo_Cpp_CppVariableDeclaration140", None)
        self.__Metamodelo_Cpp_CppVariableDeclaration140 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Metamodelo_Cpp_CppExpression141"):
                    opp_val = getattr(item, "Metamodelo_Cpp_CppExpression141", None)
                    
                    if opp_val == self:
                        setattr(item, "Metamodelo_Cpp_CppExpression141", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Metamodelo_Cpp_CppExpression141"):
                    opp_val = getattr(item, "Metamodelo_Cpp_CppExpression141", None)
                    
                    setattr(item, "Metamodelo_Cpp_CppExpression141", self)
                    

class Metamodelo_Cpp_CppClassFile(CppPathReferentiable):

    pass
class Metamodelo_Cpp_CppType(CppPathReferentiable):

    pass