from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class UnaryOp(Enum):
    NEGATE = "NEGATE"
    NOT = "NOT"
class BinaryOp(Enum):
    ADD = "ADD"
    SUB = "SUB"
    MUL = "MUL"
    LT = "LT"
    LEQ = "LEQ"
    EQ = "EQ"
    GEQ = "GEQ"
    GT = "GT"
    AND = "AND"
    OR = "OR"


############################################
# Definition of Classes
############################################

class NamedElement:

    pass
class imp_NamedElement(ABC):

    pass
class imp_Symbol(NamedElement):

    pass
class imp_Member(ABC):

    pass
class Member:

    pass
class imp_AttributeDecl(Member):

    def __init__(self, name: str, imp_AttributeDecl: "imp_Class" = None):
        self.name = name
        self.imp_AttributeDecl = imp_AttributeDecl
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def imp_AttributeDecl(self):
        return self.__imp_AttributeDecl

    @imp_AttributeDecl.setter
    def imp_AttributeDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imp_AttributeDecl__imp_AttributeDecl", None)
        self.__imp_AttributeDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imp_Class45"):
                opp_val = getattr(old_value, "imp_Class45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imp_Class45"):
                opp_val = getattr(value, "imp_Class45", None)
                if opp_val is None:
                    setattr(value, "imp_Class45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class imp_Class(NamedElement):

    def __init__(self, name: str, imp_Class: "imp_Program" = None, imp_Class45: set["imp_AttributeDecl"] = None, imp_Class47: set["imp_MethodDecl"] = None, imp_Class50: "imp_NewClass" = None):
        self.name = name
        self.imp_Class = imp_Class
        self.imp_Class45 = imp_Class45 if imp_Class45 is not None else set()
        self.imp_Class47 = imp_Class47 if imp_Class47 is not None else set()
        self.imp_Class50 = imp_Class50
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def imp_Class45(self):
        return self.__imp_Class45

    @imp_Class45.setter
    def imp_Class45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imp_Class__imp_Class45", None)
        self.__imp_Class45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "imp_AttributeDecl"):
                    opp_val = getattr(item, "imp_AttributeDecl", None)
                    
                    if opp_val == self:
                        setattr(item, "imp_AttributeDecl", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "imp_AttributeDecl"):
                    opp_val = getattr(item, "imp_AttributeDecl", None)
                    
                    setattr(item, "imp_AttributeDecl", self)
                    

    @property
    def imp_Class50(self):
        return self.__imp_Class50

    @imp_Class50.setter
    def imp_Class50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imp_Class__imp_Class50", None)
        self.__imp_Class50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imp_NewClass"):
                opp_val = getattr(old_value, "imp_NewClass", None)
                if opp_val == self:
                    setattr(old_value, "imp_NewClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imp_NewClass"):
                opp_val = getattr(value, "imp_NewClass", None)
                setattr(value, "imp_NewClass", self)

    @property
    def imp_Class(self):
        return self.__imp_Class

    @imp_Class.setter
    def imp_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imp_Class__imp_Class", None)
        self.__imp_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imp_Program34"):
                opp_val = getattr(old_value, "imp_Program34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imp_Program34"):
                opp_val = getattr(value, "imp_Program34", None)
                if opp_val is None:
                    setattr(value, "imp_Program34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def imp_Class47(self):
        return self.__imp_Class47

    @imp_Class47.setter
    def imp_Class47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imp_Class__imp_Class47", None)
        self.__imp_Class47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "imp_MethodDecl48"):
                    opp_val = getattr(item, "imp_MethodDecl48", None)
                    
                    if opp_val == self:
                        setattr(item, "imp_MethodDecl48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "imp_MethodDecl48"):
                    opp_val = getattr(item, "imp_MethodDecl48", None)
                    
                    setattr(item, "imp_MethodDecl48", self)
                    

class imp_MethodDecl(Member):

    def __init__(self, name: str, imp_MethodDecl: "imp_Program" = None, imp_MethodDecl36: "imp_Stmt" = None, imp_MethodDecl39: set["imp_ParamDecl"] = None, imp_MethodDecl48: "imp_Class" = None):
        self.name = name
        self.imp_MethodDecl = imp_MethodDecl
        self.imp_MethodDecl36 = imp_MethodDecl36
        self.imp_MethodDecl39 = imp_MethodDecl39 if imp_MethodDecl39 is not None else set()
        self.imp_MethodDecl48 = imp_MethodDecl48
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def imp_MethodDecl36(self):
        return self.__imp_MethodDecl36

    @imp_MethodDecl36.setter
    def imp_MethodDecl36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imp_MethodDecl__imp_MethodDecl36", None)
        self.__imp_MethodDecl36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imp_Stmt37"):
                opp_val = getattr(old_value, "imp_Stmt37", None)
                if opp_val == self:
                    setattr(old_value, "imp_Stmt37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imp_Stmt37"):
                opp_val = getattr(value, "imp_Stmt37", None)
                setattr(value, "imp_Stmt37", self)

    @property
    def imp_MethodDecl48(self):
        return self.__imp_MethodDecl48

    @imp_MethodDecl48.setter
    def imp_MethodDecl48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imp_MethodDecl__imp_MethodDecl48", None)
        self.__imp_MethodDecl48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imp_Class47"):
                opp_val = getattr(old_value, "imp_Class47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imp_Class47"):
                opp_val = getattr(value, "imp_Class47", None)
                if opp_val is None:
                    setattr(value, "imp_Class47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def imp_MethodDecl39(self):
        return self.__imp_MethodDecl39

    @imp_MethodDecl39.setter
    def imp_MethodDecl39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imp_MethodDecl__imp_MethodDecl39", None)
        self.__imp_MethodDecl39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "imp_ParamDecl"):
                    opp_val = getattr(item, "imp_ParamDecl", None)
                    
                    if opp_val == self:
                        setattr(item, "imp_ParamDecl", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "imp_ParamDecl"):
                    opp_val = getattr(item, "imp_ParamDecl", None)
                    
                    setattr(item, "imp_ParamDecl", self)
                    

    @property
    def imp_MethodDecl(self):
        return self.__imp_MethodDecl

    @imp_MethodDecl.setter
    def imp_MethodDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imp_MethodDecl__imp_MethodDecl", None)
        self.__imp_MethodDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imp_Program"):
                opp_val = getattr(old_value, "imp_Program", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imp_Program"):
                opp_val = getattr(value, "imp_Program", None)
                if opp_val is None:
                    setattr(value, "imp_Program", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class imp_Program:

    pass
class Value:

    pass
class imp_StringValue(Value):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class imp_ArrayValue(Value):

    pass
class imp_BoolValue(Value):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class imp_IntValue(Value):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class imp_Value(ABC):

    pass
class imp_StringToValueMap:

    def __init__(self, key: str, imp_StringToValueMap: "imp_Store" = None, imp_StringToValueMap27: "imp_Value" = None):
        self.key = key
        self.imp_StringToValueMap = imp_StringToValueMap
        self.imp_StringToValueMap27 = imp_StringToValueMap27
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def imp_StringToValueMap(self):
        return self.__imp_StringToValueMap

    @imp_StringToValueMap.setter
    def imp_StringToValueMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imp_StringToValueMap__imp_StringToValueMap", None)
        self.__imp_StringToValueMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imp_Store"):
                opp_val = getattr(old_value, "imp_Store", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imp_Store"):
                opp_val = getattr(value, "imp_Store", None)
                if opp_val is None:
                    setattr(value, "imp_Store", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def imp_StringToValueMap27(self):
        return self.__imp_StringToValueMap27

    @imp_StringToValueMap27.setter
    def imp_StringToValueMap27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imp_StringToValueMap__imp_StringToValueMap27", None)
        self.__imp_StringToValueMap27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imp_Value"):
                opp_val = getattr(old_value, "imp_Value", None)
                if opp_val == self:
                    setattr(old_value, "imp_Value", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imp_Value"):
                opp_val = getattr(value, "imp_Value", None)
                setattr(value, "imp_Value", self)

class imp_Store:

    pass
class Expr:

    pass
class imp_VarRef(Expr):

    pass
class imp_This(Expr):

    pass
class imp_Unary(Expr):

    def __init__(self, op: str, imp_Unary: "imp_Expr" = None):
        self.op = op
        self.imp_Unary = imp_Unary
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def imp_Unary(self):
        return self.__imp_Unary

    @imp_Unary.setter
    def imp_Unary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imp_Unary__imp_Unary", None)
        self.__imp_Unary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imp_Expr19"):
                opp_val = getattr(old_value, "imp_Expr19", None)
                if opp_val == self:
                    setattr(old_value, "imp_Expr19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imp_Expr19"):
                opp_val = getattr(value, "imp_Expr19", None)
                setattr(value, "imp_Expr19", self)

class imp_Project(Expr):

    def __init__(self, ismethodcall: bool, imp_Project: "imp_Expr" = None, imp_Project59: "imp_Member" = None, imp_Project61: set["imp_Expr"] = None):
        self.ismethodcall = ismethodcall
        self.imp_Project = imp_Project
        self.imp_Project59 = imp_Project59
        self.imp_Project61 = imp_Project61 if imp_Project61 is not None else set()
        
    @property
    def ismethodcall(self) -> bool:
        return self.__ismethodcall

    @ismethodcall.setter
    def ismethodcall(self, ismethodcall: bool):
        self.__ismethodcall = ismethodcall

    @property
    def imp_Project59(self):
        return self.__imp_Project59

    @imp_Project59.setter
    def imp_Project59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imp_Project__imp_Project59", None)
        self.__imp_Project59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imp_Member"):
                opp_val = getattr(old_value, "imp_Member", None)
                if opp_val == self:
                    setattr(old_value, "imp_Member", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imp_Member"):
                opp_val = getattr(value, "imp_Member", None)
                setattr(value, "imp_Member", self)

    @property
    def imp_Project61(self):
        return self.__imp_Project61

    @imp_Project61.setter
    def imp_Project61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imp_Project__imp_Project61", None)
        self.__imp_Project61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "imp_Expr62"):
                    opp_val = getattr(item, "imp_Expr62", None)
                    
                    if opp_val == self:
                        setattr(item, "imp_Expr62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "imp_Expr62"):
                    opp_val = getattr(item, "imp_Expr62", None)
                    
                    setattr(item, "imp_Expr62", self)
                    

    @property
    def imp_Project(self):
        return self.__imp_Project

    @imp_Project.setter
    def imp_Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imp_Project__imp_Project", None)
        self.__imp_Project = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imp_Expr57"):
                opp_val = getattr(old_value, "imp_Expr57", None)
                if opp_val == self:
                    setattr(old_value, "imp_Expr57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imp_Expr57"):
                opp_val = getattr(value, "imp_Expr57", None)
                setattr(value, "imp_Expr57", self)

class imp_BoolConst(Expr):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class imp_StringConst(Expr):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class imp_Binary(Expr):

    def __init__(self, op: str, imp_Binary: "imp_Expr" = None, imp_Binary23: "imp_Expr" = None):
        self.op = op
        self.imp_Binary = imp_Binary
        self.imp_Binary23 = imp_Binary23
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def imp_Binary23(self):
        return self.__imp_Binary23

    @imp_Binary23.setter
    def imp_Binary23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imp_Binary__imp_Binary23", None)
        self.__imp_Binary23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imp_Expr24"):
                opp_val = getattr(old_value, "imp_Expr24", None)
                if opp_val == self:
                    setattr(old_value, "imp_Expr24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imp_Expr24"):
                opp_val = getattr(value, "imp_Expr24", None)
                setattr(value, "imp_Expr24", self)

    @property
    def imp_Binary(self):
        return self.__imp_Binary

    @imp_Binary.setter
    def imp_Binary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imp_Binary__imp_Binary", None)
        self.__imp_Binary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imp_Expr21"):
                opp_val = getattr(old_value, "imp_Expr21", None)
                if opp_val == self:
                    setattr(old_value, "imp_Expr21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imp_Expr21"):
                opp_val = getattr(value, "imp_Expr21", None)
                setattr(value, "imp_Expr21", self)

class imp_NewClass(Expr):

    pass
class imp_ArrayDecl(Expr):

    pass
class imp_IntConst(Expr):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class Symbol:

    pass
class imp_ParamDecl(Symbol):

    def __init__(self, name: str, imp_ParamDecl: "imp_MethodDecl" = None):
        self.name = name
        self.imp_ParamDecl = imp_ParamDecl
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def imp_ParamDecl(self):
        return self.__imp_ParamDecl

    @imp_ParamDecl.setter
    def imp_ParamDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imp_ParamDecl__imp_ParamDecl", None)
        self.__imp_ParamDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imp_MethodDecl39"):
                opp_val = getattr(old_value, "imp_MethodDecl39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imp_MethodDecl39"):
                opp_val = getattr(value, "imp_MethodDecl39", None)
                if opp_val is None:
                    setattr(value, "imp_MethodDecl39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Stmt:

    pass
class imp_While(Stmt):

    pass
class imp_Expr(Stmt):

    pass
class imp_If(Stmt):

    pass
class imp_Print(Stmt):

    pass
class imp_Assignment(Stmt):

    pass
class imp_Block(Stmt):

    pass
class imp_Return(Stmt):

    pass
class imp_Declaration(Stmt, Symbol):

    def __init__(self, name: str, imp_Declaration: "imp_Expr" = None, imp_Declaration2: "imp_Expr" = None):
        self.name = name
        self.imp_Declaration = imp_Declaration
        self.imp_Declaration2 = imp_Declaration2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def imp_Declaration(self):
        return self.__imp_Declaration

    @imp_Declaration.setter
    def imp_Declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imp_Declaration__imp_Declaration", None)
        self.__imp_Declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imp_Expr"):
                opp_val = getattr(old_value, "imp_Expr", None)
                if opp_val == self:
                    setattr(old_value, "imp_Expr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imp_Expr"):
                opp_val = getattr(value, "imp_Expr", None)
                setattr(value, "imp_Expr", self)

    @property
    def imp_Declaration2(self):
        return self.__imp_Declaration2

    @imp_Declaration2.setter
    def imp_Declaration2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imp_Declaration__imp_Declaration2", None)
        self.__imp_Declaration2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imp_Expr3"):
                opp_val = getattr(old_value, "imp_Expr3", None)
                if opp_val == self:
                    setattr(old_value, "imp_Expr3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imp_Expr3"):
                opp_val = getattr(value, "imp_Expr3", None)
                setattr(value, "imp_Expr3", self)

class imp_Stmt(ABC):

    pass