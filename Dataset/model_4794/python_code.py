from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Expr:

    pass
class jkind_RecordExpr(Expr):

    pass
class jkind_NodeCallExpr(Expr):

    pass
class jkind_BinaryExpr(Expr):

    def __init__(self, op: str, jkind_BinaryExpr51: "jkind_Expr" = None, jkind_BinaryExpr: "jkind_Expr" = None):
        self.op = op
        self.jkind_BinaryExpr51 = jkind_BinaryExpr51
        self.jkind_BinaryExpr = jkind_BinaryExpr
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def jkind_BinaryExpr51(self):
        return self.__jkind_BinaryExpr51

    @jkind_BinaryExpr51.setter
    def jkind_BinaryExpr51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jkind_BinaryExpr__jkind_BinaryExpr51", None)
        self.__jkind_BinaryExpr51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jkind_Expr52"):
                opp_val = getattr(old_value, "jkind_Expr52", None)
                if opp_val == self:
                    setattr(old_value, "jkind_Expr52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jkind_Expr52"):
                opp_val = getattr(value, "jkind_Expr52", None)
                setattr(value, "jkind_Expr52", self)

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
            if hasattr(old_value, "jkind_Expr49"):
                opp_val = getattr(old_value, "jkind_Expr49", None)
                if opp_val == self:
                    setattr(old_value, "jkind_Expr49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jkind_Expr49"):
                opp_val = getattr(value, "jkind_Expr49", None)
                setattr(value, "jkind_Expr49", self)

class Type:

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

class jkind_BoolType(Type):

    pass
class jkind_RealType(Type):

    pass
class jkind_UserType(Type):

    pass
class jkind_IntType(Type):

    pass
class jkind_IfThenElseExpr(Expr):

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

class jkind_RealExpr(Expr):

    def __init__(self, val: str):
        self.val = val
        
    @property
    def val(self) -> str:
        return self.__val

    @val.setter
    def val(self, val: str):
        self.__val = val

class jkind_IntExpr(Expr):

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
class jkind_ProjectionExpr(Expr):

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
            if hasattr(old_value, "jkind_Expr54"):
                opp_val = getattr(old_value, "jkind_Expr54", None)
                if opp_val == self:
                    setattr(old_value, "jkind_Expr54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jkind_Expr54"):
                opp_val = getattr(value, "jkind_Expr54", None)
                setattr(value, "jkind_Expr54", self)

class jkind_Assertion:

    pass
class jkind_Equation:

    pass
class jkind_VariableGroup:

    pass
class Typedef:

    pass
class jkind_RecordType(Typedef):

    pass
class jkind_AbbreviationType(Typedef):

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

class jkind_Property:

    pass
class jkind_Expr:

    pass
class IdRef:

    pass
class jkind_Variable(IdRef):

    pass
class jkind_Field:

    def __init__(self, name: str, jkind_Field: "jkind_RecordType" = None, jkind_Field59: "jkind_ProjectionExpr" = None, jkind_Field78: "jkind_RecordExpr" = None):
        self.name = name
        self.jkind_Field = jkind_Field
        self.jkind_Field59 = jkind_Field59
        self.jkind_Field78 = jkind_Field78
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "jkind_RecordExpr77"):
                opp_val = getattr(old_value, "jkind_RecordExpr77", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jkind_RecordExpr77"):
                opp_val = getattr(value, "jkind_RecordExpr77", None)
                if opp_val is None:
                    setattr(value, "jkind_RecordExpr77", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jkind_Field59(self):
        return self.__jkind_Field59

    @jkind_Field59.setter
    def jkind_Field59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jkind_Field__jkind_Field59", None)
        self.__jkind_Field59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jkind_ProjectionExpr58"):
                opp_val = getattr(old_value, "jkind_ProjectionExpr58", None)
                if opp_val == self:
                    setattr(old_value, "jkind_ProjectionExpr58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jkind_ProjectionExpr58"):
                opp_val = getattr(value, "jkind_ProjectionExpr58", None)
                setattr(value, "jkind_ProjectionExpr58", self)

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

class jkind_Type:

    pass
class jkind_Node:

    def __init__(self, name: str, main: str, jkind_Node: "jkind_File" = None, jkind_Node22: set["jkind_Property"] = None, jkind_Node10: set["jkind_VariableGroup"] = None, jkind_Node12: set["jkind_VariableGroup"] = None, jkind_Node15: set["jkind_VariableGroup"] = None, jkind_Node18: set["jkind_Equation"] = None, jkind_Node20: set["jkind_Assertion"] = None, jkind_Node70: "jkind_NodeCallExpr" = None):
        self.name = name
        self.main = main
        self.jkind_Node = jkind_Node
        self.jkind_Node22 = jkind_Node22 if jkind_Node22 is not None else set()
        self.jkind_Node10 = jkind_Node10 if jkind_Node10 is not None else set()
        self.jkind_Node12 = jkind_Node12 if jkind_Node12 is not None else set()
        self.jkind_Node15 = jkind_Node15 if jkind_Node15 is not None else set()
        self.jkind_Node18 = jkind_Node18 if jkind_Node18 is not None else set()
        self.jkind_Node20 = jkind_Node20 if jkind_Node20 is not None else set()
        self.jkind_Node70 = jkind_Node70
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def main(self) -> str:
        return self.__main

    @main.setter
    def main(self, main: str):
        self.__main = main

    @property
    def jkind_Node70(self):
        return self.__jkind_Node70

    @jkind_Node70.setter
    def jkind_Node70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jkind_Node__jkind_Node70", None)
        self.__jkind_Node70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jkind_NodeCallExpr"):
                opp_val = getattr(old_value, "jkind_NodeCallExpr", None)
                if opp_val == self:
                    setattr(old_value, "jkind_NodeCallExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jkind_NodeCallExpr"):
                opp_val = getattr(value, "jkind_NodeCallExpr", None)
                setattr(value, "jkind_NodeCallExpr", self)

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
                if hasattr(item, "jkind_VariableGroup13"):
                    opp_val = getattr(item, "jkind_VariableGroup13", None)
                    
                    if opp_val == self:
                        setattr(item, "jkind_VariableGroup13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jkind_VariableGroup13"):
                    opp_val = getattr(item, "jkind_VariableGroup13", None)
                    
                    setattr(item, "jkind_VariableGroup13", self)
                    

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
            if hasattr(old_value, "jkind_File4"):
                opp_val = getattr(old_value, "jkind_File4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jkind_File4"):
                opp_val = getattr(value, "jkind_File4", None)
                if opp_val is None:
                    setattr(value, "jkind_File4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def jkind_Node15(self):
        return self.__jkind_Node15

    @jkind_Node15.setter
    def jkind_Node15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jkind_Node__jkind_Node15", None)
        self.__jkind_Node15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jkind_VariableGroup16"):
                    opp_val = getattr(item, "jkind_VariableGroup16", None)
                    
                    if opp_val == self:
                        setattr(item, "jkind_VariableGroup16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jkind_VariableGroup16"):
                    opp_val = getattr(item, "jkind_VariableGroup16", None)
                    
                    setattr(item, "jkind_VariableGroup16", self)
                    

    @property
    def jkind_Node10(self):
        return self.__jkind_Node10

    @jkind_Node10.setter
    def jkind_Node10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jkind_Node__jkind_Node10", None)
        self.__jkind_Node10 = value if value is not None else set()
        
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
                    

class jkind_Constant(IdRef):

    pass
class jkind_Typedef:

    def __init__(self, name: str, jkind_Typedef: "jkind_File" = None, jkind_Typedef47: "jkind_UserType" = None):
        self.name = name
        self.jkind_Typedef = jkind_Typedef
        self.jkind_Typedef47 = jkind_Typedef47
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def jkind_Typedef47(self):
        return self.__jkind_Typedef47

    @jkind_Typedef47.setter
    def jkind_Typedef47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jkind_Typedef__jkind_Typedef47", None)
        self.__jkind_Typedef47 = value
        
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
    def jkind_Typedef(self):
        return self.__jkind_Typedef

    @jkind_Typedef.setter
    def jkind_Typedef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jkind_Typedef__jkind_Typedef", None)
        self.__jkind_Typedef = value
        
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

class jkind_File:

    pass