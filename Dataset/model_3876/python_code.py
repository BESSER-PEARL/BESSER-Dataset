from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Ops(Enum):
    Equal = "Equal"
    Plus = "Plus"
    Minus = "Minus"


############################################
# Definition of Classes
############################################

class fl_ProgramType:

    pass
class fl_EStringToStringMapEntry:

    pass
class fl_DocumentRoot:

    def __init__(self, mixed: str, fl_DocumentRoot: set["fl_EStringToStringMapEntry"] = None, fl_DocumentRoot8: set["fl_EStringToStringMapEntry"] = None, fl_DocumentRoot11: set["fl_Expr"] = None, fl_DocumentRoot14: set["fl_ProgramType"] = None):
        self.mixed = mixed
        self.fl_DocumentRoot = fl_DocumentRoot if fl_DocumentRoot is not None else set()
        self.fl_DocumentRoot8 = fl_DocumentRoot8 if fl_DocumentRoot8 is not None else set()
        self.fl_DocumentRoot11 = fl_DocumentRoot11 if fl_DocumentRoot11 is not None else set()
        self.fl_DocumentRoot14 = fl_DocumentRoot14 if fl_DocumentRoot14 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def fl_DocumentRoot11(self):
        return self.__fl_DocumentRoot11

    @fl_DocumentRoot11.setter
    def fl_DocumentRoot11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fl_DocumentRoot__fl_DocumentRoot11", None)
        self.__fl_DocumentRoot11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fl_Expr12"):
                    opp_val = getattr(item, "fl_Expr12", None)
                    
                    if opp_val == self:
                        setattr(item, "fl_Expr12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fl_Expr12"):
                    opp_val = getattr(item, "fl_Expr12", None)
                    
                    setattr(item, "fl_Expr12", self)
                    

    @property
    def fl_DocumentRoot14(self):
        return self.__fl_DocumentRoot14

    @fl_DocumentRoot14.setter
    def fl_DocumentRoot14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fl_DocumentRoot__fl_DocumentRoot14", None)
        self.__fl_DocumentRoot14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fl_ProgramType"):
                    opp_val = getattr(item, "fl_ProgramType", None)
                    
                    if opp_val == self:
                        setattr(item, "fl_ProgramType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fl_ProgramType"):
                    opp_val = getattr(item, "fl_ProgramType", None)
                    
                    setattr(item, "fl_ProgramType", self)
                    

    @property
    def fl_DocumentRoot(self):
        return self.__fl_DocumentRoot

    @fl_DocumentRoot.setter
    def fl_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fl_DocumentRoot__fl_DocumentRoot", None)
        self.__fl_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fl_EStringToStringMapEntry"):
                    opp_val = getattr(item, "fl_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "fl_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fl_EStringToStringMapEntry"):
                    opp_val = getattr(item, "fl_EStringToStringMapEntry", None)
                    
                    setattr(item, "fl_EStringToStringMapEntry", self)
                    

    @property
    def fl_DocumentRoot8(self):
        return self.__fl_DocumentRoot8

    @fl_DocumentRoot8.setter
    def fl_DocumentRoot8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fl_DocumentRoot__fl_DocumentRoot8", None)
        self.__fl_DocumentRoot8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fl_EStringToStringMapEntry9"):
                    opp_val = getattr(item, "fl_EStringToStringMapEntry9", None)
                    
                    if opp_val == self:
                        setattr(item, "fl_EStringToStringMapEntry9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fl_EStringToStringMapEntry9"):
                    opp_val = getattr(item, "fl_EStringToStringMapEntry9", None)
                    
                    setattr(item, "fl_EStringToStringMapEntry9", self)
                    

class fl_Function:

    def __init__(self, name: str, arg: str, fl_Function27: "fl_ProgramType" = None, fl_Function: "fl_Expr" = None):
        self.name = name
        self.arg = arg
        self.fl_Function27 = fl_Function27
        self.fl_Function = fl_Function
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def arg(self) -> str:
        return self.__arg

    @arg.setter
    def arg(self, arg: str):
        self.__arg = arg

    @property
    def fl_Function(self):
        return self.__fl_Function

    @fl_Function.setter
    def fl_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fl_Function__fl_Function", None)
        self.__fl_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fl_Expr16"):
                opp_val = getattr(old_value, "fl_Expr16", None)
                if opp_val == self:
                    setattr(old_value, "fl_Expr16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fl_Expr16"):
                opp_val = getattr(value, "fl_Expr16", None)
                setattr(value, "fl_Expr16", self)

    @property
    def fl_Function27(self):
        return self.__fl_Function27

    @fl_Function27.setter
    def fl_Function27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fl_Function__fl_Function27", None)
        self.__fl_Function27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fl_ProgramType26"):
                opp_val = getattr(old_value, "fl_ProgramType26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fl_ProgramType26"):
                opp_val = getattr(value, "fl_ProgramType26", None)
                if opp_val is None:
                    setattr(value, "fl_ProgramType26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fl_Expr(ABC):

    pass
class Expr:

    pass
class fl_IfThenElse(Expr):

    pass
class fl_Literal(Expr):

    def __init__(self, info: str):
        self.info = info
        
    @property
    def info(self) -> str:
        return self.__info

    @info.setter
    def info(self, info: str):
        self.__info = info

class fl_Argument(Expr):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class fl_Apply(Expr):

    def __init__(self, name: str, fl_Apply: set["fl_Expr"] = None):
        self.name = name
        self.fl_Apply = fl_Apply if fl_Apply is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fl_Apply(self):
        return self.__fl_Apply

    @fl_Apply.setter
    def fl_Apply(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fl_Apply__fl_Apply", None)
        self.__fl_Apply = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fl_Expr"):
                    opp_val = getattr(item, "fl_Expr", None)
                    
                    if opp_val == self:
                        setattr(item, "fl_Expr", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fl_Expr"):
                    opp_val = getattr(item, "fl_Expr", None)
                    
                    setattr(item, "fl_Expr", self)
                    

class fl_Binary(Expr):

    def __init__(self, ops: str, fl_Binary: "fl_Expr" = None, fl_Binary4: "fl_Expr" = None):
        self.ops = ops
        self.fl_Binary = fl_Binary
        self.fl_Binary4 = fl_Binary4
        
    @property
    def ops(self) -> str:
        return self.__ops

    @ops.setter
    def ops(self, ops: str):
        self.__ops = ops

    @property
    def fl_Binary(self):
        return self.__fl_Binary

    @fl_Binary.setter
    def fl_Binary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fl_Binary__fl_Binary", None)
        self.__fl_Binary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fl_Expr2"):
                opp_val = getattr(old_value, "fl_Expr2", None)
                if opp_val == self:
                    setattr(old_value, "fl_Expr2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fl_Expr2"):
                opp_val = getattr(value, "fl_Expr2", None)
                setattr(value, "fl_Expr2", self)

    @property
    def fl_Binary4(self):
        return self.__fl_Binary4

    @fl_Binary4.setter
    def fl_Binary4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fl_Binary__fl_Binary4", None)
        self.__fl_Binary4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fl_Expr5"):
                opp_val = getattr(old_value, "fl_Expr5", None)
                if opp_val == self:
                    setattr(old_value, "fl_Expr5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fl_Expr5"):
                opp_val = getattr(value, "fl_Expr5", None)
                setattr(value, "fl_Expr5", self)
