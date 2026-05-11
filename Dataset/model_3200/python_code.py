from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class BooleanBinaryOperator(Enum):
    AND = "AND"
    OR = "OR"
class BooleanUnaryOperator(Enum):
    NOT = "NOT"
class ParameterMode(Enum):
    PARAM_IN = "PARAM_IN"
    PARAM_OUT = "PARAM_OUT"
    PARAM_INOUT = "PARAM_INOUT"
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
    SMALLER_EQUALS = "SMALLER_EQUALS"
    EQUALS = "EQUALS"
    GREATER_EQUALS = "GREATER_EQUALS"
    GREATER = "GREATER"
    SMALLER = "SMALLER"
class IntegerCalculationOperator(Enum):
    ADD = "ADD"
    SUBRACT = "SUBRACT"
class BoardType(Enum):
    RaspberryPi = "RaspberryPi"
    Arduino = "Arduino"
    BeagleBoard = "BeagleBoard"


############################################
# Definition of Classes
############################################

class iot2_Trace:

    pass
class IntegerExpression:

    pass
class iot2_IntegerComparisonExpression(IntegerExpression):

    def __init__(self, operator: str, iot2_IntegerComparisonExpression: "iot2_BooleanVariable" = None):
        self.operator = operator
        self.iot2_IntegerComparisonExpression = iot2_IntegerComparisonExpression
        
        pass
    @property
    def operator(self):
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
            if hasattr(old_value, "iot2_BooleanVariable242"):
                opp_val = getattr(old_value, "iot2_BooleanVariable242", None)
                if opp_val == self:
                    setattr(old_value, "iot2_BooleanVariable242", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_BooleanVariable242"):
                opp_val = getattr(value, "iot2_BooleanVariable242", None)
                setattr(value, "iot2_BooleanVariable242", self)

class iot2_IntegerCalculationExpression(IntegerExpression):

    def __init__(self, operator: str, iot2_IntegerCalculationExpression: "iot2_IntegerVariable" = None):
        self.operator = operator
        self.iot2_IntegerCalculationExpression = iot2_IntegerCalculationExpression
        
        pass
    @property
    def operator(self):
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
            if hasattr(old_value, "iot2_IntegerVariable240"):
                opp_val = getattr(old_value, "iot2_IntegerVariable240", None)
                if opp_val == self:
                    setattr(old_value, "iot2_IntegerVariable240", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_IntegerVariable240"):
                opp_val = getattr(value, "iot2_IntegerVariable240", None)
                setattr(value, "iot2_IntegerVariable240", self)

class iot2_Token:

    pass
class iot2_Input:

    pass
class iot2_InputValue:

    pass
class BooleanExpression:

    pass
class iot2_BooleanBinaryExpression(BooleanExpression):

    def __init__(self, operator: str, iot2_BooleanBinaryExpression: "iot2_BooleanVariable" = None, iot2_BooleanBinaryExpression248: "iot2_BooleanVariable" = None):
        self.operator = operator
        self.iot2_BooleanBinaryExpression = iot2_BooleanBinaryExpression
        self.iot2_BooleanBinaryExpression248 = iot2_BooleanBinaryExpression248
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def iot2_BooleanBinaryExpression248(self):
        return self.__iot2_BooleanBinaryExpression248

    @iot2_BooleanBinaryExpression248.setter
    def iot2_BooleanBinaryExpression248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_BooleanBinaryExpression__iot2_BooleanBinaryExpression248", None)
        self.__iot2_BooleanBinaryExpression248 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_BooleanVariable249"):
                opp_val = getattr(old_value, "iot2_BooleanVariable249", None)
                if opp_val == self:
                    setattr(old_value, "iot2_BooleanVariable249", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_BooleanVariable249"):
                opp_val = getattr(value, "iot2_BooleanVariable249", None)
                setattr(value, "iot2_BooleanVariable249", self)

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
            if hasattr(old_value, "iot2_BooleanVariable246"):
                opp_val = getattr(old_value, "iot2_BooleanVariable246", None)
                if opp_val == self:
                    setattr(old_value, "iot2_BooleanVariable246", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_BooleanVariable246"):
                opp_val = getattr(value, "iot2_BooleanVariable246", None)
                setattr(value, "iot2_BooleanVariable246", self)

class iot2_BooleanUnaryExpression(BooleanExpression):

    def __init__(self, operator: str, iot2_BooleanUnaryExpression: "iot2_BooleanVariable" = None):
        self.operator = operator
        self.iot2_BooleanUnaryExpression = iot2_BooleanUnaryExpression
        
        pass
    @property
    def operator(self):
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
            if hasattr(old_value, "iot2_BooleanVariable244"):
                opp_val = getattr(old_value, "iot2_BooleanVariable244", None)
                if opp_val == self:
                    setattr(old_value, "iot2_BooleanVariable244", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_BooleanVariable244"):
                opp_val = getattr(value, "iot2_BooleanVariable244", None)
                setattr(value, "iot2_BooleanVariable244", self)

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
class iot2_ControlNode(ActivityNode):

    pass
class ActivityEdge:

    pass
class iot2_ControlFlow(ActivityEdge):

    pass
class Value:

    pass
class iot2_IntegerValue(Value):

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class iot2_BooleanValue(Value):

    def __init__(self, value: bool):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value


class Variable:

    pass
class iot2_BooleanVariable(Variable):

    pass
class iot2_IntegerVariable(Variable):

    pass
class iot2_Value:

    pass
class FinalNode:

    pass
class iot2_ActivityFinalNode(FinalNode):

    pass
class ControlNode:

    pass
class iot2_MergeNode(ControlNode):

    pass
class iot2_JoinNode(ControlNode):

    pass
class iot2_FinalNode(ControlNode):

    pass
class iot2_ForkNode(ControlNode):

    pass
class iot2_DecisionNode(ControlNode):

    pass
class iot2_InitialNode(ControlNode):

    pass
class Expression:

    pass
class iot2_Expression_Negate(Expression):

    pass
class iot2_Expression_Number(Expression):

    def __init__(self, value: float):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value


class iot2_Expression_Multiplication(Expression):

    pass
class iot2_Expression_Plus(Expression):

    pass
class iot2_Expression_CallMemberFunction(Expression):

    def __init__(self, memberFunctionName: str, iot2_Expression_CallMemberFunction: "iot2_Expression" = None, iot2_Expression_CallMemberFunction200: "iot2_Functioncall_Arguments" = None):
        self.memberFunctionName = memberFunctionName
        self.iot2_Expression_CallMemberFunction = iot2_Expression_CallMemberFunction
        self.iot2_Expression_CallMemberFunction200 = iot2_Expression_CallMemberFunction200
        
        pass
    @property
    def memberFunctionName(self):
        return self.__memberFunctionName

    @memberFunctionName.setter
    def memberFunctionName(self, memberFunctionName: str):
        self.__memberFunctionName = memberFunctionName


    @property
    def iot2_Expression_CallMemberFunction200(self):
        return self.__iot2_Expression_CallMemberFunction200

    @iot2_Expression_CallMemberFunction200.setter
    def iot2_Expression_CallMemberFunction200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_CallMemberFunction__iot2_Expression_CallMemberFunction200", None)
        self.__iot2_Expression_CallMemberFunction200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Functioncall_Arguments201"):
                opp_val = getattr(old_value, "iot2_Functioncall_Arguments201", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Functioncall_Arguments201", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Functioncall_Arguments201"):
                opp_val = getattr(value, "iot2_Functioncall_Arguments201", None)
                setattr(value, "iot2_Functioncall_Arguments201", self)

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
            if hasattr(old_value, "iot2_Expression198"):
                opp_val = getattr(old_value, "iot2_Expression198", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression198", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression198"):
                opp_val = getattr(value, "iot2_Expression198", None)
                setattr(value, "iot2_Expression198", self)

class iot2_Expression_AccessArray(Expression):

    pass
class iot2_Expression_Equal(Expression):

    pass
class iot2_IntegerExpression(Expression):

    pass
class iot2_Expression_Function(Expression):

    pass
class iot2_Expression_True(Expression):

    pass
class iot2_Expression_Invert(Expression):

    pass
class iot2_Expression_Minus(Expression):

    pass
class iot2_Expression_And(Expression):

    pass
class iot2_Expression_Concatenation(Expression):

    pass
class iot2_Expression_Modulo(Expression):

    pass
class iot2_Expression_String(Expression):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class iot2_Expression_CallFunction(Expression):

    pass
class iot2_Expression_Division(Expression):

    pass
class iot2_Expression_VarArgs(Expression):

    pass
class iot2_Expression_False(Expression):

    pass
class iot2_Expression_Larger_Equal(Expression):

    pass
class iot2_Expression_Larger(Expression):

    pass
class iot2_Expression_Not_Equal(Expression):

    pass
class iot2_Expression_Length(Expression):

    pass
class iot2_Expression_AccessMember(Expression):

    def __init__(self, memberName: str, iot2_Expression_AccessMember: "iot2_Expression" = None):
        self.memberName = memberName
        self.iot2_Expression_AccessMember = iot2_Expression_AccessMember
        
        pass
    @property
    def memberName(self):
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
            if hasattr(old_value, "iot2_Expression213"):
                opp_val = getattr(old_value, "iot2_Expression213", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression213", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression213"):
                opp_val = getattr(value, "iot2_Expression213", None)
                setattr(value, "iot2_Expression213", self)

class iot2_Expression_VariableName(Expression):

    def __init__(self, variable: str):
        self.variable = variable
        
        pass
    @property
    def variable(self):
        return self.__variable

    @variable.setter
    def variable(self, variable: str):
        self.__variable = variable


class iot2_Expression_Exponentiation(Expression):

    pass
class iot2_Expression_Smaller(Expression):

    pass
class iot2_Expression_Or(Expression):

    pass
class iot2_BooleanExpression(Expression):

    pass
class iot2_Expression_Smaller_Equal(Expression):

    pass
class iot2_Expression_Nil(Expression):

    pass
class Statement_FunctioncallOrAssignment:

    pass
class iot2_Statement_CallMemberFunction(Statement_FunctioncallOrAssignment):

    def __init__(self, memberFunctionName: str, iot2_Statement_CallMemberFunction: "iot2_Expression" = None, iot2_Statement_CallMemberFunction109: "iot2_Functioncall_Arguments" = None):
        self.memberFunctionName = memberFunctionName
        self.iot2_Statement_CallMemberFunction = iot2_Statement_CallMemberFunction
        self.iot2_Statement_CallMemberFunction109 = iot2_Statement_CallMemberFunction109
        
        pass
    @property
    def memberFunctionName(self):
        return self.__memberFunctionName

    @memberFunctionName.setter
    def memberFunctionName(self, memberFunctionName: str):
        self.__memberFunctionName = memberFunctionName


    @property
    def iot2_Statement_CallMemberFunction109(self):
        return self.__iot2_Statement_CallMemberFunction109

    @iot2_Statement_CallMemberFunction109.setter
    def iot2_Statement_CallMemberFunction109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_CallMemberFunction__iot2_Statement_CallMemberFunction109", None)
        self.__iot2_Statement_CallMemberFunction109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Functioncall_Arguments110"):
                opp_val = getattr(old_value, "iot2_Functioncall_Arguments110", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Functioncall_Arguments110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Functioncall_Arguments110"):
                opp_val = getattr(value, "iot2_Functioncall_Arguments110", None)
                setattr(value, "iot2_Functioncall_Arguments110", self)

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
            if hasattr(old_value, "iot2_Expression107"):
                opp_val = getattr(old_value, "iot2_Expression107", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression107"):
                opp_val = getattr(value, "iot2_Expression107", None)
                setattr(value, "iot2_Expression107", self)

class iot2_Statement_CallFunction(Statement_FunctioncallOrAssignment):

    pass
class iot2_Statement_Assignment(Statement_FunctioncallOrAssignment):

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
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


class iot2_Field_AddEntryToTable_Brackets(Field):

    pass
class iot2_Functioncall_Arguments:

    pass
class iot2_Expression_TableConstructor(Expression):

    pass
class iot2_Statement_If_Then_Else_ElseIfPart:

    pass
class iot2_Function:

    def __init__(self, parameters: str, varArgs: bool, iot2_Function85: "iot2_Statement_LocalFunction_Declaration" = None, iot2_Function: "iot2_Statement_GlobalFunction_Declaration" = None, iot2_Function89: "iot2_Expression_Function" = None, iot2_Function93: "iot2_Block" = None):
        self.parameters = parameters
        self.varArgs = varArgs
        self.iot2_Function85 = iot2_Function85
        self.iot2_Function = iot2_Function
        self.iot2_Function89 = iot2_Function89
        self.iot2_Function93 = iot2_Function93
        
        pass
    @property
    def varArgs(self):
        return self.__varArgs

    @varArgs.setter
    def varArgs(self, varArgs: bool):
        self.__varArgs = varArgs


    @property
    def parameters(self):
        return self.__parameters

    @parameters.setter
    def parameters(self, parameters: str):
        self.__parameters = parameters


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
    def iot2_Function85(self):
        return self.__iot2_Function85

    @iot2_Function85.setter
    def iot2_Function85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Function__iot2_Function85", None)
        self.__iot2_Function85 = value
        
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
    def iot2_Function89(self):
        return self.__iot2_Function89

    @iot2_Function89.setter
    def iot2_Function89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Function__iot2_Function89", None)
        self.__iot2_Function89 = value
        
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

    @property
    def iot2_Function93(self):
        return self.__iot2_Function93

    @iot2_Function93.setter
    def iot2_Function93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Function__iot2_Function93", None)
        self.__iot2_Function93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Block94"):
                opp_val = getattr(old_value, "iot2_Block94", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Block94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Block94"):
                opp_val = getattr(value, "iot2_Block94", None)
                setattr(value, "iot2_Block94", self)

class iot2_Expression(Statement_FunctioncallOrAssignment):

    pass
class IDLType:

    pass
class Statement:

    pass
class iot2_Statement_If_Then_Else(Statement):

    pass
class iot2_Statement_While(Statement):

    pass
class iot2_Statement_Repeat(Statement):

    pass
class iot2_Statement_GlobalFunction_Declaration(Statement):

    def __init__(self, prefix: str, functionName: str, iot2_Statement_GlobalFunction_Declaration: "iot2_Function" = None):
        self.prefix = prefix
        self.functionName = functionName
        self.iot2_Statement_GlobalFunction_Declaration = iot2_Statement_GlobalFunction_Declaration
        
        pass
    @property
    def prefix(self):
        return self.__prefix

    @prefix.setter
    def prefix(self, prefix: str):
        self.__prefix = prefix


    @property
    def functionName(self):
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

class iot2_Statement_Local_Variable_Declaration(Statement):

    def __init__(self, variableNames: str, iot2_Statement_Local_Variable_Declaration: set["iot2_Expression"] = None):
        self.variableNames = variableNames
        self.iot2_Statement_Local_Variable_Declaration = iot2_Statement_Local_Variable_Declaration if iot2_Statement_Local_Variable_Declaration is not None else set()
        
        pass
    @property
    def variableNames(self):
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
                if hasattr(item, "iot2_Expression87"):
                    opp_val = getattr(item, "iot2_Expression87", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_Expression87", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_Expression87"):
                    opp_val = getattr(item, "iot2_Expression87", None)
                    
                    setattr(item, "iot2_Expression87", self)
                    

class iot2_Statement_FunctioncallOrAssignment(Statement):

    pass
class iot2_Statement_For_Generic(Statement):

    def __init__(self, names: str, iot2_Statement_For_Generic: set["iot2_Expression"] = None, iot2_Statement_For_Generic81: "iot2_Block" = None):
        self.names = names
        self.iot2_Statement_For_Generic = iot2_Statement_For_Generic if iot2_Statement_For_Generic is not None else set()
        self.iot2_Statement_For_Generic81 = iot2_Statement_For_Generic81
        
        pass
    @property
    def names(self):
        return self.__names

    @names.setter
    def names(self, names: str):
        self.__names = names


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
                if hasattr(item, "iot2_Expression79"):
                    opp_val = getattr(item, "iot2_Expression79", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_Expression79", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_Expression79"):
                    opp_val = getattr(item, "iot2_Expression79", None)
                    
                    setattr(item, "iot2_Expression79", self)
                    

    @property
    def iot2_Statement_For_Generic81(self):
        return self.__iot2_Statement_For_Generic81

    @iot2_Statement_For_Generic81.setter
    def iot2_Statement_For_Generic81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_For_Generic__iot2_Statement_For_Generic81", None)
        self.__iot2_Statement_For_Generic81 = value
        
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

class iot2_Statement_For_Numeric(Statement):

    def __init__(self, iteratorName: str, iot2_Statement_For_Numeric: "iot2_Expression" = None, iot2_Statement_For_Numeric70: "iot2_Expression" = None, iot2_Statement_For_Numeric73: "iot2_Expression" = None, iot2_Statement_For_Numeric76: "iot2_Block" = None):
        self.iteratorName = iteratorName
        self.iot2_Statement_For_Numeric = iot2_Statement_For_Numeric
        self.iot2_Statement_For_Numeric70 = iot2_Statement_For_Numeric70
        self.iot2_Statement_For_Numeric73 = iot2_Statement_For_Numeric73
        self.iot2_Statement_For_Numeric76 = iot2_Statement_For_Numeric76
        
        pass
    @property
    def iteratorName(self):
        return self.__iteratorName

    @iteratorName.setter
    def iteratorName(self, iteratorName: str):
        self.__iteratorName = iteratorName


    @property
    def iot2_Statement_For_Numeric70(self):
        return self.__iot2_Statement_For_Numeric70

    @iot2_Statement_For_Numeric70.setter
    def iot2_Statement_For_Numeric70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_For_Numeric__iot2_Statement_For_Numeric70", None)
        self.__iot2_Statement_For_Numeric70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression71"):
                opp_val = getattr(old_value, "iot2_Expression71", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression71"):
                opp_val = getattr(value, "iot2_Expression71", None)
                setattr(value, "iot2_Expression71", self)

    @property
    def iot2_Statement_For_Numeric76(self):
        return self.__iot2_Statement_For_Numeric76

    @iot2_Statement_For_Numeric76.setter
    def iot2_Statement_For_Numeric76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_For_Numeric__iot2_Statement_For_Numeric76", None)
        self.__iot2_Statement_For_Numeric76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Block77"):
                opp_val = getattr(old_value, "iot2_Block77", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Block77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Block77"):
                opp_val = getattr(value, "iot2_Block77", None)
                setattr(value, "iot2_Block77", self)

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
            if hasattr(old_value, "iot2_Expression68"):
                opp_val = getattr(old_value, "iot2_Expression68", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression68"):
                opp_val = getattr(value, "iot2_Expression68", None)
                setattr(value, "iot2_Expression68", self)

    @property
    def iot2_Statement_For_Numeric73(self):
        return self.__iot2_Statement_For_Numeric73

    @iot2_Statement_For_Numeric73.setter
    def iot2_Statement_For_Numeric73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_For_Numeric__iot2_Statement_For_Numeric73", None)
        self.__iot2_Statement_For_Numeric73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression74"):
                opp_val = getattr(old_value, "iot2_Expression74", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression74"):
                opp_val = getattr(value, "iot2_Expression74", None)
                setattr(value, "iot2_Expression74", self)

class iot2_Statement_LocalFunction_Declaration(Statement):

    def __init__(self, functionName: str, iot2_Statement_LocalFunction_Declaration: "iot2_Function" = None):
        self.functionName = functionName
        self.iot2_Statement_LocalFunction_Declaration = iot2_Statement_LocalFunction_Declaration
        
        pass
    @property
    def functionName(self):
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
            if hasattr(old_value, "iot2_Function85"):
                opp_val = getattr(old_value, "iot2_Function85", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Function85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Function85"):
                opp_val = getattr(value, "iot2_Function85", None)
                setattr(value, "iot2_Function85", self)

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
class iot2_PrimitiveDef(IDLType):

    def __init__(self, kind: str):
        self.kind = kind
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


class Typed:

    pass
class iot2_Field(Typed):

    def __init__(self, identifier: str, iot2_Field: "iot2_ExceptionDef" = None, iot2_Field34: "iot2_Expression" = None, iot2_Field91: "iot2_Expression_TableConstructor" = None):
        self.identifier = identifier
        self.iot2_Field = iot2_Field
        self.iot2_Field34 = iot2_Field34
        self.iot2_Field91 = iot2_Field91
        
        pass
    @property
    def identifier(self):
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier


    @property
    def iot2_Field34(self):
        return self.__iot2_Field34

    @iot2_Field34.setter
    def iot2_Field34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Field__iot2_Field34", None)
        self.__iot2_Field34 = value
        
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
            if hasattr(old_value, "iot2_ExceptionDef32"):
                opp_val = getattr(old_value, "iot2_ExceptionDef32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_ExceptionDef32"):
                opp_val = getattr(value, "iot2_ExceptionDef32", None)
                if opp_val is None:
                    setattr(value, "iot2_ExceptionDef32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_Field91(self):
        return self.__iot2_Field91

    @iot2_Field91.setter
    def iot2_Field91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Field__iot2_Field91", None)
        self.__iot2_Field91 = value
        
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

class iot2_ParameterDef(Typed):

    def __init__(self, identifier: str, direction: str, iot2_ParameterDef: "iot2_OperationDef" = None):
        self.identifier = identifier
        self.direction = direction
        self.iot2_ParameterDef = iot2_ParameterDef
        
        pass
    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction


    @property
    def identifier(self):
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier


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
            if hasattr(old_value, "iot2_OperationDef21"):
                opp_val = getattr(old_value, "iot2_OperationDef21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_OperationDef21"):
                opp_val = getattr(value, "iot2_OperationDef21", None)
                if opp_val is None:
                    setattr(value, "iot2_OperationDef21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Contained:

    pass
class iot2_Variable:

    def __init__(self, name: str, iot2_Variable: "iot2_Activity" = None, iot2_Variable19: "iot2_Activity" = None, iot2_Variable254: "iot2_InputValue" = None, iot2_Variable229: "iot2_Value" = None, iot2_Variable231: "iot2_Value" = None):
        self.name = name
        self.iot2_Variable = iot2_Variable
        self.iot2_Variable19 = iot2_Variable19
        self.iot2_Variable254 = iot2_Variable254
        self.iot2_Variable229 = iot2_Variable229
        self.iot2_Variable231 = iot2_Variable231
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def iot2_Variable229(self):
        return self.__iot2_Variable229

    @iot2_Variable229.setter
    def iot2_Variable229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Variable__iot2_Variable229", None)
        self.__iot2_Variable229 = value
        
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
            if hasattr(old_value, "iot2_Activity16"):
                opp_val = getattr(old_value, "iot2_Activity16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Activity16"):
                opp_val = getattr(value, "iot2_Activity16", None)
                if opp_val is None:
                    setattr(value, "iot2_Activity16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_Variable254(self):
        return self.__iot2_Variable254

    @iot2_Variable254.setter
    def iot2_Variable254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Variable__iot2_Variable254", None)
        self.__iot2_Variable254 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_InputValue253"):
                opp_val = getattr(old_value, "iot2_InputValue253", None)
                if opp_val == self:
                    setattr(old_value, "iot2_InputValue253", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_InputValue253"):
                opp_val = getattr(value, "iot2_InputValue253", None)
                setattr(value, "iot2_InputValue253", self)

    @property
    def iot2_Variable19(self):
        return self.__iot2_Variable19

    @iot2_Variable19.setter
    def iot2_Variable19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Variable__iot2_Variable19", None)
        self.__iot2_Variable19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Activity18"):
                opp_val = getattr(old_value, "iot2_Activity18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Activity18"):
                opp_val = getattr(value, "iot2_Activity18", None)
                if opp_val is None:
                    setattr(value, "iot2_Activity18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_Variable231(self):
        return self.__iot2_Variable231

    @iot2_Variable231.setter
    def iot2_Variable231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Variable__iot2_Variable231", None)
        self.__iot2_Variable231 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Value232"):
                opp_val = getattr(old_value, "iot2_Value232", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Value232", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Value232"):
                opp_val = getattr(value, "iot2_Value232", None)
                setattr(value, "iot2_Value232", self)

class NamedElement:

    pass
class iot2_ActivityNode(NamedElement):

    def __init__(self, running: bool, ActivityNode: "iot2_Activity" = None, iot2_ActivityNode: "iot2_Token" = None, iot2_ActivityNode259: "iot2_Trace" = None, source: set["iot2_ActivityEdge"] = None, target: set["iot2_ActivityEdge"] = None, nodes: "iot2_Activity" = None, ActivityNode219: "iot2_ActivityEdge" = None, ActivityNode221: "iot2_ActivityEdge" = None):
        self.running = running
        self.ActivityNode = ActivityNode
        self.iot2_ActivityNode = iot2_ActivityNode
        self.iot2_ActivityNode259 = iot2_ActivityNode259
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.nodes = nodes
        self.ActivityNode219 = ActivityNode219
        self.ActivityNode221 = ActivityNode221
        
        pass
    @property
    def running(self):
        return self.__running

    @running.setter
    def running(self, running: bool):
        self.__running = running


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
    def ActivityNode221(self):
        return self.__ActivityNode221

    @ActivityNode221.setter
    def ActivityNode221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityNode__ActivityNode221", None)
        self.__ActivityNode221 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incoming"):
                opp_val = getattr(old_value, "incoming", None)
                if opp_val == self:
                    setattr(old_value, "incoming", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incoming"):
                opp_val = getattr(value, "incoming", None)
                setattr(value, "incoming", self)

    @property
    def iot2_ActivityNode259(self):
        return self.__iot2_ActivityNode259

    @iot2_ActivityNode259.setter
    def iot2_ActivityNode259(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityNode__iot2_ActivityNode259", None)
        self.__iot2_ActivityNode259 = value
        
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
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityNode__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityEdge216"):
                    opp_val = getattr(item, "ActivityEdge216", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityEdge216", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityEdge216"):
                    opp_val = getattr(item, "ActivityEdge216", None)
                    
                    setattr(item, "ActivityEdge216", self)
                    

    @property
    def ActivityNode219(self):
        return self.__ActivityNode219

    @ActivityNode219.setter
    def ActivityNode219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityNode__ActivityNode219", None)
        self.__ActivityNode219 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoing"):
                opp_val = getattr(old_value, "outgoing", None)
                if opp_val == self:
                    setattr(old_value, "outgoing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoing"):
                opp_val = getattr(value, "outgoing", None)
                setattr(value, "outgoing", self)

    @property
    def nodes(self):
        return self.__nodes

    @nodes.setter
    def nodes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityNode__nodes", None)
        self.__nodes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Activity"):
                opp_val = getattr(old_value, "Activity", None)
                if opp_val == self:
                    setattr(old_value, "Activity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Activity"):
                opp_val = getattr(value, "Activity", None)
                setattr(value, "Activity", self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityNode__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityEdge"):
                    opp_val = getattr(item, "ActivityEdge", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityEdge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityEdge"):
                    opp_val = getattr(item, "ActivityEdge", None)
                    
                    setattr(item, "ActivityEdge", self)
                    

    @property
    def ActivityNode(self):
        return self.__ActivityNode

    @ActivityNode.setter
    def ActivityNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityNode__ActivityNode", None)
        self.__ActivityNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activity"):
                opp_val = getattr(old_value, "activity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activity"):
                opp_val = getattr(value, "activity", None)
                if opp_val is None:
                    setattr(value, "activity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class iot2_ActivityEdge(NamedElement):

    pass
class iot2_TypedefDef(Contained, IDLType):

    pass
class iot2_IDLType(ABC):

    def __init__(self, typeCode: str, iot2_IDLType: "iot2_Typed" = None):
        self.typeCode = typeCode
        self.iot2_IDLType = iot2_IDLType
        
        pass
    @property
    def typeCode(self):
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
        
        pass
    @property
    def identifier(self):
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class iot2_Container(Contained):

    pass
class iot2_Contained(NamedElement):

    def __init__(self, repositoryId: str, version: str, absoluteName: str, contains: "iot2_Container" = None, Contained: "iot2_Container" = None):
        self.repositoryId = repositoryId
        self.version = version
        self.absoluteName = absoluteName
        self.contains = contains
        self.Contained = Contained
        
        pass
    @property
    def absoluteName(self):
        return self.__absoluteName

    @absoluteName.setter
    def absoluteName(self, absoluteName: str):
        self.__absoluteName = absoluteName


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def repositoryId(self):
        return self.__repositoryId

    @repositoryId.setter
    def repositoryId(self, repositoryId: str):
        self.__repositoryId = repositoryId


    @property
    def contains(self):
        return self.__contains

    @contains.setter
    def contains(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Contained__contains", None)
        self.__contains = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Container"):
                opp_val = getattr(old_value, "Container", None)
                if opp_val == self:
                    setattr(old_value, "Container", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Container"):
                opp_val = getattr(value, "Container", None)
                setattr(value, "Container", self)

    @property
    def Contained(self):
        return self.__Contained

    @Contained.setter
    def Contained(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Contained__Contained", None)
        self.__Contained = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "definedIn"):
                opp_val = getattr(old_value, "definedIn", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "definedIn"):
                opp_val = getattr(value, "definedIn", None)
                if opp_val is None:
                    setattr(value, "definedIn", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class iot2_Block(Chunk):

    pass
class iot2_ExceptionDef(Contained):

    def __init__(self, typeCode: str, iot2_ExceptionDef: "iot2_OperationDef" = None, iot2_ExceptionDef32: set["iot2_Field"] = None):
        self.typeCode = typeCode
        self.iot2_ExceptionDef = iot2_ExceptionDef
        self.iot2_ExceptionDef32 = iot2_ExceptionDef32 if iot2_ExceptionDef32 is not None else set()
        
        pass
    @property
    def typeCode(self):
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
            if hasattr(old_value, "iot2_OperationDef23"):
                opp_val = getattr(old_value, "iot2_OperationDef23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_OperationDef23"):
                opp_val = getattr(value, "iot2_OperationDef23", None)
                if opp_val is None:
                    setattr(value, "iot2_OperationDef23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_ExceptionDef32(self):
        return self.__iot2_ExceptionDef32

    @iot2_ExceptionDef32.setter
    def iot2_ExceptionDef32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ExceptionDef__iot2_ExceptionDef32", None)
        self.__iot2_ExceptionDef32 = value if value is not None else set()
        
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
                    

class HWComponent:

    pass
class iot2_Actuator(HWComponent):

    pass
class iot2_Sensor(HWComponent):

    pass
class iot2_OperationDef(Contained, Typed):

    def __init__(self, isOneway: bool, contexts: str, iot2_OperationDef: "iot2_HWComponent" = None, iot2_OperationDef23: set["iot2_ExceptionDef"] = None, iot2_OperationDef25: "iot2_Block" = None, iot2_OperationDef21: set["iot2_ParameterDef"] = None, iot2_OperationDef227: "iot2_OpaqueAction" = None):
        self.isOneway = isOneway
        self.contexts = contexts
        self.iot2_OperationDef = iot2_OperationDef
        self.iot2_OperationDef23 = iot2_OperationDef23 if iot2_OperationDef23 is not None else set()
        self.iot2_OperationDef25 = iot2_OperationDef25
        self.iot2_OperationDef21 = iot2_OperationDef21 if iot2_OperationDef21 is not None else set()
        self.iot2_OperationDef227 = iot2_OperationDef227
        
        pass
    @property
    def contexts(self):
        return self.__contexts

    @contexts.setter
    def contexts(self, contexts: str):
        self.__contexts = contexts


    @property
    def isOneway(self):
        return self.__isOneway

    @isOneway.setter
    def isOneway(self, isOneway: bool):
        self.__isOneway = isOneway


    @property
    def iot2_OperationDef23(self):
        return self.__iot2_OperationDef23

    @iot2_OperationDef23.setter
    def iot2_OperationDef23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_OperationDef__iot2_OperationDef23", None)
        self.__iot2_OperationDef23 = value if value is not None else set()
        
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
    def iot2_OperationDef25(self):
        return self.__iot2_OperationDef25

    @iot2_OperationDef25.setter
    def iot2_OperationDef25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_OperationDef__iot2_OperationDef25", None)
        self.__iot2_OperationDef25 = value
        
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
    def iot2_OperationDef227(self):
        return self.__iot2_OperationDef227

    @iot2_OperationDef227.setter
    def iot2_OperationDef227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_OperationDef__iot2_OperationDef227", None)
        self.__iot2_OperationDef227 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_OpaqueAction226"):
                opp_val = getattr(old_value, "iot2_OpaqueAction226", None)
                if opp_val == self:
                    setattr(old_value, "iot2_OpaqueAction226", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_OpaqueAction226"):
                opp_val = getattr(value, "iot2_OpaqueAction226", None)
                setattr(value, "iot2_OpaqueAction226", self)

    @property
    def iot2_OperationDef21(self):
        return self.__iot2_OperationDef21

    @iot2_OperationDef21.setter
    def iot2_OperationDef21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_OperationDef__iot2_OperationDef21", None)
        self.__iot2_OperationDef21 = value if value is not None else set()
        
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
                    

class iot2_Activity(NamedElement):

    pass
class iot2_Sketch:

    pass
class iot2_Board:

    def __init__(self, name: str, type: str, iot2_Board: "iot2_System" = None, iot2_Board6: set["iot2_HWComponent"] = None):
        self.name = name
        self.type = type
        self.iot2_Board = iot2_Board
        self.iot2_Board6 = iot2_Board6 if iot2_Board6 is not None else set()
        
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
                    

class iot2_HWComponent(ABC):

    def __init__(self, name: str, iot2_HWComponent: "iot2_System" = None, iot2_HWComponent7: "iot2_Board" = None, iot2_HWComponent11: set["iot2_OperationDef"] = None):
        self.name = name
        self.iot2_HWComponent = iot2_HWComponent
        self.iot2_HWComponent7 = iot2_HWComponent7
        self.iot2_HWComponent11 = iot2_HWComponent11 if iot2_HWComponent11 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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

class iot2_System:

    def __init__(self, name: str, iot2_System: set["iot2_HWComponent"] = None, iot2_System2: set["iot2_Board"] = None, iot2_System4: "iot2_Sketch" = None):
        self.name = name
        self.iot2_System = iot2_System if iot2_System is not None else set()
        self.iot2_System2 = iot2_System2 if iot2_System2 is not None else set()
        self.iot2_System4 = iot2_System4
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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
