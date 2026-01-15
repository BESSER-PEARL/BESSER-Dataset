from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ComparisonOperator(Enum):
    UNEQUAL = "UNEQUAL"
    LESS_THAN = "LESS_THAN"
    LESS_THAN_OR_EQUAL = "LESS_THAN_OR_EQUAL"
    GREATER_THAN_OR_EQUAL = "GREATER_THAN_OR_EQUAL"
    GREATER_THAN = "GREATER_THAN"
    EQUAL = "EQUAL"


############################################
# Definition of Classes
############################################

class BinaryExpression:

    pass
class hlp_ArithmeticExpression(BinaryExpression):

    pass
class UnaryExpression:

    pass
class hlp_UnaryMinusExpression(UnaryExpression):

    pass
class ConditionalLoop:

    pass
class hlp_WhileLoop(ConditionalLoop):

    pass
class Loop:

    pass
class hlp_ForLoop(Loop):

    def __init__(self, incrementing: bool, hlp_ForLoop: "hlp_VariableReference" = None, hlp_ForLoop43: "hlp_Expression" = None, hlp_ForLoop46: "hlp_Expression" = None):
        self.incrementing = incrementing
        self.hlp_ForLoop = hlp_ForLoop
        self.hlp_ForLoop43 = hlp_ForLoop43
        self.hlp_ForLoop46 = hlp_ForLoop46
        
    @property
    def incrementing(self) -> bool:
        return self.__incrementing

    @incrementing.setter
    def incrementing(self, incrementing: bool):
        self.__incrementing = incrementing

    @property
    def hlp_ForLoop(self):
        return self.__hlp_ForLoop

    @hlp_ForLoop.setter
    def hlp_ForLoop(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlp_ForLoop__hlp_ForLoop", None)
        self.__hlp_ForLoop = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hlp_VariableReference41"):
                opp_val = getattr(old_value, "hlp_VariableReference41", None)
                if opp_val == self:
                    setattr(old_value, "hlp_VariableReference41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hlp_VariableReference41"):
                opp_val = getattr(value, "hlp_VariableReference41", None)
                setattr(value, "hlp_VariableReference41", self)

    @property
    def hlp_ForLoop46(self):
        return self.__hlp_ForLoop46

    @hlp_ForLoop46.setter
    def hlp_ForLoop46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlp_ForLoop__hlp_ForLoop46", None)
        self.__hlp_ForLoop46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hlp_Expression47"):
                opp_val = getattr(old_value, "hlp_Expression47", None)
                if opp_val == self:
                    setattr(old_value, "hlp_Expression47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hlp_Expression47"):
                opp_val = getattr(value, "hlp_Expression47", None)
                setattr(value, "hlp_Expression47", self)

    @property
    def hlp_ForLoop43(self):
        return self.__hlp_ForLoop43

    @hlp_ForLoop43.setter
    def hlp_ForLoop43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlp_ForLoop__hlp_ForLoop43", None)
        self.__hlp_ForLoop43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hlp_Expression44"):
                opp_val = getattr(old_value, "hlp_Expression44", None)
                if opp_val == self:
                    setattr(old_value, "hlp_Expression44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hlp_Expression44"):
                opp_val = getattr(value, "hlp_Expression44", None)
                setattr(value, "hlp_Expression44", self)

class hlp_Nameable(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class hlp_ConditionalLoop(Loop):

    pass
class hlp_Condition:

    def __init__(self, operator: str, hlp_Condition: "hlp_IfStatement" = None, hlp_Condition29: "hlp_Expression" = None, hlp_Condition32: "hlp_Expression" = None, hlp_Condition39: "hlp_ConditionalLoop" = None):
        self.operator = operator
        self.hlp_Condition = hlp_Condition
        self.hlp_Condition29 = hlp_Condition29
        self.hlp_Condition32 = hlp_Condition32
        self.hlp_Condition39 = hlp_Condition39
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def hlp_Condition(self):
        return self.__hlp_Condition

    @hlp_Condition.setter
    def hlp_Condition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlp_Condition__hlp_Condition", None)
        self.__hlp_Condition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hlp_IfStatement27"):
                opp_val = getattr(old_value, "hlp_IfStatement27", None)
                if opp_val == self:
                    setattr(old_value, "hlp_IfStatement27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hlp_IfStatement27"):
                opp_val = getattr(value, "hlp_IfStatement27", None)
                setattr(value, "hlp_IfStatement27", self)

    @property
    def hlp_Condition39(self):
        return self.__hlp_Condition39

    @hlp_Condition39.setter
    def hlp_Condition39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlp_Condition__hlp_Condition39", None)
        self.__hlp_Condition39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hlp_ConditionalLoop"):
                opp_val = getattr(old_value, "hlp_ConditionalLoop", None)
                if opp_val == self:
                    setattr(old_value, "hlp_ConditionalLoop", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hlp_ConditionalLoop"):
                opp_val = getattr(value, "hlp_ConditionalLoop", None)
                setattr(value, "hlp_ConditionalLoop", self)

    @property
    def hlp_Condition29(self):
        return self.__hlp_Condition29

    @hlp_Condition29.setter
    def hlp_Condition29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlp_Condition__hlp_Condition29", None)
        self.__hlp_Condition29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hlp_Expression30"):
                opp_val = getattr(old_value, "hlp_Expression30", None)
                if opp_val == self:
                    setattr(old_value, "hlp_Expression30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hlp_Expression30"):
                opp_val = getattr(value, "hlp_Expression30", None)
                setattr(value, "hlp_Expression30", self)

    @property
    def hlp_Condition32(self):
        return self.__hlp_Condition32

    @hlp_Condition32.setter
    def hlp_Condition32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlp_Condition__hlp_Condition32", None)
        self.__hlp_Condition32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hlp_Expression33"):
                opp_val = getattr(old_value, "hlp_Expression33", None)
                if opp_val == self:
                    setattr(old_value, "hlp_Expression33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hlp_Expression33"):
                opp_val = getattr(value, "hlp_Expression33", None)
                setattr(value, "hlp_Expression33", self)

class hlp_VariableDeclarationScope(ABC):

    pass
class hlp_Block:

    pass
class AtomicExpression:

    pass
class hlp_LiteralValue(AtomicExpression):

    def __init__(self, rawValue: str):
        self.rawValue = rawValue
        
    @property
    def rawValue(self) -> str:
        return self.__rawValue

    @rawValue.setter
    def rawValue(self, rawValue: str):
        self.__rawValue = rawValue

class hlp_Statement(ABC):

    pass
class hlp_VariableReference(AtomicExpression):

    pass
class Expression:

    pass
class hlp_ParenthesisExpression(Expression):

    pass
class hlp_BinaryExpression(Expression):

    pass
class hlp_UnaryExpression(Expression):

    pass
class hlp_AtomicExpression(Expression):

    pass
class ArithmeticExpression:

    pass
class hlp_DivideExpression(ArithmeticExpression):

    pass
class hlp_SubtractExpression(ArithmeticExpression):

    pass
class hlp_MultiplyExpression(ArithmeticExpression):

    pass
class hlp_AddExpression(ArithmeticExpression):

    pass
class Nameable:

    pass
class VariableDeclarationScope:

    pass
class hlp_Task(VariableDeclarationScope, Nameable):

    pass
class hlp_HighLevelProgram(VariableDeclarationScope, Nameable):

    pass
class Statement:

    pass
class hlp_ExpressionStatement(Statement):

    pass
class hlp_IfStatement(Statement):

    pass
class hlp_SynchronizedStatement(Statement):

    pass
class hlp_Loop(Statement):

    pass
class hlp_Assignment(Statement):

    pass
class hlp_Expression(ABC):

    pass
class hlp_Variable(Nameable):

    pass
class hlp_VariableDeclaration:

    pass
class hlp_ScheduleInstruction:

    pass