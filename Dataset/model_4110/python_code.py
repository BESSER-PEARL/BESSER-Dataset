from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Expr:

    pass
class wh_ExprSym(Expr):

    def __init__(self, arg1: str, wh_ExprSym: set["wh_Expr"] = None):
        self.arg1 = arg1
        self.wh_ExprSym = wh_ExprSym if wh_ExprSym is not None else set()
        
    @property
    def arg1(self) -> str:
        return self.__arg1

    @arg1.setter
    def arg1(self, arg1: str):
        self.__arg1 = arg1

    @property
    def wh_ExprSym(self):
        return self.__wh_ExprSym

    @wh_ExprSym.setter
    def wh_ExprSym(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_ExprSym__wh_ExprSym", None)
        self.__wh_ExprSym = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wh_Expr55"):
                    opp_val = getattr(item, "wh_Expr55", None)
                    
                    if opp_val == self:
                        setattr(item, "wh_Expr55", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wh_Expr55"):
                    opp_val = getattr(item, "wh_Expr55", None)
                    
                    setattr(item, "wh_Expr55", self)
                    

class wh_ExprAnd(Expr):

    pass
class wh_ExprEq(Expr):

    pass
class wh_ExprNot(Expr):

    pass
class wh_ExprSimple(Expr):

    def __init__(self, str: str, varSimple: str, sym: str, wh_ExprSimple42: "wh_ExprOr" = None, wh_ExprSimple: "wh_ExprAnd" = None, wh_ExprSimple59: "wh_ExprEq" = None, wh_ExprSimple62: "wh_ExprEq" = None):
        self.str = str
        self.varSimple = varSimple
        self.sym = sym
        self.wh_ExprSimple42 = wh_ExprSimple42
        self.wh_ExprSimple = wh_ExprSimple
        self.wh_ExprSimple59 = wh_ExprSimple59
        self.wh_ExprSimple62 = wh_ExprSimple62
        
    @property
    def sym(self) -> str:
        return self.__sym

    @sym.setter
    def sym(self, sym: str):
        self.__sym = sym

    @property
    def varSimple(self) -> str:
        return self.__varSimple

    @varSimple.setter
    def varSimple(self, varSimple: str):
        self.__varSimple = varSimple

    @property
    def str(self) -> str:
        return self.__str

    @str.setter
    def str(self, str: str):
        self.__str = str

    @property
    def wh_ExprSimple62(self):
        return self.__wh_ExprSimple62

    @wh_ExprSimple62.setter
    def wh_ExprSimple62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_ExprSimple__wh_ExprSimple62", None)
        self.__wh_ExprSimple62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_ExprEq61"):
                opp_val = getattr(old_value, "wh_ExprEq61", None)
                if opp_val == self:
                    setattr(old_value, "wh_ExprEq61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_ExprEq61"):
                opp_val = getattr(value, "wh_ExprEq61", None)
                setattr(value, "wh_ExprEq61", self)

    @property
    def wh_ExprSimple59(self):
        return self.__wh_ExprSimple59

    @wh_ExprSimple59.setter
    def wh_ExprSimple59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_ExprSimple__wh_ExprSimple59", None)
        self.__wh_ExprSimple59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_ExprEq58"):
                opp_val = getattr(old_value, "wh_ExprEq58", None)
                if opp_val == self:
                    setattr(old_value, "wh_ExprEq58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_ExprEq58"):
                opp_val = getattr(value, "wh_ExprEq58", None)
                setattr(value, "wh_ExprEq58", self)

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
            if hasattr(old_value, "wh_ExprAnd"):
                opp_val = getattr(old_value, "wh_ExprAnd", None)
                if opp_val == self:
                    setattr(old_value, "wh_ExprAnd", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_ExprAnd"):
                opp_val = getattr(value, "wh_ExprAnd", None)
                setattr(value, "wh_ExprAnd", self)

    @property
    def wh_ExprSimple42(self):
        return self.__wh_ExprSimple42

    @wh_ExprSimple42.setter
    def wh_ExprSimple42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_ExprSimple__wh_ExprSimple42", None)
        self.__wh_ExprSimple42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_ExprOr"):
                opp_val = getattr(old_value, "wh_ExprOr", None)
                if opp_val == self:
                    setattr(old_value, "wh_ExprOr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_ExprOr"):
                opp_val = getattr(value, "wh_ExprOr", None)
                setattr(value, "wh_ExprOr", self)

class wh_While:

    pass
class wh_For:

    pass
class wh_ExprTl(Expr):

    pass
class wh_ExprHd(Expr):

    pass
class wh_ExprList(Expr):

    pass
class wh_ExprCons(Expr):

    pass
class wh_ExprOr(Expr):

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
            if hasattr(old_value, "wh_Definition10"):
                opp_val = getattr(old_value, "wh_Definition10", None)
                if opp_val == self:
                    setattr(old_value, "wh_Definition10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_Definition10"):
                opp_val = getattr(value, "wh_Definition10", None)
                setattr(value, "wh_Definition10", self)

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
            if hasattr(old_value, "wh_Definition6"):
                opp_val = getattr(old_value, "wh_Definition6", None)
                if opp_val == self:
                    setattr(old_value, "wh_Definition6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_Definition6"):
                opp_val = getattr(value, "wh_Definition6", None)
                setattr(value, "wh_Definition6", self)

class wh_Definition:

    pass
class wh_Function:

    def __init__(self, name: str, wh_Function: "wh_Program" = None, wh_Function4: "wh_Definition" = None):
        self.name = name
        self.wh_Function = wh_Function
        self.wh_Function4 = wh_Function4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def wh_Function4(self):
        return self.__wh_Function4

    @wh_Function4.setter
    def wh_Function4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_Function__wh_Function4", None)
        self.__wh_Function4 = value
        
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
    def wh_Function(self):
        return self.__wh_Function

    @wh_Function.setter
    def wh_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_Function__wh_Function", None)
        self.__wh_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_Program2"):
                opp_val = getattr(old_value, "wh_Program2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_Program2"):
                opp_val = getattr(value, "wh_Program2", None)
                if opp_val is None:
                    setattr(value, "wh_Program2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class wh_Program:

    pass
class wh_Wh:

    pass
class wh_Affect:

    def __init__(self, vars: str, wh_Affect: set["wh_Expr"] = None):
        self.vars = vars
        self.wh_Affect = wh_Affect if wh_Affect is not None else set()
        
    @property
    def vars(self) -> str:
        return self.__vars

    @vars.setter
    def vars(self, vars: str):
        self.__vars = vars

    @property
    def wh_Affect(self):
        return self.__wh_Affect

    @wh_Affect.setter
    def wh_Affect(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_Affect__wh_Affect", None)
        self.__wh_Affect = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wh_Expr23"):
                    opp_val = getattr(item, "wh_Expr23", None)
                    
                    if opp_val == self:
                        setattr(item, "wh_Expr23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wh_Expr23"):
                    opp_val = getattr(item, "wh_Expr23", None)
                    
                    setattr(item, "wh_Expr23", self)
                    

class wh_Nop:

    def __init__(self, nop: str):
        self.nop = nop
        
    @property
    def nop(self) -> str:
        return self.__nop

    @nop.setter
    def nop(self, nop: str):
        self.__nop = nop

class wh_Expr:

    pass
class wh_If:

    pass
class wh_EObject:

    pass
class wh_Command:

    pass