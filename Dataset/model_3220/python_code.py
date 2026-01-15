from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ComparisonOperator(Enum):
    EQUAL = "EQUAL"
    INEQUAL = "INEQUAL"
    LESS_THAN = "LESS_THAN"
    LESS_THAN_EQUAL = "LESS_THAN_EQUAL"
    GREATER_THAN = "GREATER_THAN"
    GREATER_THAN_EQUAL = "GREATER_THAN_EQUAL"
class ForLoopDirection(Enum):
    UP = "UP"
    DOWN = "DOWN"


############################################
# Definition of Classes
############################################

class UnaryExpression:

    pass
class mpl_ParenthesisExpression(UnaryExpression):

    pass
class mpl_UnaryMinusExpression(UnaryExpression):

    pass
class ArithmeticExpression:

    pass
class mpl_AddExpression(ArithmeticExpression):

    pass
class mpl_MulExpression(ArithmeticExpression):

    pass
class mpl_DivExpression(ArithmeticExpression):

    pass
class mpl_SubExpression(ArithmeticExpression):

    pass
class AtomicExpression:

    pass
class mpl_LiteralValue(AtomicExpression):

    def __init__(self, rawValue: int):
        self.rawValue = rawValue
        
    @property
    def rawValue(self) -> int:
        return self.__rawValue

    @rawValue.setter
    def rawValue(self, rawValue: int):
        self.__rawValue = rawValue

class Expression:

    pass
class mpl_ArithmeticExpression(Expression):

    pass
class mpl_OperationExpression(Expression):

    pass
class mpl_UnaryExpression(Expression):

    pass
class mpl_AtomicExpression(Expression):

    pass
class Statement:

    pass
class mpl_ExpressionStatement(Statement):

    pass
class mpl_ForLoop(Statement):

    def __init__(self, direction: str, mpl_ForLoop: "mpl_Assignment" = None, mpl_ForLoop34: "mpl_Expression" = None, mpl_ForLoop37: "mpl_Block" = None):
        self.direction = direction
        self.mpl_ForLoop = mpl_ForLoop
        self.mpl_ForLoop34 = mpl_ForLoop34
        self.mpl_ForLoop37 = mpl_ForLoop37
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def mpl_ForLoop37(self):
        return self.__mpl_ForLoop37

    @mpl_ForLoop37.setter
    def mpl_ForLoop37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpl_ForLoop__mpl_ForLoop37", None)
        self.__mpl_ForLoop37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mpl_Block38"):
                opp_val = getattr(old_value, "mpl_Block38", None)
                if opp_val == self:
                    setattr(old_value, "mpl_Block38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mpl_Block38"):
                opp_val = getattr(value, "mpl_Block38", None)
                setattr(value, "mpl_Block38", self)

    @property
    def mpl_ForLoop(self):
        return self.__mpl_ForLoop

    @mpl_ForLoop.setter
    def mpl_ForLoop(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpl_ForLoop__mpl_ForLoop", None)
        self.__mpl_ForLoop = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mpl_Assignment32"):
                opp_val = getattr(old_value, "mpl_Assignment32", None)
                if opp_val == self:
                    setattr(old_value, "mpl_Assignment32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mpl_Assignment32"):
                opp_val = getattr(value, "mpl_Assignment32", None)
                setattr(value, "mpl_Assignment32", self)

    @property
    def mpl_ForLoop34(self):
        return self.__mpl_ForLoop34

    @mpl_ForLoop34.setter
    def mpl_ForLoop34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpl_ForLoop__mpl_ForLoop34", None)
        self.__mpl_ForLoop34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mpl_Expression35"):
                opp_val = getattr(old_value, "mpl_Expression35", None)
                if opp_val == self:
                    setattr(old_value, "mpl_Expression35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mpl_Expression35"):
                opp_val = getattr(value, "mpl_Expression35", None)
                setattr(value, "mpl_Expression35", self)

class mpl_ReturnStatement(Statement):

    pass
class mpl_Trace(Statement):

    pass
class mpl_WhileLoop(Statement):

    pass
class mpl_Assignment(Statement):

    pass
class mpl_Statement(ABC):

    pass
class mpl_Expression(ABC):

    pass
class mpl_ComparisonExpression:

    def __init__(self, comparisonOperator: str, mpl_ComparisonExpression: "mpl_IfStatement" = None, mpl_ComparisonExpression27: "mpl_WhileLoop" = None, mpl_ComparisonExpression49: "mpl_Expression" = None, mpl_ComparisonExpression52: "mpl_Expression" = None):
        self.comparisonOperator = comparisonOperator
        self.mpl_ComparisonExpression = mpl_ComparisonExpression
        self.mpl_ComparisonExpression27 = mpl_ComparisonExpression27
        self.mpl_ComparisonExpression49 = mpl_ComparisonExpression49
        self.mpl_ComparisonExpression52 = mpl_ComparisonExpression52
        
    @property
    def comparisonOperator(self) -> str:
        return self.__comparisonOperator

    @comparisonOperator.setter
    def comparisonOperator(self, comparisonOperator: str):
        self.__comparisonOperator = comparisonOperator

    @property
    def mpl_ComparisonExpression52(self):
        return self.__mpl_ComparisonExpression52

    @mpl_ComparisonExpression52.setter
    def mpl_ComparisonExpression52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpl_ComparisonExpression__mpl_ComparisonExpression52", None)
        self.__mpl_ComparisonExpression52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mpl_Expression53"):
                opp_val = getattr(old_value, "mpl_Expression53", None)
                if opp_val == self:
                    setattr(old_value, "mpl_Expression53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mpl_Expression53"):
                opp_val = getattr(value, "mpl_Expression53", None)
                setattr(value, "mpl_Expression53", self)

    @property
    def mpl_ComparisonExpression(self):
        return self.__mpl_ComparisonExpression

    @mpl_ComparisonExpression.setter
    def mpl_ComparisonExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpl_ComparisonExpression__mpl_ComparisonExpression", None)
        self.__mpl_ComparisonExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mpl_IfStatement"):
                opp_val = getattr(old_value, "mpl_IfStatement", None)
                if opp_val == self:
                    setattr(old_value, "mpl_IfStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mpl_IfStatement"):
                opp_val = getattr(value, "mpl_IfStatement", None)
                setattr(value, "mpl_IfStatement", self)

    @property
    def mpl_ComparisonExpression27(self):
        return self.__mpl_ComparisonExpression27

    @mpl_ComparisonExpression27.setter
    def mpl_ComparisonExpression27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpl_ComparisonExpression__mpl_ComparisonExpression27", None)
        self.__mpl_ComparisonExpression27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mpl_WhileLoop"):
                opp_val = getattr(old_value, "mpl_WhileLoop", None)
                if opp_val == self:
                    setattr(old_value, "mpl_WhileLoop", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mpl_WhileLoop"):
                opp_val = getattr(value, "mpl_WhileLoop", None)
                setattr(value, "mpl_WhileLoop", self)

    @property
    def mpl_ComparisonExpression49(self):
        return self.__mpl_ComparisonExpression49

    @mpl_ComparisonExpression49.setter
    def mpl_ComparisonExpression49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpl_ComparisonExpression__mpl_ComparisonExpression49", None)
        self.__mpl_ComparisonExpression49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mpl_Expression50"):
                opp_val = getattr(old_value, "mpl_Expression50", None)
                if opp_val == self:
                    setattr(old_value, "mpl_Expression50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mpl_Expression50"):
                opp_val = getattr(value, "mpl_Expression50", None)
                setattr(value, "mpl_Expression50", self)

class mpl_IfStatement(Statement):

    pass
class mpl_VariableReference(AtomicExpression):

    pass
class Operation:

    pass
class mpl_Function(Operation):

    pass
class mpl_Variable:

    def __init__(self, name: str, mpl_Variable10: "mpl_VariableDeclaration" = None, mpl_Variable: "mpl_Operation" = None, mpl_Variable47: "mpl_VariableReference" = None):
        self.name = name
        self.mpl_Variable10 = mpl_Variable10
        self.mpl_Variable = mpl_Variable
        self.mpl_Variable47 = mpl_Variable47
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mpl_Variable10(self):
        return self.__mpl_Variable10

    @mpl_Variable10.setter
    def mpl_Variable10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpl_Variable__mpl_Variable10", None)
        self.__mpl_Variable10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mpl_VariableDeclaration9"):
                opp_val = getattr(old_value, "mpl_VariableDeclaration9", None)
                if opp_val == self:
                    setattr(old_value, "mpl_VariableDeclaration9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mpl_VariableDeclaration9"):
                opp_val = getattr(value, "mpl_VariableDeclaration9", None)
                setattr(value, "mpl_VariableDeclaration9", self)

    @property
    def mpl_Variable47(self):
        return self.__mpl_Variable47

    @mpl_Variable47.setter
    def mpl_Variable47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpl_Variable__mpl_Variable47", None)
        self.__mpl_Variable47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mpl_VariableReference46"):
                opp_val = getattr(old_value, "mpl_VariableReference46", None)
                if opp_val == self:
                    setattr(old_value, "mpl_VariableReference46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mpl_VariableReference46"):
                opp_val = getattr(value, "mpl_VariableReference46", None)
                setattr(value, "mpl_VariableReference46", self)

    @property
    def mpl_Variable(self):
        return self.__mpl_Variable

    @mpl_Variable.setter
    def mpl_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpl_Variable__mpl_Variable", None)
        self.__mpl_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mpl_Operation7"):
                opp_val = getattr(old_value, "mpl_Operation7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mpl_Operation7"):
                opp_val = getattr(value, "mpl_Operation7", None)
                if opp_val is None:
                    setattr(value, "mpl_Operation7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class FunctionalUnit:

    pass
class mpl_Block:

    pass
class mpl_VariableDeclaration:

    pass
class mpl_Procedure(Operation):

    pass
class mpl_Program(FunctionalUnit):

    pass
class mpl_MPLModel:

    pass
class mpl_FunctionalUnit(ABC):

    def __init__(self, name: str, mpl_FunctionalUnit: set["mpl_VariableDeclaration"] = None, mpl_FunctionalUnit5: "mpl_Block" = None):
        self.name = name
        self.mpl_FunctionalUnit = mpl_FunctionalUnit if mpl_FunctionalUnit is not None else set()
        self.mpl_FunctionalUnit5 = mpl_FunctionalUnit5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mpl_FunctionalUnit5(self):
        return self.__mpl_FunctionalUnit5

    @mpl_FunctionalUnit5.setter
    def mpl_FunctionalUnit5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpl_FunctionalUnit__mpl_FunctionalUnit5", None)
        self.__mpl_FunctionalUnit5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mpl_Block"):
                opp_val = getattr(old_value, "mpl_Block", None)
                if opp_val == self:
                    setattr(old_value, "mpl_Block", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mpl_Block"):
                opp_val = getattr(value, "mpl_Block", None)
                setattr(value, "mpl_Block", self)

    @property
    def mpl_FunctionalUnit(self):
        return self.__mpl_FunctionalUnit

    @mpl_FunctionalUnit.setter
    def mpl_FunctionalUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpl_FunctionalUnit__mpl_FunctionalUnit", None)
        self.__mpl_FunctionalUnit = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mpl_VariableDeclaration"):
                    opp_val = getattr(item, "mpl_VariableDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "mpl_VariableDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mpl_VariableDeclaration"):
                    opp_val = getattr(item, "mpl_VariableDeclaration", None)
                    
                    setattr(item, "mpl_VariableDeclaration", self)
                    

class mpl_Operation(FunctionalUnit):

    pass