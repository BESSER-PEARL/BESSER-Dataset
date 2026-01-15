from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class py_ExprList:

    pass
class py_ExprEq:

    pass
class py_ExprNot:

    pass
class py_ExprSym:

    def __init__(self, arg1: str, py_ExprSym: set["py_Expr"] = None):
        self.arg1 = arg1
        self.py_ExprSym = py_ExprSym if py_ExprSym is not None else set()
        
    @property
    def arg1(self) -> str:
        return self.__arg1

    @arg1.setter
    def arg1(self, arg1: str):
        self.__arg1 = arg1

    @property
    def py_ExprSym(self):
        return self.__py_ExprSym

    @py_ExprSym.setter
    def py_ExprSym(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_py_ExprSym__py_ExprSym", None)
        self.__py_ExprSym = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "py_Expr62"):
                    opp_val = getattr(item, "py_Expr62", None)
                    
                    if opp_val == self:
                        setattr(item, "py_Expr62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "py_Expr62"):
                    opp_val = getattr(item, "py_Expr62", None)
                    
                    setattr(item, "py_Expr62", self)
                    

class py_ExprTl:

    pass
class py_ExprHd:

    pass
class py_For:

    pass
class py_Affect:

    def __init__(self, vars: str, py_Affect: set["py_Expr"] = None):
        self.vars = vars
        self.py_Affect = py_Affect if py_Affect is not None else set()
        
    @property
    def vars(self) -> str:
        return self.__vars

    @vars.setter
    def vars(self, vars: str):
        self.__vars = vars

    @property
    def py_Affect(self):
        return self.__py_Affect

    @py_Affect.setter
    def py_Affect(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_py_Affect__py_Affect", None)
        self.__py_Affect = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "py_Expr23"):
                    opp_val = getattr(item, "py_Expr23", None)
                    
                    if opp_val == self:
                        setattr(item, "py_Expr23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "py_Expr23"):
                    opp_val = getattr(item, "py_Expr23", None)
                    
                    setattr(item, "py_Expr23", self)
                    

class py_Nop:

    def __init__(self, nop: str):
        self.nop = nop
        
    @property
    def nop(self) -> str:
        return self.__nop

    @nop.setter
    def nop(self, nop: str):
        self.__nop = nop

class py_LExpr:

    pass
class py_ExprCons:

    pass
class py_ExprOr:

    pass
class py_ExprAnd:

    pass
class py_ExprSimple:

    def __init__(self, str: str, varSimple: str, sym: str, py_ExprSimple: "py_ExprAnd" = None, py_ExprSimple47: "py_ExprOr" = None, py_ExprSimple66: "py_ExprEq" = None):
        self.str = str
        self.varSimple = varSimple
        self.sym = sym
        self.py_ExprSimple = py_ExprSimple
        self.py_ExprSimple47 = py_ExprSimple47
        self.py_ExprSimple66 = py_ExprSimple66
        
    @property
    def str(self) -> str:
        return self.__str

    @str.setter
    def str(self, str: str):
        self.__str = str

    @property
    def varSimple(self) -> str:
        return self.__varSimple

    @varSimple.setter
    def varSimple(self, varSimple: str):
        self.__varSimple = varSimple

    @property
    def sym(self) -> str:
        return self.__sym

    @sym.setter
    def sym(self, sym: str):
        self.__sym = sym

    @property
    def py_ExprSimple66(self):
        return self.__py_ExprSimple66

    @py_ExprSimple66.setter
    def py_ExprSimple66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_py_ExprSimple__py_ExprSimple66", None)
        self.__py_ExprSimple66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "py_ExprEq"):
                opp_val = getattr(old_value, "py_ExprEq", None)
                if opp_val == self:
                    setattr(old_value, "py_ExprEq", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "py_ExprEq"):
                opp_val = getattr(value, "py_ExprEq", None)
                setattr(value, "py_ExprEq", self)

    @property
    def py_ExprSimple(self):
        return self.__py_ExprSimple

    @py_ExprSimple.setter
    def py_ExprSimple(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_py_ExprSimple__py_ExprSimple", None)
        self.__py_ExprSimple = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "py_ExprAnd"):
                opp_val = getattr(old_value, "py_ExprAnd", None)
                if opp_val == self:
                    setattr(old_value, "py_ExprAnd", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "py_ExprAnd"):
                opp_val = getattr(value, "py_ExprAnd", None)
                setattr(value, "py_ExprAnd", self)

    @property
    def py_ExprSimple47(self):
        return self.__py_ExprSimple47

    @py_ExprSimple47.setter
    def py_ExprSimple47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_py_ExprSimple__py_ExprSimple47", None)
        self.__py_ExprSimple47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "py_ExprOr"):
                opp_val = getattr(old_value, "py_ExprOr", None)
                if opp_val == self:
                    setattr(old_value, "py_ExprOr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "py_ExprOr"):
                opp_val = getattr(value, "py_ExprOr", None)
                setattr(value, "py_ExprOr", self)

class py_While:

    pass
class py_Foreach:

    def __init__(self, var: str, py_Foreach: "py_Expr" = None, py_Foreach32: "py_Commands" = None):
        self.var = var
        self.py_Foreach = py_Foreach
        self.py_Foreach32 = py_Foreach32
        
    @property
    def var(self) -> str:
        return self.__var

    @var.setter
    def var(self, var: str):
        self.__var = var

    @property
    def py_Foreach(self):
        return self.__py_Foreach

    @py_Foreach.setter
    def py_Foreach(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_py_Foreach__py_Foreach", None)
        self.__py_Foreach = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "py_Expr30"):
                opp_val = getattr(old_value, "py_Expr30", None)
                if opp_val == self:
                    setattr(old_value, "py_Expr30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "py_Expr30"):
                opp_val = getattr(value, "py_Expr30", None)
                setattr(value, "py_Expr30", self)

    @property
    def py_Foreach32(self):
        return self.__py_Foreach32

    @py_Foreach32.setter
    def py_Foreach32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_py_Foreach__py_Foreach32", None)
        self.__py_Foreach32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "py_Commands33"):
                opp_val = getattr(old_value, "py_Commands33", None)
                if opp_val == self:
                    setattr(old_value, "py_Commands33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "py_Commands33"):
                opp_val = getattr(value, "py_Commands33", None)
                setattr(value, "py_Commands33", self)

class py_Wh:

    pass
class py_Expr:

    pass
class py_If:

    pass
class py_EObject:

    pass
class py_Command:

    pass
class py_Output:

    def __init__(self, vars: str, py_Output: "py_Definition" = None):
        self.vars = vars
        self.py_Output = py_Output
        
    @property
    def vars(self) -> str:
        return self.__vars

    @vars.setter
    def vars(self, vars: str):
        self.__vars = vars

    @property
    def py_Output(self):
        return self.__py_Output

    @py_Output.setter
    def py_Output(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_py_Output__py_Output", None)
        self.__py_Output = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "py_Definition10"):
                opp_val = getattr(old_value, "py_Definition10", None)
                if opp_val == self:
                    setattr(old_value, "py_Definition10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "py_Definition10"):
                opp_val = getattr(value, "py_Definition10", None)
                setattr(value, "py_Definition10", self)

class py_Commands:

    pass
class py_Input:

    def __init__(self, vars: str, py_Input: "py_Definition" = None):
        self.vars = vars
        self.py_Input = py_Input
        
    @property
    def vars(self) -> str:
        return self.__vars

    @vars.setter
    def vars(self, vars: str):
        self.__vars = vars

    @property
    def py_Input(self):
        return self.__py_Input

    @py_Input.setter
    def py_Input(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_py_Input__py_Input", None)
        self.__py_Input = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "py_Definition6"):
                opp_val = getattr(old_value, "py_Definition6", None)
                if opp_val == self:
                    setattr(old_value, "py_Definition6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "py_Definition6"):
                opp_val = getattr(value, "py_Definition6", None)
                setattr(value, "py_Definition6", self)

class py_Definition:

    pass
class py_FunctionP:

    def __init__(self, name: str, py_FunctionP: "py_Program" = None, py_FunctionP4: "py_Definition" = None):
        self.name = name
        self.py_FunctionP = py_FunctionP
        self.py_FunctionP4 = py_FunctionP4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def py_FunctionP4(self):
        return self.__py_FunctionP4

    @py_FunctionP4.setter
    def py_FunctionP4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_py_FunctionP__py_FunctionP4", None)
        self.__py_FunctionP4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "py_Definition"):
                opp_val = getattr(old_value, "py_Definition", None)
                if opp_val == self:
                    setattr(old_value, "py_Definition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "py_Definition"):
                opp_val = getattr(value, "py_Definition", None)
                setattr(value, "py_Definition", self)

    @property
    def py_FunctionP(self):
        return self.__py_FunctionP

    @py_FunctionP.setter
    def py_FunctionP(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_py_FunctionP__py_FunctionP", None)
        self.__py_FunctionP = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "py_Program2"):
                opp_val = getattr(old_value, "py_Program2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "py_Program2"):
                opp_val = getattr(value, "py_Program2", None)
                if opp_val is None:
                    setattr(value, "py_Program2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class py_Program:

    pass