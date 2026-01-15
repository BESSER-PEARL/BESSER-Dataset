from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class IntegerCalculationOperator(Enum):
    ADD = "ADD"
    SUBRACT = "SUBRACT"
class ParameterMode(Enum):
    PARAM_IN = "PARAM_IN"
    PARAM_OUT = "PARAM_OUT"
    PARAM_INOUT = "PARAM_INOUT"
class BooleanBinaryOperator(Enum):
    AND = "AND"
    OR = "OR"
class PrimitiveKind(Enum):
    PK_NULL = "PK_NULL"
    PK_VOID = "PK_VOID"
    PK_SHORT = "PK_SHORT"
    PK_LONG = "PK_LONG"
    PK_USHORT = "PK_USHORT"
    PK_ULONG = "PK_ULONG"
    PK_FLOAT = "PK_FLOAT"
    PK_DOUBLE = "PK_DOUBLE"
    PK_BOOLEAN = "PK_BOOLEAN"
    PK_CHAR = "PK_CHAR"
    PK_OCTET = "PK_OCTET"
    PK_ANY = "PK_ANY"
    PK_LONGDOUBLE = "PK_LONGDOUBLE"
    PK_WSTRING = "PK_WSTRING"
    PK_TYPECODE = "PK_TYPECODE"
    PK_WCHAR = "PK_WCHAR"
    PK_PRINCIPAL = "PK_PRINCIPAL"
    PK_STRING = "PK_STRING"
    PK_ULONGLONG = "PK_ULONGLONG"
    PK_OBJREF = "PK_OBJREF"
    PK_LONGLONG = "PK_LONGLONG"
class IntegerComparisonOperator(Enum):
    SMALLER = "SMALLER"
    SMALLER_EQUALS = "SMALLER_EQUALS"
    EQUALS = "EQUALS"
    GREATER_EQUALS = "GREATER_EQUALS"
    GREATER = "GREATER"
class BooleanUnaryOperator(Enum):
    NOT = "NOT"
class BoardType(Enum):
    RaspberryPi = "RaspberryPi"
    Arduino = "Arduino"
    BeagleBoard = "BeagleBoard"


############################################
# Definition of Classes
############################################

class iot2_Token:

    pass
class iot2_Input:

    pass
class iot2_InputValue:

    pass
class iot2_Trace:

    pass
class BooleanExpression:

    pass
class iot2_BooleanUnaryExpression(BooleanExpression):

    def __init__(self, operator: str, iot2_BooleanUnaryExpression: "iot2_BooleanVariable" = None):
        self.operator = operator
        self.iot2_BooleanUnaryExpression = iot2_BooleanUnaryExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def iot2_BooleanUnaryExpression(self):
        return self.__iot2_BooleanUnaryExpression

    @iot2_BooleanUnaryExpression.setter
    def iot2_BooleanUnaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_BooleanUnaryExpression__iot2_BooleanUnaryExpression", None)
        self.__iot2_BooleanUnaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_BooleanVariable256"):
                opp_val = getattr(old_value, "iot2_BooleanVariable256", None)
                if opp_val == self:
                    setattr(old_value, "iot2_BooleanVariable256", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_BooleanVariable256"):
                opp_val = getattr(value, "iot2_BooleanVariable256", None)
                setattr(value, "iot2_BooleanVariable256", self)

class iot2_BooleanBinaryExpression(BooleanExpression):

    def __init__(self, operator: str, iot2_BooleanBinaryExpression: "iot2_BooleanVariable" = None, iot2_BooleanBinaryExpression260: "iot2_BooleanVariable" = None):
        self.operator = operator
        self.iot2_BooleanBinaryExpression = iot2_BooleanBinaryExpression
        self.iot2_BooleanBinaryExpression260 = iot2_BooleanBinaryExpression260
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def iot2_BooleanBinaryExpression(self):
        return self.__iot2_BooleanBinaryExpression

    @iot2_BooleanBinaryExpression.setter
    def iot2_BooleanBinaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_BooleanBinaryExpression__iot2_BooleanBinaryExpression", None)
        self.__iot2_BooleanBinaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_BooleanVariable258"):
                opp_val = getattr(old_value, "iot2_BooleanVariable258", None)
                if opp_val == self:
                    setattr(old_value, "iot2_BooleanVariable258", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_BooleanVariable258"):
                opp_val = getattr(value, "iot2_BooleanVariable258", None)
                setattr(value, "iot2_BooleanVariable258", self)

    @property
    def iot2_BooleanBinaryExpression260(self):
        return self.__iot2_BooleanBinaryExpression260

    @iot2_BooleanBinaryExpression260.setter
    def iot2_BooleanBinaryExpression260(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_BooleanBinaryExpression__iot2_BooleanBinaryExpression260", None)
        self.__iot2_BooleanBinaryExpression260 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_BooleanVariable261"):
                opp_val = getattr(old_value, "iot2_BooleanVariable261", None)
                if opp_val == self:
                    setattr(old_value, "iot2_BooleanVariable261", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_BooleanVariable261"):
                opp_val = getattr(value, "iot2_BooleanVariable261", None)
                setattr(value, "iot2_BooleanVariable261", self)

class Value:

    pass
class iot2_IntegerValue(Value):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class iot2_BooleanValue(Value):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class Variable:

    pass
class iot2_IntegerVariable(Variable):

    pass
class IntegerExpression:

    pass
class iot2_IntegerComparisonExpression(IntegerExpression):

    def __init__(self, operator: str, iot2_IntegerComparisonExpression: "iot2_BooleanVariable" = None):
        self.operator = operator
        self.iot2_IntegerComparisonExpression = iot2_IntegerComparisonExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def iot2_IntegerComparisonExpression(self):
        return self.__iot2_IntegerComparisonExpression

    @iot2_IntegerComparisonExpression.setter
    def iot2_IntegerComparisonExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_IntegerComparisonExpression__iot2_IntegerComparisonExpression", None)
        self.__iot2_IntegerComparisonExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_BooleanVariable254"):
                opp_val = getattr(old_value, "iot2_BooleanVariable254", None)
                if opp_val == self:
                    setattr(old_value, "iot2_BooleanVariable254", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_BooleanVariable254"):
                opp_val = getattr(value, "iot2_BooleanVariable254", None)
                setattr(value, "iot2_BooleanVariable254", self)

class iot2_IntegerCalculationExpression(IntegerExpression):

    def __init__(self, operator: str, iot2_IntegerCalculationExpression: "iot2_IntegerVariable" = None):
        self.operator = operator
        self.iot2_IntegerCalculationExpression = iot2_IntegerCalculationExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def iot2_IntegerCalculationExpression(self):
        return self.__iot2_IntegerCalculationExpression

    @iot2_IntegerCalculationExpression.setter
    def iot2_IntegerCalculationExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_IntegerCalculationExpression__iot2_IntegerCalculationExpression", None)
        self.__iot2_IntegerCalculationExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_IntegerVariable252"):
                opp_val = getattr(old_value, "iot2_IntegerVariable252", None)
                if opp_val == self:
                    setattr(old_value, "iot2_IntegerVariable252", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_IntegerVariable252"):
                opp_val = getattr(value, "iot2_IntegerVariable252", None)
                setattr(value, "iot2_IntegerVariable252", self)

class FinalNode:

    pass
class iot2_ActivityFinalNode(FinalNode):

    pass
class ControlNode:

    pass
class iot2_ForkNode(ControlNode):

    pass
class iot2_FinalNode(ControlNode):

    pass
class iot2_InitialNode(ControlNode):

    pass
class Action:

    pass
class iot2_OpaqueAction(Action):

    pass
class ExecutableNode:

    pass
class iot2_Action(ExecutableNode):

    pass
class ActivityNode:

    pass
class iot2_ExecutableNode(ActivityNode):

    pass
class iot2_Value:

    pass
class iot2_DecisionNode(ControlNode):

    pass
class iot2_MergeNode(ControlNode):

    pass
class iot2_JoinNode(ControlNode):

    pass
class iot2_ControlNode(ActivityNode):

    pass
class iot2_BooleanVariable(Variable):

    pass
class ActivityEdge:

    pass
class iot2_ControlFlow(ActivityEdge):

    pass
class LastStatement_Return:

    pass
class iot2_LastStatement_ReturnWithValue(LastStatement_Return):

    pass
class Field:

    pass
class iot2_Field_AppendEntryToTable(Field):

    pass
class iot2_Field_AddEntryToTable(Field):

    def __init__(self, key: str):
        self.key = key
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

class iot2_Field_AddEntryToTable_Brackets(Field):

    pass
class iot2_Functioncall_Arguments:

    pass
class Expression:

    pass
class iot2_Expression_Equal(Expression):

    pass
class iot2_Expression_VariableName(Expression):

    def __init__(self, variable: str):
        self.variable = variable
        
    @property
    def variable(self) -> str:
        return self.__variable

    @variable.setter
    def variable(self, variable: str):
        self.__variable = variable

class iot2_Expression_Larger_Equal(Expression):

    pass
class iot2_Expression_Number(Expression):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class iot2_Expression_Not_Equal(Expression):

    pass
class iot2_Expression_And(Expression):

    pass
class iot2_Expression_Multiplication(Expression):

    pass
class iot2_Expression_CallMemberFunction(Expression):

    def __init__(self, memberFunctionName: str, iot2_Expression_CallMemberFunction: "iot2_Expression" = None, iot2_Expression_CallMemberFunction205: "iot2_Functioncall_Arguments" = None):
        self.memberFunctionName = memberFunctionName
        self.iot2_Expression_CallMemberFunction = iot2_Expression_CallMemberFunction
        self.iot2_Expression_CallMemberFunction205 = iot2_Expression_CallMemberFunction205
        
    @property
    def memberFunctionName(self) -> str:
        return self.__memberFunctionName

    @memberFunctionName.setter
    def memberFunctionName(self, memberFunctionName: str):
        self.__memberFunctionName = memberFunctionName

    @property
    def iot2_Expression_CallMemberFunction(self):
        return self.__iot2_Expression_CallMemberFunction

    @iot2_Expression_CallMemberFunction.setter
    def iot2_Expression_CallMemberFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_CallMemberFunction__iot2_Expression_CallMemberFunction", None)
        self.__iot2_Expression_CallMemberFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression203"):
                opp_val = getattr(old_value, "iot2_Expression203", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression203", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression203"):
                opp_val = getattr(value, "iot2_Expression203", None)
                setattr(value, "iot2_Expression203", self)

    @property
    def iot2_Expression_CallMemberFunction205(self):
        return self.__iot2_Expression_CallMemberFunction205

    @iot2_Expression_CallMemberFunction205.setter
    def iot2_Expression_CallMemberFunction205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_CallMemberFunction__iot2_Expression_CallMemberFunction205", None)
        self.__iot2_Expression_CallMemberFunction205 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Functioncall_Arguments206"):
                opp_val = getattr(old_value, "iot2_Functioncall_Arguments206", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Functioncall_Arguments206", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Functioncall_Arguments206"):
                opp_val = getattr(value, "iot2_Functioncall_Arguments206", None)
                setattr(value, "iot2_Functioncall_Arguments206", self)

class iot2_BooleanExpression(Expression):

    pass
class iot2_Expression_VarArgs(Expression):

    pass
class iot2_Expression_Or(Expression):

    pass
class iot2_Expression_AccessMember(Expression):

    def __init__(self, memberName: str, iot2_Expression_AccessMember: "iot2_Expression" = None):
        self.memberName = memberName
        self.iot2_Expression_AccessMember = iot2_Expression_AccessMember
        
    @property
    def memberName(self) -> str:
        return self.__memberName

    @memberName.setter
    def memberName(self, memberName: str):
        self.__memberName = memberName

    @property
    def iot2_Expression_AccessMember(self):
        return self.__iot2_Expression_AccessMember

    @iot2_Expression_AccessMember.setter
    def iot2_Expression_AccessMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_AccessMember__iot2_Expression_AccessMember", None)
        self.__iot2_Expression_AccessMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression218"):
                opp_val = getattr(old_value, "iot2_Expression218", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression218", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression218"):
                opp_val = getattr(value, "iot2_Expression218", None)
                setattr(value, "iot2_Expression218", self)

class iot2_Expression_Exponentiation(Expression):

    pass
class iot2_Expression_Minus(Expression):

    pass
class iot2_Expression_Plus(Expression):

    pass
class iot2_Expression_False(Expression):

    pass
class iot2_IntegerExpression(Expression):

    pass
class iot2_Expression_AccessArray(Expression):

    pass
class iot2_Expression_String(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class iot2_Expression_True(Expression):

    pass
class iot2_Expression_Invert(Expression):

    pass
class iot2_Expression_Division(Expression):

    pass
class iot2_Expression_Smaller_Equal(Expression):

    pass
class iot2_Expression_Modulo(Expression):

    pass
class iot2_Expression_Concatenation(Expression):

    pass
class iot2_Expression_TableConstructor(Expression):

    pass
class iot2_Expression_Larger(Expression):

    pass
class iot2_Expression_CallFunction(Expression):

    pass
class iot2_Expression_Negate(Expression):

    pass
class iot2_Expression_Smaller(Expression):

    pass
class iot2_Expression_Function(Expression):

    pass
class iot2_Expression_Length(Expression):

    pass
class iot2_Expression_Nil(Expression):

    pass
class Statement_FunctioncallOrAssignment:

    pass
class iot2_Statement_Assignment(Statement_FunctioncallOrAssignment):

    pass
class iot2_Statement_CallMemberFunction(Statement_FunctioncallOrAssignment):

    def __init__(self, memberFunctionName: str, iot2_Statement_CallMemberFunction: "iot2_Expression" = None, iot2_Statement_CallMemberFunction114: "iot2_Functioncall_Arguments" = None):
        self.memberFunctionName = memberFunctionName
        self.iot2_Statement_CallMemberFunction = iot2_Statement_CallMemberFunction
        self.iot2_Statement_CallMemberFunction114 = iot2_Statement_CallMemberFunction114
        
    @property
    def memberFunctionName(self) -> str:
        return self.__memberFunctionName

    @memberFunctionName.setter
    def memberFunctionName(self, memberFunctionName: str):
        self.__memberFunctionName = memberFunctionName

    @property
    def iot2_Statement_CallMemberFunction(self):
        return self.__iot2_Statement_CallMemberFunction

    @iot2_Statement_CallMemberFunction.setter
    def iot2_Statement_CallMemberFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_CallMemberFunction__iot2_Statement_CallMemberFunction", None)
        self.__iot2_Statement_CallMemberFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression112"):
                opp_val = getattr(old_value, "iot2_Expression112", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression112"):
                opp_val = getattr(value, "iot2_Expression112", None)
                setattr(value, "iot2_Expression112", self)

    @property
    def iot2_Statement_CallMemberFunction114(self):
        return self.__iot2_Statement_CallMemberFunction114

    @iot2_Statement_CallMemberFunction114.setter
    def iot2_Statement_CallMemberFunction114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_CallMemberFunction__iot2_Statement_CallMemberFunction114", None)
        self.__iot2_Statement_CallMemberFunction114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Functioncall_Arguments115"):
                opp_val = getattr(old_value, "iot2_Functioncall_Arguments115", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Functioncall_Arguments115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Functioncall_Arguments115"):
                opp_val = getattr(value, "iot2_Functioncall_Arguments115", None)
                setattr(value, "iot2_Functioncall_Arguments115", self)

class iot2_Statement_CallFunction(Statement_FunctioncallOrAssignment):

    pass
class iot2_Function:

    def __init__(self, parameters: str, varArgs: bool, iot2_Function: "iot2_Statement_GlobalFunction_Declaration" = None, iot2_Function90: "iot2_Statement_LocalFunction_Declaration" = None, iot2_Function94: "iot2_Expression_Function" = None, iot2_Function98: "iot2_Block" = None):
        self.parameters = parameters
        self.varArgs = varArgs
        self.iot2_Function = iot2_Function
        self.iot2_Function90 = iot2_Function90
        self.iot2_Function94 = iot2_Function94
        self.iot2_Function98 = iot2_Function98
        
    @property
    def parameters(self) -> str:
        return self.__parameters

    @parameters.setter
    def parameters(self, parameters: str):
        self.__parameters = parameters

    @property
    def varArgs(self) -> bool:
        return self.__varArgs

    @varArgs.setter
    def varArgs(self, varArgs: bool):
        self.__varArgs = varArgs

    @property
    def iot2_Function90(self):
        return self.__iot2_Function90

    @iot2_Function90.setter
    def iot2_Function90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Function__iot2_Function90", None)
        self.__iot2_Function90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_LocalFunction_Declaration"):
                opp_val = getattr(old_value, "iot2_Statement_LocalFunction_Declaration", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_LocalFunction_Declaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_LocalFunction_Declaration"):
                opp_val = getattr(value, "iot2_Statement_LocalFunction_Declaration", None)
                setattr(value, "iot2_Statement_LocalFunction_Declaration", self)

    @property
    def iot2_Function(self):
        return self.__iot2_Function

    @iot2_Function.setter
    def iot2_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Function__iot2_Function", None)
        self.__iot2_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_GlobalFunction_Declaration"):
                opp_val = getattr(old_value, "iot2_Statement_GlobalFunction_Declaration", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_GlobalFunction_Declaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_GlobalFunction_Declaration"):
                opp_val = getattr(value, "iot2_Statement_GlobalFunction_Declaration", None)
                setattr(value, "iot2_Statement_GlobalFunction_Declaration", self)

    @property
    def iot2_Function98(self):
        return self.__iot2_Function98

    @iot2_Function98.setter
    def iot2_Function98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Function__iot2_Function98", None)
        self.__iot2_Function98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Block99"):
                opp_val = getattr(old_value, "iot2_Block99", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Block99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Block99"):
                opp_val = getattr(value, "iot2_Block99", None)
                setattr(value, "iot2_Block99", self)

    @property
    def iot2_Function94(self):
        return self.__iot2_Function94

    @iot2_Function94.setter
    def iot2_Function94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Function__iot2_Function94", None)
        self.__iot2_Function94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Function"):
                opp_val = getattr(old_value, "iot2_Expression_Function", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Function", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Function"):
                opp_val = getattr(value, "iot2_Expression_Function", None)
                setattr(value, "iot2_Expression_Function", self)

class Statement:

    pass
class iot2_Statement_FunctioncallOrAssignment(Statement):

    pass
class iot2_Statement_For_Generic(Statement):

    def __init__(self, names: str, iot2_Statement_For_Generic: set["iot2_Expression"] = None, iot2_Statement_For_Generic86: "iot2_Block" = None):
        self.names = names
        self.iot2_Statement_For_Generic = iot2_Statement_For_Generic if iot2_Statement_For_Generic is not None else set()
        self.iot2_Statement_For_Generic86 = iot2_Statement_For_Generic86
        
    @property
    def names(self) -> str:
        return self.__names

    @names.setter
    def names(self, names: str):
        self.__names = names

    @property
    def iot2_Statement_For_Generic86(self):
        return self.__iot2_Statement_For_Generic86

    @iot2_Statement_For_Generic86.setter
    def iot2_Statement_For_Generic86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_For_Generic__iot2_Statement_For_Generic86", None)
        self.__iot2_Statement_For_Generic86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Block87"):
                opp_val = getattr(old_value, "iot2_Block87", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Block87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Block87"):
                opp_val = getattr(value, "iot2_Block87", None)
                setattr(value, "iot2_Block87", self)

    @property
    def iot2_Statement_For_Generic(self):
        return self.__iot2_Statement_For_Generic

    @iot2_Statement_For_Generic.setter
    def iot2_Statement_For_Generic(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_For_Generic__iot2_Statement_For_Generic", None)
        self.__iot2_Statement_For_Generic = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_Expression84"):
                    opp_val = getattr(item, "iot2_Expression84", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_Expression84", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_Expression84"):
                    opp_val = getattr(item, "iot2_Expression84", None)
                    
                    setattr(item, "iot2_Expression84", self)
                    

class iot2_Statement_GlobalFunction_Declaration(Statement):

    def __init__(self, prefix: str, functionName: str, iot2_Statement_GlobalFunction_Declaration: "iot2_Function" = None):
        self.prefix = prefix
        self.functionName = functionName
        self.iot2_Statement_GlobalFunction_Declaration = iot2_Statement_GlobalFunction_Declaration
        
    @property
    def prefix(self) -> str:
        return self.__prefix

    @prefix.setter
    def prefix(self, prefix: str):
        self.__prefix = prefix

    @property
    def functionName(self) -> str:
        return self.__functionName

    @functionName.setter
    def functionName(self, functionName: str):
        self.__functionName = functionName

    @property
    def iot2_Statement_GlobalFunction_Declaration(self):
        return self.__iot2_Statement_GlobalFunction_Declaration

    @iot2_Statement_GlobalFunction_Declaration.setter
    def iot2_Statement_GlobalFunction_Declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_GlobalFunction_Declaration__iot2_Statement_GlobalFunction_Declaration", None)
        self.__iot2_Statement_GlobalFunction_Declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Function"):
                opp_val = getattr(old_value, "iot2_Function", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Function", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Function"):
                opp_val = getattr(value, "iot2_Function", None)
                setattr(value, "iot2_Function", self)

class iot2_Statement_LocalFunction_Declaration(Statement):

    def __init__(self, functionName: str, iot2_Statement_LocalFunction_Declaration: "iot2_Function" = None):
        self.functionName = functionName
        self.iot2_Statement_LocalFunction_Declaration = iot2_Statement_LocalFunction_Declaration
        
    @property
    def functionName(self) -> str:
        return self.__functionName

    @functionName.setter
    def functionName(self, functionName: str):
        self.__functionName = functionName

    @property
    def iot2_Statement_LocalFunction_Declaration(self):
        return self.__iot2_Statement_LocalFunction_Declaration

    @iot2_Statement_LocalFunction_Declaration.setter
    def iot2_Statement_LocalFunction_Declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_LocalFunction_Declaration__iot2_Statement_LocalFunction_Declaration", None)
        self.__iot2_Statement_LocalFunction_Declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Function90"):
                opp_val = getattr(old_value, "iot2_Function90", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Function90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Function90"):
                opp_val = getattr(value, "iot2_Function90", None)
                setattr(value, "iot2_Function90", self)

class iot2_Statement_While(Statement):

    pass
class iot2_Statement_Local_Variable_Declaration(Statement):

    def __init__(self, variableNames: str, iot2_Statement_Local_Variable_Declaration: set["iot2_Expression"] = None):
        self.variableNames = variableNames
        self.iot2_Statement_Local_Variable_Declaration = iot2_Statement_Local_Variable_Declaration if iot2_Statement_Local_Variable_Declaration is not None else set()
        
    @property
    def variableNames(self) -> str:
        return self.__variableNames

    @variableNames.setter
    def variableNames(self, variableNames: str):
        self.__variableNames = variableNames

    @property
    def iot2_Statement_Local_Variable_Declaration(self):
        return self.__iot2_Statement_Local_Variable_Declaration

    @iot2_Statement_Local_Variable_Declaration.setter
    def iot2_Statement_Local_Variable_Declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_Local_Variable_Declaration__iot2_Statement_Local_Variable_Declaration", None)
        self.__iot2_Statement_Local_Variable_Declaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_Expression92"):
                    opp_val = getattr(item, "iot2_Expression92", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_Expression92", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_Expression92"):
                    opp_val = getattr(item, "iot2_Expression92", None)
                    
                    setattr(item, "iot2_Expression92", self)
                    

class iot2_Statement_Repeat(Statement):

    pass
class iot2_Statement_For_Numeric(Statement):

    def __init__(self, iteratorName: str, iot2_Statement_For_Numeric: "iot2_Expression" = None, iot2_Statement_For_Numeric75: "iot2_Expression" = None, iot2_Statement_For_Numeric78: "iot2_Expression" = None, iot2_Statement_For_Numeric81: "iot2_Block" = None):
        self.iteratorName = iteratorName
        self.iot2_Statement_For_Numeric = iot2_Statement_For_Numeric
        self.iot2_Statement_For_Numeric75 = iot2_Statement_For_Numeric75
        self.iot2_Statement_For_Numeric78 = iot2_Statement_For_Numeric78
        self.iot2_Statement_For_Numeric81 = iot2_Statement_For_Numeric81
        
    @property
    def iteratorName(self) -> str:
        return self.__iteratorName

    @iteratorName.setter
    def iteratorName(self, iteratorName: str):
        self.__iteratorName = iteratorName

    @property
    def iot2_Statement_For_Numeric(self):
        return self.__iot2_Statement_For_Numeric

    @iot2_Statement_For_Numeric.setter
    def iot2_Statement_For_Numeric(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_For_Numeric__iot2_Statement_For_Numeric", None)
        self.__iot2_Statement_For_Numeric = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression73"):
                opp_val = getattr(old_value, "iot2_Expression73", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression73"):
                opp_val = getattr(value, "iot2_Expression73", None)
                setattr(value, "iot2_Expression73", self)

    @property
    def iot2_Statement_For_Numeric81(self):
        return self.__iot2_Statement_For_Numeric81

    @iot2_Statement_For_Numeric81.setter
    def iot2_Statement_For_Numeric81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_For_Numeric__iot2_Statement_For_Numeric81", None)
        self.__iot2_Statement_For_Numeric81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Block82"):
                opp_val = getattr(old_value, "iot2_Block82", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Block82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Block82"):
                opp_val = getattr(value, "iot2_Block82", None)
                setattr(value, "iot2_Block82", self)

    @property
    def iot2_Statement_For_Numeric75(self):
        return self.__iot2_Statement_For_Numeric75

    @iot2_Statement_For_Numeric75.setter
    def iot2_Statement_For_Numeric75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_For_Numeric__iot2_Statement_For_Numeric75", None)
        self.__iot2_Statement_For_Numeric75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression76"):
                opp_val = getattr(old_value, "iot2_Expression76", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression76"):
                opp_val = getattr(value, "iot2_Expression76", None)
                setattr(value, "iot2_Expression76", self)

    @property
    def iot2_Statement_For_Numeric78(self):
        return self.__iot2_Statement_For_Numeric78

    @iot2_Statement_For_Numeric78.setter
    def iot2_Statement_For_Numeric78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_For_Numeric__iot2_Statement_For_Numeric78", None)
        self.__iot2_Statement_For_Numeric78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression79"):
                opp_val = getattr(old_value, "iot2_Expression79", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression79"):
                opp_val = getattr(value, "iot2_Expression79", None)
                setattr(value, "iot2_Expression79", self)

class iot2_Statement_Block(Statement):

    pass
class LastStatement:

    pass
class iot2_LastStatement_Break(LastStatement):

    pass
class iot2_LastStatement_Return(LastStatement):

    pass
class iot2_LastStatement:

    pass
class iot2_Statement:

    pass
class Chunk:

    pass
class iot2_Chunk:

    pass
class iot2_Statement_If_Then_Else_ElseIfPart:

    pass
class iot2_Statement_If_Then_Else(Statement):

    pass
class IDLType:

    pass
class iot2_IDLType(ABC):

    def __init__(self, typeCode: str, iot2_IDLType: "iot2_Typed" = None):
        self.typeCode = typeCode
        self.iot2_IDLType = iot2_IDLType
        
    @property
    def typeCode(self) -> str:
        return self.__typeCode

    @typeCode.setter
    def typeCode(self, typeCode: str):
        self.__typeCode = typeCode

    @property
    def iot2_IDLType(self):
        return self.__iot2_IDLType

    @iot2_IDLType.setter
    def iot2_IDLType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_IDLType__iot2_IDLType", None)
        self.__iot2_IDLType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Typed"):
                opp_val = getattr(old_value, "iot2_Typed", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Typed", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Typed"):
                opp_val = getattr(value, "iot2_Typed", None)
                setattr(value, "iot2_Typed", self)

class iot2_Typed(ABC):

    pass
class iot2_NamedElement(ABC):

    def __init__(self, identifier: str, name: str):
        self.identifier = identifier
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

class iot2_PrimitiveDef(IDLType):

    def __init__(self, kind: str):
        self.kind = kind
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

class iot2_Expression(Statement_FunctioncallOrAssignment):

    pass
class Typed:

    pass
class iot2_Field(Typed):

    def __init__(self, identifier: str, iot2_Field39: "iot2_Expression" = None, iot2_Field: "iot2_ExceptionDef" = None, iot2_Field96: "iot2_Expression_TableConstructor" = None):
        self.identifier = identifier
        self.iot2_Field39 = iot2_Field39
        self.iot2_Field = iot2_Field
        self.iot2_Field96 = iot2_Field96
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def iot2_Field96(self):
        return self.__iot2_Field96

    @iot2_Field96.setter
    def iot2_Field96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Field__iot2_Field96", None)
        self.__iot2_Field96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_TableConstructor"):
                opp_val = getattr(old_value, "iot2_Expression_TableConstructor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_TableConstructor"):
                opp_val = getattr(value, "iot2_Expression_TableConstructor", None)
                if opp_val is None:
                    setattr(value, "iot2_Expression_TableConstructor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_Field(self):
        return self.__iot2_Field

    @iot2_Field.setter
    def iot2_Field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Field__iot2_Field", None)
        self.__iot2_Field = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_ExceptionDef37"):
                opp_val = getattr(old_value, "iot2_ExceptionDef37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_ExceptionDef37"):
                opp_val = getattr(value, "iot2_ExceptionDef37", None)
                if opp_val is None:
                    setattr(value, "iot2_ExceptionDef37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_Field39(self):
        return self.__iot2_Field39

    @iot2_Field39.setter
    def iot2_Field39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Field__iot2_Field39", None)
        self.__iot2_Field39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression"):
                opp_val = getattr(old_value, "iot2_Expression", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression"):
                opp_val = getattr(value, "iot2_Expression", None)
                setattr(value, "iot2_Expression", self)

class iot2_ParameterDef(Typed):

    def __init__(self, identifier: str, direction: str, iot2_ParameterDef: "iot2_OperationDef" = None):
        self.identifier = identifier
        self.direction = direction
        self.iot2_ParameterDef = iot2_ParameterDef
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def iot2_ParameterDef(self):
        return self.__iot2_ParameterDef

    @iot2_ParameterDef.setter
    def iot2_ParameterDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ParameterDef__iot2_ParameterDef", None)
        self.__iot2_ParameterDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_OperationDef22"):
                opp_val = getattr(old_value, "iot2_OperationDef22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_OperationDef22"):
                opp_val = getattr(value, "iot2_OperationDef22", None)
                if opp_val is None:
                    setattr(value, "iot2_OperationDef22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Contained:

    pass
class iot2_TypedefDef(Contained, IDLType):

    pass
class iot2_Container(Contained):

    pass
class iot2_Variable:

    def __init__(self, name: str, iot2_Variable: "iot2_Activity" = None, iot2_Variable20: "iot2_Activity" = None, iot2_Variable241: "iot2_Value" = None, iot2_Variable243: "iot2_Value" = None, iot2_Variable266: "iot2_InputValue" = None):
        self.name = name
        self.iot2_Variable = iot2_Variable
        self.iot2_Variable20 = iot2_Variable20
        self.iot2_Variable241 = iot2_Variable241
        self.iot2_Variable243 = iot2_Variable243
        self.iot2_Variable266 = iot2_Variable266
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iot2_Variable241(self):
        return self.__iot2_Variable241

    @iot2_Variable241.setter
    def iot2_Variable241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Variable__iot2_Variable241", None)
        self.__iot2_Variable241 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Value"):
                opp_val = getattr(old_value, "iot2_Value", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Value", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Value"):
                opp_val = getattr(value, "iot2_Value", None)
                setattr(value, "iot2_Value", self)

    @property
    def iot2_Variable(self):
        return self.__iot2_Variable

    @iot2_Variable.setter
    def iot2_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Variable__iot2_Variable", None)
        self.__iot2_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Activity17"):
                opp_val = getattr(old_value, "iot2_Activity17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Activity17"):
                opp_val = getattr(value, "iot2_Activity17", None)
                if opp_val is None:
                    setattr(value, "iot2_Activity17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_Variable20(self):
        return self.__iot2_Variable20

    @iot2_Variable20.setter
    def iot2_Variable20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Variable__iot2_Variable20", None)
        self.__iot2_Variable20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Activity19"):
                opp_val = getattr(old_value, "iot2_Activity19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Activity19"):
                opp_val = getattr(value, "iot2_Activity19", None)
                if opp_val is None:
                    setattr(value, "iot2_Activity19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_Variable266(self):
        return self.__iot2_Variable266

    @iot2_Variable266.setter
    def iot2_Variable266(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Variable__iot2_Variable266", None)
        self.__iot2_Variable266 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_InputValue265"):
                opp_val = getattr(old_value, "iot2_InputValue265", None)
                if opp_val == self:
                    setattr(old_value, "iot2_InputValue265", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_InputValue265"):
                opp_val = getattr(value, "iot2_InputValue265", None)
                setattr(value, "iot2_InputValue265", self)

    @property
    def iot2_Variable243(self):
        return self.__iot2_Variable243

    @iot2_Variable243.setter
    def iot2_Variable243(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Variable__iot2_Variable243", None)
        self.__iot2_Variable243 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Value244"):
                opp_val = getattr(old_value, "iot2_Value244", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Value244", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Value244"):
                opp_val = getattr(value, "iot2_Value244", None)
                setattr(value, "iot2_Value244", self)

class NamedElement:

    pass
class iot2_ActivityEdge(NamedElement):

    pass
class iot2_ActivityNode(NamedElement):

    def __init__(self, running: bool, 13: "iot2_Activity" = None, 233: "iot2_ActivityEdge" = None, 220: set["iot2_ActivityEdge"] = None, 223: set["iot2_ActivityEdge"] = None, 226: "iot2_Activity" = None, 230: "iot2_ActivityEdge" = None, iot2_ActivityNode271: "iot2_Trace" = None, iot2_ActivityNode: "iot2_Token" = None):
        self.running = running
        self.13 = 13
        self.233 = 233
        self.220 = 220 if 220 is not None else set()
        self.223 = 223 if 223 is not None else set()
        self.226 = 226
        self.230 = 230
        self.iot2_ActivityNode271 = iot2_ActivityNode271
        self.iot2_ActivityNode = iot2_ActivityNode
        
    @property
    def running(self) -> bool:
        return self.__running

    @running.setter
    def running(self, running: bool):
        self.__running = running

    @property
    def iot2_ActivityNode271(self):
        return self.__iot2_ActivityNode271

    @iot2_ActivityNode271.setter
    def iot2_ActivityNode271(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityNode__iot2_ActivityNode271", None)
        self.__iot2_ActivityNode271 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Trace"):
                opp_val = getattr(old_value, "iot2_Trace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Trace"):
                opp_val = getattr(value, "iot2_Trace", None)
                if opp_val is None:
                    setattr(value, "iot2_Trace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 230(self):
        return self.__230

    @230.setter
    def 230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityNode__230", None)
        self.__230 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "229"):
                opp_val = getattr(old_value, "229", None)
                if opp_val == self:
                    setattr(old_value, "229", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "229"):
                opp_val = getattr(value, "229", None)
                setattr(value, "229", self)

    @property
    def iot2_ActivityNode(self):
        return self.__iot2_ActivityNode

    @iot2_ActivityNode.setter
    def iot2_ActivityNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityNode__iot2_ActivityNode", None)
        self.__iot2_ActivityNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Token"):
                opp_val = getattr(old_value, "iot2_Token", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Token", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Token"):
                opp_val = getattr(value, "iot2_Token", None)
                setattr(value, "iot2_Token", self)

    @property
    def 13(self):
        return self.__13

    @13.setter
    def 13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityNode__13", None)
        self.__13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, ""):
                opp_val = getattr(old_value, "", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, ""):
                opp_val = getattr(value, "", None)
                if opp_val is None:
                    setattr(value, "", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 223(self):
        return self.__223

    @223.setter
    def 223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityNode__223", None)
        self.__223 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "224"):
                    opp_val = getattr(item, "224", None)
                    
                    if opp_val == self:
                        setattr(item, "224", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "224"):
                    opp_val = getattr(item, "224", None)
                    
                    setattr(item, "224", self)
                    

    @property
    def 220(self):
        return self.__220

    @220.setter
    def 220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityNode__220", None)
        self.__220 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "221"):
                    opp_val = getattr(item, "221", None)
                    
                    if opp_val == self:
                        setattr(item, "221", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "221"):
                    opp_val = getattr(item, "221", None)
                    
                    setattr(item, "221", self)
                    

    @property
    def 233(self):
        return self.__233

    @233.setter
    def 233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityNode__233", None)
        self.__233 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "232"):
                opp_val = getattr(old_value, "232", None)
                if opp_val == self:
                    setattr(old_value, "232", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "232"):
                opp_val = getattr(value, "232", None)
                setattr(value, "232", self)

    @property
    def 226(self):
        return self.__226

    @226.setter
    def 226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityNode__226", None)
        self.__226 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "227"):
                opp_val = getattr(old_value, "227", None)
                if opp_val == self:
                    setattr(old_value, "227", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "227"):
                opp_val = getattr(value, "227", None)
                setattr(value, "227", self)

class HWComponent:

    pass
class iot2_Actuator(HWComponent):

    pass
class iot2_Sensor(HWComponent):

    pass
class iot2_OperationDef(Contained, Typed):

    def __init__(self, isOneway: bool, contexts: str, iot2_OperationDef24: set["iot2_ExceptionDef"] = None, iot2_OperationDef26: "iot2_Block" = None, iot2_OperationDef: "iot2_HWComponent" = None, iot2_OperationDef22: set["iot2_ParameterDef"] = None, iot2_OperationDef239: "iot2_OpaqueAction" = None):
        self.isOneway = isOneway
        self.contexts = contexts
        self.iot2_OperationDef24 = iot2_OperationDef24 if iot2_OperationDef24 is not None else set()
        self.iot2_OperationDef26 = iot2_OperationDef26
        self.iot2_OperationDef = iot2_OperationDef
        self.iot2_OperationDef22 = iot2_OperationDef22 if iot2_OperationDef22 is not None else set()
        self.iot2_OperationDef239 = iot2_OperationDef239
        
    @property
    def contexts(self) -> str:
        return self.__contexts

    @contexts.setter
    def contexts(self, contexts: str):
        self.__contexts = contexts

    @property
    def isOneway(self) -> bool:
        return self.__isOneway

    @isOneway.setter
    def isOneway(self, isOneway: bool):
        self.__isOneway = isOneway

    @property
    def iot2_OperationDef26(self):
        return self.__iot2_OperationDef26

    @iot2_OperationDef26.setter
    def iot2_OperationDef26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_OperationDef__iot2_OperationDef26", None)
        self.__iot2_OperationDef26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Block"):
                opp_val = getattr(old_value, "iot2_Block", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Block", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Block"):
                opp_val = getattr(value, "iot2_Block", None)
                setattr(value, "iot2_Block", self)

    @property
    def iot2_OperationDef22(self):
        return self.__iot2_OperationDef22

    @iot2_OperationDef22.setter
    def iot2_OperationDef22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_OperationDef__iot2_OperationDef22", None)
        self.__iot2_OperationDef22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_ParameterDef"):
                    opp_val = getattr(item, "iot2_ParameterDef", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_ParameterDef", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_ParameterDef"):
                    opp_val = getattr(item, "iot2_ParameterDef", None)
                    
                    setattr(item, "iot2_ParameterDef", self)
                    

    @property
    def iot2_OperationDef239(self):
        return self.__iot2_OperationDef239

    @iot2_OperationDef239.setter
    def iot2_OperationDef239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_OperationDef__iot2_OperationDef239", None)
        self.__iot2_OperationDef239 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_OpaqueAction238"):
                opp_val = getattr(old_value, "iot2_OpaqueAction238", None)
                if opp_val == self:
                    setattr(old_value, "iot2_OpaqueAction238", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_OpaqueAction238"):
                opp_val = getattr(value, "iot2_OpaqueAction238", None)
                setattr(value, "iot2_OpaqueAction238", self)

    @property
    def iot2_OperationDef(self):
        return self.__iot2_OperationDef

    @iot2_OperationDef.setter
    def iot2_OperationDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_OperationDef__iot2_OperationDef", None)
        self.__iot2_OperationDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_HWComponent11"):
                opp_val = getattr(old_value, "iot2_HWComponent11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_HWComponent11"):
                opp_val = getattr(value, "iot2_HWComponent11", None)
                if opp_val is None:
                    setattr(value, "iot2_HWComponent11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_OperationDef24(self):
        return self.__iot2_OperationDef24

    @iot2_OperationDef24.setter
    def iot2_OperationDef24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_OperationDef__iot2_OperationDef24", None)
        self.__iot2_OperationDef24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_ExceptionDef"):
                    opp_val = getattr(item, "iot2_ExceptionDef", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_ExceptionDef", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_ExceptionDef"):
                    opp_val = getattr(item, "iot2_ExceptionDef", None)
                    
                    setattr(item, "iot2_ExceptionDef", self)
                    

class iot2_Activity(NamedElement):

    pass
class iot2_Contained(NamedElement):

    def __init__(self, repositoryId: str, version: str, absoluteName: str, 28: "iot2_Container" = None, 32: "iot2_Container" = None):
        self.repositoryId = repositoryId
        self.version = version
        self.absoluteName = absoluteName
        self.28 = 28
        self.32 = 32
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def absoluteName(self) -> str:
        return self.__absoluteName

    @absoluteName.setter
    def absoluteName(self, absoluteName: str):
        self.__absoluteName = absoluteName

    @property
    def repositoryId(self) -> str:
        return self.__repositoryId

    @repositoryId.setter
    def repositoryId(self, repositoryId: str):
        self.__repositoryId = repositoryId

    @property
    def 32(self):
        return self.__32

    @32.setter
    def 32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Contained__32", None)
        self.__32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "31"):
                opp_val = getattr(old_value, "31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "31"):
                opp_val = getattr(value, "31", None)
                if opp_val is None:
                    setattr(value, "31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 28(self):
        return self.__28

    @28.setter
    def 28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Contained__28", None)
        self.__28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "29"):
                opp_val = getattr(old_value, "29", None)
                if opp_val == self:
                    setattr(old_value, "29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "29"):
                opp_val = getattr(value, "29", None)
                setattr(value, "29", self)

class iot2_Block(Chunk):

    pass
class iot2_ExceptionDef(Contained):

    def __init__(self, typeCode: str, iot2_ExceptionDef: "iot2_OperationDef" = None, iot2_ExceptionDef37: set["iot2_Field"] = None):
        self.typeCode = typeCode
        self.iot2_ExceptionDef = iot2_ExceptionDef
        self.iot2_ExceptionDef37 = iot2_ExceptionDef37 if iot2_ExceptionDef37 is not None else set()
        
    @property
    def typeCode(self) -> str:
        return self.__typeCode

    @typeCode.setter
    def typeCode(self, typeCode: str):
        self.__typeCode = typeCode

    @property
    def iot2_ExceptionDef(self):
        return self.__iot2_ExceptionDef

    @iot2_ExceptionDef.setter
    def iot2_ExceptionDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ExceptionDef__iot2_ExceptionDef", None)
        self.__iot2_ExceptionDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_OperationDef24"):
                opp_val = getattr(old_value, "iot2_OperationDef24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_OperationDef24"):
                opp_val = getattr(value, "iot2_OperationDef24", None)
                if opp_val is None:
                    setattr(value, "iot2_OperationDef24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_ExceptionDef37(self):
        return self.__iot2_ExceptionDef37

    @iot2_ExceptionDef37.setter
    def iot2_ExceptionDef37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ExceptionDef__iot2_ExceptionDef37", None)
        self.__iot2_ExceptionDef37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_Field"):
                    opp_val = getattr(item, "iot2_Field", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_Field", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_Field"):
                    opp_val = getattr(item, "iot2_Field", None)
                    
                    setattr(item, "iot2_Field", self)
                    

class iot2_Sketch:

    pass
class iot2_Board:

    def __init__(self, name: str, type: str, iot2_Board: "iot2_System" = None, iot2_Board6: set["iot2_HWComponent"] = None):
        self.name = name
        self.type = type
        self.iot2_Board = iot2_Board
        self.iot2_Board6 = iot2_Board6 if iot2_Board6 is not None else set()
        
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
    def iot2_Board6(self):
        return self.__iot2_Board6

    @iot2_Board6.setter
    def iot2_Board6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Board__iot2_Board6", None)
        self.__iot2_Board6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_HWComponent7"):
                    opp_val = getattr(item, "iot2_HWComponent7", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_HWComponent7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_HWComponent7"):
                    opp_val = getattr(item, "iot2_HWComponent7", None)
                    
                    setattr(item, "iot2_HWComponent7", self)
                    

    @property
    def iot2_Board(self):
        return self.__iot2_Board

    @iot2_Board.setter
    def iot2_Board(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Board__iot2_Board", None)
        self.__iot2_Board = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_System2"):
                opp_val = getattr(old_value, "iot2_System2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_System2"):
                opp_val = getattr(value, "iot2_System2", None)
                if opp_val is None:
                    setattr(value, "iot2_System2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class iot2_HWComponent(ABC):

    def __init__(self, name: str, iot2_HWComponent: "iot2_System" = None, iot2_HWComponent7: "iot2_Board" = None, iot2_HWComponent11: set["iot2_OperationDef"] = None):
        self.name = name
        self.iot2_HWComponent = iot2_HWComponent
        self.iot2_HWComponent7 = iot2_HWComponent7
        self.iot2_HWComponent11 = iot2_HWComponent11 if iot2_HWComponent11 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iot2_HWComponent11(self):
        return self.__iot2_HWComponent11

    @iot2_HWComponent11.setter
    def iot2_HWComponent11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_HWComponent__iot2_HWComponent11", None)
        self.__iot2_HWComponent11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_OperationDef"):
                    opp_val = getattr(item, "iot2_OperationDef", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_OperationDef", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_OperationDef"):
                    opp_val = getattr(item, "iot2_OperationDef", None)
                    
                    setattr(item, "iot2_OperationDef", self)
                    

    @property
    def iot2_HWComponent(self):
        return self.__iot2_HWComponent

    @iot2_HWComponent.setter
    def iot2_HWComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_HWComponent__iot2_HWComponent", None)
        self.__iot2_HWComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_System"):
                opp_val = getattr(old_value, "iot2_System", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_System"):
                opp_val = getattr(value, "iot2_System", None)
                if opp_val is None:
                    setattr(value, "iot2_System", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_HWComponent7(self):
        return self.__iot2_HWComponent7

    @iot2_HWComponent7.setter
    def iot2_HWComponent7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_HWComponent__iot2_HWComponent7", None)
        self.__iot2_HWComponent7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Board6"):
                opp_val = getattr(old_value, "iot2_Board6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Board6"):
                opp_val = getattr(value, "iot2_Board6", None)
                if opp_val is None:
                    setattr(value, "iot2_Board6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class iot2_System:

    def __init__(self, name: str, iot2_System: set["iot2_HWComponent"] = None, iot2_System2: set["iot2_Board"] = None, iot2_System4: "iot2_Sketch" = None):
        self.name = name
        self.iot2_System = iot2_System if iot2_System is not None else set()
        self.iot2_System2 = iot2_System2 if iot2_System2 is not None else set()
        self.iot2_System4 = iot2_System4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iot2_System4(self):
        return self.__iot2_System4

    @iot2_System4.setter
    def iot2_System4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_System__iot2_System4", None)
        self.__iot2_System4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Sketch"):
                opp_val = getattr(old_value, "iot2_Sketch", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Sketch", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Sketch"):
                opp_val = getattr(value, "iot2_Sketch", None)
                setattr(value, "iot2_Sketch", self)

    @property
    def iot2_System(self):
        return self.__iot2_System

    @iot2_System.setter
    def iot2_System(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_System__iot2_System", None)
        self.__iot2_System = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_HWComponent"):
                    opp_val = getattr(item, "iot2_HWComponent", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_HWComponent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_HWComponent"):
                    opp_val = getattr(item, "iot2_HWComponent", None)
                    
                    setattr(item, "iot2_HWComponent", self)
                    

    @property
    def iot2_System2(self):
        return self.__iot2_System2

    @iot2_System2.setter
    def iot2_System2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_System__iot2_System2", None)
        self.__iot2_System2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_Board"):
                    opp_val = getattr(item, "iot2_Board", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_Board", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_Board"):
                    opp_val = getattr(item, "iot2_Board", None)
                    
                    setattr(item, "iot2_Board", self)
                    
