from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class langage_while_ExprEq:

    pass
class langage_while_ExprNot:

    pass
class langage_while_ExprOr:

    pass
class langage_while_LExpr:

    pass
class langage_while_ExprAnd:

    pass
class langage_while_ExprSimple:

    def __init__(self, nil: str, mot: str, langage_while_ExprSimple: "langage_while_Expr" = None, langage_while_ExprSimple85: "langage_while_VAR" = None, langage_while_ExprSimple88: "langage_while_SYMB" = None, langage_while_ExprSimple91: "langage_while_LExpr" = None, langage_while_ExprSimple93: "langage_while_Expr" = None, langage_while_ExprSimple118: "langage_while_ExprEq" = None, langage_while_ExprSimple115: "langage_while_ExprEq" = None):
        self.nil = nil
        self.mot = mot
        self.langage_while_ExprSimple = langage_while_ExprSimple
        self.langage_while_ExprSimple85 = langage_while_ExprSimple85
        self.langage_while_ExprSimple88 = langage_while_ExprSimple88
        self.langage_while_ExprSimple91 = langage_while_ExprSimple91
        self.langage_while_ExprSimple93 = langage_while_ExprSimple93
        self.langage_while_ExprSimple118 = langage_while_ExprSimple118
        self.langage_while_ExprSimple115 = langage_while_ExprSimple115
        
    @property
    def nil(self) -> str:
        return self.__nil

    @nil.setter
    def nil(self, nil: str):
        self.__nil = nil

    @property
    def mot(self) -> str:
        return self.__mot

    @mot.setter
    def mot(self, mot: str):
        self.__mot = mot

    @property
    def langage_while_ExprSimple(self):
        return self.__langage_while_ExprSimple

    @langage_while_ExprSimple.setter
    def langage_while_ExprSimple(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langage_while_ExprSimple__langage_while_ExprSimple", None)
        self.__langage_while_ExprSimple = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langage_while_Expr81"):
                opp_val = getattr(old_value, "langage_while_Expr81", None)
                if opp_val == self:
                    setattr(old_value, "langage_while_Expr81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langage_while_Expr81"):
                opp_val = getattr(value, "langage_while_Expr81", None)
                setattr(value, "langage_while_Expr81", self)

    @property
    def langage_while_ExprSimple93(self):
        return self.__langage_while_ExprSimple93

    @langage_while_ExprSimple93.setter
    def langage_while_ExprSimple93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langage_while_ExprSimple__langage_while_ExprSimple93", None)
        self.__langage_while_ExprSimple93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langage_while_Expr94"):
                opp_val = getattr(old_value, "langage_while_Expr94", None)
                if opp_val == self:
                    setattr(old_value, "langage_while_Expr94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langage_while_Expr94"):
                opp_val = getattr(value, "langage_while_Expr94", None)
                setattr(value, "langage_while_Expr94", self)

    @property
    def langage_while_ExprSimple115(self):
        return self.__langage_while_ExprSimple115

    @langage_while_ExprSimple115.setter
    def langage_while_ExprSimple115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langage_while_ExprSimple__langage_while_ExprSimple115", None)
        self.__langage_while_ExprSimple115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langage_while_ExprEq114"):
                opp_val = getattr(old_value, "langage_while_ExprEq114", None)
                if opp_val == self:
                    setattr(old_value, "langage_while_ExprEq114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langage_while_ExprEq114"):
                opp_val = getattr(value, "langage_while_ExprEq114", None)
                setattr(value, "langage_while_ExprEq114", self)

    @property
    def langage_while_ExprSimple88(self):
        return self.__langage_while_ExprSimple88

    @langage_while_ExprSimple88.setter
    def langage_while_ExprSimple88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langage_while_ExprSimple__langage_while_ExprSimple88", None)
        self.__langage_while_ExprSimple88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langage_while_SYMB89"):
                opp_val = getattr(old_value, "langage_while_SYMB89", None)
                if opp_val == self:
                    setattr(old_value, "langage_while_SYMB89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langage_while_SYMB89"):
                opp_val = getattr(value, "langage_while_SYMB89", None)
                setattr(value, "langage_while_SYMB89", self)

    @property
    def langage_while_ExprSimple85(self):
        return self.__langage_while_ExprSimple85

    @langage_while_ExprSimple85.setter
    def langage_while_ExprSimple85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langage_while_ExprSimple__langage_while_ExprSimple85", None)
        self.__langage_while_ExprSimple85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langage_while_VAR86"):
                opp_val = getattr(old_value, "langage_while_VAR86", None)
                if opp_val == self:
                    setattr(old_value, "langage_while_VAR86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langage_while_VAR86"):
                opp_val = getattr(value, "langage_while_VAR86", None)
                setattr(value, "langage_while_VAR86", self)

    @property
    def langage_while_ExprSimple91(self):
        return self.__langage_while_ExprSimple91

    @langage_while_ExprSimple91.setter
    def langage_while_ExprSimple91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langage_while_ExprSimple__langage_while_ExprSimple91", None)
        self.__langage_while_ExprSimple91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langage_while_LExpr"):
                opp_val = getattr(old_value, "langage_while_LExpr", None)
                if opp_val == self:
                    setattr(old_value, "langage_while_LExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langage_while_LExpr"):
                opp_val = getattr(value, "langage_while_LExpr", None)
                setattr(value, "langage_while_LExpr", self)

    @property
    def langage_while_ExprSimple118(self):
        return self.__langage_while_ExprSimple118

    @langage_while_ExprSimple118.setter
    def langage_while_ExprSimple118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langage_while_ExprSimple__langage_while_ExprSimple118", None)
        self.__langage_while_ExprSimple118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langage_while_ExprEq117"):
                opp_val = getattr(old_value, "langage_while_ExprEq117", None)
                if opp_val == self:
                    setattr(old_value, "langage_while_ExprEq117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langage_while_ExprEq117"):
                opp_val = getattr(value, "langage_while_ExprEq117", None)
                setattr(value, "langage_while_ExprEq117", self)

class langage_while_Command:

    def __init__(self, nop: str, langage_while_Command24: "langage_while_Assign" = None, langage_while_Command26: "langage_while_While" = None, langage_while_Command28: "langage_while_For" = None, langage_while_Command30: "langage_while_If" = None, langage_while_Command32: "langage_while_Foreach" = None, langage_while_Command34: "langage_while_Ifconfort" = None, langage_while_Command: "langage_while_Commands" = None):
        self.nop = nop
        self.langage_while_Command24 = langage_while_Command24
        self.langage_while_Command26 = langage_while_Command26
        self.langage_while_Command28 = langage_while_Command28
        self.langage_while_Command30 = langage_while_Command30
        self.langage_while_Command32 = langage_while_Command32
        self.langage_while_Command34 = langage_while_Command34
        self.langage_while_Command = langage_while_Command
        
    @property
    def nop(self) -> str:
        return self.__nop

    @nop.setter
    def nop(self, nop: str):
        self.__nop = nop

    @property
    def langage_while_Command28(self):
        return self.__langage_while_Command28

    @langage_while_Command28.setter
    def langage_while_Command28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langage_while_Command__langage_while_Command28", None)
        self.__langage_while_Command28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langage_while_For"):
                opp_val = getattr(old_value, "langage_while_For", None)
                if opp_val == self:
                    setattr(old_value, "langage_while_For", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langage_while_For"):
                opp_val = getattr(value, "langage_while_For", None)
                setattr(value, "langage_while_For", self)

    @property
    def langage_while_Command(self):
        return self.__langage_while_Command

    @langage_while_Command.setter
    def langage_while_Command(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langage_while_Command__langage_while_Command", None)
        self.__langage_while_Command = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langage_while_Commands22"):
                opp_val = getattr(old_value, "langage_while_Commands22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langage_while_Commands22"):
                opp_val = getattr(value, "langage_while_Commands22", None)
                if opp_val is None:
                    setattr(value, "langage_while_Commands22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def langage_while_Command34(self):
        return self.__langage_while_Command34

    @langage_while_Command34.setter
    def langage_while_Command34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langage_while_Command__langage_while_Command34", None)
        self.__langage_while_Command34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langage_while_Ifconfort"):
                opp_val = getattr(old_value, "langage_while_Ifconfort", None)
                if opp_val == self:
                    setattr(old_value, "langage_while_Ifconfort", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langage_while_Ifconfort"):
                opp_val = getattr(value, "langage_while_Ifconfort", None)
                setattr(value, "langage_while_Ifconfort", self)

    @property
    def langage_while_Command30(self):
        return self.__langage_while_Command30

    @langage_while_Command30.setter
    def langage_while_Command30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langage_while_Command__langage_while_Command30", None)
        self.__langage_while_Command30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langage_while_If"):
                opp_val = getattr(old_value, "langage_while_If", None)
                if opp_val == self:
                    setattr(old_value, "langage_while_If", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langage_while_If"):
                opp_val = getattr(value, "langage_while_If", None)
                setattr(value, "langage_while_If", self)

    @property
    def langage_while_Command24(self):
        return self.__langage_while_Command24

    @langage_while_Command24.setter
    def langage_while_Command24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langage_while_Command__langage_while_Command24", None)
        self.__langage_while_Command24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langage_while_Assign"):
                opp_val = getattr(old_value, "langage_while_Assign", None)
                if opp_val == self:
                    setattr(old_value, "langage_while_Assign", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langage_while_Assign"):
                opp_val = getattr(value, "langage_while_Assign", None)
                setattr(value, "langage_while_Assign", self)

    @property
    def langage_while_Command32(self):
        return self.__langage_while_Command32

    @langage_while_Command32.setter
    def langage_while_Command32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langage_while_Command__langage_while_Command32", None)
        self.__langage_while_Command32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langage_while_Foreach"):
                opp_val = getattr(old_value, "langage_while_Foreach", None)
                if opp_val == self:
                    setattr(old_value, "langage_while_Foreach", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langage_while_Foreach"):
                opp_val = getattr(value, "langage_while_Foreach", None)
                setattr(value, "langage_while_Foreach", self)

    @property
    def langage_while_Command26(self):
        return self.__langage_while_Command26

    @langage_while_Command26.setter
    def langage_while_Command26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langage_while_Command__langage_while_Command26", None)
        self.__langage_while_Command26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langage_while_While"):
                opp_val = getattr(old_value, "langage_while_While", None)
                if opp_val == self:
                    setattr(old_value, "langage_while_While", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langage_while_While"):
                opp_val = getattr(value, "langage_while_While", None)
                setattr(value, "langage_while_While", self)

class langage_while_VAR:

    def __init__(self, bv: str, cf: str, langage_while_VAR: "langage_while_Input" = None, langage_while_VAR20: "langage_while_Output" = None, langage_while_VAR76: "langage_while_Vars" = None, langage_while_VAR86: "langage_while_ExprSimple" = None):
        self.bv = bv
        self.cf = cf
        self.langage_while_VAR = langage_while_VAR
        self.langage_while_VAR20 = langage_while_VAR20
        self.langage_while_VAR76 = langage_while_VAR76
        self.langage_while_VAR86 = langage_while_VAR86
        
    @property
    def cf(self) -> str:
        return self.__cf

    @cf.setter
    def cf(self, cf: str):
        self.__cf = cf

    @property
    def bv(self) -> str:
        return self.__bv

    @bv.setter
    def bv(self, bv: str):
        self.__bv = bv

    @property
    def langage_while_VAR(self):
        return self.__langage_while_VAR

    @langage_while_VAR.setter
    def langage_while_VAR(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langage_while_VAR__langage_while_VAR", None)
        self.__langage_while_VAR = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langage_while_Input17"):
                opp_val = getattr(old_value, "langage_while_Input17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langage_while_Input17"):
                opp_val = getattr(value, "langage_while_Input17", None)
                if opp_val is None:
                    setattr(value, "langage_while_Input17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def langage_while_VAR76(self):
        return self.__langage_while_VAR76

    @langage_while_VAR76.setter
    def langage_while_VAR76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langage_while_VAR__langage_while_VAR76", None)
        self.__langage_while_VAR76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langage_while_Vars75"):
                opp_val = getattr(old_value, "langage_while_Vars75", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langage_while_Vars75"):
                opp_val = getattr(value, "langage_while_Vars75", None)
                if opp_val is None:
                    setattr(value, "langage_while_Vars75", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def langage_while_VAR20(self):
        return self.__langage_while_VAR20

    @langage_while_VAR20.setter
    def langage_while_VAR20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langage_while_VAR__langage_while_VAR20", None)
        self.__langage_while_VAR20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langage_while_Output19"):
                opp_val = getattr(old_value, "langage_while_Output19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langage_while_Output19"):
                opp_val = getattr(value, "langage_while_Output19", None)
                if opp_val is None:
                    setattr(value, "langage_while_Output19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def langage_while_VAR86(self):
        return self.__langage_while_VAR86

    @langage_while_VAR86.setter
    def langage_while_VAR86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langage_while_VAR__langage_while_VAR86", None)
        self.__langage_while_VAR86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langage_while_ExprSimple85"):
                opp_val = getattr(old_value, "langage_while_ExprSimple85", None)
                if opp_val == self:
                    setattr(old_value, "langage_while_ExprSimple85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langage_while_ExprSimple85"):
                opp_val = getattr(value, "langage_while_ExprSimple85", None)
                setattr(value, "langage_while_ExprSimple85", self)

class langage_while_Expr:

    pass
class langage_while_Exprs:

    pass
class langage_while_Vars:

    pass
class langage_while_Ifconfort:

    pass
class langage_while_Foreach:

    pass
class langage_while_If:

    pass
class langage_while_For:

    pass
class langage_while_While:

    pass
class langage_while_Assign:

    pass
class langage_while_Output:

    pass
class langage_while_Commands:

    pass
class langage_while_Input:

    pass
class langage_while_Definition:

    pass
class langage_while_SYMB:

    def __init__(self, bs: str, cf: str, langage_while_SYMB: "langage_while_Function" = None, langage_while_SYMB89: "langage_while_ExprSimple" = None):
        self.bs = bs
        self.cf = cf
        self.langage_while_SYMB = langage_while_SYMB
        self.langage_while_SYMB89 = langage_while_SYMB89
        
    @property
    def cf(self) -> str:
        return self.__cf

    @cf.setter
    def cf(self, cf: str):
        self.__cf = cf

    @property
    def bs(self) -> str:
        return self.__bs

    @bs.setter
    def bs(self, bs: str):
        self.__bs = bs

    @property
    def langage_while_SYMB89(self):
        return self.__langage_while_SYMB89

    @langage_while_SYMB89.setter
    def langage_while_SYMB89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langage_while_SYMB__langage_while_SYMB89", None)
        self.__langage_while_SYMB89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langage_while_ExprSimple88"):
                opp_val = getattr(old_value, "langage_while_ExprSimple88", None)
                if opp_val == self:
                    setattr(old_value, "langage_while_ExprSimple88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langage_while_ExprSimple88"):
                opp_val = getattr(value, "langage_while_ExprSimple88", None)
                setattr(value, "langage_while_ExprSimple88", self)

    @property
    def langage_while_SYMB(self):
        return self.__langage_while_SYMB

    @langage_while_SYMB.setter
    def langage_while_SYMB(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langage_while_SYMB__langage_while_SYMB", None)
        self.__langage_while_SYMB = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langage_while_Function7"):
                opp_val = getattr(old_value, "langage_while_Function7", None)
                if opp_val == self:
                    setattr(old_value, "langage_while_Function7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langage_while_Function7"):
                opp_val = getattr(value, "langage_while_Function7", None)
                setattr(value, "langage_while_Function7", self)

class langage_while_Function:

    pass
class langage_while_Program:

    def __init__(self, u: str, langage_while_Program: "langage_while_Model" = None, langage_while_Program2: set["langage_while_Function"] = None, langage_while_Program5: "langage_while_Program" = None, langage_while_Program3: "langage_while_Program" = None):
        self.u = u
        self.langage_while_Program = langage_while_Program
        self.langage_while_Program2 = langage_while_Program2 if langage_while_Program2 is not None else set()
        self.langage_while_Program5 = langage_while_Program5
        self.langage_while_Program3 = langage_while_Program3
        
    @property
    def u(self) -> str:
        return self.__u

    @u.setter
    def u(self, u: str):
        self.__u = u

    @property
    def langage_while_Program(self):
        return self.__langage_while_Program

    @langage_while_Program.setter
    def langage_while_Program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langage_while_Program__langage_while_Program", None)
        self.__langage_while_Program = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langage_while_Model"):
                opp_val = getattr(old_value, "langage_while_Model", None)
                if opp_val == self:
                    setattr(old_value, "langage_while_Model", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langage_while_Model"):
                opp_val = getattr(value, "langage_while_Model", None)
                setattr(value, "langage_while_Model", self)

    @property
    def langage_while_Program5(self):
        return self.__langage_while_Program5

    @langage_while_Program5.setter
    def langage_while_Program5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langage_while_Program__langage_while_Program5", None)
        self.__langage_while_Program5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langage_while_Program3"):
                opp_val = getattr(old_value, "langage_while_Program3", None)
                if opp_val == self:
                    setattr(old_value, "langage_while_Program3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langage_while_Program3"):
                opp_val = getattr(value, "langage_while_Program3", None)
                setattr(value, "langage_while_Program3", self)

    @property
    def langage_while_Program3(self):
        return self.__langage_while_Program3

    @langage_while_Program3.setter
    def langage_while_Program3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langage_while_Program__langage_while_Program3", None)
        self.__langage_while_Program3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langage_while_Program5"):
                opp_val = getattr(old_value, "langage_while_Program5", None)
                if opp_val == self:
                    setattr(old_value, "langage_while_Program5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langage_while_Program5"):
                opp_val = getattr(value, "langage_while_Program5", None)
                setattr(value, "langage_while_Program5", self)

    @property
    def langage_while_Program2(self):
        return self.__langage_while_Program2

    @langage_while_Program2.setter
    def langage_while_Program2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langage_while_Program__langage_while_Program2", None)
        self.__langage_while_Program2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "langage_while_Function"):
                    opp_val = getattr(item, "langage_while_Function", None)
                    
                    if opp_val == self:
                        setattr(item, "langage_while_Function", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "langage_while_Function"):
                    opp_val = getattr(item, "langage_while_Function", None)
                    
                    setattr(item, "langage_while_Function", self)
                    

class langage_while_Model:

    pass