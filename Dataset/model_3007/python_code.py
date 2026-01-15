from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AccessLevel(Enum):
    PRIVATE = "PRIVATE"
    PROTECTED = "PROTECTED"
    PUBLIC = "PUBLIC"


############################################
# Definition of Classes
############################################

class miniJava_Frame:

    pass
class miniJava_OutputStream:

    def __init__(self, stream: str, miniJava_OutputStream: "miniJava_State" = None):
        self.stream = stream
        self.miniJava_OutputStream = miniJava_OutputStream
        
    @property
    def stream(self) -> str:
        return self.__stream

    @stream.setter
    def stream(self, stream: str):
        self.__stream = stream

    @property
    def miniJava_OutputStream(self):
        return self.__miniJava_OutputStream

    @miniJava_OutputStream.setter
    def miniJava_OutputStream(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_OutputStream__miniJava_OutputStream", None)
        self.__miniJava_OutputStream = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_State173"):
                opp_val = getattr(old_value, "miniJava_State173", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_State173", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_State173"):
                opp_val = getattr(value, "miniJava_State173", None)
                setattr(value, "miniJava_State173", self)

class Call:

    pass
class miniJava_MethodCall2(Call):

    pass
class miniJava_NewCall(Call):

    pass
class miniJava_Call(ABC):

    pass
class miniJava_ArrayInstance:

    def __init__(self, size: int, miniJava_ArrayInstance: "miniJava_State" = None, miniJava_ArrayInstance209: set["miniJava_Value"] = None, miniJava_ArrayInstance214: "miniJava_ArrayRefValue" = None):
        self.size = size
        self.miniJava_ArrayInstance = miniJava_ArrayInstance
        self.miniJava_ArrayInstance209 = miniJava_ArrayInstance209 if miniJava_ArrayInstance209 is not None else set()
        self.miniJava_ArrayInstance214 = miniJava_ArrayInstance214
        
    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def miniJava_ArrayInstance209(self):
        return self.__miniJava_ArrayInstance209

    @miniJava_ArrayInstance209.setter
    def miniJava_ArrayInstance209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_ArrayInstance__miniJava_ArrayInstance209", None)
        self.__miniJava_ArrayInstance209 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "miniJava_Value210"):
                    opp_val = getattr(item, "miniJava_Value210", None)
                    
                    if opp_val == self:
                        setattr(item, "miniJava_Value210", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "miniJava_Value210"):
                    opp_val = getattr(item, "miniJava_Value210", None)
                    
                    setattr(item, "miniJava_Value210", self)
                    

    @property
    def miniJava_ArrayInstance(self):
        return self.__miniJava_ArrayInstance

    @miniJava_ArrayInstance.setter
    def miniJava_ArrayInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_ArrayInstance__miniJava_ArrayInstance", None)
        self.__miniJava_ArrayInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_State175"):
                opp_val = getattr(old_value, "miniJava_State175", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_State175"):
                opp_val = getattr(value, "miniJava_State175", None)
                if opp_val is None:
                    setattr(value, "miniJava_State175", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def miniJava_ArrayInstance214(self):
        return self.__miniJava_ArrayInstance214

    @miniJava_ArrayInstance214.setter
    def miniJava_ArrayInstance214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_ArrayInstance__miniJava_ArrayInstance214", None)
        self.__miniJava_ArrayInstance214 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_ArrayRefValue"):
                opp_val = getattr(old_value, "miniJava_ArrayRefValue", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_ArrayRefValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_ArrayRefValue"):
                opp_val = getattr(value, "miniJava_ArrayRefValue", None)
                setattr(value, "miniJava_ArrayRefValue", self)

class miniJava_ObjectInstance:

    pass
class miniJava_FieldBinding:

    pass
class Value:

    pass
class miniJava_ObjectRefValue(Value):

    pass
class miniJava_BooleanValue(Value):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class miniJava_NullValue(Value):

    pass
class miniJava_ArrayRefValue(Value):

    pass
class miniJava_StringValue(Value):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class miniJava_IntegerValue(Value):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class miniJava_Value:

    pass
class miniJava_SymbolToSymbolBindingMap:

    pass
class miniJava_SymbolBinding:

    pass
class miniJava_Context:

    pass
class miniJava_Assignee:

    pass
class Assignee:

    pass
class Expression:

    pass
class miniJava_InferiorOrEqual(Expression):

    pass
class miniJava_Modulo(Expression):

    pass
class miniJava_ArrayAccess(Expression):

    pass
class miniJava_Not(Expression):

    pass
class miniJava_Null(Expression):

    pass
class miniJava_MethodCall(Expression):

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

class miniJava_BoolConstant(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class miniJava_Super(Expression):

    pass
class miniJava_Superior(Expression):

    pass
class miniJava_And(Expression):

    pass
class miniJava_FieldAccess(Expression):

    pass
class miniJava_Equality(Expression):

    pass
class miniJava_Inferior(Expression):

    pass
class miniJava_Inequality(Expression):

    pass
class miniJava_NewObject(Expression):

    pass
class miniJava_This(Expression):

    pass
class miniJava_ArrayLength(Expression):

    pass
class miniJava_Plus(Expression):

    pass
class miniJava_Division(Expression):

    pass
class miniJava_Neg(Expression):

    pass
class miniJava_SymbolRef(Expression):

    pass
class miniJava_Minus(Expression):

    pass
class miniJava_NewArray(Expression):

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

class miniJava_SuperiorOrEqual(Expression):

    pass
class miniJava_Multiplication(Expression):

    pass
class miniJava_Or(Expression):

    pass
class SingleTypeRef:

    pass
class miniJava_IntegerTypeRef(SingleTypeRef):

    pass
class miniJava_BooleanTypeRef(SingleTypeRef):

    pass
class miniJava_StringTypeRef(SingleTypeRef):

    pass
class miniJava_VoidTypeRef(SingleTypeRef):

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
class miniJava_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class miniJava_Statement:

    pass
class Statement:

    pass
class miniJava_WhileStatement(Statement):

    pass
class miniJava_Return(Statement):

    pass
class miniJava_Assignment(Statement):

    pass
class miniJava_PrintStatement(Statement):

    pass
class miniJava_ForStatement(Statement):

    pass
class miniJava_IfStatement(Statement):

    pass
class miniJava_Expression(Statement, Assignee):

    pass
class Symbol:

    pass
class miniJava_VariableDeclaration(Assignee, Symbol):

    pass
class miniJava_Parameter(Symbol):

    pass
class Member:

    pass
class miniJava_Field(Member):

    pass
class miniJava_Method(Member):

    def __init__(self, isabstract: bool, isstatic: bool, miniJava_Method: set["miniJava_Parameter"] = None, miniJava_Method13: "miniJava_Block" = None, miniJava_Method15: set["miniJava_ClazzToMethodMap"] = None, miniJava_Method135: "miniJava_MethodCall" = None, miniJava_Method226: "miniJava_ClazzToMethodMap" = None):
        self.isabstract = isabstract
        self.isstatic = isstatic
        self.miniJava_Method = miniJava_Method if miniJava_Method is not None else set()
        self.miniJava_Method13 = miniJava_Method13
        self.miniJava_Method15 = miniJava_Method15 if miniJava_Method15 is not None else set()
        self.miniJava_Method135 = miniJava_Method135
        self.miniJava_Method226 = miniJava_Method226
        
    @property
    def isabstract(self) -> bool:
        return self.__isabstract

    @isabstract.setter
    def isabstract(self, isabstract: bool):
        self.__isabstract = isabstract

    @property
    def isstatic(self) -> bool:
        return self.__isstatic

    @isstatic.setter
    def isstatic(self, isstatic: bool):
        self.__isstatic = isstatic

    @property
    def miniJava_Method135(self):
        return self.__miniJava_Method135

    @miniJava_Method135.setter
    def miniJava_Method135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Method__miniJava_Method135", None)
        self.__miniJava_Method135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_MethodCall134"):
                opp_val = getattr(old_value, "miniJava_MethodCall134", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_MethodCall134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_MethodCall134"):
                opp_val = getattr(value, "miniJava_MethodCall134", None)
                setattr(value, "miniJava_MethodCall134", self)

    @property
    def miniJava_Method15(self):
        return self.__miniJava_Method15

    @miniJava_Method15.setter
    def miniJava_Method15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Method__miniJava_Method15", None)
        self.__miniJava_Method15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "miniJava_ClazzToMethodMap"):
                    opp_val = getattr(item, "miniJava_ClazzToMethodMap", None)
                    
                    if opp_val == self:
                        setattr(item, "miniJava_ClazzToMethodMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "miniJava_ClazzToMethodMap"):
                    opp_val = getattr(item, "miniJava_ClazzToMethodMap", None)
                    
                    setattr(item, "miniJava_ClazzToMethodMap", self)
                    

    @property
    def miniJava_Method13(self):
        return self.__miniJava_Method13

    @miniJava_Method13.setter
    def miniJava_Method13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Method__miniJava_Method13", None)
        self.__miniJava_Method13 = value
        
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
    def miniJava_Method226(self):
        return self.__miniJava_Method226

    @miniJava_Method226.setter
    def miniJava_Method226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Method__miniJava_Method226", None)
        self.__miniJava_Method226 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_ClazzToMethodMap225"):
                opp_val = getattr(old_value, "miniJava_ClazzToMethodMap225", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_ClazzToMethodMap225", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_ClazzToMethodMap225"):
                opp_val = getattr(value, "miniJava_ClazzToMethodMap225", None)
                setattr(value, "miniJava_ClazzToMethodMap225", self)

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
class TypeDeclaration:

    pass
class miniJava_Clazz(TypeDeclaration):

    def __init__(self, isabstract: bool, miniJava_Clazz: "miniJava_Clazz" = None, miniJava_Clazz9: "miniJava_Clazz" = None, miniJava_Clazz140: "miniJava_NewObject" = None, miniJava_Clazz207: "miniJava_ObjectInstance" = None, miniJava_Clazz223: "miniJava_ClazzToMethodMap" = None):
        self.isabstract = isabstract
        self.miniJava_Clazz = miniJava_Clazz
        self.miniJava_Clazz9 = miniJava_Clazz9
        self.miniJava_Clazz140 = miniJava_Clazz140
        self.miniJava_Clazz207 = miniJava_Clazz207
        self.miniJava_Clazz223 = miniJava_Clazz223
        
    @property
    def isabstract(self) -> bool:
        return self.__isabstract

    @isabstract.setter
    def isabstract(self, isabstract: bool):
        self.__isabstract = isabstract

    @property
    def miniJava_Clazz(self):
        return self.__miniJava_Clazz

    @miniJava_Clazz.setter
    def miniJava_Clazz(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Clazz__miniJava_Clazz", None)
        self.__miniJava_Clazz = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Clazz9"):
                opp_val = getattr(old_value, "miniJava_Clazz9", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Clazz9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Clazz9"):
                opp_val = getattr(value, "miniJava_Clazz9", None)
                setattr(value, "miniJava_Clazz9", self)

    @property
    def miniJava_Clazz140(self):
        return self.__miniJava_Clazz140

    @miniJava_Clazz140.setter
    def miniJava_Clazz140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Clazz__miniJava_Clazz140", None)
        self.__miniJava_Clazz140 = value
        
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
    def miniJava_Clazz223(self):
        return self.__miniJava_Clazz223

    @miniJava_Clazz223.setter
    def miniJava_Clazz223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Clazz__miniJava_Clazz223", None)
        self.__miniJava_Clazz223 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_ClazzToMethodMap222"):
                opp_val = getattr(old_value, "miniJava_ClazzToMethodMap222", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_ClazzToMethodMap222", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_ClazzToMethodMap222"):
                opp_val = getattr(value, "miniJava_ClazzToMethodMap222", None)
                setattr(value, "miniJava_ClazzToMethodMap222", self)

    @property
    def miniJava_Clazz207(self):
        return self.__miniJava_Clazz207

    @miniJava_Clazz207.setter
    def miniJava_Clazz207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Clazz__miniJava_Clazz207", None)
        self.__miniJava_Clazz207 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_ObjectInstance206"):
                opp_val = getattr(old_value, "miniJava_ObjectInstance206", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_ObjectInstance206", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_ObjectInstance206"):
                opp_val = getattr(value, "miniJava_ObjectInstance206", None)
                setattr(value, "miniJava_ObjectInstance206", self)

    @property
    def miniJava_Clazz9(self):
        return self.__miniJava_Clazz9

    @miniJava_Clazz9.setter
    def miniJava_Clazz9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Clazz__miniJava_Clazz9", None)
        self.__miniJava_Clazz9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Clazz"):
                opp_val = getattr(old_value, "miniJava_Clazz", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Clazz", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Clazz"):
                opp_val = getattr(value, "miniJava_Clazz", None)
                setattr(value, "miniJava_Clazz", self)

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
            if hasattr(old_value, "miniJava_TypeDeclaration8"):
                opp_val = getattr(old_value, "miniJava_TypeDeclaration8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_TypeDeclaration8"):
                opp_val = getattr(value, "miniJava_TypeDeclaration8", None)
                if opp_val is None:
                    setattr(value, "miniJava_TypeDeclaration8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class miniJava_Interface(TypeDeclaration):

    pass
class NamedElement:

    pass
class miniJava_TypedDeclaration(NamedElement):

    pass
class miniJava_ClazzToMethodMap:

    pass
class miniJava_Block(Statement):

    pass
class miniJava_TypeDeclaration(NamedElement):

    def __init__(self, accessLevel: str, miniJava_TypeDeclaration: "miniJava_Program" = None, miniJava_TypeDeclaration6: set["miniJava_Interface"] = None, miniJava_TypeDeclaration8: set["miniJava_Member"] = None, miniJava_TypeDeclaration47: "miniJava_ClassRef" = None):
        self.accessLevel = accessLevel
        self.miniJava_TypeDeclaration = miniJava_TypeDeclaration
        self.miniJava_TypeDeclaration6 = miniJava_TypeDeclaration6 if miniJava_TypeDeclaration6 is not None else set()
        self.miniJava_TypeDeclaration8 = miniJava_TypeDeclaration8 if miniJava_TypeDeclaration8 is not None else set()
        self.miniJava_TypeDeclaration47 = miniJava_TypeDeclaration47
        
    @property
    def accessLevel(self) -> str:
        return self.__accessLevel

    @accessLevel.setter
    def accessLevel(self, accessLevel: str):
        self.__accessLevel = accessLevel

    @property
    def miniJava_TypeDeclaration47(self):
        return self.__miniJava_TypeDeclaration47

    @miniJava_TypeDeclaration47.setter
    def miniJava_TypeDeclaration47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_TypeDeclaration__miniJava_TypeDeclaration47", None)
        self.__miniJava_TypeDeclaration47 = value
        
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
    def miniJava_TypeDeclaration8(self):
        return self.__miniJava_TypeDeclaration8

    @miniJava_TypeDeclaration8.setter
    def miniJava_TypeDeclaration8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_TypeDeclaration__miniJava_TypeDeclaration8", None)
        self.__miniJava_TypeDeclaration8 = value if value is not None else set()
        
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

    def __init__(self, name: str, miniJava_Program2: set["miniJava_TypeDeclaration"] = None, miniJava_Program4: "miniJava_State" = None, miniJava_Program: set["miniJava_Import"] = None):
        self.name = name
        self.miniJava_Program2 = miniJava_Program2 if miniJava_Program2 is not None else set()
        self.miniJava_Program4 = miniJava_Program4
        self.miniJava_Program = miniJava_Program if miniJava_Program is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
                    

    @property
    def miniJava_Program4(self):
        return self.__miniJava_Program4

    @miniJava_Program4.setter
    def miniJava_Program4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Program__miniJava_Program4", None)
        self.__miniJava_Program4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_State"):
                opp_val = getattr(old_value, "miniJava_State", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_State"):
                opp_val = getattr(value, "miniJava_State", None)
                setattr(value, "miniJava_State", self)

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
                    

class miniJava_State:

    pass