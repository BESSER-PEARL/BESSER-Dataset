from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class simpleALEnv_EqualityTest:

    pass
class Stmt:

    pass
class simpleALEnv_Assign(Stmt):

    def __init__(self, name: str, simpleALEnv_Assign: "simpleALEnv_Arith" = None, simpleALEnv_Assign8: "simpleALEnv_IfStmt" = None, simpleALEnv_Assign11: "simpleALEnv_IfStmt" = None):
        self.name = name
        self.simpleALEnv_Assign = simpleALEnv_Assign
        self.simpleALEnv_Assign8 = simpleALEnv_Assign8
        self.simpleALEnv_Assign11 = simpleALEnv_Assign11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simpleALEnv_Assign11(self):
        return self.__simpleALEnv_Assign11

    @simpleALEnv_Assign11.setter
    def simpleALEnv_Assign11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleALEnv_Assign__simpleALEnv_Assign11", None)
        self.__simpleALEnv_Assign11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleALEnv_IfStmt10"):
                opp_val = getattr(old_value, "simpleALEnv_IfStmt10", None)
                if opp_val == self:
                    setattr(old_value, "simpleALEnv_IfStmt10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleALEnv_IfStmt10"):
                opp_val = getattr(value, "simpleALEnv_IfStmt10", None)
                setattr(value, "simpleALEnv_IfStmt10", self)

    @property
    def simpleALEnv_Assign(self):
        return self.__simpleALEnv_Assign

    @simpleALEnv_Assign.setter
    def simpleALEnv_Assign(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleALEnv_Assign__simpleALEnv_Assign", None)
        self.__simpleALEnv_Assign = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleALEnv_Arith6"):
                opp_val = getattr(old_value, "simpleALEnv_Arith6", None)
                if opp_val == self:
                    setattr(old_value, "simpleALEnv_Arith6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleALEnv_Arith6"):
                opp_val = getattr(value, "simpleALEnv_Arith6", None)
                setattr(value, "simpleALEnv_Arith6", self)

    @property
    def simpleALEnv_Assign8(self):
        return self.__simpleALEnv_Assign8

    @simpleALEnv_Assign8.setter
    def simpleALEnv_Assign8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleALEnv_Assign__simpleALEnv_Assign8", None)
        self.__simpleALEnv_Assign8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleALEnv_IfStmt"):
                opp_val = getattr(old_value, "simpleALEnv_IfStmt", None)
                if opp_val == self:
                    setattr(old_value, "simpleALEnv_IfStmt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleALEnv_IfStmt"):
                opp_val = getattr(value, "simpleALEnv_IfStmt", None)
                setattr(value, "simpleALEnv_IfStmt", self)

class simpleALEnv_IfStmt(Stmt):

    pass
class simpleALEnv_Print(Stmt):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class ArithOp:

    pass
class simpleALEnv_ArithMinus(ArithOp):

    pass
class simpleALEnv_ArithPlus(ArithOp):

    pass
class Arith:

    pass
class simpleALEnv_ArithLit(Arith):

    def __init__(self, val: int):
        self.val = val
        
    @property
    def val(self) -> int:
        return self.__val

    @val.setter
    def val(self, val: int):
        self.__val = val

class simpleALEnv_RandRange(Arith):

    def __init__(self, min: int, max: int):
        self.min = min
        self.max = max
        
    @property
    def max(self) -> int:
        return self.__max

    @max.setter
    def max(self, max: int):
        self.__max = max

    @property
    def min(self) -> int:
        return self.__min

    @min.setter
    def min(self, min: int):
        self.__min = min

class simpleALEnv_ArithOp(Arith):

    pass
class simpleALEnv_ALVarRef(Arith):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class simpleALEnv_Arith(ABC):

    pass
class simpleALEnv_Stmt(ABC):

    pass
class simpleALEnv_Block:

    pass