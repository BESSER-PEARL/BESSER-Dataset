from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ArithmeticExpression:

    pass
class mpl_AddExpression(ArithmeticExpression):

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

class mpl_VariableRefrence(AtomicExpression):

    pass
class mpl_Expression(ABC):

    pass
class Statement:

    pass
class mpl_ExpressionStatement(Statement):

    pass
class mpl_Assignment(Statement):

    pass
class mpl_Variable:

    def __init__(self, name: str, mpl_Variable: "mpl_VariableDeclaration" = None, mpl_Variable17: "mpl_VariableRefrence" = None):
        self.name = name
        self.mpl_Variable = mpl_Variable
        self.mpl_Variable17 = mpl_Variable17
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "mpl_VariableDeclaration4"):
                opp_val = getattr(old_value, "mpl_VariableDeclaration4", None)
                if opp_val == self:
                    setattr(old_value, "mpl_VariableDeclaration4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mpl_VariableDeclaration4"):
                opp_val = getattr(value, "mpl_VariableDeclaration4", None)
                setattr(value, "mpl_VariableDeclaration4", self)

    @property
    def mpl_Variable17(self):
        return self.__mpl_Variable17

    @mpl_Variable17.setter
    def mpl_Variable17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpl_Variable__mpl_Variable17", None)
        self.__mpl_Variable17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mpl_VariableRefrence16"):
                opp_val = getattr(old_value, "mpl_VariableRefrence16", None)
                if opp_val == self:
                    setattr(old_value, "mpl_VariableRefrence16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mpl_VariableRefrence16"):
                opp_val = getattr(value, "mpl_VariableRefrence16", None)
                setattr(value, "mpl_VariableRefrence16", self)

class Expression:

    pass
class mpl_AtomicExpression(Expression):

    pass
class mpl_ArithmeticExpression(Expression):

    pass
class mpl_Statement(ABC):

    pass
class mpl_VariableDeclaration:

    pass
class mpl_Program:

    def __init__(self, name: str, mpl_Program: set["mpl_VariableDeclaration"] = None, mpl_Program2: set["mpl_Statement"] = None):
        self.name = name
        self.mpl_Program = mpl_Program if mpl_Program is not None else set()
        self.mpl_Program2 = mpl_Program2 if mpl_Program2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mpl_Program(self):
        return self.__mpl_Program

    @mpl_Program.setter
    def mpl_Program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpl_Program__mpl_Program", None)
        self.__mpl_Program = value if value is not None else set()
        
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
    def mpl_Program2(self):
        return self.__mpl_Program2

    @mpl_Program2.setter
    def mpl_Program2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mpl_Program__mpl_Program2", None)
        self.__mpl_Program2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mpl_Statement"):
                    opp_val = getattr(item, "mpl_Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "mpl_Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mpl_Statement"):
                    opp_val = getattr(item, "mpl_Statement", None)
                    
                    setattr(item, "mpl_Statement", self)
                    
