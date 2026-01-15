from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class myDsl_OpAccSucc:

    def __init__(self, op: str, myDsl_OpAccSucc: "myDsl_AccSucc" = None):
        self.op = op
        self.myDsl_OpAccSucc = myDsl_OpAccSucc
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def myDsl_OpAccSucc(self):
        return self.__myDsl_OpAccSucc

    @myDsl_OpAccSucc.setter
    def myDsl_OpAccSucc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_OpAccSucc__myDsl_OpAccSucc", None)
        self.__myDsl_OpAccSucc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_AccSucc83"):
                opp_val = getattr(old_value, "myDsl_AccSucc83", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_AccSucc83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_AccSucc83"):
                opp_val = getattr(value, "myDsl_AccSucc83", None)
                setattr(value, "myDsl_AccSucc83", self)

class myDsl_OpConstructeur:

    def __init__(self, op: str, myDsl_OpConstructeur: "myDsl_ABin" = None):
        self.op = op
        self.myDsl_OpConstructeur = myDsl_OpConstructeur
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def myDsl_OpConstructeur(self):
        return self.__myDsl_OpConstructeur

    @myDsl_OpConstructeur.setter
    def myDsl_OpConstructeur(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_OpConstructeur__myDsl_OpConstructeur", None)
        self.__myDsl_OpConstructeur = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ABin75"):
                opp_val = getattr(old_value, "myDsl_ABin75", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ABin75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ABin75"):
                opp_val = getattr(value, "myDsl_ABin75", None)
                setattr(value, "myDsl_ABin75", self)

class Condition:

    pass
class myDsl_Not(Condition):

    def __init__(self, not: str, myDsl_Not: "myDsl_Expression" = None):
        self.not = not
        self.myDsl_Not = myDsl_Not
        
    @property
    def not(self) -> str:
        return self.__not

    @not.setter
    def not(self, not: str):
        self.__not = not

    @property
    def myDsl_Not(self):
        return self.__myDsl_Not

    @myDsl_Not.setter
    def myDsl_Not(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Not__myDsl_Not", None)
        self.__myDsl_Not = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression88"):
                opp_val = getattr(old_value, "myDsl_Expression88", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression88"):
                opp_val = getattr(value, "myDsl_Expression88", None)
                setattr(value, "myDsl_Expression88", self)

class myDsl_ABin:

    pass
class myDsl_Nill:

    def __init__(self, nil: str, myDsl_Nill: "myDsl_ExprSimple" = None):
        self.nil = nil
        self.myDsl_Nill = myDsl_Nill
        
    @property
    def nil(self) -> str:
        return self.__nil

    @nil.setter
    def nil(self, nil: str):
        self.__nil = nil

    @property
    def myDsl_Nill(self):
        return self.__myDsl_Nill

    @myDsl_Nill.setter
    def myDsl_Nill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Nill__myDsl_Nill", None)
        self.__myDsl_Nill = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ExprSimple48"):
                opp_val = getattr(old_value, "myDsl_ExprSimple48", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ExprSimple48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ExprSimple48"):
                opp_val = getattr(value, "myDsl_ExprSimple48", None)
                setattr(value, "myDsl_ExprSimple48", self)

class myDsl_ExprSimple:

    def __init__(self, symb: str, myDsl_ExprSimple55: "myDsl_AccSucc" = None, myDsl_ExprSimple57: "myDsl_ElemSimple" = None, myDsl_ExprSimple59: "myDsl_Lexpr" = None, myDsl_ExprSimple68: "myDsl_Condition" = None, myDsl_ExprSimple: "myDsl_Expression" = None, myDsl_ExprSimple48: "myDsl_Nill" = None, myDsl_ExprSimple50: "myDsl_Variable" = None, myDsl_ExprSimple53: "myDsl_ABin" = None, myDsl_ExprSimple86: "myDsl_AccSucc" = None):
        self.symb = symb
        self.myDsl_ExprSimple55 = myDsl_ExprSimple55
        self.myDsl_ExprSimple57 = myDsl_ExprSimple57
        self.myDsl_ExprSimple59 = myDsl_ExprSimple59
        self.myDsl_ExprSimple68 = myDsl_ExprSimple68
        self.myDsl_ExprSimple = myDsl_ExprSimple
        self.myDsl_ExprSimple48 = myDsl_ExprSimple48
        self.myDsl_ExprSimple50 = myDsl_ExprSimple50
        self.myDsl_ExprSimple53 = myDsl_ExprSimple53
        self.myDsl_ExprSimple86 = myDsl_ExprSimple86
        
    @property
    def symb(self) -> str:
        return self.__symb

    @symb.setter
    def symb(self, symb: str):
        self.__symb = symb

    @property
    def myDsl_ExprSimple48(self):
        return self.__myDsl_ExprSimple48

    @myDsl_ExprSimple48.setter
    def myDsl_ExprSimple48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ExprSimple__myDsl_ExprSimple48", None)
        self.__myDsl_ExprSimple48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Nill"):
                opp_val = getattr(old_value, "myDsl_Nill", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Nill", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Nill"):
                opp_val = getattr(value, "myDsl_Nill", None)
                setattr(value, "myDsl_Nill", self)

    @property
    def myDsl_ExprSimple59(self):
        return self.__myDsl_ExprSimple59

    @myDsl_ExprSimple59.setter
    def myDsl_ExprSimple59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ExprSimple__myDsl_ExprSimple59", None)
        self.__myDsl_ExprSimple59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Lexpr"):
                opp_val = getattr(old_value, "myDsl_Lexpr", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Lexpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Lexpr"):
                opp_val = getattr(value, "myDsl_Lexpr", None)
                setattr(value, "myDsl_Lexpr", self)

    @property
    def myDsl_ExprSimple53(self):
        return self.__myDsl_ExprSimple53

    @myDsl_ExprSimple53.setter
    def myDsl_ExprSimple53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ExprSimple__myDsl_ExprSimple53", None)
        self.__myDsl_ExprSimple53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ABin"):
                opp_val = getattr(old_value, "myDsl_ABin", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ABin", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ABin"):
                opp_val = getattr(value, "myDsl_ABin", None)
                setattr(value, "myDsl_ABin", self)

    @property
    def myDsl_ExprSimple55(self):
        return self.__myDsl_ExprSimple55

    @myDsl_ExprSimple55.setter
    def myDsl_ExprSimple55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ExprSimple__myDsl_ExprSimple55", None)
        self.__myDsl_ExprSimple55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_AccSucc"):
                opp_val = getattr(old_value, "myDsl_AccSucc", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_AccSucc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_AccSucc"):
                opp_val = getattr(value, "myDsl_AccSucc", None)
                setattr(value, "myDsl_AccSucc", self)

    @property
    def myDsl_ExprSimple86(self):
        return self.__myDsl_ExprSimple86

    @myDsl_ExprSimple86.setter
    def myDsl_ExprSimple86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ExprSimple__myDsl_ExprSimple86", None)
        self.__myDsl_ExprSimple86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_AccSucc85"):
                opp_val = getattr(old_value, "myDsl_AccSucc85", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_AccSucc85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_AccSucc85"):
                opp_val = getattr(value, "myDsl_AccSucc85", None)
                setattr(value, "myDsl_AccSucc85", self)

    @property
    def myDsl_ExprSimple57(self):
        return self.__myDsl_ExprSimple57

    @myDsl_ExprSimple57.setter
    def myDsl_ExprSimple57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ExprSimple__myDsl_ExprSimple57", None)
        self.__myDsl_ExprSimple57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ElemSimple"):
                opp_val = getattr(old_value, "myDsl_ElemSimple", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ElemSimple", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ElemSimple"):
                opp_val = getattr(value, "myDsl_ElemSimple", None)
                setattr(value, "myDsl_ElemSimple", self)

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
            if hasattr(old_value, "myDsl_Expression46"):
                opp_val = getattr(old_value, "myDsl_Expression46", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression46"):
                opp_val = getattr(value, "myDsl_Expression46", None)
                setattr(value, "myDsl_Expression46", self)

    @property
    def myDsl_ExprSimple50(self):
        return self.__myDsl_ExprSimple50

    @myDsl_ExprSimple50.setter
    def myDsl_ExprSimple50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ExprSimple__myDsl_ExprSimple50", None)
        self.__myDsl_ExprSimple50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Variable51"):
                opp_val = getattr(old_value, "myDsl_Variable51", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Variable51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Variable51"):
                opp_val = getattr(value, "myDsl_Variable51", None)
                setattr(value, "myDsl_Variable51", self)

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
            if hasattr(old_value, "myDsl_Condition67"):
                opp_val = getattr(old_value, "myDsl_Condition67", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Condition67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Condition67"):
                opp_val = getattr(value, "myDsl_Condition67", None)
                setattr(value, "myDsl_Condition67", self)

class myDsl_Condition:

    pass
class myDsl_Nop:

    def __init__(self, nop: str):
        self.nop = nop
        
    @property
    def nop(self) -> str:
        return self.__nop

    @nop.setter
    def nop(self, nop: str):
        self.__nop = nop

class myDsl_ForEach:

    pass
class myDsl_COMPARATEUR:

    def __init__(self, comparateur: str, myDsl_COMPARATEUR: "myDsl_Condition" = None):
        self.comparateur = comparateur
        self.myDsl_COMPARATEUR = myDsl_COMPARATEUR
        
    @property
    def comparateur(self) -> str:
        return self.__comparateur

    @comparateur.setter
    def comparateur(self, comparateur: str):
        self.__comparateur = comparateur

    @property
    def myDsl_COMPARATEUR(self):
        return self.__myDsl_COMPARATEUR

    @myDsl_COMPARATEUR.setter
    def myDsl_COMPARATEUR(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_COMPARATEUR__myDsl_COMPARATEUR", None)
        self.__myDsl_COMPARATEUR = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Condition70"):
                opp_val = getattr(old_value, "myDsl_Condition70", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Condition70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Condition70"):
                opp_val = getattr(value, "myDsl_Condition70", None)
                setattr(value, "myDsl_Condition70", self)

class myDsl_Lexpr:

    pass
class myDsl_ElemSimple:

    def __init__(self, symb: str, myDsl_ElemSimple: "myDsl_ExprSimple" = None, myDsl_ElemSimple64: "myDsl_Lexpr" = None):
        self.symb = symb
        self.myDsl_ElemSimple = myDsl_ElemSimple
        self.myDsl_ElemSimple64 = myDsl_ElemSimple64
        
    @property
    def symb(self) -> str:
        return self.__symb

    @symb.setter
    def symb(self, symb: str):
        self.__symb = symb

    @property
    def myDsl_ElemSimple64(self):
        return self.__myDsl_ElemSimple64

    @myDsl_ElemSimple64.setter
    def myDsl_ElemSimple64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ElemSimple__myDsl_ElemSimple64", None)
        self.__myDsl_ElemSimple64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Lexpr65"):
                opp_val = getattr(old_value, "myDsl_Lexpr65", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Lexpr65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Lexpr65"):
                opp_val = getattr(value, "myDsl_Lexpr65", None)
                setattr(value, "myDsl_Lexpr65", self)

    @property
    def myDsl_ElemSimple(self):
        return self.__myDsl_ElemSimple

    @myDsl_ElemSimple.setter
    def myDsl_ElemSimple(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ElemSimple__myDsl_ElemSimple", None)
        self.__myDsl_ElemSimple = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ExprSimple57"):
                opp_val = getattr(old_value, "myDsl_ExprSimple57", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ExprSimple57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ExprSimple57"):
                opp_val = getattr(value, "myDsl_ExprSimple57", None)
                setattr(value, "myDsl_ExprSimple57", self)

class myDsl_AccSucc:

    pass
class myDsl_EObject:

    pass
class myDsl_Commande:

    pass
class myDsl_Output:

    def __init__(self, out: str, myDsl_Output: "myDsl_Fonction" = None):
        self.out = out
        self.myDsl_Output = myDsl_Output
        
    @property
    def out(self) -> str:
        return self.__out

    @out.setter
    def out(self, out: str):
        self.__out = out

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
            if hasattr(old_value, "myDsl_Fonction6"):
                opp_val = getattr(old_value, "myDsl_Fonction6", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Fonction6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Fonction6"):
                opp_val = getattr(value, "myDsl_Fonction6", None)
                setattr(value, "myDsl_Fonction6", self)

class myDsl_For:

    pass
class myDsl_While:

    pass
class myDsl_If:

    pass
class myDsl_Expression:

    pass
class myDsl_Variable:

    def __init__(self, variable: str, myDsl_Variable: "myDsl_Affectation" = None, myDsl_Variable51: "myDsl_ExprSimple" = None):
        self.variable = variable
        self.myDsl_Variable = myDsl_Variable
        self.myDsl_Variable51 = myDsl_Variable51
        
    @property
    def variable(self) -> str:
        return self.__variable

    @variable.setter
    def variable(self, variable: str):
        self.__variable = variable

    @property
    def myDsl_Variable(self):
        return self.__myDsl_Variable

    @myDsl_Variable.setter
    def myDsl_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Variable__myDsl_Variable", None)
        self.__myDsl_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Affectation"):
                opp_val = getattr(old_value, "myDsl_Affectation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Affectation"):
                opp_val = getattr(value, "myDsl_Affectation", None)
                if opp_val is None:
                    setattr(value, "myDsl_Affectation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Variable51(self):
        return self.__myDsl_Variable51

    @myDsl_Variable51.setter
    def myDsl_Variable51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Variable__myDsl_Variable51", None)
        self.__myDsl_Variable51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ExprSimple50"):
                opp_val = getattr(old_value, "myDsl_ExprSimple50", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ExprSimple50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ExprSimple50"):
                opp_val = getattr(value, "myDsl_ExprSimple50", None)
                setattr(value, "myDsl_ExprSimple50", self)

class myDsl_Affectation:

    pass
class myDsl_Commandes:

    pass
class myDsl_Input:

    def __init__(self, in: str, myDsl_Input: "myDsl_Fonction" = None):
        self.in = in
        self.myDsl_Input = myDsl_Input
        
    @property
    def in(self) -> str:
        return self.__in

    @in.setter
    def in(self, in: str):
        self.__in = in

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
            if hasattr(old_value, "myDsl_Fonction2"):
                opp_val = getattr(old_value, "myDsl_Fonction2", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Fonction2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Fonction2"):
                opp_val = getattr(value, "myDsl_Fonction2", None)
                setattr(value, "myDsl_Fonction2", self)

class myDsl_Fonction:

    def __init__(self, nom: str, myDsl_Fonction: "myDsl_Program" = None, myDsl_Fonction2: "myDsl_Input" = None, myDsl_Fonction4: "myDsl_Commandes" = None, myDsl_Fonction6: "myDsl_Output" = None):
        self.nom = nom
        self.myDsl_Fonction = myDsl_Fonction
        self.myDsl_Fonction2 = myDsl_Fonction2
        self.myDsl_Fonction4 = myDsl_Fonction4
        self.myDsl_Fonction6 = myDsl_Fonction6
        
    @property
    def nom(self) -> str:
        return self.__nom

    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

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
    def myDsl_Fonction2(self):
        return self.__myDsl_Fonction2

    @myDsl_Fonction2.setter
    def myDsl_Fonction2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Fonction__myDsl_Fonction2", None)
        self.__myDsl_Fonction2 = value
        
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
            if hasattr(old_value, "myDsl_Program"):
                opp_val = getattr(old_value, "myDsl_Program", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Program"):
                opp_val = getattr(value, "myDsl_Program", None)
                if opp_val is None:
                    setattr(value, "myDsl_Program", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_Program:

    pass