from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Expression:

    pass
class tym_Comparison(Expression):

    def __init__(self, op: str, tym_Comparison: "tym_Expression" = None, tym_Comparison53: "tym_Expression" = None):
        self.op = op
        self.tym_Comparison = tym_Comparison
        self.tym_Comparison53 = tym_Comparison53
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def tym_Comparison(self):
        return self.__tym_Comparison

    @tym_Comparison.setter
    def tym_Comparison(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tym_Comparison__tym_Comparison", None)
        self.__tym_Comparison = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tym_Expression51"):
                opp_val = getattr(old_value, "tym_Expression51", None)
                if opp_val == self:
                    setattr(old_value, "tym_Expression51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tym_Expression51"):
                opp_val = getattr(value, "tym_Expression51", None)
                setattr(value, "tym_Expression51", self)

    @property
    def tym_Comparison53(self):
        return self.__tym_Comparison53

    @tym_Comparison53.setter
    def tym_Comparison53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tym_Comparison__tym_Comparison53", None)
        self.__tym_Comparison53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tym_Expression54"):
                opp_val = getattr(old_value, "tym_Expression54", None)
                if opp_val == self:
                    setattr(old_value, "tym_Expression54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tym_Expression54"):
                opp_val = getattr(value, "tym_Expression54", None)
                setattr(value, "tym_Expression54", self)

class tym_And(Expression):

    pass
class tym_IntConstant(Expression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class tym_StringConstant(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class tym_Minus(Expression):

    pass
class tym_BoolConstant(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class tym_Plus(Expression):

    pass
class tym_MulOrDiv(Expression):

    def __init__(self, op: str, tym_MulOrDiv68: "tym_Expression" = None, tym_MulOrDiv: "tym_Expression" = None):
        self.op = op
        self.tym_MulOrDiv68 = tym_MulOrDiv68
        self.tym_MulOrDiv = tym_MulOrDiv
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def tym_MulOrDiv68(self):
        return self.__tym_MulOrDiv68

    @tym_MulOrDiv68.setter
    def tym_MulOrDiv68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tym_MulOrDiv__tym_MulOrDiv68", None)
        self.__tym_MulOrDiv68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tym_Expression69"):
                opp_val = getattr(old_value, "tym_Expression69", None)
                if opp_val == self:
                    setattr(old_value, "tym_Expression69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tym_Expression69"):
                opp_val = getattr(value, "tym_Expression69", None)
                setattr(value, "tym_Expression69", self)

    @property
    def tym_MulOrDiv(self):
        return self.__tym_MulOrDiv

    @tym_MulOrDiv.setter
    def tym_MulOrDiv(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tym_MulOrDiv__tym_MulOrDiv", None)
        self.__tym_MulOrDiv = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tym_Expression66"):
                opp_val = getattr(old_value, "tym_Expression66", None)
                if opp_val == self:
                    setattr(old_value, "tym_Expression66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tym_Expression66"):
                opp_val = getattr(value, "tym_Expression66", None)
                setattr(value, "tym_Expression66", self)

class tym_Not(Expression):

    pass
class tym_VariableRef(Expression):

    pass
class tym_Or(Expression):

    pass
class tym_Expression:

    pass
class tym_Equality(Expression):

    def __init__(self, op: str, tym_Equality: "tym_Expression" = None, tym_Equality48: "tym_Expression" = None):
        self.op = op
        self.tym_Equality = tym_Equality
        self.tym_Equality48 = tym_Equality48
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def tym_Equality(self):
        return self.__tym_Equality

    @tym_Equality.setter
    def tym_Equality(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tym_Equality__tym_Equality", None)
        self.__tym_Equality = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tym_Expression46"):
                opp_val = getattr(old_value, "tym_Expression46", None)
                if opp_val == self:
                    setattr(old_value, "tym_Expression46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tym_Expression46"):
                opp_val = getattr(value, "tym_Expression46", None)
                setattr(value, "tym_Expression46", self)

    @property
    def tym_Equality48(self):
        return self.__tym_Equality48

    @tym_Equality48.setter
    def tym_Equality48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tym_Equality__tym_Equality48", None)
        self.__tym_Equality48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tym_Expression49"):
                opp_val = getattr(old_value, "tym_Expression49", None)
                if opp_val == self:
                    setattr(old_value, "tym_Expression49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tym_Expression49"):
                opp_val = getattr(value, "tym_Expression49", None)
                setattr(value, "tym_Expression49", self)

class tym_Block:

    pass
class tym_FunctionBlock:

    pass
class tym_Function:

    def __init__(self, return: str, name: str, tym_Function: set["tym_Variable"] = None, tym_Function9: "tym_FunctionBlock" = None, tym_Function32: "tym_FunctionCall" = None):
        self.return = return
        self.name = name
        self.tym_Function = tym_Function if tym_Function is not None else set()
        self.tym_Function9 = tym_Function9
        self.tym_Function32 = tym_Function32
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def return(self) -> str:
        return self.__return

    @return.setter
    def return(self, return: str):
        self.__return = return

    @property
    def tym_Function9(self):
        return self.__tym_Function9

    @tym_Function9.setter
    def tym_Function9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tym_Function__tym_Function9", None)
        self.__tym_Function9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tym_FunctionBlock"):
                opp_val = getattr(old_value, "tym_FunctionBlock", None)
                if opp_val == self:
                    setattr(old_value, "tym_FunctionBlock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tym_FunctionBlock"):
                opp_val = getattr(value, "tym_FunctionBlock", None)
                setattr(value, "tym_FunctionBlock", self)

    @property
    def tym_Function32(self):
        return self.__tym_Function32

    @tym_Function32.setter
    def tym_Function32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tym_Function__tym_Function32", None)
        self.__tym_Function32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tym_FunctionCall"):
                opp_val = getattr(old_value, "tym_FunctionCall", None)
                if opp_val == self:
                    setattr(old_value, "tym_FunctionCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tym_FunctionCall"):
                opp_val = getattr(value, "tym_FunctionCall", None)
                setattr(value, "tym_FunctionCall", self)

    @property
    def tym_Function(self):
        return self.__tym_Function

    @tym_Function.setter
    def tym_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tym_Function__tym_Function", None)
        self.__tym_Function = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tym_Variable7"):
                    opp_val = getattr(item, "tym_Variable7", None)
                    
                    if opp_val == self:
                        setattr(item, "tym_Variable7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tym_Variable7"):
                    opp_val = getattr(item, "tym_Variable7", None)
                    
                    setattr(item, "tym_Variable7", self)
                    

class AbstractElement:

    pass
class tym_PrintStatement(AbstractElement):

    pass
class tym_FunctionCall(AbstractElement):

    pass
class tym_TestStatement(AbstractElement):

    pass
class tym_LoopStatement(AbstractElement):

    pass
class tym_Return(AbstractElement):

    pass
class tym_Variable(AbstractElement):

    def __init__(self, vartype: str, name: str, tym_Variable: "tym_Variable" = None, tym_Variable1: "tym_Variable" = None, tym_Variable4: "tym_EObject" = None, tym_Variable7: "tym_Function" = None, tym_Variable73: "tym_VariableRef" = None):
        self.vartype = vartype
        self.name = name
        self.tym_Variable = tym_Variable
        self.tym_Variable1 = tym_Variable1
        self.tym_Variable4 = tym_Variable4
        self.tym_Variable7 = tym_Variable7
        self.tym_Variable73 = tym_Variable73
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def vartype(self) -> str:
        return self.__vartype

    @vartype.setter
    def vartype(self, vartype: str):
        self.__vartype = vartype

    @property
    def tym_Variable4(self):
        return self.__tym_Variable4

    @tym_Variable4.setter
    def tym_Variable4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tym_Variable__tym_Variable4", None)
        self.__tym_Variable4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tym_EObject5"):
                opp_val = getattr(old_value, "tym_EObject5", None)
                if opp_val == self:
                    setattr(old_value, "tym_EObject5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tym_EObject5"):
                opp_val = getattr(value, "tym_EObject5", None)
                setattr(value, "tym_EObject5", self)

    @property
    def tym_Variable1(self):
        return self.__tym_Variable1

    @tym_Variable1.setter
    def tym_Variable1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tym_Variable__tym_Variable1", None)
        self.__tym_Variable1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tym_Variable"):
                opp_val = getattr(old_value, "tym_Variable", None)
                if opp_val == self:
                    setattr(old_value, "tym_Variable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tym_Variable"):
                opp_val = getattr(value, "tym_Variable", None)
                setattr(value, "tym_Variable", self)

    @property
    def tym_Variable73(self):
        return self.__tym_Variable73

    @tym_Variable73.setter
    def tym_Variable73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tym_Variable__tym_Variable73", None)
        self.__tym_Variable73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tym_VariableRef"):
                opp_val = getattr(old_value, "tym_VariableRef", None)
                if opp_val == self:
                    setattr(old_value, "tym_VariableRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tym_VariableRef"):
                opp_val = getattr(value, "tym_VariableRef", None)
                setattr(value, "tym_VariableRef", self)

    @property
    def tym_Variable7(self):
        return self.__tym_Variable7

    @tym_Variable7.setter
    def tym_Variable7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tym_Variable__tym_Variable7", None)
        self.__tym_Variable7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tym_Function"):
                opp_val = getattr(old_value, "tym_Function", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tym_Function"):
                opp_val = getattr(value, "tym_Function", None)
                if opp_val is None:
                    setattr(value, "tym_Function", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tym_Variable(self):
        return self.__tym_Variable

    @tym_Variable.setter
    def tym_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tym_Variable__tym_Variable", None)
        self.__tym_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tym_Variable1"):
                opp_val = getattr(old_value, "tym_Variable1", None)
                if opp_val == self:
                    setattr(old_value, "tym_Variable1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tym_Variable1"):
                opp_val = getattr(value, "tym_Variable1", None)
                setattr(value, "tym_Variable1", self)

class tym_AbstractElement:

    pass
class tym_EObject:

    pass
class tym_Model:

    pass