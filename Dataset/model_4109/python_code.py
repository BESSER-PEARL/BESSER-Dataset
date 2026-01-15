from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ExprSimple:

    pass
class wh_cons(ExprSimple):

    def __init__(self, list: str):
        self.list = list
        
    @property
    def list(self) -> str:
        return self.__list

    @list.setter
    def list(self, list: str):
        self.__list = list

class Expr:

    pass
class wh_ExprSimple(Expr):

    pass
class wh_Expr:

    pass
class wh_Nop:

    def __init__(self, nop: str):
        self.nop = nop
        
    @property
    def nop(self) -> str:
        return self.__nop

    @nop.setter
    def nop(self, nop: str):
        self.__nop = nop

class wh_EObject:

    pass
class wh_Command:

    pass
class wh_Output:

    def __init__(self, vars: str, wh_Output: "wh_Definition" = None):
        self.vars = vars
        self.wh_Output = wh_Output
        
    @property
    def vars(self) -> str:
        return self.__vars

    @vars.setter
    def vars(self, vars: str):
        self.__vars = vars

    @property
    def wh_Output(self):
        return self.__wh_Output

    @wh_Output.setter
    def wh_Output(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_Output__wh_Output", None)
        self.__wh_Output = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_Definition8"):
                opp_val = getattr(old_value, "wh_Definition8", None)
                if opp_val == self:
                    setattr(old_value, "wh_Definition8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_Definition8"):
                opp_val = getattr(value, "wh_Definition8", None)
                setattr(value, "wh_Definition8", self)

class wh_Commands:

    pass
class wh_Input:

    def __init__(self, vars: str, wh_Input: "wh_Definition" = None):
        self.vars = vars
        self.wh_Input = wh_Input
        
    @property
    def vars(self) -> str:
        return self.__vars

    @vars.setter
    def vars(self, vars: str):
        self.__vars = vars

    @property
    def wh_Input(self):
        return self.__wh_Input

    @wh_Input.setter
    def wh_Input(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_Input__wh_Input", None)
        self.__wh_Input = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_Definition4"):
                opp_val = getattr(old_value, "wh_Definition4", None)
                if opp_val == self:
                    setattr(old_value, "wh_Definition4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_Definition4"):
                opp_val = getattr(value, "wh_Definition4", None)
                setattr(value, "wh_Definition4", self)

class wh_Definition:

    pass
class wh_Program:

    def __init__(self, name: str, wh_Program: "wh_Wh" = None, wh_Program2: "wh_Definition" = None):
        self.name = name
        self.wh_Program = wh_Program
        self.wh_Program2 = wh_Program2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def wh_Program(self):
        return self.__wh_Program

    @wh_Program.setter
    def wh_Program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_Program__wh_Program", None)
        self.__wh_Program = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_Wh"):
                opp_val = getattr(old_value, "wh_Wh", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_Wh"):
                opp_val = getattr(value, "wh_Wh", None)
                if opp_val is None:
                    setattr(value, "wh_Wh", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def wh_Program2(self):
        return self.__wh_Program2

    @wh_Program2.setter
    def wh_Program2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_Program__wh_Program2", None)
        self.__wh_Program2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_Definition"):
                opp_val = getattr(old_value, "wh_Definition", None)
                if opp_val == self:
                    setattr(old_value, "wh_Definition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_Definition"):
                opp_val = getattr(value, "wh_Definition", None)
                setattr(value, "wh_Definition", self)

class wh_Wh:

    pass
class wh_Exprs:

    pass
class wh_Vars:

    def __init__(self, vars: str, wh_Vars: "wh_Affect" = None):
        self.vars = vars
        self.wh_Vars = wh_Vars
        
    @property
    def vars(self) -> str:
        return self.__vars

    @vars.setter
    def vars(self, vars: str):
        self.__vars = vars

    @property
    def wh_Vars(self):
        return self.__wh_Vars

    @wh_Vars.setter
    def wh_Vars(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_Vars__wh_Vars", None)
        self.__wh_Vars = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_Affect"):
                opp_val = getattr(old_value, "wh_Affect", None)
                if opp_val == self:
                    setattr(old_value, "wh_Affect", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_Affect"):
                opp_val = getattr(value, "wh_Affect", None)
                setattr(value, "wh_Affect", self)

class wh_Affect:

    pass