from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class myDsl_Not:

    def __init__(self, non: str, myDsl_Not50: "myDsl_Or" = None, myDsl_Not52: "myDsl_Eq" = None, myDsl_Not: "myDsl_Or" = None):
        self.non = non
        self.myDsl_Not50 = myDsl_Not50
        self.myDsl_Not52 = myDsl_Not52
        self.myDsl_Not = myDsl_Not
        
    @property
    def non(self) -> str:
        return self.__non

    @non.setter
    def non(self, non: str):
        self.__non = non

    @property
    def myDsl_Not52(self):
        return self.__myDsl_Not52

    @myDsl_Not52.setter
    def myDsl_Not52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Not__myDsl_Not52", None)
        self.__myDsl_Not52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Eq"):
                opp_val = getattr(old_value, "myDsl_Eq", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Eq", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Eq"):
                opp_val = getattr(value, "myDsl_Eq", None)
                setattr(value, "myDsl_Eq", self)

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
            if hasattr(old_value, "myDsl_Or47"):
                opp_val = getattr(old_value, "myDsl_Or47", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Or47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Or47"):
                opp_val = getattr(value, "myDsl_Or47", None)
                setattr(value, "myDsl_Or47", self)

    @property
    def myDsl_Not50(self):
        return self.__myDsl_Not50

    @myDsl_Not50.setter
    def myDsl_Not50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Not__myDsl_Not50", None)
        self.__myDsl_Not50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Or49"):
                opp_val = getattr(old_value, "myDsl_Or49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Or49"):
                opp_val = getattr(value, "myDsl_Or49", None)
                if opp_val is None:
                    setattr(value, "myDsl_Or49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_Or:

    pass
class myDsl_ExprTerm:

    def __init__(self, termVar: str, termSym: str, myDsl_ExprTerm: "myDsl_Expr" = None):
        self.termVar = termVar
        self.termSym = termSym
        self.myDsl_ExprTerm = myDsl_ExprTerm
        
    @property
    def termVar(self) -> str:
        return self.__termVar

    @termVar.setter
    def termVar(self, termVar: str):
        self.__termVar = termVar

    @property
    def termSym(self) -> str:
        return self.__termSym

    @termSym.setter
    def termSym(self, termSym: str):
        self.__termSym = termSym

    @property
    def myDsl_ExprTerm(self):
        return self.__myDsl_ExprTerm

    @myDsl_ExprTerm.setter
    def myDsl_ExprTerm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ExprTerm__myDsl_ExprTerm", None)
        self.__myDsl_ExprTerm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expr40"):
                opp_val = getattr(old_value, "myDsl_Expr40", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expr40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expr40"):
                opp_val = getattr(value, "myDsl_Expr40", None)
                setattr(value, "myDsl_Expr40", self)

class myDsl_And:

    pass
class myDsl_ExprSimple:

    def __init__(self, mot: str, myDsl_ExprSimple62: "myDsl_Lexpr" = None, myDsl_ExprSimple64: "myDsl_Expr" = None, myDsl_ExprSimple: "myDsl_Expr" = None):
        self.mot = mot
        self.myDsl_ExprSimple62 = myDsl_ExprSimple62
        self.myDsl_ExprSimple64 = myDsl_ExprSimple64
        self.myDsl_ExprSimple = myDsl_ExprSimple
        
    @property
    def mot(self) -> str:
        return self.__mot

    @mot.setter
    def mot(self, mot: str):
        self.__mot = mot

    @property
    def myDsl_ExprSimple62(self):
        return self.__myDsl_ExprSimple62

    @myDsl_ExprSimple62.setter
    def myDsl_ExprSimple62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ExprSimple__myDsl_ExprSimple62", None)
        self.__myDsl_ExprSimple62 = value
        
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
    def myDsl_ExprSimple64(self):
        return self.__myDsl_ExprSimple64

    @myDsl_ExprSimple64.setter
    def myDsl_ExprSimple64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ExprSimple__myDsl_ExprSimple64", None)
        self.__myDsl_ExprSimple64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expr65"):
                opp_val = getattr(old_value, "myDsl_Expr65", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expr65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expr65"):
                opp_val = getattr(value, "myDsl_Expr65", None)
                setattr(value, "myDsl_Expr65", self)

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
            if hasattr(old_value, "myDsl_Expr36"):
                opp_val = getattr(old_value, "myDsl_Expr36", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expr36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expr36"):
                opp_val = getattr(value, "myDsl_Expr36", None)
                setattr(value, "myDsl_Expr36", self)

class myDsl_Lexpr:

    pass
class myDsl_EObject:

    pass
class myDsl_Eq:

    pass
class myDsl_Output:

    def __init__(self, v: str, v2: str, myDsl_Output: "myDsl_Definiton" = None):
        self.v = v
        self.v2 = v2
        self.myDsl_Output = myDsl_Output
        
    @property
    def v(self) -> str:
        return self.__v

    @v.setter
    def v(self, v: str):
        self.__v = v

    @property
    def v2(self) -> str:
        return self.__v2

    @v2.setter
    def v2(self, v2: str):
        self.__v2 = v2

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
            if hasattr(old_value, "myDsl_Definiton8"):
                opp_val = getattr(old_value, "myDsl_Definiton8", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Definiton8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Definiton8"):
                opp_val = getattr(value, "myDsl_Definiton8", None)
                setattr(value, "myDsl_Definiton8", self)

class myDsl_Commands:

    pass
class myDsl_Input:

    def __init__(self, v: str, v2: str, myDsl_Input: "myDsl_Definiton" = None):
        self.v = v
        self.v2 = v2
        self.myDsl_Input = myDsl_Input
        
    @property
    def v2(self) -> str:
        return self.__v2

    @v2.setter
    def v2(self, v2: str):
        self.__v2 = v2

    @property
    def v(self) -> str:
        return self.__v

    @v.setter
    def v(self, v: str):
        self.__v = v

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
            if hasattr(old_value, "myDsl_Definiton4"):
                opp_val = getattr(old_value, "myDsl_Definiton4", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Definiton4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Definiton4"):
                opp_val = getattr(value, "myDsl_Definiton4", None)
                setattr(value, "myDsl_Definiton4", self)

class myDsl_Expr:

    pass
class myDsl_Exprs:

    pass
class myDsl_Vars:

    def __init__(self, v1: str, v2: str, myDsl_Vars: "myDsl_Command" = None):
        self.v1 = v1
        self.v2 = v2
        self.myDsl_Vars = myDsl_Vars
        
    @property
    def v2(self) -> str:
        return self.__v2

    @v2.setter
    def v2(self, v2: str):
        self.__v2 = v2

    @property
    def v1(self) -> str:
        return self.__v1

    @v1.setter
    def v1(self, v1: str):
        self.__v1 = v1

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
            if hasattr(old_value, "myDsl_Command16"):
                opp_val = getattr(old_value, "myDsl_Command16", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Command16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Command16"):
                opp_val = getattr(value, "myDsl_Command16", None)
                setattr(value, "myDsl_Command16", self)

class myDsl_Command:

    def __init__(self, nom: str, myDsl_Command: "myDsl_Commands" = None, myDsl_Command16: "myDsl_Vars" = None, myDsl_Command18: "myDsl_Exprs" = None, myDsl_Command21: "myDsl_Expr" = None, myDsl_Command24: "myDsl_Commands" = None, myDsl_Command27: "myDsl_Expr" = None, myDsl_Command30: "myDsl_Expr" = None, myDsl_Command33: "myDsl_Commands" = None):
        self.nom = nom
        self.myDsl_Command = myDsl_Command
        self.myDsl_Command16 = myDsl_Command16
        self.myDsl_Command18 = myDsl_Command18
        self.myDsl_Command21 = myDsl_Command21
        self.myDsl_Command24 = myDsl_Command24
        self.myDsl_Command27 = myDsl_Command27
        self.myDsl_Command30 = myDsl_Command30
        self.myDsl_Command33 = myDsl_Command33
        
    @property
    def nom(self) -> str:
        return self.__nom

    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def myDsl_Command(self):
        return self.__myDsl_Command

    @myDsl_Command.setter
    def myDsl_Command(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Command__myDsl_Command", None)
        self.__myDsl_Command = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Commands10"):
                opp_val = getattr(old_value, "myDsl_Commands10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Commands10"):
                opp_val = getattr(value, "myDsl_Commands10", None)
                if opp_val is None:
                    setattr(value, "myDsl_Commands10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Command24(self):
        return self.__myDsl_Command24

    @myDsl_Command24.setter
    def myDsl_Command24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Command__myDsl_Command24", None)
        self.__myDsl_Command24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Commands25"):
                opp_val = getattr(old_value, "myDsl_Commands25", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Commands25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Commands25"):
                opp_val = getattr(value, "myDsl_Commands25", None)
                setattr(value, "myDsl_Commands25", self)

    @property
    def myDsl_Command16(self):
        return self.__myDsl_Command16

    @myDsl_Command16.setter
    def myDsl_Command16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Command__myDsl_Command16", None)
        self.__myDsl_Command16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Vars"):
                opp_val = getattr(old_value, "myDsl_Vars", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Vars", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Vars"):
                opp_val = getattr(value, "myDsl_Vars", None)
                setattr(value, "myDsl_Vars", self)

    @property
    def myDsl_Command33(self):
        return self.__myDsl_Command33

    @myDsl_Command33.setter
    def myDsl_Command33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Command__myDsl_Command33", None)
        self.__myDsl_Command33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Commands34"):
                opp_val = getattr(old_value, "myDsl_Commands34", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Commands34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Commands34"):
                opp_val = getattr(value, "myDsl_Commands34", None)
                setattr(value, "myDsl_Commands34", self)

    @property
    def myDsl_Command18(self):
        return self.__myDsl_Command18

    @myDsl_Command18.setter
    def myDsl_Command18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Command__myDsl_Command18", None)
        self.__myDsl_Command18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Exprs19"):
                opp_val = getattr(old_value, "myDsl_Exprs19", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Exprs19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Exprs19"):
                opp_val = getattr(value, "myDsl_Exprs19", None)
                setattr(value, "myDsl_Exprs19", self)

    @property
    def myDsl_Command30(self):
        return self.__myDsl_Command30

    @myDsl_Command30.setter
    def myDsl_Command30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Command__myDsl_Command30", None)
        self.__myDsl_Command30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expr31"):
                opp_val = getattr(old_value, "myDsl_Expr31", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expr31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expr31"):
                opp_val = getattr(value, "myDsl_Expr31", None)
                setattr(value, "myDsl_Expr31", self)

    @property
    def myDsl_Command21(self):
        return self.__myDsl_Command21

    @myDsl_Command21.setter
    def myDsl_Command21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Command__myDsl_Command21", None)
        self.__myDsl_Command21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expr22"):
                opp_val = getattr(old_value, "myDsl_Expr22", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expr22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expr22"):
                opp_val = getattr(value, "myDsl_Expr22", None)
                setattr(value, "myDsl_Expr22", self)

    @property
    def myDsl_Command27(self):
        return self.__myDsl_Command27

    @myDsl_Command27.setter
    def myDsl_Command27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Command__myDsl_Command27", None)
        self.__myDsl_Command27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expr28"):
                opp_val = getattr(old_value, "myDsl_Expr28", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expr28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expr28"):
                opp_val = getattr(value, "myDsl_Expr28", None)
                setattr(value, "myDsl_Expr28", self)

class myDsl_Definiton:

    pass
class myDsl_Function:

    def __init__(self, funName: str, myDsl_Function: "myDsl_Model" = None, myDsl_Function2: "myDsl_Definiton" = None):
        self.funName = funName
        self.myDsl_Function = myDsl_Function
        self.myDsl_Function2 = myDsl_Function2
        
    @property
    def funName(self) -> str:
        return self.__funName

    @funName.setter
    def funName(self, funName: str):
        self.__funName = funName

    @property
    def myDsl_Function(self):
        return self.__myDsl_Function

    @myDsl_Function.setter
    def myDsl_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Function__myDsl_Function", None)
        self.__myDsl_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Model"):
                opp_val = getattr(old_value, "myDsl_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Model"):
                opp_val = getattr(value, "myDsl_Model", None)
                if opp_val is None:
                    setattr(value, "myDsl_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Function2(self):
        return self.__myDsl_Function2

    @myDsl_Function2.setter
    def myDsl_Function2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Function__myDsl_Function2", None)
        self.__myDsl_Function2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Definiton"):
                opp_val = getattr(old_value, "myDsl_Definiton", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Definiton", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Definiton"):
                opp_val = getattr(value, "myDsl_Definiton", None)
                setattr(value, "myDsl_Definiton", self)

class myDsl_Model:

    pass