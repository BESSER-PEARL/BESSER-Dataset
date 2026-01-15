from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class while_l_ExprNot:

    pass
class while_l_ExprHd:

    pass
class while_l_ExprList:

    pass
class while_l_ExprCons:

    pass
class while_l_ExprOr:

    pass
class while_l_ExprAnd:

    pass
class while_l_ExprSimple:

    def __init__(self, str: str, varSimple: str, sym: str, nameFunction: str, while_l_ExprSimple: "while_l_Input" = None, while_l_ExprSimple42: "while_l_ExprAnd" = None, while_l_ExprSimple47: "while_l_ExprOr" = None, while_l_ExprSimple68: "while_l_ExprEq" = None, while_l_ExprSimple71: "while_l_ExprEq" = None):
        self.str = str
        self.varSimple = varSimple
        self.sym = sym
        self.nameFunction = nameFunction
        self.while_l_ExprSimple = while_l_ExprSimple
        self.while_l_ExprSimple42 = while_l_ExprSimple42
        self.while_l_ExprSimple47 = while_l_ExprSimple47
        self.while_l_ExprSimple68 = while_l_ExprSimple68
        self.while_l_ExprSimple71 = while_l_ExprSimple71
        
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
    def nameFunction(self) -> str:
        return self.__nameFunction

    @nameFunction.setter
    def nameFunction(self, nameFunction: str):
        self.__nameFunction = nameFunction

    @property
    def while_l_ExprSimple47(self):
        return self.__while_l_ExprSimple47

    @while_l_ExprSimple47.setter
    def while_l_ExprSimple47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_while_l_ExprSimple__while_l_ExprSimple47", None)
        self.__while_l_ExprSimple47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "while_l_ExprOr"):
                opp_val = getattr(old_value, "while_l_ExprOr", None)
                if opp_val == self:
                    setattr(old_value, "while_l_ExprOr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "while_l_ExprOr"):
                opp_val = getattr(value, "while_l_ExprOr", None)
                setattr(value, "while_l_ExprOr", self)

    @property
    def while_l_ExprSimple68(self):
        return self.__while_l_ExprSimple68

    @while_l_ExprSimple68.setter
    def while_l_ExprSimple68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_while_l_ExprSimple__while_l_ExprSimple68", None)
        self.__while_l_ExprSimple68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "while_l_ExprEq67"):
                opp_val = getattr(old_value, "while_l_ExprEq67", None)
                if opp_val == self:
                    setattr(old_value, "while_l_ExprEq67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "while_l_ExprEq67"):
                opp_val = getattr(value, "while_l_ExprEq67", None)
                setattr(value, "while_l_ExprEq67", self)

    @property
    def while_l_ExprSimple42(self):
        return self.__while_l_ExprSimple42

    @while_l_ExprSimple42.setter
    def while_l_ExprSimple42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_while_l_ExprSimple__while_l_ExprSimple42", None)
        self.__while_l_ExprSimple42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "while_l_ExprAnd"):
                opp_val = getattr(old_value, "while_l_ExprAnd", None)
                if opp_val == self:
                    setattr(old_value, "while_l_ExprAnd", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "while_l_ExprAnd"):
                opp_val = getattr(value, "while_l_ExprAnd", None)
                setattr(value, "while_l_ExprAnd", self)

    @property
    def while_l_ExprSimple71(self):
        return self.__while_l_ExprSimple71

    @while_l_ExprSimple71.setter
    def while_l_ExprSimple71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_while_l_ExprSimple__while_l_ExprSimple71", None)
        self.__while_l_ExprSimple71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "while_l_ExprEq70"):
                opp_val = getattr(old_value, "while_l_ExprEq70", None)
                if opp_val == self:
                    setattr(old_value, "while_l_ExprEq70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "while_l_ExprEq70"):
                opp_val = getattr(value, "while_l_ExprEq70", None)
                setattr(value, "while_l_ExprEq70", self)

    @property
    def while_l_ExprSimple(self):
        return self.__while_l_ExprSimple

    @while_l_ExprSimple.setter
    def while_l_ExprSimple(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_while_l_ExprSimple__while_l_ExprSimple", None)
        self.__while_l_ExprSimple = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "while_l_Input40"):
                opp_val = getattr(old_value, "while_l_Input40", None)
                if opp_val == self:
                    setattr(old_value, "while_l_Input40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "while_l_Input40"):
                opp_val = getattr(value, "while_l_Input40", None)
                setattr(value, "while_l_Input40", self)

class while_l_ExprEq:

    pass
class while_l_While:

    pass
class while_l_ExprSym:

    def __init__(self, arg1: str, while_l_ExprSym: set["while_l_Expr"] = None):
        self.arg1 = arg1
        self.while_l_ExprSym = while_l_ExprSym if while_l_ExprSym is not None else set()
        
    @property
    def arg1(self) -> str:
        return self.__arg1

    @arg1.setter
    def arg1(self, arg1: str):
        self.__arg1 = arg1

    @property
    def while_l_ExprSym(self):
        return self.__while_l_ExprSym

    @while_l_ExprSym.setter
    def while_l_ExprSym(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_while_l_ExprSym__while_l_ExprSym", None)
        self.__while_l_ExprSym = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "while_l_Expr63"):
                    opp_val = getattr(item, "while_l_Expr63", None)
                    
                    if opp_val == self:
                        setattr(item, "while_l_Expr63", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "while_l_Expr63"):
                    opp_val = getattr(item, "while_l_Expr63", None)
                    
                    setattr(item, "while_l_Expr63", self)
                    

class while_l_ExprTl:

    pass
class while_l_Affect:

    def __init__(self, vars: str, while_l_Affect: set["while_l_Expr"] = None):
        self.vars = vars
        self.while_l_Affect = while_l_Affect if while_l_Affect is not None else set()
        
    @property
    def vars(self) -> str:
        return self.__vars

    @vars.setter
    def vars(self, vars: str):
        self.__vars = vars

    @property
    def while_l_Affect(self):
        return self.__while_l_Affect

    @while_l_Affect.setter
    def while_l_Affect(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_while_l_Affect__while_l_Affect", None)
        self.__while_l_Affect = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "while_l_Expr23"):
                    opp_val = getattr(item, "while_l_Expr23", None)
                    
                    if opp_val == self:
                        setattr(item, "while_l_Expr23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "while_l_Expr23"):
                    opp_val = getattr(item, "while_l_Expr23", None)
                    
                    setattr(item, "while_l_Expr23", self)
                    

class while_l_Nop:

    def __init__(self, nop: str):
        self.nop = nop
        
    @property
    def nop(self) -> str:
        return self.__nop

    @nop.setter
    def nop(self, nop: str):
        self.__nop = nop

class while_l_Expr:

    pass
class while_l_If:

    pass
class while_l_EObject:

    pass
class while_l_Command:

    pass
class while_l_Output:

    def __init__(self, vars: str, while_l_Output: "while_l_Definition" = None):
        self.vars = vars
        self.while_l_Output = while_l_Output
        
    @property
    def vars(self) -> str:
        return self.__vars

    @vars.setter
    def vars(self, vars: str):
        self.__vars = vars

    @property
    def while_l_Output(self):
        return self.__while_l_Output

    @while_l_Output.setter
    def while_l_Output(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_while_l_Output__while_l_Output", None)
        self.__while_l_Output = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "while_l_Definition10"):
                opp_val = getattr(old_value, "while_l_Definition10", None)
                if opp_val == self:
                    setattr(old_value, "while_l_Definition10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "while_l_Definition10"):
                opp_val = getattr(value, "while_l_Definition10", None)
                setattr(value, "while_l_Definition10", self)

class while_l_Commands:

    pass
class while_l_Input:

    def __init__(self, vars: str, while_l_Input: "while_l_Definition" = None, while_l_Input40: "while_l_ExprSimple" = None):
        self.vars = vars
        self.while_l_Input = while_l_Input
        self.while_l_Input40 = while_l_Input40
        
    @property
    def vars(self) -> str:
        return self.__vars

    @vars.setter
    def vars(self, vars: str):
        self.__vars = vars

    @property
    def while_l_Input40(self):
        return self.__while_l_Input40

    @while_l_Input40.setter
    def while_l_Input40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_while_l_Input__while_l_Input40", None)
        self.__while_l_Input40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "while_l_ExprSimple"):
                opp_val = getattr(old_value, "while_l_ExprSimple", None)
                if opp_val == self:
                    setattr(old_value, "while_l_ExprSimple", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "while_l_ExprSimple"):
                opp_val = getattr(value, "while_l_ExprSimple", None)
                setattr(value, "while_l_ExprSimple", self)

    @property
    def while_l_Input(self):
        return self.__while_l_Input

    @while_l_Input.setter
    def while_l_Input(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_while_l_Input__while_l_Input", None)
        self.__while_l_Input = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "while_l_Definition6"):
                opp_val = getattr(old_value, "while_l_Definition6", None)
                if opp_val == self:
                    setattr(old_value, "while_l_Definition6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "while_l_Definition6"):
                opp_val = getattr(value, "while_l_Definition6", None)
                setattr(value, "while_l_Definition6", self)

class while_l_Definition:

    pass
class while_l_Function:

    def __init__(self, name: str, while_l_Function: "while_l_Program" = None, while_l_Function4: "while_l_Definition" = None):
        self.name = name
        self.while_l_Function = while_l_Function
        self.while_l_Function4 = while_l_Function4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def while_l_Function(self):
        return self.__while_l_Function

    @while_l_Function.setter
    def while_l_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_while_l_Function__while_l_Function", None)
        self.__while_l_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "while_l_Program2"):
                opp_val = getattr(old_value, "while_l_Program2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "while_l_Program2"):
                opp_val = getattr(value, "while_l_Program2", None)
                if opp_val is None:
                    setattr(value, "while_l_Program2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def while_l_Function4(self):
        return self.__while_l_Function4

    @while_l_Function4.setter
    def while_l_Function4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_while_l_Function__while_l_Function4", None)
        self.__while_l_Function4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "while_l_Definition"):
                opp_val = getattr(old_value, "while_l_Definition", None)
                if opp_val == self:
                    setattr(old_value, "while_l_Definition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "while_l_Definition"):
                opp_val = getattr(value, "while_l_Definition", None)
                setattr(value, "while_l_Definition", self)

class while_l_For:

    pass
class while_l_Program:

    pass
class while_l_Wh:

    pass