from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class mpl_Operation(ABC):

    def __init__(self, name: str, mpl_Operation66: "mpl_MPLModel" = None, mpl_Operation: set["mpl_VariableDeclaration"] = None, mpl_Operation51: set["mpl_VariableDeclaration"] = None, mpl_Operation54: "mpl_Block" = None, mpl_Operation62: "mpl_OperationCall" = None):
        self.name = name
        self.mpl_Operation66 = mpl_Operation66
        self.mpl_Operation = mpl_Operation if mpl_Operation is not None else set()
        self.mpl_Operation51 = mpl_Operation51 if mpl_Operation51 is not None else set()
        self.mpl_Operation54 = mpl_Operation54
        self.mpl_Operation62 = mpl_Operation62
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mpl_Operation62(self):
        return self.__mpl_Operation62

    @mpl_Operation62.setter
    def mpl_Operation62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpl_Operation__mpl_Operation62", None)
        self.__mpl_Operation62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mpl_OperationCall61"):
                opp_val = getattr(old_value, "mpl_OperationCall61", None)
                if opp_val == self:
                    setattr(old_value, "mpl_OperationCall61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mpl_OperationCall61"):
                opp_val = getattr(value, "mpl_OperationCall61", None)
                setattr(value, "mpl_OperationCall61", self)

    @property
    def mpl_Operation66(self):
        return self.__mpl_Operation66

    @mpl_Operation66.setter
    def mpl_Operation66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpl_Operation__mpl_Operation66", None)
        self.__mpl_Operation66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mpl_MPLModel65"):
                opp_val = getattr(old_value, "mpl_MPLModel65", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mpl_MPLModel65"):
                opp_val = getattr(value, "mpl_MPLModel65", None)
                if opp_val is None:
                    setattr(value, "mpl_MPLModel65", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mpl_Operation51(self):
        return self.__mpl_Operation51

    @mpl_Operation51.setter
    def mpl_Operation51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpl_Operation__mpl_Operation51", None)
        self.__mpl_Operation51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mpl_VariableDeclaration52"):
                    opp_val = getattr(item, "mpl_VariableDeclaration52", None)
                    
                    if opp_val == self:
                        setattr(item, "mpl_VariableDeclaration52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mpl_VariableDeclaration52"):
                    opp_val = getattr(item, "mpl_VariableDeclaration52", None)
                    
                    setattr(item, "mpl_VariableDeclaration52", self)
                    

    @property
    def mpl_Operation54(self):
        return self.__mpl_Operation54

    @mpl_Operation54.setter
    def mpl_Operation54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpl_Operation__mpl_Operation54", None)
        self.__mpl_Operation54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mpl_Block55"):
                opp_val = getattr(old_value, "mpl_Block55", None)
                if opp_val == self:
                    setattr(old_value, "mpl_Block55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mpl_Block55"):
                opp_val = getattr(value, "mpl_Block55", None)
                setattr(value, "mpl_Block55", self)

    @property
    def mpl_Operation(self):
        return self.__mpl_Operation

    @mpl_Operation.setter
    def mpl_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpl_Operation__mpl_Operation", None)
        self.__mpl_Operation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mpl_VariableDeclaration49"):
                    opp_val = getattr(item, "mpl_VariableDeclaration49", None)
                    
                    if opp_val == self:
                        setattr(item, "mpl_VariableDeclaration49", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mpl_VariableDeclaration49"):
                    opp_val = getattr(item, "mpl_VariableDeclaration49", None)
                    
                    setattr(item, "mpl_VariableDeclaration49", self)
                    

class mpl_MPLModel:

    pass
class mpl_Comparison:

    def __init__(self, operator: str, mpl_Comparison37: "mpl_WhileLoop" = None, mpl_Comparison: "mpl_IfStatement" = None, mpl_Comparison28: "mpl_Expression" = None, mpl_Comparison31: "mpl_Expression" = None):
        self.operator = operator
        self.mpl_Comparison37 = mpl_Comparison37
        self.mpl_Comparison = mpl_Comparison
        self.mpl_Comparison28 = mpl_Comparison28
        self.mpl_Comparison31 = mpl_Comparison31
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def mpl_Comparison(self):
        return self.__mpl_Comparison

    @mpl_Comparison.setter
    def mpl_Comparison(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpl_Comparison__mpl_Comparison", None)
        self.__mpl_Comparison = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mpl_IfStatement26"):
                opp_val = getattr(old_value, "mpl_IfStatement26", None)
                if opp_val == self:
                    setattr(old_value, "mpl_IfStatement26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mpl_IfStatement26"):
                opp_val = getattr(value, "mpl_IfStatement26", None)
                setattr(value, "mpl_IfStatement26", self)

    @property
    def mpl_Comparison37(self):
        return self.__mpl_Comparison37

    @mpl_Comparison37.setter
    def mpl_Comparison37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpl_Comparison__mpl_Comparison37", None)
        self.__mpl_Comparison37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mpl_WhileLoop36"):
                opp_val = getattr(old_value, "mpl_WhileLoop36", None)
                if opp_val == self:
                    setattr(old_value, "mpl_WhileLoop36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mpl_WhileLoop36"):
                opp_val = getattr(value, "mpl_WhileLoop36", None)
                setattr(value, "mpl_WhileLoop36", self)

    @property
    def mpl_Comparison31(self):
        return self.__mpl_Comparison31

    @mpl_Comparison31.setter
    def mpl_Comparison31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpl_Comparison__mpl_Comparison31", None)
        self.__mpl_Comparison31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mpl_Expression32"):
                opp_val = getattr(old_value, "mpl_Expression32", None)
                if opp_val == self:
                    setattr(old_value, "mpl_Expression32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mpl_Expression32"):
                opp_val = getattr(value, "mpl_Expression32", None)
                setattr(value, "mpl_Expression32", self)

    @property
    def mpl_Comparison28(self):
        return self.__mpl_Comparison28

    @mpl_Comparison28.setter
    def mpl_Comparison28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpl_Comparison__mpl_Comparison28", None)
        self.__mpl_Comparison28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mpl_Expression29"):
                opp_val = getattr(old_value, "mpl_Expression29", None)
                if opp_val == self:
                    setattr(old_value, "mpl_Expression29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mpl_Expression29"):
                opp_val = getattr(value, "mpl_Expression29", None)
                setattr(value, "mpl_Expression29", self)

class mpl_Block:

    pass
class UnaryExpression:

    pass
class mpl_UnaryMinusExpression(UnaryExpression):

    pass
class BinaryExpression:

    pass
class mpl_MultExpression(BinaryExpression):

    pass
class mpl_DivExpression(BinaryExpression):

    pass
class mpl_SubExpression(BinaryExpression):

    pass
class mpl_AddExpression(BinaryExpression):

    pass
class AtomicExpression:

    pass
class mpl_OperationCall(AtomicExpression):

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
class mpl_UnaryExpression(Expression):

    pass
class mpl_AtomicExpression(Expression):

    pass
class Statement:

    pass
class mpl_TraceStatement(Statement):

    pass
class mpl_WhileLoop(Statement):

    pass
class mpl_ReturnStatement(Statement):

    pass
class mpl_ForLoop(Statement):

    def __init__(self, increment: bool, mpl_ForLoop: "mpl_Block" = None, mpl_ForLoop41: "mpl_Assignment" = None, mpl_ForLoop44: "mpl_Expression" = None):
        self.increment = increment
        self.mpl_ForLoop = mpl_ForLoop
        self.mpl_ForLoop41 = mpl_ForLoop41
        self.mpl_ForLoop44 = mpl_ForLoop44
        
    @property
    def increment(self) -> bool:
        return self.__increment

    @increment.setter
    def increment(self, increment: bool):
        self.__increment = increment

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
            if hasattr(old_value, "mpl_Block39"):
                opp_val = getattr(old_value, "mpl_Block39", None)
                if opp_val == self:
                    setattr(old_value, "mpl_Block39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mpl_Block39"):
                opp_val = getattr(value, "mpl_Block39", None)
                setattr(value, "mpl_Block39", self)

    @property
    def mpl_ForLoop41(self):
        return self.__mpl_ForLoop41

    @mpl_ForLoop41.setter
    def mpl_ForLoop41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpl_ForLoop__mpl_ForLoop41", None)
        self.__mpl_ForLoop41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mpl_Assignment42"):
                opp_val = getattr(old_value, "mpl_Assignment42", None)
                if opp_val == self:
                    setattr(old_value, "mpl_Assignment42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mpl_Assignment42"):
                opp_val = getattr(value, "mpl_Assignment42", None)
                setattr(value, "mpl_Assignment42", self)

    @property
    def mpl_ForLoop44(self):
        return self.__mpl_ForLoop44

    @mpl_ForLoop44.setter
    def mpl_ForLoop44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpl_ForLoop__mpl_ForLoop44", None)
        self.__mpl_ForLoop44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mpl_Expression45"):
                opp_val = getattr(old_value, "mpl_Expression45", None)
                if opp_val == self:
                    setattr(old_value, "mpl_Expression45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mpl_Expression45"):
                opp_val = getattr(value, "mpl_Expression45", None)
                setattr(value, "mpl_Expression45", self)

class mpl_AssignmentStatement(Statement):

    pass
class mpl_IfStatement(Statement):

    pass
class mpl_ExpressionStatement(Statement):

    pass
class mpl_VariableReference(AtomicExpression):

    pass
class mpl_Assignment:

    pass
class mpl_BinaryExpression(Expression):

    pass
class mpl_ParenthesisExpression(UnaryExpression):

    pass
class mpl_Variable:

    def __init__(self, name: str, value: int, mpl_Variable: "mpl_VariableDeclaration" = None, mpl_Variable11: "mpl_VariableReference" = None):
        self.name = name
        self.value = value
        self.mpl_Variable = mpl_Variable
        self.mpl_Variable11 = mpl_Variable11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

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
            if hasattr(old_value, "mpl_VariableDeclaration"):
                opp_val = getattr(old_value, "mpl_VariableDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "mpl_VariableDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mpl_VariableDeclaration"):
                opp_val = getattr(value, "mpl_VariableDeclaration", None)
                setattr(value, "mpl_VariableDeclaration", self)

    @property
    def mpl_Variable11(self):
        return self.__mpl_Variable11

    @mpl_Variable11.setter
    def mpl_Variable11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpl_Variable__mpl_Variable11", None)
        self.__mpl_Variable11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mpl_VariableReference10"):
                opp_val = getattr(old_value, "mpl_VariableReference10", None)
                if opp_val == self:
                    setattr(old_value, "mpl_VariableReference10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mpl_VariableReference10"):
                opp_val = getattr(value, "mpl_VariableReference10", None)
                setattr(value, "mpl_VariableReference10", self)

class mpl_VariableDeclaration:

    pass
class Operation:

    pass
class mpl_Function(Operation):

    pass
class mpl_Procedure(Operation):

    pass
class mpl_Program(Operation):

    pass
class mpl_Statement(ABC):

    pass
class mpl_Expression(ABC):

    pass