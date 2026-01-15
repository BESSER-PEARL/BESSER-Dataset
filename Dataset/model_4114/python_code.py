from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class whileCpp_Cons:

    def __init__(self, exprCons: str, whileCpp_Cons: "whileCpp_ExprSimple" = None, whileCpp_Cons84: set["whileCpp_Expr"] = None):
        self.exprCons = exprCons
        self.whileCpp_Cons = whileCpp_Cons
        self.whileCpp_Cons84 = whileCpp_Cons84 if whileCpp_Cons84 is not None else set()
        
    @property
    def exprCons(self) -> str:
        return self.__exprCons

    @exprCons.setter
    def exprCons(self, exprCons: str):
        self.__exprCons = exprCons

    @property
    def whileCpp_Cons(self):
        return self.__whileCpp_Cons

    @whileCpp_Cons.setter
    def whileCpp_Cons(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileCpp_Cons__whileCpp_Cons", None)
        self.__whileCpp_Cons = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileCpp_ExprSimple52"):
                opp_val = getattr(old_value, "whileCpp_ExprSimple52", None)
                if opp_val == self:
                    setattr(old_value, "whileCpp_ExprSimple52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileCpp_ExprSimple52"):
                opp_val = getattr(value, "whileCpp_ExprSimple52", None)
                setattr(value, "whileCpp_ExprSimple52", self)

    @property
    def whileCpp_Cons84(self):
        return self.__whileCpp_Cons84

    @whileCpp_Cons84.setter
    def whileCpp_Cons84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileCpp_Cons__whileCpp_Cons84", None)
        self.__whileCpp_Cons84 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "whileCpp_Expr85"):
                    opp_val = getattr(item, "whileCpp_Expr85", None)
                    
                    if opp_val == self:
                        setattr(item, "whileCpp_Expr85", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "whileCpp_Expr85"):
                    opp_val = getattr(item, "whileCpp_Expr85", None)
                    
                    setattr(item, "whileCpp_Expr85", self)
                    

class whileCpp_ExprEq:

    pass
class whileCpp_ExprNot:

    def __init__(self, not: str, whileCpp_ExprNot: "whileCpp_ExprOr" = None, whileCpp_ExprNot73: "whileCpp_ExprEq" = None):
        self.not = not
        self.whileCpp_ExprNot = whileCpp_ExprNot
        self.whileCpp_ExprNot73 = whileCpp_ExprNot73
        
    @property
    def not(self) -> str:
        return self.__not

    @not.setter
    def not(self, not: str):
        self.__not = not

    @property
    def whileCpp_ExprNot(self):
        return self.__whileCpp_ExprNot

    @whileCpp_ExprNot.setter
    def whileCpp_ExprNot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileCpp_ExprNot__whileCpp_ExprNot", None)
        self.__whileCpp_ExprNot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileCpp_ExprOr68"):
                opp_val = getattr(old_value, "whileCpp_ExprOr68", None)
                if opp_val == self:
                    setattr(old_value, "whileCpp_ExprOr68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileCpp_ExprOr68"):
                opp_val = getattr(value, "whileCpp_ExprOr68", None)
                setattr(value, "whileCpp_ExprOr68", self)

    @property
    def whileCpp_ExprNot73(self):
        return self.__whileCpp_ExprNot73

    @whileCpp_ExprNot73.setter
    def whileCpp_ExprNot73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileCpp_ExprNot__whileCpp_ExprNot73", None)
        self.__whileCpp_ExprNot73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileCpp_ExprEq"):
                opp_val = getattr(old_value, "whileCpp_ExprEq", None)
                if opp_val == self:
                    setattr(old_value, "whileCpp_ExprEq", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileCpp_ExprEq"):
                opp_val = getattr(value, "whileCpp_ExprEq", None)
                setattr(value, "whileCpp_ExprEq", self)

class whileCpp_ExprOr:

    def __init__(self, exprOr: str, whileCpp_ExprOr: "whileCpp_ExprAnd" = None, whileCpp_ExprOr68: "whileCpp_ExprNot" = None, whileCpp_ExprOr71: "whileCpp_ExprOr" = None, whileCpp_ExprOr69: "whileCpp_ExprOr" = None):
        self.exprOr = exprOr
        self.whileCpp_ExprOr = whileCpp_ExprOr
        self.whileCpp_ExprOr68 = whileCpp_ExprOr68
        self.whileCpp_ExprOr71 = whileCpp_ExprOr71
        self.whileCpp_ExprOr69 = whileCpp_ExprOr69
        
    @property
    def exprOr(self) -> str:
        return self.__exprOr

    @exprOr.setter
    def exprOr(self, exprOr: str):
        self.__exprOr = exprOr

    @property
    def whileCpp_ExprOr71(self):
        return self.__whileCpp_ExprOr71

    @whileCpp_ExprOr71.setter
    def whileCpp_ExprOr71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileCpp_ExprOr__whileCpp_ExprOr71", None)
        self.__whileCpp_ExprOr71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileCpp_ExprOr69"):
                opp_val = getattr(old_value, "whileCpp_ExprOr69", None)
                if opp_val == self:
                    setattr(old_value, "whileCpp_ExprOr69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileCpp_ExprOr69"):
                opp_val = getattr(value, "whileCpp_ExprOr69", None)
                setattr(value, "whileCpp_ExprOr69", self)

    @property
    def whileCpp_ExprOr(self):
        return self.__whileCpp_ExprOr

    @whileCpp_ExprOr.setter
    def whileCpp_ExprOr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileCpp_ExprOr__whileCpp_ExprOr", None)
        self.__whileCpp_ExprOr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileCpp_ExprAnd63"):
                opp_val = getattr(old_value, "whileCpp_ExprAnd63", None)
                if opp_val == self:
                    setattr(old_value, "whileCpp_ExprAnd63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileCpp_ExprAnd63"):
                opp_val = getattr(value, "whileCpp_ExprAnd63", None)
                setattr(value, "whileCpp_ExprAnd63", self)

    @property
    def whileCpp_ExprOr69(self):
        return self.__whileCpp_ExprOr69

    @whileCpp_ExprOr69.setter
    def whileCpp_ExprOr69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileCpp_ExprOr__whileCpp_ExprOr69", None)
        self.__whileCpp_ExprOr69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileCpp_ExprOr71"):
                opp_val = getattr(old_value, "whileCpp_ExprOr71", None)
                if opp_val == self:
                    setattr(old_value, "whileCpp_ExprOr71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileCpp_ExprOr71"):
                opp_val = getattr(value, "whileCpp_ExprOr71", None)
                setattr(value, "whileCpp_ExprOr71", self)

    @property
    def whileCpp_ExprOr68(self):
        return self.__whileCpp_ExprOr68

    @whileCpp_ExprOr68.setter
    def whileCpp_ExprOr68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileCpp_ExprOr__whileCpp_ExprOr68", None)
        self.__whileCpp_ExprOr68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileCpp_ExprNot"):
                opp_val = getattr(old_value, "whileCpp_ExprNot", None)
                if opp_val == self:
                    setattr(old_value, "whileCpp_ExprNot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileCpp_ExprNot"):
                opp_val = getattr(value, "whileCpp_ExprNot", None)
                setattr(value, "whileCpp_ExprNot", self)

class whileCpp_Expr:

    pass
class whileCpp_CommandForEach:

    pass
class whileCpp_CommandIf:

    pass
class whileCpp_CommandWhile:

    def __init__(self, w: str, whileCpp_CommandWhile: "whileCpp_Command" = None, whileCpp_CommandWhile22: "whileCpp_Expr" = None, whileCpp_CommandWhile24: "whileCpp_Commands" = None):
        self.w = w
        self.whileCpp_CommandWhile = whileCpp_CommandWhile
        self.whileCpp_CommandWhile22 = whileCpp_CommandWhile22
        self.whileCpp_CommandWhile24 = whileCpp_CommandWhile24
        
    @property
    def w(self) -> str:
        return self.__w

    @w.setter
    def w(self, w: str):
        self.__w = w

    @property
    def whileCpp_CommandWhile22(self):
        return self.__whileCpp_CommandWhile22

    @whileCpp_CommandWhile22.setter
    def whileCpp_CommandWhile22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileCpp_CommandWhile__whileCpp_CommandWhile22", None)
        self.__whileCpp_CommandWhile22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileCpp_Expr"):
                opp_val = getattr(old_value, "whileCpp_Expr", None)
                if opp_val == self:
                    setattr(old_value, "whileCpp_Expr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileCpp_Expr"):
                opp_val = getattr(value, "whileCpp_Expr", None)
                setattr(value, "whileCpp_Expr", self)

    @property
    def whileCpp_CommandWhile24(self):
        return self.__whileCpp_CommandWhile24

    @whileCpp_CommandWhile24.setter
    def whileCpp_CommandWhile24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileCpp_CommandWhile__whileCpp_CommandWhile24", None)
        self.__whileCpp_CommandWhile24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileCpp_Commands25"):
                opp_val = getattr(old_value, "whileCpp_Commands25", None)
                if opp_val == self:
                    setattr(old_value, "whileCpp_Commands25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileCpp_Commands25"):
                opp_val = getattr(value, "whileCpp_Commands25", None)
                setattr(value, "whileCpp_Commands25", self)

    @property
    def whileCpp_CommandWhile(self):
        return self.__whileCpp_CommandWhile

    @whileCpp_CommandWhile.setter
    def whileCpp_CommandWhile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileCpp_CommandWhile__whileCpp_CommandWhile", None)
        self.__whileCpp_CommandWhile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileCpp_Command16"):
                opp_val = getattr(old_value, "whileCpp_Command16", None)
                if opp_val == self:
                    setattr(old_value, "whileCpp_Command16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileCpp_Command16"):
                opp_val = getattr(value, "whileCpp_Command16", None)
                setattr(value, "whileCpp_Command16", self)

class whileCpp_Exprs:

    pass
class whileCpp_ExprAnd:

    def __init__(self, exprAnd: str, whileCpp_ExprAnd: "whileCpp_Expr" = None, whileCpp_ExprAnd63: "whileCpp_ExprOr" = None, whileCpp_ExprAnd66: "whileCpp_ExprAnd" = None, whileCpp_ExprAnd64: "whileCpp_ExprAnd" = None):
        self.exprAnd = exprAnd
        self.whileCpp_ExprAnd = whileCpp_ExprAnd
        self.whileCpp_ExprAnd63 = whileCpp_ExprAnd63
        self.whileCpp_ExprAnd66 = whileCpp_ExprAnd66
        self.whileCpp_ExprAnd64 = whileCpp_ExprAnd64
        
    @property
    def exprAnd(self) -> str:
        return self.__exprAnd

    @exprAnd.setter
    def exprAnd(self, exprAnd: str):
        self.__exprAnd = exprAnd

    @property
    def whileCpp_ExprAnd(self):
        return self.__whileCpp_ExprAnd

    @whileCpp_ExprAnd.setter
    def whileCpp_ExprAnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileCpp_ExprAnd__whileCpp_ExprAnd", None)
        self.__whileCpp_ExprAnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileCpp_Expr50"):
                opp_val = getattr(old_value, "whileCpp_Expr50", None)
                if opp_val == self:
                    setattr(old_value, "whileCpp_Expr50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileCpp_Expr50"):
                opp_val = getattr(value, "whileCpp_Expr50", None)
                setattr(value, "whileCpp_Expr50", self)

    @property
    def whileCpp_ExprAnd64(self):
        return self.__whileCpp_ExprAnd64

    @whileCpp_ExprAnd64.setter
    def whileCpp_ExprAnd64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileCpp_ExprAnd__whileCpp_ExprAnd64", None)
        self.__whileCpp_ExprAnd64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileCpp_ExprAnd66"):
                opp_val = getattr(old_value, "whileCpp_ExprAnd66", None)
                if opp_val == self:
                    setattr(old_value, "whileCpp_ExprAnd66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileCpp_ExprAnd66"):
                opp_val = getattr(value, "whileCpp_ExprAnd66", None)
                setattr(value, "whileCpp_ExprAnd66", self)

    @property
    def whileCpp_ExprAnd66(self):
        return self.__whileCpp_ExprAnd66

    @whileCpp_ExprAnd66.setter
    def whileCpp_ExprAnd66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileCpp_ExprAnd__whileCpp_ExprAnd66", None)
        self.__whileCpp_ExprAnd66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileCpp_ExprAnd64"):
                opp_val = getattr(old_value, "whileCpp_ExprAnd64", None)
                if opp_val == self:
                    setattr(old_value, "whileCpp_ExprAnd64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileCpp_ExprAnd64"):
                opp_val = getattr(value, "whileCpp_ExprAnd64", None)
                setattr(value, "whileCpp_ExprAnd64", self)

    @property
    def whileCpp_ExprAnd63(self):
        return self.__whileCpp_ExprAnd63

    @whileCpp_ExprAnd63.setter
    def whileCpp_ExprAnd63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileCpp_ExprAnd__whileCpp_ExprAnd63", None)
        self.__whileCpp_ExprAnd63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileCpp_ExprOr"):
                opp_val = getattr(old_value, "whileCpp_ExprOr", None)
                if opp_val == self:
                    setattr(old_value, "whileCpp_ExprOr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileCpp_ExprOr"):
                opp_val = getattr(value, "whileCpp_ExprOr", None)
                setattr(value, "whileCpp_ExprOr", self)

class whileCpp_ExprSimple:

    def __init__(self, nil: str, vari: str, symb: str, exprHead: str, exprTail: str, nomSymb: str, whileCpp_ExprSimple: "whileCpp_Expr" = None, whileCpp_ExprSimple60: set["whileCpp_Expr"] = None, whileCpp_ExprSimple79: "whileCpp_ExprEq" = None, whileCpp_ExprSimple52: "whileCpp_Cons" = None, whileCpp_ExprSimple54: "whileCpp_Expr" = None, whileCpp_ExprSimple57: "whileCpp_Expr" = None, whileCpp_ExprSimple82: "whileCpp_ExprEq" = None):
        self.nil = nil
        self.vari = vari
        self.symb = symb
        self.exprHead = exprHead
        self.exprTail = exprTail
        self.nomSymb = nomSymb
        self.whileCpp_ExprSimple = whileCpp_ExprSimple
        self.whileCpp_ExprSimple60 = whileCpp_ExprSimple60 if whileCpp_ExprSimple60 is not None else set()
        self.whileCpp_ExprSimple79 = whileCpp_ExprSimple79
        self.whileCpp_ExprSimple52 = whileCpp_ExprSimple52
        self.whileCpp_ExprSimple54 = whileCpp_ExprSimple54
        self.whileCpp_ExprSimple57 = whileCpp_ExprSimple57
        self.whileCpp_ExprSimple82 = whileCpp_ExprSimple82
        
    @property
    def vari(self) -> str:
        return self.__vari

    @vari.setter
    def vari(self, vari: str):
        self.__vari = vari

    @property
    def nomSymb(self) -> str:
        return self.__nomSymb

    @nomSymb.setter
    def nomSymb(self, nomSymb: str):
        self.__nomSymb = nomSymb

    @property
    def exprHead(self) -> str:
        return self.__exprHead

    @exprHead.setter
    def exprHead(self, exprHead: str):
        self.__exprHead = exprHead

    @property
    def exprTail(self) -> str:
        return self.__exprTail

    @exprTail.setter
    def exprTail(self, exprTail: str):
        self.__exprTail = exprTail

    @property
    def symb(self) -> str:
        return self.__symb

    @symb.setter
    def symb(self, symb: str):
        self.__symb = symb

    @property
    def nil(self) -> str:
        return self.__nil

    @nil.setter
    def nil(self, nil: str):
        self.__nil = nil

    @property
    def whileCpp_ExprSimple82(self):
        return self.__whileCpp_ExprSimple82

    @whileCpp_ExprSimple82.setter
    def whileCpp_ExprSimple82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileCpp_ExprSimple__whileCpp_ExprSimple82", None)
        self.__whileCpp_ExprSimple82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileCpp_ExprEq81"):
                opp_val = getattr(old_value, "whileCpp_ExprEq81", None)
                if opp_val == self:
                    setattr(old_value, "whileCpp_ExprEq81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileCpp_ExprEq81"):
                opp_val = getattr(value, "whileCpp_ExprEq81", None)
                setattr(value, "whileCpp_ExprEq81", self)

    @property
    def whileCpp_ExprSimple79(self):
        return self.__whileCpp_ExprSimple79

    @whileCpp_ExprSimple79.setter
    def whileCpp_ExprSimple79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileCpp_ExprSimple__whileCpp_ExprSimple79", None)
        self.__whileCpp_ExprSimple79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileCpp_ExprEq78"):
                opp_val = getattr(old_value, "whileCpp_ExprEq78", None)
                if opp_val == self:
                    setattr(old_value, "whileCpp_ExprEq78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileCpp_ExprEq78"):
                opp_val = getattr(value, "whileCpp_ExprEq78", None)
                setattr(value, "whileCpp_ExprEq78", self)

    @property
    def whileCpp_ExprSimple60(self):
        return self.__whileCpp_ExprSimple60

    @whileCpp_ExprSimple60.setter
    def whileCpp_ExprSimple60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileCpp_ExprSimple__whileCpp_ExprSimple60", None)
        self.__whileCpp_ExprSimple60 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "whileCpp_Expr61"):
                    opp_val = getattr(item, "whileCpp_Expr61", None)
                    
                    if opp_val == self:
                        setattr(item, "whileCpp_Expr61", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "whileCpp_Expr61"):
                    opp_val = getattr(item, "whileCpp_Expr61", None)
                    
                    setattr(item, "whileCpp_Expr61", self)
                    

    @property
    def whileCpp_ExprSimple54(self):
        return self.__whileCpp_ExprSimple54

    @whileCpp_ExprSimple54.setter
    def whileCpp_ExprSimple54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileCpp_ExprSimple__whileCpp_ExprSimple54", None)
        self.__whileCpp_ExprSimple54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileCpp_Expr55"):
                opp_val = getattr(old_value, "whileCpp_Expr55", None)
                if opp_val == self:
                    setattr(old_value, "whileCpp_Expr55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileCpp_Expr55"):
                opp_val = getattr(value, "whileCpp_Expr55", None)
                setattr(value, "whileCpp_Expr55", self)

    @property
    def whileCpp_ExprSimple57(self):
        return self.__whileCpp_ExprSimple57

    @whileCpp_ExprSimple57.setter
    def whileCpp_ExprSimple57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileCpp_ExprSimple__whileCpp_ExprSimple57", None)
        self.__whileCpp_ExprSimple57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileCpp_Expr58"):
                opp_val = getattr(old_value, "whileCpp_Expr58", None)
                if opp_val == self:
                    setattr(old_value, "whileCpp_Expr58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileCpp_Expr58"):
                opp_val = getattr(value, "whileCpp_Expr58", None)
                setattr(value, "whileCpp_Expr58", self)

    @property
    def whileCpp_ExprSimple(self):
        return self.__whileCpp_ExprSimple

    @whileCpp_ExprSimple.setter
    def whileCpp_ExprSimple(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileCpp_ExprSimple__whileCpp_ExprSimple", None)
        self.__whileCpp_ExprSimple = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileCpp_Expr48"):
                opp_val = getattr(old_value, "whileCpp_Expr48", None)
                if opp_val == self:
                    setattr(old_value, "whileCpp_Expr48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileCpp_Expr48"):
                opp_val = getattr(value, "whileCpp_Expr48", None)
                setattr(value, "whileCpp_Expr48", self)

    @property
    def whileCpp_ExprSimple52(self):
        return self.__whileCpp_ExprSimple52

    @whileCpp_ExprSimple52.setter
    def whileCpp_ExprSimple52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileCpp_ExprSimple__whileCpp_ExprSimple52", None)
        self.__whileCpp_ExprSimple52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileCpp_Cons"):
                opp_val = getattr(old_value, "whileCpp_Cons", None)
                if opp_val == self:
                    setattr(old_value, "whileCpp_Cons", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileCpp_Cons"):
                opp_val = getattr(value, "whileCpp_Cons", None)
                setattr(value, "whileCpp_Cons", self)

class whileCpp_Input:

    def __init__(self, varIn: str, whileCpp_Input: "whileCpp_Definition" = None):
        self.varIn = varIn
        self.whileCpp_Input = whileCpp_Input
        
    @property
    def varIn(self) -> str:
        return self.__varIn

    @varIn.setter
    def varIn(self, varIn: str):
        self.__varIn = varIn

    @property
    def whileCpp_Input(self):
        return self.__whileCpp_Input

    @whileCpp_Input.setter
    def whileCpp_Input(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileCpp_Input__whileCpp_Input", None)
        self.__whileCpp_Input = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileCpp_Definition4"):
                opp_val = getattr(old_value, "whileCpp_Definition4", None)
                if opp_val == self:
                    setattr(old_value, "whileCpp_Definition4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileCpp_Definition4"):
                opp_val = getattr(value, "whileCpp_Definition4", None)
                setattr(value, "whileCpp_Definition4", self)

class whileCpp_Definition:

    pass
class whileCpp_Function:

    def __init__(self, nom: str, whileCpp_Function: "whileCpp_Program" = None, whileCpp_Function2: "whileCpp_Definition" = None):
        self.nom = nom
        self.whileCpp_Function = whileCpp_Function
        self.whileCpp_Function2 = whileCpp_Function2
        
    @property
    def nom(self) -> str:
        return self.__nom

    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def whileCpp_Function2(self):
        return self.__whileCpp_Function2

    @whileCpp_Function2.setter
    def whileCpp_Function2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileCpp_Function__whileCpp_Function2", None)
        self.__whileCpp_Function2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileCpp_Definition"):
                opp_val = getattr(old_value, "whileCpp_Definition", None)
                if opp_val == self:
                    setattr(old_value, "whileCpp_Definition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileCpp_Definition"):
                opp_val = getattr(value, "whileCpp_Definition", None)
                setattr(value, "whileCpp_Definition", self)

    @property
    def whileCpp_Function(self):
        return self.__whileCpp_Function

    @whileCpp_Function.setter
    def whileCpp_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileCpp_Function__whileCpp_Function", None)
        self.__whileCpp_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileCpp_Program"):
                opp_val = getattr(old_value, "whileCpp_Program", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileCpp_Program"):
                opp_val = getattr(value, "whileCpp_Program", None)
                if opp_val is None:
                    setattr(value, "whileCpp_Program", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class whileCpp_Program:

    pass
class whileCpp_Command:

    def __init__(self, nop: str, whileCpp_Command: "whileCpp_Commands" = None, whileCpp_Command12: "whileCpp_Vars" = None, whileCpp_Command14: "whileCpp_Exprs" = None, whileCpp_Command16: "whileCpp_CommandWhile" = None, whileCpp_Command18: "whileCpp_CommandIf" = None, whileCpp_Command20: "whileCpp_CommandForEach" = None):
        self.nop = nop
        self.whileCpp_Command = whileCpp_Command
        self.whileCpp_Command12 = whileCpp_Command12
        self.whileCpp_Command14 = whileCpp_Command14
        self.whileCpp_Command16 = whileCpp_Command16
        self.whileCpp_Command18 = whileCpp_Command18
        self.whileCpp_Command20 = whileCpp_Command20
        
    @property
    def nop(self) -> str:
        return self.__nop

    @nop.setter
    def nop(self, nop: str):
        self.__nop = nop

    @property
    def whileCpp_Command20(self):
        return self.__whileCpp_Command20

    @whileCpp_Command20.setter
    def whileCpp_Command20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileCpp_Command__whileCpp_Command20", None)
        self.__whileCpp_Command20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileCpp_CommandForEach"):
                opp_val = getattr(old_value, "whileCpp_CommandForEach", None)
                if opp_val == self:
                    setattr(old_value, "whileCpp_CommandForEach", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileCpp_CommandForEach"):
                opp_val = getattr(value, "whileCpp_CommandForEach", None)
                setattr(value, "whileCpp_CommandForEach", self)

    @property
    def whileCpp_Command12(self):
        return self.__whileCpp_Command12

    @whileCpp_Command12.setter
    def whileCpp_Command12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileCpp_Command__whileCpp_Command12", None)
        self.__whileCpp_Command12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileCpp_Vars"):
                opp_val = getattr(old_value, "whileCpp_Vars", None)
                if opp_val == self:
                    setattr(old_value, "whileCpp_Vars", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileCpp_Vars"):
                opp_val = getattr(value, "whileCpp_Vars", None)
                setattr(value, "whileCpp_Vars", self)

    @property
    def whileCpp_Command(self):
        return self.__whileCpp_Command

    @whileCpp_Command.setter
    def whileCpp_Command(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileCpp_Command__whileCpp_Command", None)
        self.__whileCpp_Command = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileCpp_Commands10"):
                opp_val = getattr(old_value, "whileCpp_Commands10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileCpp_Commands10"):
                opp_val = getattr(value, "whileCpp_Commands10", None)
                if opp_val is None:
                    setattr(value, "whileCpp_Commands10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def whileCpp_Command18(self):
        return self.__whileCpp_Command18

    @whileCpp_Command18.setter
    def whileCpp_Command18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileCpp_Command__whileCpp_Command18", None)
        self.__whileCpp_Command18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileCpp_CommandIf"):
                opp_val = getattr(old_value, "whileCpp_CommandIf", None)
                if opp_val == self:
                    setattr(old_value, "whileCpp_CommandIf", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileCpp_CommandIf"):
                opp_val = getattr(value, "whileCpp_CommandIf", None)
                setattr(value, "whileCpp_CommandIf", self)

    @property
    def whileCpp_Command16(self):
        return self.__whileCpp_Command16

    @whileCpp_Command16.setter
    def whileCpp_Command16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileCpp_Command__whileCpp_Command16", None)
        self.__whileCpp_Command16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileCpp_CommandWhile"):
                opp_val = getattr(old_value, "whileCpp_CommandWhile", None)
                if opp_val == self:
                    setattr(old_value, "whileCpp_CommandWhile", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileCpp_CommandWhile"):
                opp_val = getattr(value, "whileCpp_CommandWhile", None)
                setattr(value, "whileCpp_CommandWhile", self)

    @property
    def whileCpp_Command14(self):
        return self.__whileCpp_Command14

    @whileCpp_Command14.setter
    def whileCpp_Command14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileCpp_Command__whileCpp_Command14", None)
        self.__whileCpp_Command14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileCpp_Exprs"):
                opp_val = getattr(old_value, "whileCpp_Exprs", None)
                if opp_val == self:
                    setattr(old_value, "whileCpp_Exprs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileCpp_Exprs"):
                opp_val = getattr(value, "whileCpp_Exprs", None)
                setattr(value, "whileCpp_Exprs", self)

class whileCpp_Vars:

    def __init__(self, varGen: str, whileCpp_Vars: "whileCpp_Command" = None):
        self.varGen = varGen
        self.whileCpp_Vars = whileCpp_Vars
        
    @property
    def varGen(self) -> str:
        return self.__varGen

    @varGen.setter
    def varGen(self, varGen: str):
        self.__varGen = varGen

    @property
    def whileCpp_Vars(self):
        return self.__whileCpp_Vars

    @whileCpp_Vars.setter
    def whileCpp_Vars(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileCpp_Vars__whileCpp_Vars", None)
        self.__whileCpp_Vars = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileCpp_Command12"):
                opp_val = getattr(old_value, "whileCpp_Command12", None)
                if opp_val == self:
                    setattr(old_value, "whileCpp_Command12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileCpp_Command12"):
                opp_val = getattr(value, "whileCpp_Command12", None)
                setattr(value, "whileCpp_Command12", self)

class whileCpp_Output:

    def __init__(self, varOut: str, whileCpp_Output: "whileCpp_Definition" = None):
        self.varOut = varOut
        self.whileCpp_Output = whileCpp_Output
        
    @property
    def varOut(self) -> str:
        return self.__varOut

    @varOut.setter
    def varOut(self, varOut: str):
        self.__varOut = varOut

    @property
    def whileCpp_Output(self):
        return self.__whileCpp_Output

    @whileCpp_Output.setter
    def whileCpp_Output(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileCpp_Output__whileCpp_Output", None)
        self.__whileCpp_Output = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileCpp_Definition8"):
                opp_val = getattr(old_value, "whileCpp_Definition8", None)
                if opp_val == self:
                    setattr(old_value, "whileCpp_Definition8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileCpp_Definition8"):
                opp_val = getattr(value, "whileCpp_Definition8", None)
                setattr(value, "whileCpp_Definition8", self)

class whileCpp_Commands:

    pass