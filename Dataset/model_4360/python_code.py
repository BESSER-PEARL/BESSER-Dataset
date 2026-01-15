from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Operation:

    pass
class mpl_Procedure(Operation):

    pass
class mpl_Function(Operation):

    pass
class ComparisonOperator:

    pass
class mpl_LT(ComparisonOperator):

    pass
class mpl_GE(ComparisonOperator):

    pass
class mpl_LE(ComparisonOperator):

    pass
class mpl_NE(ComparisonOperator):

    pass
class mpl_GT(ComparisonOperator):

    pass
class mpl_EQ(ComparisonOperator):

    pass
class mpl_ComparisonOperator(ABC):

    pass
class mpl_Comparison:

    pass
class Loop:

    pass
class mpl_For(Loop):

    def __init__(self, downwards: str, mpl_For: "mpl_Assignment" = None, mpl_For56: "mpl_Expression" = None):
        self.downwards = downwards
        self.mpl_For = mpl_For
        self.mpl_For56 = mpl_For56
        
    @property
    def downwards(self) -> str:
        return self.__downwards

    @downwards.setter
    def downwards(self, downwards: str):
        self.__downwards = downwards

    @property
    def mpl_For56(self):
        return self.__mpl_For56

    @mpl_For56.setter
    def mpl_For56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpl_For__mpl_For56", None)
        self.__mpl_For56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mpl_Expression57"):
                opp_val = getattr(old_value, "mpl_Expression57", None)
                if opp_val == self:
                    setattr(old_value, "mpl_Expression57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mpl_Expression57"):
                opp_val = getattr(value, "mpl_Expression57", None)
                setattr(value, "mpl_Expression57", self)

    @property
    def mpl_For(self):
        return self.__mpl_For

    @mpl_For.setter
    def mpl_For(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpl_For__mpl_For", None)
        self.__mpl_For = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mpl_Assignment54"):
                opp_val = getattr(old_value, "mpl_Assignment54", None)
                if opp_val == self:
                    setattr(old_value, "mpl_Assignment54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mpl_Assignment54"):
                opp_val = getattr(value, "mpl_Assignment54", None)
                setattr(value, "mpl_Assignment54", self)

class mpl_While(Loop):

    pass
class UnaryExpression:

    pass
class mpl_NegateExpression(UnaryExpression):

    pass
class ArithmeticExpression:

    pass
class mpl_MultiplyExpression(ArithmeticExpression):

    pass
class mpl_SubtractExpression(ArithmeticExpression):

    pass
class mpl_DivisionExpression(ArithmeticExpression):

    pass
class mpl_AddExpression(ArithmeticExpression):

    pass
class AtomicExpression:

    pass
class mpl_LiteralValue(AtomicExpression):

    def __init__(self, rawValue: int, mpl_LiteralValue: "mpl_InputExpression" = None, mpl_LiteralValue33: "mpl_InputExpression" = None):
        self.rawValue = rawValue
        self.mpl_LiteralValue = mpl_LiteralValue
        self.mpl_LiteralValue33 = mpl_LiteralValue33
        
    @property
    def rawValue(self) -> int:
        return self.__rawValue

    @rawValue.setter
    def rawValue(self, rawValue: int):
        self.__rawValue = rawValue

    @property
    def mpl_LiteralValue(self):
        return self.__mpl_LiteralValue

    @mpl_LiteralValue.setter
    def mpl_LiteralValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpl_LiteralValue__mpl_LiteralValue", None)
        self.__mpl_LiteralValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mpl_InputExpression"):
                opp_val = getattr(old_value, "mpl_InputExpression", None)
                if opp_val == self:
                    setattr(old_value, "mpl_InputExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mpl_InputExpression"):
                opp_val = getattr(value, "mpl_InputExpression", None)
                setattr(value, "mpl_InputExpression", self)

    @property
    def mpl_LiteralValue33(self):
        return self.__mpl_LiteralValue33

    @mpl_LiteralValue33.setter
    def mpl_LiteralValue33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpl_LiteralValue__mpl_LiteralValue33", None)
        self.__mpl_LiteralValue33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mpl_InputExpression32"):
                opp_val = getattr(old_value, "mpl_InputExpression32", None)
                if opp_val == self:
                    setattr(old_value, "mpl_InputExpression32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mpl_InputExpression32"):
                opp_val = getattr(value, "mpl_InputExpression32", None)
                setattr(value, "mpl_InputExpression32", self)

class Expression:

    pass
class mpl_UnaryExpression(Expression):

    pass
class mpl_ArithmeticExpression(Expression):

    pass
class mpl_OperationExpression(Expression):

    pass
class mpl_AtomicExpression(Expression):

    pass
class mpl_InputExpression(Expression):

    pass
class mpl_ParenExpression(UnaryExpression):

    pass
class mpl_Form(ABC):

    pass
class mpl_Statement:

    pass
class mpl_Expression(ABC):

    pass
class mpl_Variable:

    def __init__(self, name: str, mpl_Variable: "mpl_VariableDeclaration" = None, mpl_Variable22: "mpl_VariableReference" = None, mpl_Variable60: "mpl_Operation" = None):
        self.name = name
        self.mpl_Variable = mpl_Variable
        self.mpl_Variable22 = mpl_Variable22
        self.mpl_Variable60 = mpl_Variable60
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mpl_Variable22(self):
        return self.__mpl_Variable22

    @mpl_Variable22.setter
    def mpl_Variable22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpl_Variable__mpl_Variable22", None)
        self.__mpl_Variable22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mpl_VariableReference21"):
                opp_val = getattr(old_value, "mpl_VariableReference21", None)
                if opp_val == self:
                    setattr(old_value, "mpl_VariableReference21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mpl_VariableReference21"):
                opp_val = getattr(value, "mpl_VariableReference21", None)
                setattr(value, "mpl_VariableReference21", self)

    @property
    def mpl_Variable60(self):
        return self.__mpl_Variable60

    @mpl_Variable60.setter
    def mpl_Variable60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpl_Variable__mpl_Variable60", None)
        self.__mpl_Variable60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mpl_Operation59"):
                opp_val = getattr(old_value, "mpl_Operation59", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mpl_Operation59"):
                opp_val = getattr(value, "mpl_Operation59", None)
                if opp_val is None:
                    setattr(value, "mpl_Operation59", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "mpl_VariableDeclaration7"):
                opp_val = getattr(old_value, "mpl_VariableDeclaration7", None)
                if opp_val == self:
                    setattr(old_value, "mpl_VariableDeclaration7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mpl_VariableDeclaration7"):
                opp_val = getattr(value, "mpl_VariableDeclaration7", None)
                setattr(value, "mpl_VariableDeclaration7", self)

class FunctionalUnit:

    pass
class mpl_Block:

    pass
class mpl_VariableDeclaration:

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

class mpl_Operation(FunctionalUnit):

    pass
class mpl_Program(FunctionalUnit):

    pass
class mpl_MPLModel:

    pass
class mpl_VariableReference(AtomicExpression):

    pass
class Form:

    pass
class mpl_ExpressionStatement(Form):

    pass
class mpl_TraceCall(Form):

    pass
class mpl_Return(Form):

    pass
class mpl_Loop(Form):

    pass
class mpl_If(Form):

    pass
class mpl_Assignment(Form):

    pass