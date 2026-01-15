from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class myDsl_ExprEq:

    pass
class myDsl_ExprNotDo:

    pass
class myDsl_ExprNotNot:

    pass
class myDsl_ExprNot:

    pass
class myDsl_ExprOr:

    pass
class myDsl_SymboleEx:

    def __init__(self, p: str, myDsl_SymboleEx: "myDsl_ExprSimple" = None, myDsl_SymboleEx89: "myDsl_LExpr" = None):
        self.p = p
        self.myDsl_SymboleEx = myDsl_SymboleEx
        self.myDsl_SymboleEx89 = myDsl_SymboleEx89
        
    @property
    def p(self) -> str:
        return self.__p

    @p.setter
    def p(self, p: str):
        self.__p = p

    @property
    def myDsl_SymboleEx(self):
        return self.__myDsl_SymboleEx

    @myDsl_SymboleEx.setter
    def myDsl_SymboleEx(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_SymboleEx__myDsl_SymboleEx", None)
        self.__myDsl_SymboleEx = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ExprSimple76"):
                opp_val = getattr(old_value, "myDsl_ExprSimple76", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ExprSimple76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ExprSimple76"):
                opp_val = getattr(value, "myDsl_ExprSimple76", None)
                setattr(value, "myDsl_ExprSimple76", self)

    @property
    def myDsl_SymboleEx89(self):
        return self.__myDsl_SymboleEx89

    @myDsl_SymboleEx89.setter
    def myDsl_SymboleEx89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_SymboleEx__myDsl_SymboleEx89", None)
        self.__myDsl_SymboleEx89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_LExpr90"):
                opp_val = getattr(old_value, "myDsl_LExpr90", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_LExpr90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_LExpr90"):
                opp_val = getattr(value, "myDsl_LExpr90", None)
                setattr(value, "myDsl_LExpr90", self)

class myDsl_Tl:

    pass
class myDsl_Hd:

    pass
class myDsl_Liste:

    pass
class myDsl_Cons:

    pass
class myDsl_ExprSimple:

    def __init__(self, vide: str, variable: str, symbole: str, myDsl_ExprSimple: "myDsl_Expr" = None, myDsl_ExprSimple68: "myDsl_Cons" = None, myDsl_ExprSimple70: "myDsl_Liste" = None, myDsl_ExprSimple72: "myDsl_Hd" = None, myDsl_ExprSimple74: "myDsl_Tl" = None, myDsl_ExprSimple76: "myDsl_SymboleEx" = None, myDsl_ExprSimple115: "myDsl_ExprEq" = None, myDsl_ExprSimple118: "myDsl_ExprEq" = None):
        self.vide = vide
        self.variable = variable
        self.symbole = symbole
        self.myDsl_ExprSimple = myDsl_ExprSimple
        self.myDsl_ExprSimple68 = myDsl_ExprSimple68
        self.myDsl_ExprSimple70 = myDsl_ExprSimple70
        self.myDsl_ExprSimple72 = myDsl_ExprSimple72
        self.myDsl_ExprSimple74 = myDsl_ExprSimple74
        self.myDsl_ExprSimple76 = myDsl_ExprSimple76
        self.myDsl_ExprSimple115 = myDsl_ExprSimple115
        self.myDsl_ExprSimple118 = myDsl_ExprSimple118
        
    @property
    def variable(self) -> str:
        return self.__variable

    @variable.setter
    def variable(self, variable: str):
        self.__variable = variable

    @property
    def vide(self) -> str:
        return self.__vide

    @vide.setter
    def vide(self, vide: str):
        self.__vide = vide

    @property
    def symbole(self) -> str:
        return self.__symbole

    @symbole.setter
    def symbole(self, symbole: str):
        self.__symbole = symbole

    @property
    def myDsl_ExprSimple(self):
        return self.__myDsl_ExprSimple

    @myDsl_ExprSimple.setter
    def myDsl_ExprSimple(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ExprSimple__myDsl_ExprSimple", None)
        self.__myDsl_ExprSimple = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expr66"):
                opp_val = getattr(old_value, "myDsl_Expr66", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expr66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expr66"):
                opp_val = getattr(value, "myDsl_Expr66", None)
                setattr(value, "myDsl_Expr66", self)

    @property
    def myDsl_ExprSimple115(self):
        return self.__myDsl_ExprSimple115

    @myDsl_ExprSimple115.setter
    def myDsl_ExprSimple115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ExprSimple__myDsl_ExprSimple115", None)
        self.__myDsl_ExprSimple115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ExprEq114"):
                opp_val = getattr(old_value, "myDsl_ExprEq114", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ExprEq114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ExprEq114"):
                opp_val = getattr(value, "myDsl_ExprEq114", None)
                setattr(value, "myDsl_ExprEq114", self)

    @property
    def myDsl_ExprSimple70(self):
        return self.__myDsl_ExprSimple70

    @myDsl_ExprSimple70.setter
    def myDsl_ExprSimple70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ExprSimple__myDsl_ExprSimple70", None)
        self.__myDsl_ExprSimple70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Liste"):
                opp_val = getattr(old_value, "myDsl_Liste", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Liste", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Liste"):
                opp_val = getattr(value, "myDsl_Liste", None)
                setattr(value, "myDsl_Liste", self)

    @property
    def myDsl_ExprSimple72(self):
        return self.__myDsl_ExprSimple72

    @myDsl_ExprSimple72.setter
    def myDsl_ExprSimple72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ExprSimple__myDsl_ExprSimple72", None)
        self.__myDsl_ExprSimple72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Hd"):
                opp_val = getattr(old_value, "myDsl_Hd", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Hd", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Hd"):
                opp_val = getattr(value, "myDsl_Hd", None)
                setattr(value, "myDsl_Hd", self)

    @property
    def myDsl_ExprSimple76(self):
        return self.__myDsl_ExprSimple76

    @myDsl_ExprSimple76.setter
    def myDsl_ExprSimple76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ExprSimple__myDsl_ExprSimple76", None)
        self.__myDsl_ExprSimple76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_SymboleEx"):
                opp_val = getattr(old_value, "myDsl_SymboleEx", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_SymboleEx", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_SymboleEx"):
                opp_val = getattr(value, "myDsl_SymboleEx", None)
                setattr(value, "myDsl_SymboleEx", self)

    @property
    def myDsl_ExprSimple118(self):
        return self.__myDsl_ExprSimple118

    @myDsl_ExprSimple118.setter
    def myDsl_ExprSimple118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ExprSimple__myDsl_ExprSimple118", None)
        self.__myDsl_ExprSimple118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ExprEq117"):
                opp_val = getattr(old_value, "myDsl_ExprEq117", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ExprEq117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ExprEq117"):
                opp_val = getattr(value, "myDsl_ExprEq117", None)
                setattr(value, "myDsl_ExprEq117", self)

    @property
    def myDsl_ExprSimple68(self):
        return self.__myDsl_ExprSimple68

    @myDsl_ExprSimple68.setter
    def myDsl_ExprSimple68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ExprSimple__myDsl_ExprSimple68", None)
        self.__myDsl_ExprSimple68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Cons"):
                opp_val = getattr(old_value, "myDsl_Cons", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Cons", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Cons"):
                opp_val = getattr(value, "myDsl_Cons", None)
                setattr(value, "myDsl_Cons", self)

    @property
    def myDsl_ExprSimple74(self):
        return self.__myDsl_ExprSimple74

    @myDsl_ExprSimple74.setter
    def myDsl_ExprSimple74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ExprSimple__myDsl_ExprSimple74", None)
        self.__myDsl_ExprSimple74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Tl"):
                opp_val = getattr(old_value, "myDsl_Tl", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Tl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Tl"):
                opp_val = getattr(value, "myDsl_Tl", None)
                setattr(value, "myDsl_Tl", self)

class myDsl_ExprAnd:

    pass
class myDsl_LExpr:

    pass
class myDsl_Expr:

    pass
class myDsl_Exprs:

    pass
class myDsl_Vars:

    def __init__(self, var2: str, var3: str, myDsl_Vars: "myDsl_AffectVar" = None):
        self.var2 = var2
        self.var3 = var3
        self.myDsl_Vars = myDsl_Vars
        
    @property
    def var2(self) -> str:
        return self.__var2

    @var2.setter
    def var2(self, var2: str):
        self.__var2 = var2

    @property
    def var3(self) -> str:
        return self.__var3

    @var3.setter
    def var3(self, var3: str):
        self.__var3 = var3

    @property
    def myDsl_Vars(self):
        return self.__myDsl_Vars

    @myDsl_Vars.setter
    def myDsl_Vars(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Vars__myDsl_Vars", None)
        self.__myDsl_Vars = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_AffectVar25"):
                opp_val = getattr(old_value, "myDsl_AffectVar25", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_AffectVar25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_AffectVar25"):
                opp_val = getattr(value, "myDsl_AffectVar25", None)
                setattr(value, "myDsl_AffectVar25", self)

class myDsl_Foreach:

    pass
class myDsl_If:

    pass
class myDsl_For:

    pass
class myDsl_While:

    pass
class myDsl_AffectVar:

    pass
class myDsl_Commande:

    def __init__(self, nop: str, myDsl_Commande: "myDsl_Commandes" = None, myDsl_Commande13: "myDsl_Commandes" = None, myDsl_Commande15: "myDsl_AffectVar" = None, myDsl_Commande17: "myDsl_While" = None, myDsl_Commande19: "myDsl_For" = None, myDsl_Commande21: "myDsl_If" = None, myDsl_Commande23: "myDsl_Foreach" = None):
        self.nop = nop
        self.myDsl_Commande = myDsl_Commande
        self.myDsl_Commande13 = myDsl_Commande13
        self.myDsl_Commande15 = myDsl_Commande15
        self.myDsl_Commande17 = myDsl_Commande17
        self.myDsl_Commande19 = myDsl_Commande19
        self.myDsl_Commande21 = myDsl_Commande21
        self.myDsl_Commande23 = myDsl_Commande23
        
    @property
    def nop(self) -> str:
        return self.__nop

    @nop.setter
    def nop(self, nop: str):
        self.__nop = nop

    @property
    def myDsl_Commande19(self):
        return self.__myDsl_Commande19

    @myDsl_Commande19.setter
    def myDsl_Commande19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Commande__myDsl_Commande19", None)
        self.__myDsl_Commande19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_For"):
                opp_val = getattr(old_value, "myDsl_For", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_For", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_For"):
                opp_val = getattr(value, "myDsl_For", None)
                setattr(value, "myDsl_For", self)

    @property
    def myDsl_Commande15(self):
        return self.__myDsl_Commande15

    @myDsl_Commande15.setter
    def myDsl_Commande15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Commande__myDsl_Commande15", None)
        self.__myDsl_Commande15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_AffectVar"):
                opp_val = getattr(old_value, "myDsl_AffectVar", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_AffectVar", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_AffectVar"):
                opp_val = getattr(value, "myDsl_AffectVar", None)
                setattr(value, "myDsl_AffectVar", self)

    @property
    def myDsl_Commande17(self):
        return self.__myDsl_Commande17

    @myDsl_Commande17.setter
    def myDsl_Commande17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Commande__myDsl_Commande17", None)
        self.__myDsl_Commande17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_While"):
                opp_val = getattr(old_value, "myDsl_While", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_While", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_While"):
                opp_val = getattr(value, "myDsl_While", None)
                setattr(value, "myDsl_While", self)

    @property
    def myDsl_Commande23(self):
        return self.__myDsl_Commande23

    @myDsl_Commande23.setter
    def myDsl_Commande23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Commande__myDsl_Commande23", None)
        self.__myDsl_Commande23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Foreach"):
                opp_val = getattr(old_value, "myDsl_Foreach", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Foreach", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Foreach"):
                opp_val = getattr(value, "myDsl_Foreach", None)
                setattr(value, "myDsl_Foreach", self)

    @property
    def myDsl_Commande13(self):
        return self.__myDsl_Commande13

    @myDsl_Commande13.setter
    def myDsl_Commande13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Commande__myDsl_Commande13", None)
        self.__myDsl_Commande13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Commandes12"):
                opp_val = getattr(old_value, "myDsl_Commandes12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Commandes12"):
                opp_val = getattr(value, "myDsl_Commandes12", None)
                if opp_val is None:
                    setattr(value, "myDsl_Commandes12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Commande(self):
        return self.__myDsl_Commande

    @myDsl_Commande.setter
    def myDsl_Commande(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Commande__myDsl_Commande", None)
        self.__myDsl_Commande = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Commandes10"):
                opp_val = getattr(old_value, "myDsl_Commandes10", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Commandes10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Commandes10"):
                opp_val = getattr(value, "myDsl_Commandes10", None)
                setattr(value, "myDsl_Commandes10", self)

    @property
    def myDsl_Commande21(self):
        return self.__myDsl_Commande21

    @myDsl_Commande21.setter
    def myDsl_Commande21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Commande__myDsl_Commande21", None)
        self.__myDsl_Commande21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_If"):
                opp_val = getattr(old_value, "myDsl_If", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_If", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_If"):
                opp_val = getattr(value, "myDsl_If", None)
                setattr(value, "myDsl_If", self)

class myDsl_Commandes:

    pass
class myDsl_Input:

    def __init__(self, var1: str, var2: str, myDsl_Input: "myDsl_Fonction" = None):
        self.var1 = var1
        self.var2 = var2
        self.myDsl_Input = myDsl_Input
        
    @property
    def var1(self) -> str:
        return self.__var1

    @var1.setter
    def var1(self, var1: str):
        self.__var1 = var1

    @property
    def var2(self) -> str:
        return self.__var2

    @var2.setter
    def var2(self, var2: str):
        self.__var2 = var2

    @property
    def myDsl_Input(self):
        return self.__myDsl_Input

    @myDsl_Input.setter
    def myDsl_Input(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Input__myDsl_Input", None)
        self.__myDsl_Input = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Fonction4"):
                opp_val = getattr(old_value, "myDsl_Fonction4", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Fonction4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Fonction4"):
                opp_val = getattr(value, "myDsl_Fonction4", None)
                setattr(value, "myDsl_Fonction4", self)

class myDsl_Fonction:

    def __init__(self, symbole: str, myDsl_Fonction8: "myDsl_Output" = None, myDsl_Fonction: "myDsl_Programme" = None, myDsl_Fonction4: "myDsl_Input" = None, myDsl_Fonction6: "myDsl_Commandes" = None):
        self.symbole = symbole
        self.myDsl_Fonction8 = myDsl_Fonction8
        self.myDsl_Fonction = myDsl_Fonction
        self.myDsl_Fonction4 = myDsl_Fonction4
        self.myDsl_Fonction6 = myDsl_Fonction6
        
    @property
    def symbole(self) -> str:
        return self.__symbole

    @symbole.setter
    def symbole(self, symbole: str):
        self.__symbole = symbole

    @property
    def myDsl_Fonction6(self):
        return self.__myDsl_Fonction6

    @myDsl_Fonction6.setter
    def myDsl_Fonction6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Fonction__myDsl_Fonction6", None)
        self.__myDsl_Fonction6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Commandes"):
                opp_val = getattr(old_value, "myDsl_Commandes", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Commandes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Commandes"):
                opp_val = getattr(value, "myDsl_Commandes", None)
                setattr(value, "myDsl_Commandes", self)

    @property
    def myDsl_Fonction8(self):
        return self.__myDsl_Fonction8

    @myDsl_Fonction8.setter
    def myDsl_Fonction8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Fonction__myDsl_Fonction8", None)
        self.__myDsl_Fonction8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Output"):
                opp_val = getattr(old_value, "myDsl_Output", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Output", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Output"):
                opp_val = getattr(value, "myDsl_Output", None)
                setattr(value, "myDsl_Output", self)

    @property
    def myDsl_Fonction(self):
        return self.__myDsl_Fonction

    @myDsl_Fonction.setter
    def myDsl_Fonction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Fonction__myDsl_Fonction", None)
        self.__myDsl_Fonction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Programme2"):
                opp_val = getattr(old_value, "myDsl_Programme2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Programme2"):
                opp_val = getattr(value, "myDsl_Programme2", None)
                if opp_val is None:
                    setattr(value, "myDsl_Programme2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Fonction4(self):
        return self.__myDsl_Fonction4

    @myDsl_Fonction4.setter
    def myDsl_Fonction4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Fonction__myDsl_Fonction4", None)
        self.__myDsl_Fonction4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Input"):
                opp_val = getattr(old_value, "myDsl_Input", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Input", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Input"):
                opp_val = getattr(value, "myDsl_Input", None)
                setattr(value, "myDsl_Input", self)

class myDsl_Programme:

    pass
class myDsl_Model:

    pass
class myDsl_Output:

    def __init__(self, var1: str, var2: str, myDsl_Output: "myDsl_Fonction" = None):
        self.var1 = var1
        self.var2 = var2
        self.myDsl_Output = myDsl_Output
        
    @property
    def var1(self) -> str:
        return self.__var1

    @var1.setter
    def var1(self, var1: str):
        self.__var1 = var1

    @property
    def var2(self) -> str:
        return self.__var2

    @var2.setter
    def var2(self, var2: str):
        self.__var2 = var2

    @property
    def myDsl_Output(self):
        return self.__myDsl_Output

    @myDsl_Output.setter
    def myDsl_Output(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Output__myDsl_Output", None)
        self.__myDsl_Output = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Fonction8"):
                opp_val = getattr(old_value, "myDsl_Fonction8", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Fonction8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Fonction8"):
                opp_val = getattr(value, "myDsl_Fonction8", None)
                setattr(value, "myDsl_Fonction8", self)
