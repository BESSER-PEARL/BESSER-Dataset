from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class simpliC_Factor:

    pass
class simpliC_TFact:

    def __init__(self, op: str, simpliC_TFact: "simpliC_Expr" = None, simpliC_TFact50: "simpliC_Expr" = None):
        self.op = op
        self.simpliC_TFact = simpliC_TFact
        self.simpliC_TFact50 = simpliC_TFact50
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def simpliC_TFact50(self):
        return self.__simpliC_TFact50

    @simpliC_TFact50.setter
    def simpliC_TFact50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpliC_TFact__simpliC_TFact50", None)
        self.__simpliC_TFact50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpliC_Expr51"):
                opp_val = getattr(old_value, "simpliC_Expr51", None)
                if opp_val == self:
                    setattr(old_value, "simpliC_Expr51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpliC_Expr51"):
                opp_val = getattr(value, "simpliC_Expr51", None)
                setattr(value, "simpliC_Expr51", self)

    @property
    def simpliC_TFact(self):
        return self.__simpliC_TFact

    @simpliC_TFact.setter
    def simpliC_TFact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpliC_TFact__simpliC_TFact", None)
        self.__simpliC_TFact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpliC_Expr48"):
                opp_val = getattr(old_value, "simpliC_Expr48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpliC_Expr48"):
                opp_val = getattr(value, "simpliC_Expr48", None)
                if opp_val is None:
                    setattr(value, "simpliC_Expr48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class simpliC_EObject:

    pass
class Factor:

    pass
class simpliC_IDuse(Factor):

    pass
class simpliC_ExprCall(Factor):

    pass
class simpliC_Expr:

    def __init__(self, op: str, simpliC_Expr: "simpliC_Call" = None, simpliC_Expr17: "simpliC_ExprCall" = None, simpliC_Expr19: "simpliC_Ifstmt" = None, simpliC_Expr27: "simpliC_Whilestmt" = None, simpliC_Expr32: "simpliC_Return" = None, simpliC_Expr39: "simpliC_Decl" = None, simpliC_Expr41: "simpliC_Assign" = None, simpliC_Expr43: "simpliC_EObject" = None, simpliC_Expr45: "simpliC_EObject" = None, simpliC_Expr48: set["simpliC_TFact"] = None, simpliC_Expr51: "simpliC_TFact" = None):
        self.op = op
        self.simpliC_Expr = simpliC_Expr
        self.simpliC_Expr17 = simpliC_Expr17
        self.simpliC_Expr19 = simpliC_Expr19
        self.simpliC_Expr27 = simpliC_Expr27
        self.simpliC_Expr32 = simpliC_Expr32
        self.simpliC_Expr39 = simpliC_Expr39
        self.simpliC_Expr41 = simpliC_Expr41
        self.simpliC_Expr43 = simpliC_Expr43
        self.simpliC_Expr45 = simpliC_Expr45
        self.simpliC_Expr48 = simpliC_Expr48 if simpliC_Expr48 is not None else set()
        self.simpliC_Expr51 = simpliC_Expr51
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def simpliC_Expr51(self):
        return self.__simpliC_Expr51

    @simpliC_Expr51.setter
    def simpliC_Expr51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpliC_Expr__simpliC_Expr51", None)
        self.__simpliC_Expr51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpliC_TFact50"):
                opp_val = getattr(old_value, "simpliC_TFact50", None)
                if opp_val == self:
                    setattr(old_value, "simpliC_TFact50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpliC_TFact50"):
                opp_val = getattr(value, "simpliC_TFact50", None)
                setattr(value, "simpliC_TFact50", self)

    @property
    def simpliC_Expr45(self):
        return self.__simpliC_Expr45

    @simpliC_Expr45.setter
    def simpliC_Expr45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpliC_Expr__simpliC_Expr45", None)
        self.__simpliC_Expr45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpliC_EObject46"):
                opp_val = getattr(old_value, "simpliC_EObject46", None)
                if opp_val == self:
                    setattr(old_value, "simpliC_EObject46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpliC_EObject46"):
                opp_val = getattr(value, "simpliC_EObject46", None)
                setattr(value, "simpliC_EObject46", self)

    @property
    def simpliC_Expr48(self):
        return self.__simpliC_Expr48

    @simpliC_Expr48.setter
    def simpliC_Expr48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpliC_Expr__simpliC_Expr48", None)
        self.__simpliC_Expr48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpliC_TFact"):
                    opp_val = getattr(item, "simpliC_TFact", None)
                    
                    if opp_val == self:
                        setattr(item, "simpliC_TFact", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpliC_TFact"):
                    opp_val = getattr(item, "simpliC_TFact", None)
                    
                    setattr(item, "simpliC_TFact", self)
                    

    @property
    def simpliC_Expr(self):
        return self.__simpliC_Expr

    @simpliC_Expr.setter
    def simpliC_Expr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpliC_Expr__simpliC_Expr", None)
        self.__simpliC_Expr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpliC_Call12"):
                opp_val = getattr(old_value, "simpliC_Call12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpliC_Call12"):
                opp_val = getattr(value, "simpliC_Call12", None)
                if opp_val is None:
                    setattr(value, "simpliC_Call12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simpliC_Expr17(self):
        return self.__simpliC_Expr17

    @simpliC_Expr17.setter
    def simpliC_Expr17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpliC_Expr__simpliC_Expr17", None)
        self.__simpliC_Expr17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpliC_ExprCall16"):
                opp_val = getattr(old_value, "simpliC_ExprCall16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpliC_ExprCall16"):
                opp_val = getattr(value, "simpliC_ExprCall16", None)
                if opp_val is None:
                    setattr(value, "simpliC_ExprCall16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simpliC_Expr41(self):
        return self.__simpliC_Expr41

    @simpliC_Expr41.setter
    def simpliC_Expr41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpliC_Expr__simpliC_Expr41", None)
        self.__simpliC_Expr41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpliC_Assign"):
                opp_val = getattr(old_value, "simpliC_Assign", None)
                if opp_val == self:
                    setattr(old_value, "simpliC_Assign", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpliC_Assign"):
                opp_val = getattr(value, "simpliC_Assign", None)
                setattr(value, "simpliC_Assign", self)

    @property
    def simpliC_Expr27(self):
        return self.__simpliC_Expr27

    @simpliC_Expr27.setter
    def simpliC_Expr27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpliC_Expr__simpliC_Expr27", None)
        self.__simpliC_Expr27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpliC_Whilestmt"):
                opp_val = getattr(old_value, "simpliC_Whilestmt", None)
                if opp_val == self:
                    setattr(old_value, "simpliC_Whilestmt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpliC_Whilestmt"):
                opp_val = getattr(value, "simpliC_Whilestmt", None)
                setattr(value, "simpliC_Whilestmt", self)

    @property
    def simpliC_Expr32(self):
        return self.__simpliC_Expr32

    @simpliC_Expr32.setter
    def simpliC_Expr32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpliC_Expr__simpliC_Expr32", None)
        self.__simpliC_Expr32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpliC_Return"):
                opp_val = getattr(old_value, "simpliC_Return", None)
                if opp_val == self:
                    setattr(old_value, "simpliC_Return", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpliC_Return"):
                opp_val = getattr(value, "simpliC_Return", None)
                setattr(value, "simpliC_Return", self)

    @property
    def simpliC_Expr19(self):
        return self.__simpliC_Expr19

    @simpliC_Expr19.setter
    def simpliC_Expr19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpliC_Expr__simpliC_Expr19", None)
        self.__simpliC_Expr19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpliC_Ifstmt"):
                opp_val = getattr(old_value, "simpliC_Ifstmt", None)
                if opp_val == self:
                    setattr(old_value, "simpliC_Ifstmt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpliC_Ifstmt"):
                opp_val = getattr(value, "simpliC_Ifstmt", None)
                setattr(value, "simpliC_Ifstmt", self)

    @property
    def simpliC_Expr43(self):
        return self.__simpliC_Expr43

    @simpliC_Expr43.setter
    def simpliC_Expr43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpliC_Expr__simpliC_Expr43", None)
        self.__simpliC_Expr43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpliC_EObject"):
                opp_val = getattr(old_value, "simpliC_EObject", None)
                if opp_val == self:
                    setattr(old_value, "simpliC_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpliC_EObject"):
                opp_val = getattr(value, "simpliC_EObject", None)
                setattr(value, "simpliC_EObject", self)

    @property
    def simpliC_Expr39(self):
        return self.__simpliC_Expr39

    @simpliC_Expr39.setter
    def simpliC_Expr39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpliC_Expr__simpliC_Expr39", None)
        self.__simpliC_Expr39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpliC_Decl38"):
                opp_val = getattr(old_value, "simpliC_Decl38", None)
                if opp_val == self:
                    setattr(old_value, "simpliC_Decl38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpliC_Decl38"):
                opp_val = getattr(value, "simpliC_Decl38", None)
                setattr(value, "simpliC_Decl38", self)

class simpliC_Stmt:

    pass
class Stmt:

    pass
class simpliC_Whilestmt(Stmt):

    pass
class simpliC_Return(Stmt):

    pass
class simpliC_Typedef(Stmt):

    def __init__(self, name: str, simpliC_Typedef: "simpliC_Decl" = None, simpliC_Typedef58: "simpliC_EObject" = None):
        self.name = name
        self.simpliC_Typedef = simpliC_Typedef
        self.simpliC_Typedef58 = simpliC_Typedef58
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simpliC_Typedef(self):
        return self.__simpliC_Typedef

    @simpliC_Typedef.setter
    def simpliC_Typedef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpliC_Typedef__simpliC_Typedef", None)
        self.__simpliC_Typedef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpliC_Decl36"):
                opp_val = getattr(old_value, "simpliC_Decl36", None)
                if opp_val == self:
                    setattr(old_value, "simpliC_Decl36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpliC_Decl36"):
                opp_val = getattr(value, "simpliC_Decl36", None)
                setattr(value, "simpliC_Decl36", self)

    @property
    def simpliC_Typedef58(self):
        return self.__simpliC_Typedef58

    @simpliC_Typedef58.setter
    def simpliC_Typedef58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpliC_Typedef__simpliC_Typedef58", None)
        self.__simpliC_Typedef58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpliC_EObject59"):
                opp_val = getattr(old_value, "simpliC_EObject59", None)
                if opp_val == self:
                    setattr(old_value, "simpliC_EObject59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpliC_EObject59"):
                opp_val = getattr(value, "simpliC_EObject59", None)
                setattr(value, "simpliC_EObject59", self)

class simpliC_Assign(Stmt):

    def __init__(self, var: str, simpliC_Assign: "simpliC_Expr" = None):
        self.var = var
        self.simpliC_Assign = simpliC_Assign
        
    @property
    def var(self) -> str:
        return self.__var

    @var.setter
    def var(self, var: str):
        self.__var = var

    @property
    def simpliC_Assign(self):
        return self.__simpliC_Assign

    @simpliC_Assign.setter
    def simpliC_Assign(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpliC_Assign__simpliC_Assign", None)
        self.__simpliC_Assign = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpliC_Expr41"):
                opp_val = getattr(old_value, "simpliC_Expr41", None)
                if opp_val == self:
                    setattr(old_value, "simpliC_Expr41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpliC_Expr41"):
                opp_val = getattr(value, "simpliC_Expr41", None)
                setattr(value, "simpliC_Expr41", self)

class simpliC_Decl(Stmt):

    def __init__(self, name: str, simpliC_Decl: "simpliC_Type" = None, simpliC_Decl36: "simpliC_Typedef" = None, simpliC_Decl38: "simpliC_Expr" = None, simpliC_Decl53: "simpliC_IDuse" = None):
        self.name = name
        self.simpliC_Decl = simpliC_Decl
        self.simpliC_Decl36 = simpliC_Decl36
        self.simpliC_Decl38 = simpliC_Decl38
        self.simpliC_Decl53 = simpliC_Decl53
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simpliC_Decl38(self):
        return self.__simpliC_Decl38

    @simpliC_Decl38.setter
    def simpliC_Decl38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpliC_Decl__simpliC_Decl38", None)
        self.__simpliC_Decl38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpliC_Expr39"):
                opp_val = getattr(old_value, "simpliC_Expr39", None)
                if opp_val == self:
                    setattr(old_value, "simpliC_Expr39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpliC_Expr39"):
                opp_val = getattr(value, "simpliC_Expr39", None)
                setattr(value, "simpliC_Expr39", self)

    @property
    def simpliC_Decl53(self):
        return self.__simpliC_Decl53

    @simpliC_Decl53.setter
    def simpliC_Decl53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpliC_Decl__simpliC_Decl53", None)
        self.__simpliC_Decl53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpliC_IDuse"):
                opp_val = getattr(old_value, "simpliC_IDuse", None)
                if opp_val == self:
                    setattr(old_value, "simpliC_IDuse", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpliC_IDuse"):
                opp_val = getattr(value, "simpliC_IDuse", None)
                setattr(value, "simpliC_IDuse", self)

    @property
    def simpliC_Decl(self):
        return self.__simpliC_Decl

    @simpliC_Decl.setter
    def simpliC_Decl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpliC_Decl__simpliC_Decl", None)
        self.__simpliC_Decl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpliC_Type34"):
                opp_val = getattr(old_value, "simpliC_Type34", None)
                if opp_val == self:
                    setattr(old_value, "simpliC_Type34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpliC_Type34"):
                opp_val = getattr(value, "simpliC_Type34", None)
                setattr(value, "simpliC_Type34", self)

    @property
    def simpliC_Decl36(self):
        return self.__simpliC_Decl36

    @simpliC_Decl36.setter
    def simpliC_Decl36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpliC_Decl__simpliC_Decl36", None)
        self.__simpliC_Decl36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpliC_Typedef"):
                opp_val = getattr(old_value, "simpliC_Typedef", None)
                if opp_val == self:
                    setattr(old_value, "simpliC_Typedef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpliC_Typedef"):
                opp_val = getattr(value, "simpliC_Typedef", None)
                setattr(value, "simpliC_Typedef", self)

class simpliC_Ifstmt(Stmt):

    pass
class simpliC_Call(Stmt):

    pass
class simpliC_Block(Stmt):

    pass
class simpliC_Args:

    def __init__(self, name: str, simpliC_Args: "simpliC_Function" = None, simpliC_Args55: "simpliC_Type" = None):
        self.name = name
        self.simpliC_Args = simpliC_Args
        self.simpliC_Args55 = simpliC_Args55
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simpliC_Args55(self):
        return self.__simpliC_Args55

    @simpliC_Args55.setter
    def simpliC_Args55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpliC_Args__simpliC_Args55", None)
        self.__simpliC_Args55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpliC_Type56"):
                opp_val = getattr(old_value, "simpliC_Type56", None)
                if opp_val == self:
                    setattr(old_value, "simpliC_Type56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpliC_Type56"):
                opp_val = getattr(value, "simpliC_Type56", None)
                setattr(value, "simpliC_Type56", self)

    @property
    def simpliC_Args(self):
        return self.__simpliC_Args

    @simpliC_Args.setter
    def simpliC_Args(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpliC_Args__simpliC_Args", None)
        self.__simpliC_Args = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpliC_Function4"):
                opp_val = getattr(old_value, "simpliC_Function4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpliC_Function4"):
                opp_val = getattr(value, "simpliC_Function4", None)
                if opp_val is None:
                    setattr(value, "simpliC_Function4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class simpliC_Type:

    def __init__(self, name: str, simpliC_Type: "simpliC_Function" = None, simpliC_Type56: "simpliC_Args" = None, simpliC_Type34: "simpliC_Decl" = None):
        self.name = name
        self.simpliC_Type = simpliC_Type
        self.simpliC_Type56 = simpliC_Type56
        self.simpliC_Type34 = simpliC_Type34
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simpliC_Type34(self):
        return self.__simpliC_Type34

    @simpliC_Type34.setter
    def simpliC_Type34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpliC_Type__simpliC_Type34", None)
        self.__simpliC_Type34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpliC_Decl"):
                opp_val = getattr(old_value, "simpliC_Decl", None)
                if opp_val == self:
                    setattr(old_value, "simpliC_Decl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpliC_Decl"):
                opp_val = getattr(value, "simpliC_Decl", None)
                setattr(value, "simpliC_Decl", self)

    @property
    def simpliC_Type56(self):
        return self.__simpliC_Type56

    @simpliC_Type56.setter
    def simpliC_Type56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpliC_Type__simpliC_Type56", None)
        self.__simpliC_Type56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpliC_Args55"):
                opp_val = getattr(old_value, "simpliC_Args55", None)
                if opp_val == self:
                    setattr(old_value, "simpliC_Args55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpliC_Args55"):
                opp_val = getattr(value, "simpliC_Args55", None)
                setattr(value, "simpliC_Args55", self)

    @property
    def simpliC_Type(self):
        return self.__simpliC_Type

    @simpliC_Type.setter
    def simpliC_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpliC_Type__simpliC_Type", None)
        self.__simpliC_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpliC_Function2"):
                opp_val = getattr(old_value, "simpliC_Function2", None)
                if opp_val == self:
                    setattr(old_value, "simpliC_Function2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpliC_Function2"):
                opp_val = getattr(value, "simpliC_Function2", None)
                setattr(value, "simpliC_Function2", self)

class simpliC_Function:

    def __init__(self, name: str, simpliC_Function: "simpliC_Model" = None, simpliC_Function2: "simpliC_Type" = None, simpliC_Function4: set["simpliC_Args"] = None, simpliC_Function6: "simpliC_Block" = None, simpliC_Function10: "simpliC_Call" = None, simpliC_Function14: "simpliC_ExprCall" = None):
        self.name = name
        self.simpliC_Function = simpliC_Function
        self.simpliC_Function2 = simpliC_Function2
        self.simpliC_Function4 = simpliC_Function4 if simpliC_Function4 is not None else set()
        self.simpliC_Function6 = simpliC_Function6
        self.simpliC_Function10 = simpliC_Function10
        self.simpliC_Function14 = simpliC_Function14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simpliC_Function6(self):
        return self.__simpliC_Function6

    @simpliC_Function6.setter
    def simpliC_Function6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpliC_Function__simpliC_Function6", None)
        self.__simpliC_Function6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpliC_Block"):
                opp_val = getattr(old_value, "simpliC_Block", None)
                if opp_val == self:
                    setattr(old_value, "simpliC_Block", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpliC_Block"):
                opp_val = getattr(value, "simpliC_Block", None)
                setattr(value, "simpliC_Block", self)

    @property
    def simpliC_Function4(self):
        return self.__simpliC_Function4

    @simpliC_Function4.setter
    def simpliC_Function4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpliC_Function__simpliC_Function4", None)
        self.__simpliC_Function4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpliC_Args"):
                    opp_val = getattr(item, "simpliC_Args", None)
                    
                    if opp_val == self:
                        setattr(item, "simpliC_Args", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpliC_Args"):
                    opp_val = getattr(item, "simpliC_Args", None)
                    
                    setattr(item, "simpliC_Args", self)
                    

    @property
    def simpliC_Function14(self):
        return self.__simpliC_Function14

    @simpliC_Function14.setter
    def simpliC_Function14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpliC_Function__simpliC_Function14", None)
        self.__simpliC_Function14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpliC_ExprCall"):
                opp_val = getattr(old_value, "simpliC_ExprCall", None)
                if opp_val == self:
                    setattr(old_value, "simpliC_ExprCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpliC_ExprCall"):
                opp_val = getattr(value, "simpliC_ExprCall", None)
                setattr(value, "simpliC_ExprCall", self)

    @property
    def simpliC_Function2(self):
        return self.__simpliC_Function2

    @simpliC_Function2.setter
    def simpliC_Function2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpliC_Function__simpliC_Function2", None)
        self.__simpliC_Function2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpliC_Type"):
                opp_val = getattr(old_value, "simpliC_Type", None)
                if opp_val == self:
                    setattr(old_value, "simpliC_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpliC_Type"):
                opp_val = getattr(value, "simpliC_Type", None)
                setattr(value, "simpliC_Type", self)

    @property
    def simpliC_Function(self):
        return self.__simpliC_Function

    @simpliC_Function.setter
    def simpliC_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpliC_Function__simpliC_Function", None)
        self.__simpliC_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpliC_Model"):
                opp_val = getattr(old_value, "simpliC_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpliC_Model"):
                opp_val = getattr(value, "simpliC_Model", None)
                if opp_val is None:
                    setattr(value, "simpliC_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simpliC_Function10(self):
        return self.__simpliC_Function10

    @simpliC_Function10.setter
    def simpliC_Function10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpliC_Function__simpliC_Function10", None)
        self.__simpliC_Function10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpliC_Call"):
                opp_val = getattr(old_value, "simpliC_Call", None)
                if opp_val == self:
                    setattr(old_value, "simpliC_Call", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpliC_Call"):
                opp_val = getattr(value, "simpliC_Call", None)
                setattr(value, "simpliC_Call", self)

class simpliC_Model:

    pass