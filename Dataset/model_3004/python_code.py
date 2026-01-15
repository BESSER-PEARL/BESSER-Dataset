from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class AccessLevel(Enum):
    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"
    PROTECTED = "PROTECTED"


############################################
# Definition of Classes
############################################

class Expression:

    pass
class miniJava_Neg(Expression):

    pass
class miniJava_FieldAccess(Expression):

    pass
class miniJava_Superior(Expression):

    pass
class miniJava_MethodCall(Expression):

    pass
class miniJava_Inferior(Expression):

    pass
class miniJava_Null(Expression):

    pass
class miniJava_Super(Expression):

    pass
class miniJava_InferiorOrEqual(Expression):

    pass
class miniJava_Plus(Expression):

    pass
class miniJava_ArrayLength(Expression):

    pass
class miniJava_Division(Expression):

    pass
class miniJava_BoolConstant(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class miniJava_Minus(Expression):

    pass
class miniJava_This(Expression):

    pass
class miniJava_Not(Expression):

    pass
class miniJava_Multiplication(Expression):

    pass
class miniJava_SymbolRef(Expression):

    pass
class miniJava_IntConstant(Expression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class miniJava_ArrayAccess(Expression):

    pass
class miniJava_StringConstant(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class miniJava_NewObject(Expression):

    pass
class miniJava_NewArray(Expression):

    pass
class miniJava_SuperiorOrEqual(Expression):

    pass
class miniJava_Or(Expression):

    pass
class miniJava_Inequality(Expression):

    pass
class miniJava_Equality(Expression):

    pass
class miniJava_And(Expression):

    pass
class miniJava_Assignee:

    pass
class miniJava_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class SingleTypeRef:

    pass
class miniJava_VoidTypeRef(SingleTypeRef):

    pass
class miniJava_IntegerTypeRef(SingleTypeRef):

    pass
class miniJava_BooleanTypeRef(SingleTypeRef):

    pass
class miniJava_StringTypeRef(SingleTypeRef):

    pass
class miniJava_ClassRef(SingleTypeRef):

    pass
class TypeRef:

    pass
class miniJava_ArrayTypeRef(TypeRef):

    pass
class miniJava_SingleTypeRef(TypeRef):

    pass
class miniJava_TypeRef:

    pass
class Assignee:

    pass
class Symbol:

    pass
class miniJava_VariableDeclaration(Symbol, Assignee):

    pass
class miniJava_Parameter(Symbol):

    pass
class Member:

    pass
class miniJava_Field(Member):

    pass
class miniJava_Method(Member):

    def __init__(self, abstract: bool, static: bool, miniJava_Method: set["miniJava_Parameter"] = None, miniJava_Method11: "miniJava_Block" = None, miniJava_Method131: "miniJava_MethodCall" = None):
        self.abstract = abstract
        self.static = static
        self.miniJava_Method = miniJava_Method if miniJava_Method is not None else set()
        self.miniJava_Method11 = miniJava_Method11
        self.miniJava_Method131 = miniJava_Method131
        
    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def miniJava_Method11(self):
        return self.__miniJava_Method11

    @miniJava_Method11.setter
    def miniJava_Method11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Method__miniJava_Method11", None)
        self.__miniJava_Method11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Block"):
                opp_val = getattr(old_value, "miniJava_Block", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Block", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Block"):
                opp_val = getattr(value, "miniJava_Block", None)
                setattr(value, "miniJava_Block", self)

    @property
    def miniJava_Method131(self):
        return self.__miniJava_Method131

    @miniJava_Method131.setter
    def miniJava_Method131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Method__miniJava_Method131", None)
        self.__miniJava_Method131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_MethodCall130"):
                opp_val = getattr(old_value, "miniJava_MethodCall130", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_MethodCall130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_MethodCall130"):
                opp_val = getattr(value, "miniJava_MethodCall130", None)
                setattr(value, "miniJava_MethodCall130", self)

    @property
    def miniJava_Method(self):
        return self.__miniJava_Method

    @miniJava_Method.setter
    def miniJava_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Method__miniJava_Method", None)
        self.__miniJava_Method = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "miniJava_Parameter"):
                    opp_val = getattr(item, "miniJava_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "miniJava_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "miniJava_Parameter"):
                    opp_val = getattr(item, "miniJava_Parameter", None)
                    
                    setattr(item, "miniJava_Parameter", self)
                    

class TypedDeclaration:

    pass
class miniJava_Symbol(TypedDeclaration):

    pass
class miniJava_Statement:

    pass
class Statement:

    pass
class miniJava_PrintStatement(Statement):

    pass
class miniJava_IfStatement(Statement):

    pass
class miniJava_Assignment(Statement):

    pass
class miniJava_Block(Statement):

    pass
class miniJava_WhileStatement(Statement):

    pass
class miniJava_Return(Statement):

    pass
class miniJava_ForStatement(Statement):

    pass
class miniJava_Expression(Assignee, Statement):

    pass
class TypeDeclaration:

    pass
class miniJava_Class(TypeDeclaration):

    def __init__(self, abstract: bool, miniJava_Class: "miniJava_Class" = None, miniJava_Class7: "miniJava_Class" = None, miniJava_Class136: "miniJava_NewObject" = None):
        self.abstract = abstract
        self.miniJava_Class = miniJava_Class
        self.miniJava_Class7 = miniJava_Class7
        self.miniJava_Class136 = miniJava_Class136
        
    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def miniJava_Class136(self):
        return self.__miniJava_Class136

    @miniJava_Class136.setter
    def miniJava_Class136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Class__miniJava_Class136", None)
        self.__miniJava_Class136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_NewObject"):
                opp_val = getattr(old_value, "miniJava_NewObject", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_NewObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_NewObject"):
                opp_val = getattr(value, "miniJava_NewObject", None)
                setattr(value, "miniJava_NewObject", self)

    @property
    def miniJava_Class7(self):
        return self.__miniJava_Class7

    @miniJava_Class7.setter
    def miniJava_Class7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Class__miniJava_Class7", None)
        self.__miniJava_Class7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Class"):
                opp_val = getattr(old_value, "miniJava_Class", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Class"):
                opp_val = getattr(value, "miniJava_Class", None)
                setattr(value, "miniJava_Class", self)

    @property
    def miniJava_Class(self):
        return self.__miniJava_Class

    @miniJava_Class.setter
    def miniJava_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Class__miniJava_Class", None)
        self.__miniJava_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Class7"):
                opp_val = getattr(old_value, "miniJava_Class7", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Class7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Class7"):
                opp_val = getattr(value, "miniJava_Class7", None)
                setattr(value, "miniJava_Class7", self)

class miniJava_Member(TypedDeclaration):

    def __init__(self, access: str, miniJava_Member: "miniJava_TypeDeclaration" = None):
        self.access = access
        self.miniJava_Member = miniJava_Member
        
    @property
    def access(self) -> str:
        return self.__access

    @access.setter
    def access(self, access: str):
        self.__access = access

    @property
    def miniJava_Member(self):
        return self.__miniJava_Member

    @miniJava_Member.setter
    def miniJava_Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Member__miniJava_Member", None)
        self.__miniJava_Member = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_TypeDeclaration6"):
                opp_val = getattr(old_value, "miniJava_TypeDeclaration6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_TypeDeclaration6"):
                opp_val = getattr(value, "miniJava_TypeDeclaration6", None)
                if opp_val is None:
                    setattr(value, "miniJava_TypeDeclaration6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class miniJava_Interface(TypeDeclaration):

    pass
class NamedElement:

    pass
class miniJava_TypedDeclaration(NamedElement):

    pass
class miniJava_TypeDeclaration(NamedElement):

    def __init__(self, accessLevel: str, miniJava_TypeDeclaration: "miniJava_Program" = None, miniJava_TypeDeclaration4: set["miniJava_Interface"] = None, miniJava_TypeDeclaration6: set["miniJava_Member"] = None, miniJava_TypeDeclaration43: "miniJava_ClassRef" = None):
        self.accessLevel = accessLevel
        self.miniJava_TypeDeclaration = miniJava_TypeDeclaration
        self.miniJava_TypeDeclaration4 = miniJava_TypeDeclaration4 if miniJava_TypeDeclaration4 is not None else set()
        self.miniJava_TypeDeclaration6 = miniJava_TypeDeclaration6 if miniJava_TypeDeclaration6 is not None else set()
        self.miniJava_TypeDeclaration43 = miniJava_TypeDeclaration43
        
    @property
    def accessLevel(self) -> str:
        return self.__accessLevel

    @accessLevel.setter
    def accessLevel(self, accessLevel: str):
        self.__accessLevel = accessLevel

    @property
    def miniJava_TypeDeclaration43(self):
        return self.__miniJava_TypeDeclaration43

    @miniJava_TypeDeclaration43.setter
    def miniJava_TypeDeclaration43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_TypeDeclaration__miniJava_TypeDeclaration43", None)
        self.__miniJava_TypeDeclaration43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_ClassRef"):
                opp_val = getattr(old_value, "miniJava_ClassRef", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_ClassRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_ClassRef"):
                opp_val = getattr(value, "miniJava_ClassRef", None)
                setattr(value, "miniJava_ClassRef", self)

    @property
    def miniJava_TypeDeclaration(self):
        return self.__miniJava_TypeDeclaration

    @miniJava_TypeDeclaration.setter
    def miniJava_TypeDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_TypeDeclaration__miniJava_TypeDeclaration", None)
        self.__miniJava_TypeDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Program2"):
                opp_val = getattr(old_value, "miniJava_Program2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Program2"):
                opp_val = getattr(value, "miniJava_Program2", None)
                if opp_val is None:
                    setattr(value, "miniJava_Program2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def miniJava_TypeDeclaration4(self):
        return self.__miniJava_TypeDeclaration4

    @miniJava_TypeDeclaration4.setter
    def miniJava_TypeDeclaration4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_TypeDeclaration__miniJava_TypeDeclaration4", None)
        self.__miniJava_TypeDeclaration4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "miniJava_Interface"):
                    opp_val = getattr(item, "miniJava_Interface", None)
                    
                    if opp_val == self:
                        setattr(item, "miniJava_Interface", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "miniJava_Interface"):
                    opp_val = getattr(item, "miniJava_Interface", None)
                    
                    setattr(item, "miniJava_Interface", self)
                    

    @property
    def miniJava_TypeDeclaration6(self):
        return self.__miniJava_TypeDeclaration6

    @miniJava_TypeDeclaration6.setter
    def miniJava_TypeDeclaration6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_TypeDeclaration__miniJava_TypeDeclaration6", None)
        self.__miniJava_TypeDeclaration6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "miniJava_Member"):
                    opp_val = getattr(item, "miniJava_Member", None)
                    
                    if opp_val == self:
                        setattr(item, "miniJava_Member", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "miniJava_Member"):
                    opp_val = getattr(item, "miniJava_Member", None)
                    
                    setattr(item, "miniJava_Member", self)
                    

class miniJava_Import:

    def __init__(self, importedNamespace: str, miniJava_Import: "miniJava_Program" = None):
        self.importedNamespace = importedNamespace
        self.miniJava_Import = miniJava_Import
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

    @property
    def miniJava_Import(self):
        return self.__miniJava_Import

    @miniJava_Import.setter
    def miniJava_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Import__miniJava_Import", None)
        self.__miniJava_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Program"):
                opp_val = getattr(old_value, "miniJava_Program", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Program"):
                opp_val = getattr(value, "miniJava_Program", None)
                if opp_val is None:
                    setattr(value, "miniJava_Program", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class miniJava_Program:

    def __init__(self, name: str, miniJava_Program: set["miniJava_Import"] = None, miniJava_Program2: set["miniJava_TypeDeclaration"] = None):
        self.name = name
        self.miniJava_Program = miniJava_Program if miniJava_Program is not None else set()
        self.miniJava_Program2 = miniJava_Program2 if miniJava_Program2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def miniJava_Program2(self):
        return self.__miniJava_Program2

    @miniJava_Program2.setter
    def miniJava_Program2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Program__miniJava_Program2", None)
        self.__miniJava_Program2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "miniJava_TypeDeclaration"):
                    opp_val = getattr(item, "miniJava_TypeDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "miniJava_TypeDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "miniJava_TypeDeclaration"):
                    opp_val = getattr(item, "miniJava_TypeDeclaration", None)
                    
                    setattr(item, "miniJava_TypeDeclaration", self)
                    

    @property
    def miniJava_Program(self):
        return self.__miniJava_Program

    @miniJava_Program.setter
    def miniJava_Program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Program__miniJava_Program", None)
        self.__miniJava_Program = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "miniJava_Import"):
                    opp_val = getattr(item, "miniJava_Import", None)
                    
                    if opp_val == self:
                        setattr(item, "miniJava_Import", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "miniJava_Import"):
                    opp_val = getattr(item, "miniJava_Import", None)
                    
                    setattr(item, "miniJava_Import", self)
                    
