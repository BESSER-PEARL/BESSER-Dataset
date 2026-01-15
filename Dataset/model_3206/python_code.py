from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class TypeEnum(Enum):
    Integer = "Integer"
    IntegerArray = "IntegerArray"
class BinaryOperatorEnum(Enum):
    bitand = "bitand"
    bitor = "bitor"
    plus = "plus"
    minus = "minus"
    times = "times"
    div = "div"
    mod = "mod"
    equal = "equal"
    notequal = "notequal"
    less = "less"
    greater = "greater"
    leq = "leq"
    geq = "geq"
    and = "and"
    or = "or"
class AssignmentStatementEnum(Enum):
    assign = "assign"


############################################
# Definition of Classes
############################################

class CallStatement:

    pass
class NQC_FunctionCall(CallStatement):

    pass
class NQC_SubroutineCall(CallStatement):

    pass
class ConstantExpression:

    pass
class NQC_BooleanConstant(ConstantExpression):

    def __init__(self, Value: bool):
        self.Value = Value
        
    @property
    def Value(self) -> bool:
        return self.__Value

    @Value.setter
    def Value(self, Value: bool):
        self.__Value = Value

class VariableExpression:

    pass
class NQC_ArrayExpression(VariableExpression):

    pass
class ValueExpression:

    pass
class Expression:

    pass
class NQC_ValueExpression(Expression):

    pass
class CompoundExpression:

    pass
class NQC_BinaryExpression(CompoundExpression):

    def __init__(self, Operator: str, NQC_BinaryExpression: "NQC_Expression" = None, NQC_BinaryExpression98: "NQC_Expression" = None):
        self.Operator = Operator
        self.NQC_BinaryExpression = NQC_BinaryExpression
        self.NQC_BinaryExpression98 = NQC_BinaryExpression98
        
    @property
    def Operator(self) -> str:
        return self.__Operator

    @Operator.setter
    def Operator(self, Operator: str):
        self.__Operator = Operator

    @property
    def NQC_BinaryExpression(self):
        return self.__NQC_BinaryExpression

    @NQC_BinaryExpression.setter
    def NQC_BinaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NQC_BinaryExpression__NQC_BinaryExpression", None)
        self.__NQC_BinaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NQC_Expression96"):
                opp_val = getattr(old_value, "NQC_Expression96", None)
                if opp_val == self:
                    setattr(old_value, "NQC_Expression96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NQC_Expression96"):
                opp_val = getattr(value, "NQC_Expression96", None)
                setattr(value, "NQC_Expression96", self)

    @property
    def NQC_BinaryExpression98(self):
        return self.__NQC_BinaryExpression98

    @NQC_BinaryExpression98.setter
    def NQC_BinaryExpression98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NQC_BinaryExpression__NQC_BinaryExpression98", None)
        self.__NQC_BinaryExpression98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NQC_Expression99"):
                opp_val = getattr(old_value, "NQC_Expression99", None)
                if opp_val == self:
                    setattr(old_value, "NQC_Expression99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NQC_Expression99"):
                opp_val = getattr(value, "NQC_Expression99", None)
                setattr(value, "NQC_Expression99", self)

class NQC_CompoundExpression(Expression):

    pass
class NQC_Case:

    def __init__(self, IsDefault: bool, NQC_Case: "NQC_SwitchStatement" = None, NQC_Case85: set["NQC_ConstantExpression"] = None, NQC_Case88: set["NQC_Statement"] = None):
        self.IsDefault = IsDefault
        self.NQC_Case = NQC_Case
        self.NQC_Case85 = NQC_Case85 if NQC_Case85 is not None else set()
        self.NQC_Case88 = NQC_Case88 if NQC_Case88 is not None else set()
        
    @property
    def IsDefault(self) -> bool:
        return self.__IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault: bool):
        self.__IsDefault = IsDefault

    @property
    def NQC_Case85(self):
        return self.__NQC_Case85

    @NQC_Case85.setter
    def NQC_Case85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NQC_Case__NQC_Case85", None)
        self.__NQC_Case85 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NQC_ConstantExpression86"):
                    opp_val = getattr(item, "NQC_ConstantExpression86", None)
                    
                    if opp_val == self:
                        setattr(item, "NQC_ConstantExpression86", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NQC_ConstantExpression86"):
                    opp_val = getattr(item, "NQC_ConstantExpression86", None)
                    
                    setattr(item, "NQC_ConstantExpression86", self)
                    

    @property
    def NQC_Case88(self):
        return self.__NQC_Case88

    @NQC_Case88.setter
    def NQC_Case88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NQC_Case__NQC_Case88", None)
        self.__NQC_Case88 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NQC_Statement89"):
                    opp_val = getattr(item, "NQC_Statement89", None)
                    
                    if opp_val == self:
                        setattr(item, "NQC_Statement89", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NQC_Statement89"):
                    opp_val = getattr(item, "NQC_Statement89", None)
                    
                    setattr(item, "NQC_Statement89", self)
                    

    @property
    def NQC_Case(self):
        return self.__NQC_Case

    @NQC_Case.setter
    def NQC_Case(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NQC_Case__NQC_Case", None)
        self.__NQC_Case = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NQC_SwitchStatement73"):
                opp_val = getattr(old_value, "NQC_SwitchStatement73", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NQC_SwitchStatement73"):
                opp_val = getattr(value, "NQC_SwitchStatement73", None)
                if opp_val is None:
                    setattr(value, "NQC_SwitchStatement73", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ControlStructure:

    pass
class NQC_ForStatement(ControlStructure):

    pass
class NQC_RepeatStatement(ControlStructure):

    pass
class NQC_UntilStatement(ControlStructure):

    pass
class NQC_WhileStatement(ControlStructure):

    pass
class NQC_SwitchStatement(ControlStructure):

    pass
class NQC_DoWhileStatement(ControlStructure):

    pass
class NQC_IfStatement(ControlStructure):

    pass
class NQC_GoToStatement(ControlStructure):

    pass
class NQC_VariableExpression(ValueExpression):

    pass
class Statement:

    pass
class NQC_CallStatement(Statement):

    pass
class NQC_ControlStructure(Statement):

    pass
class NQC_StopStatement(Statement):

    pass
class NQC_StartStatement(Statement):

    pass
class NQC_ReturnStatement(Statement):

    pass
class NQC_EmptyStatement(Statement):

    pass
class NQC_ContinueStatement(Statement):

    pass
class NQC_BreakStatement(Statement):

    pass
class NQC_AssignmentStatement(Statement):

    def __init__(self, Operator: str, NQC_AssignmentStatement: "NQC_VariableExpression" = None, NQC_AssignmentStatement32: "NQC_Expression" = None):
        self.Operator = Operator
        self.NQC_AssignmentStatement = NQC_AssignmentStatement
        self.NQC_AssignmentStatement32 = NQC_AssignmentStatement32
        
    @property
    def Operator(self) -> str:
        return self.__Operator

    @Operator.setter
    def Operator(self, Operator: str):
        self.__Operator = Operator

    @property
    def NQC_AssignmentStatement32(self):
        return self.__NQC_AssignmentStatement32

    @NQC_AssignmentStatement32.setter
    def NQC_AssignmentStatement32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NQC_AssignmentStatement__NQC_AssignmentStatement32", None)
        self.__NQC_AssignmentStatement32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NQC_Expression"):
                opp_val = getattr(old_value, "NQC_Expression", None)
                if opp_val == self:
                    setattr(old_value, "NQC_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NQC_Expression"):
                opp_val = getattr(value, "NQC_Expression", None)
                setattr(value, "NQC_Expression", self)

    @property
    def NQC_AssignmentStatement(self):
        return self.__NQC_AssignmentStatement

    @NQC_AssignmentStatement.setter
    def NQC_AssignmentStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NQC_AssignmentStatement__NQC_AssignmentStatement", None)
        self.__NQC_AssignmentStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NQC_VariableExpression"):
                opp_val = getattr(old_value, "NQC_VariableExpression", None)
                if opp_val == self:
                    setattr(old_value, "NQC_VariableExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NQC_VariableExpression"):
                opp_val = getattr(value, "NQC_VariableExpression", None)
                setattr(value, "NQC_VariableExpression", self)

class NQC_Label:

    def __init__(self, Label: str, NQC_Label: "NQC_Statement" = None, NQC_Label56: "NQC_GoToStatement" = None):
        self.Label = Label
        self.NQC_Label = NQC_Label
        self.NQC_Label56 = NQC_Label56
        
    @property
    def Label(self) -> str:
        return self.__Label

    @Label.setter
    def Label(self, Label: str):
        self.__Label = Label

    @property
    def NQC_Label56(self):
        return self.__NQC_Label56

    @NQC_Label56.setter
    def NQC_Label56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NQC_Label__NQC_Label56", None)
        self.__NQC_Label56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NQC_GoToStatement"):
                opp_val = getattr(old_value, "NQC_GoToStatement", None)
                if opp_val == self:
                    setattr(old_value, "NQC_GoToStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NQC_GoToStatement"):
                opp_val = getattr(value, "NQC_GoToStatement", None)
                setattr(value, "NQC_GoToStatement", self)

    @property
    def NQC_Label(self):
        return self.__NQC_Label

    @NQC_Label.setter
    def NQC_Label(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NQC_Label__NQC_Label", None)
        self.__NQC_Label = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NQC_Statement29"):
                opp_val = getattr(old_value, "NQC_Statement29", None)
                if opp_val == self:
                    setattr(old_value, "NQC_Statement29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NQC_Statement29"):
                opp_val = getattr(value, "NQC_Statement29", None)
                setattr(value, "NQC_Statement29", self)

class NQC_IntegerConstant(ConstantExpression):

    def __init__(self, Value: int, NQC_IntegerConstant: "NQC_Variable" = None):
        self.Value = Value
        self.NQC_IntegerConstant = NQC_IntegerConstant
        
    @property
    def Value(self) -> int:
        return self.__Value

    @Value.setter
    def Value(self, Value: int):
        self.__Value = Value

    @property
    def NQC_IntegerConstant(self):
        return self.__NQC_IntegerConstant

    @NQC_IntegerConstant.setter
    def NQC_IntegerConstant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NQC_IntegerConstant__NQC_IntegerConstant", None)
        self.__NQC_IntegerConstant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NQC_Variable27"):
                opp_val = getattr(old_value, "NQC_Variable27", None)
                if opp_val == self:
                    setattr(old_value, "NQC_Variable27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NQC_Variable27"):
                opp_val = getattr(value, "NQC_Variable27", None)
                setattr(value, "NQC_Variable27", self)

class NQC_BlockStatement(Statement):

    pass
class NQC_Expression(Statement):

    pass
class Variable:

    pass
class NQC_Parameter(Variable):

    pass
class NQC_ConstantExpression(ValueExpression):

    pass
class NQC_Variable(ABC):

    def __init__(self, Name: str, Type: str, NQC_Variable: "NQC_ConstantExpression" = None, NQC_Variable27: "NQC_IntegerConstant" = None, NQC_Variable92: "NQC_VariableExpression" = None):
        self.Name = Name
        self.Type = Type
        self.NQC_Variable = NQC_Variable
        self.NQC_Variable27 = NQC_Variable27
        self.NQC_Variable92 = NQC_Variable92
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Type(self) -> str:
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def NQC_Variable92(self):
        return self.__NQC_Variable92

    @NQC_Variable92.setter
    def NQC_Variable92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NQC_Variable__NQC_Variable92", None)
        self.__NQC_Variable92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NQC_VariableExpression91"):
                opp_val = getattr(old_value, "NQC_VariableExpression91", None)
                if opp_val == self:
                    setattr(old_value, "NQC_VariableExpression91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NQC_VariableExpression91"):
                opp_val = getattr(value, "NQC_VariableExpression91", None)
                setattr(value, "NQC_VariableExpression91", self)

    @property
    def NQC_Variable27(self):
        return self.__NQC_Variable27

    @NQC_Variable27.setter
    def NQC_Variable27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NQC_Variable__NQC_Variable27", None)
        self.__NQC_Variable27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NQC_IntegerConstant"):
                opp_val = getattr(old_value, "NQC_IntegerConstant", None)
                if opp_val == self:
                    setattr(old_value, "NQC_IntegerConstant", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NQC_IntegerConstant"):
                opp_val = getattr(value, "NQC_IntegerConstant", None)
                setattr(value, "NQC_IntegerConstant", self)

    @property
    def NQC_Variable(self):
        return self.__NQC_Variable

    @NQC_Variable.setter
    def NQC_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NQC_Variable__NQC_Variable", None)
        self.__NQC_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NQC_ConstantExpression"):
                opp_val = getattr(old_value, "NQC_ConstantExpression", None)
                if opp_val == self:
                    setattr(old_value, "NQC_ConstantExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NQC_ConstantExpression"):
                opp_val = getattr(value, "NQC_ConstantExpression", None)
                setattr(value, "NQC_ConstantExpression", self)

class NQC_Statement(ABC):

    pass
class NQC_GlobalVariable(Variable):

    pass
class NQC_Subroutine:

    def __init__(self, Name: str, NQC_Subroutine: "NQC_Program" = None, NQC_Subroutine23: set["NQC_LocalVariable"] = None, NQC_Subroutine20: set["NQC_Statement"] = None, NQC_Subroutine106: "NQC_SubroutineCall" = None):
        self.Name = Name
        self.NQC_Subroutine = NQC_Subroutine
        self.NQC_Subroutine23 = NQC_Subroutine23 if NQC_Subroutine23 is not None else set()
        self.NQC_Subroutine20 = NQC_Subroutine20 if NQC_Subroutine20 is not None else set()
        self.NQC_Subroutine106 = NQC_Subroutine106
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def NQC_Subroutine23(self):
        return self.__NQC_Subroutine23

    @NQC_Subroutine23.setter
    def NQC_Subroutine23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NQC_Subroutine__NQC_Subroutine23", None)
        self.__NQC_Subroutine23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NQC_LocalVariable24"):
                    opp_val = getattr(item, "NQC_LocalVariable24", None)
                    
                    if opp_val == self:
                        setattr(item, "NQC_LocalVariable24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NQC_LocalVariable24"):
                    opp_val = getattr(item, "NQC_LocalVariable24", None)
                    
                    setattr(item, "NQC_LocalVariable24", self)
                    

    @property
    def NQC_Subroutine106(self):
        return self.__NQC_Subroutine106

    @NQC_Subroutine106.setter
    def NQC_Subroutine106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NQC_Subroutine__NQC_Subroutine106", None)
        self.__NQC_Subroutine106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NQC_SubroutineCall"):
                opp_val = getattr(old_value, "NQC_SubroutineCall", None)
                if opp_val == self:
                    setattr(old_value, "NQC_SubroutineCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NQC_SubroutineCall"):
                opp_val = getattr(value, "NQC_SubroutineCall", None)
                setattr(value, "NQC_SubroutineCall", self)

    @property
    def NQC_Subroutine20(self):
        return self.__NQC_Subroutine20

    @NQC_Subroutine20.setter
    def NQC_Subroutine20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NQC_Subroutine__NQC_Subroutine20", None)
        self.__NQC_Subroutine20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NQC_Statement21"):
                    opp_val = getattr(item, "NQC_Statement21", None)
                    
                    if opp_val == self:
                        setattr(item, "NQC_Statement21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NQC_Statement21"):
                    opp_val = getattr(item, "NQC_Statement21", None)
                    
                    setattr(item, "NQC_Statement21", self)
                    

    @property
    def NQC_Subroutine(self):
        return self.__NQC_Subroutine

    @NQC_Subroutine.setter
    def NQC_Subroutine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NQC_Subroutine__NQC_Subroutine", None)
        self.__NQC_Subroutine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NQC_Program4"):
                opp_val = getattr(old_value, "NQC_Program4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NQC_Program4"):
                opp_val = getattr(value, "NQC_Program4", None)
                if opp_val is None:
                    setattr(value, "NQC_Program4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class NQC_Function:

    def __init__(self, Name: str, NQC_Function: "NQC_Program" = None, NQC_Function12: set["NQC_Statement"] = None, NQC_Function15: set["NQC_LocalVariable"] = None, NQC_Function18: set["NQC_Parameter"] = None, NQC_Function101: "NQC_FunctionCall" = None):
        self.Name = Name
        self.NQC_Function = NQC_Function
        self.NQC_Function12 = NQC_Function12 if NQC_Function12 is not None else set()
        self.NQC_Function15 = NQC_Function15 if NQC_Function15 is not None else set()
        self.NQC_Function18 = NQC_Function18 if NQC_Function18 is not None else set()
        self.NQC_Function101 = NQC_Function101
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def NQC_Function18(self):
        return self.__NQC_Function18

    @NQC_Function18.setter
    def NQC_Function18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NQC_Function__NQC_Function18", None)
        self.__NQC_Function18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NQC_Parameter"):
                    opp_val = getattr(item, "NQC_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "NQC_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NQC_Parameter"):
                    opp_val = getattr(item, "NQC_Parameter", None)
                    
                    setattr(item, "NQC_Parameter", self)
                    

    @property
    def NQC_Function101(self):
        return self.__NQC_Function101

    @NQC_Function101.setter
    def NQC_Function101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NQC_Function__NQC_Function101", None)
        self.__NQC_Function101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NQC_FunctionCall"):
                opp_val = getattr(old_value, "NQC_FunctionCall", None)
                if opp_val == self:
                    setattr(old_value, "NQC_FunctionCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NQC_FunctionCall"):
                opp_val = getattr(value, "NQC_FunctionCall", None)
                setattr(value, "NQC_FunctionCall", self)

    @property
    def NQC_Function12(self):
        return self.__NQC_Function12

    @NQC_Function12.setter
    def NQC_Function12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NQC_Function__NQC_Function12", None)
        self.__NQC_Function12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NQC_Statement13"):
                    opp_val = getattr(item, "NQC_Statement13", None)
                    
                    if opp_val == self:
                        setattr(item, "NQC_Statement13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NQC_Statement13"):
                    opp_val = getattr(item, "NQC_Statement13", None)
                    
                    setattr(item, "NQC_Statement13", self)
                    

    @property
    def NQC_Function(self):
        return self.__NQC_Function

    @NQC_Function.setter
    def NQC_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NQC_Function__NQC_Function", None)
        self.__NQC_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NQC_Program2"):
                opp_val = getattr(old_value, "NQC_Program2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NQC_Program2"):
                opp_val = getattr(value, "NQC_Program2", None)
                if opp_val is None:
                    setattr(value, "NQC_Program2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def NQC_Function15(self):
        return self.__NQC_Function15

    @NQC_Function15.setter
    def NQC_Function15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NQC_Function__NQC_Function15", None)
        self.__NQC_Function15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NQC_LocalVariable16"):
                    opp_val = getattr(item, "NQC_LocalVariable16", None)
                    
                    if opp_val == self:
                        setattr(item, "NQC_LocalVariable16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NQC_LocalVariable16"):
                    opp_val = getattr(item, "NQC_LocalVariable16", None)
                    
                    setattr(item, "NQC_LocalVariable16", self)
                    

class NQC_LocalVariable(Variable):

    pass
class NQC_Task:

    def __init__(self, Name: str, NQC_Task8: set["NQC_Statement"] = None, NQC_Task10: set["NQC_LocalVariable"] = None, NQC_Task: "NQC_Program" = None, NQC_Task39: "NQC_StartStatement" = None, NQC_Task41: "NQC_StopStatement" = None):
        self.Name = Name
        self.NQC_Task8 = NQC_Task8 if NQC_Task8 is not None else set()
        self.NQC_Task10 = NQC_Task10 if NQC_Task10 is not None else set()
        self.NQC_Task = NQC_Task
        self.NQC_Task39 = NQC_Task39
        self.NQC_Task41 = NQC_Task41
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def NQC_Task10(self):
        return self.__NQC_Task10

    @NQC_Task10.setter
    def NQC_Task10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NQC_Task__NQC_Task10", None)
        self.__NQC_Task10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NQC_LocalVariable"):
                    opp_val = getattr(item, "NQC_LocalVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "NQC_LocalVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NQC_LocalVariable"):
                    opp_val = getattr(item, "NQC_LocalVariable", None)
                    
                    setattr(item, "NQC_LocalVariable", self)
                    

    @property
    def NQC_Task41(self):
        return self.__NQC_Task41

    @NQC_Task41.setter
    def NQC_Task41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NQC_Task__NQC_Task41", None)
        self.__NQC_Task41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NQC_StopStatement"):
                opp_val = getattr(old_value, "NQC_StopStatement", None)
                if opp_val == self:
                    setattr(old_value, "NQC_StopStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NQC_StopStatement"):
                opp_val = getattr(value, "NQC_StopStatement", None)
                setattr(value, "NQC_StopStatement", self)

    @property
    def NQC_Task39(self):
        return self.__NQC_Task39

    @NQC_Task39.setter
    def NQC_Task39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NQC_Task__NQC_Task39", None)
        self.__NQC_Task39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NQC_StartStatement"):
                opp_val = getattr(old_value, "NQC_StartStatement", None)
                if opp_val == self:
                    setattr(old_value, "NQC_StartStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NQC_StartStatement"):
                opp_val = getattr(value, "NQC_StartStatement", None)
                setattr(value, "NQC_StartStatement", self)

    @property
    def NQC_Task8(self):
        return self.__NQC_Task8

    @NQC_Task8.setter
    def NQC_Task8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NQC_Task__NQC_Task8", None)
        self.__NQC_Task8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NQC_Statement"):
                    opp_val = getattr(item, "NQC_Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "NQC_Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NQC_Statement"):
                    opp_val = getattr(item, "NQC_Statement", None)
                    
                    setattr(item, "NQC_Statement", self)
                    

    @property
    def NQC_Task(self):
        return self.__NQC_Task

    @NQC_Task.setter
    def NQC_Task(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NQC_Task__NQC_Task", None)
        self.__NQC_Task = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NQC_Program"):
                opp_val = getattr(old_value, "NQC_Program", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NQC_Program"):
                opp_val = getattr(value, "NQC_Program", None)
                if opp_val is None:
                    setattr(value, "NQC_Program", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class NQC_Program:

    def __init__(self, Name: str, NQC_Program: set["NQC_Task"] = None, NQC_Program2: set["NQC_Function"] = None, NQC_Program4: set["NQC_Subroutine"] = None, NQC_Program6: set["NQC_GlobalVariable"] = None):
        self.Name = Name
        self.NQC_Program = NQC_Program if NQC_Program is not None else set()
        self.NQC_Program2 = NQC_Program2 if NQC_Program2 is not None else set()
        self.NQC_Program4 = NQC_Program4 if NQC_Program4 is not None else set()
        self.NQC_Program6 = NQC_Program6 if NQC_Program6 is not None else set()
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def NQC_Program(self):
        return self.__NQC_Program

    @NQC_Program.setter
    def NQC_Program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NQC_Program__NQC_Program", None)
        self.__NQC_Program = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NQC_Task"):
                    opp_val = getattr(item, "NQC_Task", None)
                    
                    if opp_val == self:
                        setattr(item, "NQC_Task", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NQC_Task"):
                    opp_val = getattr(item, "NQC_Task", None)
                    
                    setattr(item, "NQC_Task", self)
                    

    @property
    def NQC_Program6(self):
        return self.__NQC_Program6

    @NQC_Program6.setter
    def NQC_Program6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NQC_Program__NQC_Program6", None)
        self.__NQC_Program6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NQC_GlobalVariable"):
                    opp_val = getattr(item, "NQC_GlobalVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "NQC_GlobalVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NQC_GlobalVariable"):
                    opp_val = getattr(item, "NQC_GlobalVariable", None)
                    
                    setattr(item, "NQC_GlobalVariable", self)
                    

    @property
    def NQC_Program2(self):
        return self.__NQC_Program2

    @NQC_Program2.setter
    def NQC_Program2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NQC_Program__NQC_Program2", None)
        self.__NQC_Program2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NQC_Function"):
                    opp_val = getattr(item, "NQC_Function", None)
                    
                    if opp_val == self:
                        setattr(item, "NQC_Function", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NQC_Function"):
                    opp_val = getattr(item, "NQC_Function", None)
                    
                    setattr(item, "NQC_Function", self)
                    

    @property
    def NQC_Program4(self):
        return self.__NQC_Program4

    @NQC_Program4.setter
    def NQC_Program4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NQC_Program__NQC_Program4", None)
        self.__NQC_Program4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NQC_Subroutine"):
                    opp_val = getattr(item, "NQC_Subroutine", None)
                    
                    if opp_val == self:
                        setattr(item, "NQC_Subroutine", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NQC_Subroutine"):
                    opp_val = getattr(item, "NQC_Subroutine", None)
                    
                    setattr(item, "NQC_Subroutine", self)
                    
