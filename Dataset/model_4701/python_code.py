from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class paplj_Symbol:

    def __init__(self, name: str, paplj_Symbol: "paplj_Type" = None, paplj_Symbol105: "paplj_Var" = None):
        self.name = name
        self.paplj_Symbol = paplj_Symbol
        self.paplj_Symbol105 = paplj_Symbol105
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def paplj_Symbol105(self):
        return self.__paplj_Symbol105

    @paplj_Symbol105.setter
    def paplj_Symbol105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_paplj_Symbol__paplj_Symbol105", None)
        self.__paplj_Symbol105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "paplj_Var"):
                opp_val = getattr(old_value, "paplj_Var", None)
                if opp_val == self:
                    setattr(old_value, "paplj_Var", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "paplj_Var"):
                opp_val = getattr(value, "paplj_Var", None)
                setattr(value, "paplj_Var", self)

    @property
    def paplj_Symbol(self):
        return self.__paplj_Symbol

    @paplj_Symbol.setter
    def paplj_Symbol(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_paplj_Symbol__paplj_Symbol", None)
        self.__paplj_Symbol = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "paplj_Type11"):
                opp_val = getattr(old_value, "paplj_Type11", None)
                if opp_val == self:
                    setattr(old_value, "paplj_Type11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "paplj_Type11"):
                opp_val = getattr(value, "paplj_Type11", None)
                setattr(value, "paplj_Type11", self)

class Symbol:

    pass
class paplj_Member(Symbol):

    pass
class Expr:

    pass
class paplj_MemberRef(Expr):

    def __init__(self, methodInvocation: bool, paplj_MemberRef: "paplj_Expr" = None, paplj_MemberRef95: "paplj_Member" = None, paplj_MemberRef98: set["paplj_Expr"] = None):
        self.methodInvocation = methodInvocation
        self.paplj_MemberRef = paplj_MemberRef
        self.paplj_MemberRef95 = paplj_MemberRef95
        self.paplj_MemberRef98 = paplj_MemberRef98 if paplj_MemberRef98 is not None else set()
        
    @property
    def methodInvocation(self) -> bool:
        return self.__methodInvocation

    @methodInvocation.setter
    def methodInvocation(self, methodInvocation: bool):
        self.__methodInvocation = methodInvocation

    @property
    def paplj_MemberRef95(self):
        return self.__paplj_MemberRef95

    @paplj_MemberRef95.setter
    def paplj_MemberRef95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_paplj_MemberRef__paplj_MemberRef95", None)
        self.__paplj_MemberRef95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "paplj_Member96"):
                opp_val = getattr(old_value, "paplj_Member96", None)
                if opp_val == self:
                    setattr(old_value, "paplj_Member96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "paplj_Member96"):
                opp_val = getattr(value, "paplj_Member96", None)
                setattr(value, "paplj_Member96", self)

    @property
    def paplj_MemberRef98(self):
        return self.__paplj_MemberRef98

    @paplj_MemberRef98.setter
    def paplj_MemberRef98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_paplj_MemberRef__paplj_MemberRef98", None)
        self.__paplj_MemberRef98 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "paplj_Expr99"):
                    opp_val = getattr(item, "paplj_Expr99", None)
                    
                    if opp_val == self:
                        setattr(item, "paplj_Expr99", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "paplj_Expr99"):
                    opp_val = getattr(item, "paplj_Expr99", None)
                    
                    setattr(item, "paplj_Expr99", self)
                    

    @property
    def paplj_MemberRef(self):
        return self.__paplj_MemberRef

    @paplj_MemberRef.setter
    def paplj_MemberRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_paplj_MemberRef__paplj_MemberRef", None)
        self.__paplj_MemberRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "paplj_Expr93"):
                opp_val = getattr(old_value, "paplj_Expr93", None)
                if opp_val == self:
                    setattr(old_value, "paplj_Expr93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "paplj_Expr93"):
                opp_val = getattr(value, "paplj_Expr93", None)
                setattr(value, "paplj_Expr93", self)

class paplj_Var(Expr):

    def __init__(self, methodInvocation: bool, paplj_Var: "paplj_Symbol" = None, paplj_Var107: set["paplj_Expr"] = None):
        self.methodInvocation = methodInvocation
        self.paplj_Var = paplj_Var
        self.paplj_Var107 = paplj_Var107 if paplj_Var107 is not None else set()
        
    @property
    def methodInvocation(self) -> bool:
        return self.__methodInvocation

    @methodInvocation.setter
    def methodInvocation(self, methodInvocation: bool):
        self.__methodInvocation = methodInvocation

    @property
    def paplj_Var107(self):
        return self.__paplj_Var107

    @paplj_Var107.setter
    def paplj_Var107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_paplj_Var__paplj_Var107", None)
        self.__paplj_Var107 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "paplj_Expr108"):
                    opp_val = getattr(item, "paplj_Expr108", None)
                    
                    if opp_val == self:
                        setattr(item, "paplj_Expr108", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "paplj_Expr108"):
                    opp_val = getattr(item, "paplj_Expr108", None)
                    
                    setattr(item, "paplj_Expr108", self)
                    

    @property
    def paplj_Var(self):
        return self.__paplj_Var

    @paplj_Var.setter
    def paplj_Var(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_paplj_Var__paplj_Var", None)
        self.__paplj_Var = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "paplj_Symbol105"):
                opp_val = getattr(old_value, "paplj_Symbol105", None)
                if opp_val == self:
                    setattr(old_value, "paplj_Symbol105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "paplj_Symbol105"):
                opp_val = getattr(value, "paplj_Symbol105", None)
                setattr(value, "paplj_Symbol105", self)

class paplj_Assignment(Expr):

    pass
class paplj_Lt(Expr):

    pass
class paplj_Null(Expr):

    pass
class paplj_Neq(Expr):

    pass
class paplj_New(Expr):

    pass
class paplj_Bool(Expr):

    def __init__(self, true: bool):
        self.true = true
        
    @property
    def true(self) -> bool:
        return self.__true

    @true.setter
    def true(self, true: bool):
        self.__true = true

class paplj_Not(Expr):

    pass
class paplj_Let(Expr):

    pass
class paplj_And(Expr):

    pass
class paplj_Num(Expr):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class paplj_Eq(Expr):

    pass
class paplj_If(Expr):

    pass
class paplj_This(Expr):

    pass
class paplj_Cast(Expr):

    pass
class paplj_Or(Expr):

    pass
class paplj_Mul(Expr):

    pass
class paplj_Div(Expr):

    pass
class paplj_Sub(Expr):

    pass
class paplj_Add(Expr):

    pass
class paplj_Min(Expr):

    pass
class paplj_Binding(Symbol):

    pass
class paplj_Block2(Expr):

    pass
class paplj_Param(Symbol):

    pass
class Member:

    pass
class paplj_Method(Member):

    pass
class paplj_Field(Member):

    pass
class paplj_Expr:

    pass
class paplj_Type:

    def __init__(self, name: str, paplj_Type: "paplj_Program" = None, paplj_Type7: "paplj_Type" = None, paplj_Type5: "paplj_Type" = None, paplj_Type9: set["paplj_Member"] = None, paplj_Type11: "paplj_Symbol" = None, paplj_Type87: "paplj_Cast" = None, paplj_Type101: "paplj_Null" = None, paplj_Type103: "paplj_New" = None):
        self.name = name
        self.paplj_Type = paplj_Type
        self.paplj_Type7 = paplj_Type7
        self.paplj_Type5 = paplj_Type5
        self.paplj_Type9 = paplj_Type9 if paplj_Type9 is not None else set()
        self.paplj_Type11 = paplj_Type11
        self.paplj_Type87 = paplj_Type87
        self.paplj_Type101 = paplj_Type101
        self.paplj_Type103 = paplj_Type103
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def paplj_Type101(self):
        return self.__paplj_Type101

    @paplj_Type101.setter
    def paplj_Type101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_paplj_Type__paplj_Type101", None)
        self.__paplj_Type101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "paplj_Null"):
                opp_val = getattr(old_value, "paplj_Null", None)
                if opp_val == self:
                    setattr(old_value, "paplj_Null", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "paplj_Null"):
                opp_val = getattr(value, "paplj_Null", None)
                setattr(value, "paplj_Null", self)

    @property
    def paplj_Type11(self):
        return self.__paplj_Type11

    @paplj_Type11.setter
    def paplj_Type11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_paplj_Type__paplj_Type11", None)
        self.__paplj_Type11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "paplj_Symbol"):
                opp_val = getattr(old_value, "paplj_Symbol", None)
                if opp_val == self:
                    setattr(old_value, "paplj_Symbol", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "paplj_Symbol"):
                opp_val = getattr(value, "paplj_Symbol", None)
                setattr(value, "paplj_Symbol", self)

    @property
    def paplj_Type9(self):
        return self.__paplj_Type9

    @paplj_Type9.setter
    def paplj_Type9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_paplj_Type__paplj_Type9", None)
        self.__paplj_Type9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "paplj_Member"):
                    opp_val = getattr(item, "paplj_Member", None)
                    
                    if opp_val == self:
                        setattr(item, "paplj_Member", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "paplj_Member"):
                    opp_val = getattr(item, "paplj_Member", None)
                    
                    setattr(item, "paplj_Member", self)
                    

    @property
    def paplj_Type7(self):
        return self.__paplj_Type7

    @paplj_Type7.setter
    def paplj_Type7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_paplj_Type__paplj_Type7", None)
        self.__paplj_Type7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "paplj_Type5"):
                opp_val = getattr(old_value, "paplj_Type5", None)
                if opp_val == self:
                    setattr(old_value, "paplj_Type5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "paplj_Type5"):
                opp_val = getattr(value, "paplj_Type5", None)
                setattr(value, "paplj_Type5", self)

    @property
    def paplj_Type(self):
        return self.__paplj_Type

    @paplj_Type.setter
    def paplj_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_paplj_Type__paplj_Type", None)
        self.__paplj_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "paplj_Program2"):
                opp_val = getattr(old_value, "paplj_Program2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "paplj_Program2"):
                opp_val = getattr(value, "paplj_Program2", None)
                if opp_val is None:
                    setattr(value, "paplj_Program2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def paplj_Type5(self):
        return self.__paplj_Type5

    @paplj_Type5.setter
    def paplj_Type5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_paplj_Type__paplj_Type5", None)
        self.__paplj_Type5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "paplj_Type7"):
                opp_val = getattr(old_value, "paplj_Type7", None)
                if opp_val == self:
                    setattr(old_value, "paplj_Type7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "paplj_Type7"):
                opp_val = getattr(value, "paplj_Type7", None)
                setattr(value, "paplj_Type7", self)

    @property
    def paplj_Type87(self):
        return self.__paplj_Type87

    @paplj_Type87.setter
    def paplj_Type87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_paplj_Type__paplj_Type87", None)
        self.__paplj_Type87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "paplj_Cast86"):
                opp_val = getattr(old_value, "paplj_Cast86", None)
                if opp_val == self:
                    setattr(old_value, "paplj_Cast86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "paplj_Cast86"):
                opp_val = getattr(value, "paplj_Cast86", None)
                setattr(value, "paplj_Cast86", self)

    @property
    def paplj_Type103(self):
        return self.__paplj_Type103

    @paplj_Type103.setter
    def paplj_Type103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_paplj_Type__paplj_Type103", None)
        self.__paplj_Type103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "paplj_New"):
                opp_val = getattr(old_value, "paplj_New", None)
                if opp_val == self:
                    setattr(old_value, "paplj_New", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "paplj_New"):
                opp_val = getattr(value, "paplj_New", None)
                setattr(value, "paplj_New", self)

class paplj_Import:

    def __init__(self, importedNamespace: str, paplj_Import: "paplj_Program" = None):
        self.importedNamespace = importedNamespace
        self.paplj_Import = paplj_Import
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

    @property
    def paplj_Import(self):
        return self.__paplj_Import

    @paplj_Import.setter
    def paplj_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_paplj_Import__paplj_Import", None)
        self.__paplj_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "paplj_Program"):
                opp_val = getattr(old_value, "paplj_Program", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "paplj_Program"):
                opp_val = getattr(value, "paplj_Program", None)
                if opp_val is None:
                    setattr(value, "paplj_Program", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class paplj_Program:

    def __init__(self, name: str, paplj_Program: set["paplj_Import"] = None, paplj_Program2: set["paplj_Type"] = None, paplj_Program4: "paplj_Expr" = None):
        self.name = name
        self.paplj_Program = paplj_Program if paplj_Program is not None else set()
        self.paplj_Program2 = paplj_Program2 if paplj_Program2 is not None else set()
        self.paplj_Program4 = paplj_Program4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def paplj_Program4(self):
        return self.__paplj_Program4

    @paplj_Program4.setter
    def paplj_Program4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_paplj_Program__paplj_Program4", None)
        self.__paplj_Program4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "paplj_Expr"):
                opp_val = getattr(old_value, "paplj_Expr", None)
                if opp_val == self:
                    setattr(old_value, "paplj_Expr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "paplj_Expr"):
                opp_val = getattr(value, "paplj_Expr", None)
                setattr(value, "paplj_Expr", self)

    @property
    def paplj_Program(self):
        return self.__paplj_Program

    @paplj_Program.setter
    def paplj_Program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_paplj_Program__paplj_Program", None)
        self.__paplj_Program = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "paplj_Import"):
                    opp_val = getattr(item, "paplj_Import", None)
                    
                    if opp_val == self:
                        setattr(item, "paplj_Import", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "paplj_Import"):
                    opp_val = getattr(item, "paplj_Import", None)
                    
                    setattr(item, "paplj_Import", self)
                    

    @property
    def paplj_Program2(self):
        return self.__paplj_Program2

    @paplj_Program2.setter
    def paplj_Program2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_paplj_Program__paplj_Program2", None)
        self.__paplj_Program2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "paplj_Type"):
                    opp_val = getattr(item, "paplj_Type", None)
                    
                    if opp_val == self:
                        setattr(item, "paplj_Type", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "paplj_Type"):
                    opp_val = getattr(item, "paplj_Type", None)
                    
                    setattr(item, "paplj_Type", self)
                    
