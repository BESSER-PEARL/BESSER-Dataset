from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class BoolExp:

    pass
class BinaryExp:

    pass
class while_EqExp(BoolExp, BinaryExp):

    pass
class while_AndExp(BoolExp, BinaryExp):

    pass
class while_Exp(ABC):

    pass
class Exp:

    pass
class while_VarExp(Exp):

    pass
class while_BinaryExp(Exp):

    pass
class while_NEqExp(BoolExp, BinaryExp):

    pass
class while_Val(Exp):

    def __init__(self, id: str, while_Val: "while_Program" = None):
        self.id = id
        self.while_Val = while_Val
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def while_Val(self):
        return self.__while_Val

    @while_Val.setter
    def while_Val(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_while_Val__while_Val", None)
        self.__while_Val = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "while_Program4"):
                opp_val = getattr(old_value, "while_Program4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "while_Program4"):
                opp_val = getattr(value, "while_Program4", None)
                if opp_val is None:
                    setattr(value, "while_Program4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class while_Var:

    def __init__(self, id: str, while_Var: "while_Program" = None, while_Var25: "while_VarExp" = None, while_Var27: "while_Assignment" = None):
        self.id = id
        self.while_Var = while_Var
        self.while_Var25 = while_Var25
        self.while_Var27 = while_Var27
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def while_Var25(self):
        return self.__while_Var25

    @while_Var25.setter
    def while_Var25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_while_Var__while_Var25", None)
        self.__while_Var25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "while_VarExp"):
                opp_val = getattr(old_value, "while_VarExp", None)
                if opp_val == self:
                    setattr(old_value, "while_VarExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "while_VarExp"):
                opp_val = getattr(value, "while_VarExp", None)
                setattr(value, "while_VarExp", self)

    @property
    def while_Var27(self):
        return self.__while_Var27

    @while_Var27.setter
    def while_Var27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_while_Var__while_Var27", None)
        self.__while_Var27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "while_Assignment"):
                opp_val = getattr(old_value, "while_Assignment", None)
                if opp_val == self:
                    setattr(old_value, "while_Assignment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "while_Assignment"):
                opp_val = getattr(value, "while_Assignment", None)
                setattr(value, "while_Assignment", self)

    @property
    def while_Var(self):
        return self.__while_Var

    @while_Var.setter
    def while_Var(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_while_Var__while_Var", None)
        self.__while_Var = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "while_Program2"):
                opp_val = getattr(old_value, "while_Program2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "while_Program2"):
                opp_val = getattr(value, "while_Program2", None)
                if opp_val is None:
                    setattr(value, "while_Program2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class while_Statement(ABC):

    pass
class while_Program:

    pass
class while_BoolExp(Exp):

    pass
class Statement:

    pass
class while_Ret(Statement):

    pass
class while_Assignment(Statement):

    pass
class while_If(Statement):

    pass
class while_While(Statement):

    pass