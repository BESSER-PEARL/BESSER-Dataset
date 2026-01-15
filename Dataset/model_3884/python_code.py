from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class BoolLiteralEnum(Enum):
    TRUE = "TRUE"
    FALSE = "FALSE"
class InequalityOp(Enum):
    LESS = "LESS"
    LESS_EQ = "LESS_EQ"
    GREATER = "GREATER"
    GREATER_EQ = "GREATER_EQ"
class PrimitiveTypeEnum(Enum):
    BOOL = "BOOL"
    INT = "INT"
    NAT = "NAT"
    NAT1 = "NAT1"
    STRING = "STRING"


############################################
# Definition of Classes
############################################

class ReturnTypeExpr:

    pass
class b_ReturnOr(ReturnTypeExpr):

    pass
class b_Program:

    pass
class PropertyExpr:

    pass
class b_PropertyRange(PropertyExpr):

    pass
class b_PropertyTyped(PropertyExpr):

    pass
class ReturnExpr:

    pass
class b_Neg(ReturnExpr):

    pass
class Type:

    pass
class b_PrimitiveType(Type):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class b_SimpleCall:

    pass
class b_CaseExpr:

    pass
class Return:

    pass
class b_ReturnTuple(Return):

    pass
class b_ReturnTypeExpr(Return):

    pass
class b_ReturnExpr:

    pass
class Statement:

    pass
class b_BeginBody:

    pass
class BeginBody:

    pass
class b_FinalExpr(BeginBody):

    pass
class b_PreExpr:

    pass
class b_Condition:

    pass
class b_IfCond:

    pass
class FinalExpr:

    pass
class b_Statement:

    pass
class Expr:

    pass
class b_Case(Expr, FinalExpr):

    pass
class b_Call(Expr, Statement):

    pass
class b_Return(Expr, FinalExpr):

    pass
class b_Assign(Expr, Statement):

    pass
class Body:

    pass
class b_Seq(BeginBody, Body):

    pass
class b_Pre(Body):

    pass
class b_If(Expr, Body, FinalExpr):

    pass
class b_Begin(Body):

    pass
class b_Skip(Expr, Body):

    pass
class b_Expr:

    pass
class b_Body:

    pass
class b_Operation:

    def __init__(self, name: str, b_Operation: "b_Operations" = None, b_Operation97: set["b_Variable"] = None, b_Operation100: set["b_Variable"] = None, b_Operation103: "b_Body" = None, b_Operation153: "b_Call" = None, b_Operation158: "b_SimpleCall" = None, b_Operation164: "b_LocalOperations" = None):
        self.name = name
        self.b_Operation = b_Operation
        self.b_Operation97 = b_Operation97 if b_Operation97 is not None else set()
        self.b_Operation100 = b_Operation100 if b_Operation100 is not None else set()
        self.b_Operation103 = b_Operation103
        self.b_Operation153 = b_Operation153
        self.b_Operation158 = b_Operation158
        self.b_Operation164 = b_Operation164
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def b_Operation158(self):
        return self.__b_Operation158

    @b_Operation158.setter
    def b_Operation158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Operation__b_Operation158", None)
        self.__b_Operation158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_SimpleCall"):
                opp_val = getattr(old_value, "b_SimpleCall", None)
                if opp_val == self:
                    setattr(old_value, "b_SimpleCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_SimpleCall"):
                opp_val = getattr(value, "b_SimpleCall", None)
                setattr(value, "b_SimpleCall", self)

    @property
    def b_Operation153(self):
        return self.__b_Operation153

    @b_Operation153.setter
    def b_Operation153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Operation__b_Operation153", None)
        self.__b_Operation153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_Call152"):
                opp_val = getattr(old_value, "b_Call152", None)
                if opp_val == self:
                    setattr(old_value, "b_Call152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_Call152"):
                opp_val = getattr(value, "b_Call152", None)
                setattr(value, "b_Call152", self)

    @property
    def b_Operation97(self):
        return self.__b_Operation97

    @b_Operation97.setter
    def b_Operation97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Operation__b_Operation97", None)
        self.__b_Operation97 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "b_Variable98"):
                    opp_val = getattr(item, "b_Variable98", None)
                    
                    if opp_val == self:
                        setattr(item, "b_Variable98", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "b_Variable98"):
                    opp_val = getattr(item, "b_Variable98", None)
                    
                    setattr(item, "b_Variable98", self)
                    

    @property
    def b_Operation(self):
        return self.__b_Operation

    @b_Operation.setter
    def b_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Operation__b_Operation", None)
        self.__b_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_Operations95"):
                opp_val = getattr(old_value, "b_Operations95", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_Operations95"):
                opp_val = getattr(value, "b_Operations95", None)
                if opp_val is None:
                    setattr(value, "b_Operations95", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def b_Operation100(self):
        return self.__b_Operation100

    @b_Operation100.setter
    def b_Operation100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Operation__b_Operation100", None)
        self.__b_Operation100 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "b_Variable101"):
                    opp_val = getattr(item, "b_Variable101", None)
                    
                    if opp_val == self:
                        setattr(item, "b_Variable101", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "b_Variable101"):
                    opp_val = getattr(item, "b_Variable101", None)
                    
                    setattr(item, "b_Variable101", self)
                    

    @property
    def b_Operation164(self):
        return self.__b_Operation164

    @b_Operation164.setter
    def b_Operation164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Operation__b_Operation164", None)
        self.__b_Operation164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_LocalOperations163"):
                opp_val = getattr(old_value, "b_LocalOperations163", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_LocalOperations163"):
                opp_val = getattr(value, "b_LocalOperations163", None)
                if opp_val is None:
                    setattr(value, "b_LocalOperations163", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def b_Operation103(self):
        return self.__b_Operation103

    @b_Operation103.setter
    def b_Operation103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Operation__b_Operation103", None)
        self.__b_Operation103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_Body"):
                opp_val = getattr(old_value, "b_Body", None)
                if opp_val == self:
                    setattr(old_value, "b_Body", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_Body"):
                opp_val = getattr(value, "b_Body", None)
                setattr(value, "b_Body", self)

class b_Var(Expr, Body, FinalExpr):

    pass
class Arg:

    pass
class b_ArgMinus(Arg):

    pass
class b_StringLiteral(Arg):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class Condition:

    pass
class b_CondAnd(Condition):

    pass
class b_CondNeg(Condition):

    pass
class b_CondMinus(Condition):

    pass
class b_CondEq(Condition):

    pass
class b_BoolLiteral(Arg, Condition, ReturnExpr):

    def __init__(self, value: str, constant: str):
        self.value = value
        self.constant = constant
        
    @property
    def constant(self) -> str:
        return self.__constant

    @constant.setter
    def constant(self, constant: str):
        self.__constant = constant

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class b_CondLessThan(Condition):

    pass
class b_Arg:

    pass
class LogicalExpr:

    pass
class b_BoolTest(ReturnExpr, LogicalExpr):

    pass
class b_IntLiteral(Arg, Condition, LogicalExpr):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class b_AndExpr(LogicalExpr):

    pass
class b_EqualExpr(LogicalExpr):

    pass
class b_NegExpr(LogicalExpr):

    pass
class b_TypeConstraint(LogicalExpr):

    pass
class b_Ref(ReturnExpr, LogicalExpr, Type, Arg, Condition):

    pass
class b_ImplyExpr(LogicalExpr):

    pass
class b_InequalityExpr(LogicalExpr):

    def __init__(self, op: str, b_InequalityExpr: "b_LogicalExpr" = None, b_InequalityExpr184: "b_LogicalExpr" = None):
        self.op = op
        self.b_InequalityExpr = b_InequalityExpr
        self.b_InequalityExpr184 = b_InequalityExpr184
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def b_InequalityExpr(self):
        return self.__b_InequalityExpr

    @b_InequalityExpr.setter
    def b_InequalityExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_InequalityExpr__b_InequalityExpr", None)
        self.__b_InequalityExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_LogicalExpr182"):
                opp_val = getattr(old_value, "b_LogicalExpr182", None)
                if opp_val == self:
                    setattr(old_value, "b_LogicalExpr182", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_LogicalExpr182"):
                opp_val = getattr(value, "b_LogicalExpr182", None)
                setattr(value, "b_LogicalExpr182", self)

    @property
    def b_InequalityExpr184(self):
        return self.__b_InequalityExpr184

    @b_InequalityExpr184.setter
    def b_InequalityExpr184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_InequalityExpr__b_InequalityExpr184", None)
        self.__b_InequalityExpr184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_LogicalExpr185"):
                opp_val = getattr(old_value, "b_LogicalExpr185", None)
                if opp_val == self:
                    setattr(old_value, "b_LogicalExpr185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_LogicalExpr185"):
                opp_val = getattr(value, "b_LogicalExpr185", None)
                setattr(value, "b_LogicalExpr185", self)

class b_ConstantExpr(LogicalExpr):

    def __init__(self, constant: str):
        self.constant = constant
        
    @property
    def constant(self) -> str:
        return self.__constant

    @constant.setter
    def constant(self, constant: str):
        self.__constant = constant

class b_DefinitionCall(LogicalExpr):

    pass
class b_LogicalExpr:

    pass
class b_Definition:

    def __init__(self, name: str, b_Definition: "b_Definitions" = None, b_Definition78: set["b_Variable"] = None, b_Definition81: "b_LogicalExpr" = None, b_Definition83: "b_DefinitionCall" = None):
        self.name = name
        self.b_Definition = b_Definition
        self.b_Definition78 = b_Definition78 if b_Definition78 is not None else set()
        self.b_Definition81 = b_Definition81
        self.b_Definition83 = b_Definition83
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def b_Definition(self):
        return self.__b_Definition

    @b_Definition.setter
    def b_Definition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Definition__b_Definition", None)
        self.__b_Definition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_Definitions76"):
                opp_val = getattr(old_value, "b_Definitions76", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_Definitions76"):
                opp_val = getattr(value, "b_Definitions76", None)
                if opp_val is None:
                    setattr(value, "b_Definitions76", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def b_Definition81(self):
        return self.__b_Definition81

    @b_Definition81.setter
    def b_Definition81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Definition__b_Definition81", None)
        self.__b_Definition81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_LogicalExpr"):
                opp_val = getattr(old_value, "b_LogicalExpr", None)
                if opp_val == self:
                    setattr(old_value, "b_LogicalExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_LogicalExpr"):
                opp_val = getattr(value, "b_LogicalExpr", None)
                setattr(value, "b_LogicalExpr", self)

    @property
    def b_Definition78(self):
        return self.__b_Definition78

    @b_Definition78.setter
    def b_Definition78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Definition__b_Definition78", None)
        self.__b_Definition78 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "b_Variable79"):
                    opp_val = getattr(item, "b_Variable79", None)
                    
                    if opp_val == self:
                        setattr(item, "b_Variable79", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "b_Variable79"):
                    opp_val = getattr(item, "b_Variable79", None)
                    
                    setattr(item, "b_Variable79", self)
                    

    @property
    def b_Definition83(self):
        return self.__b_Definition83

    @b_Definition83.setter
    def b_Definition83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Definition__b_Definition83", None)
        self.__b_Definition83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_DefinitionCall"):
                opp_val = getattr(old_value, "b_DefinitionCall", None)
                if opp_val == self:
                    setattr(old_value, "b_DefinitionCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_DefinitionCall"):
                opp_val = getattr(value, "b_DefinitionCall", None)
                setattr(value, "b_DefinitionCall", self)

class b_Set:

    pass
class b_Range:

    def __init__(self, lowerBound: int, b_Range: "b_Variable" = None, b_Range173: "b_PropertyRange" = None):
        self.lowerBound = lowerBound
        self.b_Range = b_Range
        self.b_Range173 = b_Range173
        
    @property
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

    @property
    def b_Range(self):
        return self.__b_Range

    @b_Range.setter
    def b_Range(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Range__b_Range", None)
        self.__b_Range = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_Variable66"):
                opp_val = getattr(old_value, "b_Variable66", None)
                if opp_val == self:
                    setattr(old_value, "b_Variable66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_Variable66"):
                opp_val = getattr(value, "b_Variable66", None)
                setattr(value, "b_Variable66", self)

    @property
    def b_Range173(self):
        return self.__b_Range173

    @b_Range173.setter
    def b_Range173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Range__b_Range173", None)
        self.__b_Range173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_PropertyRange"):
                opp_val = getattr(old_value, "b_PropertyRange", None)
                if opp_val == self:
                    setattr(old_value, "b_PropertyRange", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_PropertyRange"):
                opp_val = getattr(value, "b_PropertyRange", None)
                setattr(value, "b_PropertyRange", self)

class b_AssertionExpr:

    pass
class b_InitialisationExpr:

    pass
class b_Type:

    pass
class b_InvariantExpr:

    pass
class b_Variable:

    def __init__(self, name: str, b_Variable53: "b_InitialisationExpr" = None, b_Variable: "b_ValueExpr" = None, b_Variable38: "b_ConcreteVariables" = None, b_Variable41: "b_ConcreteConstants" = None, b_Variable46: "b_InvariantExpr" = None, b_Variable64: "b_PropertyExpr" = None, b_Variable66: "b_Range" = None, b_Variable90: "b_Set" = None, b_Variable93: "b_Set" = None, b_Variable71: "b_AssertionExpr" = None, b_Variable79: "b_Definition" = None, b_Variable118: "b_PreExpr" = None, b_Variable123: "b_Var" = None, b_Variable98: "b_Operation" = None, b_Variable101: "b_Operation" = None, b_Variable150: "b_Call" = None, b_Variable128: "b_Assign" = None, b_Variable132: "b_ReturnTypeExpr" = None, b_Variable137: "b_Case" = None, b_Variable142: "b_CaseExpr" = None, b_Variable166: "b_Ref" = None, b_Variable169: "b_Ref" = None, b_Variable196: "b_TypeConstraint" = None, b_Variable220: "b_ReturnTuple" = None):
        self.name = name
        self.b_Variable53 = b_Variable53
        self.b_Variable = b_Variable
        self.b_Variable38 = b_Variable38
        self.b_Variable41 = b_Variable41
        self.b_Variable46 = b_Variable46
        self.b_Variable64 = b_Variable64
        self.b_Variable66 = b_Variable66
        self.b_Variable90 = b_Variable90
        self.b_Variable93 = b_Variable93
        self.b_Variable71 = b_Variable71
        self.b_Variable79 = b_Variable79
        self.b_Variable118 = b_Variable118
        self.b_Variable123 = b_Variable123
        self.b_Variable98 = b_Variable98
        self.b_Variable101 = b_Variable101
        self.b_Variable150 = b_Variable150
        self.b_Variable128 = b_Variable128
        self.b_Variable132 = b_Variable132
        self.b_Variable137 = b_Variable137
        self.b_Variable142 = b_Variable142
        self.b_Variable166 = b_Variable166
        self.b_Variable169 = b_Variable169
        self.b_Variable196 = b_Variable196
        self.b_Variable220 = b_Variable220
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def b_Variable71(self):
        return self.__b_Variable71

    @b_Variable71.setter
    def b_Variable71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Variable__b_Variable71", None)
        self.__b_Variable71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_AssertionExpr70"):
                opp_val = getattr(old_value, "b_AssertionExpr70", None)
                if opp_val == self:
                    setattr(old_value, "b_AssertionExpr70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_AssertionExpr70"):
                opp_val = getattr(value, "b_AssertionExpr70", None)
                setattr(value, "b_AssertionExpr70", self)

    @property
    def b_Variable196(self):
        return self.__b_Variable196

    @b_Variable196.setter
    def b_Variable196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Variable__b_Variable196", None)
        self.__b_Variable196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_TypeConstraint"):
                opp_val = getattr(old_value, "b_TypeConstraint", None)
                if opp_val == self:
                    setattr(old_value, "b_TypeConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_TypeConstraint"):
                opp_val = getattr(value, "b_TypeConstraint", None)
                setattr(value, "b_TypeConstraint", self)

    @property
    def b_Variable166(self):
        return self.__b_Variable166

    @b_Variable166.setter
    def b_Variable166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Variable__b_Variable166", None)
        self.__b_Variable166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_Ref"):
                opp_val = getattr(old_value, "b_Ref", None)
                if opp_val == self:
                    setattr(old_value, "b_Ref", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_Ref"):
                opp_val = getattr(value, "b_Ref", None)
                setattr(value, "b_Ref", self)

    @property
    def b_Variable46(self):
        return self.__b_Variable46

    @b_Variable46.setter
    def b_Variable46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Variable__b_Variable46", None)
        self.__b_Variable46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_InvariantExpr45"):
                opp_val = getattr(old_value, "b_InvariantExpr45", None)
                if opp_val == self:
                    setattr(old_value, "b_InvariantExpr45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_InvariantExpr45"):
                opp_val = getattr(value, "b_InvariantExpr45", None)
                setattr(value, "b_InvariantExpr45", self)

    @property
    def b_Variable132(self):
        return self.__b_Variable132

    @b_Variable132.setter
    def b_Variable132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Variable__b_Variable132", None)
        self.__b_Variable132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_ReturnTypeExpr"):
                opp_val = getattr(old_value, "b_ReturnTypeExpr", None)
                if opp_val == self:
                    setattr(old_value, "b_ReturnTypeExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_ReturnTypeExpr"):
                opp_val = getattr(value, "b_ReturnTypeExpr", None)
                setattr(value, "b_ReturnTypeExpr", self)

    @property
    def b_Variable41(self):
        return self.__b_Variable41

    @b_Variable41.setter
    def b_Variable41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Variable__b_Variable41", None)
        self.__b_Variable41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_ConcreteConstants40"):
                opp_val = getattr(old_value, "b_ConcreteConstants40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_ConcreteConstants40"):
                opp_val = getattr(value, "b_ConcreteConstants40", None)
                if opp_val is None:
                    setattr(value, "b_ConcreteConstants40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def b_Variable64(self):
        return self.__b_Variable64

    @b_Variable64.setter
    def b_Variable64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Variable__b_Variable64", None)
        self.__b_Variable64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_PropertyExpr63"):
                opp_val = getattr(old_value, "b_PropertyExpr63", None)
                if opp_val == self:
                    setattr(old_value, "b_PropertyExpr63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_PropertyExpr63"):
                opp_val = getattr(value, "b_PropertyExpr63", None)
                setattr(value, "b_PropertyExpr63", self)

    @property
    def b_Variable150(self):
        return self.__b_Variable150

    @b_Variable150.setter
    def b_Variable150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Variable__b_Variable150", None)
        self.__b_Variable150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_Call"):
                opp_val = getattr(old_value, "b_Call", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_Call"):
                opp_val = getattr(value, "b_Call", None)
                if opp_val is None:
                    setattr(value, "b_Call", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def b_Variable137(self):
        return self.__b_Variable137

    @b_Variable137.setter
    def b_Variable137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Variable__b_Variable137", None)
        self.__b_Variable137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_Case"):
                opp_val = getattr(old_value, "b_Case", None)
                if opp_val == self:
                    setattr(old_value, "b_Case", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_Case"):
                opp_val = getattr(value, "b_Case", None)
                setattr(value, "b_Case", self)

    @property
    def b_Variable101(self):
        return self.__b_Variable101

    @b_Variable101.setter
    def b_Variable101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Variable__b_Variable101", None)
        self.__b_Variable101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_Operation100"):
                opp_val = getattr(old_value, "b_Operation100", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_Operation100"):
                opp_val = getattr(value, "b_Operation100", None)
                if opp_val is None:
                    setattr(value, "b_Operation100", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def b_Variable118(self):
        return self.__b_Variable118

    @b_Variable118.setter
    def b_Variable118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Variable__b_Variable118", None)
        self.__b_Variable118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_PreExpr117"):
                opp_val = getattr(old_value, "b_PreExpr117", None)
                if opp_val == self:
                    setattr(old_value, "b_PreExpr117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_PreExpr117"):
                opp_val = getattr(value, "b_PreExpr117", None)
                setattr(value, "b_PreExpr117", self)

    @property
    def b_Variable123(self):
        return self.__b_Variable123

    @b_Variable123.setter
    def b_Variable123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Variable__b_Variable123", None)
        self.__b_Variable123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_Var"):
                opp_val = getattr(old_value, "b_Var", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_Var"):
                opp_val = getattr(value, "b_Var", None)
                if opp_val is None:
                    setattr(value, "b_Var", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def b_Variable38(self):
        return self.__b_Variable38

    @b_Variable38.setter
    def b_Variable38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Variable__b_Variable38", None)
        self.__b_Variable38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_ConcreteVariables37"):
                opp_val = getattr(old_value, "b_ConcreteVariables37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_ConcreteVariables37"):
                opp_val = getattr(value, "b_ConcreteVariables37", None)
                if opp_val is None:
                    setattr(value, "b_ConcreteVariables37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def b_Variable220(self):
        return self.__b_Variable220

    @b_Variable220.setter
    def b_Variable220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Variable__b_Variable220", None)
        self.__b_Variable220 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_ReturnTuple"):
                opp_val = getattr(old_value, "b_ReturnTuple", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_ReturnTuple"):
                opp_val = getattr(value, "b_ReturnTuple", None)
                if opp_val is None:
                    setattr(value, "b_ReturnTuple", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def b_Variable53(self):
        return self.__b_Variable53

    @b_Variable53.setter
    def b_Variable53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Variable__b_Variable53", None)
        self.__b_Variable53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_InitialisationExpr52"):
                opp_val = getattr(old_value, "b_InitialisationExpr52", None)
                if opp_val == self:
                    setattr(old_value, "b_InitialisationExpr52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_InitialisationExpr52"):
                opp_val = getattr(value, "b_InitialisationExpr52", None)
                setattr(value, "b_InitialisationExpr52", self)

    @property
    def b_Variable93(self):
        return self.__b_Variable93

    @b_Variable93.setter
    def b_Variable93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Variable__b_Variable93", None)
        self.__b_Variable93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_Set92"):
                opp_val = getattr(old_value, "b_Set92", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_Set92"):
                opp_val = getattr(value, "b_Set92", None)
                if opp_val is None:
                    setattr(value, "b_Set92", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def b_Variable169(self):
        return self.__b_Variable169

    @b_Variable169.setter
    def b_Variable169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Variable__b_Variable169", None)
        self.__b_Variable169 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_Ref168"):
                opp_val = getattr(old_value, "b_Ref168", None)
                if opp_val == self:
                    setattr(old_value, "b_Ref168", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_Ref168"):
                opp_val = getattr(value, "b_Ref168", None)
                setattr(value, "b_Ref168", self)

    @property
    def b_Variable90(self):
        return self.__b_Variable90

    @b_Variable90.setter
    def b_Variable90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Variable__b_Variable90", None)
        self.__b_Variable90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_Set89"):
                opp_val = getattr(old_value, "b_Set89", None)
                if opp_val == self:
                    setattr(old_value, "b_Set89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_Set89"):
                opp_val = getattr(value, "b_Set89", None)
                setattr(value, "b_Set89", self)

    @property
    def b_Variable79(self):
        return self.__b_Variable79

    @b_Variable79.setter
    def b_Variable79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Variable__b_Variable79", None)
        self.__b_Variable79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_Definition78"):
                opp_val = getattr(old_value, "b_Definition78", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_Definition78"):
                opp_val = getattr(value, "b_Definition78", None)
                if opp_val is None:
                    setattr(value, "b_Definition78", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def b_Variable(self):
        return self.__b_Variable

    @b_Variable.setter
    def b_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Variable__b_Variable", None)
        self.__b_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_ValueExpr35"):
                opp_val = getattr(old_value, "b_ValueExpr35", None)
                if opp_val == self:
                    setattr(old_value, "b_ValueExpr35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_ValueExpr35"):
                opp_val = getattr(value, "b_ValueExpr35", None)
                setattr(value, "b_ValueExpr35", self)

    @property
    def b_Variable128(self):
        return self.__b_Variable128

    @b_Variable128.setter
    def b_Variable128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Variable__b_Variable128", None)
        self.__b_Variable128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_Assign"):
                opp_val = getattr(old_value, "b_Assign", None)
                if opp_val == self:
                    setattr(old_value, "b_Assign", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_Assign"):
                opp_val = getattr(value, "b_Assign", None)
                setattr(value, "b_Assign", self)

    @property
    def b_Variable66(self):
        return self.__b_Variable66

    @b_Variable66.setter
    def b_Variable66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Variable__b_Variable66", None)
        self.__b_Variable66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_Range"):
                opp_val = getattr(old_value, "b_Range", None)
                if opp_val == self:
                    setattr(old_value, "b_Range", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_Range"):
                opp_val = getattr(value, "b_Range", None)
                setattr(value, "b_Range", self)

    @property
    def b_Variable98(self):
        return self.__b_Variable98

    @b_Variable98.setter
    def b_Variable98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Variable__b_Variable98", None)
        self.__b_Variable98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_Operation97"):
                opp_val = getattr(old_value, "b_Operation97", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_Operation97"):
                opp_val = getattr(value, "b_Operation97", None)
                if opp_val is None:
                    setattr(value, "b_Operation97", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def b_Variable142(self):
        return self.__b_Variable142

    @b_Variable142.setter
    def b_Variable142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Variable__b_Variable142", None)
        self.__b_Variable142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_CaseExpr141"):
                opp_val = getattr(old_value, "b_CaseExpr141", None)
                if opp_val == self:
                    setattr(old_value, "b_CaseExpr141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_CaseExpr141"):
                opp_val = getattr(value, "b_CaseExpr141", None)
                setattr(value, "b_CaseExpr141", self)

class b_ValueExpr:

    def __init__(self, value: str, b_ValueExpr: "b_Values" = None, b_ValueExpr35: "b_Variable" = None):
        self.value = value
        self.b_ValueExpr = b_ValueExpr
        self.b_ValueExpr35 = b_ValueExpr35
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def b_ValueExpr(self):
        return self.__b_ValueExpr

    @b_ValueExpr.setter
    def b_ValueExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_ValueExpr__b_ValueExpr", None)
        self.__b_ValueExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_Values33"):
                opp_val = getattr(old_value, "b_Values33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_Values33"):
                opp_val = getattr(value, "b_Values33", None)
                if opp_val is None:
                    setattr(value, "b_Values33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def b_ValueExpr35(self):
        return self.__b_ValueExpr35

    @b_ValueExpr35.setter
    def b_ValueExpr35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_ValueExpr__b_ValueExpr35", None)
        self.__b_ValueExpr35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_Variable"):
                opp_val = getattr(old_value, "b_Variable", None)
                if opp_val == self:
                    setattr(old_value, "b_Variable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_Variable"):
                opp_val = getattr(value, "b_Variable", None)
                setattr(value, "b_Variable", self)

class b_PropertyExpr:

    pass
class b_Sets:

    pass
class b_Assertions:

    pass
class b_Initialisation:

    pass
class b_Invariant:

    pass
class b_ConcreteVariables:

    pass
class Abstraction:

    pass
class b_Implementation(Abstraction):

    pass
class b_Machine(Abstraction):

    pass
class b_Operations:

    pass
class b_Properties:

    pass
class b_Definitions:

    pass
class b_ConcreteConstants:

    pass
class b_Sees:

    pass
class b_Abstraction:

    def __init__(self, name: str, b_Abstraction28: "b_Sees" = None, b_Abstraction: "b_Sees" = None, b_Abstraction2: "b_ConcreteConstants" = None, b_Abstraction4: "b_Definitions" = None, b_Abstraction6: "b_Properties" = None, b_Abstraction8: "b_Operations" = None, b_Abstraction31: "b_Imports" = None):
        self.name = name
        self.b_Abstraction28 = b_Abstraction28
        self.b_Abstraction = b_Abstraction
        self.b_Abstraction2 = b_Abstraction2
        self.b_Abstraction4 = b_Abstraction4
        self.b_Abstraction6 = b_Abstraction6
        self.b_Abstraction8 = b_Abstraction8
        self.b_Abstraction31 = b_Abstraction31
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def b_Abstraction4(self):
        return self.__b_Abstraction4

    @b_Abstraction4.setter
    def b_Abstraction4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Abstraction__b_Abstraction4", None)
        self.__b_Abstraction4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_Definitions"):
                opp_val = getattr(old_value, "b_Definitions", None)
                if opp_val == self:
                    setattr(old_value, "b_Definitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_Definitions"):
                opp_val = getattr(value, "b_Definitions", None)
                setattr(value, "b_Definitions", self)

    @property
    def b_Abstraction31(self):
        return self.__b_Abstraction31

    @b_Abstraction31.setter
    def b_Abstraction31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Abstraction__b_Abstraction31", None)
        self.__b_Abstraction31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_Imports30"):
                opp_val = getattr(old_value, "b_Imports30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_Imports30"):
                opp_val = getattr(value, "b_Imports30", None)
                if opp_val is None:
                    setattr(value, "b_Imports30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def b_Abstraction6(self):
        return self.__b_Abstraction6

    @b_Abstraction6.setter
    def b_Abstraction6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Abstraction__b_Abstraction6", None)
        self.__b_Abstraction6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_Properties"):
                opp_val = getattr(old_value, "b_Properties", None)
                if opp_val == self:
                    setattr(old_value, "b_Properties", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_Properties"):
                opp_val = getattr(value, "b_Properties", None)
                setattr(value, "b_Properties", self)

    @property
    def b_Abstraction2(self):
        return self.__b_Abstraction2

    @b_Abstraction2.setter
    def b_Abstraction2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Abstraction__b_Abstraction2", None)
        self.__b_Abstraction2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_ConcreteConstants"):
                opp_val = getattr(old_value, "b_ConcreteConstants", None)
                if opp_val == self:
                    setattr(old_value, "b_ConcreteConstants", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_ConcreteConstants"):
                opp_val = getattr(value, "b_ConcreteConstants", None)
                setattr(value, "b_ConcreteConstants", self)

    @property
    def b_Abstraction28(self):
        return self.__b_Abstraction28

    @b_Abstraction28.setter
    def b_Abstraction28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Abstraction__b_Abstraction28", None)
        self.__b_Abstraction28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_Sees27"):
                opp_val = getattr(old_value, "b_Sees27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_Sees27"):
                opp_val = getattr(value, "b_Sees27", None)
                if opp_val is None:
                    setattr(value, "b_Sees27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def b_Abstraction(self):
        return self.__b_Abstraction

    @b_Abstraction.setter
    def b_Abstraction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Abstraction__b_Abstraction", None)
        self.__b_Abstraction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_Sees"):
                opp_val = getattr(old_value, "b_Sees", None)
                if opp_val == self:
                    setattr(old_value, "b_Sees", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_Sees"):
                opp_val = getattr(value, "b_Sees", None)
                setattr(value, "b_Sees", self)

    @property
    def b_Abstraction8(self):
        return self.__b_Abstraction8

    @b_Abstraction8.setter
    def b_Abstraction8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Abstraction__b_Abstraction8", None)
        self.__b_Abstraction8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_Operations"):
                opp_val = getattr(old_value, "b_Operations", None)
                if opp_val == self:
                    setattr(old_value, "b_Operations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_Operations"):
                opp_val = getattr(value, "b_Operations", None)
                setattr(value, "b_Operations", self)

class b_LocalOperations:

    pass
class b_Values:

    pass
class b_Imports:

    pass