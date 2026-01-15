from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class PrimitiveType(Enum):
    Int = "Int"
    Real = "Real"
    Bool = "Bool"


############################################
# Definition of Classes
############################################

class Expression:

    pass
class nabla_Modulo(Expression):

    def __init__(self, op: str, nabla_Modulo: "nabla_Expression" = None, nabla_Modulo192: "nabla_Expression" = None):
        self.op = op
        self.nabla_Modulo = nabla_Modulo
        self.nabla_Modulo192 = nabla_Modulo192
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def nabla_Modulo192(self):
        return self.__nabla_Modulo192

    @nabla_Modulo192.setter
    def nabla_Modulo192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_Modulo__nabla_Modulo192", None)
        self.__nabla_Modulo192 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_Expression193"):
                opp_val = getattr(old_value, "nabla_Expression193", None)
                if opp_val == self:
                    setattr(old_value, "nabla_Expression193", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_Expression193"):
                opp_val = getattr(value, "nabla_Expression193", None)
                setattr(value, "nabla_Expression193", self)

    @property
    def nabla_Modulo(self):
        return self.__nabla_Modulo

    @nabla_Modulo.setter
    def nabla_Modulo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_Modulo__nabla_Modulo", None)
        self.__nabla_Modulo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_Expression190"):
                opp_val = getattr(old_value, "nabla_Expression190", None)
                if opp_val == self:
                    setattr(old_value, "nabla_Expression190", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_Expression190"):
                opp_val = getattr(value, "nabla_Expression190", None)
                setattr(value, "nabla_Expression190", self)

class nabla_And(Expression):

    def __init__(self, op: str, nabla_And: "nabla_Expression" = None, nabla_And157: "nabla_Expression" = None):
        self.op = op
        self.nabla_And = nabla_And
        self.nabla_And157 = nabla_And157
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def nabla_And(self):
        return self.__nabla_And

    @nabla_And.setter
    def nabla_And(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_And__nabla_And", None)
        self.__nabla_And = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_Expression155"):
                opp_val = getattr(old_value, "nabla_Expression155", None)
                if opp_val == self:
                    setattr(old_value, "nabla_Expression155", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_Expression155"):
                opp_val = getattr(value, "nabla_Expression155", None)
                setattr(value, "nabla_Expression155", self)

    @property
    def nabla_And157(self):
        return self.__nabla_And157

    @nabla_And157.setter
    def nabla_And157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_And__nabla_And157", None)
        self.__nabla_And157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_Expression158"):
                opp_val = getattr(old_value, "nabla_Expression158", None)
                if opp_val == self:
                    setattr(old_value, "nabla_Expression158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_Expression158"):
                opp_val = getattr(value, "nabla_Expression158", None)
                setattr(value, "nabla_Expression158", self)

class nabla_Div(Expression):

    def __init__(self, op: str, nabla_Div: "nabla_Expression" = None, nabla_Div187: "nabla_Expression" = None):
        self.op = op
        self.nabla_Div = nabla_Div
        self.nabla_Div187 = nabla_Div187
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def nabla_Div187(self):
        return self.__nabla_Div187

    @nabla_Div187.setter
    def nabla_Div187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_Div__nabla_Div187", None)
        self.__nabla_Div187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_Expression188"):
                opp_val = getattr(old_value, "nabla_Expression188", None)
                if opp_val == self:
                    setattr(old_value, "nabla_Expression188", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_Expression188"):
                opp_val = getattr(value, "nabla_Expression188", None)
                setattr(value, "nabla_Expression188", self)

    @property
    def nabla_Div(self):
        return self.__nabla_Div

    @nabla_Div.setter
    def nabla_Div(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_Div__nabla_Div", None)
        self.__nabla_Div = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_Expression185"):
                opp_val = getattr(old_value, "nabla_Expression185", None)
                if opp_val == self:
                    setattr(old_value, "nabla_Expression185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_Expression185"):
                opp_val = getattr(value, "nabla_Expression185", None)
                setattr(value, "nabla_Expression185", self)

class nabla_Cardinality(Expression):

    pass
class nabla_MaxConstant(Expression):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class nabla_Plus(Expression):

    def __init__(self, op: str, nabla_Plus: "nabla_Expression" = None, nabla_Plus172: "nabla_Expression" = None):
        self.op = op
        self.nabla_Plus = nabla_Plus
        self.nabla_Plus172 = nabla_Plus172
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def nabla_Plus(self):
        return self.__nabla_Plus

    @nabla_Plus.setter
    def nabla_Plus(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_Plus__nabla_Plus", None)
        self.__nabla_Plus = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_Expression170"):
                opp_val = getattr(old_value, "nabla_Expression170", None)
                if opp_val == self:
                    setattr(old_value, "nabla_Expression170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_Expression170"):
                opp_val = getattr(value, "nabla_Expression170", None)
                setattr(value, "nabla_Expression170", self)

    @property
    def nabla_Plus172(self):
        return self.__nabla_Plus172

    @nabla_Plus172.setter
    def nabla_Plus172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_Plus__nabla_Plus172", None)
        self.__nabla_Plus172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_Expression173"):
                opp_val = getattr(old_value, "nabla_Expression173", None)
                if opp_val == self:
                    setattr(old_value, "nabla_Expression173", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_Expression173"):
                opp_val = getattr(value, "nabla_Expression173", None)
                setattr(value, "nabla_Expression173", self)

class nabla_Or(Expression):

    def __init__(self, op: str, nabla_Or152: "nabla_Expression" = None, nabla_Or: "nabla_Expression" = None):
        self.op = op
        self.nabla_Or152 = nabla_Or152
        self.nabla_Or = nabla_Or
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def nabla_Or(self):
        return self.__nabla_Or

    @nabla_Or.setter
    def nabla_Or(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_Or__nabla_Or", None)
        self.__nabla_Or = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_Expression150"):
                opp_val = getattr(old_value, "nabla_Expression150", None)
                if opp_val == self:
                    setattr(old_value, "nabla_Expression150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_Expression150"):
                opp_val = getattr(value, "nabla_Expression150", None)
                setattr(value, "nabla_Expression150", self)

    @property
    def nabla_Or152(self):
        return self.__nabla_Or152

    @nabla_Or152.setter
    def nabla_Or152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_Or__nabla_Or152", None)
        self.__nabla_Or152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_Expression153"):
                opp_val = getattr(old_value, "nabla_Expression153", None)
                if opp_val == self:
                    setattr(old_value, "nabla_Expression153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_Expression153"):
                opp_val = getattr(value, "nabla_Expression153", None)
                setattr(value, "nabla_Expression153", self)

class nabla_Not(Expression):

    pass
class nabla_Equality(Expression):

    def __init__(self, op: str, nabla_Equality162: "nabla_Expression" = None, nabla_Equality: "nabla_Expression" = None):
        self.op = op
        self.nabla_Equality162 = nabla_Equality162
        self.nabla_Equality = nabla_Equality
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def nabla_Equality(self):
        return self.__nabla_Equality

    @nabla_Equality.setter
    def nabla_Equality(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_Equality__nabla_Equality", None)
        self.__nabla_Equality = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_Expression160"):
                opp_val = getattr(old_value, "nabla_Expression160", None)
                if opp_val == self:
                    setattr(old_value, "nabla_Expression160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_Expression160"):
                opp_val = getattr(value, "nabla_Expression160", None)
                setattr(value, "nabla_Expression160", self)

    @property
    def nabla_Equality162(self):
        return self.__nabla_Equality162

    @nabla_Equality162.setter
    def nabla_Equality162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_Equality__nabla_Equality162", None)
        self.__nabla_Equality162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_Expression163"):
                opp_val = getattr(old_value, "nabla_Expression163", None)
                if opp_val == self:
                    setattr(old_value, "nabla_Expression163", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_Expression163"):
                opp_val = getattr(value, "nabla_Expression163", None)
                setattr(value, "nabla_Expression163", self)

class nabla_FunctionCall(Expression):

    pass
class nabla_BoolConstant(Expression):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class nabla_MinConstant(Expression):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class nabla_RealConstant(Expression):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class nabla_ContractedIf(Expression):

    pass
class nabla_Mul(Expression):

    def __init__(self, op: str, nabla_Mul: "nabla_Expression" = None, nabla_Mul182: "nabla_Expression" = None):
        self.op = op
        self.nabla_Mul = nabla_Mul
        self.nabla_Mul182 = nabla_Mul182
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def nabla_Mul(self):
        return self.__nabla_Mul

    @nabla_Mul.setter
    def nabla_Mul(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_Mul__nabla_Mul", None)
        self.__nabla_Mul = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_Expression180"):
                opp_val = getattr(old_value, "nabla_Expression180", None)
                if opp_val == self:
                    setattr(old_value, "nabla_Expression180", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_Expression180"):
                opp_val = getattr(value, "nabla_Expression180", None)
                setattr(value, "nabla_Expression180", self)

    @property
    def nabla_Mul182(self):
        return self.__nabla_Mul182

    @nabla_Mul182.setter
    def nabla_Mul182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_Mul__nabla_Mul182", None)
        self.__nabla_Mul182 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_Expression183"):
                opp_val = getattr(old_value, "nabla_Expression183", None)
                if opp_val == self:
                    setattr(old_value, "nabla_Expression183", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_Expression183"):
                opp_val = getattr(value, "nabla_Expression183", None)
                setattr(value, "nabla_Expression183", self)

class nabla_BaseTypeConstant(Expression):

    pass
class nabla_VectorConstant(Expression):

    pass
class nabla_Minus(Expression):

    def __init__(self, op: str, nabla_Minus: "nabla_Expression" = None, nabla_Minus177: "nabla_Expression" = None):
        self.op = op
        self.nabla_Minus = nabla_Minus
        self.nabla_Minus177 = nabla_Minus177
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def nabla_Minus177(self):
        return self.__nabla_Minus177

    @nabla_Minus177.setter
    def nabla_Minus177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_Minus__nabla_Minus177", None)
        self.__nabla_Minus177 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_Expression178"):
                opp_val = getattr(old_value, "nabla_Expression178", None)
                if opp_val == self:
                    setattr(old_value, "nabla_Expression178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_Expression178"):
                opp_val = getattr(value, "nabla_Expression178", None)
                setattr(value, "nabla_Expression178", self)

    @property
    def nabla_Minus(self):
        return self.__nabla_Minus

    @nabla_Minus.setter
    def nabla_Minus(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_Minus__nabla_Minus", None)
        self.__nabla_Minus = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_Expression175"):
                opp_val = getattr(old_value, "nabla_Expression175", None)
                if opp_val == self:
                    setattr(old_value, "nabla_Expression175", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_Expression175"):
                opp_val = getattr(value, "nabla_Expression175", None)
                setattr(value, "nabla_Expression175", self)

class nabla_Parenthesis(Expression):

    pass
class nabla_Comparison(Expression):

    def __init__(self, op: str, nabla_Comparison: "nabla_Expression" = None, nabla_Comparison167: "nabla_Expression" = None):
        self.op = op
        self.nabla_Comparison = nabla_Comparison
        self.nabla_Comparison167 = nabla_Comparison167
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def nabla_Comparison(self):
        return self.__nabla_Comparison

    @nabla_Comparison.setter
    def nabla_Comparison(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_Comparison__nabla_Comparison", None)
        self.__nabla_Comparison = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_Expression165"):
                opp_val = getattr(old_value, "nabla_Expression165", None)
                if opp_val == self:
                    setattr(old_value, "nabla_Expression165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_Expression165"):
                opp_val = getattr(value, "nabla_Expression165", None)
                setattr(value, "nabla_Expression165", self)

    @property
    def nabla_Comparison167(self):
        return self.__nabla_Comparison167

    @nabla_Comparison167.setter
    def nabla_Comparison167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_Comparison__nabla_Comparison167", None)
        self.__nabla_Comparison167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_Expression168"):
                opp_val = getattr(old_value, "nabla_Expression168", None)
                if opp_val == self:
                    setattr(old_value, "nabla_Expression168", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_Expression168"):
                opp_val = getattr(value, "nabla_Expression168", None)
                setattr(value, "nabla_Expression168", self)

class nabla_UnaryMinus(Expression):

    pass
class nabla_IntConstant(Expression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class FunctionOrReduction:

    pass
class nabla_FunctionOrReduction:

    def __init__(self, name: str, nabla_FunctionOrReduction106: set["nabla_Arg"] = None, nabla_FunctionOrReduction108: "nabla_Instruction" = None, nabla_FunctionOrReduction: set["nabla_SimpleVar"] = None):
        self.name = name
        self.nabla_FunctionOrReduction106 = nabla_FunctionOrReduction106 if nabla_FunctionOrReduction106 is not None else set()
        self.nabla_FunctionOrReduction108 = nabla_FunctionOrReduction108
        self.nabla_FunctionOrReduction = nabla_FunctionOrReduction if nabla_FunctionOrReduction is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def nabla_FunctionOrReduction106(self):
        return self.__nabla_FunctionOrReduction106

    @nabla_FunctionOrReduction106.setter
    def nabla_FunctionOrReduction106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_FunctionOrReduction__nabla_FunctionOrReduction106", None)
        self.__nabla_FunctionOrReduction106 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nabla_Arg"):
                    opp_val = getattr(item, "nabla_Arg", None)
                    
                    if opp_val == self:
                        setattr(item, "nabla_Arg", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nabla_Arg"):
                    opp_val = getattr(item, "nabla_Arg", None)
                    
                    setattr(item, "nabla_Arg", self)
                    

    @property
    def nabla_FunctionOrReduction108(self):
        return self.__nabla_FunctionOrReduction108

    @nabla_FunctionOrReduction108.setter
    def nabla_FunctionOrReduction108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_FunctionOrReduction__nabla_FunctionOrReduction108", None)
        self.__nabla_FunctionOrReduction108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_Instruction109"):
                opp_val = getattr(old_value, "nabla_Instruction109", None)
                if opp_val == self:
                    setattr(old_value, "nabla_Instruction109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_Instruction109"):
                opp_val = getattr(value, "nabla_Instruction109", None)
                setattr(value, "nabla_Instruction109", self)

    @property
    def nabla_FunctionOrReduction(self):
        return self.__nabla_FunctionOrReduction

    @nabla_FunctionOrReduction.setter
    def nabla_FunctionOrReduction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_FunctionOrReduction__nabla_FunctionOrReduction", None)
        self.__nabla_FunctionOrReduction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nabla_SimpleVar104"):
                    opp_val = getattr(item, "nabla_SimpleVar104", None)
                    
                    if opp_val == self:
                        setattr(item, "nabla_SimpleVar104", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nabla_SimpleVar104"):
                    opp_val = getattr(item, "nabla_SimpleVar104", None)
                    
                    setattr(item, "nabla_SimpleVar104", self)
                    

class Var:

    pass
class nabla_ConnectivityVar(Var):

    pass
class TimeIteratorRef:

    pass
class nabla_NextTimeIteratorRef(TimeIteratorRef):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class nabla_InitTimeIteratorRef(TimeIteratorRef):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class nabla_CurrentTimeIteratorRef(TimeIteratorRef):

    pass
class nabla_ArgOrVar:

    def __init__(self, name: str, nabla_ArgOrVar: "nabla_ArgOrVarRef" = None):
        self.name = name
        self.nabla_ArgOrVar = nabla_ArgOrVar
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def nabla_ArgOrVar(self):
        return self.__nabla_ArgOrVar

    @nabla_ArgOrVar.setter
    def nabla_ArgOrVar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_ArgOrVar__nabla_ArgOrVar", None)
        self.__nabla_ArgOrVar = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_ArgOrVarRef128"):
                opp_val = getattr(old_value, "nabla_ArgOrVarRef128", None)
                if opp_val == self:
                    setattr(old_value, "nabla_ArgOrVarRef128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_ArgOrVarRef128"):
                opp_val = getattr(value, "nabla_ArgOrVarRef128", None)
                setattr(value, "nabla_ArgOrVarRef128", self)

class ArgOrVar:

    pass
class nabla_Arg(ArgOrVar):

    pass
class nabla_TimeIterator(ArgOrVar):

    pass
class nabla_TimeIteratorRef:

    pass
class ConnectivityCall:

    pass
class nabla_ItemRef:

    def __init__(self, inc: int, dec: int, nabla_ItemRef: "nabla_ConnectivityCall" = None, nabla_ItemRef92: "nabla_Item" = None, nabla_ItemRef134: "nabla_ArgOrVarRef" = None):
        self.inc = inc
        self.dec = dec
        self.nabla_ItemRef = nabla_ItemRef
        self.nabla_ItemRef92 = nabla_ItemRef92
        self.nabla_ItemRef134 = nabla_ItemRef134
        
    @property
    def dec(self) -> int:
        return self.__dec

    @dec.setter
    def dec(self, dec: int):
        self.__dec = dec

    @property
    def inc(self) -> int:
        return self.__inc

    @inc.setter
    def inc(self, inc: int):
        self.__inc = inc

    @property
    def nabla_ItemRef134(self):
        return self.__nabla_ItemRef134

    @nabla_ItemRef134.setter
    def nabla_ItemRef134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_ItemRef__nabla_ItemRef134", None)
        self.__nabla_ItemRef134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_ArgOrVarRef133"):
                opp_val = getattr(old_value, "nabla_ArgOrVarRef133", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_ArgOrVarRef133"):
                opp_val = getattr(value, "nabla_ArgOrVarRef133", None)
                if opp_val is None:
                    setattr(value, "nabla_ArgOrVarRef133", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def nabla_ItemRef(self):
        return self.__nabla_ItemRef

    @nabla_ItemRef.setter
    def nabla_ItemRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_ItemRef__nabla_ItemRef", None)
        self.__nabla_ItemRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_ConnectivityCall"):
                opp_val = getattr(old_value, "nabla_ConnectivityCall", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_ConnectivityCall"):
                opp_val = getattr(value, "nabla_ConnectivityCall", None)
                if opp_val is None:
                    setattr(value, "nabla_ConnectivityCall", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def nabla_ItemRef92(self):
        return self.__nabla_ItemRef92

    @nabla_ItemRef92.setter
    def nabla_ItemRef92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_ItemRef__nabla_ItemRef92", None)
        self.__nabla_ItemRef92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_Item93"):
                opp_val = getattr(old_value, "nabla_Item93", None)
                if opp_val == self:
                    setattr(old_value, "nabla_Item93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_Item93"):
                opp_val = getattr(value, "nabla_Item93", None)
                setattr(value, "nabla_Item93", self)

class nabla_ConnectivityCall:

    pass
class IterationBlock:

    pass
class nabla_Interval(IterationBlock):

    def __init__(self, from: int, nabla_Interval: "nabla_SimpleVar" = None, nabla_Interval84: "nabla_Expression" = None):
        self.from = from
        self.nabla_Interval = nabla_Interval
        self.nabla_Interval84 = nabla_Interval84
        
    @property
    def from(self) -> int:
        return self.__from

    @from.setter
    def from(self, from: int):
        self.__from = from

    @property
    def nabla_Interval84(self):
        return self.__nabla_Interval84

    @nabla_Interval84.setter
    def nabla_Interval84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_Interval__nabla_Interval84", None)
        self.__nabla_Interval84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_Expression85"):
                opp_val = getattr(old_value, "nabla_Expression85", None)
                if opp_val == self:
                    setattr(old_value, "nabla_Expression85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_Expression85"):
                opp_val = getattr(value, "nabla_Expression85", None)
                setattr(value, "nabla_Expression85", self)

    @property
    def nabla_Interval(self):
        return self.__nabla_Interval

    @nabla_Interval.setter
    def nabla_Interval(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_Interval__nabla_Interval", None)
        self.__nabla_Interval = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_SimpleVar82"):
                opp_val = getattr(old_value, "nabla_SimpleVar82", None)
                if opp_val == self:
                    setattr(old_value, "nabla_SimpleVar82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_SimpleVar82"):
                opp_val = getattr(value, "nabla_SimpleVar82", None)
                setattr(value, "nabla_SimpleVar82", self)

class nabla_SpaceIterator(IterationBlock):

    pass
class Container:

    pass
class nabla_SetRef(Container):

    pass
class nabla_SingletonDefinition:

    pass
class nabla_MultipleConnectivityCall(ConnectivityCall, Container):

    pass
class nabla_SingleConnectivityCall(ConnectivityCall):

    pass
class nabla_Container:

    pass
class nabla_Item:

    def __init__(self, name: str, nabla_Item: "nabla_ItemDefinition" = None, nabla_Item67: "nabla_SpaceIterator" = None, nabla_Item77: "nabla_SingletonDefinition" = None, nabla_Item93: "nabla_ItemRef" = None):
        self.name = name
        self.nabla_Item = nabla_Item
        self.nabla_Item67 = nabla_Item67
        self.nabla_Item77 = nabla_Item77
        self.nabla_Item93 = nabla_Item93
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def nabla_Item93(self):
        return self.__nabla_Item93

    @nabla_Item93.setter
    def nabla_Item93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_Item__nabla_Item93", None)
        self.__nabla_Item93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_ItemRef92"):
                opp_val = getattr(old_value, "nabla_ItemRef92", None)
                if opp_val == self:
                    setattr(old_value, "nabla_ItemRef92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_ItemRef92"):
                opp_val = getattr(value, "nabla_ItemRef92", None)
                setattr(value, "nabla_ItemRef92", self)

    @property
    def nabla_Item(self):
        return self.__nabla_Item

    @nabla_Item.setter
    def nabla_Item(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_Item__nabla_Item", None)
        self.__nabla_Item = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_ItemDefinition"):
                opp_val = getattr(old_value, "nabla_ItemDefinition", None)
                if opp_val == self:
                    setattr(old_value, "nabla_ItemDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_ItemDefinition"):
                opp_val = getattr(value, "nabla_ItemDefinition", None)
                setattr(value, "nabla_ItemDefinition", self)

    @property
    def nabla_Item77(self):
        return self.__nabla_Item77

    @nabla_Item77.setter
    def nabla_Item77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_Item__nabla_Item77", None)
        self.__nabla_Item77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_SingletonDefinition76"):
                opp_val = getattr(old_value, "nabla_SingletonDefinition76", None)
                if opp_val == self:
                    setattr(old_value, "nabla_SingletonDefinition76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_SingletonDefinition76"):
                opp_val = getattr(value, "nabla_SingletonDefinition76", None)
                setattr(value, "nabla_SingletonDefinition76", self)

    @property
    def nabla_Item67(self):
        return self.__nabla_Item67

    @nabla_Item67.setter
    def nabla_Item67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_Item__nabla_Item67", None)
        self.__nabla_Item67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_SpaceIterator"):
                opp_val = getattr(old_value, "nabla_SpaceIterator", None)
                if opp_val == self:
                    setattr(old_value, "nabla_SpaceIterator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_SpaceIterator"):
                opp_val = getattr(value, "nabla_SpaceIterator", None)
                setattr(value, "nabla_SpaceIterator", self)

class Iterable:

    pass
class nabla_ReductionCall(Expression, Iterable):

    pass
class nabla_Var(ArgOrVar):

    pass
class nabla_BaseType:

    def __init__(self, primitive: str, nabla_BaseType: "nabla_VarGroupDeclaration" = None, nabla_BaseType112: "nabla_Function" = None, nabla_BaseType115: "nabla_Function" = None, nabla_BaseType121: "nabla_Reduction" = None, nabla_BaseType139: set["nabla_Expression"] = None, nabla_BaseType206: "nabla_BaseTypeConstant" = None):
        self.primitive = primitive
        self.nabla_BaseType = nabla_BaseType
        self.nabla_BaseType112 = nabla_BaseType112
        self.nabla_BaseType115 = nabla_BaseType115
        self.nabla_BaseType121 = nabla_BaseType121
        self.nabla_BaseType139 = nabla_BaseType139 if nabla_BaseType139 is not None else set()
        self.nabla_BaseType206 = nabla_BaseType206
        
    @property
    def primitive(self) -> str:
        return self.__primitive

    @primitive.setter
    def primitive(self, primitive: str):
        self.__primitive = primitive

    @property
    def nabla_BaseType139(self):
        return self.__nabla_BaseType139

    @nabla_BaseType139.setter
    def nabla_BaseType139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_BaseType__nabla_BaseType139", None)
        self.__nabla_BaseType139 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nabla_Expression140"):
                    opp_val = getattr(item, "nabla_Expression140", None)
                    
                    if opp_val == self:
                        setattr(item, "nabla_Expression140", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nabla_Expression140"):
                    opp_val = getattr(item, "nabla_Expression140", None)
                    
                    setattr(item, "nabla_Expression140", self)
                    

    @property
    def nabla_BaseType206(self):
        return self.__nabla_BaseType206

    @nabla_BaseType206.setter
    def nabla_BaseType206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_BaseType__nabla_BaseType206", None)
        self.__nabla_BaseType206 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_BaseTypeConstant"):
                opp_val = getattr(old_value, "nabla_BaseTypeConstant", None)
                if opp_val == self:
                    setattr(old_value, "nabla_BaseTypeConstant", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_BaseTypeConstant"):
                opp_val = getattr(value, "nabla_BaseTypeConstant", None)
                setattr(value, "nabla_BaseTypeConstant", self)

    @property
    def nabla_BaseType121(self):
        return self.__nabla_BaseType121

    @nabla_BaseType121.setter
    def nabla_BaseType121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_BaseType__nabla_BaseType121", None)
        self.__nabla_BaseType121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_Reduction120"):
                opp_val = getattr(old_value, "nabla_Reduction120", None)
                if opp_val == self:
                    setattr(old_value, "nabla_Reduction120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_Reduction120"):
                opp_val = getattr(value, "nabla_Reduction120", None)
                setattr(value, "nabla_Reduction120", self)

    @property
    def nabla_BaseType115(self):
        return self.__nabla_BaseType115

    @nabla_BaseType115.setter
    def nabla_BaseType115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_BaseType__nabla_BaseType115", None)
        self.__nabla_BaseType115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_Function114"):
                opp_val = getattr(old_value, "nabla_Function114", None)
                if opp_val == self:
                    setattr(old_value, "nabla_Function114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_Function114"):
                opp_val = getattr(value, "nabla_Function114", None)
                setattr(value, "nabla_Function114", self)

    @property
    def nabla_BaseType(self):
        return self.__nabla_BaseType

    @nabla_BaseType.setter
    def nabla_BaseType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_BaseType__nabla_BaseType", None)
        self.__nabla_BaseType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_VarGroupDeclaration39"):
                opp_val = getattr(old_value, "nabla_VarGroupDeclaration39", None)
                if opp_val == self:
                    setattr(old_value, "nabla_VarGroupDeclaration39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_VarGroupDeclaration39"):
                opp_val = getattr(value, "nabla_VarGroupDeclaration39", None)
                setattr(value, "nabla_VarGroupDeclaration39", self)

    @property
    def nabla_BaseType112(self):
        return self.__nabla_BaseType112

    @nabla_BaseType112.setter
    def nabla_BaseType112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_BaseType__nabla_BaseType112", None)
        self.__nabla_BaseType112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_Function111"):
                opp_val = getattr(old_value, "nabla_Function111", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_Function111"):
                opp_val = getattr(value, "nabla_Function111", None)
                if opp_val is None:
                    setattr(value, "nabla_Function111", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class nabla_ArgOrVarRef(Expression):

    pass
class Instruction:

    pass
class nabla_Loop(Iterable, Instruction):

    pass
class nabla_Exit(Instruction):

    def __init__(self, message: str):
        self.message = message
        
    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

class nabla_Return(Instruction):

    pass
class nabla_If(Instruction):

    pass
class nabla_SetDefinition(Instruction):

    def __init__(self, name: str, nabla_SetDefinition: "nabla_MultipleConnectivityCall" = None, nabla_SetDefinition65: "nabla_SetRef" = None):
        self.name = name
        self.nabla_SetDefinition = nabla_SetDefinition
        self.nabla_SetDefinition65 = nabla_SetDefinition65
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def nabla_SetDefinition65(self):
        return self.__nabla_SetDefinition65

    @nabla_SetDefinition65.setter
    def nabla_SetDefinition65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_SetDefinition__nabla_SetDefinition65", None)
        self.__nabla_SetDefinition65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_SetRef"):
                opp_val = getattr(old_value, "nabla_SetRef", None)
                if opp_val == self:
                    setattr(old_value, "nabla_SetRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_SetRef"):
                opp_val = getattr(value, "nabla_SetRef", None)
                setattr(value, "nabla_SetRef", self)

    @property
    def nabla_SetDefinition(self):
        return self.__nabla_SetDefinition

    @nabla_SetDefinition.setter
    def nabla_SetDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_SetDefinition__nabla_SetDefinition", None)
        self.__nabla_SetDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_MultipleConnectivityCall"):
                opp_val = getattr(old_value, "nabla_MultipleConnectivityCall", None)
                if opp_val == self:
                    setattr(old_value, "nabla_MultipleConnectivityCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_MultipleConnectivityCall"):
                opp_val = getattr(value, "nabla_MultipleConnectivityCall", None)
                setattr(value, "nabla_MultipleConnectivityCall", self)

class nabla_InstructionBlock(Instruction):

    pass
class nabla_ItemDefinition(Instruction):

    pass
class nabla_Affectation(Instruction):

    pass
class nabla_IterationBlock:

    pass
class nabla_Iterable:

    pass
class nabla_Instruction:

    pass
class Connectivity:

    pass
class nabla_MultipleConnectivity(Connectivity):

    pass
class nabla_SingleConnectivity(Connectivity):

    pass
class nabla_Job:

    def __init__(self, name: str, nabla_Job: "nabla_NablaModule" = None, nabla_Job30: "nabla_Instruction" = None):
        self.name = name
        self.nabla_Job = nabla_Job
        self.nabla_Job30 = nabla_Job30
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def nabla_Job30(self):
        return self.__nabla_Job30

    @nabla_Job30.setter
    def nabla_Job30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_Job__nabla_Job30", None)
        self.__nabla_Job30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_Instruction"):
                opp_val = getattr(old_value, "nabla_Instruction", None)
                if opp_val == self:
                    setattr(old_value, "nabla_Instruction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_Instruction"):
                opp_val = getattr(value, "nabla_Instruction", None)
                setattr(value, "nabla_Instruction", self)

    @property
    def nabla_Job(self):
        return self.__nabla_Job

    @nabla_Job.setter
    def nabla_Job(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_Job__nabla_Job", None)
        self.__nabla_Job = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_NablaModule18"):
                opp_val = getattr(old_value, "nabla_NablaModule18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_NablaModule18"):
                opp_val = getattr(value, "nabla_NablaModule18", None)
                if opp_val is None:
                    setattr(value, "nabla_NablaModule18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class nabla_Expression:

    pass
class nabla_SimpleVar(Var):

    pass
class nabla_OptDefinition:

    pass
class nabla_Function(FunctionOrReduction):

    def __init__(self, external: bool, nabla_Function: "nabla_NablaModule" = None, nabla_Function111: set["nabla_BaseType"] = None, nabla_Function114: "nabla_BaseType" = None, nabla_Function201: "nabla_FunctionCall" = None):
        self.external = external
        self.nabla_Function = nabla_Function
        self.nabla_Function111 = nabla_Function111 if nabla_Function111 is not None else set()
        self.nabla_Function114 = nabla_Function114
        self.nabla_Function201 = nabla_Function201
        
    @property
    def external(self) -> bool:
        return self.__external

    @external.setter
    def external(self, external: bool):
        self.__external = external

    @property
    def nabla_Function114(self):
        return self.__nabla_Function114

    @nabla_Function114.setter
    def nabla_Function114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_Function__nabla_Function114", None)
        self.__nabla_Function114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_BaseType115"):
                opp_val = getattr(old_value, "nabla_BaseType115", None)
                if opp_val == self:
                    setattr(old_value, "nabla_BaseType115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_BaseType115"):
                opp_val = getattr(value, "nabla_BaseType115", None)
                setattr(value, "nabla_BaseType115", self)

    @property
    def nabla_Function111(self):
        return self.__nabla_Function111

    @nabla_Function111.setter
    def nabla_Function111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_Function__nabla_Function111", None)
        self.__nabla_Function111 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nabla_BaseType112"):
                    opp_val = getattr(item, "nabla_BaseType112", None)
                    
                    if opp_val == self:
                        setattr(item, "nabla_BaseType112", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nabla_BaseType112"):
                    opp_val = getattr(item, "nabla_BaseType112", None)
                    
                    setattr(item, "nabla_BaseType112", self)
                    

    @property
    def nabla_Function201(self):
        return self.__nabla_Function201

    @nabla_Function201.setter
    def nabla_Function201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_Function__nabla_Function201", None)
        self.__nabla_Function201 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_FunctionCall"):
                opp_val = getattr(old_value, "nabla_FunctionCall", None)
                if opp_val == self:
                    setattr(old_value, "nabla_FunctionCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_FunctionCall"):
                opp_val = getattr(value, "nabla_FunctionCall", None)
                setattr(value, "nabla_FunctionCall", self)

    @property
    def nabla_Function(self):
        return self.__nabla_Function

    @nabla_Function.setter
    def nabla_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_Function__nabla_Function", None)
        self.__nabla_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_NablaModule8"):
                opp_val = getattr(old_value, "nabla_NablaModule8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_NablaModule8"):
                opp_val = getattr(value, "nabla_NablaModule8", None)
                if opp_val is None:
                    setattr(value, "nabla_NablaModule8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class nabla_Reduction(FunctionOrReduction):

    pass
class nabla_Connectivity:

    def __init__(self, name: str, nabla_Connectivity: "nabla_NablaModule" = None, nabla_Connectivity24: set["nabla_ItemType"] = None, nabla_Connectivity27: "nabla_ItemType" = None):
        self.name = name
        self.nabla_Connectivity = nabla_Connectivity
        self.nabla_Connectivity24 = nabla_Connectivity24 if nabla_Connectivity24 is not None else set()
        self.nabla_Connectivity27 = nabla_Connectivity27
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def nabla_Connectivity(self):
        return self.__nabla_Connectivity

    @nabla_Connectivity.setter
    def nabla_Connectivity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_Connectivity__nabla_Connectivity", None)
        self.__nabla_Connectivity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_NablaModule4"):
                opp_val = getattr(old_value, "nabla_NablaModule4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_NablaModule4"):
                opp_val = getattr(value, "nabla_NablaModule4", None)
                if opp_val is None:
                    setattr(value, "nabla_NablaModule4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def nabla_Connectivity24(self):
        return self.__nabla_Connectivity24

    @nabla_Connectivity24.setter
    def nabla_Connectivity24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_Connectivity__nabla_Connectivity24", None)
        self.__nabla_Connectivity24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nabla_ItemType25"):
                    opp_val = getattr(item, "nabla_ItemType25", None)
                    
                    if opp_val == self:
                        setattr(item, "nabla_ItemType25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nabla_ItemType25"):
                    opp_val = getattr(item, "nabla_ItemType25", None)
                    
                    setattr(item, "nabla_ItemType25", self)
                    

    @property
    def nabla_Connectivity27(self):
        return self.__nabla_Connectivity27

    @nabla_Connectivity27.setter
    def nabla_Connectivity27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_Connectivity__nabla_Connectivity27", None)
        self.__nabla_Connectivity27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_ItemType28"):
                opp_val = getattr(old_value, "nabla_ItemType28", None)
                if opp_val == self:
                    setattr(old_value, "nabla_ItemType28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_ItemType28"):
                opp_val = getattr(value, "nabla_ItemType28", None)
                setattr(value, "nabla_ItemType28", self)

class nabla_ItemType:

    def __init__(self, name: str, nabla_ItemType: "nabla_NablaModule" = None, nabla_ItemType25: "nabla_Connectivity" = None, nabla_ItemType28: "nabla_Connectivity" = None):
        self.name = name
        self.nabla_ItemType = nabla_ItemType
        self.nabla_ItemType25 = nabla_ItemType25
        self.nabla_ItemType28 = nabla_ItemType28
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def nabla_ItemType28(self):
        return self.__nabla_ItemType28

    @nabla_ItemType28.setter
    def nabla_ItemType28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_ItemType__nabla_ItemType28", None)
        self.__nabla_ItemType28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_Connectivity27"):
                opp_val = getattr(old_value, "nabla_Connectivity27", None)
                if opp_val == self:
                    setattr(old_value, "nabla_Connectivity27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_Connectivity27"):
                opp_val = getattr(value, "nabla_Connectivity27", None)
                setattr(value, "nabla_Connectivity27", self)

    @property
    def nabla_ItemType25(self):
        return self.__nabla_ItemType25

    @nabla_ItemType25.setter
    def nabla_ItemType25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_ItemType__nabla_ItemType25", None)
        self.__nabla_ItemType25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_Connectivity24"):
                opp_val = getattr(old_value, "nabla_Connectivity24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_Connectivity24"):
                opp_val = getattr(value, "nabla_Connectivity24", None)
                if opp_val is None:
                    setattr(value, "nabla_Connectivity24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def nabla_ItemType(self):
        return self.__nabla_ItemType

    @nabla_ItemType.setter
    def nabla_ItemType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_ItemType__nabla_ItemType", None)
        self.__nabla_ItemType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_NablaModule2"):
                opp_val = getattr(old_value, "nabla_NablaModule2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_NablaModule2"):
                opp_val = getattr(value, "nabla_NablaModule2", None)
                if opp_val is None:
                    setattr(value, "nabla_NablaModule2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class nabla_Import:

    def __init__(self, importedNamespace: str, nabla_Import: "nabla_NablaModule" = None):
        self.importedNamespace = importedNamespace
        self.nabla_Import = nabla_Import
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

    @property
    def nabla_Import(self):
        return self.__nabla_Import

    @nabla_Import.setter
    def nabla_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_Import__nabla_Import", None)
        self.__nabla_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_NablaModule"):
                opp_val = getattr(old_value, "nabla_NablaModule", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_NablaModule"):
                opp_val = getattr(value, "nabla_NablaModule", None)
                if opp_val is None:
                    setattr(value, "nabla_NablaModule", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class nabla_TimeIteratorDefinition:

    pass
class nabla_VarGroupDeclaration(Instruction):

    pass
class nabla_SimpleVarDefinition(Instruction):

    pass
class nabla_NablaModule:

    def __init__(self, name: str, nabla_NablaModule12: set["nabla_SimpleVarDefinition"] = None, nabla_NablaModule14: set["nabla_VarGroupDeclaration"] = None, nabla_NablaModule16: "nabla_TimeIteratorDefinition" = None, nabla_NablaModule: set["nabla_Import"] = None, nabla_NablaModule2: set["nabla_ItemType"] = None, nabla_NablaModule4: set["nabla_Connectivity"] = None, nabla_NablaModule6: set["nabla_Reduction"] = None, nabla_NablaModule8: set["nabla_Function"] = None, nabla_NablaModule10: set["nabla_OptDefinition"] = None, nabla_NablaModule18: set["nabla_Job"] = None):
        self.name = name
        self.nabla_NablaModule12 = nabla_NablaModule12 if nabla_NablaModule12 is not None else set()
        self.nabla_NablaModule14 = nabla_NablaModule14 if nabla_NablaModule14 is not None else set()
        self.nabla_NablaModule16 = nabla_NablaModule16
        self.nabla_NablaModule = nabla_NablaModule if nabla_NablaModule is not None else set()
        self.nabla_NablaModule2 = nabla_NablaModule2 if nabla_NablaModule2 is not None else set()
        self.nabla_NablaModule4 = nabla_NablaModule4 if nabla_NablaModule4 is not None else set()
        self.nabla_NablaModule6 = nabla_NablaModule6 if nabla_NablaModule6 is not None else set()
        self.nabla_NablaModule8 = nabla_NablaModule8 if nabla_NablaModule8 is not None else set()
        self.nabla_NablaModule10 = nabla_NablaModule10 if nabla_NablaModule10 is not None else set()
        self.nabla_NablaModule18 = nabla_NablaModule18 if nabla_NablaModule18 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def nabla_NablaModule(self):
        return self.__nabla_NablaModule

    @nabla_NablaModule.setter
    def nabla_NablaModule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_NablaModule__nabla_NablaModule", None)
        self.__nabla_NablaModule = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nabla_Import"):
                    opp_val = getattr(item, "nabla_Import", None)
                    
                    if opp_val == self:
                        setattr(item, "nabla_Import", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nabla_Import"):
                    opp_val = getattr(item, "nabla_Import", None)
                    
                    setattr(item, "nabla_Import", self)
                    

    @property
    def nabla_NablaModule6(self):
        return self.__nabla_NablaModule6

    @nabla_NablaModule6.setter
    def nabla_NablaModule6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_NablaModule__nabla_NablaModule6", None)
        self.__nabla_NablaModule6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nabla_Reduction"):
                    opp_val = getattr(item, "nabla_Reduction", None)
                    
                    if opp_val == self:
                        setattr(item, "nabla_Reduction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nabla_Reduction"):
                    opp_val = getattr(item, "nabla_Reduction", None)
                    
                    setattr(item, "nabla_Reduction", self)
                    

    @property
    def nabla_NablaModule2(self):
        return self.__nabla_NablaModule2

    @nabla_NablaModule2.setter
    def nabla_NablaModule2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_NablaModule__nabla_NablaModule2", None)
        self.__nabla_NablaModule2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nabla_ItemType"):
                    opp_val = getattr(item, "nabla_ItemType", None)
                    
                    if opp_val == self:
                        setattr(item, "nabla_ItemType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nabla_ItemType"):
                    opp_val = getattr(item, "nabla_ItemType", None)
                    
                    setattr(item, "nabla_ItemType", self)
                    

    @property
    def nabla_NablaModule18(self):
        return self.__nabla_NablaModule18

    @nabla_NablaModule18.setter
    def nabla_NablaModule18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_NablaModule__nabla_NablaModule18", None)
        self.__nabla_NablaModule18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nabla_Job"):
                    opp_val = getattr(item, "nabla_Job", None)
                    
                    if opp_val == self:
                        setattr(item, "nabla_Job", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nabla_Job"):
                    opp_val = getattr(item, "nabla_Job", None)
                    
                    setattr(item, "nabla_Job", self)
                    

    @property
    def nabla_NablaModule14(self):
        return self.__nabla_NablaModule14

    @nabla_NablaModule14.setter
    def nabla_NablaModule14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_NablaModule__nabla_NablaModule14", None)
        self.__nabla_NablaModule14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nabla_VarGroupDeclaration"):
                    opp_val = getattr(item, "nabla_VarGroupDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "nabla_VarGroupDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nabla_VarGroupDeclaration"):
                    opp_val = getattr(item, "nabla_VarGroupDeclaration", None)
                    
                    setattr(item, "nabla_VarGroupDeclaration", self)
                    

    @property
    def nabla_NablaModule8(self):
        return self.__nabla_NablaModule8

    @nabla_NablaModule8.setter
    def nabla_NablaModule8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_NablaModule__nabla_NablaModule8", None)
        self.__nabla_NablaModule8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nabla_Function"):
                    opp_val = getattr(item, "nabla_Function", None)
                    
                    if opp_val == self:
                        setattr(item, "nabla_Function", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nabla_Function"):
                    opp_val = getattr(item, "nabla_Function", None)
                    
                    setattr(item, "nabla_Function", self)
                    

    @property
    def nabla_NablaModule16(self):
        return self.__nabla_NablaModule16

    @nabla_NablaModule16.setter
    def nabla_NablaModule16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_NablaModule__nabla_NablaModule16", None)
        self.__nabla_NablaModule16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nabla_TimeIteratorDefinition"):
                opp_val = getattr(old_value, "nabla_TimeIteratorDefinition", None)
                if opp_val == self:
                    setattr(old_value, "nabla_TimeIteratorDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nabla_TimeIteratorDefinition"):
                opp_val = getattr(value, "nabla_TimeIteratorDefinition", None)
                setattr(value, "nabla_TimeIteratorDefinition", self)

    @property
    def nabla_NablaModule12(self):
        return self.__nabla_NablaModule12

    @nabla_NablaModule12.setter
    def nabla_NablaModule12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_NablaModule__nabla_NablaModule12", None)
        self.__nabla_NablaModule12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nabla_SimpleVarDefinition"):
                    opp_val = getattr(item, "nabla_SimpleVarDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "nabla_SimpleVarDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nabla_SimpleVarDefinition"):
                    opp_val = getattr(item, "nabla_SimpleVarDefinition", None)
                    
                    setattr(item, "nabla_SimpleVarDefinition", self)
                    

    @property
    def nabla_NablaModule4(self):
        return self.__nabla_NablaModule4

    @nabla_NablaModule4.setter
    def nabla_NablaModule4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_NablaModule__nabla_NablaModule4", None)
        self.__nabla_NablaModule4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nabla_Connectivity"):
                    opp_val = getattr(item, "nabla_Connectivity", None)
                    
                    if opp_val == self:
                        setattr(item, "nabla_Connectivity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nabla_Connectivity"):
                    opp_val = getattr(item, "nabla_Connectivity", None)
                    
                    setattr(item, "nabla_Connectivity", self)
                    

    @property
    def nabla_NablaModule10(self):
        return self.__nabla_NablaModule10

    @nabla_NablaModule10.setter
    def nabla_NablaModule10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nabla_NablaModule__nabla_NablaModule10", None)
        self.__nabla_NablaModule10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nabla_OptDefinition"):
                    opp_val = getattr(item, "nabla_OptDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "nabla_OptDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nabla_OptDefinition"):
                    opp_val = getattr(item, "nabla_OptDefinition", None)
                    
                    setattr(item, "nabla_OptDefinition", self)
                    
