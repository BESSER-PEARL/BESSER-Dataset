from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Stmt:

    pass
class simpleal_Assign(Stmt):

    def __init__(self, name: str, simpleal_Assign: "simpleal_Arith" = None):
        self.name = name
        self.simpleal_Assign = simpleal_Assign
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simpleal_Assign(self):
        return self.__simpleal_Assign

    @simpleal_Assign.setter
    def simpleal_Assign(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleal_Assign__simpleal_Assign", None)
        self.__simpleal_Assign = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleal_Arith6"):
                opp_val = getattr(old_value, "simpleal_Arith6", None)
                if opp_val == self:
                    setattr(old_value, "simpleal_Arith6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleal_Arith6"):
                opp_val = getattr(value, "simpleal_Arith6", None)
                setattr(value, "simpleal_Arith6", self)

class simpleal_Print(Stmt):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Arith:

    pass
class simpleal_ArithLit(Arith):

    def __init__(self, val: int):
        self.val = val
        
    @property
    def val(self) -> int:
        return self.__val

    @val.setter
    def val(self, val: int):
        self.__val = val

class simpleal_VarRef(Arith):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class simpleal_Arith(ABC):

    pass
class simpleal_Stmt(ABC):

    pass
class simpleal_Block:

    pass
class ArithOp:

    pass
class simpleal_ArithMinus(ArithOp):

    pass
class simpleal_ArithPlus(ArithOp):

    pass
class simpleal_ArithOp(Arith):

    pass