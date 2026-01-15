from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class BinaryExp:

    pass
class fl_MinusExp(BinaryExp):

    pass
class fl_EqualExp(BinaryExp):

    pass
class fl_PlusExp(BinaryExp):

    pass
class fl_Argument:

    def __init__(self, name: str, fl_Argument: "fl_Function" = None, fl_Argument6: "fl_ArgumentExp" = None):
        self.name = name
        self.fl_Argument = fl_Argument
        self.fl_Argument6 = fl_Argument6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fl_Argument(self):
        return self.__fl_Argument

    @fl_Argument.setter
    def fl_Argument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fl_Argument__fl_Argument", None)
        self.__fl_Argument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fl_Function2"):
                opp_val = getattr(old_value, "fl_Function2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fl_Function2"):
                opp_val = getattr(value, "fl_Function2", None)
                if opp_val is None:
                    setattr(value, "fl_Function2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fl_Argument6(self):
        return self.__fl_Argument6

    @fl_Argument6.setter
    def fl_Argument6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fl_Argument__fl_Argument6", None)
        self.__fl_Argument6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fl_ArgumentExp"):
                opp_val = getattr(old_value, "fl_ArgumentExp", None)
                if opp_val == self:
                    setattr(old_value, "fl_ArgumentExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fl_ArgumentExp"):
                opp_val = getattr(value, "fl_ArgumentExp", None)
                setattr(value, "fl_ArgumentExp", self)

class fl_Function:

    def __init__(self, name: str, fl_Function4: "fl_Exp" = None, fl_Function: "fl_Program" = None, fl_Function2: set["fl_Argument"] = None, fl_Function16: "fl_ApplyExp" = None):
        self.name = name
        self.fl_Function4 = fl_Function4
        self.fl_Function = fl_Function
        self.fl_Function2 = fl_Function2 if fl_Function2 is not None else set()
        self.fl_Function16 = fl_Function16
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fl_Function16(self):
        return self.__fl_Function16

    @fl_Function16.setter
    def fl_Function16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fl_Function__fl_Function16", None)
        self.__fl_Function16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fl_ApplyExp"):
                opp_val = getattr(old_value, "fl_ApplyExp", None)
                if opp_val == self:
                    setattr(old_value, "fl_ApplyExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fl_ApplyExp"):
                opp_val = getattr(value, "fl_ApplyExp", None)
                setattr(value, "fl_ApplyExp", self)

    @property
    def fl_Function2(self):
        return self.__fl_Function2

    @fl_Function2.setter
    def fl_Function2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fl_Function__fl_Function2", None)
        self.__fl_Function2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fl_Argument"):
                    opp_val = getattr(item, "fl_Argument", None)
                    
                    if opp_val == self:
                        setattr(item, "fl_Argument", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fl_Argument"):
                    opp_val = getattr(item, "fl_Argument", None)
                    
                    setattr(item, "fl_Argument", self)
                    

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
            if hasattr(old_value, "fl_Program"):
                opp_val = getattr(old_value, "fl_Program", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fl_Program"):
                opp_val = getattr(value, "fl_Program", None)
                if opp_val is None:
                    setattr(value, "fl_Program", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fl_Function4(self):
        return self.__fl_Function4

    @fl_Function4.setter
    def fl_Function4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fl_Function__fl_Function4", None)
        self.__fl_Function4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fl_Exp"):
                opp_val = getattr(old_value, "fl_Exp", None)
                if opp_val == self:
                    setattr(old_value, "fl_Exp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fl_Exp"):
                opp_val = getattr(value, "fl_Exp", None)
                setattr(value, "fl_Exp", self)

class fl_Program:

    pass
class Exp:

    pass
class fl_IfThenElseExp(Exp):

    pass
class fl_BinaryExp(Exp):

    pass
class fl_ArgumentExp(Exp):

    pass
class fl_ApplyExp(Exp):

    pass
class fl_LiteralExp(Exp):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class fl_Exp(ABC):

    pass