from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Type:

    pass
class jkind_ArrayType(Type):

    def __init__(self, size: str, jkind_ArrayType: "jkind_Type" = None):
        self.size = size
        self.jkind_ArrayType = jkind_ArrayType
        
    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def jkind_ArrayType(self):
        return self.__jkind_ArrayType

    @jkind_ArrayType.setter
    def jkind_ArrayType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jkind_ArrayType__jkind_ArrayType", None)
        self.__jkind_ArrayType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jkind_Type64"):
                opp_val = getattr(old_value, "jkind_Type64", None)
                if opp_val == self:
                    setattr(old_value, "jkind_Type64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jkind_Type64"):
                opp_val = getattr(value, "jkind_Type64", None)
                setattr(value, "jkind_Type64", self)

class TypeDef:

    pass
class jkind_EnumType(TypeDef):

    pass
class jkind_RecordType(TypeDef):

    pass
class jkind_AbbreviationType(TypeDef):

    pass
class jkind_UserType(Type):

    pass
class jkind_SubrangeType(Type):

    def __init__(self, low: str, high: str):
        self.low = low
        self.high = high
        
    @property
    def low(self) -> str:
        return self.__low

    @low.setter
    def low(self, low: str):
        self.__low = low

    @property
    def high(self) -> str:
        return self.__high

    @high.setter
    def high(self, high: str):
        self.__high = high

class jkind_RealType(Type):

    pass
class jkind_BoolType(Type):

    pass
class jkind_IntType(Type):

    pass
class jkind_RealizabilityInputs:

    pass
class jkind_Ivc:

    pass
class jkind_Property:

    pass
class jkind_Assertion:

    pass
class jkind_IdRef:

    def __init__(self, name: str, jkind_IdRef: "jkind_IdExpr" = None):
        self.name = name
        self.jkind_IdRef = jkind_IdRef
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def jkind_IdRef(self):
        return self.__jkind_IdRef

    @jkind_IdRef.setter
    def jkind_IdRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jkind_IdRef__jkind_IdRef", None)
        self.__jkind_IdRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jkind_IdExpr"):
                opp_val = getattr(old_value, "jkind_IdExpr", None)
                if opp_val == self:
                    setattr(old_value, "jkind_IdExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jkind_IdExpr"):
                opp_val = getattr(value, "jkind_IdExpr", None)
                setattr(value, "jkind_IdExpr", self)

class jkind_Callable:

    def __init__(self, name: str, jkind_Callable: "jkind_CallExpr" = None, jkind_Callable51: set["jkind_VariableGroup"] = None, jkind_Callable54: set["jkind_VariableGroup"] = None):
        self.name = name
        self.jkind_Callable = jkind_Callable
        self.jkind_Callable51 = jkind_Callable51 if jkind_Callable51 is not None else set()
        self.jkind_Callable54 = jkind_Callable54 if jkind_Callable54 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def jkind_Callable54(self):
        return self.__jkind_Callable54

    @jkind_Callable54.setter
    def jkind_Callable54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jkind_Callable__jkind_Callable54", None)
        self.__jkind_Callable54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jkind_VariableGroup55"):
                    opp_val = getattr(item, "jkind_VariableGroup55", None)
                    
                    if opp_val == self:
                        setattr(item, "jkind_VariableGroup55", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jkind_VariableGroup55"):
                    opp_val = getattr(item, "jkind_VariableGroup55", None)
                    
                    setattr(item, "jkind_VariableGroup55", self)
                    

    @property
    def jkind_Callable51(self):
        return self.__jkind_Callable51

    @jkind_Callable51.setter
    def jkind_Callable51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jkind_Callable__jkind_Callable51", None)
        self.__jkind_Callable51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jkind_VariableGroup52"):
                    opp_val = getattr(item, "jkind_VariableGroup52", None)
                    
                    if opp_val == self:
                        setattr(item, "jkind_VariableGroup52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jkind_VariableGroup52"):
                    opp_val = getattr(item, "jkind_VariableGroup52", None)
                    
                    setattr(item, "jkind_VariableGroup52", self)
                    

    @property
    def jkind_Callable(self):
        return self.__jkind_Callable

    @jkind_Callable.setter
    def jkind_Callable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jkind_Callable__jkind_Callable", None)
        self.__jkind_Callable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jkind_CallExpr"):
                opp_val = getattr(old_value, "jkind_CallExpr", None)
                if opp_val == self:
                    setattr(old_value, "jkind_CallExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jkind_CallExpr"):
                opp_val = getattr(value, "jkind_CallExpr", None)
                setattr(value, "jkind_CallExpr", self)

class Expr:

    pass
class jkind_BoolExpr(Expr):

    def __init__(self, val: str):
        self.val = val
        
    @property
    def val(self) -> str:
        return self.__val

    @val.setter
    def val(self, val: str):
        self.__val = val

class jkind_CondactExpr(Expr):

    pass
class jkind_RecordExpr(Expr):

    pass
class jkind_ArrayExpr(Expr):

    pass
class jkind_BinaryExpr(Expr):

    def __init__(self, op: str, jkind_BinaryExpr: "jkind_Expr" = None, jkind_BinaryExpr70: "jkind_Expr" = None):
        self.op = op
        self.jkind_BinaryExpr = jkind_BinaryExpr
        self.jkind_BinaryExpr70 = jkind_BinaryExpr70
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def jkind_BinaryExpr70(self):
        return self.__jkind_BinaryExpr70

    @jkind_BinaryExpr70.setter
    def jkind_BinaryExpr70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jkind_BinaryExpr__jkind_BinaryExpr70", None)
        self.__jkind_BinaryExpr70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jkind_Expr71"):
                opp_val = getattr(old_value, "jkind_Expr71", None)
                if opp_val == self:
                    setattr(old_value, "jkind_Expr71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jkind_Expr71"):
                opp_val = getattr(value, "jkind_Expr71", None)
                setattr(value, "jkind_Expr71", self)

    @property
    def jkind_BinaryExpr(self):
        return self.__jkind_BinaryExpr

    @jkind_BinaryExpr.setter
    def jkind_BinaryExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jkind_BinaryExpr__jkind_BinaryExpr", None)
        self.__jkind_BinaryExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jkind_Expr68"):
                opp_val = getattr(old_value, "jkind_Expr68", None)
                if opp_val == self:
                    setattr(old_value, "jkind_Expr68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jkind_Expr68"):
                opp_val = getattr(value, "jkind_Expr68", None)
                setattr(value, "jkind_Expr68", self)

class jkind_RecordUpdateExpr(Expr):

    pass
class jkind_IntExpr(Expr):

    def __init__(self, val: str):
        self.val = val
        
    @property
    def val(self) -> str:
        return self.__val

    @val.setter
    def val(self, val: str):
        self.__val = val

class jkind_TupleExpr(Expr):

    pass
class jkind_RealExpr(Expr):

    def __init__(self, val: str):
        self.val = val
        
    @property
    def val(self) -> str:
        return self.__val

    @val.setter
    def val(self, val: str):
        self.__val = val

class jkind_IdExpr(Expr):

    pass
class jkind_ArrayUpdateExpr(Expr):

    pass
class jkind_UnaryExpr(Expr):

    def __init__(self, op: str, jkind_UnaryExpr: "jkind_Expr" = None):
        self.op = op
        self.jkind_UnaryExpr = jkind_UnaryExpr
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def jkind_UnaryExpr(self):
        return self.__jkind_UnaryExpr

    @jkind_UnaryExpr.setter
    def jkind_UnaryExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jkind_UnaryExpr__jkind_UnaryExpr", None)
        self.__jkind_UnaryExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jkind_Expr73"):
                opp_val = getattr(old_value, "jkind_Expr73", None)
                if opp_val == self:
                    setattr(old_value, "jkind_Expr73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jkind_Expr73"):
                opp_val = getattr(value, "jkind_Expr73", None)
                setattr(value, "jkind_Expr73", self)

class jkind_RecordAccessExpr(Expr):

    pass
class jkind_ArrayAccessExpr(Expr):

    pass
class jkind_CastExpr(Expr):

    def __init__(self, op: str, jkind_CastExpr: "jkind_Expr" = None):
        self.op = op
        self.jkind_CastExpr = jkind_CastExpr
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def jkind_CastExpr(self):
        return self.__jkind_CastExpr

    @jkind_CastExpr.setter
    def jkind_CastExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jkind_CastExpr__jkind_CastExpr", None)
        self.__jkind_CastExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jkind_Expr107"):
                opp_val = getattr(old_value, "jkind_Expr107", None)
                if opp_val == self:
                    setattr(old_value, "jkind_Expr107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jkind_Expr107"):
                opp_val = getattr(value, "jkind_Expr107", None)
                setattr(value, "jkind_Expr107", self)

class jkind_IfThenElseExpr(Expr):

    pass
class jkind_CallExpr(Expr):

    pass
class jkind_File:

    pass
class jkind_Equation:

    pass
class jkind_VariableGroup:

    pass
class Callable:

    pass
class jkind_Expr:

    pass
class jkind_Field:

    def __init__(self, name: str, jkind_Field78: "jkind_RecordAccessExpr" = None, jkind_Field83: "jkind_RecordUpdateExpr" = None, jkind_Field: "jkind_RecordType" = None, jkind_Field122: "jkind_RecordExpr" = None):
        self.name = name
        self.jkind_Field78 = jkind_Field78
        self.jkind_Field83 = jkind_Field83
        self.jkind_Field = jkind_Field
        self.jkind_Field122 = jkind_Field122
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def jkind_Field(self):
        return self.__jkind_Field

    @jkind_Field.setter
    def jkind_Field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jkind_Field__jkind_Field", None)
        self.__jkind_Field = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jkind_RecordType"):
                opp_val = getattr(old_value, "jkind_RecordType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jkind_RecordType"):
                opp_val = getattr(value, "jkind_RecordType", None)
                if opp_val is None:
                    setattr(value, "jkind_RecordType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jkind_Field78(self):
        return self.__jkind_Field78

    @jkind_Field78.setter
    def jkind_Field78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jkind_Field__jkind_Field78", None)
        self.__jkind_Field78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jkind_RecordAccessExpr77"):
                opp_val = getattr(old_value, "jkind_RecordAccessExpr77", None)
                if opp_val == self:
                    setattr(old_value, "jkind_RecordAccessExpr77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jkind_RecordAccessExpr77"):
                opp_val = getattr(value, "jkind_RecordAccessExpr77", None)
                setattr(value, "jkind_RecordAccessExpr77", self)

    @property
    def jkind_Field122(self):
        return self.__jkind_Field122

    @jkind_Field122.setter
    def jkind_Field122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jkind_Field__jkind_Field122", None)
        self.__jkind_Field122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jkind_RecordExpr121"):
                opp_val = getattr(old_value, "jkind_RecordExpr121", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jkind_RecordExpr121"):
                opp_val = getattr(value, "jkind_RecordExpr121", None)
                if opp_val is None:
                    setattr(value, "jkind_RecordExpr121", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jkind_Field83(self):
        return self.__jkind_Field83

    @jkind_Field83.setter
    def jkind_Field83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jkind_Field__jkind_Field83", None)
        self.__jkind_Field83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jkind_RecordUpdateExpr82"):
                opp_val = getattr(old_value, "jkind_RecordUpdateExpr82", None)
                if opp_val == self:
                    setattr(old_value, "jkind_RecordUpdateExpr82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jkind_RecordUpdateExpr82"):
                opp_val = getattr(value, "jkind_RecordUpdateExpr82", None)
                setattr(value, "jkind_RecordUpdateExpr82", self)

class jkind_Type:

    pass
class IdRef:

    pass
class jkind_Variable(IdRef):

    pass
class jkind_EnumValue(IdRef):

    pass
class jkind_Node(Callable):

    def __init__(self, main: str, jkind_Node: "jkind_File" = None, jkind_Node12: set["jkind_VariableGroup"] = None, jkind_Node14: set["jkind_Equation"] = None, jkind_Node16: set["jkind_Assertion"] = None, jkind_Node18: set["jkind_Property"] = None, jkind_Node20: set["jkind_Ivc"] = None, jkind_Node22: set["jkind_RealizabilityInputs"] = None):
        self.main = main
        self.jkind_Node = jkind_Node
        self.jkind_Node12 = jkind_Node12 if jkind_Node12 is not None else set()
        self.jkind_Node14 = jkind_Node14 if jkind_Node14 is not None else set()
        self.jkind_Node16 = jkind_Node16 if jkind_Node16 is not None else set()
        self.jkind_Node18 = jkind_Node18 if jkind_Node18 is not None else set()
        self.jkind_Node20 = jkind_Node20 if jkind_Node20 is not None else set()
        self.jkind_Node22 = jkind_Node22 if jkind_Node22 is not None else set()
        
    @property
    def main(self) -> str:
        return self.__main

    @main.setter
    def main(self, main: str):
        self.__main = main

    @property
    def jkind_Node22(self):
        return self.__jkind_Node22

    @jkind_Node22.setter
    def jkind_Node22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jkind_Node__jkind_Node22", None)
        self.__jkind_Node22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jkind_RealizabilityInputs"):
                    opp_val = getattr(item, "jkind_RealizabilityInputs", None)
                    
                    if opp_val == self:
                        setattr(item, "jkind_RealizabilityInputs", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jkind_RealizabilityInputs"):
                    opp_val = getattr(item, "jkind_RealizabilityInputs", None)
                    
                    setattr(item, "jkind_RealizabilityInputs", self)
                    

    @property
    def jkind_Node16(self):
        return self.__jkind_Node16

    @jkind_Node16.setter
    def jkind_Node16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jkind_Node__jkind_Node16", None)
        self.__jkind_Node16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jkind_Assertion"):
                    opp_val = getattr(item, "jkind_Assertion", None)
                    
                    if opp_val == self:
                        setattr(item, "jkind_Assertion", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jkind_Assertion"):
                    opp_val = getattr(item, "jkind_Assertion", None)
                    
                    setattr(item, "jkind_Assertion", self)
                    

    @property
    def jkind_Node12(self):
        return self.__jkind_Node12

    @jkind_Node12.setter
    def jkind_Node12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jkind_Node__jkind_Node12", None)
        self.__jkind_Node12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jkind_VariableGroup"):
                    opp_val = getattr(item, "jkind_VariableGroup", None)
                    
                    if opp_val == self:
                        setattr(item, "jkind_VariableGroup", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jkind_VariableGroup"):
                    opp_val = getattr(item, "jkind_VariableGroup", None)
                    
                    setattr(item, "jkind_VariableGroup", self)
                    

    @property
    def jkind_Node(self):
        return self.__jkind_Node

    @jkind_Node.setter
    def jkind_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jkind_Node__jkind_Node", None)
        self.__jkind_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jkind_File6"):
                opp_val = getattr(old_value, "jkind_File6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jkind_File6"):
                opp_val = getattr(value, "jkind_File6", None)
                if opp_val is None:
                    setattr(value, "jkind_File6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jkind_Node20(self):
        return self.__jkind_Node20

    @jkind_Node20.setter
    def jkind_Node20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jkind_Node__jkind_Node20", None)
        self.__jkind_Node20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jkind_Ivc"):
                    opp_val = getattr(item, "jkind_Ivc", None)
                    
                    if opp_val == self:
                        setattr(item, "jkind_Ivc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jkind_Ivc"):
                    opp_val = getattr(item, "jkind_Ivc", None)
                    
                    setattr(item, "jkind_Ivc", self)
                    

    @property
    def jkind_Node18(self):
        return self.__jkind_Node18

    @jkind_Node18.setter
    def jkind_Node18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jkind_Node__jkind_Node18", None)
        self.__jkind_Node18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jkind_Property"):
                    opp_val = getattr(item, "jkind_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "jkind_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jkind_Property"):
                    opp_val = getattr(item, "jkind_Property", None)
                    
                    setattr(item, "jkind_Property", self)
                    

    @property
    def jkind_Node14(self):
        return self.__jkind_Node14

    @jkind_Node14.setter
    def jkind_Node14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jkind_Node__jkind_Node14", None)
        self.__jkind_Node14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jkind_Equation"):
                    opp_val = getattr(item, "jkind_Equation", None)
                    
                    if opp_val == self:
                        setattr(item, "jkind_Equation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jkind_Equation"):
                    opp_val = getattr(item, "jkind_Equation", None)
                    
                    setattr(item, "jkind_Equation", self)
                    

class jkind_Function(Callable):

    pass
class jkind_Constant(IdRef):

    pass
class jkind_TypeDef:

    def __init__(self, name: str, jkind_TypeDef: "jkind_File" = None, jkind_TypeDef66: "jkind_UserType" = None):
        self.name = name
        self.jkind_TypeDef = jkind_TypeDef
        self.jkind_TypeDef66 = jkind_TypeDef66
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def jkind_TypeDef66(self):
        return self.__jkind_TypeDef66

    @jkind_TypeDef66.setter
    def jkind_TypeDef66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jkind_TypeDef__jkind_TypeDef66", None)
        self.__jkind_TypeDef66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jkind_UserType"):
                opp_val = getattr(old_value, "jkind_UserType", None)
                if opp_val == self:
                    setattr(old_value, "jkind_UserType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jkind_UserType"):
                opp_val = getattr(value, "jkind_UserType", None)
                setattr(value, "jkind_UserType", self)

    @property
    def jkind_TypeDef(self):
        return self.__jkind_TypeDef

    @jkind_TypeDef.setter
    def jkind_TypeDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jkind_TypeDef__jkind_TypeDef", None)
        self.__jkind_TypeDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jkind_File"):
                opp_val = getattr(old_value, "jkind_File", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jkind_File"):
                opp_val = getattr(value, "jkind_File", None)
                if opp_val is None:
                    setattr(value, "jkind_File", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
