from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class wh_ExprNot:

    def __init__(self, not: str, wh_ExprNot35: "wh_ExprOr" = None, wh_ExprNot37: "wh_ExprEq" = None, wh_ExprNot: "wh_ExprOr" = None):
        self.not = not
        self.wh_ExprNot35 = wh_ExprNot35
        self.wh_ExprNot37 = wh_ExprNot37
        self.wh_ExprNot = wh_ExprNot
        
    @property
    def not(self) -> str:
        return self.__not

    @not.setter
    def not(self, not: str):
        self.__not = not

    @property
    def wh_ExprNot(self):
        return self.__wh_ExprNot

    @wh_ExprNot.setter
    def wh_ExprNot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_ExprNot__wh_ExprNot", None)
        self.__wh_ExprNot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_ExprOr32"):
                opp_val = getattr(old_value, "wh_ExprOr32", None)
                if opp_val == self:
                    setattr(old_value, "wh_ExprOr32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_ExprOr32"):
                opp_val = getattr(value, "wh_ExprOr32", None)
                setattr(value, "wh_ExprOr32", self)

    @property
    def wh_ExprNot37(self):
        return self.__wh_ExprNot37

    @wh_ExprNot37.setter
    def wh_ExprNot37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_ExprNot__wh_ExprNot37", None)
        self.__wh_ExprNot37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_ExprEq"):
                opp_val = getattr(old_value, "wh_ExprEq", None)
                if opp_val == self:
                    setattr(old_value, "wh_ExprEq", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_ExprEq"):
                opp_val = getattr(value, "wh_ExprEq", None)
                setattr(value, "wh_ExprEq", self)

    @property
    def wh_ExprNot35(self):
        return self.__wh_ExprNot35

    @wh_ExprNot35.setter
    def wh_ExprNot35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_ExprNot__wh_ExprNot35", None)
        self.__wh_ExprNot35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_ExprOr34"):
                opp_val = getattr(old_value, "wh_ExprOr34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_ExprOr34"):
                opp_val = getattr(value, "wh_ExprOr34", None)
                if opp_val is None:
                    setattr(value, "wh_ExprOr34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class wh_ExprOr:

    pass
class wh_ExprAnd:

    pass
class wh_ExprEq:

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
class wh_ListExpr:

    pass
class wh_Cons:

    pass
class wh_ExprSimple:

    def __init__(self, str: str, wh_ExprSimple: "wh_Cons" = None, wh_ExprSimple40: "wh_ExprEq" = None, wh_ExprSimple43: "wh_ExprEq" = None):
        self.str = str
        self.wh_ExprSimple = wh_ExprSimple
        self.wh_ExprSimple40 = wh_ExprSimple40
        self.wh_ExprSimple43 = wh_ExprSimple43
        
    @property
    def str(self) -> str:
        return self.__str

    @str.setter
    def str(self, str: str):
        self.__str = str

    @property
    def wh_ExprSimple40(self):
        return self.__wh_ExprSimple40

    @wh_ExprSimple40.setter
    def wh_ExprSimple40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_ExprSimple__wh_ExprSimple40", None)
        self.__wh_ExprSimple40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_ExprEq39"):
                opp_val = getattr(old_value, "wh_ExprEq39", None)
                if opp_val == self:
                    setattr(old_value, "wh_ExprEq39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_ExprEq39"):
                opp_val = getattr(value, "wh_ExprEq39", None)
                setattr(value, "wh_ExprEq39", self)

    @property
    def wh_ExprSimple43(self):
        return self.__wh_ExprSimple43

    @wh_ExprSimple43.setter
    def wh_ExprSimple43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_ExprSimple__wh_ExprSimple43", None)
        self.__wh_ExprSimple43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_ExprEq42"):
                opp_val = getattr(old_value, "wh_ExprEq42", None)
                if opp_val == self:
                    setattr(old_value, "wh_ExprEq42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_ExprEq42"):
                opp_val = getattr(value, "wh_ExprEq42", None)
                setattr(value, "wh_ExprEq42", self)

    @property
    def wh_ExprSimple(self):
        return self.__wh_ExprSimple

    @wh_ExprSimple.setter
    def wh_ExprSimple(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_ExprSimple__wh_ExprSimple", None)
        self.__wh_ExprSimple = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_Cons"):
                opp_val = getattr(old_value, "wh_Cons", None)
                if opp_val == self:
                    setattr(old_value, "wh_Cons", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_Cons"):
                opp_val = getattr(value, "wh_Cons", None)
                setattr(value, "wh_Cons", self)

class wh_Expr:

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

class wh_Wh:

    pass