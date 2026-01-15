from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class whileComp_Lexpr:

    pass
class whileComp_Nil2:

    def __init__(self, nil: str):
        self.nil = nil
        
    @property
    def nil(self) -> str:
        return self.__nil

    @nil.setter
    def nil(self, nil: str):
        self.__nil = nil

class whileComp_Tl:

    def __init__(self, tl: str):
        self.tl = tl
        
    @property
    def tl(self) -> str:
        return self.__tl

    @tl.setter
    def tl(self, tl: str):
        self.__tl = tl

class whileComp_Hd:

    def __init__(self, hd: str):
        self.hd = hd
        
    @property
    def hd(self) -> str:
        return self.__hd

    @hd.setter
    def hd(self, hd: str):
        self.__hd = hd

class whileComp_List:

    def __init__(self, list: str):
        self.list = list
        
    @property
    def list(self) -> str:
        return self.__list

    @list.setter
    def list(self, list: str):
        self.__list = list

class whileComp_Cons:

    def __init__(self, cons: str):
        self.cons = cons
        
    @property
    def cons(self) -> str:
        return self.__cons

    @cons.setter
    def cons(self, cons: str):
        self.__cons = cons

class whileComp_Not:

    def __init__(self, not: str, whileComp_Not: "whileComp_ExprSimple" = None):
        self.not = not
        self.whileComp_Not = whileComp_Not
        
    @property
    def not(self) -> str:
        return self.__not

    @not.setter
    def not(self, not: str):
        self.__not = not

    @property
    def whileComp_Not(self):
        return self.__whileComp_Not

    @whileComp_Not.setter
    def whileComp_Not(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileComp_Not__whileComp_Not", None)
        self.__whileComp_Not = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileComp_ExprSimple51"):
                opp_val = getattr(old_value, "whileComp_ExprSimple51", None)
                if opp_val == self:
                    setattr(old_value, "whileComp_ExprSimple51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileComp_ExprSimple51"):
                opp_val = getattr(value, "whileComp_ExprSimple51", None)
                setattr(value, "whileComp_ExprSimple51", self)

class whileComp_Affectation:

    def __init__(self, affectations: str, whileComp_Affectation: set["whileComp_Expr"] = None):
        self.affectations = affectations
        self.whileComp_Affectation = whileComp_Affectation if whileComp_Affectation is not None else set()
        
    @property
    def affectations(self) -> str:
        return self.__affectations

    @affectations.setter
    def affectations(self, affectations: str):
        self.__affectations = affectations

    @property
    def whileComp_Affectation(self):
        return self.__whileComp_Affectation

    @whileComp_Affectation.setter
    def whileComp_Affectation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileComp_Affectation__whileComp_Affectation", None)
        self.__whileComp_Affectation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "whileComp_Expr"):
                    opp_val = getattr(item, "whileComp_Expr", None)
                    
                    if opp_val == self:
                        setattr(item, "whileComp_Expr", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "whileComp_Expr"):
                    opp_val = getattr(item, "whileComp_Expr", None)
                    
                    setattr(item, "whileComp_Expr", self)
                    

class whileComp_ExprSimple:

    def __init__(self, valeur: str, call: str, ope: str, whileComp_ExprSimple: "whileComp_Expr" = None, whileComp_ExprSimple46: "whileComp_Lexpr" = None, whileComp_ExprSimple48: "whileComp_Expr" = None, whileComp_ExprSimple51: "whileComp_Not" = None, whileComp_ExprSimple53: "whileComp_Expr" = None, whileComp_ExprSimple56: "whileComp_Expr" = None):
        self.valeur = valeur
        self.call = call
        self.ope = ope
        self.whileComp_ExprSimple = whileComp_ExprSimple
        self.whileComp_ExprSimple46 = whileComp_ExprSimple46
        self.whileComp_ExprSimple48 = whileComp_ExprSimple48
        self.whileComp_ExprSimple51 = whileComp_ExprSimple51
        self.whileComp_ExprSimple53 = whileComp_ExprSimple53
        self.whileComp_ExprSimple56 = whileComp_ExprSimple56
        
    @property
    def valeur(self) -> str:
        return self.__valeur

    @valeur.setter
    def valeur(self, valeur: str):
        self.__valeur = valeur

    @property
    def ope(self) -> str:
        return self.__ope

    @ope.setter
    def ope(self, ope: str):
        self.__ope = ope

    @property
    def call(self) -> str:
        return self.__call

    @call.setter
    def call(self, call: str):
        self.__call = call

    @property
    def whileComp_ExprSimple53(self):
        return self.__whileComp_ExprSimple53

    @whileComp_ExprSimple53.setter
    def whileComp_ExprSimple53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileComp_ExprSimple__whileComp_ExprSimple53", None)
        self.__whileComp_ExprSimple53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileComp_Expr54"):
                opp_val = getattr(old_value, "whileComp_Expr54", None)
                if opp_val == self:
                    setattr(old_value, "whileComp_Expr54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileComp_Expr54"):
                opp_val = getattr(value, "whileComp_Expr54", None)
                setattr(value, "whileComp_Expr54", self)

    @property
    def whileComp_ExprSimple56(self):
        return self.__whileComp_ExprSimple56

    @whileComp_ExprSimple56.setter
    def whileComp_ExprSimple56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileComp_ExprSimple__whileComp_ExprSimple56", None)
        self.__whileComp_ExprSimple56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileComp_Expr57"):
                opp_val = getattr(old_value, "whileComp_Expr57", None)
                if opp_val == self:
                    setattr(old_value, "whileComp_Expr57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileComp_Expr57"):
                opp_val = getattr(value, "whileComp_Expr57", None)
                setattr(value, "whileComp_Expr57", self)

    @property
    def whileComp_ExprSimple46(self):
        return self.__whileComp_ExprSimple46

    @whileComp_ExprSimple46.setter
    def whileComp_ExprSimple46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileComp_ExprSimple__whileComp_ExprSimple46", None)
        self.__whileComp_ExprSimple46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileComp_Lexpr"):
                opp_val = getattr(old_value, "whileComp_Lexpr", None)
                if opp_val == self:
                    setattr(old_value, "whileComp_Lexpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileComp_Lexpr"):
                opp_val = getattr(value, "whileComp_Lexpr", None)
                setattr(value, "whileComp_Lexpr", self)

    @property
    def whileComp_ExprSimple48(self):
        return self.__whileComp_ExprSimple48

    @whileComp_ExprSimple48.setter
    def whileComp_ExprSimple48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileComp_ExprSimple__whileComp_ExprSimple48", None)
        self.__whileComp_ExprSimple48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileComp_Expr49"):
                opp_val = getattr(old_value, "whileComp_Expr49", None)
                if opp_val == self:
                    setattr(old_value, "whileComp_Expr49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileComp_Expr49"):
                opp_val = getattr(value, "whileComp_Expr49", None)
                setattr(value, "whileComp_Expr49", self)

    @property
    def whileComp_ExprSimple51(self):
        return self.__whileComp_ExprSimple51

    @whileComp_ExprSimple51.setter
    def whileComp_ExprSimple51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileComp_ExprSimple__whileComp_ExprSimple51", None)
        self.__whileComp_ExprSimple51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileComp_Not"):
                opp_val = getattr(old_value, "whileComp_Not", None)
                if opp_val == self:
                    setattr(old_value, "whileComp_Not", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileComp_Not"):
                opp_val = getattr(value, "whileComp_Not", None)
                setattr(value, "whileComp_Not", self)

    @property
    def whileComp_ExprSimple(self):
        return self.__whileComp_ExprSimple

    @whileComp_ExprSimple.setter
    def whileComp_ExprSimple(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileComp_ExprSimple__whileComp_ExprSimple", None)
        self.__whileComp_ExprSimple = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileComp_Expr44"):
                opp_val = getattr(old_value, "whileComp_Expr44", None)
                if opp_val == self:
                    setattr(old_value, "whileComp_Expr44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileComp_Expr44"):
                opp_val = getattr(value, "whileComp_Expr44", None)
                setattr(value, "whileComp_Expr44", self)

class whileComp_While:

    pass
class whileComp_For:

    pass
class whileComp_If:

    pass
class whileComp_Foreach:

    pass
class whileComp_EObject:

    pass
class whileComp_Command:

    pass
class whileComp_Nop:

    def __init__(self, nop: str):
        self.nop = nop
        
    @property
    def nop(self) -> str:
        return self.__nop

    @nop.setter
    def nop(self, nop: str):
        self.__nop = nop

class whileComp_Expr:

    pass
class whileComp_Write:

    def __init__(self, variable: str, whileComp_Write: "whileComp_Definition" = None):
        self.variable = variable
        self.whileComp_Write = whileComp_Write
        
    @property
    def variable(self) -> str:
        return self.__variable

    @variable.setter
    def variable(self, variable: str):
        self.__variable = variable

    @property
    def whileComp_Write(self):
        return self.__whileComp_Write

    @whileComp_Write.setter
    def whileComp_Write(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileComp_Write__whileComp_Write", None)
        self.__whileComp_Write = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileComp_Definition8"):
                opp_val = getattr(old_value, "whileComp_Definition8", None)
                if opp_val == self:
                    setattr(old_value, "whileComp_Definition8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileComp_Definition8"):
                opp_val = getattr(value, "whileComp_Definition8", None)
                setattr(value, "whileComp_Definition8", self)

class whileComp_Commands:

    pass
class whileComp_Read:

    def __init__(self, variable: str, whileComp_Read: "whileComp_Definition" = None):
        self.variable = variable
        self.whileComp_Read = whileComp_Read
        
    @property
    def variable(self) -> str:
        return self.__variable

    @variable.setter
    def variable(self, variable: str):
        self.__variable = variable

    @property
    def whileComp_Read(self):
        return self.__whileComp_Read

    @whileComp_Read.setter
    def whileComp_Read(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileComp_Read__whileComp_Read", None)
        self.__whileComp_Read = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileComp_Definition4"):
                opp_val = getattr(old_value, "whileComp_Definition4", None)
                if opp_val == self:
                    setattr(old_value, "whileComp_Definition4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileComp_Definition4"):
                opp_val = getattr(value, "whileComp_Definition4", None)
                setattr(value, "whileComp_Definition4", self)

class whileComp_Definition:

    pass
class whileComp_Function:

    def __init__(self, function: str, whileComp_Function: "whileComp_Program" = None, whileComp_Function2: "whileComp_Definition" = None):
        self.function = function
        self.whileComp_Function = whileComp_Function
        self.whileComp_Function2 = whileComp_Function2
        
    @property
    def function(self) -> str:
        return self.__function

    @function.setter
    def function(self, function: str):
        self.__function = function

    @property
    def whileComp_Function2(self):
        return self.__whileComp_Function2

    @whileComp_Function2.setter
    def whileComp_Function2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileComp_Function__whileComp_Function2", None)
        self.__whileComp_Function2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileComp_Definition"):
                opp_val = getattr(old_value, "whileComp_Definition", None)
                if opp_val == self:
                    setattr(old_value, "whileComp_Definition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileComp_Definition"):
                opp_val = getattr(value, "whileComp_Definition", None)
                setattr(value, "whileComp_Definition", self)

    @property
    def whileComp_Function(self):
        return self.__whileComp_Function

    @whileComp_Function.setter
    def whileComp_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileComp_Function__whileComp_Function", None)
        self.__whileComp_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileComp_Program"):
                opp_val = getattr(old_value, "whileComp_Program", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileComp_Program"):
                opp_val = getattr(value, "whileComp_Program", None)
                if opp_val is None:
                    setattr(value, "whileComp_Program", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class whileComp_Program:

    pass