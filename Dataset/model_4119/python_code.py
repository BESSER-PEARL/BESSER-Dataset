from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class whileLanguage_Lexpr:

    pass
class whileLanguage_While:

    pass
class whileLanguage_For:

    pass
class whileLanguage_If:

    pass
class whileLanguage_Foreach:

    pass
class whileLanguage_Write:

    def __init__(self, variable: str, whileLanguage_Write: "whileLanguage_Definition" = None):
        self.variable = variable
        self.whileLanguage_Write = whileLanguage_Write
        
    @property
    def variable(self) -> str:
        return self.__variable

    @variable.setter
    def variable(self, variable: str):
        self.__variable = variable

    @property
    def whileLanguage_Write(self):
        return self.__whileLanguage_Write

    @whileLanguage_Write.setter
    def whileLanguage_Write(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileLanguage_Write__whileLanguage_Write", None)
        self.__whileLanguage_Write = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileLanguage_Definition8"):
                opp_val = getattr(old_value, "whileLanguage_Definition8", None)
                if opp_val == self:
                    setattr(old_value, "whileLanguage_Definition8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileLanguage_Definition8"):
                opp_val = getattr(value, "whileLanguage_Definition8", None)
                setattr(value, "whileLanguage_Definition8", self)

class whileLanguage_Commands:

    pass
class whileLanguage_Read:

    def __init__(self, variable: str, whileLanguage_Read: "whileLanguage_Definition" = None):
        self.variable = variable
        self.whileLanguage_Read = whileLanguage_Read
        
    @property
    def variable(self) -> str:
        return self.__variable

    @variable.setter
    def variable(self, variable: str):
        self.__variable = variable

    @property
    def whileLanguage_Read(self):
        return self.__whileLanguage_Read

    @whileLanguage_Read.setter
    def whileLanguage_Read(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileLanguage_Read__whileLanguage_Read", None)
        self.__whileLanguage_Read = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileLanguage_Definition4"):
                opp_val = getattr(old_value, "whileLanguage_Definition4", None)
                if opp_val == self:
                    setattr(old_value, "whileLanguage_Definition4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileLanguage_Definition4"):
                opp_val = getattr(value, "whileLanguage_Definition4", None)
                setattr(value, "whileLanguage_Definition4", self)

class whileLanguage_Definition:

    pass
class whileLanguage_Function:

    def __init__(self, name: str, whileLanguage_Function: "whileLanguage_Program" = None, whileLanguage_Function2: "whileLanguage_Definition" = None):
        self.name = name
        self.whileLanguage_Function = whileLanguage_Function
        self.whileLanguage_Function2 = whileLanguage_Function2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def whileLanguage_Function(self):
        return self.__whileLanguage_Function

    @whileLanguage_Function.setter
    def whileLanguage_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileLanguage_Function__whileLanguage_Function", None)
        self.__whileLanguage_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileLanguage_Program"):
                opp_val = getattr(old_value, "whileLanguage_Program", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileLanguage_Program"):
                opp_val = getattr(value, "whileLanguage_Program", None)
                if opp_val is None:
                    setattr(value, "whileLanguage_Program", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def whileLanguage_Function2(self):
        return self.__whileLanguage_Function2

    @whileLanguage_Function2.setter
    def whileLanguage_Function2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileLanguage_Function__whileLanguage_Function2", None)
        self.__whileLanguage_Function2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileLanguage_Definition"):
                opp_val = getattr(old_value, "whileLanguage_Definition", None)
                if opp_val == self:
                    setattr(old_value, "whileLanguage_Definition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileLanguage_Definition"):
                opp_val = getattr(value, "whileLanguage_Definition", None)
                setattr(value, "whileLanguage_Definition", self)

class whileLanguage_Program:

    pass
class whileLanguage_EObject:

    pass
class whileLanguage_Command:

    pass
class whileLanguage_Nop:

    def __init__(self, nop: str):
        self.nop = nop
        
    @property
    def nop(self) -> str:
        return self.__nop

    @nop.setter
    def nop(self, nop: str):
        self.__nop = nop

class whileLanguage_Expr:

    def __init__(self, valeur: str, ope: str, whileLanguage_Expr: "whileLanguage_Affectation" = None, whileLanguage_Expr47: "whileLanguage_Expr" = None, whileLanguage_Expr45: "whileLanguage_Expr" = None, whileLanguage_Expr50: "whileLanguage_Expr" = None, whileLanguage_Expr48: "whileLanguage_Expr" = None, whileLanguage_Expr53: "whileLanguage_Lexpr" = None, whileLanguage_Expr15: "whileLanguage_Foreach" = None, whileLanguage_Expr18: "whileLanguage_Foreach" = None, whileLanguage_Expr23: "whileLanguage_If" = None, whileLanguage_Expr31: "whileLanguage_For" = None, whileLanguage_Expr36: "whileLanguage_While" = None, whileLanguage_Expr41: "whileLanguage_Lexpr" = None, whileLanguage_Expr44: "whileLanguage_Expr" = None, whileLanguage_Expr42: "whileLanguage_Expr" = None):
        self.valeur = valeur
        self.ope = ope
        self.whileLanguage_Expr = whileLanguage_Expr
        self.whileLanguage_Expr47 = whileLanguage_Expr47
        self.whileLanguage_Expr45 = whileLanguage_Expr45
        self.whileLanguage_Expr50 = whileLanguage_Expr50
        self.whileLanguage_Expr48 = whileLanguage_Expr48
        self.whileLanguage_Expr53 = whileLanguage_Expr53
        self.whileLanguage_Expr15 = whileLanguage_Expr15
        self.whileLanguage_Expr18 = whileLanguage_Expr18
        self.whileLanguage_Expr23 = whileLanguage_Expr23
        self.whileLanguage_Expr31 = whileLanguage_Expr31
        self.whileLanguage_Expr36 = whileLanguage_Expr36
        self.whileLanguage_Expr41 = whileLanguage_Expr41
        self.whileLanguage_Expr44 = whileLanguage_Expr44
        self.whileLanguage_Expr42 = whileLanguage_Expr42
        
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
    def whileLanguage_Expr18(self):
        return self.__whileLanguage_Expr18

    @whileLanguage_Expr18.setter
    def whileLanguage_Expr18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileLanguage_Expr__whileLanguage_Expr18", None)
        self.__whileLanguage_Expr18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileLanguage_Foreach17"):
                opp_val = getattr(old_value, "whileLanguage_Foreach17", None)
                if opp_val == self:
                    setattr(old_value, "whileLanguage_Foreach17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileLanguage_Foreach17"):
                opp_val = getattr(value, "whileLanguage_Foreach17", None)
                setattr(value, "whileLanguage_Foreach17", self)

    @property
    def whileLanguage_Expr41(self):
        return self.__whileLanguage_Expr41

    @whileLanguage_Expr41.setter
    def whileLanguage_Expr41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileLanguage_Expr__whileLanguage_Expr41", None)
        self.__whileLanguage_Expr41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileLanguage_Lexpr"):
                opp_val = getattr(old_value, "whileLanguage_Lexpr", None)
                if opp_val == self:
                    setattr(old_value, "whileLanguage_Lexpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileLanguage_Lexpr"):
                opp_val = getattr(value, "whileLanguage_Lexpr", None)
                setattr(value, "whileLanguage_Lexpr", self)

    @property
    def whileLanguage_Expr15(self):
        return self.__whileLanguage_Expr15

    @whileLanguage_Expr15.setter
    def whileLanguage_Expr15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileLanguage_Expr__whileLanguage_Expr15", None)
        self.__whileLanguage_Expr15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileLanguage_Foreach"):
                opp_val = getattr(old_value, "whileLanguage_Foreach", None)
                if opp_val == self:
                    setattr(old_value, "whileLanguage_Foreach", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileLanguage_Foreach"):
                opp_val = getattr(value, "whileLanguage_Foreach", None)
                setattr(value, "whileLanguage_Foreach", self)

    @property
    def whileLanguage_Expr31(self):
        return self.__whileLanguage_Expr31

    @whileLanguage_Expr31.setter
    def whileLanguage_Expr31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileLanguage_Expr__whileLanguage_Expr31", None)
        self.__whileLanguage_Expr31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileLanguage_For"):
                opp_val = getattr(old_value, "whileLanguage_For", None)
                if opp_val == self:
                    setattr(old_value, "whileLanguage_For", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileLanguage_For"):
                opp_val = getattr(value, "whileLanguage_For", None)
                setattr(value, "whileLanguage_For", self)

    @property
    def whileLanguage_Expr45(self):
        return self.__whileLanguage_Expr45

    @whileLanguage_Expr45.setter
    def whileLanguage_Expr45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileLanguage_Expr__whileLanguage_Expr45", None)
        self.__whileLanguage_Expr45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileLanguage_Expr47"):
                opp_val = getattr(old_value, "whileLanguage_Expr47", None)
                if opp_val == self:
                    setattr(old_value, "whileLanguage_Expr47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileLanguage_Expr47"):
                opp_val = getattr(value, "whileLanguage_Expr47", None)
                setattr(value, "whileLanguage_Expr47", self)

    @property
    def whileLanguage_Expr53(self):
        return self.__whileLanguage_Expr53

    @whileLanguage_Expr53.setter
    def whileLanguage_Expr53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileLanguage_Expr__whileLanguage_Expr53", None)
        self.__whileLanguage_Expr53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileLanguage_Lexpr52"):
                opp_val = getattr(old_value, "whileLanguage_Lexpr52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileLanguage_Lexpr52"):
                opp_val = getattr(value, "whileLanguage_Lexpr52", None)
                if opp_val is None:
                    setattr(value, "whileLanguage_Lexpr52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def whileLanguage_Expr50(self):
        return self.__whileLanguage_Expr50

    @whileLanguage_Expr50.setter
    def whileLanguage_Expr50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileLanguage_Expr__whileLanguage_Expr50", None)
        self.__whileLanguage_Expr50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileLanguage_Expr48"):
                opp_val = getattr(old_value, "whileLanguage_Expr48", None)
                if opp_val == self:
                    setattr(old_value, "whileLanguage_Expr48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileLanguage_Expr48"):
                opp_val = getattr(value, "whileLanguage_Expr48", None)
                setattr(value, "whileLanguage_Expr48", self)

    @property
    def whileLanguage_Expr23(self):
        return self.__whileLanguage_Expr23

    @whileLanguage_Expr23.setter
    def whileLanguage_Expr23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileLanguage_Expr__whileLanguage_Expr23", None)
        self.__whileLanguage_Expr23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileLanguage_If"):
                opp_val = getattr(old_value, "whileLanguage_If", None)
                if opp_val == self:
                    setattr(old_value, "whileLanguage_If", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileLanguage_If"):
                opp_val = getattr(value, "whileLanguage_If", None)
                setattr(value, "whileLanguage_If", self)

    @property
    def whileLanguage_Expr36(self):
        return self.__whileLanguage_Expr36

    @whileLanguage_Expr36.setter
    def whileLanguage_Expr36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileLanguage_Expr__whileLanguage_Expr36", None)
        self.__whileLanguage_Expr36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileLanguage_While"):
                opp_val = getattr(old_value, "whileLanguage_While", None)
                if opp_val == self:
                    setattr(old_value, "whileLanguage_While", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileLanguage_While"):
                opp_val = getattr(value, "whileLanguage_While", None)
                setattr(value, "whileLanguage_While", self)

    @property
    def whileLanguage_Expr42(self):
        return self.__whileLanguage_Expr42

    @whileLanguage_Expr42.setter
    def whileLanguage_Expr42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileLanguage_Expr__whileLanguage_Expr42", None)
        self.__whileLanguage_Expr42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileLanguage_Expr44"):
                opp_val = getattr(old_value, "whileLanguage_Expr44", None)
                if opp_val == self:
                    setattr(old_value, "whileLanguage_Expr44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileLanguage_Expr44"):
                opp_val = getattr(value, "whileLanguage_Expr44", None)
                setattr(value, "whileLanguage_Expr44", self)

    @property
    def whileLanguage_Expr44(self):
        return self.__whileLanguage_Expr44

    @whileLanguage_Expr44.setter
    def whileLanguage_Expr44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileLanguage_Expr__whileLanguage_Expr44", None)
        self.__whileLanguage_Expr44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileLanguage_Expr42"):
                opp_val = getattr(old_value, "whileLanguage_Expr42", None)
                if opp_val == self:
                    setattr(old_value, "whileLanguage_Expr42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileLanguage_Expr42"):
                opp_val = getattr(value, "whileLanguage_Expr42", None)
                setattr(value, "whileLanguage_Expr42", self)

    @property
    def whileLanguage_Expr48(self):
        return self.__whileLanguage_Expr48

    @whileLanguage_Expr48.setter
    def whileLanguage_Expr48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileLanguage_Expr__whileLanguage_Expr48", None)
        self.__whileLanguage_Expr48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileLanguage_Expr50"):
                opp_val = getattr(old_value, "whileLanguage_Expr50", None)
                if opp_val == self:
                    setattr(old_value, "whileLanguage_Expr50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileLanguage_Expr50"):
                opp_val = getattr(value, "whileLanguage_Expr50", None)
                setattr(value, "whileLanguage_Expr50", self)

    @property
    def whileLanguage_Expr(self):
        return self.__whileLanguage_Expr

    @whileLanguage_Expr.setter
    def whileLanguage_Expr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileLanguage_Expr__whileLanguage_Expr", None)
        self.__whileLanguage_Expr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileLanguage_Affectation"):
                opp_val = getattr(old_value, "whileLanguage_Affectation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileLanguage_Affectation"):
                opp_val = getattr(value, "whileLanguage_Affectation", None)
                if opp_val is None:
                    setattr(value, "whileLanguage_Affectation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def whileLanguage_Expr47(self):
        return self.__whileLanguage_Expr47

    @whileLanguage_Expr47.setter
    def whileLanguage_Expr47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileLanguage_Expr__whileLanguage_Expr47", None)
        self.__whileLanguage_Expr47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileLanguage_Expr45"):
                opp_val = getattr(old_value, "whileLanguage_Expr45", None)
                if opp_val == self:
                    setattr(old_value, "whileLanguage_Expr45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileLanguage_Expr45"):
                opp_val = getattr(value, "whileLanguage_Expr45", None)
                setattr(value, "whileLanguage_Expr45", self)

class whileLanguage_Affectation:

    def __init__(self, affectations: str, whileLanguage_Affectation: set["whileLanguage_Expr"] = None):
        self.affectations = affectations
        self.whileLanguage_Affectation = whileLanguage_Affectation if whileLanguage_Affectation is not None else set()
        
    @property
    def affectations(self) -> str:
        return self.__affectations

    @affectations.setter
    def affectations(self, affectations: str):
        self.__affectations = affectations

    @property
    def whileLanguage_Affectation(self):
        return self.__whileLanguage_Affectation

    @whileLanguage_Affectation.setter
    def whileLanguage_Affectation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileLanguage_Affectation__whileLanguage_Affectation", None)
        self.__whileLanguage_Affectation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "whileLanguage_Expr"):
                    opp_val = getattr(item, "whileLanguage_Expr", None)
                    
                    if opp_val == self:
                        setattr(item, "whileLanguage_Expr", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "whileLanguage_Expr"):
                    opp_val = getattr(item, "whileLanguage_Expr", None)
                    
                    setattr(item, "whileLanguage_Expr", self)
                    
