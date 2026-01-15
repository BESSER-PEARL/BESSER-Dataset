from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class AdditionOpEnum(Enum):
    ADD = "ADD"
    SUB = "SUB"
class AssignmentOpEnum(Enum):
    ASSIGN = "ASSIGN"
    ASSIGN_OR = "ASSIGN_OR"
    ASSIGN_XOR = "ASSIGN_XOR"
    ASSIGN_AND = "ASSIGN_AND"
    ASSIGN_SHIFT_LEFT = "ASSIGN_SHIFT_LEFT"
    ASSIGN_SHIFT_RIGHT = "ASSIGN_SHIFT_RIGHT"
    ASSIGN_SHIFT_RIGHT_ARIMETIC = "ASSIGN_SHIFT_RIGHT_ARIMETIC"
    ASSIGN_ADD = "ASSIGN_ADD"
    ASSIGN_SUB = "ASSIGN_SUB"
    ASSIGN_MULT = "ASSIGN_MULT"
    ASSIGN_DIV = "ASSIGN_DIV"
    ASSIGN_MOD = "ASSIGN_MOD"
class ReservedWordsEnum(Enum):
    OF = "OF"
    RELOCATABLE = "RELOCATABLE"
    SWITCH = "SWITCH"
    TRY = "TRY"
    TYPE = "TYPE"
    TYPEOF = "TYPEOF"
    USING = "USING"
    ILLEGAL = "ILLEGAL"
    AS = "AS"
    CASE = "CASE"
    CATCH = "CATCH"
    FINAL = "FINAL"
    LET = "LET"
    MATCH = "MATCH"
class ComparisonOpEnum(Enum):
    LT = "LT"
    GT = "GT"
    LTE = "LTE"
    GTE = "GTE"
    IN = "IN"
class IncDecOpEnum(Enum):
    INC = "INC"
    DEC = "DEC"
class EqualityOpEnum(Enum):
    EQ = "EQ"
    NOTEQ = "NOTEQ"
class SpecialExpressionTypeEnum(Enum):
    SUPER = "SUPER"
    THIS = "THIS"
class MulDivModOpEnum(Enum):
    MULT = "MULT"
    DIV = "DIV"
    MOD = "MOD"
class ShiftOpEnum(Enum):
    LEFT_SHIFT = "LEFT_SHIFT"
    RIGHT_SHIFT = "RIGHT_SHIFT"
    ARITHMETIC_RIGHT_SHIFT = "ARITHMETIC_RIGHT_SHIFT"


############################################
# Definition of Classes
############################################

class ContinueStatement:

    pass
class optGrammar_Continue(ContinueStatement):

    pass
class optGrammar_UnitsLiteral:

    def __init__(self, value: str, optGrammar_UnitsLiteral: "optGrammar_UnitTypes" = None):
        self.value = value
        self.optGrammar_UnitsLiteral = optGrammar_UnitsLiteral
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def optGrammar_UnitsLiteral(self):
        return self.__optGrammar_UnitsLiteral

    @optGrammar_UnitsLiteral.setter
    def optGrammar_UnitsLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_UnitsLiteral__optGrammar_UnitsLiteral", None)
        self.__optGrammar_UnitsLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_UnitTypes206"):
                opp_val = getattr(old_value, "optGrammar_UnitTypes206", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_UnitTypes206", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_UnitTypes206"):
                opp_val = getattr(value, "optGrammar_UnitTypes206", None)
                setattr(value, "optGrammar_UnitTypes206", self)

class optGrammar_TimeUnitsLiteral:

    def __init__(self, value: str, optGrammar_TimeUnitsLiteral: "optGrammar_UnitTypes" = None):
        self.value = value
        self.optGrammar_TimeUnitsLiteral = optGrammar_TimeUnitsLiteral
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def optGrammar_TimeUnitsLiteral(self):
        return self.__optGrammar_TimeUnitsLiteral

    @optGrammar_TimeUnitsLiteral.setter
    def optGrammar_TimeUnitsLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_TimeUnitsLiteral__optGrammar_TimeUnitsLiteral", None)
        self.__optGrammar_TimeUnitsLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_UnitTypes204"):
                opp_val = getattr(old_value, "optGrammar_UnitTypes204", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_UnitTypes204", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_UnitTypes204"):
                opp_val = getattr(value, "optGrammar_UnitTypes204", None)
                setattr(value, "optGrammar_UnitTypes204", self)

class NamedType:

    pass
class optGrammar_IntParameter:

    pass
class Literal:

    pass
class optGrammar_GasleftFunction(Literal):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class optGrammar_StringLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class optGrammar_SpecialLiteral(Literal):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class optGrammar_MathematicalFunction(Literal):

    def __init__(self, function: str, optGrammar_MathematicalFunction: set["optGrammar_IntParameter"] = None):
        self.function = function
        self.optGrammar_MathematicalFunction = optGrammar_MathematicalFunction if optGrammar_MathematicalFunction is not None else set()
        
    @property
    def function(self) -> str:
        return self.__function

    @function.setter
    def function(self, function: str):
        self.__function = function

    @property
    def optGrammar_MathematicalFunction(self):
        return self.__optGrammar_MathematicalFunction

    @optGrammar_MathematicalFunction.setter
    def optGrammar_MathematicalFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_MathematicalFunction__optGrammar_MathematicalFunction", None)
        self.__optGrammar_MathematicalFunction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "optGrammar_IntParameter186"):
                    opp_val = getattr(item, "optGrammar_IntParameter186", None)
                    
                    if opp_val == self:
                        setattr(item, "optGrammar_IntParameter186", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "optGrammar_IntParameter186"):
                    opp_val = getattr(item, "optGrammar_IntParameter186", None)
                    
                    setattr(item, "optGrammar_IntParameter186", self)
                    

class optGrammar_BlockhashFunction(Literal):

    pass
class optGrammar_UnitTypes:

    pass
class optGrammar_DecimalLiteral:

    def __init__(self, value: float, optGrammar_DecimalLiteral: "optGrammar_NumericLiteral" = None):
        self.value = value
        self.optGrammar_DecimalLiteral = optGrammar_DecimalLiteral
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def optGrammar_DecimalLiteral(self):
        return self.__optGrammar_DecimalLiteral

    @optGrammar_DecimalLiteral.setter
    def optGrammar_DecimalLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_DecimalLiteral__optGrammar_DecimalLiteral", None)
        self.__optGrammar_DecimalLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_NumericLiteral195"):
                opp_val = getattr(old_value, "optGrammar_NumericLiteral195", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_NumericLiteral195", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_NumericLiteral195"):
                opp_val = getattr(value, "optGrammar_NumericLiteral195", None)
                setattr(value, "optGrammar_NumericLiteral195", self)

class optGrammar_HexLiteral:

    def __init__(self, value: str, optGrammar_HexLiteral: "optGrammar_NumericLiteral" = None):
        self.value = value
        self.optGrammar_HexLiteral = optGrammar_HexLiteral
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def optGrammar_HexLiteral(self):
        return self.__optGrammar_HexLiteral

    @optGrammar_HexLiteral.setter
    def optGrammar_HexLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_HexLiteral__optGrammar_HexLiteral", None)
        self.__optGrammar_HexLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_NumericLiteral193"):
                opp_val = getattr(old_value, "optGrammar_NumericLiteral193", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_NumericLiteral193", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_NumericLiteral193"):
                opp_val = getattr(value, "optGrammar_NumericLiteral193", None)
                setattr(value, "optGrammar_NumericLiteral193", self)

class optGrammar_IntLiteral:

    def __init__(self, value: int, optGrammar_IntLiteral: "optGrammar_NumericLiteral" = None):
        self.value = value
        self.optGrammar_IntLiteral = optGrammar_IntLiteral
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def optGrammar_IntLiteral(self):
        return self.__optGrammar_IntLiteral

    @optGrammar_IntLiteral.setter
    def optGrammar_IntLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_IntLiteral__optGrammar_IntLiteral", None)
        self.__optGrammar_IntLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_NumericLiteral"):
                opp_val = getattr(old_value, "optGrammar_NumericLiteral", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_NumericLiteral", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_NumericLiteral"):
                opp_val = getattr(value, "optGrammar_NumericLiteral", None)
                setattr(value, "optGrammar_NumericLiteral", self)

class optGrammar_BooleanLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class optGrammar_EcrecoverFunction(Literal):

    def __init__(self, function: str, optGrammar_EcrecoverFunction: set["optGrammar_IntParameter"] = None):
        self.function = function
        self.optGrammar_EcrecoverFunction = optGrammar_EcrecoverFunction if optGrammar_EcrecoverFunction is not None else set()
        
    @property
    def function(self) -> str:
        return self.__function

    @function.setter
    def function(self, function: str):
        self.__function = function

    @property
    def optGrammar_EcrecoverFunction(self):
        return self.__optGrammar_EcrecoverFunction

    @optGrammar_EcrecoverFunction.setter
    def optGrammar_EcrecoverFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_EcrecoverFunction__optGrammar_EcrecoverFunction", None)
        self.__optGrammar_EcrecoverFunction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "optGrammar_IntParameter190"):
                    opp_val = getattr(item, "optGrammar_IntParameter190", None)
                    
                    if opp_val == self:
                        setattr(item, "optGrammar_IntParameter190", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "optGrammar_IntParameter190"):
                    opp_val = getattr(item, "optGrammar_IntParameter190", None)
                    
                    setattr(item, "optGrammar_IntParameter190", self)
                    

class optGrammar_HashFunction(Literal):

    def __init__(self, name: str, optGrammar_HashFunction: "optGrammar_IntParameter" = None):
        self.name = name
        self.optGrammar_HashFunction = optGrammar_HashFunction
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def optGrammar_HashFunction(self):
        return self.__optGrammar_HashFunction

    @optGrammar_HashFunction.setter
    def optGrammar_HashFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_HashFunction__optGrammar_HashFunction", None)
        self.__optGrammar_HashFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_IntParameter188"):
                opp_val = getattr(old_value, "optGrammar_IntParameter188", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_IntParameter188", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_IntParameter188"):
                opp_val = getattr(value, "optGrammar_IntParameter188", None)
                setattr(value, "optGrammar_IntParameter188", self)

class PrimaryArithmetic:

    pass
class optGrammar_NumericLiteral(Literal, PrimaryArithmetic):

    pass
class optGrammar_SecondOperators:

    def __init__(self, operator: str, optGrammar_SecondOperators: "optGrammar_ArithmeticOperations" = None, optGrammar_SecondOperators170: "optGrammar_PrimaryArithmetic" = None):
        self.operator = operator
        self.optGrammar_SecondOperators = optGrammar_SecondOperators
        self.optGrammar_SecondOperators170 = optGrammar_SecondOperators170
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def optGrammar_SecondOperators(self):
        return self.__optGrammar_SecondOperators

    @optGrammar_SecondOperators.setter
    def optGrammar_SecondOperators(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_SecondOperators__optGrammar_SecondOperators", None)
        self.__optGrammar_SecondOperators = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_ArithmeticOperations168"):
                opp_val = getattr(old_value, "optGrammar_ArithmeticOperations168", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_ArithmeticOperations168"):
                opp_val = getattr(value, "optGrammar_ArithmeticOperations168", None)
                if opp_val is None:
                    setattr(value, "optGrammar_ArithmeticOperations168", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def optGrammar_SecondOperators170(self):
        return self.__optGrammar_SecondOperators170

    @optGrammar_SecondOperators170.setter
    def optGrammar_SecondOperators170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_SecondOperators__optGrammar_SecondOperators170", None)
        self.__optGrammar_SecondOperators170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_PrimaryArithmetic171"):
                opp_val = getattr(old_value, "optGrammar_PrimaryArithmetic171", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_PrimaryArithmetic171", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_PrimaryArithmetic171"):
                opp_val = getattr(value, "optGrammar_PrimaryArithmetic171", None)
                setattr(value, "optGrammar_PrimaryArithmetic171", self)

class optGrammar_PrimaryArithmetic:

    pass
class optGrammar_ArithmeticOperations:

    pass
class LoopStructures:

    pass
class optGrammar_WhileStatement(LoopStructures):

    pass
class optGrammar_IfStatement(LoopStructures):

    pass
class optGrammar_FunctionCall:

    pass
class optGrammar_Statement:

    pass
class optGrammar_ForStatement(LoopStructures):

    pass
class Qualifier:

    pass
class optGrammar_Index(Qualifier):

    pass
class optGrammar_Arguments(Qualifier):

    pass
class optGrammar_Field(Qualifier):

    def __init__(self, field: str, optGrammar_Field: "optGrammar_SpecialExpression" = None):
        self.field = field
        self.optGrammar_Field = optGrammar_Field
        
    @property
    def field(self) -> str:
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field

    @property
    def optGrammar_Field(self):
        return self.__optGrammar_Field

    @optGrammar_Field.setter
    def optGrammar_Field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_Field__optGrammar_Field", None)
        self.__optGrammar_Field = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_SpecialExpression"):
                opp_val = getattr(old_value, "optGrammar_SpecialExpression", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_SpecialExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_SpecialExpression"):
                opp_val = getattr(value, "optGrammar_SpecialExpression", None)
                setattr(value, "optGrammar_SpecialExpression", self)

class optGrammar_Qualifier:

    pass
class optGrammar_ReturnParameterDeclaration:

    pass
class SimpleStatement:

    pass
class Type:

    pass
class optGrammar_StandardType(Type):

    pass
class optGrammar_ArrayType:

    pass
class StandardTypeWithoutQualifiedIdentifier:

    pass
class StandardType:

    pass
class optGrammar_NamedType(StandardType, StandardTypeWithoutQualifiedIdentifier):

    def __init__(self, type: str, optGrammar_NamedType: "optGrammar_ArrayType" = None):
        self.type = type
        self.optGrammar_NamedType = optGrammar_NamedType
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def optGrammar_NamedType(self):
        return self.__optGrammar_NamedType

    @optGrammar_NamedType.setter
    def optGrammar_NamedType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_NamedType__optGrammar_NamedType", None)
        self.__optGrammar_NamedType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_ArrayType"):
                opp_val = getattr(old_value, "optGrammar_ArrayType", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_ArrayType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_ArrayType"):
                opp_val = getattr(value, "optGrammar_ArrayType", None)
                setattr(value, "optGrammar_ArrayType", self)

class optGrammar_Type:

    def __init__(self, isVarType: bool, optGrammar_Type: "optGrammar_Mapping" = None, optGrammar_Type109: "optGrammar_ReturnParameterDeclaration" = None):
        self.isVarType = isVarType
        self.optGrammar_Type = optGrammar_Type
        self.optGrammar_Type109 = optGrammar_Type109
        
    @property
    def isVarType(self) -> bool:
        return self.__isVarType

    @isVarType.setter
    def isVarType(self, isVarType: bool):
        self.__isVarType = isVarType

    @property
    def optGrammar_Type(self):
        return self.__optGrammar_Type

    @optGrammar_Type.setter
    def optGrammar_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_Type__optGrammar_Type", None)
        self.__optGrammar_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_Mapping79"):
                opp_val = getattr(old_value, "optGrammar_Mapping79", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_Mapping79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_Mapping79"):
                opp_val = getattr(value, "optGrammar_Mapping79", None)
                setattr(value, "optGrammar_Mapping79", self)

    @property
    def optGrammar_Type109(self):
        return self.__optGrammar_Type109

    @optGrammar_Type109.setter
    def optGrammar_Type109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_Type__optGrammar_Type109", None)
        self.__optGrammar_Type109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_ReturnParameterDeclaration108"):
                opp_val = getattr(old_value, "optGrammar_ReturnParameterDeclaration108", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_ReturnParameterDeclaration108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_ReturnParameterDeclaration108"):
                opp_val = getattr(value, "optGrammar_ReturnParameterDeclaration108", None)
                setattr(value, "optGrammar_ReturnParameterDeclaration108", self)

class VariableDeclarationOptionalElement:

    pass
class optGrammar_IndexedSpecifer(VariableDeclarationOptionalElement):

    pass
class optGrammar_LocationSpecifier(VariableDeclarationOptionalElement):

    pass
class optGrammar_ConstantSpecifier(VariableDeclarationOptionalElement):

    pass
class optGrammar_VisibilitySpecifier(VariableDeclarationOptionalElement):

    pass
class optGrammar_VariableDeclarationOptionalElement:

    pass
class optGrammar_SizedDeclaration(NamedType):

    pass
class optGrammar_SimpleTypeDeclaration(NamedType):

    pass
class optGrammar_SimpleStatement2:

    pass
class Statement:

    pass
class optGrammar_DoWhileStatement(Statement):

    pass
class optGrammar_EmitStatement(Statement):

    pass
class optGrammar_ContinueStatement(Statement):

    pass
class optGrammar_BreakStatement(Statement):

    pass
class optGrammar_LoopStructures(Statement):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class optGrammar_PlaceHolderStatement(Statement):

    pass
class optGrammar_ReturnStatement(Statement):

    pass
class optGrammar_DeleteStatement(Statement):

    pass
class optGrammar_ThrowStatement(Statement):

    pass
class optGrammar_SimpleStatement(Statement):

    pass
class Expression:

    pass
class optGrammar_NewExpression(Expression):

    pass
class optGrammar_SignExpression(Expression):

    def __init__(self, signOp: str, optGrammar_SignExpression: "optGrammar_Expression" = None):
        self.signOp = signOp
        self.optGrammar_SignExpression = optGrammar_SignExpression
        
    @property
    def signOp(self) -> str:
        return self.__signOp

    @signOp.setter
    def signOp(self, signOp: str):
        self.__signOp = signOp

    @property
    def optGrammar_SignExpression(self):
        return self.__optGrammar_SignExpression

    @optGrammar_SignExpression.setter
    def optGrammar_SignExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_SignExpression__optGrammar_SignExpression", None)
        self.__optGrammar_SignExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_Expression160"):
                opp_val = getattr(old_value, "optGrammar_Expression160", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_Expression160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_Expression160"):
                opp_val = getattr(value, "optGrammar_Expression160", None)
                setattr(value, "optGrammar_Expression160", self)

class optGrammar_Shift(Expression):

    def __init__(self, shiftOp: str, optGrammar_Shift: "optGrammar_Expression" = None, optGrammar_Shift277: "optGrammar_Expression" = None):
        self.shiftOp = shiftOp
        self.optGrammar_Shift = optGrammar_Shift
        self.optGrammar_Shift277 = optGrammar_Shift277
        
    @property
    def shiftOp(self) -> str:
        return self.__shiftOp

    @shiftOp.setter
    def shiftOp(self, shiftOp: str):
        self.__shiftOp = shiftOp

    @property
    def optGrammar_Shift277(self):
        return self.__optGrammar_Shift277

    @optGrammar_Shift277.setter
    def optGrammar_Shift277(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_Shift__optGrammar_Shift277", None)
        self.__optGrammar_Shift277 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_Expression278"):
                opp_val = getattr(old_value, "optGrammar_Expression278", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_Expression278", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_Expression278"):
                opp_val = getattr(value, "optGrammar_Expression278", None)
                setattr(value, "optGrammar_Expression278", self)

    @property
    def optGrammar_Shift(self):
        return self.__optGrammar_Shift

    @optGrammar_Shift.setter
    def optGrammar_Shift(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_Shift__optGrammar_Shift", None)
        self.__optGrammar_Shift = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_Expression275"):
                opp_val = getattr(old_value, "optGrammar_Expression275", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_Expression275", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_Expression275"):
                opp_val = getattr(value, "optGrammar_Expression275", None)
                setattr(value, "optGrammar_Expression275", self)

class optGrammar_Exponent(Expression):

    pass
class optGrammar_Literal(Expression):

    pass
class optGrammar_PreDecExpression(Expression):

    pass
class optGrammar_BitXor(Expression):

    pass
class optGrammar_NotExpression(Expression):

    pass
class optGrammar_PostIncDecExpression(Expression):

    def __init__(self, postOp: str, optGrammar_PostIncDecExpression: "optGrammar_Expression" = None):
        self.postOp = postOp
        self.optGrammar_PostIncDecExpression = optGrammar_PostIncDecExpression
        
    @property
    def postOp(self) -> str:
        return self.__postOp

    @postOp.setter
    def postOp(self, postOp: str):
        self.__postOp = postOp

    @property
    def optGrammar_PostIncDecExpression(self):
        return self.__optGrammar_PostIncDecExpression

    @optGrammar_PostIncDecExpression.setter
    def optGrammar_PostIncDecExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_PostIncDecExpression__optGrammar_PostIncDecExpression", None)
        self.__optGrammar_PostIncDecExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_Expression295"):
                opp_val = getattr(old_value, "optGrammar_Expression295", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_Expression295", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_Expression295"):
                opp_val = getattr(value, "optGrammar_Expression295", None)
                setattr(value, "optGrammar_Expression295", self)

class optGrammar_MulDivMod(Expression):

    def __init__(self, multipliciativeOp: str, optGrammar_MulDivMod: "optGrammar_Expression" = None, optGrammar_MulDivMod287: "optGrammar_Expression" = None):
        self.multipliciativeOp = multipliciativeOp
        self.optGrammar_MulDivMod = optGrammar_MulDivMod
        self.optGrammar_MulDivMod287 = optGrammar_MulDivMod287
        
    @property
    def multipliciativeOp(self) -> str:
        return self.__multipliciativeOp

    @multipliciativeOp.setter
    def multipliciativeOp(self, multipliciativeOp: str):
        self.__multipliciativeOp = multipliciativeOp

    @property
    def optGrammar_MulDivMod(self):
        return self.__optGrammar_MulDivMod

    @optGrammar_MulDivMod.setter
    def optGrammar_MulDivMod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_MulDivMod__optGrammar_MulDivMod", None)
        self.__optGrammar_MulDivMod = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_Expression285"):
                opp_val = getattr(old_value, "optGrammar_Expression285", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_Expression285", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_Expression285"):
                opp_val = getattr(value, "optGrammar_Expression285", None)
                setattr(value, "optGrammar_Expression285", self)

    @property
    def optGrammar_MulDivMod287(self):
        return self.__optGrammar_MulDivMod287

    @optGrammar_MulDivMod287.setter
    def optGrammar_MulDivMod287(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_MulDivMod__optGrammar_MulDivMod287", None)
        self.__optGrammar_MulDivMod287 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_Expression288"):
                opp_val = getattr(old_value, "optGrammar_Expression288", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_Expression288", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_Expression288"):
                opp_val = getattr(value, "optGrammar_Expression288", None)
                setattr(value, "optGrammar_Expression288", self)

class optGrammar_BinaryNotExpression(Expression):

    pass
class optGrammar_SpecialExpression(Expression):

    def __init__(self, type: str, optGrammar_SpecialExpression: "optGrammar_Field" = None, optGrammar_SpecialExpression149: set["optGrammar_Qualifier"] = None):
        self.type = type
        self.optGrammar_SpecialExpression = optGrammar_SpecialExpression
        self.optGrammar_SpecialExpression149 = optGrammar_SpecialExpression149 if optGrammar_SpecialExpression149 is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def optGrammar_SpecialExpression(self):
        return self.__optGrammar_SpecialExpression

    @optGrammar_SpecialExpression.setter
    def optGrammar_SpecialExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_SpecialExpression__optGrammar_SpecialExpression", None)
        self.__optGrammar_SpecialExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_Field"):
                opp_val = getattr(old_value, "optGrammar_Field", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_Field", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_Field"):
                opp_val = getattr(value, "optGrammar_Field", None)
                setattr(value, "optGrammar_Field", self)

    @property
    def optGrammar_SpecialExpression149(self):
        return self.__optGrammar_SpecialExpression149

    @optGrammar_SpecialExpression149.setter
    def optGrammar_SpecialExpression149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_SpecialExpression__optGrammar_SpecialExpression149", None)
        self.__optGrammar_SpecialExpression149 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "optGrammar_Qualifier150"):
                    opp_val = getattr(item, "optGrammar_Qualifier150", None)
                    
                    if opp_val == self:
                        setattr(item, "optGrammar_Qualifier150", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "optGrammar_Qualifier150"):
                    opp_val = getattr(item, "optGrammar_Qualifier150", None)
                    
                    setattr(item, "optGrammar_Qualifier150", self)
                    

class optGrammar_VariableDeclarationExpression(Expression):

    pass
class optGrammar_Comparison(Expression):

    def __init__(self, comparisonOp: str, optGrammar_Comparison: "optGrammar_Expression" = None, optGrammar_Comparison257: "optGrammar_Expression" = None):
        self.comparisonOp = comparisonOp
        self.optGrammar_Comparison = optGrammar_Comparison
        self.optGrammar_Comparison257 = optGrammar_Comparison257
        
    @property
    def comparisonOp(self) -> str:
        return self.__comparisonOp

    @comparisonOp.setter
    def comparisonOp(self, comparisonOp: str):
        self.__comparisonOp = comparisonOp

    @property
    def optGrammar_Comparison(self):
        return self.__optGrammar_Comparison

    @optGrammar_Comparison.setter
    def optGrammar_Comparison(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_Comparison__optGrammar_Comparison", None)
        self.__optGrammar_Comparison = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_Expression255"):
                opp_val = getattr(old_value, "optGrammar_Expression255", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_Expression255", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_Expression255"):
                opp_val = getattr(value, "optGrammar_Expression255", None)
                setattr(value, "optGrammar_Expression255", self)

    @property
    def optGrammar_Comparison257(self):
        return self.__optGrammar_Comparison257

    @optGrammar_Comparison257.setter
    def optGrammar_Comparison257(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_Comparison__optGrammar_Comparison257", None)
        self.__optGrammar_Comparison257 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_Expression258"):
                opp_val = getattr(old_value, "optGrammar_Expression258", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_Expression258", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_Expression258"):
                opp_val = getattr(value, "optGrammar_Expression258", None)
                setattr(value, "optGrammar_Expression258", self)

class optGrammar_And(Expression):

    pass
class optGrammar_BitAnd(Expression):

    pass
class optGrammar_TupleSeparator(Expression):

    pass
class optGrammar_PreIncExpression(Expression):

    pass
class optGrammar_Equality(Expression):

    def __init__(self, equalityOp: str, optGrammar_Equality: "optGrammar_Expression" = None, optGrammar_Equality252: "optGrammar_Expression" = None):
        self.equalityOp = equalityOp
        self.optGrammar_Equality = optGrammar_Equality
        self.optGrammar_Equality252 = optGrammar_Equality252
        
    @property
    def equalityOp(self) -> str:
        return self.__equalityOp

    @equalityOp.setter
    def equalityOp(self, equalityOp: str):
        self.__equalityOp = equalityOp

    @property
    def optGrammar_Equality252(self):
        return self.__optGrammar_Equality252

    @optGrammar_Equality252.setter
    def optGrammar_Equality252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_Equality__optGrammar_Equality252", None)
        self.__optGrammar_Equality252 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_Expression253"):
                opp_val = getattr(old_value, "optGrammar_Expression253", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_Expression253", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_Expression253"):
                opp_val = getattr(value, "optGrammar_Expression253", None)
                setattr(value, "optGrammar_Expression253", self)

    @property
    def optGrammar_Equality(self):
        return self.__optGrammar_Equality

    @optGrammar_Equality.setter
    def optGrammar_Equality(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_Equality__optGrammar_Equality", None)
        self.__optGrammar_Equality = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_Expression250"):
                opp_val = getattr(old_value, "optGrammar_Expression250", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_Expression250", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_Expression250"):
                opp_val = getattr(value, "optGrammar_Expression250", None)
                setattr(value, "optGrammar_Expression250", self)

class optGrammar_TypeCast(Expression):

    pass
class optGrammar_Or(Expression):

    pass
class optGrammar_Assignment(Expression):

    def __init__(self, assignmentOp: str, optGrammar_Assignment: "optGrammar_Expression" = None, optGrammar_Assignment229: "optGrammar_Expression" = None):
        self.assignmentOp = assignmentOp
        self.optGrammar_Assignment = optGrammar_Assignment
        self.optGrammar_Assignment229 = optGrammar_Assignment229
        
    @property
    def assignmentOp(self) -> str:
        return self.__assignmentOp

    @assignmentOp.setter
    def assignmentOp(self, assignmentOp: str):
        self.__assignmentOp = assignmentOp

    @property
    def optGrammar_Assignment229(self):
        return self.__optGrammar_Assignment229

    @optGrammar_Assignment229.setter
    def optGrammar_Assignment229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_Assignment__optGrammar_Assignment229", None)
        self.__optGrammar_Assignment229 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_Expression230"):
                opp_val = getattr(old_value, "optGrammar_Expression230", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_Expression230", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_Expression230"):
                opp_val = getattr(value, "optGrammar_Expression230", None)
                setattr(value, "optGrammar_Expression230", self)

    @property
    def optGrammar_Assignment(self):
        return self.__optGrammar_Assignment

    @optGrammar_Assignment.setter
    def optGrammar_Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_Assignment__optGrammar_Assignment", None)
        self.__optGrammar_Assignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_Expression227"):
                opp_val = getattr(old_value, "optGrammar_Expression227", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_Expression227", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_Expression227"):
                opp_val = getattr(value, "optGrammar_Expression227", None)
                setattr(value, "optGrammar_Expression227", self)

class optGrammar_AddSub(Expression):

    def __init__(self, additionOp: str, optGrammar_AddSub: "optGrammar_Expression" = None, optGrammar_AddSub282: "optGrammar_Expression" = None):
        self.additionOp = additionOp
        self.optGrammar_AddSub = optGrammar_AddSub
        self.optGrammar_AddSub282 = optGrammar_AddSub282
        
    @property
    def additionOp(self) -> str:
        return self.__additionOp

    @additionOp.setter
    def additionOp(self, additionOp: str):
        self.__additionOp = additionOp

    @property
    def optGrammar_AddSub(self):
        return self.__optGrammar_AddSub

    @optGrammar_AddSub.setter
    def optGrammar_AddSub(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_AddSub__optGrammar_AddSub", None)
        self.__optGrammar_AddSub = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_Expression280"):
                opp_val = getattr(old_value, "optGrammar_Expression280", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_Expression280", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_Expression280"):
                opp_val = getattr(value, "optGrammar_Expression280", None)
                setattr(value, "optGrammar_Expression280", self)

    @property
    def optGrammar_AddSub282(self):
        return self.__optGrammar_AddSub282

    @optGrammar_AddSub282.setter
    def optGrammar_AddSub282(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_AddSub__optGrammar_AddSub282", None)
        self.__optGrammar_AddSub282 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_Expression283"):
                opp_val = getattr(old_value, "optGrammar_Expression283", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_Expression283", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_Expression283"):
                opp_val = getattr(value, "optGrammar_Expression283", None)
                setattr(value, "optGrammar_Expression283", self)

class optGrammar_QualifiedIdentifier(StandardType, Expression):

    def __init__(self, identifier: str, optGrammar_QualifiedIdentifier: set["optGrammar_Qualifier"] = None, optGrammar_QualifiedIdentifier118: "optGrammar_DeleteStatement" = None):
        self.identifier = identifier
        self.optGrammar_QualifiedIdentifier = optGrammar_QualifiedIdentifier if optGrammar_QualifiedIdentifier is not None else set()
        self.optGrammar_QualifiedIdentifier118 = optGrammar_QualifiedIdentifier118
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def optGrammar_QualifiedIdentifier(self):
        return self.__optGrammar_QualifiedIdentifier

    @optGrammar_QualifiedIdentifier.setter
    def optGrammar_QualifiedIdentifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_QualifiedIdentifier__optGrammar_QualifiedIdentifier", None)
        self.__optGrammar_QualifiedIdentifier = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "optGrammar_Qualifier"):
                    opp_val = getattr(item, "optGrammar_Qualifier", None)
                    
                    if opp_val == self:
                        setattr(item, "optGrammar_Qualifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "optGrammar_Qualifier"):
                    opp_val = getattr(item, "optGrammar_Qualifier", None)
                    
                    setattr(item, "optGrammar_Qualifier", self)
                    

    @property
    def optGrammar_QualifiedIdentifier118(self):
        return self.__optGrammar_QualifiedIdentifier118

    @optGrammar_QualifiedIdentifier118.setter
    def optGrammar_QualifiedIdentifier118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_QualifiedIdentifier__optGrammar_QualifiedIdentifier118", None)
        self.__optGrammar_QualifiedIdentifier118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_DeleteStatement"):
                opp_val = getattr(old_value, "optGrammar_DeleteStatement", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_DeleteStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_DeleteStatement"):
                opp_val = getattr(value, "optGrammar_DeleteStatement", None)
                setattr(value, "optGrammar_DeleteStatement", self)

class optGrammar_BitOr(Expression):

    pass
class optGrammar_Tuple(Expression):

    pass
class optGrammar_Mapping(StandardType, StandardTypeWithoutQualifiedIdentifier):

    pass
class SimpleStatement2:

    pass
class optGrammar_VarVariableTypeDeclaration(SimpleStatement2, SimpleStatement):

    def __init__(self, semicolon: bool, optGrammar_VarVariableTypeDeclaration: "optGrammar_Variable" = None, optGrammar_VarVariableTypeDeclaration219: "optGrammar_Expression" = None):
        self.semicolon = semicolon
        self.optGrammar_VarVariableTypeDeclaration = optGrammar_VarVariableTypeDeclaration
        self.optGrammar_VarVariableTypeDeclaration219 = optGrammar_VarVariableTypeDeclaration219
        
    @property
    def semicolon(self) -> bool:
        return self.__semicolon

    @semicolon.setter
    def semicolon(self, semicolon: bool):
        self.__semicolon = semicolon

    @property
    def optGrammar_VarVariableTypeDeclaration(self):
        return self.__optGrammar_VarVariableTypeDeclaration

    @optGrammar_VarVariableTypeDeclaration.setter
    def optGrammar_VarVariableTypeDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_VarVariableTypeDeclaration__optGrammar_VarVariableTypeDeclaration", None)
        self.__optGrammar_VarVariableTypeDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_Variable217"):
                opp_val = getattr(old_value, "optGrammar_Variable217", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_Variable217", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_Variable217"):
                opp_val = getattr(value, "optGrammar_Variable217", None)
                setattr(value, "optGrammar_Variable217", self)

    @property
    def optGrammar_VarVariableTypeDeclaration219(self):
        return self.__optGrammar_VarVariableTypeDeclaration219

    @optGrammar_VarVariableTypeDeclaration219.setter
    def optGrammar_VarVariableTypeDeclaration219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_VarVariableTypeDeclaration__optGrammar_VarVariableTypeDeclaration219", None)
        self.__optGrammar_VarVariableTypeDeclaration219 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_Expression220"):
                opp_val = getattr(old_value, "optGrammar_Expression220", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_Expression220", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_Expression220"):
                opp_val = getattr(value, "optGrammar_Expression220", None)
                setattr(value, "optGrammar_Expression220", self)

class optGrammar_StandardTypeWithoutQualifiedIdentifier(SimpleStatement2, SimpleStatement):

    pass
class optGrammar_StandardVariableDeclaration(SimpleStatement2, SimpleStatement):

    def __init__(self, semicolon: bool, optGrammar_StandardVariableDeclaration: "optGrammar_StandardTypeWithoutQualifiedIdentifier" = None, optGrammar_StandardVariableDeclaration209: set["optGrammar_VariableDeclarationOptionalElement"] = None, optGrammar_StandardVariableDeclaration211: "optGrammar_Variable" = None, optGrammar_StandardVariableDeclaration214: "optGrammar_Expression" = None):
        self.semicolon = semicolon
        self.optGrammar_StandardVariableDeclaration = optGrammar_StandardVariableDeclaration
        self.optGrammar_StandardVariableDeclaration209 = optGrammar_StandardVariableDeclaration209 if optGrammar_StandardVariableDeclaration209 is not None else set()
        self.optGrammar_StandardVariableDeclaration211 = optGrammar_StandardVariableDeclaration211
        self.optGrammar_StandardVariableDeclaration214 = optGrammar_StandardVariableDeclaration214
        
    @property
    def semicolon(self) -> bool:
        return self.__semicolon

    @semicolon.setter
    def semicolon(self, semicolon: bool):
        self.__semicolon = semicolon

    @property
    def optGrammar_StandardVariableDeclaration209(self):
        return self.__optGrammar_StandardVariableDeclaration209

    @optGrammar_StandardVariableDeclaration209.setter
    def optGrammar_StandardVariableDeclaration209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_StandardVariableDeclaration__optGrammar_StandardVariableDeclaration209", None)
        self.__optGrammar_StandardVariableDeclaration209 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "optGrammar_VariableDeclarationOptionalElement"):
                    opp_val = getattr(item, "optGrammar_VariableDeclarationOptionalElement", None)
                    
                    if opp_val == self:
                        setattr(item, "optGrammar_VariableDeclarationOptionalElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "optGrammar_VariableDeclarationOptionalElement"):
                    opp_val = getattr(item, "optGrammar_VariableDeclarationOptionalElement", None)
                    
                    setattr(item, "optGrammar_VariableDeclarationOptionalElement", self)
                    

    @property
    def optGrammar_StandardVariableDeclaration214(self):
        return self.__optGrammar_StandardVariableDeclaration214

    @optGrammar_StandardVariableDeclaration214.setter
    def optGrammar_StandardVariableDeclaration214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_StandardVariableDeclaration__optGrammar_StandardVariableDeclaration214", None)
        self.__optGrammar_StandardVariableDeclaration214 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_Expression215"):
                opp_val = getattr(old_value, "optGrammar_Expression215", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_Expression215", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_Expression215"):
                opp_val = getattr(value, "optGrammar_Expression215", None)
                setattr(value, "optGrammar_Expression215", self)

    @property
    def optGrammar_StandardVariableDeclaration(self):
        return self.__optGrammar_StandardVariableDeclaration

    @optGrammar_StandardVariableDeclaration.setter
    def optGrammar_StandardVariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_StandardVariableDeclaration__optGrammar_StandardVariableDeclaration", None)
        self.__optGrammar_StandardVariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_StandardTypeWithoutQualifiedIdentifier"):
                opp_val = getattr(old_value, "optGrammar_StandardTypeWithoutQualifiedIdentifier", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_StandardTypeWithoutQualifiedIdentifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_StandardTypeWithoutQualifiedIdentifier"):
                opp_val = getattr(value, "optGrammar_StandardTypeWithoutQualifiedIdentifier", None)
                setattr(value, "optGrammar_StandardTypeWithoutQualifiedIdentifier", self)

    @property
    def optGrammar_StandardVariableDeclaration211(self):
        return self.__optGrammar_StandardVariableDeclaration211

    @optGrammar_StandardVariableDeclaration211.setter
    def optGrammar_StandardVariableDeclaration211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_StandardVariableDeclaration__optGrammar_StandardVariableDeclaration211", None)
        self.__optGrammar_StandardVariableDeclaration211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_Variable212"):
                opp_val = getattr(old_value, "optGrammar_Variable212", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_Variable212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_Variable212"):
                opp_val = getattr(value, "optGrammar_Variable212", None)
                setattr(value, "optGrammar_Variable212", self)

class optGrammar_VarVariableTupleVariableDeclaration(SimpleStatement2, SimpleStatement):

    def __init__(self, semicolon: bool, optGrammar_VarVariableTupleVariableDeclaration: "optGrammar_Tuple" = None, optGrammar_VarVariableTupleVariableDeclaration224: "optGrammar_Expression" = None):
        self.semicolon = semicolon
        self.optGrammar_VarVariableTupleVariableDeclaration = optGrammar_VarVariableTupleVariableDeclaration
        self.optGrammar_VarVariableTupleVariableDeclaration224 = optGrammar_VarVariableTupleVariableDeclaration224
        
    @property
    def semicolon(self) -> bool:
        return self.__semicolon

    @semicolon.setter
    def semicolon(self, semicolon: bool):
        self.__semicolon = semicolon

    @property
    def optGrammar_VarVariableTupleVariableDeclaration224(self):
        return self.__optGrammar_VarVariableTupleVariableDeclaration224

    @optGrammar_VarVariableTupleVariableDeclaration224.setter
    def optGrammar_VarVariableTupleVariableDeclaration224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_VarVariableTupleVariableDeclaration__optGrammar_VarVariableTupleVariableDeclaration224", None)
        self.__optGrammar_VarVariableTupleVariableDeclaration224 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_Expression225"):
                opp_val = getattr(old_value, "optGrammar_Expression225", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_Expression225", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_Expression225"):
                opp_val = getattr(value, "optGrammar_Expression225", None)
                setattr(value, "optGrammar_Expression225", self)

    @property
    def optGrammar_VarVariableTupleVariableDeclaration(self):
        return self.__optGrammar_VarVariableTupleVariableDeclaration

    @optGrammar_VarVariableTupleVariableDeclaration.setter
    def optGrammar_VarVariableTupleVariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_VarVariableTupleVariableDeclaration__optGrammar_VarVariableTupleVariableDeclaration", None)
        self.__optGrammar_VarVariableTupleVariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_Tuple222"):
                opp_val = getattr(old_value, "optGrammar_Tuple222", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_Tuple222", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_Tuple222"):
                opp_val = getattr(value, "optGrammar_Tuple222", None)
                setattr(value, "optGrammar_Tuple222", self)

class optGrammar_ExpressionStatement(SimpleStatement2, SimpleStatement):

    def __init__(self, semicolon: bool, optGrammar_ExpressionStatement: "optGrammar_Expression" = None, optGrammar_ExpressionStatement138: "optGrammar_ForStatement" = None):
        self.semicolon = semicolon
        self.optGrammar_ExpressionStatement = optGrammar_ExpressionStatement
        self.optGrammar_ExpressionStatement138 = optGrammar_ExpressionStatement138
        
    @property
    def semicolon(self) -> bool:
        return self.__semicolon

    @semicolon.setter
    def semicolon(self, semicolon: bool):
        self.__semicolon = semicolon

    @property
    def optGrammar_ExpressionStatement(self):
        return self.__optGrammar_ExpressionStatement

    @optGrammar_ExpressionStatement.setter
    def optGrammar_ExpressionStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_ExpressionStatement__optGrammar_ExpressionStatement", None)
        self.__optGrammar_ExpressionStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_Expression83"):
                opp_val = getattr(old_value, "optGrammar_Expression83", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_Expression83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_Expression83"):
                opp_val = getattr(value, "optGrammar_Expression83", None)
                setattr(value, "optGrammar_Expression83", self)

    @property
    def optGrammar_ExpressionStatement138(self):
        return self.__optGrammar_ExpressionStatement138

    @optGrammar_ExpressionStatement138.setter
    def optGrammar_ExpressionStatement138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_ExpressionStatement__optGrammar_ExpressionStatement138", None)
        self.__optGrammar_ExpressionStatement138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_ForStatement137"):
                opp_val = getattr(old_value, "optGrammar_ForStatement137", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_ForStatement137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_ForStatement137"):
                opp_val = getattr(value, "optGrammar_ForStatement137", None)
                setattr(value, "optGrammar_ForStatement137", self)

class optGrammar_ReturnsParameterList:

    pass
class optGrammar_FunctionCallArg:

    def __init__(self, name: str, optGrammar_FunctionCallArg: "optGrammar_FunctionCallArguments" = None, optGrammar_FunctionCallArg33: "optGrammar_Expression" = None):
        self.name = name
        self.optGrammar_FunctionCallArg = optGrammar_FunctionCallArg
        self.optGrammar_FunctionCallArg33 = optGrammar_FunctionCallArg33
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def optGrammar_FunctionCallArg33(self):
        return self.__optGrammar_FunctionCallArg33

    @optGrammar_FunctionCallArg33.setter
    def optGrammar_FunctionCallArg33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_FunctionCallArg__optGrammar_FunctionCallArg33", None)
        self.__optGrammar_FunctionCallArg33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_Expression34"):
                opp_val = getattr(old_value, "optGrammar_Expression34", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_Expression34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_Expression34"):
                opp_val = getattr(value, "optGrammar_Expression34", None)
                setattr(value, "optGrammar_Expression34", self)

    @property
    def optGrammar_FunctionCallArg(self):
        return self.__optGrammar_FunctionCallArg

    @optGrammar_FunctionCallArg.setter
    def optGrammar_FunctionCallArg(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_FunctionCallArg__optGrammar_FunctionCallArg", None)
        self.__optGrammar_FunctionCallArg = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_FunctionCallArguments"):
                opp_val = getattr(old_value, "optGrammar_FunctionCallArguments", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_FunctionCallArguments"):
                opp_val = getattr(value, "optGrammar_FunctionCallArguments", None)
                if opp_val is None:
                    setattr(value, "optGrammar_FunctionCallArguments", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class optGrammar_FunctionCallArguments:

    pass
class optGrammar_LocationLiteral:

    def __init__(self, type: str, optGrammar_LocationLiteral: "optGrammar_NonArrayableDeclaration" = None, optGrammar_LocationLiteral71: "optGrammar_LocationSpecifier" = None):
        self.type = type
        self.optGrammar_LocationLiteral = optGrammar_LocationLiteral
        self.optGrammar_LocationLiteral71 = optGrammar_LocationLiteral71
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def optGrammar_LocationLiteral(self):
        return self.__optGrammar_LocationLiteral

    @optGrammar_LocationLiteral.setter
    def optGrammar_LocationLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_LocationLiteral__optGrammar_LocationLiteral", None)
        self.__optGrammar_LocationLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_NonArrayableDeclaration"):
                opp_val = getattr(old_value, "optGrammar_NonArrayableDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_NonArrayableDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_NonArrayableDeclaration"):
                opp_val = getattr(value, "optGrammar_NonArrayableDeclaration", None)
                setattr(value, "optGrammar_NonArrayableDeclaration", self)

    @property
    def optGrammar_LocationLiteral71(self):
        return self.__optGrammar_LocationLiteral71

    @optGrammar_LocationLiteral71.setter
    def optGrammar_LocationLiteral71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_LocationLiteral__optGrammar_LocationLiteral71", None)
        self.__optGrammar_LocationLiteral71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_LocationSpecifier"):
                opp_val = getattr(old_value, "optGrammar_LocationSpecifier", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_LocationSpecifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_LocationSpecifier"):
                opp_val = getattr(value, "optGrammar_LocationSpecifier", None)
                setattr(value, "optGrammar_LocationSpecifier", self)

class PrimaryTypeDeclaration:

    pass
class optGrammar_ArrayableDeclaration(PrimaryTypeDeclaration):

    pass
class optGrammar_NonArrayableDeclaration(PrimaryTypeDeclaration):

    pass
class PrimaryTypeDefinitionDeclaration:

    pass
class optGrammar_PrimaryTypeDeclaration(PrimaryTypeDefinitionDeclaration):

    def __init__(self, constant: bool, name: str, optGrammar_PrimaryTypeDeclaration: "optGrammar_PrimaryTypeDefinitionDeclaration" = None, optGrammar_PrimaryTypeDeclaration62: "optGrammar_VisibilityLiteral" = None):
        self.constant = constant
        self.name = name
        self.optGrammar_PrimaryTypeDeclaration = optGrammar_PrimaryTypeDeclaration
        self.optGrammar_PrimaryTypeDeclaration62 = optGrammar_PrimaryTypeDeclaration62
        
    @property
    def constant(self) -> bool:
        return self.__constant

    @constant.setter
    def constant(self, constant: bool):
        self.__constant = constant

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def optGrammar_PrimaryTypeDeclaration62(self):
        return self.__optGrammar_PrimaryTypeDeclaration62

    @optGrammar_PrimaryTypeDeclaration62.setter
    def optGrammar_PrimaryTypeDeclaration62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_PrimaryTypeDeclaration__optGrammar_PrimaryTypeDeclaration62", None)
        self.__optGrammar_PrimaryTypeDeclaration62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_VisibilityLiteral63"):
                opp_val = getattr(old_value, "optGrammar_VisibilityLiteral63", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_VisibilityLiteral63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_VisibilityLiteral63"):
                opp_val = getattr(value, "optGrammar_VisibilityLiteral63", None)
                setattr(value, "optGrammar_VisibilityLiteral63", self)

    @property
    def optGrammar_PrimaryTypeDeclaration(self):
        return self.__optGrammar_PrimaryTypeDeclaration

    @optGrammar_PrimaryTypeDeclaration.setter
    def optGrammar_PrimaryTypeDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_PrimaryTypeDeclaration__optGrammar_PrimaryTypeDeclaration", None)
        self.__optGrammar_PrimaryTypeDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_PrimaryTypeDefinitionDeclaration57"):
                opp_val = getattr(old_value, "optGrammar_PrimaryTypeDefinitionDeclaration57", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_PrimaryTypeDefinitionDeclaration57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_PrimaryTypeDefinitionDeclaration57"):
                opp_val = getattr(value, "optGrammar_PrimaryTypeDefinitionDeclaration57", None)
                setattr(value, "optGrammar_PrimaryTypeDefinitionDeclaration57", self)

class optGrammar_Variable:

    def __init__(self, name: str, optGrammar_Variable: "optGrammar_ReturnParameterDeclaration" = None, optGrammar_Variable212: "optGrammar_StandardVariableDeclaration" = None, optGrammar_Variable235: "optGrammar_VariableDeclarationExpression" = None, optGrammar_Variable217: "optGrammar_VarVariableTypeDeclaration" = None):
        self.name = name
        self.optGrammar_Variable = optGrammar_Variable
        self.optGrammar_Variable212 = optGrammar_Variable212
        self.optGrammar_Variable235 = optGrammar_Variable235
        self.optGrammar_Variable217 = optGrammar_Variable217
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def optGrammar_Variable(self):
        return self.__optGrammar_Variable

    @optGrammar_Variable.setter
    def optGrammar_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_Variable__optGrammar_Variable", None)
        self.__optGrammar_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_ReturnParameterDeclaration111"):
                opp_val = getattr(old_value, "optGrammar_ReturnParameterDeclaration111", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_ReturnParameterDeclaration111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_ReturnParameterDeclaration111"):
                opp_val = getattr(value, "optGrammar_ReturnParameterDeclaration111", None)
                setattr(value, "optGrammar_ReturnParameterDeclaration111", self)

    @property
    def optGrammar_Variable235(self):
        return self.__optGrammar_Variable235

    @optGrammar_Variable235.setter
    def optGrammar_Variable235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_Variable__optGrammar_Variable235", None)
        self.__optGrammar_Variable235 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_VariableDeclarationExpression234"):
                opp_val = getattr(old_value, "optGrammar_VariableDeclarationExpression234", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_VariableDeclarationExpression234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_VariableDeclarationExpression234"):
                opp_val = getattr(value, "optGrammar_VariableDeclarationExpression234", None)
                setattr(value, "optGrammar_VariableDeclarationExpression234", self)

    @property
    def optGrammar_Variable212(self):
        return self.__optGrammar_Variable212

    @optGrammar_Variable212.setter
    def optGrammar_Variable212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_Variable__optGrammar_Variable212", None)
        self.__optGrammar_Variable212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_StandardVariableDeclaration211"):
                opp_val = getattr(old_value, "optGrammar_StandardVariableDeclaration211", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_StandardVariableDeclaration211", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_StandardVariableDeclaration211"):
                opp_val = getattr(value, "optGrammar_StandardVariableDeclaration211", None)
                setattr(value, "optGrammar_StandardVariableDeclaration211", self)

    @property
    def optGrammar_Variable217(self):
        return self.__optGrammar_Variable217

    @optGrammar_Variable217.setter
    def optGrammar_Variable217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_Variable__optGrammar_Variable217", None)
        self.__optGrammar_Variable217 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_VarVariableTypeDeclaration"):
                opp_val = getattr(old_value, "optGrammar_VarVariableTypeDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_VarVariableTypeDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_VarVariableTypeDeclaration"):
                opp_val = getattr(value, "optGrammar_VarVariableTypeDeclaration", None)
                setattr(value, "optGrammar_VarVariableTypeDeclaration", self)

class optGrammar_EnumValue:

    def __init__(self, name: str, optGrammar_EnumValue: "optGrammar_EnumDefinition" = None):
        self.name = name
        self.optGrammar_EnumValue = optGrammar_EnumValue
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def optGrammar_EnumValue(self):
        return self.__optGrammar_EnumValue

    @optGrammar_EnumValue.setter
    def optGrammar_EnumValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_EnumValue__optGrammar_EnumValue", None)
        self.__optGrammar_EnumValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_EnumDefinition"):
                opp_val = getattr(old_value, "optGrammar_EnumDefinition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_EnumDefinition"):
                opp_val = getattr(value, "optGrammar_EnumDefinition", None)
                if opp_val is None:
                    setattr(value, "optGrammar_EnumDefinition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class optGrammar_InheritanceSpecifier:

    pass
class optGrammar_SymbolAlias:

    def __init__(self, symbol: str, alias: str, optGrammar_SymbolAlias: "optGrammar_ImportDirective" = None):
        self.symbol = symbol
        self.alias = alias
        self.optGrammar_SymbolAlias = optGrammar_SymbolAlias
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def optGrammar_SymbolAlias(self):
        return self.__optGrammar_SymbolAlias

    @optGrammar_SymbolAlias.setter
    def optGrammar_SymbolAlias(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_SymbolAlias__optGrammar_SymbolAlias", None)
        self.__optGrammar_SymbolAlias = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_ImportDirective8"):
                opp_val = getattr(old_value, "optGrammar_ImportDirective8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_ImportDirective8"):
                opp_val = getattr(value, "optGrammar_ImportDirective8", None)
                if opp_val is None:
                    setattr(value, "optGrammar_ImportDirective8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class optGrammar_versionOperator:

    def __init__(self, value: str, optGrammar_versionOperator: "optGrammar_PragmaDirective" = None):
        self.value = value
        self.optGrammar_versionOperator = optGrammar_versionOperator
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def optGrammar_versionOperator(self):
        return self.__optGrammar_versionOperator

    @optGrammar_versionOperator.setter
    def optGrammar_versionOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_versionOperator__optGrammar_versionOperator", None)
        self.__optGrammar_versionOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_PragmaDirective6"):
                opp_val = getattr(old_value, "optGrammar_PragmaDirective6", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_PragmaDirective6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_PragmaDirective6"):
                opp_val = getattr(value, "optGrammar_PragmaDirective6", None)
                setattr(value, "optGrammar_PragmaDirective6", self)

class optGrammar_Contract:

    def __init__(self, name: str, optGrammar_Contract12: set["optGrammar_DefinitionBody"] = None, optGrammar_Contract26: "optGrammar_InheritanceSpecifier" = None, optGrammar_Contract: "optGrammar_Model" = None, optGrammar_Contract10: set["optGrammar_InheritanceSpecifier"] = None, optGrammar_Contract162: "optGrammar_NewExpression" = None):
        self.name = name
        self.optGrammar_Contract12 = optGrammar_Contract12 if optGrammar_Contract12 is not None else set()
        self.optGrammar_Contract26 = optGrammar_Contract26
        self.optGrammar_Contract = optGrammar_Contract
        self.optGrammar_Contract10 = optGrammar_Contract10 if optGrammar_Contract10 is not None else set()
        self.optGrammar_Contract162 = optGrammar_Contract162
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def optGrammar_Contract12(self):
        return self.__optGrammar_Contract12

    @optGrammar_Contract12.setter
    def optGrammar_Contract12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_Contract__optGrammar_Contract12", None)
        self.__optGrammar_Contract12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "optGrammar_DefinitionBody"):
                    opp_val = getattr(item, "optGrammar_DefinitionBody", None)
                    
                    if opp_val == self:
                        setattr(item, "optGrammar_DefinitionBody", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "optGrammar_DefinitionBody"):
                    opp_val = getattr(item, "optGrammar_DefinitionBody", None)
                    
                    setattr(item, "optGrammar_DefinitionBody", self)
                    

    @property
    def optGrammar_Contract26(self):
        return self.__optGrammar_Contract26

    @optGrammar_Contract26.setter
    def optGrammar_Contract26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_Contract__optGrammar_Contract26", None)
        self.__optGrammar_Contract26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_InheritanceSpecifier25"):
                opp_val = getattr(old_value, "optGrammar_InheritanceSpecifier25", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_InheritanceSpecifier25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_InheritanceSpecifier25"):
                opp_val = getattr(value, "optGrammar_InheritanceSpecifier25", None)
                setattr(value, "optGrammar_InheritanceSpecifier25", self)

    @property
    def optGrammar_Contract10(self):
        return self.__optGrammar_Contract10

    @optGrammar_Contract10.setter
    def optGrammar_Contract10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_Contract__optGrammar_Contract10", None)
        self.__optGrammar_Contract10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "optGrammar_InheritanceSpecifier"):
                    opp_val = getattr(item, "optGrammar_InheritanceSpecifier", None)
                    
                    if opp_val == self:
                        setattr(item, "optGrammar_InheritanceSpecifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "optGrammar_InheritanceSpecifier"):
                    opp_val = getattr(item, "optGrammar_InheritanceSpecifier", None)
                    
                    setattr(item, "optGrammar_InheritanceSpecifier", self)
                    

    @property
    def optGrammar_Contract(self):
        return self.__optGrammar_Contract

    @optGrammar_Contract.setter
    def optGrammar_Contract(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_Contract__optGrammar_Contract", None)
        self.__optGrammar_Contract = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_Model4"):
                opp_val = getattr(old_value, "optGrammar_Model4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_Model4"):
                opp_val = getattr(value, "optGrammar_Model4", None)
                if opp_val is None:
                    setattr(value, "optGrammar_Model4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def optGrammar_Contract162(self):
        return self.__optGrammar_Contract162

    @optGrammar_Contract162.setter
    def optGrammar_Contract162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_Contract__optGrammar_Contract162", None)
        self.__optGrammar_Contract162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_NewExpression"):
                opp_val = getattr(old_value, "optGrammar_NewExpression", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_NewExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_NewExpression"):
                opp_val = getattr(value, "optGrammar_NewExpression", None)
                setattr(value, "optGrammar_NewExpression", self)

class optGrammar_ImportDirective:

    def __init__(self, importURI: str, unitAlias: str, optGrammar_ImportDirective: "optGrammar_Model" = None, optGrammar_ImportDirective8: set["optGrammar_SymbolAlias"] = None):
        self.importURI = importURI
        self.unitAlias = unitAlias
        self.optGrammar_ImportDirective = optGrammar_ImportDirective
        self.optGrammar_ImportDirective8 = optGrammar_ImportDirective8 if optGrammar_ImportDirective8 is not None else set()
        
    @property
    def importURI(self) -> str:
        return self.__importURI

    @importURI.setter
    def importURI(self, importURI: str):
        self.__importURI = importURI

    @property
    def unitAlias(self) -> str:
        return self.__unitAlias

    @unitAlias.setter
    def unitAlias(self, unitAlias: str):
        self.__unitAlias = unitAlias

    @property
    def optGrammar_ImportDirective8(self):
        return self.__optGrammar_ImportDirective8

    @optGrammar_ImportDirective8.setter
    def optGrammar_ImportDirective8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_ImportDirective__optGrammar_ImportDirective8", None)
        self.__optGrammar_ImportDirective8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "optGrammar_SymbolAlias"):
                    opp_val = getattr(item, "optGrammar_SymbolAlias", None)
                    
                    if opp_val == self:
                        setattr(item, "optGrammar_SymbolAlias", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "optGrammar_SymbolAlias"):
                    opp_val = getattr(item, "optGrammar_SymbolAlias", None)
                    
                    setattr(item, "optGrammar_SymbolAlias", self)
                    

    @property
    def optGrammar_ImportDirective(self):
        return self.__optGrammar_ImportDirective

    @optGrammar_ImportDirective.setter
    def optGrammar_ImportDirective(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_ImportDirective__optGrammar_ImportDirective", None)
        self.__optGrammar_ImportDirective = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_Model2"):
                opp_val = getattr(old_value, "optGrammar_Model2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_Model2"):
                opp_val = getattr(value, "optGrammar_Model2", None)
                if opp_val is None:
                    setattr(value, "optGrammar_Model2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class optGrammar_PragmaDirective:

    pass
class optGrammar_Expression(PrimaryArithmetic):

    pass
class FunctionCallArguments:

    pass
class optGrammar_FunctionCallListArguments(FunctionCallArguments):

    pass
class optGrammar_Body(Statement):

    pass
class optGrammar_VisibilityLiteral:

    def __init__(self, type: str, optGrammar_VisibilityLiteral: "optGrammar_ConstructorDefinition" = None, optGrammar_VisibilityLiteral63: "optGrammar_PrimaryTypeDeclaration" = None, optGrammar_VisibilityLiteral48: "optGrammar_FunctionDefinition" = None, optGrammar_VisibilityLiteral69: "optGrammar_VisibilitySpecifier" = None):
        self.type = type
        self.optGrammar_VisibilityLiteral = optGrammar_VisibilityLiteral
        self.optGrammar_VisibilityLiteral63 = optGrammar_VisibilityLiteral63
        self.optGrammar_VisibilityLiteral48 = optGrammar_VisibilityLiteral48
        self.optGrammar_VisibilityLiteral69 = optGrammar_VisibilityLiteral69
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def optGrammar_VisibilityLiteral(self):
        return self.__optGrammar_VisibilityLiteral

    @optGrammar_VisibilityLiteral.setter
    def optGrammar_VisibilityLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_VisibilityLiteral__optGrammar_VisibilityLiteral", None)
        self.__optGrammar_VisibilityLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_ConstructorDefinition21"):
                opp_val = getattr(old_value, "optGrammar_ConstructorDefinition21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_ConstructorDefinition21"):
                opp_val = getattr(value, "optGrammar_ConstructorDefinition21", None)
                if opp_val is None:
                    setattr(value, "optGrammar_ConstructorDefinition21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def optGrammar_VisibilityLiteral48(self):
        return self.__optGrammar_VisibilityLiteral48

    @optGrammar_VisibilityLiteral48.setter
    def optGrammar_VisibilityLiteral48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_VisibilityLiteral__optGrammar_VisibilityLiteral48", None)
        self.__optGrammar_VisibilityLiteral48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_FunctionDefinition47"):
                opp_val = getattr(old_value, "optGrammar_FunctionDefinition47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_FunctionDefinition47"):
                opp_val = getattr(value, "optGrammar_FunctionDefinition47", None)
                if opp_val is None:
                    setattr(value, "optGrammar_FunctionDefinition47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def optGrammar_VisibilityLiteral63(self):
        return self.__optGrammar_VisibilityLiteral63

    @optGrammar_VisibilityLiteral63.setter
    def optGrammar_VisibilityLiteral63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_VisibilityLiteral__optGrammar_VisibilityLiteral63", None)
        self.__optGrammar_VisibilityLiteral63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_PrimaryTypeDeclaration62"):
                opp_val = getattr(old_value, "optGrammar_PrimaryTypeDeclaration62", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_PrimaryTypeDeclaration62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_PrimaryTypeDeclaration62"):
                opp_val = getattr(value, "optGrammar_PrimaryTypeDeclaration62", None)
                setattr(value, "optGrammar_PrimaryTypeDeclaration62", self)

    @property
    def optGrammar_VisibilityLiteral69(self):
        return self.__optGrammar_VisibilityLiteral69

    @optGrammar_VisibilityLiteral69.setter
    def optGrammar_VisibilityLiteral69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_VisibilityLiteral__optGrammar_VisibilityLiteral69", None)
        self.__optGrammar_VisibilityLiteral69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_VisibilitySpecifier"):
                opp_val = getattr(old_value, "optGrammar_VisibilitySpecifier", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_VisibilitySpecifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_VisibilitySpecifier"):
                opp_val = getattr(value, "optGrammar_VisibilitySpecifier", None)
                setattr(value, "optGrammar_VisibilitySpecifier", self)

class optGrammar_ModifierInvocation:

    pass
class optGrammar_Const:

    pass
class optGrammar_StateMutability:

    def __init__(self, type: str, optGrammar_StateMutability: "optGrammar_ConstructorDefinition" = None, optGrammar_StateMutability39: "optGrammar_FunctionDefinition" = None):
        self.type = type
        self.optGrammar_StateMutability = optGrammar_StateMutability
        self.optGrammar_StateMutability39 = optGrammar_StateMutability39
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def optGrammar_StateMutability(self):
        return self.__optGrammar_StateMutability

    @optGrammar_StateMutability.setter
    def optGrammar_StateMutability(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_StateMutability__optGrammar_StateMutability", None)
        self.__optGrammar_StateMutability = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_ConstructorDefinition15"):
                opp_val = getattr(old_value, "optGrammar_ConstructorDefinition15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_ConstructorDefinition15"):
                opp_val = getattr(value, "optGrammar_ConstructorDefinition15", None)
                if opp_val is None:
                    setattr(value, "optGrammar_ConstructorDefinition15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def optGrammar_StateMutability39(self):
        return self.__optGrammar_StateMutability39

    @optGrammar_StateMutability39.setter
    def optGrammar_StateMutability39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_StateMutability__optGrammar_StateMutability39", None)
        self.__optGrammar_StateMutability39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_FunctionDefinition38"):
                opp_val = getattr(old_value, "optGrammar_FunctionDefinition38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_FunctionDefinition38"):
                opp_val = getattr(value, "optGrammar_FunctionDefinition38", None)
                if opp_val is None:
                    setattr(value, "optGrammar_FunctionDefinition38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class optGrammar_ParameterList:

    pass
class DefinitionBody:

    pass
class optGrammar_StructDefinition(DefinitionBody):

    def __init__(self, name: str, optGrammar_StructDefinition: set["optGrammar_PrimaryTypeDefinitionDeclaration"] = None):
        self.name = name
        self.optGrammar_StructDefinition = optGrammar_StructDefinition if optGrammar_StructDefinition is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def optGrammar_StructDefinition(self):
        return self.__optGrammar_StructDefinition

    @optGrammar_StructDefinition.setter
    def optGrammar_StructDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_StructDefinition__optGrammar_StructDefinition", None)
        self.__optGrammar_StructDefinition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "optGrammar_PrimaryTypeDefinitionDeclaration"):
                    opp_val = getattr(item, "optGrammar_PrimaryTypeDefinitionDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "optGrammar_PrimaryTypeDefinitionDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "optGrammar_PrimaryTypeDefinitionDeclaration"):
                    opp_val = getattr(item, "optGrammar_PrimaryTypeDefinitionDeclaration", None)
                    
                    setattr(item, "optGrammar_PrimaryTypeDefinitionDeclaration", self)
                    

class optGrammar_EnumDefinition(DefinitionBody):

    def __init__(self, name: str, optGrammar_EnumDefinition: set["optGrammar_EnumValue"] = None):
        self.name = name
        self.optGrammar_EnumDefinition = optGrammar_EnumDefinition if optGrammar_EnumDefinition is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def optGrammar_EnumDefinition(self):
        return self.__optGrammar_EnumDefinition

    @optGrammar_EnumDefinition.setter
    def optGrammar_EnumDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_EnumDefinition__optGrammar_EnumDefinition", None)
        self.__optGrammar_EnumDefinition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "optGrammar_EnumValue"):
                    opp_val = getattr(item, "optGrammar_EnumValue", None)
                    
                    if opp_val == self:
                        setattr(item, "optGrammar_EnumValue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "optGrammar_EnumValue"):
                    opp_val = getattr(item, "optGrammar_EnumValue", None)
                    
                    setattr(item, "optGrammar_EnumValue", self)
                    

class optGrammar_FunctionDefinition(DefinitionBody):

    def __init__(self, name: str, optGrammar_FunctionDefinition: "optGrammar_ParameterList" = None, optGrammar_FunctionDefinition38: set["optGrammar_StateMutability"] = None, optGrammar_FunctionDefinition41: set["optGrammar_Const"] = None, optGrammar_FunctionDefinition44: set["optGrammar_ModifierInvocation"] = None, optGrammar_FunctionDefinition47: set["optGrammar_VisibilityLiteral"] = None, optGrammar_FunctionDefinition50: "optGrammar_ReturnsParameterList" = None, optGrammar_FunctionDefinition52: "optGrammar_Body" = None, optGrammar_FunctionDefinition174: "optGrammar_FunctionCall" = None):
        self.name = name
        self.optGrammar_FunctionDefinition = optGrammar_FunctionDefinition
        self.optGrammar_FunctionDefinition38 = optGrammar_FunctionDefinition38 if optGrammar_FunctionDefinition38 is not None else set()
        self.optGrammar_FunctionDefinition41 = optGrammar_FunctionDefinition41 if optGrammar_FunctionDefinition41 is not None else set()
        self.optGrammar_FunctionDefinition44 = optGrammar_FunctionDefinition44 if optGrammar_FunctionDefinition44 is not None else set()
        self.optGrammar_FunctionDefinition47 = optGrammar_FunctionDefinition47 if optGrammar_FunctionDefinition47 is not None else set()
        self.optGrammar_FunctionDefinition50 = optGrammar_FunctionDefinition50
        self.optGrammar_FunctionDefinition52 = optGrammar_FunctionDefinition52
        self.optGrammar_FunctionDefinition174 = optGrammar_FunctionDefinition174
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def optGrammar_FunctionDefinition(self):
        return self.__optGrammar_FunctionDefinition

    @optGrammar_FunctionDefinition.setter
    def optGrammar_FunctionDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_FunctionDefinition__optGrammar_FunctionDefinition", None)
        self.__optGrammar_FunctionDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_ParameterList36"):
                opp_val = getattr(old_value, "optGrammar_ParameterList36", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_ParameterList36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_ParameterList36"):
                opp_val = getattr(value, "optGrammar_ParameterList36", None)
                setattr(value, "optGrammar_ParameterList36", self)

    @property
    def optGrammar_FunctionDefinition38(self):
        return self.__optGrammar_FunctionDefinition38

    @optGrammar_FunctionDefinition38.setter
    def optGrammar_FunctionDefinition38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_FunctionDefinition__optGrammar_FunctionDefinition38", None)
        self.__optGrammar_FunctionDefinition38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "optGrammar_StateMutability39"):
                    opp_val = getattr(item, "optGrammar_StateMutability39", None)
                    
                    if opp_val == self:
                        setattr(item, "optGrammar_StateMutability39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "optGrammar_StateMutability39"):
                    opp_val = getattr(item, "optGrammar_StateMutability39", None)
                    
                    setattr(item, "optGrammar_StateMutability39", self)
                    

    @property
    def optGrammar_FunctionDefinition50(self):
        return self.__optGrammar_FunctionDefinition50

    @optGrammar_FunctionDefinition50.setter
    def optGrammar_FunctionDefinition50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_FunctionDefinition__optGrammar_FunctionDefinition50", None)
        self.__optGrammar_FunctionDefinition50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_ReturnsParameterList"):
                opp_val = getattr(old_value, "optGrammar_ReturnsParameterList", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_ReturnsParameterList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_ReturnsParameterList"):
                opp_val = getattr(value, "optGrammar_ReturnsParameterList", None)
                setattr(value, "optGrammar_ReturnsParameterList", self)

    @property
    def optGrammar_FunctionDefinition44(self):
        return self.__optGrammar_FunctionDefinition44

    @optGrammar_FunctionDefinition44.setter
    def optGrammar_FunctionDefinition44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_FunctionDefinition__optGrammar_FunctionDefinition44", None)
        self.__optGrammar_FunctionDefinition44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "optGrammar_ModifierInvocation45"):
                    opp_val = getattr(item, "optGrammar_ModifierInvocation45", None)
                    
                    if opp_val == self:
                        setattr(item, "optGrammar_ModifierInvocation45", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "optGrammar_ModifierInvocation45"):
                    opp_val = getattr(item, "optGrammar_ModifierInvocation45", None)
                    
                    setattr(item, "optGrammar_ModifierInvocation45", self)
                    

    @property
    def optGrammar_FunctionDefinition41(self):
        return self.__optGrammar_FunctionDefinition41

    @optGrammar_FunctionDefinition41.setter
    def optGrammar_FunctionDefinition41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_FunctionDefinition__optGrammar_FunctionDefinition41", None)
        self.__optGrammar_FunctionDefinition41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "optGrammar_Const42"):
                    opp_val = getattr(item, "optGrammar_Const42", None)
                    
                    if opp_val == self:
                        setattr(item, "optGrammar_Const42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "optGrammar_Const42"):
                    opp_val = getattr(item, "optGrammar_Const42", None)
                    
                    setattr(item, "optGrammar_Const42", self)
                    

    @property
    def optGrammar_FunctionDefinition47(self):
        return self.__optGrammar_FunctionDefinition47

    @optGrammar_FunctionDefinition47.setter
    def optGrammar_FunctionDefinition47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_FunctionDefinition__optGrammar_FunctionDefinition47", None)
        self.__optGrammar_FunctionDefinition47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "optGrammar_VisibilityLiteral48"):
                    opp_val = getattr(item, "optGrammar_VisibilityLiteral48", None)
                    
                    if opp_val == self:
                        setattr(item, "optGrammar_VisibilityLiteral48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "optGrammar_VisibilityLiteral48"):
                    opp_val = getattr(item, "optGrammar_VisibilityLiteral48", None)
                    
                    setattr(item, "optGrammar_VisibilityLiteral48", self)
                    

    @property
    def optGrammar_FunctionDefinition174(self):
        return self.__optGrammar_FunctionDefinition174

    @optGrammar_FunctionDefinition174.setter
    def optGrammar_FunctionDefinition174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_FunctionDefinition__optGrammar_FunctionDefinition174", None)
        self.__optGrammar_FunctionDefinition174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_FunctionCall173"):
                opp_val = getattr(old_value, "optGrammar_FunctionCall173", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_FunctionCall173", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_FunctionCall173"):
                opp_val = getattr(value, "optGrammar_FunctionCall173", None)
                setattr(value, "optGrammar_FunctionCall173", self)

    @property
    def optGrammar_FunctionDefinition52(self):
        return self.__optGrammar_FunctionDefinition52

    @optGrammar_FunctionDefinition52.setter
    def optGrammar_FunctionDefinition52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_FunctionDefinition__optGrammar_FunctionDefinition52", None)
        self.__optGrammar_FunctionDefinition52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_Body53"):
                opp_val = getattr(old_value, "optGrammar_Body53", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_Body53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_Body53"):
                opp_val = getattr(value, "optGrammar_Body53", None)
                setattr(value, "optGrammar_Body53", self)

class optGrammar_Event(DefinitionBody):

    def __init__(self, name: str, isAnonymous: bool, optGrammar_Event: "optGrammar_ParameterList" = None):
        self.name = name
        self.isAnonymous = isAnonymous
        self.optGrammar_Event = optGrammar_Event
        
    @property
    def isAnonymous(self) -> bool:
        return self.__isAnonymous

    @isAnonymous.setter
    def isAnonymous(self, isAnonymous: bool):
        self.__isAnonymous = isAnonymous

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def optGrammar_Event(self):
        return self.__optGrammar_Event

    @optGrammar_Event.setter
    def optGrammar_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_Event__optGrammar_Event", None)
        self.__optGrammar_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_ParameterList95"):
                opp_val = getattr(old_value, "optGrammar_ParameterList95", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_ParameterList95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_ParameterList95"):
                opp_val = getattr(value, "optGrammar_ParameterList95", None)
                setattr(value, "optGrammar_ParameterList95", self)

class optGrammar_Modifier(DefinitionBody):

    def __init__(self, name: str, optGrammar_Modifier98: "optGrammar_ModifierInvocation" = None, optGrammar_Modifier: "optGrammar_ParameterList" = None, optGrammar_Modifier92: "optGrammar_Body" = None):
        self.name = name
        self.optGrammar_Modifier98 = optGrammar_Modifier98
        self.optGrammar_Modifier = optGrammar_Modifier
        self.optGrammar_Modifier92 = optGrammar_Modifier92
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def optGrammar_Modifier92(self):
        return self.__optGrammar_Modifier92

    @optGrammar_Modifier92.setter
    def optGrammar_Modifier92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_Modifier__optGrammar_Modifier92", None)
        self.__optGrammar_Modifier92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_Body93"):
                opp_val = getattr(old_value, "optGrammar_Body93", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_Body93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_Body93"):
                opp_val = getattr(value, "optGrammar_Body93", None)
                setattr(value, "optGrammar_Body93", self)

    @property
    def optGrammar_Modifier(self):
        return self.__optGrammar_Modifier

    @optGrammar_Modifier.setter
    def optGrammar_Modifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_Modifier__optGrammar_Modifier", None)
        self.__optGrammar_Modifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_ParameterList90"):
                opp_val = getattr(old_value, "optGrammar_ParameterList90", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_ParameterList90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_ParameterList90"):
                opp_val = getattr(value, "optGrammar_ParameterList90", None)
                setattr(value, "optGrammar_ParameterList90", self)

    @property
    def optGrammar_Modifier98(self):
        return self.__optGrammar_Modifier98

    @optGrammar_Modifier98.setter
    def optGrammar_Modifier98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_Modifier__optGrammar_Modifier98", None)
        self.__optGrammar_Modifier98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_ModifierInvocation97"):
                opp_val = getattr(old_value, "optGrammar_ModifierInvocation97", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_ModifierInvocation97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_ModifierInvocation97"):
                opp_val = getattr(value, "optGrammar_ModifierInvocation97", None)
                setattr(value, "optGrammar_ModifierInvocation97", self)

class optGrammar_PrimaryTypeDefinitionDeclaration(DefinitionBody):

    pass
class optGrammar_ConstructorDefinition(DefinitionBody):

    def __init__(self, name: str, optGrammar_ConstructorDefinition: "optGrammar_ParameterList" = None, optGrammar_ConstructorDefinition15: set["optGrammar_StateMutability"] = None, optGrammar_ConstructorDefinition17: set["optGrammar_Const"] = None, optGrammar_ConstructorDefinition19: set["optGrammar_ModifierInvocation"] = None, optGrammar_ConstructorDefinition21: set["optGrammar_VisibilityLiteral"] = None, optGrammar_ConstructorDefinition23: "optGrammar_Body" = None):
        self.name = name
        self.optGrammar_ConstructorDefinition = optGrammar_ConstructorDefinition
        self.optGrammar_ConstructorDefinition15 = optGrammar_ConstructorDefinition15 if optGrammar_ConstructorDefinition15 is not None else set()
        self.optGrammar_ConstructorDefinition17 = optGrammar_ConstructorDefinition17 if optGrammar_ConstructorDefinition17 is not None else set()
        self.optGrammar_ConstructorDefinition19 = optGrammar_ConstructorDefinition19 if optGrammar_ConstructorDefinition19 is not None else set()
        self.optGrammar_ConstructorDefinition21 = optGrammar_ConstructorDefinition21 if optGrammar_ConstructorDefinition21 is not None else set()
        self.optGrammar_ConstructorDefinition23 = optGrammar_ConstructorDefinition23
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def optGrammar_ConstructorDefinition19(self):
        return self.__optGrammar_ConstructorDefinition19

    @optGrammar_ConstructorDefinition19.setter
    def optGrammar_ConstructorDefinition19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_ConstructorDefinition__optGrammar_ConstructorDefinition19", None)
        self.__optGrammar_ConstructorDefinition19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "optGrammar_ModifierInvocation"):
                    opp_val = getattr(item, "optGrammar_ModifierInvocation", None)
                    
                    if opp_val == self:
                        setattr(item, "optGrammar_ModifierInvocation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "optGrammar_ModifierInvocation"):
                    opp_val = getattr(item, "optGrammar_ModifierInvocation", None)
                    
                    setattr(item, "optGrammar_ModifierInvocation", self)
                    

    @property
    def optGrammar_ConstructorDefinition15(self):
        return self.__optGrammar_ConstructorDefinition15

    @optGrammar_ConstructorDefinition15.setter
    def optGrammar_ConstructorDefinition15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_ConstructorDefinition__optGrammar_ConstructorDefinition15", None)
        self.__optGrammar_ConstructorDefinition15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "optGrammar_StateMutability"):
                    opp_val = getattr(item, "optGrammar_StateMutability", None)
                    
                    if opp_val == self:
                        setattr(item, "optGrammar_StateMutability", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "optGrammar_StateMutability"):
                    opp_val = getattr(item, "optGrammar_StateMutability", None)
                    
                    setattr(item, "optGrammar_StateMutability", self)
                    

    @property
    def optGrammar_ConstructorDefinition21(self):
        return self.__optGrammar_ConstructorDefinition21

    @optGrammar_ConstructorDefinition21.setter
    def optGrammar_ConstructorDefinition21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_ConstructorDefinition__optGrammar_ConstructorDefinition21", None)
        self.__optGrammar_ConstructorDefinition21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "optGrammar_VisibilityLiteral"):
                    opp_val = getattr(item, "optGrammar_VisibilityLiteral", None)
                    
                    if opp_val == self:
                        setattr(item, "optGrammar_VisibilityLiteral", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "optGrammar_VisibilityLiteral"):
                    opp_val = getattr(item, "optGrammar_VisibilityLiteral", None)
                    
                    setattr(item, "optGrammar_VisibilityLiteral", self)
                    

    @property
    def optGrammar_ConstructorDefinition17(self):
        return self.__optGrammar_ConstructorDefinition17

    @optGrammar_ConstructorDefinition17.setter
    def optGrammar_ConstructorDefinition17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_ConstructorDefinition__optGrammar_ConstructorDefinition17", None)
        self.__optGrammar_ConstructorDefinition17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "optGrammar_Const"):
                    opp_val = getattr(item, "optGrammar_Const", None)
                    
                    if opp_val == self:
                        setattr(item, "optGrammar_Const", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "optGrammar_Const"):
                    opp_val = getattr(item, "optGrammar_Const", None)
                    
                    setattr(item, "optGrammar_Const", self)
                    

    @property
    def optGrammar_ConstructorDefinition23(self):
        return self.__optGrammar_ConstructorDefinition23

    @optGrammar_ConstructorDefinition23.setter
    def optGrammar_ConstructorDefinition23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_ConstructorDefinition__optGrammar_ConstructorDefinition23", None)
        self.__optGrammar_ConstructorDefinition23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_Body"):
                opp_val = getattr(old_value, "optGrammar_Body", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_Body", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_Body"):
                opp_val = getattr(value, "optGrammar_Body", None)
                setattr(value, "optGrammar_Body", self)

    @property
    def optGrammar_ConstructorDefinition(self):
        return self.__optGrammar_ConstructorDefinition

    @optGrammar_ConstructorDefinition.setter
    def optGrammar_ConstructorDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_optGrammar_ConstructorDefinition__optGrammar_ConstructorDefinition", None)
        self.__optGrammar_ConstructorDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optGrammar_ParameterList"):
                opp_val = getattr(old_value, "optGrammar_ParameterList", None)
                if opp_val == self:
                    setattr(old_value, "optGrammar_ParameterList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optGrammar_ParameterList"):
                opp_val = getattr(value, "optGrammar_ParameterList", None)
                setattr(value, "optGrammar_ParameterList", self)

class optGrammar_DefinitionBody:

    pass
class optGrammar_Model:

    pass