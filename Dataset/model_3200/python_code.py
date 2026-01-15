from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class IntegerComparisonOperator(Enum):
    GREATER = "GREATER"
    SMALLER = "SMALLER"
    SMALLER_EQUALS = "SMALLER_EQUALS"
    EQUALS = "EQUALS"
    GREATER_EQUALS = "GREATER_EQUALS"
class BooleanBinaryOperator(Enum):
    AND = "AND"
    OR = "OR"
class ParameterMode(Enum):
    PARAM_IN = "PARAM_IN"
    PARAM_OUT = "PARAM_OUT"
    PARAM_INOUT = "PARAM_INOUT"
class BoardType(Enum):
    RaspberryPi = "RaspberryPi"
    Arduino = "Arduino"
    BeagleBoard = "BeagleBoard"
class IntegerCalculationOperator(Enum):
    ADD = "ADD"
    SUBRACT = "SUBRACT"
class BooleanUnaryOperator(Enum):
    NOT = "NOT"
class PrimitiveKind(Enum):
    PK_OCTET = "PK_OCTET"
    PK_ANY = "PK_ANY"
    PK_LONGDOUBLE = "PK_LONGDOUBLE"
    PK_WSTRING = "PK_WSTRING"
    PK_NULL = "PK_NULL"
    PK_VOID = "PK_VOID"
    PK_SHORT = "PK_SHORT"
    PK_LONG = "PK_LONG"
    PK_USHORT = "PK_USHORT"
    PK_ULONG = "PK_ULONG"
    PK_FLOAT = "PK_FLOAT"
    PK_DOUBLE = "PK_DOUBLE"
    PK_BOOLEAN = "PK_BOOLEAN"
    PK_CHAR = "PK_CHAR"
    PK_TYPECODE = "PK_TYPECODE"
    PK_WCHAR = "PK_WCHAR"
    PK_PRINCIPAL = "PK_PRINCIPAL"
    PK_STRING = "PK_STRING"
    PK_ULONGLONG = "PK_ULONGLONG"
    PK_OBJREF = "PK_OBJREF"
    PK_LONGLONG = "PK_LONGLONG"


############################################
# Definition of Classes
############################################

class Token:

    pass
class iot2_ControlToken(Token):

    pass
class iot2_ForkedToken(Token):

    def __init__(self, remainingOffersCount: str, iot2_ForkedToken: "iot2_Token" = None):
        self.remainingOffersCount = remainingOffersCount
        self.iot2_ForkedToken = iot2_ForkedToken
        
    @property
    def remainingOffersCount(self) -> str:
        return self.__remainingOffersCount

    @remainingOffersCount.setter
    def remainingOffersCount(self, remainingOffersCount: str):
        self.__remainingOffersCount = remainingOffersCount

    @property
    def iot2_ForkedToken(self):
        return self.__iot2_ForkedToken

    @iot2_ForkedToken.setter
    def iot2_ForkedToken(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ForkedToken__iot2_ForkedToken", None)
        self.__iot2_ForkedToken = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Token293"):
                opp_val = getattr(old_value, "iot2_Token293", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Token293", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Token293"):
                opp_val = getattr(value, "iot2_Token293", None)
                setattr(value, "iot2_Token293", self)

class iot2_Trace:

    pass
class iot2_Context:

    pass
class iot2_Token:

    def __init__(self, iot2_Token: "iot2_Offer" = None, iot2_Token276: "iot2_ActivityNode" = None, iot2_Token293: "iot2_ForkedToken" = None):
        self.iot2_Token = iot2_Token
        self.iot2_Token276 = iot2_Token276
        self.iot2_Token293 = iot2_Token293
        
    @property
    def iot2_Token(self):
        return self.__iot2_Token

    @iot2_Token.setter
    def iot2_Token(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Token__iot2_Token", None)
        self.__iot2_Token = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Offer274"):
                opp_val = getattr(old_value, "iot2_Offer274", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Offer274"):
                opp_val = getattr(value, "iot2_Offer274", None)
                if opp_val is None:
                    setattr(value, "iot2_Offer274", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_Token293(self):
        return self.__iot2_Token293

    @iot2_Token293.setter
    def iot2_Token293(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Token__iot2_Token293", None)
        self.__iot2_Token293 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_ForkedToken"):
                opp_val = getattr(old_value, "iot2_ForkedToken", None)
                if opp_val == self:
                    setattr(old_value, "iot2_ForkedToken", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_ForkedToken"):
                opp_val = getattr(value, "iot2_ForkedToken", None)
                setattr(value, "iot2_ForkedToken", self)

    @property
    def iot2_Token276(self):
        return self.__iot2_Token276

    @iot2_Token276.setter
    def iot2_Token276(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Token__iot2_Token276", None)
        self.__iot2_Token276 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_ActivityNode"):
                opp_val = getattr(old_value, "iot2_ActivityNode", None)
                if opp_val == self:
                    setattr(old_value, "iot2_ActivityNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_ActivityNode"):
                opp_val = getattr(value, "iot2_ActivityNode", None)
                setattr(value, "iot2_ActivityNode", self)

    def isWithdrawn(self):
        # TODO: Implement isWithdrawn method
        pass

    def transfer(self, holder: ActivityNode) -> str:
        # TODO: Implement transfer method
        pass

    def withdraw(self):
        # TODO: Implement withdraw method
        pass

class iot2_Input:

    pass
class iot2_InputValue:

    pass
class IntegerExpression:

    pass
class iot2_IntegerComparisonExpression(IntegerExpression):

    def __init__(self, operator: str, iot2_IntegerComparisonExpression: "iot2_BooleanVariable" = None):
        self.operator = operator
        self.iot2_IntegerComparisonExpression = iot2_IntegerComparisonExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def iot2_IntegerComparisonExpression(self):
        return self.__iot2_IntegerComparisonExpression

    @iot2_IntegerComparisonExpression.setter
    def iot2_IntegerComparisonExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_IntegerComparisonExpression__iot2_IntegerComparisonExpression", None)
        self.__iot2_IntegerComparisonExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_BooleanVariable258"):
                opp_val = getattr(old_value, "iot2_BooleanVariable258", None)
                if opp_val == self:
                    setattr(old_value, "iot2_BooleanVariable258", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_BooleanVariable258"):
                opp_val = getattr(value, "iot2_BooleanVariable258", None)
                setattr(value, "iot2_BooleanVariable258", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_IntegerCalculationExpression(IntegerExpression):

    def __init__(self, operator: str, iot2_IntegerCalculationExpression: "iot2_IntegerVariable" = None):
        self.operator = operator
        self.iot2_IntegerCalculationExpression = iot2_IntegerCalculationExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def iot2_IntegerCalculationExpression(self):
        return self.__iot2_IntegerCalculationExpression

    @iot2_IntegerCalculationExpression.setter
    def iot2_IntegerCalculationExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_IntegerCalculationExpression__iot2_IntegerCalculationExpression", None)
        self.__iot2_IntegerCalculationExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_IntegerVariable256"):
                opp_val = getattr(old_value, "iot2_IntegerVariable256", None)
                if opp_val == self:
                    setattr(old_value, "iot2_IntegerVariable256", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_IntegerVariable256"):
                opp_val = getattr(value, "iot2_IntegerVariable256", None)
                setattr(value, "iot2_IntegerVariable256", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class BooleanExpression:

    pass
class iot2_BooleanBinaryExpression(BooleanExpression):

    def __init__(self, operator: bool, iot2_BooleanBinaryExpression: "iot2_BooleanVariable" = None, iot2_BooleanBinaryExpression264: "iot2_BooleanVariable" = None):
        self.operator = operator
        self.iot2_BooleanBinaryExpression = iot2_BooleanBinaryExpression
        self.iot2_BooleanBinaryExpression264 = iot2_BooleanBinaryExpression264
        
    @property
    def operator(self) -> bool:
        return self.__operator

    @operator.setter
    def operator(self, operator: bool):
        self.__operator = operator

    @property
    def iot2_BooleanBinaryExpression(self):
        return self.__iot2_BooleanBinaryExpression

    @iot2_BooleanBinaryExpression.setter
    def iot2_BooleanBinaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_BooleanBinaryExpression__iot2_BooleanBinaryExpression", None)
        self.__iot2_BooleanBinaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_BooleanVariable262"):
                opp_val = getattr(old_value, "iot2_BooleanVariable262", None)
                if opp_val == self:
                    setattr(old_value, "iot2_BooleanVariable262", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_BooleanVariable262"):
                opp_val = getattr(value, "iot2_BooleanVariable262", None)
                setattr(value, "iot2_BooleanVariable262", self)

    @property
    def iot2_BooleanBinaryExpression264(self):
        return self.__iot2_BooleanBinaryExpression264

    @iot2_BooleanBinaryExpression264.setter
    def iot2_BooleanBinaryExpression264(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_BooleanBinaryExpression__iot2_BooleanBinaryExpression264", None)
        self.__iot2_BooleanBinaryExpression264 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_BooleanVariable265"):
                opp_val = getattr(old_value, "iot2_BooleanVariable265", None)
                if opp_val == self:
                    setattr(old_value, "iot2_BooleanVariable265", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_BooleanVariable265"):
                opp_val = getattr(value, "iot2_BooleanVariable265", None)
                setattr(value, "iot2_BooleanVariable265", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_BooleanUnaryExpression(BooleanExpression):

    def __init__(self, operator: str, iot2_BooleanUnaryExpression: "iot2_BooleanVariable" = None):
        self.operator = operator
        self.iot2_BooleanUnaryExpression = iot2_BooleanUnaryExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def iot2_BooleanUnaryExpression(self):
        return self.__iot2_BooleanUnaryExpression

    @iot2_BooleanUnaryExpression.setter
    def iot2_BooleanUnaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_BooleanUnaryExpression__iot2_BooleanUnaryExpression", None)
        self.__iot2_BooleanUnaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_BooleanVariable260"):
                opp_val = getattr(old_value, "iot2_BooleanVariable260", None)
                if opp_val == self:
                    setattr(old_value, "iot2_BooleanVariable260", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_BooleanVariable260"):
                opp_val = getattr(value, "iot2_BooleanVariable260", None)
                setattr(value, "iot2_BooleanVariable260", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class Value:

    pass
class iot2_BooleanValue(Value):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class Variable:

    pass
class iot2_IntegerVariable(Variable):

    def __init__(self, iot2_IntegerVariable: "iot2_IntegerExpression" = None, iot2_IntegerVariable252: "iot2_IntegerExpression" = None, iot2_IntegerVariable256: "iot2_IntegerCalculationExpression" = None):
        self.iot2_IntegerVariable = iot2_IntegerVariable
        self.iot2_IntegerVariable252 = iot2_IntegerVariable252
        self.iot2_IntegerVariable256 = iot2_IntegerVariable256
        
    @property
    def iot2_IntegerVariable(self):
        return self.__iot2_IntegerVariable

    @iot2_IntegerVariable.setter
    def iot2_IntegerVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_IntegerVariable__iot2_IntegerVariable", None)
        self.__iot2_IntegerVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_IntegerExpression"):
                opp_val = getattr(old_value, "iot2_IntegerExpression", None)
                if opp_val == self:
                    setattr(old_value, "iot2_IntegerExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_IntegerExpression"):
                opp_val = getattr(value, "iot2_IntegerExpression", None)
                setattr(value, "iot2_IntegerExpression", self)

    @property
    def iot2_IntegerVariable256(self):
        return self.__iot2_IntegerVariable256

    @iot2_IntegerVariable256.setter
    def iot2_IntegerVariable256(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_IntegerVariable__iot2_IntegerVariable256", None)
        self.__iot2_IntegerVariable256 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_IntegerCalculationExpression"):
                opp_val = getattr(old_value, "iot2_IntegerCalculationExpression", None)
                if opp_val == self:
                    setattr(old_value, "iot2_IntegerCalculationExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_IntegerCalculationExpression"):
                opp_val = getattr(value, "iot2_IntegerCalculationExpression", None)
                setattr(value, "iot2_IntegerCalculationExpression", self)

    @property
    def iot2_IntegerVariable252(self):
        return self.__iot2_IntegerVariable252

    @iot2_IntegerVariable252.setter
    def iot2_IntegerVariable252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_IntegerVariable__iot2_IntegerVariable252", None)
        self.__iot2_IntegerVariable252 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_IntegerExpression251"):
                opp_val = getattr(old_value, "iot2_IntegerExpression251", None)
                if opp_val == self:
                    setattr(old_value, "iot2_IntegerExpression251", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_IntegerExpression251"):
                opp_val = getattr(value, "iot2_IntegerExpression251", None)
                setattr(value, "iot2_IntegerExpression251", self)

    def print(self):
        # TODO: Implement print method
        pass

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Value:

    pass
class iot2_IntegerValue(Value):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class FinalNode:

    pass
class iot2_ActivityFinalNode(FinalNode):

    def __init__(self):
        
    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class Action:

    pass
class iot2_OpaqueAction(Action):

    def __init__(self, iot2_OpaqueAction: set["iot2_Expression"] = None, iot2_OpaqueAction242: "iot2_OperationDef" = None):
        self.iot2_OpaqueAction = iot2_OpaqueAction if iot2_OpaqueAction is not None else set()
        self.iot2_OpaqueAction242 = iot2_OpaqueAction242
        
    @property
    def iot2_OpaqueAction242(self):
        return self.__iot2_OpaqueAction242

    @iot2_OpaqueAction242.setter
    def iot2_OpaqueAction242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_OpaqueAction__iot2_OpaqueAction242", None)
        self.__iot2_OpaqueAction242 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_OperationDef243"):
                opp_val = getattr(old_value, "iot2_OperationDef243", None)
                if opp_val == self:
                    setattr(old_value, "iot2_OperationDef243", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_OperationDef243"):
                opp_val = getattr(value, "iot2_OperationDef243", None)
                setattr(value, "iot2_OperationDef243", self)

    @property
    def iot2_OpaqueAction(self):
        return self.__iot2_OpaqueAction

    @iot2_OpaqueAction.setter
    def iot2_OpaqueAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_OpaqueAction__iot2_OpaqueAction", None)
        self.__iot2_OpaqueAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_Expression240"):
                    opp_val = getattr(item, "iot2_Expression240", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_Expression240", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_Expression240"):
                    opp_val = getattr(item, "iot2_Expression240", None)
                    
                    setattr(item, "iot2_Expression240", self)
                    

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

    def getValueAsString(self, v: str):
        # TODO: Implement getValueAsString method
        pass

class ExecutableNode:

    pass
class iot2_Action(ExecutableNode):

    pass
class ActivityNode:

    pass
class iot2_ExecutableNode(ActivityNode):

    pass
class iot2_ControlNode(ActivityNode):

    pass
class iot2_BooleanVariable(Variable):

    def __init__(self, iot2_BooleanVariable: "iot2_ControlFlow" = None, iot2_BooleanVariable254: "iot2_BooleanExpression" = None, iot2_BooleanVariable258: "iot2_IntegerComparisonExpression" = None, iot2_BooleanVariable260: "iot2_BooleanUnaryExpression" = None, iot2_BooleanVariable262: "iot2_BooleanBinaryExpression" = None, iot2_BooleanVariable265: "iot2_BooleanBinaryExpression" = None):
        self.iot2_BooleanVariable = iot2_BooleanVariable
        self.iot2_BooleanVariable254 = iot2_BooleanVariable254
        self.iot2_BooleanVariable258 = iot2_BooleanVariable258
        self.iot2_BooleanVariable260 = iot2_BooleanVariable260
        self.iot2_BooleanVariable262 = iot2_BooleanVariable262
        self.iot2_BooleanVariable265 = iot2_BooleanVariable265
        
    @property
    def iot2_BooleanVariable260(self):
        return self.__iot2_BooleanVariable260

    @iot2_BooleanVariable260.setter
    def iot2_BooleanVariable260(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_BooleanVariable__iot2_BooleanVariable260", None)
        self.__iot2_BooleanVariable260 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_BooleanUnaryExpression"):
                opp_val = getattr(old_value, "iot2_BooleanUnaryExpression", None)
                if opp_val == self:
                    setattr(old_value, "iot2_BooleanUnaryExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_BooleanUnaryExpression"):
                opp_val = getattr(value, "iot2_BooleanUnaryExpression", None)
                setattr(value, "iot2_BooleanUnaryExpression", self)

    @property
    def iot2_BooleanVariable262(self):
        return self.__iot2_BooleanVariable262

    @iot2_BooleanVariable262.setter
    def iot2_BooleanVariable262(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_BooleanVariable__iot2_BooleanVariable262", None)
        self.__iot2_BooleanVariable262 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_BooleanBinaryExpression"):
                opp_val = getattr(old_value, "iot2_BooleanBinaryExpression", None)
                if opp_val == self:
                    setattr(old_value, "iot2_BooleanBinaryExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_BooleanBinaryExpression"):
                opp_val = getattr(value, "iot2_BooleanBinaryExpression", None)
                setattr(value, "iot2_BooleanBinaryExpression", self)

    @property
    def iot2_BooleanVariable258(self):
        return self.__iot2_BooleanVariable258

    @iot2_BooleanVariable258.setter
    def iot2_BooleanVariable258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_BooleanVariable__iot2_BooleanVariable258", None)
        self.__iot2_BooleanVariable258 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_IntegerComparisonExpression"):
                opp_val = getattr(old_value, "iot2_IntegerComparisonExpression", None)
                if opp_val == self:
                    setattr(old_value, "iot2_IntegerComparisonExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_IntegerComparisonExpression"):
                opp_val = getattr(value, "iot2_IntegerComparisonExpression", None)
                setattr(value, "iot2_IntegerComparisonExpression", self)

    @property
    def iot2_BooleanVariable265(self):
        return self.__iot2_BooleanVariable265

    @iot2_BooleanVariable265.setter
    def iot2_BooleanVariable265(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_BooleanVariable__iot2_BooleanVariable265", None)
        self.__iot2_BooleanVariable265 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_BooleanBinaryExpression264"):
                opp_val = getattr(old_value, "iot2_BooleanBinaryExpression264", None)
                if opp_val == self:
                    setattr(old_value, "iot2_BooleanBinaryExpression264", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_BooleanBinaryExpression264"):
                opp_val = getattr(value, "iot2_BooleanBinaryExpression264", None)
                setattr(value, "iot2_BooleanBinaryExpression264", self)

    @property
    def iot2_BooleanVariable254(self):
        return self.__iot2_BooleanVariable254

    @iot2_BooleanVariable254.setter
    def iot2_BooleanVariable254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_BooleanVariable__iot2_BooleanVariable254", None)
        self.__iot2_BooleanVariable254 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_BooleanExpression"):
                opp_val = getattr(old_value, "iot2_BooleanExpression", None)
                if opp_val == self:
                    setattr(old_value, "iot2_BooleanExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_BooleanExpression"):
                opp_val = getattr(value, "iot2_BooleanExpression", None)
                setattr(value, "iot2_BooleanExpression", self)

    @property
    def iot2_BooleanVariable(self):
        return self.__iot2_BooleanVariable

    @iot2_BooleanVariable.setter
    def iot2_BooleanVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_BooleanVariable__iot2_BooleanVariable", None)
        self.__iot2_BooleanVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_ControlFlow"):
                opp_val = getattr(old_value, "iot2_ControlFlow", None)
                if opp_val == self:
                    setattr(old_value, "iot2_ControlFlow", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_ControlFlow"):
                opp_val = getattr(value, "iot2_ControlFlow", None)
                setattr(value, "iot2_ControlFlow", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

    def print(self):
        # TODO: Implement print method
        pass

class ActivityEdge:

    pass
class iot2_ControlFlow(ActivityEdge):

    pass
class iot2_Offer:

    def __init__(self, iot2_Offer: "iot2_ActivityEdge" = None, iot2_Offer274: set["iot2_Token"] = None):
        self.iot2_Offer = iot2_Offer
        self.iot2_Offer274 = iot2_Offer274 if iot2_Offer274 is not None else set()
        
    @property
    def iot2_Offer274(self):
        return self.__iot2_Offer274

    @iot2_Offer274.setter
    def iot2_Offer274(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Offer__iot2_Offer274", None)
        self.__iot2_Offer274 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_Token"):
                    opp_val = getattr(item, "iot2_Token", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_Token", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_Token"):
                    opp_val = getattr(item, "iot2_Token", None)
                    
                    setattr(item, "iot2_Token", self)
                    

    @property
    def iot2_Offer(self):
        return self.__iot2_Offer

    @iot2_Offer.setter
    def iot2_Offer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Offer__iot2_Offer", None)
        self.__iot2_Offer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_ActivityEdge237"):
                opp_val = getattr(old_value, "iot2_ActivityEdge237", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_ActivityEdge237"):
                opp_val = getattr(value, "iot2_ActivityEdge237", None)
                if opp_val is None:
                    setattr(value, "iot2_ActivityEdge237", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def hasTokens(self):
        # TODO: Implement hasTokens method
        pass

    def removeWithdrawnTokens(self):
        # TODO: Implement removeWithdrawnTokens method
        pass

class ControlNode:

    pass
class iot2_JoinNode(ControlNode):

    def __init__(self, iot2_JoinNode: "iot2_Context" = None):
        self.iot2_JoinNode = iot2_JoinNode
        
    @property
    def iot2_JoinNode(self):
        return self.__iot2_JoinNode

    @iot2_JoinNode.setter
    def iot2_JoinNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_JoinNode__iot2_JoinNode", None)
        self.__iot2_JoinNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Context288"):
                opp_val = getattr(old_value, "iot2_Context288", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Context288", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Context288"):
                opp_val = getattr(value, "iot2_Context288", None)
                setattr(value, "iot2_Context288", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_MergeNode(ControlNode):

    def __init__(self):
        
    def execute(self, c: str):
        # TODO: Implement execute method
        pass

    def hasOffers(self):
        # TODO: Implement hasOffers method
        pass

class iot2_FinalNode(ControlNode):

    pass
class iot2_DecisionNode(ControlNode):

    def __init__(self):
        
    def sendOffers(self, tokens: str):
        # TODO: Implement sendOffers method
        pass

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_ForkNode(ControlNode):

    def __init__(self):
        
    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_InitialNode(ControlNode):

    def __init__(self):
        
    def hasOffers(self):
        # TODO: Implement hasOffers method
        pass

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Environment:

    def __init__(self, iot2_Environment: "iot2_Environment" = None, iot2_Environment219: "iot2_Environment" = None):
        self.iot2_Environment = iot2_Environment
        self.iot2_Environment219 = iot2_Environment219
        
    @property
    def iot2_Environment219(self):
        return self.__iot2_Environment219

    @iot2_Environment219.setter
    def iot2_Environment219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Environment__iot2_Environment219", None)
        self.__iot2_Environment219 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Environment"):
                opp_val = getattr(old_value, "iot2_Environment", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Environment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Environment"):
                opp_val = getattr(value, "iot2_Environment", None)
                setattr(value, "iot2_Environment", self)

    @property
    def iot2_Environment(self):
        return self.__iot2_Environment

    @iot2_Environment.setter
    def iot2_Environment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Environment__iot2_Environment", None)
        self.__iot2_Environment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Environment219"):
                opp_val = getattr(old_value, "iot2_Environment219", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Environment219", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Environment219"):
                opp_val = getattr(value, "iot2_Environment219", None)
                setattr(value, "iot2_Environment219", self)

    def popValue(self) -> str:
        # TODO: Implement popValue method
        pass

    def putFunction(self, s: str, f: str):
        # TODO: Implement putFunction method
        pass

    def pushValue(self, o: str):
        # TODO: Implement pushValue method
        pass

    def getValues(self) -> str:
        # TODO: Implement getValues method
        pass

    def getVariables(self):
        # TODO: Implement getVariables method
        pass

    def getFunctions(self):
        # TODO: Implement getFunctions method
        pass

    def putAllVariables(self, v: str):
        # TODO: Implement putAllVariables method
        pass

    def putAllFunctions(self, f: str):
        # TODO: Implement putAllFunctions method
        pass

    def putVariable(self, s: str, o: str):
        # TODO: Implement putVariable method
        pass

    def getVariable(self, s: str) -> str:
        # TODO: Implement getVariable method
        pass

    def getFunction(self, s: str) -> str:
        # TODO: Implement getFunction method
        pass

    def pushAllValues(self, v: str):
        # TODO: Implement pushAllValues method
        pass

class LastStatement_Return:

    pass
class iot2_LastStatement_ReturnWithValue(LastStatement_Return):

    def __init__(self, iot2_LastStatement_ReturnWithValue: set["iot2_Expression"] = None):
        self.iot2_LastStatement_ReturnWithValue = iot2_LastStatement_ReturnWithValue if iot2_LastStatement_ReturnWithValue is not None else set()
        
    @property
    def iot2_LastStatement_ReturnWithValue(self):
        return self.__iot2_LastStatement_ReturnWithValue

    @iot2_LastStatement_ReturnWithValue.setter
    def iot2_LastStatement_ReturnWithValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_LastStatement_ReturnWithValue__iot2_LastStatement_ReturnWithValue", None)
        self.__iot2_LastStatement_ReturnWithValue = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_Expression105"):
                    opp_val = getattr(item, "iot2_Expression105", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_Expression105", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_Expression105"):
                    opp_val = getattr(item, "iot2_Expression105", None)
                    
                    setattr(item, "iot2_Expression105", self)
                    

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class Field:

    pass
class iot2_Field_AppendEntryToTable(Field):

    def __init__(self):
        
    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Field_AddEntryToTable(Field):

    def __init__(self, key: str):
        self.key = key
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Field_AddEntryToTable_Brackets(Field):

    def __init__(self, iot2_Field_AddEntryToTable_Brackets: "iot2_Expression" = None):
        self.iot2_Field_AddEntryToTable_Brackets = iot2_Field_AddEntryToTable_Brackets
        
    @property
    def iot2_Field_AddEntryToTable_Brackets(self):
        return self.__iot2_Field_AddEntryToTable_Brackets

    @iot2_Field_AddEntryToTable_Brackets.setter
    def iot2_Field_AddEntryToTable_Brackets(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Field_AddEntryToTable_Brackets__iot2_Field_AddEntryToTable_Brackets", None)
        self.__iot2_Field_AddEntryToTable_Brackets = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression103"):
                opp_val = getattr(old_value, "iot2_Expression103", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression103"):
                opp_val = getattr(value, "iot2_Expression103", None)
                setattr(value, "iot2_Expression103", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Functioncall_Arguments:

    def __init__(self, iot2_Functioncall_Arguments: set["iot2_Expression"] = None, iot2_Functioncall_Arguments115: "iot2_Statement_CallMemberFunction" = None, iot2_Functioncall_Arguments120: "iot2_Statement_CallFunction" = None, iot2_Functioncall_Arguments206: "iot2_Expression_CallMemberFunction" = None, iot2_Functioncall_Arguments211: "iot2_Expression_CallFunction" = None):
        self.iot2_Functioncall_Arguments = iot2_Functioncall_Arguments if iot2_Functioncall_Arguments is not None else set()
        self.iot2_Functioncall_Arguments115 = iot2_Functioncall_Arguments115
        self.iot2_Functioncall_Arguments120 = iot2_Functioncall_Arguments120
        self.iot2_Functioncall_Arguments206 = iot2_Functioncall_Arguments206
        self.iot2_Functioncall_Arguments211 = iot2_Functioncall_Arguments211
        
    @property
    def iot2_Functioncall_Arguments115(self):
        return self.__iot2_Functioncall_Arguments115

    @iot2_Functioncall_Arguments115.setter
    def iot2_Functioncall_Arguments115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Functioncall_Arguments__iot2_Functioncall_Arguments115", None)
        self.__iot2_Functioncall_Arguments115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_CallMemberFunction114"):
                opp_val = getattr(old_value, "iot2_Statement_CallMemberFunction114", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_CallMemberFunction114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_CallMemberFunction114"):
                opp_val = getattr(value, "iot2_Statement_CallMemberFunction114", None)
                setattr(value, "iot2_Statement_CallMemberFunction114", self)

    @property
    def iot2_Functioncall_Arguments211(self):
        return self.__iot2_Functioncall_Arguments211

    @iot2_Functioncall_Arguments211.setter
    def iot2_Functioncall_Arguments211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Functioncall_Arguments__iot2_Functioncall_Arguments211", None)
        self.__iot2_Functioncall_Arguments211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_CallFunction210"):
                opp_val = getattr(old_value, "iot2_Expression_CallFunction210", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_CallFunction210", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_CallFunction210"):
                opp_val = getattr(value, "iot2_Expression_CallFunction210", None)
                setattr(value, "iot2_Expression_CallFunction210", self)

    @property
    def iot2_Functioncall_Arguments(self):
        return self.__iot2_Functioncall_Arguments

    @iot2_Functioncall_Arguments.setter
    def iot2_Functioncall_Arguments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Functioncall_Arguments__iot2_Functioncall_Arguments", None)
        self.__iot2_Functioncall_Arguments = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_Expression101"):
                    opp_val = getattr(item, "iot2_Expression101", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_Expression101", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_Expression101"):
                    opp_val = getattr(item, "iot2_Expression101", None)
                    
                    setattr(item, "iot2_Expression101", self)
                    

    @property
    def iot2_Functioncall_Arguments120(self):
        return self.__iot2_Functioncall_Arguments120

    @iot2_Functioncall_Arguments120.setter
    def iot2_Functioncall_Arguments120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Functioncall_Arguments__iot2_Functioncall_Arguments120", None)
        self.__iot2_Functioncall_Arguments120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_CallFunction119"):
                opp_val = getattr(old_value, "iot2_Statement_CallFunction119", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_CallFunction119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_CallFunction119"):
                opp_val = getattr(value, "iot2_Statement_CallFunction119", None)
                setattr(value, "iot2_Statement_CallFunction119", self)

    @property
    def iot2_Functioncall_Arguments206(self):
        return self.__iot2_Functioncall_Arguments206

    @iot2_Functioncall_Arguments206.setter
    def iot2_Functioncall_Arguments206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Functioncall_Arguments__iot2_Functioncall_Arguments206", None)
        self.__iot2_Functioncall_Arguments206 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_CallMemberFunction205"):
                opp_val = getattr(old_value, "iot2_Expression_CallMemberFunction205", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_CallMemberFunction205", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_CallMemberFunction205"):
                opp_val = getattr(value, "iot2_Expression_CallMemberFunction205", None)
                setattr(value, "iot2_Expression_CallMemberFunction205", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class Expression:

    pass
class iot2_Expression_CallMemberFunction(Expression):

    def __init__(self, memberFunctionName: str, iot2_Expression_CallMemberFunction: "iot2_Expression" = None, iot2_Expression_CallMemberFunction205: "iot2_Functioncall_Arguments" = None):
        self.memberFunctionName = memberFunctionName
        self.iot2_Expression_CallMemberFunction = iot2_Expression_CallMemberFunction
        self.iot2_Expression_CallMemberFunction205 = iot2_Expression_CallMemberFunction205
        
    @property
    def memberFunctionName(self) -> str:
        return self.__memberFunctionName

    @memberFunctionName.setter
    def memberFunctionName(self, memberFunctionName: str):
        self.__memberFunctionName = memberFunctionName

    @property
    def iot2_Expression_CallMemberFunction(self):
        return self.__iot2_Expression_CallMemberFunction

    @iot2_Expression_CallMemberFunction.setter
    def iot2_Expression_CallMemberFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_CallMemberFunction__iot2_Expression_CallMemberFunction", None)
        self.__iot2_Expression_CallMemberFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression203"):
                opp_val = getattr(old_value, "iot2_Expression203", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression203", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression203"):
                opp_val = getattr(value, "iot2_Expression203", None)
                setattr(value, "iot2_Expression203", self)

    @property
    def iot2_Expression_CallMemberFunction205(self):
        return self.__iot2_Expression_CallMemberFunction205

    @iot2_Expression_CallMemberFunction205.setter
    def iot2_Expression_CallMemberFunction205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_CallMemberFunction__iot2_Expression_CallMemberFunction205", None)
        self.__iot2_Expression_CallMemberFunction205 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Functioncall_Arguments206"):
                opp_val = getattr(old_value, "iot2_Functioncall_Arguments206", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Functioncall_Arguments206", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Functioncall_Arguments206"):
                opp_val = getattr(value, "iot2_Functioncall_Arguments206", None)
                setattr(value, "iot2_Functioncall_Arguments206", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Expression_Minus(Expression):

    def __init__(self, iot2_Expression_Minus: "iot2_Expression" = None, iot2_Expression_Minus174: "iot2_Expression" = None):
        self.iot2_Expression_Minus = iot2_Expression_Minus
        self.iot2_Expression_Minus174 = iot2_Expression_Minus174
        
    @property
    def iot2_Expression_Minus174(self):
        return self.__iot2_Expression_Minus174

    @iot2_Expression_Minus174.setter
    def iot2_Expression_Minus174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Minus__iot2_Expression_Minus174", None)
        self.__iot2_Expression_Minus174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression175"):
                opp_val = getattr(old_value, "iot2_Expression175", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression175", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression175"):
                opp_val = getattr(value, "iot2_Expression175", None)
                setattr(value, "iot2_Expression175", self)

    @property
    def iot2_Expression_Minus(self):
        return self.__iot2_Expression_Minus

    @iot2_Expression_Minus.setter
    def iot2_Expression_Minus(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Minus__iot2_Expression_Minus", None)
        self.__iot2_Expression_Minus = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression172"):
                opp_val = getattr(old_value, "iot2_Expression172", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression172"):
                opp_val = getattr(value, "iot2_Expression172", None)
                setattr(value, "iot2_Expression172", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Expression_Plus(Expression):

    def __init__(self, iot2_Expression_Plus: "iot2_Expression" = None, iot2_Expression_Plus169: "iot2_Expression" = None):
        self.iot2_Expression_Plus = iot2_Expression_Plus
        self.iot2_Expression_Plus169 = iot2_Expression_Plus169
        
    @property
    def iot2_Expression_Plus(self):
        return self.__iot2_Expression_Plus

    @iot2_Expression_Plus.setter
    def iot2_Expression_Plus(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Plus__iot2_Expression_Plus", None)
        self.__iot2_Expression_Plus = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression167"):
                opp_val = getattr(old_value, "iot2_Expression167", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression167"):
                opp_val = getattr(value, "iot2_Expression167", None)
                setattr(value, "iot2_Expression167", self)

    @property
    def iot2_Expression_Plus169(self):
        return self.__iot2_Expression_Plus169

    @iot2_Expression_Plus169.setter
    def iot2_Expression_Plus169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Plus__iot2_Expression_Plus169", None)
        self.__iot2_Expression_Plus169 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression170"):
                opp_val = getattr(old_value, "iot2_Expression170", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression170"):
                opp_val = getattr(value, "iot2_Expression170", None)
                setattr(value, "iot2_Expression170", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Expression_Division(Expression):

    def __init__(self, iot2_Expression_Division: "iot2_Expression" = None, iot2_Expression_Division184: "iot2_Expression" = None):
        self.iot2_Expression_Division = iot2_Expression_Division
        self.iot2_Expression_Division184 = iot2_Expression_Division184
        
    @property
    def iot2_Expression_Division184(self):
        return self.__iot2_Expression_Division184

    @iot2_Expression_Division184.setter
    def iot2_Expression_Division184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Division__iot2_Expression_Division184", None)
        self.__iot2_Expression_Division184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression185"):
                opp_val = getattr(old_value, "iot2_Expression185", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression185"):
                opp_val = getattr(value, "iot2_Expression185", None)
                setattr(value, "iot2_Expression185", self)

    @property
    def iot2_Expression_Division(self):
        return self.__iot2_Expression_Division

    @iot2_Expression_Division.setter
    def iot2_Expression_Division(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Division__iot2_Expression_Division", None)
        self.__iot2_Expression_Division = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression182"):
                opp_val = getattr(old_value, "iot2_Expression182", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression182", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression182"):
                opp_val = getattr(value, "iot2_Expression182", None)
                setattr(value, "iot2_Expression182", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Expression_Exponentiation(Expression):

    def __init__(self, iot2_Expression_Exponentiation: "iot2_Expression" = None, iot2_Expression_Exponentiation200: "iot2_Expression" = None):
        self.iot2_Expression_Exponentiation = iot2_Expression_Exponentiation
        self.iot2_Expression_Exponentiation200 = iot2_Expression_Exponentiation200
        
    @property
    def iot2_Expression_Exponentiation(self):
        return self.__iot2_Expression_Exponentiation

    @iot2_Expression_Exponentiation.setter
    def iot2_Expression_Exponentiation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Exponentiation__iot2_Expression_Exponentiation", None)
        self.__iot2_Expression_Exponentiation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression198"):
                opp_val = getattr(old_value, "iot2_Expression198", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression198", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression198"):
                opp_val = getattr(value, "iot2_Expression198", None)
                setattr(value, "iot2_Expression198", self)

    @property
    def iot2_Expression_Exponentiation200(self):
        return self.__iot2_Expression_Exponentiation200

    @iot2_Expression_Exponentiation200.setter
    def iot2_Expression_Exponentiation200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Exponentiation__iot2_Expression_Exponentiation200", None)
        self.__iot2_Expression_Exponentiation200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression201"):
                opp_val = getattr(old_value, "iot2_Expression201", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression201", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression201"):
                opp_val = getattr(value, "iot2_Expression201", None)
                setattr(value, "iot2_Expression201", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Expression_True(Expression):

    def __init__(self):
        
    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Expression_Invert(Expression):

    def __init__(self, iot2_Expression_Invert: "iot2_Expression" = None):
        self.iot2_Expression_Invert = iot2_Expression_Invert
        
    @property
    def iot2_Expression_Invert(self):
        return self.__iot2_Expression_Invert

    @iot2_Expression_Invert.setter
    def iot2_Expression_Invert(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Invert__iot2_Expression_Invert", None)
        self.__iot2_Expression_Invert = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression196"):
                opp_val = getattr(old_value, "iot2_Expression196", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression196", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression196"):
                opp_val = getattr(value, "iot2_Expression196", None)
                setattr(value, "iot2_Expression196", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Expression_AccessMember(Expression):

    def __init__(self, memberName: str, iot2_Expression_AccessMember: "iot2_Expression" = None):
        self.memberName = memberName
        self.iot2_Expression_AccessMember = iot2_Expression_AccessMember
        
    @property
    def memberName(self) -> str:
        return self.__memberName

    @memberName.setter
    def memberName(self, memberName: str):
        self.__memberName = memberName

    @property
    def iot2_Expression_AccessMember(self):
        return self.__iot2_Expression_AccessMember

    @iot2_Expression_AccessMember.setter
    def iot2_Expression_AccessMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_AccessMember__iot2_Expression_AccessMember", None)
        self.__iot2_Expression_AccessMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression218"):
                opp_val = getattr(old_value, "iot2_Expression218", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression218", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression218"):
                opp_val = getattr(value, "iot2_Expression218", None)
                setattr(value, "iot2_Expression218", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Expression_Multiplication(Expression):

    def __init__(self, iot2_Expression_Multiplication179: "iot2_Expression" = None, iot2_Expression_Multiplication: "iot2_Expression" = None):
        self.iot2_Expression_Multiplication179 = iot2_Expression_Multiplication179
        self.iot2_Expression_Multiplication = iot2_Expression_Multiplication
        
    @property
    def iot2_Expression_Multiplication(self):
        return self.__iot2_Expression_Multiplication

    @iot2_Expression_Multiplication.setter
    def iot2_Expression_Multiplication(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Multiplication__iot2_Expression_Multiplication", None)
        self.__iot2_Expression_Multiplication = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression177"):
                opp_val = getattr(old_value, "iot2_Expression177", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression177", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression177"):
                opp_val = getattr(value, "iot2_Expression177", None)
                setattr(value, "iot2_Expression177", self)

    @property
    def iot2_Expression_Multiplication179(self):
        return self.__iot2_Expression_Multiplication179

    @iot2_Expression_Multiplication179.setter
    def iot2_Expression_Multiplication179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Multiplication__iot2_Expression_Multiplication179", None)
        self.__iot2_Expression_Multiplication179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression180"):
                opp_val = getattr(old_value, "iot2_Expression180", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression180", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression180"):
                opp_val = getattr(value, "iot2_Expression180", None)
                setattr(value, "iot2_Expression180", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Expression_Larger(Expression):

    def __init__(self, iot2_Expression_Larger: "iot2_Expression" = None, iot2_Expression_Larger134: "iot2_Expression" = None):
        self.iot2_Expression_Larger = iot2_Expression_Larger
        self.iot2_Expression_Larger134 = iot2_Expression_Larger134
        
    @property
    def iot2_Expression_Larger134(self):
        return self.__iot2_Expression_Larger134

    @iot2_Expression_Larger134.setter
    def iot2_Expression_Larger134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Larger__iot2_Expression_Larger134", None)
        self.__iot2_Expression_Larger134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression135"):
                opp_val = getattr(old_value, "iot2_Expression135", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression135"):
                opp_val = getattr(value, "iot2_Expression135", None)
                setattr(value, "iot2_Expression135", self)

    @property
    def iot2_Expression_Larger(self):
        return self.__iot2_Expression_Larger

    @iot2_Expression_Larger.setter
    def iot2_Expression_Larger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Larger__iot2_Expression_Larger", None)
        self.__iot2_Expression_Larger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression132"):
                opp_val = getattr(old_value, "iot2_Expression132", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression132"):
                opp_val = getattr(value, "iot2_Expression132", None)
                setattr(value, "iot2_Expression132", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Expression_Negate(Expression):

    def __init__(self, iot2_Expression_Negate: "iot2_Expression" = None):
        self.iot2_Expression_Negate = iot2_Expression_Negate
        
    @property
    def iot2_Expression_Negate(self):
        return self.__iot2_Expression_Negate

    @iot2_Expression_Negate.setter
    def iot2_Expression_Negate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Negate__iot2_Expression_Negate", None)
        self.__iot2_Expression_Negate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression192"):
                opp_val = getattr(old_value, "iot2_Expression192", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression192", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression192"):
                opp_val = getattr(value, "iot2_Expression192", None)
                setattr(value, "iot2_Expression192", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Expression_Concatenation(Expression):

    def __init__(self, iot2_Expression_Concatenation: "iot2_Expression" = None, iot2_Expression_Concatenation164: "iot2_Expression" = None):
        self.iot2_Expression_Concatenation = iot2_Expression_Concatenation
        self.iot2_Expression_Concatenation164 = iot2_Expression_Concatenation164
        
    @property
    def iot2_Expression_Concatenation164(self):
        return self.__iot2_Expression_Concatenation164

    @iot2_Expression_Concatenation164.setter
    def iot2_Expression_Concatenation164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Concatenation__iot2_Expression_Concatenation164", None)
        self.__iot2_Expression_Concatenation164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression165"):
                opp_val = getattr(old_value, "iot2_Expression165", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression165"):
                opp_val = getattr(value, "iot2_Expression165", None)
                setattr(value, "iot2_Expression165", self)

    @property
    def iot2_Expression_Concatenation(self):
        return self.__iot2_Expression_Concatenation

    @iot2_Expression_Concatenation.setter
    def iot2_Expression_Concatenation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Concatenation__iot2_Expression_Concatenation", None)
        self.__iot2_Expression_Concatenation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression162"):
                opp_val = getattr(old_value, "iot2_Expression162", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression162"):
                opp_val = getattr(value, "iot2_Expression162", None)
                setattr(value, "iot2_Expression162", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Expression_Number(Expression):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Expression_AccessArray(Expression):

    def __init__(self, iot2_Expression_AccessArray: "iot2_Expression" = None, iot2_Expression_AccessArray215: "iot2_Expression" = None):
        self.iot2_Expression_AccessArray = iot2_Expression_AccessArray
        self.iot2_Expression_AccessArray215 = iot2_Expression_AccessArray215
        
    @property
    def iot2_Expression_AccessArray(self):
        return self.__iot2_Expression_AccessArray

    @iot2_Expression_AccessArray.setter
    def iot2_Expression_AccessArray(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_AccessArray__iot2_Expression_AccessArray", None)
        self.__iot2_Expression_AccessArray = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression213"):
                opp_val = getattr(old_value, "iot2_Expression213", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression213", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression213"):
                opp_val = getattr(value, "iot2_Expression213", None)
                setattr(value, "iot2_Expression213", self)

    @property
    def iot2_Expression_AccessArray215(self):
        return self.__iot2_Expression_AccessArray215

    @iot2_Expression_AccessArray215.setter
    def iot2_Expression_AccessArray215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_AccessArray__iot2_Expression_AccessArray215", None)
        self.__iot2_Expression_AccessArray215 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression216"):
                opp_val = getattr(old_value, "iot2_Expression216", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression216", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression216"):
                opp_val = getattr(value, "iot2_Expression216", None)
                setattr(value, "iot2_Expression216", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Expression_And(Expression):

    def __init__(self, iot2_Expression_And: "iot2_Expression" = None, iot2_Expression_And129: "iot2_Expression" = None):
        self.iot2_Expression_And = iot2_Expression_And
        self.iot2_Expression_And129 = iot2_Expression_And129
        
    @property
    def iot2_Expression_And(self):
        return self.__iot2_Expression_And

    @iot2_Expression_And.setter
    def iot2_Expression_And(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_And__iot2_Expression_And", None)
        self.__iot2_Expression_And = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression127"):
                opp_val = getattr(old_value, "iot2_Expression127", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression127"):
                opp_val = getattr(value, "iot2_Expression127", None)
                setattr(value, "iot2_Expression127", self)

    @property
    def iot2_Expression_And129(self):
        return self.__iot2_Expression_And129

    @iot2_Expression_And129.setter
    def iot2_Expression_And129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_And__iot2_Expression_And129", None)
        self.__iot2_Expression_And129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression130"):
                opp_val = getattr(old_value, "iot2_Expression130", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression130"):
                opp_val = getattr(value, "iot2_Expression130", None)
                setattr(value, "iot2_Expression130", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Expression_VarArgs(Expression):

    def __init__(self):
        
    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Expression_False(Expression):

    def __init__(self):
        
    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Expression_TableConstructor(Expression):

    def __init__(self, iot2_Expression_TableConstructor: set["iot2_Field"] = None):
        self.iot2_Expression_TableConstructor = iot2_Expression_TableConstructor if iot2_Expression_TableConstructor is not None else set()
        
    @property
    def iot2_Expression_TableConstructor(self):
        return self.__iot2_Expression_TableConstructor

    @iot2_Expression_TableConstructor.setter
    def iot2_Expression_TableConstructor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_TableConstructor__iot2_Expression_TableConstructor", None)
        self.__iot2_Expression_TableConstructor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_Field96"):
                    opp_val = getattr(item, "iot2_Field96", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_Field96", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_Field96"):
                    opp_val = getattr(item, "iot2_Field96", None)
                    
                    setattr(item, "iot2_Field96", self)
                    

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Expression_Equal(Expression):

    def __init__(self, iot2_Expression_Equal: "iot2_Expression" = None, iot2_Expression_Equal154: "iot2_Expression" = None):
        self.iot2_Expression_Equal = iot2_Expression_Equal
        self.iot2_Expression_Equal154 = iot2_Expression_Equal154
        
    @property
    def iot2_Expression_Equal(self):
        return self.__iot2_Expression_Equal

    @iot2_Expression_Equal.setter
    def iot2_Expression_Equal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Equal__iot2_Expression_Equal", None)
        self.__iot2_Expression_Equal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression152"):
                opp_val = getattr(old_value, "iot2_Expression152", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression152"):
                opp_val = getattr(value, "iot2_Expression152", None)
                setattr(value, "iot2_Expression152", self)

    @property
    def iot2_Expression_Equal154(self):
        return self.__iot2_Expression_Equal154

    @iot2_Expression_Equal154.setter
    def iot2_Expression_Equal154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Equal__iot2_Expression_Equal154", None)
        self.__iot2_Expression_Equal154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression155"):
                opp_val = getattr(old_value, "iot2_Expression155", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression155", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression155"):
                opp_val = getattr(value, "iot2_Expression155", None)
                setattr(value, "iot2_Expression155", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Expression_Larger_Equal(Expression):

    def __init__(self, iot2_Expression_Larger_Equal: "iot2_Expression" = None, iot2_Expression_Larger_Equal139: "iot2_Expression" = None):
        self.iot2_Expression_Larger_Equal = iot2_Expression_Larger_Equal
        self.iot2_Expression_Larger_Equal139 = iot2_Expression_Larger_Equal139
        
    @property
    def iot2_Expression_Larger_Equal139(self):
        return self.__iot2_Expression_Larger_Equal139

    @iot2_Expression_Larger_Equal139.setter
    def iot2_Expression_Larger_Equal139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Larger_Equal__iot2_Expression_Larger_Equal139", None)
        self.__iot2_Expression_Larger_Equal139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression140"):
                opp_val = getattr(old_value, "iot2_Expression140", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression140"):
                opp_val = getattr(value, "iot2_Expression140", None)
                setattr(value, "iot2_Expression140", self)

    @property
    def iot2_Expression_Larger_Equal(self):
        return self.__iot2_Expression_Larger_Equal

    @iot2_Expression_Larger_Equal.setter
    def iot2_Expression_Larger_Equal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Larger_Equal__iot2_Expression_Larger_Equal", None)
        self.__iot2_Expression_Larger_Equal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression137"):
                opp_val = getattr(old_value, "iot2_Expression137", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression137"):
                opp_val = getattr(value, "iot2_Expression137", None)
                setattr(value, "iot2_Expression137", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Expression_Modulo(Expression):

    def __init__(self, iot2_Expression_Modulo: "iot2_Expression" = None, iot2_Expression_Modulo189: "iot2_Expression" = None):
        self.iot2_Expression_Modulo = iot2_Expression_Modulo
        self.iot2_Expression_Modulo189 = iot2_Expression_Modulo189
        
    @property
    def iot2_Expression_Modulo189(self):
        return self.__iot2_Expression_Modulo189

    @iot2_Expression_Modulo189.setter
    def iot2_Expression_Modulo189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Modulo__iot2_Expression_Modulo189", None)
        self.__iot2_Expression_Modulo189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression190"):
                opp_val = getattr(old_value, "iot2_Expression190", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression190", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression190"):
                opp_val = getattr(value, "iot2_Expression190", None)
                setattr(value, "iot2_Expression190", self)

    @property
    def iot2_Expression_Modulo(self):
        return self.__iot2_Expression_Modulo

    @iot2_Expression_Modulo.setter
    def iot2_Expression_Modulo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Modulo__iot2_Expression_Modulo", None)
        self.__iot2_Expression_Modulo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression187"):
                opp_val = getattr(old_value, "iot2_Expression187", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression187", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression187"):
                opp_val = getattr(value, "iot2_Expression187", None)
                setattr(value, "iot2_Expression187", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Expression_Not_Equal(Expression):

    def __init__(self, iot2_Expression_Not_Equal: "iot2_Expression" = None, iot2_Expression_Not_Equal159: "iot2_Expression" = None):
        self.iot2_Expression_Not_Equal = iot2_Expression_Not_Equal
        self.iot2_Expression_Not_Equal159 = iot2_Expression_Not_Equal159
        
    @property
    def iot2_Expression_Not_Equal159(self):
        return self.__iot2_Expression_Not_Equal159

    @iot2_Expression_Not_Equal159.setter
    def iot2_Expression_Not_Equal159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Not_Equal__iot2_Expression_Not_Equal159", None)
        self.__iot2_Expression_Not_Equal159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression160"):
                opp_val = getattr(old_value, "iot2_Expression160", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression160"):
                opp_val = getattr(value, "iot2_Expression160", None)
                setattr(value, "iot2_Expression160", self)

    @property
    def iot2_Expression_Not_Equal(self):
        return self.__iot2_Expression_Not_Equal

    @iot2_Expression_Not_Equal.setter
    def iot2_Expression_Not_Equal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Not_Equal__iot2_Expression_Not_Equal", None)
        self.__iot2_Expression_Not_Equal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression157"):
                opp_val = getattr(old_value, "iot2_Expression157", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression157"):
                opp_val = getattr(value, "iot2_Expression157", None)
                setattr(value, "iot2_Expression157", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Expression_Function(Expression):

    def __init__(self, iot2_Expression_Function: "iot2_Function" = None):
        self.iot2_Expression_Function = iot2_Expression_Function
        
    @property
    def iot2_Expression_Function(self):
        return self.__iot2_Expression_Function

    @iot2_Expression_Function.setter
    def iot2_Expression_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Function__iot2_Expression_Function", None)
        self.__iot2_Expression_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Function94"):
                opp_val = getattr(old_value, "iot2_Function94", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Function94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Function94"):
                opp_val = getattr(value, "iot2_Function94", None)
                setattr(value, "iot2_Function94", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Expression_CallFunction(Expression):

    def __init__(self, iot2_Expression_CallFunction: "iot2_Expression" = None, iot2_Expression_CallFunction210: "iot2_Functioncall_Arguments" = None):
        self.iot2_Expression_CallFunction = iot2_Expression_CallFunction
        self.iot2_Expression_CallFunction210 = iot2_Expression_CallFunction210
        
    @property
    def iot2_Expression_CallFunction210(self):
        return self.__iot2_Expression_CallFunction210

    @iot2_Expression_CallFunction210.setter
    def iot2_Expression_CallFunction210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_CallFunction__iot2_Expression_CallFunction210", None)
        self.__iot2_Expression_CallFunction210 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Functioncall_Arguments211"):
                opp_val = getattr(old_value, "iot2_Functioncall_Arguments211", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Functioncall_Arguments211", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Functioncall_Arguments211"):
                opp_val = getattr(value, "iot2_Functioncall_Arguments211", None)
                setattr(value, "iot2_Functioncall_Arguments211", self)

    @property
    def iot2_Expression_CallFunction(self):
        return self.__iot2_Expression_CallFunction

    @iot2_Expression_CallFunction.setter
    def iot2_Expression_CallFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_CallFunction__iot2_Expression_CallFunction", None)
        self.__iot2_Expression_CallFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression208"):
                opp_val = getattr(old_value, "iot2_Expression208", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression208", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression208"):
                opp_val = getattr(value, "iot2_Expression208", None)
                setattr(value, "iot2_Expression208", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_IntegerExpression(Expression):

    pass
class iot2_Expression_Length(Expression):

    def __init__(self, iot2_Expression_Length: "iot2_Expression" = None):
        self.iot2_Expression_Length = iot2_Expression_Length
        
    @property
    def iot2_Expression_Length(self):
        return self.__iot2_Expression_Length

    @iot2_Expression_Length.setter
    def iot2_Expression_Length(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Length__iot2_Expression_Length", None)
        self.__iot2_Expression_Length = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression194"):
                opp_val = getattr(old_value, "iot2_Expression194", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression194", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression194"):
                opp_val = getattr(value, "iot2_Expression194", None)
                setattr(value, "iot2_Expression194", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Expression_String(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Expression_Smaller_Equal(Expression):

    def __init__(self, iot2_Expression_Smaller_Equal: "iot2_Expression" = None, iot2_Expression_Smaller_Equal149: "iot2_Expression" = None):
        self.iot2_Expression_Smaller_Equal = iot2_Expression_Smaller_Equal
        self.iot2_Expression_Smaller_Equal149 = iot2_Expression_Smaller_Equal149
        
    @property
    def iot2_Expression_Smaller_Equal149(self):
        return self.__iot2_Expression_Smaller_Equal149

    @iot2_Expression_Smaller_Equal149.setter
    def iot2_Expression_Smaller_Equal149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Smaller_Equal__iot2_Expression_Smaller_Equal149", None)
        self.__iot2_Expression_Smaller_Equal149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression150"):
                opp_val = getattr(old_value, "iot2_Expression150", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression150"):
                opp_val = getattr(value, "iot2_Expression150", None)
                setattr(value, "iot2_Expression150", self)

    @property
    def iot2_Expression_Smaller_Equal(self):
        return self.__iot2_Expression_Smaller_Equal

    @iot2_Expression_Smaller_Equal.setter
    def iot2_Expression_Smaller_Equal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Smaller_Equal__iot2_Expression_Smaller_Equal", None)
        self.__iot2_Expression_Smaller_Equal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression147"):
                opp_val = getattr(old_value, "iot2_Expression147", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression147"):
                opp_val = getattr(value, "iot2_Expression147", None)
                setattr(value, "iot2_Expression147", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Expression_VariableName(Expression):

    def __init__(self, variable: bool):
        self.variable = variable
        
    @property
    def variable(self) -> bool:
        return self.__variable

    @variable.setter
    def variable(self, variable: bool):
        self.__variable = variable

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_BooleanExpression(Expression):

    pass
class iot2_Expression_Smaller(Expression):

    def __init__(self, iot2_Expression_Smaller: "iot2_Expression" = None, iot2_Expression_Smaller144: "iot2_Expression" = None):
        self.iot2_Expression_Smaller = iot2_Expression_Smaller
        self.iot2_Expression_Smaller144 = iot2_Expression_Smaller144
        
    @property
    def iot2_Expression_Smaller(self):
        return self.__iot2_Expression_Smaller

    @iot2_Expression_Smaller.setter
    def iot2_Expression_Smaller(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Smaller__iot2_Expression_Smaller", None)
        self.__iot2_Expression_Smaller = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression142"):
                opp_val = getattr(old_value, "iot2_Expression142", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression142"):
                opp_val = getattr(value, "iot2_Expression142", None)
                setattr(value, "iot2_Expression142", self)

    @property
    def iot2_Expression_Smaller144(self):
        return self.__iot2_Expression_Smaller144

    @iot2_Expression_Smaller144.setter
    def iot2_Expression_Smaller144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Smaller__iot2_Expression_Smaller144", None)
        self.__iot2_Expression_Smaller144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression145"):
                opp_val = getattr(old_value, "iot2_Expression145", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression145"):
                opp_val = getattr(value, "iot2_Expression145", None)
                setattr(value, "iot2_Expression145", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Expression_Or(Expression):

    def __init__(self, iot2_Expression_Or: "iot2_Expression" = None, iot2_Expression_Or124: "iot2_Expression" = None):
        self.iot2_Expression_Or = iot2_Expression_Or
        self.iot2_Expression_Or124 = iot2_Expression_Or124
        
    @property
    def iot2_Expression_Or(self):
        return self.__iot2_Expression_Or

    @iot2_Expression_Or.setter
    def iot2_Expression_Or(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Or__iot2_Expression_Or", None)
        self.__iot2_Expression_Or = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression122"):
                opp_val = getattr(old_value, "iot2_Expression122", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression122"):
                opp_val = getattr(value, "iot2_Expression122", None)
                setattr(value, "iot2_Expression122", self)

    @property
    def iot2_Expression_Or124(self):
        return self.__iot2_Expression_Or124

    @iot2_Expression_Or124.setter
    def iot2_Expression_Or124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Or__iot2_Expression_Or124", None)
        self.__iot2_Expression_Or124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression125"):
                opp_val = getattr(old_value, "iot2_Expression125", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression125"):
                opp_val = getattr(value, "iot2_Expression125", None)
                setattr(value, "iot2_Expression125", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Expression_Nil(Expression):

    def __init__(self):
        
    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class Statement_FunctioncallOrAssignment:

    pass
class iot2_Statement_CallMemberFunction(Statement_FunctioncallOrAssignment):

    def __init__(self, memberFunctionName: str, iot2_Statement_CallMemberFunction: "iot2_Expression" = None, iot2_Statement_CallMemberFunction114: "iot2_Functioncall_Arguments" = None):
        self.memberFunctionName = memberFunctionName
        self.iot2_Statement_CallMemberFunction = iot2_Statement_CallMemberFunction
        self.iot2_Statement_CallMemberFunction114 = iot2_Statement_CallMemberFunction114
        
    @property
    def memberFunctionName(self) -> str:
        return self.__memberFunctionName

    @memberFunctionName.setter
    def memberFunctionName(self, memberFunctionName: str):
        self.__memberFunctionName = memberFunctionName

    @property
    def iot2_Statement_CallMemberFunction114(self):
        return self.__iot2_Statement_CallMemberFunction114

    @iot2_Statement_CallMemberFunction114.setter
    def iot2_Statement_CallMemberFunction114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_CallMemberFunction__iot2_Statement_CallMemberFunction114", None)
        self.__iot2_Statement_CallMemberFunction114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Functioncall_Arguments115"):
                opp_val = getattr(old_value, "iot2_Functioncall_Arguments115", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Functioncall_Arguments115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Functioncall_Arguments115"):
                opp_val = getattr(value, "iot2_Functioncall_Arguments115", None)
                setattr(value, "iot2_Functioncall_Arguments115", self)

    @property
    def iot2_Statement_CallMemberFunction(self):
        return self.__iot2_Statement_CallMemberFunction

    @iot2_Statement_CallMemberFunction.setter
    def iot2_Statement_CallMemberFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_CallMemberFunction__iot2_Statement_CallMemberFunction", None)
        self.__iot2_Statement_CallMemberFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression112"):
                opp_val = getattr(old_value, "iot2_Expression112", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression112"):
                opp_val = getattr(value, "iot2_Expression112", None)
                setattr(value, "iot2_Expression112", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Statement_Assignment(Statement_FunctioncallOrAssignment):

    def __init__(self, iot2_Statement_Assignment: set["iot2_Expression"] = None, iot2_Statement_Assignment109: set["iot2_Expression"] = None):
        self.iot2_Statement_Assignment = iot2_Statement_Assignment if iot2_Statement_Assignment is not None else set()
        self.iot2_Statement_Assignment109 = iot2_Statement_Assignment109 if iot2_Statement_Assignment109 is not None else set()
        
    @property
    def iot2_Statement_Assignment(self):
        return self.__iot2_Statement_Assignment

    @iot2_Statement_Assignment.setter
    def iot2_Statement_Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_Assignment__iot2_Statement_Assignment", None)
        self.__iot2_Statement_Assignment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_Expression107"):
                    opp_val = getattr(item, "iot2_Expression107", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_Expression107", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_Expression107"):
                    opp_val = getattr(item, "iot2_Expression107", None)
                    
                    setattr(item, "iot2_Expression107", self)
                    

    @property
    def iot2_Statement_Assignment109(self):
        return self.__iot2_Statement_Assignment109

    @iot2_Statement_Assignment109.setter
    def iot2_Statement_Assignment109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_Assignment__iot2_Statement_Assignment109", None)
        self.__iot2_Statement_Assignment109 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_Expression110"):
                    opp_val = getattr(item, "iot2_Expression110", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_Expression110", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_Expression110"):
                    opp_val = getattr(item, "iot2_Expression110", None)
                    
                    setattr(item, "iot2_Expression110", self)
                    

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Statement_CallFunction(Statement_FunctioncallOrAssignment):

    def __init__(self, iot2_Statement_CallFunction: "iot2_Expression" = None, iot2_Statement_CallFunction119: "iot2_Functioncall_Arguments" = None):
        self.iot2_Statement_CallFunction = iot2_Statement_CallFunction
        self.iot2_Statement_CallFunction119 = iot2_Statement_CallFunction119
        
    @property
    def iot2_Statement_CallFunction(self):
        return self.__iot2_Statement_CallFunction

    @iot2_Statement_CallFunction.setter
    def iot2_Statement_CallFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_CallFunction__iot2_Statement_CallFunction", None)
        self.__iot2_Statement_CallFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression117"):
                opp_val = getattr(old_value, "iot2_Expression117", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression117"):
                opp_val = getattr(value, "iot2_Expression117", None)
                setattr(value, "iot2_Expression117", self)

    @property
    def iot2_Statement_CallFunction119(self):
        return self.__iot2_Statement_CallFunction119

    @iot2_Statement_CallFunction119.setter
    def iot2_Statement_CallFunction119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_CallFunction__iot2_Statement_CallFunction119", None)
        self.__iot2_Statement_CallFunction119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Functioncall_Arguments120"):
                opp_val = getattr(old_value, "iot2_Functioncall_Arguments120", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Functioncall_Arguments120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Functioncall_Arguments120"):
                opp_val = getattr(value, "iot2_Functioncall_Arguments120", None)
                setattr(value, "iot2_Functioncall_Arguments120", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Function:

    def __init__(self, parameters: str, varArgs: bool, iot2_Function: "iot2_Statement_GlobalFunction_Declaration" = None, iot2_Function90: "iot2_Statement_LocalFunction_Declaration" = None, iot2_Function94: "iot2_Expression_Function" = None, iot2_Function98: "iot2_Block" = None):
        self.parameters = parameters
        self.varArgs = varArgs
        self.iot2_Function = iot2_Function
        self.iot2_Function90 = iot2_Function90
        self.iot2_Function94 = iot2_Function94
        self.iot2_Function98 = iot2_Function98
        
    @property
    def parameters(self) -> str:
        return self.__parameters

    @parameters.setter
    def parameters(self, parameters: str):
        self.__parameters = parameters

    @property
    def varArgs(self) -> bool:
        return self.__varArgs

    @varArgs.setter
    def varArgs(self, varArgs: bool):
        self.__varArgs = varArgs

    @property
    def iot2_Function(self):
        return self.__iot2_Function

    @iot2_Function.setter
    def iot2_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Function__iot2_Function", None)
        self.__iot2_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_GlobalFunction_Declaration"):
                opp_val = getattr(old_value, "iot2_Statement_GlobalFunction_Declaration", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_GlobalFunction_Declaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_GlobalFunction_Declaration"):
                opp_val = getattr(value, "iot2_Statement_GlobalFunction_Declaration", None)
                setattr(value, "iot2_Statement_GlobalFunction_Declaration", self)

    @property
    def iot2_Function94(self):
        return self.__iot2_Function94

    @iot2_Function94.setter
    def iot2_Function94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Function__iot2_Function94", None)
        self.__iot2_Function94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Function"):
                opp_val = getattr(old_value, "iot2_Expression_Function", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Function", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Function"):
                opp_val = getattr(value, "iot2_Expression_Function", None)
                setattr(value, "iot2_Expression_Function", self)

    @property
    def iot2_Function98(self):
        return self.__iot2_Function98

    @iot2_Function98.setter
    def iot2_Function98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Function__iot2_Function98", None)
        self.__iot2_Function98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Block99"):
                opp_val = getattr(old_value, "iot2_Block99", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Block99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Block99"):
                opp_val = getattr(value, "iot2_Block99", None)
                setattr(value, "iot2_Block99", self)

    @property
    def iot2_Function90(self):
        return self.__iot2_Function90

    @iot2_Function90.setter
    def iot2_Function90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Function__iot2_Function90", None)
        self.__iot2_Function90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_LocalFunction_Declaration"):
                opp_val = getattr(old_value, "iot2_Statement_LocalFunction_Declaration", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_LocalFunction_Declaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_LocalFunction_Declaration"):
                opp_val = getattr(value, "iot2_Statement_LocalFunction_Declaration", None)
                setattr(value, "iot2_Statement_LocalFunction_Declaration", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Statement_If_Then_Else_ElseIfPart:

    def __init__(self, iot2_Statement_If_Then_Else_ElseIfPart: "iot2_Statement_If_Then_Else" = None, iot2_Statement_If_Then_Else_ElseIfPart67: "iot2_Expression" = None, iot2_Statement_If_Then_Else_ElseIfPart70: "iot2_Block" = None):
        self.iot2_Statement_If_Then_Else_ElseIfPart = iot2_Statement_If_Then_Else_ElseIfPart
        self.iot2_Statement_If_Then_Else_ElseIfPart67 = iot2_Statement_If_Then_Else_ElseIfPart67
        self.iot2_Statement_If_Then_Else_ElseIfPart70 = iot2_Statement_If_Then_Else_ElseIfPart70
        
    @property
    def iot2_Statement_If_Then_Else_ElseIfPart67(self):
        return self.__iot2_Statement_If_Then_Else_ElseIfPart67

    @iot2_Statement_If_Then_Else_ElseIfPart67.setter
    def iot2_Statement_If_Then_Else_ElseIfPart67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_If_Then_Else_ElseIfPart__iot2_Statement_If_Then_Else_ElseIfPart67", None)
        self.__iot2_Statement_If_Then_Else_ElseIfPart67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression68"):
                opp_val = getattr(old_value, "iot2_Expression68", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression68"):
                opp_val = getattr(value, "iot2_Expression68", None)
                setattr(value, "iot2_Expression68", self)

    @property
    def iot2_Statement_If_Then_Else_ElseIfPart(self):
        return self.__iot2_Statement_If_Then_Else_ElseIfPart

    @iot2_Statement_If_Then_Else_ElseIfPart.setter
    def iot2_Statement_If_Then_Else_ElseIfPart(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_If_Then_Else_ElseIfPart__iot2_Statement_If_Then_Else_ElseIfPart", None)
        self.__iot2_Statement_If_Then_Else_ElseIfPart = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_If_Then_Else62"):
                opp_val = getattr(old_value, "iot2_Statement_If_Then_Else62", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_If_Then_Else62"):
                opp_val = getattr(value, "iot2_Statement_If_Then_Else62", None)
                if opp_val is None:
                    setattr(value, "iot2_Statement_If_Then_Else62", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_Statement_If_Then_Else_ElseIfPart70(self):
        return self.__iot2_Statement_If_Then_Else_ElseIfPart70

    @iot2_Statement_If_Then_Else_ElseIfPart70.setter
    def iot2_Statement_If_Then_Else_ElseIfPart70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_If_Then_Else_ElseIfPart__iot2_Statement_If_Then_Else_ElseIfPart70", None)
        self.__iot2_Statement_If_Then_Else_ElseIfPart70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Block71"):
                opp_val = getattr(old_value, "iot2_Block71", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Block71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Block71"):
                opp_val = getattr(value, "iot2_Block71", None)
                setattr(value, "iot2_Block71", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class Statement:

    pass
class iot2_Statement_Repeat(Statement):

    def __init__(self, iot2_Statement_Repeat: "iot2_Block" = None, iot2_Statement_Repeat54: "iot2_Expression" = None):
        self.iot2_Statement_Repeat = iot2_Statement_Repeat
        self.iot2_Statement_Repeat54 = iot2_Statement_Repeat54
        
    @property
    def iot2_Statement_Repeat(self):
        return self.__iot2_Statement_Repeat

    @iot2_Statement_Repeat.setter
    def iot2_Statement_Repeat(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_Repeat__iot2_Statement_Repeat", None)
        self.__iot2_Statement_Repeat = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Block52"):
                opp_val = getattr(old_value, "iot2_Block52", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Block52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Block52"):
                opp_val = getattr(value, "iot2_Block52", None)
                setattr(value, "iot2_Block52", self)

    @property
    def iot2_Statement_Repeat54(self):
        return self.__iot2_Statement_Repeat54

    @iot2_Statement_Repeat54.setter
    def iot2_Statement_Repeat54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_Repeat__iot2_Statement_Repeat54", None)
        self.__iot2_Statement_Repeat54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression55"):
                opp_val = getattr(old_value, "iot2_Expression55", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression55"):
                opp_val = getattr(value, "iot2_Expression55", None)
                setattr(value, "iot2_Expression55", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Statement_For_Generic(Statement):

    def __init__(self, names: str, iot2_Statement_For_Generic: set["iot2_Expression"] = None, iot2_Statement_For_Generic86: "iot2_Block" = None):
        self.names = names
        self.iot2_Statement_For_Generic = iot2_Statement_For_Generic if iot2_Statement_For_Generic is not None else set()
        self.iot2_Statement_For_Generic86 = iot2_Statement_For_Generic86
        
    @property
    def names(self) -> str:
        return self.__names

    @names.setter
    def names(self, names: str):
        self.__names = names

    @property
    def iot2_Statement_For_Generic(self):
        return self.__iot2_Statement_For_Generic

    @iot2_Statement_For_Generic.setter
    def iot2_Statement_For_Generic(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_For_Generic__iot2_Statement_For_Generic", None)
        self.__iot2_Statement_For_Generic = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_Expression84"):
                    opp_val = getattr(item, "iot2_Expression84", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_Expression84", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_Expression84"):
                    opp_val = getattr(item, "iot2_Expression84", None)
                    
                    setattr(item, "iot2_Expression84", self)
                    

    @property
    def iot2_Statement_For_Generic86(self):
        return self.__iot2_Statement_For_Generic86

    @iot2_Statement_For_Generic86.setter
    def iot2_Statement_For_Generic86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_For_Generic__iot2_Statement_For_Generic86", None)
        self.__iot2_Statement_For_Generic86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Block87"):
                opp_val = getattr(old_value, "iot2_Block87", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Block87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Block87"):
                opp_val = getattr(value, "iot2_Block87", None)
                setattr(value, "iot2_Block87", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Statement_GlobalFunction_Declaration(Statement):

    def __init__(self, prefix: str, functionName: str, iot2_Statement_GlobalFunction_Declaration: "iot2_Function" = None):
        self.prefix = prefix
        self.functionName = functionName
        self.iot2_Statement_GlobalFunction_Declaration = iot2_Statement_GlobalFunction_Declaration
        
    @property
    def functionName(self) -> str:
        return self.__functionName

    @functionName.setter
    def functionName(self, functionName: str):
        self.__functionName = functionName

    @property
    def prefix(self) -> str:
        return self.__prefix

    @prefix.setter
    def prefix(self, prefix: str):
        self.__prefix = prefix

    @property
    def iot2_Statement_GlobalFunction_Declaration(self):
        return self.__iot2_Statement_GlobalFunction_Declaration

    @iot2_Statement_GlobalFunction_Declaration.setter
    def iot2_Statement_GlobalFunction_Declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_GlobalFunction_Declaration__iot2_Statement_GlobalFunction_Declaration", None)
        self.__iot2_Statement_GlobalFunction_Declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Function"):
                opp_val = getattr(old_value, "iot2_Function", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Function", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Function"):
                opp_val = getattr(value, "iot2_Function", None)
                setattr(value, "iot2_Function", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Statement_For_Numeric(Statement):

    def __init__(self, iteratorName: str, iot2_Statement_For_Numeric: "iot2_Expression" = None, iot2_Statement_For_Numeric75: "iot2_Expression" = None, iot2_Statement_For_Numeric78: "iot2_Expression" = None, iot2_Statement_For_Numeric81: "iot2_Block" = None):
        self.iteratorName = iteratorName
        self.iot2_Statement_For_Numeric = iot2_Statement_For_Numeric
        self.iot2_Statement_For_Numeric75 = iot2_Statement_For_Numeric75
        self.iot2_Statement_For_Numeric78 = iot2_Statement_For_Numeric78
        self.iot2_Statement_For_Numeric81 = iot2_Statement_For_Numeric81
        
    @property
    def iteratorName(self) -> str:
        return self.__iteratorName

    @iteratorName.setter
    def iteratorName(self, iteratorName: str):
        self.__iteratorName = iteratorName

    @property
    def iot2_Statement_For_Numeric75(self):
        return self.__iot2_Statement_For_Numeric75

    @iot2_Statement_For_Numeric75.setter
    def iot2_Statement_For_Numeric75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_For_Numeric__iot2_Statement_For_Numeric75", None)
        self.__iot2_Statement_For_Numeric75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression76"):
                opp_val = getattr(old_value, "iot2_Expression76", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression76"):
                opp_val = getattr(value, "iot2_Expression76", None)
                setattr(value, "iot2_Expression76", self)

    @property
    def iot2_Statement_For_Numeric(self):
        return self.__iot2_Statement_For_Numeric

    @iot2_Statement_For_Numeric.setter
    def iot2_Statement_For_Numeric(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_For_Numeric__iot2_Statement_For_Numeric", None)
        self.__iot2_Statement_For_Numeric = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression73"):
                opp_val = getattr(old_value, "iot2_Expression73", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression73"):
                opp_val = getattr(value, "iot2_Expression73", None)
                setattr(value, "iot2_Expression73", self)

    @property
    def iot2_Statement_For_Numeric81(self):
        return self.__iot2_Statement_For_Numeric81

    @iot2_Statement_For_Numeric81.setter
    def iot2_Statement_For_Numeric81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_For_Numeric__iot2_Statement_For_Numeric81", None)
        self.__iot2_Statement_For_Numeric81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Block82"):
                opp_val = getattr(old_value, "iot2_Block82", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Block82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Block82"):
                opp_val = getattr(value, "iot2_Block82", None)
                setattr(value, "iot2_Block82", self)

    @property
    def iot2_Statement_For_Numeric78(self):
        return self.__iot2_Statement_For_Numeric78

    @iot2_Statement_For_Numeric78.setter
    def iot2_Statement_For_Numeric78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_For_Numeric__iot2_Statement_For_Numeric78", None)
        self.__iot2_Statement_For_Numeric78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression79"):
                opp_val = getattr(old_value, "iot2_Expression79", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression79"):
                opp_val = getattr(value, "iot2_Expression79", None)
                setattr(value, "iot2_Expression79", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Statement_While(Statement):

    def __init__(self, iot2_Statement_While: "iot2_Expression" = None, iot2_Statement_While49: "iot2_Block" = None):
        self.iot2_Statement_While = iot2_Statement_While
        self.iot2_Statement_While49 = iot2_Statement_While49
        
    @property
    def iot2_Statement_While(self):
        return self.__iot2_Statement_While

    @iot2_Statement_While.setter
    def iot2_Statement_While(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_While__iot2_Statement_While", None)
        self.__iot2_Statement_While = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression47"):
                opp_val = getattr(old_value, "iot2_Expression47", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression47"):
                opp_val = getattr(value, "iot2_Expression47", None)
                setattr(value, "iot2_Expression47", self)

    @property
    def iot2_Statement_While49(self):
        return self.__iot2_Statement_While49

    @iot2_Statement_While49.setter
    def iot2_Statement_While49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_While__iot2_Statement_While49", None)
        self.__iot2_Statement_While49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Block50"):
                opp_val = getattr(old_value, "iot2_Block50", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Block50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Block50"):
                opp_val = getattr(value, "iot2_Block50", None)
                setattr(value, "iot2_Block50", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Statement_If_Then_Else(Statement):

    def __init__(self, iot2_Statement_If_Then_Else: "iot2_Expression" = None, iot2_Statement_If_Then_Else59: "iot2_Block" = None, iot2_Statement_If_Then_Else62: set["iot2_Statement_If_Then_Else_ElseIfPart"] = None, iot2_Statement_If_Then_Else64: "iot2_Block" = None):
        self.iot2_Statement_If_Then_Else = iot2_Statement_If_Then_Else
        self.iot2_Statement_If_Then_Else59 = iot2_Statement_If_Then_Else59
        self.iot2_Statement_If_Then_Else62 = iot2_Statement_If_Then_Else62 if iot2_Statement_If_Then_Else62 is not None else set()
        self.iot2_Statement_If_Then_Else64 = iot2_Statement_If_Then_Else64
        
    @property
    def iot2_Statement_If_Then_Else62(self):
        return self.__iot2_Statement_If_Then_Else62

    @iot2_Statement_If_Then_Else62.setter
    def iot2_Statement_If_Then_Else62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_If_Then_Else__iot2_Statement_If_Then_Else62", None)
        self.__iot2_Statement_If_Then_Else62 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_Statement_If_Then_Else_ElseIfPart"):
                    opp_val = getattr(item, "iot2_Statement_If_Then_Else_ElseIfPart", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_Statement_If_Then_Else_ElseIfPart", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_Statement_If_Then_Else_ElseIfPart"):
                    opp_val = getattr(item, "iot2_Statement_If_Then_Else_ElseIfPart", None)
                    
                    setattr(item, "iot2_Statement_If_Then_Else_ElseIfPart", self)
                    

    @property
    def iot2_Statement_If_Then_Else(self):
        return self.__iot2_Statement_If_Then_Else

    @iot2_Statement_If_Then_Else.setter
    def iot2_Statement_If_Then_Else(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_If_Then_Else__iot2_Statement_If_Then_Else", None)
        self.__iot2_Statement_If_Then_Else = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression57"):
                opp_val = getattr(old_value, "iot2_Expression57", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression57"):
                opp_val = getattr(value, "iot2_Expression57", None)
                setattr(value, "iot2_Expression57", self)

    @property
    def iot2_Statement_If_Then_Else59(self):
        return self.__iot2_Statement_If_Then_Else59

    @iot2_Statement_If_Then_Else59.setter
    def iot2_Statement_If_Then_Else59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_If_Then_Else__iot2_Statement_If_Then_Else59", None)
        self.__iot2_Statement_If_Then_Else59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Block60"):
                opp_val = getattr(old_value, "iot2_Block60", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Block60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Block60"):
                opp_val = getattr(value, "iot2_Block60", None)
                setattr(value, "iot2_Block60", self)

    @property
    def iot2_Statement_If_Then_Else64(self):
        return self.__iot2_Statement_If_Then_Else64

    @iot2_Statement_If_Then_Else64.setter
    def iot2_Statement_If_Then_Else64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_If_Then_Else__iot2_Statement_If_Then_Else64", None)
        self.__iot2_Statement_If_Then_Else64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Block65"):
                opp_val = getattr(old_value, "iot2_Block65", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Block65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Block65"):
                opp_val = getattr(value, "iot2_Block65", None)
                setattr(value, "iot2_Block65", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Statement_Local_Variable_Declaration(Statement):

    def __init__(self, variableNames: str, iot2_Statement_Local_Variable_Declaration: set["iot2_Expression"] = None):
        self.variableNames = variableNames
        self.iot2_Statement_Local_Variable_Declaration = iot2_Statement_Local_Variable_Declaration if iot2_Statement_Local_Variable_Declaration is not None else set()
        
    @property
    def variableNames(self) -> str:
        return self.__variableNames

    @variableNames.setter
    def variableNames(self, variableNames: str):
        self.__variableNames = variableNames

    @property
    def iot2_Statement_Local_Variable_Declaration(self):
        return self.__iot2_Statement_Local_Variable_Declaration

    @iot2_Statement_Local_Variable_Declaration.setter
    def iot2_Statement_Local_Variable_Declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_Local_Variable_Declaration__iot2_Statement_Local_Variable_Declaration", None)
        self.__iot2_Statement_Local_Variable_Declaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_Expression92"):
                    opp_val = getattr(item, "iot2_Expression92", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_Expression92", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_Expression92"):
                    opp_val = getattr(item, "iot2_Expression92", None)
                    
                    setattr(item, "iot2_Expression92", self)
                    

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Statement_LocalFunction_Declaration(Statement):

    def __init__(self, functionName: str, iot2_Statement_LocalFunction_Declaration: "iot2_Function" = None):
        self.functionName = functionName
        self.iot2_Statement_LocalFunction_Declaration = iot2_Statement_LocalFunction_Declaration
        
    @property
    def functionName(self) -> str:
        return self.__functionName

    @functionName.setter
    def functionName(self, functionName: str):
        self.__functionName = functionName

    @property
    def iot2_Statement_LocalFunction_Declaration(self):
        return self.__iot2_Statement_LocalFunction_Declaration

    @iot2_Statement_LocalFunction_Declaration.setter
    def iot2_Statement_LocalFunction_Declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_LocalFunction_Declaration__iot2_Statement_LocalFunction_Declaration", None)
        self.__iot2_Statement_LocalFunction_Declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Function90"):
                opp_val = getattr(old_value, "iot2_Function90", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Function90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Function90"):
                opp_val = getattr(value, "iot2_Function90", None)
                setattr(value, "iot2_Function90", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Statement_FunctioncallOrAssignment(Statement):

    def __init__(self):
        
    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Statement_Block(Statement):

    def __init__(self, iot2_Statement_Block: "iot2_Block" = None):
        self.iot2_Statement_Block = iot2_Statement_Block
        
    @property
    def iot2_Statement_Block(self):
        return self.__iot2_Statement_Block

    @iot2_Statement_Block.setter
    def iot2_Statement_Block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_Block__iot2_Statement_Block", None)
        self.__iot2_Statement_Block = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Block45"):
                opp_val = getattr(old_value, "iot2_Block45", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Block45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Block45"):
                opp_val = getattr(value, "iot2_Block45", None)
                setattr(value, "iot2_Block45", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class LastStatement:

    pass
class iot2_LastStatement_Break(LastStatement):

    pass
class iot2_LastStatement_Return(LastStatement):

    def __init__(self):
        
    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_LastStatement:

    def __init__(self, iot2_LastStatement: "iot2_Block" = None):
        self.iot2_LastStatement = iot2_LastStatement
        
    @property
    def iot2_LastStatement(self):
        return self.__iot2_LastStatement

    @iot2_LastStatement.setter
    def iot2_LastStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_LastStatement__iot2_LastStatement", None)
        self.__iot2_LastStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Block43"):
                opp_val = getattr(old_value, "iot2_Block43", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Block43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Block43"):
                opp_val = getattr(value, "iot2_Block43", None)
                setattr(value, "iot2_Block43", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class Chunk:

    pass
class iot2_Chunk:

    def __init__(self):
        
    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Statement:

    def __init__(self, iot2_Statement: "iot2_Block" = None):
        self.iot2_Statement = iot2_Statement
        
    @property
    def iot2_Statement(self):
        return self.__iot2_Statement

    @iot2_Statement.setter
    def iot2_Statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement__iot2_Statement", None)
        self.__iot2_Statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Block41"):
                opp_val = getattr(old_value, "iot2_Block41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Block41"):
                opp_val = getattr(value, "iot2_Block41", None)
                if opp_val is None:
                    setattr(value, "iot2_Block41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Expression(Statement_FunctioncallOrAssignment):

    def __init__(self, iot2_Expression: "iot2_Field" = None, iot2_Expression47: "iot2_Statement_While" = None, iot2_Expression76: "iot2_Statement_For_Numeric" = None, iot2_Expression55: "iot2_Statement_Repeat" = None, iot2_Expression57: "iot2_Statement_If_Then_Else" = None, iot2_Expression68: "iot2_Statement_If_Then_Else_ElseIfPart" = None, iot2_Expression73: "iot2_Statement_For_Numeric" = None, iot2_Expression79: "iot2_Statement_For_Numeric" = None, iot2_Expression84: "iot2_Statement_For_Generic" = None, iot2_Expression92: "iot2_Statement_Local_Variable_Declaration" = None, iot2_Expression107: "iot2_Statement_Assignment" = None, iot2_Expression101: "iot2_Functioncall_Arguments" = None, iot2_Expression103: "iot2_Field_AddEntryToTable_Brackets" = None, iot2_Expression105: "iot2_LastStatement_ReturnWithValue" = None, iot2_Expression132: "iot2_Expression_Larger" = None, iot2_Expression110: "iot2_Statement_Assignment" = None, iot2_Expression135: "iot2_Expression_Larger" = None, iot2_Expression112: "iot2_Statement_CallMemberFunction" = None, iot2_Expression117: "iot2_Statement_CallFunction" = None, iot2_Expression122: "iot2_Expression_Or" = None, iot2_Expression125: "iot2_Expression_Or" = None, iot2_Expression127: "iot2_Expression_And" = None, iot2_Expression130: "iot2_Expression_And" = None, iot2_Expression157: "iot2_Expression_Not_Equal" = None, iot2_Expression160: "iot2_Expression_Not_Equal" = None, iot2_Expression137: "iot2_Expression_Larger_Equal" = None, iot2_Expression140: "iot2_Expression_Larger_Equal" = None, iot2_Expression142: "iot2_Expression_Smaller" = None, iot2_Expression145: "iot2_Expression_Smaller" = None, iot2_Expression147: "iot2_Expression_Smaller_Equal" = None, iot2_Expression150: "iot2_Expression_Smaller_Equal" = None, iot2_Expression152: "iot2_Expression_Equal" = None, iot2_Expression155: "iot2_Expression_Equal" = None, iot2_Expression180: "iot2_Expression_Multiplication" = None, iot2_Expression182: "iot2_Expression_Division" = None, iot2_Expression162: "iot2_Expression_Concatenation" = None, iot2_Expression165: "iot2_Expression_Concatenation" = None, iot2_Expression167: "iot2_Expression_Plus" = None, iot2_Expression170: "iot2_Expression_Plus" = None, iot2_Expression172: "iot2_Expression_Minus" = None, iot2_Expression175: "iot2_Expression_Minus" = None, iot2_Expression177: "iot2_Expression_Multiplication" = None, iot2_Expression198: "iot2_Expression_Exponentiation" = None, iot2_Expression201: "iot2_Expression_Exponentiation" = None, iot2_Expression185: "iot2_Expression_Division" = None, iot2_Expression187: "iot2_Expression_Modulo" = None, iot2_Expression190: "iot2_Expression_Modulo" = None, iot2_Expression192: "iot2_Expression_Negate" = None, iot2_Expression194: "iot2_Expression_Length" = None, iot2_Expression196: "iot2_Expression_Invert" = None, iot2_Expression203: "iot2_Expression_CallMemberFunction" = None, iot2_Expression208: "iot2_Expression_CallFunction" = None, iot2_Expression213: "iot2_Expression_AccessArray" = None, iot2_Expression216: "iot2_Expression_AccessArray" = None, iot2_Expression218: "iot2_Expression_AccessMember" = None, iot2_Expression240: "iot2_OpaqueAction" = None):
        self.iot2_Expression = iot2_Expression
        self.iot2_Expression47 = iot2_Expression47
        self.iot2_Expression76 = iot2_Expression76
        self.iot2_Expression55 = iot2_Expression55
        self.iot2_Expression57 = iot2_Expression57
        self.iot2_Expression68 = iot2_Expression68
        self.iot2_Expression73 = iot2_Expression73
        self.iot2_Expression79 = iot2_Expression79
        self.iot2_Expression84 = iot2_Expression84
        self.iot2_Expression92 = iot2_Expression92
        self.iot2_Expression107 = iot2_Expression107
        self.iot2_Expression101 = iot2_Expression101
        self.iot2_Expression103 = iot2_Expression103
        self.iot2_Expression105 = iot2_Expression105
        self.iot2_Expression132 = iot2_Expression132
        self.iot2_Expression110 = iot2_Expression110
        self.iot2_Expression135 = iot2_Expression135
        self.iot2_Expression112 = iot2_Expression112
        self.iot2_Expression117 = iot2_Expression117
        self.iot2_Expression122 = iot2_Expression122
        self.iot2_Expression125 = iot2_Expression125
        self.iot2_Expression127 = iot2_Expression127
        self.iot2_Expression130 = iot2_Expression130
        self.iot2_Expression157 = iot2_Expression157
        self.iot2_Expression160 = iot2_Expression160
        self.iot2_Expression137 = iot2_Expression137
        self.iot2_Expression140 = iot2_Expression140
        self.iot2_Expression142 = iot2_Expression142
        self.iot2_Expression145 = iot2_Expression145
        self.iot2_Expression147 = iot2_Expression147
        self.iot2_Expression150 = iot2_Expression150
        self.iot2_Expression152 = iot2_Expression152
        self.iot2_Expression155 = iot2_Expression155
        self.iot2_Expression180 = iot2_Expression180
        self.iot2_Expression182 = iot2_Expression182
        self.iot2_Expression162 = iot2_Expression162
        self.iot2_Expression165 = iot2_Expression165
        self.iot2_Expression167 = iot2_Expression167
        self.iot2_Expression170 = iot2_Expression170
        self.iot2_Expression172 = iot2_Expression172
        self.iot2_Expression175 = iot2_Expression175
        self.iot2_Expression177 = iot2_Expression177
        self.iot2_Expression198 = iot2_Expression198
        self.iot2_Expression201 = iot2_Expression201
        self.iot2_Expression185 = iot2_Expression185
        self.iot2_Expression187 = iot2_Expression187
        self.iot2_Expression190 = iot2_Expression190
        self.iot2_Expression192 = iot2_Expression192
        self.iot2_Expression194 = iot2_Expression194
        self.iot2_Expression196 = iot2_Expression196
        self.iot2_Expression203 = iot2_Expression203
        self.iot2_Expression208 = iot2_Expression208
        self.iot2_Expression213 = iot2_Expression213
        self.iot2_Expression216 = iot2_Expression216
        self.iot2_Expression218 = iot2_Expression218
        self.iot2_Expression240 = iot2_Expression240
        
    @property
    def iot2_Expression117(self):
        return self.__iot2_Expression117

    @iot2_Expression117.setter
    def iot2_Expression117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression117", None)
        self.__iot2_Expression117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_CallFunction"):
                opp_val = getattr(old_value, "iot2_Statement_CallFunction", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_CallFunction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_CallFunction"):
                opp_val = getattr(value, "iot2_Statement_CallFunction", None)
                setattr(value, "iot2_Statement_CallFunction", self)

    @property
    def iot2_Expression112(self):
        return self.__iot2_Expression112

    @iot2_Expression112.setter
    def iot2_Expression112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression112", None)
        self.__iot2_Expression112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_CallMemberFunction"):
                opp_val = getattr(old_value, "iot2_Statement_CallMemberFunction", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_CallMemberFunction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_CallMemberFunction"):
                opp_val = getattr(value, "iot2_Statement_CallMemberFunction", None)
                setattr(value, "iot2_Statement_CallMemberFunction", self)

    @property
    def iot2_Expression152(self):
        return self.__iot2_Expression152

    @iot2_Expression152.setter
    def iot2_Expression152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression152", None)
        self.__iot2_Expression152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Equal"):
                opp_val = getattr(old_value, "iot2_Expression_Equal", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Equal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Equal"):
                opp_val = getattr(value, "iot2_Expression_Equal", None)
                setattr(value, "iot2_Expression_Equal", self)

    @property
    def iot2_Expression(self):
        return self.__iot2_Expression

    @iot2_Expression.setter
    def iot2_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression", None)
        self.__iot2_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Field39"):
                opp_val = getattr(old_value, "iot2_Field39", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Field39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Field39"):
                opp_val = getattr(value, "iot2_Field39", None)
                setattr(value, "iot2_Field39", self)

    @property
    def iot2_Expression105(self):
        return self.__iot2_Expression105

    @iot2_Expression105.setter
    def iot2_Expression105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression105", None)
        self.__iot2_Expression105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_LastStatement_ReturnWithValue"):
                opp_val = getattr(old_value, "iot2_LastStatement_ReturnWithValue", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_LastStatement_ReturnWithValue"):
                opp_val = getattr(value, "iot2_LastStatement_ReturnWithValue", None)
                if opp_val is None:
                    setattr(value, "iot2_LastStatement_ReturnWithValue", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_Expression155(self):
        return self.__iot2_Expression155

    @iot2_Expression155.setter
    def iot2_Expression155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression155", None)
        self.__iot2_Expression155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Equal154"):
                opp_val = getattr(old_value, "iot2_Expression_Equal154", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Equal154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Equal154"):
                opp_val = getattr(value, "iot2_Expression_Equal154", None)
                setattr(value, "iot2_Expression_Equal154", self)

    @property
    def iot2_Expression182(self):
        return self.__iot2_Expression182

    @iot2_Expression182.setter
    def iot2_Expression182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression182", None)
        self.__iot2_Expression182 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Division"):
                opp_val = getattr(old_value, "iot2_Expression_Division", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Division", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Division"):
                opp_val = getattr(value, "iot2_Expression_Division", None)
                setattr(value, "iot2_Expression_Division", self)

    @property
    def iot2_Expression180(self):
        return self.__iot2_Expression180

    @iot2_Expression180.setter
    def iot2_Expression180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression180", None)
        self.__iot2_Expression180 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Multiplication179"):
                opp_val = getattr(old_value, "iot2_Expression_Multiplication179", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Multiplication179", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Multiplication179"):
                opp_val = getattr(value, "iot2_Expression_Multiplication179", None)
                setattr(value, "iot2_Expression_Multiplication179", self)

    @property
    def iot2_Expression92(self):
        return self.__iot2_Expression92

    @iot2_Expression92.setter
    def iot2_Expression92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression92", None)
        self.__iot2_Expression92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_Local_Variable_Declaration"):
                opp_val = getattr(old_value, "iot2_Statement_Local_Variable_Declaration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_Local_Variable_Declaration"):
                opp_val = getattr(value, "iot2_Statement_Local_Variable_Declaration", None)
                if opp_val is None:
                    setattr(value, "iot2_Statement_Local_Variable_Declaration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_Expression216(self):
        return self.__iot2_Expression216

    @iot2_Expression216.setter
    def iot2_Expression216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression216", None)
        self.__iot2_Expression216 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_AccessArray215"):
                opp_val = getattr(old_value, "iot2_Expression_AccessArray215", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_AccessArray215", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_AccessArray215"):
                opp_val = getattr(value, "iot2_Expression_AccessArray215", None)
                setattr(value, "iot2_Expression_AccessArray215", self)

    @property
    def iot2_Expression125(self):
        return self.__iot2_Expression125

    @iot2_Expression125.setter
    def iot2_Expression125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression125", None)
        self.__iot2_Expression125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Or124"):
                opp_val = getattr(old_value, "iot2_Expression_Or124", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Or124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Or124"):
                opp_val = getattr(value, "iot2_Expression_Or124", None)
                setattr(value, "iot2_Expression_Or124", self)

    @property
    def iot2_Expression172(self):
        return self.__iot2_Expression172

    @iot2_Expression172.setter
    def iot2_Expression172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression172", None)
        self.__iot2_Expression172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Minus"):
                opp_val = getattr(old_value, "iot2_Expression_Minus", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Minus", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Minus"):
                opp_val = getattr(value, "iot2_Expression_Minus", None)
                setattr(value, "iot2_Expression_Minus", self)

    @property
    def iot2_Expression137(self):
        return self.__iot2_Expression137

    @iot2_Expression137.setter
    def iot2_Expression137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression137", None)
        self.__iot2_Expression137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Larger_Equal"):
                opp_val = getattr(old_value, "iot2_Expression_Larger_Equal", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Larger_Equal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Larger_Equal"):
                opp_val = getattr(value, "iot2_Expression_Larger_Equal", None)
                setattr(value, "iot2_Expression_Larger_Equal", self)

    @property
    def iot2_Expression110(self):
        return self.__iot2_Expression110

    @iot2_Expression110.setter
    def iot2_Expression110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression110", None)
        self.__iot2_Expression110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_Assignment109"):
                opp_val = getattr(old_value, "iot2_Statement_Assignment109", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_Assignment109"):
                opp_val = getattr(value, "iot2_Statement_Assignment109", None)
                if opp_val is None:
                    setattr(value, "iot2_Statement_Assignment109", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_Expression175(self):
        return self.__iot2_Expression175

    @iot2_Expression175.setter
    def iot2_Expression175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression175", None)
        self.__iot2_Expression175 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Minus174"):
                opp_val = getattr(old_value, "iot2_Expression_Minus174", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Minus174", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Minus174"):
                opp_val = getattr(value, "iot2_Expression_Minus174", None)
                setattr(value, "iot2_Expression_Minus174", self)

    @property
    def iot2_Expression213(self):
        return self.__iot2_Expression213

    @iot2_Expression213.setter
    def iot2_Expression213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression213", None)
        self.__iot2_Expression213 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_AccessArray"):
                opp_val = getattr(old_value, "iot2_Expression_AccessArray", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_AccessArray", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_AccessArray"):
                opp_val = getattr(value, "iot2_Expression_AccessArray", None)
                setattr(value, "iot2_Expression_AccessArray", self)

    @property
    def iot2_Expression165(self):
        return self.__iot2_Expression165

    @iot2_Expression165.setter
    def iot2_Expression165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression165", None)
        self.__iot2_Expression165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Concatenation164"):
                opp_val = getattr(old_value, "iot2_Expression_Concatenation164", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Concatenation164", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Concatenation164"):
                opp_val = getattr(value, "iot2_Expression_Concatenation164", None)
                setattr(value, "iot2_Expression_Concatenation164", self)

    @property
    def iot2_Expression145(self):
        return self.__iot2_Expression145

    @iot2_Expression145.setter
    def iot2_Expression145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression145", None)
        self.__iot2_Expression145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Smaller144"):
                opp_val = getattr(old_value, "iot2_Expression_Smaller144", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Smaller144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Smaller144"):
                opp_val = getattr(value, "iot2_Expression_Smaller144", None)
                setattr(value, "iot2_Expression_Smaller144", self)

    @property
    def iot2_Expression203(self):
        return self.__iot2_Expression203

    @iot2_Expression203.setter
    def iot2_Expression203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression203", None)
        self.__iot2_Expression203 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_CallMemberFunction"):
                opp_val = getattr(old_value, "iot2_Expression_CallMemberFunction", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_CallMemberFunction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_CallMemberFunction"):
                opp_val = getattr(value, "iot2_Expression_CallMemberFunction", None)
                setattr(value, "iot2_Expression_CallMemberFunction", self)

    @property
    def iot2_Expression122(self):
        return self.__iot2_Expression122

    @iot2_Expression122.setter
    def iot2_Expression122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression122", None)
        self.__iot2_Expression122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Or"):
                opp_val = getattr(old_value, "iot2_Expression_Or", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Or", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Or"):
                opp_val = getattr(value, "iot2_Expression_Or", None)
                setattr(value, "iot2_Expression_Or", self)

    @property
    def iot2_Expression103(self):
        return self.__iot2_Expression103

    @iot2_Expression103.setter
    def iot2_Expression103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression103", None)
        self.__iot2_Expression103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Field_AddEntryToTable_Brackets"):
                opp_val = getattr(old_value, "iot2_Field_AddEntryToTable_Brackets", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Field_AddEntryToTable_Brackets", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Field_AddEntryToTable_Brackets"):
                opp_val = getattr(value, "iot2_Field_AddEntryToTable_Brackets", None)
                setattr(value, "iot2_Field_AddEntryToTable_Brackets", self)

    @property
    def iot2_Expression201(self):
        return self.__iot2_Expression201

    @iot2_Expression201.setter
    def iot2_Expression201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression201", None)
        self.__iot2_Expression201 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Exponentiation200"):
                opp_val = getattr(old_value, "iot2_Expression_Exponentiation200", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Exponentiation200", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Exponentiation200"):
                opp_val = getattr(value, "iot2_Expression_Exponentiation200", None)
                setattr(value, "iot2_Expression_Exponentiation200", self)

    @property
    def iot2_Expression57(self):
        return self.__iot2_Expression57

    @iot2_Expression57.setter
    def iot2_Expression57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression57", None)
        self.__iot2_Expression57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_If_Then_Else"):
                opp_val = getattr(old_value, "iot2_Statement_If_Then_Else", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_If_Then_Else", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_If_Then_Else"):
                opp_val = getattr(value, "iot2_Statement_If_Then_Else", None)
                setattr(value, "iot2_Statement_If_Then_Else", self)

    @property
    def iot2_Expression55(self):
        return self.__iot2_Expression55

    @iot2_Expression55.setter
    def iot2_Expression55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression55", None)
        self.__iot2_Expression55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_Repeat54"):
                opp_val = getattr(old_value, "iot2_Statement_Repeat54", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_Repeat54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_Repeat54"):
                opp_val = getattr(value, "iot2_Statement_Repeat54", None)
                setattr(value, "iot2_Statement_Repeat54", self)

    @property
    def iot2_Expression192(self):
        return self.__iot2_Expression192

    @iot2_Expression192.setter
    def iot2_Expression192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression192", None)
        self.__iot2_Expression192 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Negate"):
                opp_val = getattr(old_value, "iot2_Expression_Negate", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Negate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Negate"):
                opp_val = getattr(value, "iot2_Expression_Negate", None)
                setattr(value, "iot2_Expression_Negate", self)

    @property
    def iot2_Expression240(self):
        return self.__iot2_Expression240

    @iot2_Expression240.setter
    def iot2_Expression240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression240", None)
        self.__iot2_Expression240 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_OpaqueAction"):
                opp_val = getattr(old_value, "iot2_OpaqueAction", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_OpaqueAction"):
                opp_val = getattr(value, "iot2_OpaqueAction", None)
                if opp_val is None:
                    setattr(value, "iot2_OpaqueAction", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_Expression135(self):
        return self.__iot2_Expression135

    @iot2_Expression135.setter
    def iot2_Expression135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression135", None)
        self.__iot2_Expression135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Larger134"):
                opp_val = getattr(old_value, "iot2_Expression_Larger134", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Larger134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Larger134"):
                opp_val = getattr(value, "iot2_Expression_Larger134", None)
                setattr(value, "iot2_Expression_Larger134", self)

    @property
    def iot2_Expression140(self):
        return self.__iot2_Expression140

    @iot2_Expression140.setter
    def iot2_Expression140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression140", None)
        self.__iot2_Expression140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Larger_Equal139"):
                opp_val = getattr(old_value, "iot2_Expression_Larger_Equal139", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Larger_Equal139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Larger_Equal139"):
                opp_val = getattr(value, "iot2_Expression_Larger_Equal139", None)
                setattr(value, "iot2_Expression_Larger_Equal139", self)

    @property
    def iot2_Expression218(self):
        return self.__iot2_Expression218

    @iot2_Expression218.setter
    def iot2_Expression218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression218", None)
        self.__iot2_Expression218 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_AccessMember"):
                opp_val = getattr(old_value, "iot2_Expression_AccessMember", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_AccessMember", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_AccessMember"):
                opp_val = getattr(value, "iot2_Expression_AccessMember", None)
                setattr(value, "iot2_Expression_AccessMember", self)

    @property
    def iot2_Expression101(self):
        return self.__iot2_Expression101

    @iot2_Expression101.setter
    def iot2_Expression101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression101", None)
        self.__iot2_Expression101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Functioncall_Arguments"):
                opp_val = getattr(old_value, "iot2_Functioncall_Arguments", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Functioncall_Arguments"):
                opp_val = getattr(value, "iot2_Functioncall_Arguments", None)
                if opp_val is None:
                    setattr(value, "iot2_Functioncall_Arguments", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_Expression79(self):
        return self.__iot2_Expression79

    @iot2_Expression79.setter
    def iot2_Expression79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression79", None)
        self.__iot2_Expression79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_For_Numeric78"):
                opp_val = getattr(old_value, "iot2_Statement_For_Numeric78", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_For_Numeric78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_For_Numeric78"):
                opp_val = getattr(value, "iot2_Statement_For_Numeric78", None)
                setattr(value, "iot2_Statement_For_Numeric78", self)

    @property
    def iot2_Expression47(self):
        return self.__iot2_Expression47

    @iot2_Expression47.setter
    def iot2_Expression47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression47", None)
        self.__iot2_Expression47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_While"):
                opp_val = getattr(old_value, "iot2_Statement_While", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_While", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_While"):
                opp_val = getattr(value, "iot2_Statement_While", None)
                setattr(value, "iot2_Statement_While", self)

    @property
    def iot2_Expression162(self):
        return self.__iot2_Expression162

    @iot2_Expression162.setter
    def iot2_Expression162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression162", None)
        self.__iot2_Expression162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Concatenation"):
                opp_val = getattr(old_value, "iot2_Expression_Concatenation", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Concatenation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Concatenation"):
                opp_val = getattr(value, "iot2_Expression_Concatenation", None)
                setattr(value, "iot2_Expression_Concatenation", self)

    @property
    def iot2_Expression68(self):
        return self.__iot2_Expression68

    @iot2_Expression68.setter
    def iot2_Expression68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression68", None)
        self.__iot2_Expression68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_If_Then_Else_ElseIfPart67"):
                opp_val = getattr(old_value, "iot2_Statement_If_Then_Else_ElseIfPart67", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_If_Then_Else_ElseIfPart67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_If_Then_Else_ElseIfPart67"):
                opp_val = getattr(value, "iot2_Statement_If_Then_Else_ElseIfPart67", None)
                setattr(value, "iot2_Statement_If_Then_Else_ElseIfPart67", self)

    @property
    def iot2_Expression177(self):
        return self.__iot2_Expression177

    @iot2_Expression177.setter
    def iot2_Expression177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression177", None)
        self.__iot2_Expression177 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Multiplication"):
                opp_val = getattr(old_value, "iot2_Expression_Multiplication", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Multiplication", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Multiplication"):
                opp_val = getattr(value, "iot2_Expression_Multiplication", None)
                setattr(value, "iot2_Expression_Multiplication", self)

    @property
    def iot2_Expression170(self):
        return self.__iot2_Expression170

    @iot2_Expression170.setter
    def iot2_Expression170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression170", None)
        self.__iot2_Expression170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Plus169"):
                opp_val = getattr(old_value, "iot2_Expression_Plus169", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Plus169", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Plus169"):
                opp_val = getattr(value, "iot2_Expression_Plus169", None)
                setattr(value, "iot2_Expression_Plus169", self)

    @property
    def iot2_Expression150(self):
        return self.__iot2_Expression150

    @iot2_Expression150.setter
    def iot2_Expression150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression150", None)
        self.__iot2_Expression150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Smaller_Equal149"):
                opp_val = getattr(old_value, "iot2_Expression_Smaller_Equal149", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Smaller_Equal149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Smaller_Equal149"):
                opp_val = getattr(value, "iot2_Expression_Smaller_Equal149", None)
                setattr(value, "iot2_Expression_Smaller_Equal149", self)

    @property
    def iot2_Expression208(self):
        return self.__iot2_Expression208

    @iot2_Expression208.setter
    def iot2_Expression208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression208", None)
        self.__iot2_Expression208 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_CallFunction"):
                opp_val = getattr(old_value, "iot2_Expression_CallFunction", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_CallFunction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_CallFunction"):
                opp_val = getattr(value, "iot2_Expression_CallFunction", None)
                setattr(value, "iot2_Expression_CallFunction", self)

    @property
    def iot2_Expression194(self):
        return self.__iot2_Expression194

    @iot2_Expression194.setter
    def iot2_Expression194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression194", None)
        self.__iot2_Expression194 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Length"):
                opp_val = getattr(old_value, "iot2_Expression_Length", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Length", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Length"):
                opp_val = getattr(value, "iot2_Expression_Length", None)
                setattr(value, "iot2_Expression_Length", self)

    @property
    def iot2_Expression185(self):
        return self.__iot2_Expression185

    @iot2_Expression185.setter
    def iot2_Expression185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression185", None)
        self.__iot2_Expression185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Division184"):
                opp_val = getattr(old_value, "iot2_Expression_Division184", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Division184", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Division184"):
                opp_val = getattr(value, "iot2_Expression_Division184", None)
                setattr(value, "iot2_Expression_Division184", self)

    @property
    def iot2_Expression157(self):
        return self.__iot2_Expression157

    @iot2_Expression157.setter
    def iot2_Expression157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression157", None)
        self.__iot2_Expression157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Not_Equal"):
                opp_val = getattr(old_value, "iot2_Expression_Not_Equal", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Not_Equal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Not_Equal"):
                opp_val = getattr(value, "iot2_Expression_Not_Equal", None)
                setattr(value, "iot2_Expression_Not_Equal", self)

    @property
    def iot2_Expression127(self):
        return self.__iot2_Expression127

    @iot2_Expression127.setter
    def iot2_Expression127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression127", None)
        self.__iot2_Expression127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_And"):
                opp_val = getattr(old_value, "iot2_Expression_And", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_And", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_And"):
                opp_val = getattr(value, "iot2_Expression_And", None)
                setattr(value, "iot2_Expression_And", self)

    @property
    def iot2_Expression107(self):
        return self.__iot2_Expression107

    @iot2_Expression107.setter
    def iot2_Expression107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression107", None)
        self.__iot2_Expression107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_Assignment"):
                opp_val = getattr(old_value, "iot2_Statement_Assignment", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_Assignment"):
                opp_val = getattr(value, "iot2_Statement_Assignment", None)
                if opp_val is None:
                    setattr(value, "iot2_Statement_Assignment", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_Expression132(self):
        return self.__iot2_Expression132

    @iot2_Expression132.setter
    def iot2_Expression132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression132", None)
        self.__iot2_Expression132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Larger"):
                opp_val = getattr(old_value, "iot2_Expression_Larger", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Larger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Larger"):
                opp_val = getattr(value, "iot2_Expression_Larger", None)
                setattr(value, "iot2_Expression_Larger", self)

    @property
    def iot2_Expression130(self):
        return self.__iot2_Expression130

    @iot2_Expression130.setter
    def iot2_Expression130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression130", None)
        self.__iot2_Expression130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_And129"):
                opp_val = getattr(old_value, "iot2_Expression_And129", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_And129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_And129"):
                opp_val = getattr(value, "iot2_Expression_And129", None)
                setattr(value, "iot2_Expression_And129", self)

    @property
    def iot2_Expression160(self):
        return self.__iot2_Expression160

    @iot2_Expression160.setter
    def iot2_Expression160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression160", None)
        self.__iot2_Expression160 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Not_Equal159"):
                opp_val = getattr(old_value, "iot2_Expression_Not_Equal159", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Not_Equal159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Not_Equal159"):
                opp_val = getattr(value, "iot2_Expression_Not_Equal159", None)
                setattr(value, "iot2_Expression_Not_Equal159", self)

    @property
    def iot2_Expression76(self):
        return self.__iot2_Expression76

    @iot2_Expression76.setter
    def iot2_Expression76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression76", None)
        self.__iot2_Expression76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_For_Numeric75"):
                opp_val = getattr(old_value, "iot2_Statement_For_Numeric75", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_For_Numeric75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_For_Numeric75"):
                opp_val = getattr(value, "iot2_Statement_For_Numeric75", None)
                setattr(value, "iot2_Statement_For_Numeric75", self)

    @property
    def iot2_Expression190(self):
        return self.__iot2_Expression190

    @iot2_Expression190.setter
    def iot2_Expression190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression190", None)
        self.__iot2_Expression190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Modulo189"):
                opp_val = getattr(old_value, "iot2_Expression_Modulo189", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Modulo189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Modulo189"):
                opp_val = getattr(value, "iot2_Expression_Modulo189", None)
                setattr(value, "iot2_Expression_Modulo189", self)

    @property
    def iot2_Expression147(self):
        return self.__iot2_Expression147

    @iot2_Expression147.setter
    def iot2_Expression147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression147", None)
        self.__iot2_Expression147 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Smaller_Equal"):
                opp_val = getattr(old_value, "iot2_Expression_Smaller_Equal", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Smaller_Equal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Smaller_Equal"):
                opp_val = getattr(value, "iot2_Expression_Smaller_Equal", None)
                setattr(value, "iot2_Expression_Smaller_Equal", self)

    @property
    def iot2_Expression142(self):
        return self.__iot2_Expression142

    @iot2_Expression142.setter
    def iot2_Expression142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression142", None)
        self.__iot2_Expression142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Smaller"):
                opp_val = getattr(old_value, "iot2_Expression_Smaller", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Smaller", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Smaller"):
                opp_val = getattr(value, "iot2_Expression_Smaller", None)
                setattr(value, "iot2_Expression_Smaller", self)

    @property
    def iot2_Expression167(self):
        return self.__iot2_Expression167

    @iot2_Expression167.setter
    def iot2_Expression167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression167", None)
        self.__iot2_Expression167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Plus"):
                opp_val = getattr(old_value, "iot2_Expression_Plus", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Plus", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Plus"):
                opp_val = getattr(value, "iot2_Expression_Plus", None)
                setattr(value, "iot2_Expression_Plus", self)

    @property
    def iot2_Expression73(self):
        return self.__iot2_Expression73

    @iot2_Expression73.setter
    def iot2_Expression73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression73", None)
        self.__iot2_Expression73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_For_Numeric"):
                opp_val = getattr(old_value, "iot2_Statement_For_Numeric", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_For_Numeric", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_For_Numeric"):
                opp_val = getattr(value, "iot2_Statement_For_Numeric", None)
                setattr(value, "iot2_Statement_For_Numeric", self)

    @property
    def iot2_Expression84(self):
        return self.__iot2_Expression84

    @iot2_Expression84.setter
    def iot2_Expression84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression84", None)
        self.__iot2_Expression84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_For_Generic"):
                opp_val = getattr(old_value, "iot2_Statement_For_Generic", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_For_Generic"):
                opp_val = getattr(value, "iot2_Statement_For_Generic", None)
                if opp_val is None:
                    setattr(value, "iot2_Statement_For_Generic", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_Expression196(self):
        return self.__iot2_Expression196

    @iot2_Expression196.setter
    def iot2_Expression196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression196", None)
        self.__iot2_Expression196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Invert"):
                opp_val = getattr(old_value, "iot2_Expression_Invert", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Invert", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Invert"):
                opp_val = getattr(value, "iot2_Expression_Invert", None)
                setattr(value, "iot2_Expression_Invert", self)

    @property
    def iot2_Expression198(self):
        return self.__iot2_Expression198

    @iot2_Expression198.setter
    def iot2_Expression198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression198", None)
        self.__iot2_Expression198 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Exponentiation"):
                opp_val = getattr(old_value, "iot2_Expression_Exponentiation", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Exponentiation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Exponentiation"):
                opp_val = getattr(value, "iot2_Expression_Exponentiation", None)
                setattr(value, "iot2_Expression_Exponentiation", self)

    @property
    def iot2_Expression187(self):
        return self.__iot2_Expression187

    @iot2_Expression187.setter
    def iot2_Expression187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression187", None)
        self.__iot2_Expression187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Modulo"):
                opp_val = getattr(old_value, "iot2_Expression_Modulo", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Modulo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Modulo"):
                opp_val = getattr(value, "iot2_Expression_Modulo", None)
                setattr(value, "iot2_Expression_Modulo", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class IDLType:

    pass
class iot2_PrimitiveDef(IDLType):

    def __init__(self, kind: str):
        self.kind = kind
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

class iot2_IDLType(ABC):

    def __init__(self, typeCode: str, iot2_IDLType: "iot2_Typed" = None):
        self.typeCode = typeCode
        self.iot2_IDLType = iot2_IDLType
        
    @property
    def typeCode(self) -> str:
        return self.__typeCode

    @typeCode.setter
    def typeCode(self, typeCode: str):
        self.__typeCode = typeCode

    @property
    def iot2_IDLType(self):
        return self.__iot2_IDLType

    @iot2_IDLType.setter
    def iot2_IDLType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_IDLType__iot2_IDLType", None)
        self.__iot2_IDLType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Typed"):
                opp_val = getattr(old_value, "iot2_Typed", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Typed", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Typed"):
                opp_val = getattr(value, "iot2_Typed", None)
                setattr(value, "iot2_Typed", self)

class iot2_Typed(ABC):

    pass
class iot2_NamedElement(ABC):

    def __init__(self, identifier: str, name: str):
        self.identifier = identifier
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Block(Chunk):

    def __init__(self, iot2_Block: "iot2_OperationDef" = None, iot2_Block41: set["iot2_Statement"] = None, iot2_Block43: "iot2_LastStatement" = None, iot2_Block45: "iot2_Statement_Block" = None, iot2_Block50: "iot2_Statement_While" = None, iot2_Block52: "iot2_Statement_Repeat" = None, iot2_Block60: "iot2_Statement_If_Then_Else" = None, iot2_Block65: "iot2_Statement_If_Then_Else" = None, iot2_Block71: "iot2_Statement_If_Then_Else_ElseIfPart" = None, iot2_Block82: "iot2_Statement_For_Numeric" = None, iot2_Block87: "iot2_Statement_For_Generic" = None, iot2_Block99: "iot2_Function" = None):
        self.iot2_Block = iot2_Block
        self.iot2_Block41 = iot2_Block41 if iot2_Block41 is not None else set()
        self.iot2_Block43 = iot2_Block43
        self.iot2_Block45 = iot2_Block45
        self.iot2_Block50 = iot2_Block50
        self.iot2_Block52 = iot2_Block52
        self.iot2_Block60 = iot2_Block60
        self.iot2_Block65 = iot2_Block65
        self.iot2_Block71 = iot2_Block71
        self.iot2_Block82 = iot2_Block82
        self.iot2_Block87 = iot2_Block87
        self.iot2_Block99 = iot2_Block99
        
    @property
    def iot2_Block52(self):
        return self.__iot2_Block52

    @iot2_Block52.setter
    def iot2_Block52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Block__iot2_Block52", None)
        self.__iot2_Block52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_Repeat"):
                opp_val = getattr(old_value, "iot2_Statement_Repeat", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_Repeat", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_Repeat"):
                opp_val = getattr(value, "iot2_Statement_Repeat", None)
                setattr(value, "iot2_Statement_Repeat", self)

    @property
    def iot2_Block(self):
        return self.__iot2_Block

    @iot2_Block.setter
    def iot2_Block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Block__iot2_Block", None)
        self.__iot2_Block = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_OperationDef26"):
                opp_val = getattr(old_value, "iot2_OperationDef26", None)
                if opp_val == self:
                    setattr(old_value, "iot2_OperationDef26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_OperationDef26"):
                opp_val = getattr(value, "iot2_OperationDef26", None)
                setattr(value, "iot2_OperationDef26", self)

    @property
    def iot2_Block60(self):
        return self.__iot2_Block60

    @iot2_Block60.setter
    def iot2_Block60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Block__iot2_Block60", None)
        self.__iot2_Block60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_If_Then_Else59"):
                opp_val = getattr(old_value, "iot2_Statement_If_Then_Else59", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_If_Then_Else59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_If_Then_Else59"):
                opp_val = getattr(value, "iot2_Statement_If_Then_Else59", None)
                setattr(value, "iot2_Statement_If_Then_Else59", self)

    @property
    def iot2_Block41(self):
        return self.__iot2_Block41

    @iot2_Block41.setter
    def iot2_Block41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Block__iot2_Block41", None)
        self.__iot2_Block41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_Statement"):
                    opp_val = getattr(item, "iot2_Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_Statement"):
                    opp_val = getattr(item, "iot2_Statement", None)
                    
                    setattr(item, "iot2_Statement", self)
                    

    @property
    def iot2_Block99(self):
        return self.__iot2_Block99

    @iot2_Block99.setter
    def iot2_Block99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Block__iot2_Block99", None)
        self.__iot2_Block99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Function98"):
                opp_val = getattr(old_value, "iot2_Function98", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Function98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Function98"):
                opp_val = getattr(value, "iot2_Function98", None)
                setattr(value, "iot2_Function98", self)

    @property
    def iot2_Block50(self):
        return self.__iot2_Block50

    @iot2_Block50.setter
    def iot2_Block50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Block__iot2_Block50", None)
        self.__iot2_Block50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_While49"):
                opp_val = getattr(old_value, "iot2_Statement_While49", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_While49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_While49"):
                opp_val = getattr(value, "iot2_Statement_While49", None)
                setattr(value, "iot2_Statement_While49", self)

    @property
    def iot2_Block82(self):
        return self.__iot2_Block82

    @iot2_Block82.setter
    def iot2_Block82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Block__iot2_Block82", None)
        self.__iot2_Block82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_For_Numeric81"):
                opp_val = getattr(old_value, "iot2_Statement_For_Numeric81", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_For_Numeric81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_For_Numeric81"):
                opp_val = getattr(value, "iot2_Statement_For_Numeric81", None)
                setattr(value, "iot2_Statement_For_Numeric81", self)

    @property
    def iot2_Block65(self):
        return self.__iot2_Block65

    @iot2_Block65.setter
    def iot2_Block65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Block__iot2_Block65", None)
        self.__iot2_Block65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_If_Then_Else64"):
                opp_val = getattr(old_value, "iot2_Statement_If_Then_Else64", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_If_Then_Else64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_If_Then_Else64"):
                opp_val = getattr(value, "iot2_Statement_If_Then_Else64", None)
                setattr(value, "iot2_Statement_If_Then_Else64", self)

    @property
    def iot2_Block87(self):
        return self.__iot2_Block87

    @iot2_Block87.setter
    def iot2_Block87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Block__iot2_Block87", None)
        self.__iot2_Block87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_For_Generic86"):
                opp_val = getattr(old_value, "iot2_Statement_For_Generic86", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_For_Generic86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_For_Generic86"):
                opp_val = getattr(value, "iot2_Statement_For_Generic86", None)
                setattr(value, "iot2_Statement_For_Generic86", self)

    @property
    def iot2_Block43(self):
        return self.__iot2_Block43

    @iot2_Block43.setter
    def iot2_Block43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Block__iot2_Block43", None)
        self.__iot2_Block43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_LastStatement"):
                opp_val = getattr(old_value, "iot2_LastStatement", None)
                if opp_val == self:
                    setattr(old_value, "iot2_LastStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_LastStatement"):
                opp_val = getattr(value, "iot2_LastStatement", None)
                setattr(value, "iot2_LastStatement", self)

    @property
    def iot2_Block71(self):
        return self.__iot2_Block71

    @iot2_Block71.setter
    def iot2_Block71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Block__iot2_Block71", None)
        self.__iot2_Block71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_If_Then_Else_ElseIfPart70"):
                opp_val = getattr(old_value, "iot2_Statement_If_Then_Else_ElseIfPart70", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_If_Then_Else_ElseIfPart70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_If_Then_Else_ElseIfPart70"):
                opp_val = getattr(value, "iot2_Statement_If_Then_Else_ElseIfPart70", None)
                setattr(value, "iot2_Statement_If_Then_Else_ElseIfPart70", self)

    @property
    def iot2_Block45(self):
        return self.__iot2_Block45

    @iot2_Block45.setter
    def iot2_Block45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Block__iot2_Block45", None)
        self.__iot2_Block45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_Block"):
                opp_val = getattr(old_value, "iot2_Statement_Block", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_Block", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_Block"):
                opp_val = getattr(value, "iot2_Statement_Block", None)
                setattr(value, "iot2_Statement_Block", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class Typed:

    pass
class iot2_ParameterDef(Typed):

    def __init__(self, identifier: str, direction: str, iot2_ParameterDef: "iot2_OperationDef" = None):
        self.identifier = identifier
        self.direction = direction
        self.iot2_ParameterDef = iot2_ParameterDef
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def iot2_ParameterDef(self):
        return self.__iot2_ParameterDef

    @iot2_ParameterDef.setter
    def iot2_ParameterDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ParameterDef__iot2_ParameterDef", None)
        self.__iot2_ParameterDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_OperationDef22"):
                opp_val = getattr(old_value, "iot2_OperationDef22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_OperationDef22"):
                opp_val = getattr(value, "iot2_OperationDef22", None)
                if opp_val is None:
                    setattr(value, "iot2_OperationDef22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class iot2_Field(Typed):

    def __init__(self, identifier: str, iot2_Field: "iot2_ExceptionDef" = None, iot2_Field39: "iot2_Expression" = None, iot2_Field96: "iot2_Expression_TableConstructor" = None):
        self.identifier = identifier
        self.iot2_Field = iot2_Field
        self.iot2_Field39 = iot2_Field39
        self.iot2_Field96 = iot2_Field96
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def iot2_Field96(self):
        return self.__iot2_Field96

    @iot2_Field96.setter
    def iot2_Field96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Field__iot2_Field96", None)
        self.__iot2_Field96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_TableConstructor"):
                opp_val = getattr(old_value, "iot2_Expression_TableConstructor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_TableConstructor"):
                opp_val = getattr(value, "iot2_Expression_TableConstructor", None)
                if opp_val is None:
                    setattr(value, "iot2_Expression_TableConstructor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_Field(self):
        return self.__iot2_Field

    @iot2_Field.setter
    def iot2_Field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Field__iot2_Field", None)
        self.__iot2_Field = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_ExceptionDef37"):
                opp_val = getattr(old_value, "iot2_ExceptionDef37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_ExceptionDef37"):
                opp_val = getattr(value, "iot2_ExceptionDef37", None)
                if opp_val is None:
                    setattr(value, "iot2_ExceptionDef37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_Field39(self):
        return self.__iot2_Field39

    @iot2_Field39.setter
    def iot2_Field39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Field__iot2_Field39", None)
        self.__iot2_Field39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression"):
                opp_val = getattr(old_value, "iot2_Expression", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression"):
                opp_val = getattr(value, "iot2_Expression", None)
                setattr(value, "iot2_Expression", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class Contained:

    pass
class iot2_Container(Contained):

    pass
class iot2_TypedefDef(IDLType, Contained):

    pass
class iot2_ExceptionDef(Contained):

    def __init__(self, typeCode: str, iot2_ExceptionDef: "iot2_OperationDef" = None, iot2_ExceptionDef37: set["iot2_Field"] = None):
        self.typeCode = typeCode
        self.iot2_ExceptionDef = iot2_ExceptionDef
        self.iot2_ExceptionDef37 = iot2_ExceptionDef37 if iot2_ExceptionDef37 is not None else set()
        
    @property
    def typeCode(self) -> str:
        return self.__typeCode

    @typeCode.setter
    def typeCode(self, typeCode: str):
        self.__typeCode = typeCode

    @property
    def iot2_ExceptionDef(self):
        return self.__iot2_ExceptionDef

    @iot2_ExceptionDef.setter
    def iot2_ExceptionDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ExceptionDef__iot2_ExceptionDef", None)
        self.__iot2_ExceptionDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_OperationDef24"):
                opp_val = getattr(old_value, "iot2_OperationDef24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_OperationDef24"):
                opp_val = getattr(value, "iot2_OperationDef24", None)
                if opp_val is None:
                    setattr(value, "iot2_OperationDef24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_ExceptionDef37(self):
        return self.__iot2_ExceptionDef37

    @iot2_ExceptionDef37.setter
    def iot2_ExceptionDef37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ExceptionDef__iot2_ExceptionDef37", None)
        self.__iot2_ExceptionDef37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_Field"):
                    opp_val = getattr(item, "iot2_Field", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_Field", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_Field"):
                    opp_val = getattr(item, "iot2_Field", None)
                    
                    setattr(item, "iot2_Field", self)
                    

class iot2_Variable:

    def __init__(self, name: str, iot2_Variable: "iot2_Activity" = None, iot2_Variable20: "iot2_Activity" = None, iot2_Variable245: "iot2_Value" = None, iot2_Variable247: "iot2_Value" = None, iot2_Variable270: "iot2_InputValue" = None):
        self.name = name
        self.iot2_Variable = iot2_Variable
        self.iot2_Variable20 = iot2_Variable20
        self.iot2_Variable245 = iot2_Variable245
        self.iot2_Variable247 = iot2_Variable247
        self.iot2_Variable270 = iot2_Variable270
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iot2_Variable245(self):
        return self.__iot2_Variable245

    @iot2_Variable245.setter
    def iot2_Variable245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Variable__iot2_Variable245", None)
        self.__iot2_Variable245 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Value"):
                opp_val = getattr(old_value, "iot2_Value", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Value", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Value"):
                opp_val = getattr(value, "iot2_Value", None)
                setattr(value, "iot2_Value", self)

    @property
    def iot2_Variable(self):
        return self.__iot2_Variable

    @iot2_Variable.setter
    def iot2_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Variable__iot2_Variable", None)
        self.__iot2_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Activity17"):
                opp_val = getattr(old_value, "iot2_Activity17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Activity17"):
                opp_val = getattr(value, "iot2_Activity17", None)
                if opp_val is None:
                    setattr(value, "iot2_Activity17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_Variable270(self):
        return self.__iot2_Variable270

    @iot2_Variable270.setter
    def iot2_Variable270(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Variable__iot2_Variable270", None)
        self.__iot2_Variable270 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_InputValue269"):
                opp_val = getattr(old_value, "iot2_InputValue269", None)
                if opp_val == self:
                    setattr(old_value, "iot2_InputValue269", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_InputValue269"):
                opp_val = getattr(value, "iot2_InputValue269", None)
                setattr(value, "iot2_InputValue269", self)

    @property
    def iot2_Variable247(self):
        return self.__iot2_Variable247

    @iot2_Variable247.setter
    def iot2_Variable247(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Variable__iot2_Variable247", None)
        self.__iot2_Variable247 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Value248"):
                opp_val = getattr(old_value, "iot2_Value248", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Value248", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Value248"):
                opp_val = getattr(value, "iot2_Value248", None)
                setattr(value, "iot2_Value248", self)

    @property
    def iot2_Variable20(self):
        return self.__iot2_Variable20

    @iot2_Variable20.setter
    def iot2_Variable20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Variable__iot2_Variable20", None)
        self.__iot2_Variable20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Activity19"):
                opp_val = getattr(old_value, "iot2_Activity19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Activity19"):
                opp_val = getattr(value, "iot2_Activity19", None)
                if opp_val is None:
                    setattr(value, "iot2_Activity19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

    def print(self):
        # TODO: Implement print method
        pass

    def init(self, c: str):
        # TODO: Implement init method
        pass

class NamedElement:

    pass
class iot2_ActivityEdge(NamedElement):

    def __init__(self, iot2_ActivityEdge: "iot2_Activity" = None, 223: "iot2_ActivityNode" = None, 226: "iot2_ActivityNode" = None, 231: "iot2_ActivityNode" = None, 234: "iot2_ActivityNode" = None, iot2_ActivityEdge237: set["iot2_Offer"] = None):
        self.iot2_ActivityEdge = iot2_ActivityEdge
        self.223 = 223
        self.226 = 226
        self.231 = 231
        self.234 = 234
        self.iot2_ActivityEdge237 = iot2_ActivityEdge237 if iot2_ActivityEdge237 is not None else set()
        
    @property
    def iot2_ActivityEdge237(self):
        return self.__iot2_ActivityEdge237

    @iot2_ActivityEdge237.setter
    def iot2_ActivityEdge237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityEdge__iot2_ActivityEdge237", None)
        self.__iot2_ActivityEdge237 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_Offer"):
                    opp_val = getattr(item, "iot2_Offer", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_Offer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_Offer"):
                    opp_val = getattr(item, "iot2_Offer", None)
                    
                    setattr(item, "iot2_Offer", self)
                    

    @property
    def 234(self):
        return self.__234

    @234.setter
    def 234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityEdge__234", None)
        self.__234 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "235"):
                opp_val = getattr(old_value, "235", None)
                if opp_val == self:
                    setattr(old_value, "235", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "235"):
                opp_val = getattr(value, "235", None)
                setattr(value, "235", self)

    @property
    def iot2_ActivityEdge(self):
        return self.__iot2_ActivityEdge

    @iot2_ActivityEdge.setter
    def iot2_ActivityEdge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityEdge__iot2_ActivityEdge", None)
        self.__iot2_ActivityEdge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Activity15"):
                opp_val = getattr(old_value, "iot2_Activity15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Activity15"):
                opp_val = getattr(value, "iot2_Activity15", None)
                if opp_val is None:
                    setattr(value, "iot2_Activity15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 231(self):
        return self.__231

    @231.setter
    def 231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityEdge__231", None)
        self.__231 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "232"):
                opp_val = getattr(old_value, "232", None)
                if opp_val == self:
                    setattr(old_value, "232", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "232"):
                opp_val = getattr(value, "232", None)
                setattr(value, "232", self)

    @property
    def 223(self):
        return self.__223

    @223.setter
    def 223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityEdge__223", None)
        self.__223 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "222"):
                opp_val = getattr(old_value, "222", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "222"):
                opp_val = getattr(value, "222", None)
                if opp_val is None:
                    setattr(value, "222", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 226(self):
        return self.__226

    @226.setter
    def 226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityEdge__226", None)
        self.__226 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "225"):
                opp_val = getattr(old_value, "225", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "225"):
                opp_val = getattr(value, "225", None)
                if opp_val is None:
                    setattr(value, "225", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def hasOffer(self):
        # TODO: Implement hasOffer method
        pass

    def takeOfferedTokens(self) -> str:
        # TODO: Implement takeOfferedTokens method
        pass

    def sendOffer(self, tokens: str):
        # TODO: Implement sendOffer method
        pass

class iot2_Contained(NamedElement):

    def __init__(self, absoluteName: str, repositoryId: str, version: str, 28: "iot2_Container" = None, 32: "iot2_Container" = None):
        self.absoluteName = absoluteName
        self.repositoryId = repositoryId
        self.version = version
        self.28 = 28
        self.32 = 32
        
    @property
    def repositoryId(self) -> str:
        return self.__repositoryId

    @repositoryId.setter
    def repositoryId(self, repositoryId: str):
        self.__repositoryId = repositoryId

    @property
    def absoluteName(self) -> str:
        return self.__absoluteName

    @absoluteName.setter
    def absoluteName(self, absoluteName: str):
        self.__absoluteName = absoluteName

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def 32(self):
        return self.__32

    @32.setter
    def 32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Contained__32", None)
        self.__32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "31"):
                opp_val = getattr(old_value, "31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "31"):
                opp_val = getattr(value, "31", None)
                if opp_val is None:
                    setattr(value, "31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 28(self):
        return self.__28

    @28.setter
    def 28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Contained__28", None)
        self.__28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "29"):
                opp_val = getattr(old_value, "29", None)
                if opp_val == self:
                    setattr(old_value, "29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "29"):
                opp_val = getattr(value, "29", None)
                setattr(value, "29", self)

class iot2_ActivityNode(NamedElement):

    def __init__(self, running: str, 13: "iot2_Activity" = None, 222: set["iot2_ActivityEdge"] = None, 225: set["iot2_ActivityEdge"] = None, 228: "iot2_Activity" = None, 232: "iot2_ActivityEdge" = None, 235: "iot2_ActivityEdge" = None, iot2_ActivityNode: "iot2_Token" = None, iot2_ActivityNode291: "iot2_Trace" = None):
        self.running = running
        self.13 = 13
        self.222 = 222 if 222 is not None else set()
        self.225 = 225 if 225 is not None else set()
        self.228 = 228
        self.232 = 232
        self.235 = 235
        self.iot2_ActivityNode = iot2_ActivityNode
        self.iot2_ActivityNode291 = iot2_ActivityNode291
        
    @property
    def running(self) -> str:
        return self.__running

    @running.setter
    def running(self, running: str):
        self.__running = running

    @property
    def iot2_ActivityNode291(self):
        return self.__iot2_ActivityNode291

    @iot2_ActivityNode291.setter
    def iot2_ActivityNode291(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityNode__iot2_ActivityNode291", None)
        self.__iot2_ActivityNode291 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Trace290"):
                opp_val = getattr(old_value, "iot2_Trace290", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Trace290"):
                opp_val = getattr(value, "iot2_Trace290", None)
                if opp_val is None:
                    setattr(value, "iot2_Trace290", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_ActivityNode(self):
        return self.__iot2_ActivityNode

    @iot2_ActivityNode.setter
    def iot2_ActivityNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityNode__iot2_ActivityNode", None)
        self.__iot2_ActivityNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Token276"):
                opp_val = getattr(old_value, "iot2_Token276", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Token276", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Token276"):
                opp_val = getattr(value, "iot2_Token276", None)
                setattr(value, "iot2_Token276", self)

    @property
    def 225(self):
        return self.__225

    @225.setter
    def 225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityNode__225", None)
        self.__225 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "226"):
                    opp_val = getattr(item, "226", None)
                    
                    if opp_val == self:
                        setattr(item, "226", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "226"):
                    opp_val = getattr(item, "226", None)
                    
                    setattr(item, "226", self)
                    

    @property
    def 232(self):
        return self.__232

    @232.setter
    def 232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityNode__232", None)
        self.__232 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "231"):
                opp_val = getattr(old_value, "231", None)
                if opp_val == self:
                    setattr(old_value, "231", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "231"):
                opp_val = getattr(value, "231", None)
                setattr(value, "231", self)

    @property
    def 222(self):
        return self.__222

    @222.setter
    def 222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityNode__222", None)
        self.__222 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "223"):
                    opp_val = getattr(item, "223", None)
                    
                    if opp_val == self:
                        setattr(item, "223", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "223"):
                    opp_val = getattr(item, "223", None)
                    
                    setattr(item, "223", self)
                    

    @property
    def 235(self):
        return self.__235

    @235.setter
    def 235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityNode__235", None)
        self.__235 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "234"):
                opp_val = getattr(old_value, "234", None)
                if opp_val == self:
                    setattr(old_value, "234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "234"):
                opp_val = getattr(value, "234", None)
                setattr(value, "234", self)

    @property
    def 13(self):
        return self.__13

    @13.setter
    def 13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityNode__13", None)
        self.__13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, ""):
                opp_val = getattr(old_value, "", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, ""):
                opp_val = getattr(value, "", None)
                if opp_val is None:
                    setattr(value, "", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 228(self):
        return self.__228

    @228.setter
    def 228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityNode__228", None)
        self.__228 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "229"):
                opp_val = getattr(old_value, "229", None)
                if opp_val == self:
                    setattr(old_value, "229", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "229"):
                opp_val = getattr(value, "229", None)
                setattr(value, "229", self)

    def isReady(self):
        # TODO: Implement isReady method
        pass

    def sendOffers(self, tokens: str):
        # TODO: Implement sendOffers method
        pass

    def takeOfferdTokens(self) -> str:
        # TODO: Implement takeOfferdTokens method
        pass

    def addTokens(self, tokens: str):
        # TODO: Implement addTokens method
        pass

    def removeToken(self, token: str):
        # TODO: Implement removeToken method
        pass

    def terminate(self):
        # TODO: Implement terminate method
        pass

    def hasOffers(self):
        # TODO: Implement hasOffers method
        pass

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class HWComponent:

    pass
class iot2_Actuator(HWComponent):

    pass
class iot2_Sensor(HWComponent):

    pass
class iot2_OperationDef(Contained, Typed):

    def __init__(self, isOneway: bool, contexts: str, iot2_OperationDef: "iot2_HWComponent" = None, iot2_OperationDef22: set["iot2_ParameterDef"] = None, iot2_OperationDef24: set["iot2_ExceptionDef"] = None, iot2_OperationDef26: "iot2_Block" = None, iot2_OperationDef243: "iot2_OpaqueAction" = None):
        self.isOneway = isOneway
        self.contexts = contexts
        self.iot2_OperationDef = iot2_OperationDef
        self.iot2_OperationDef22 = iot2_OperationDef22 if iot2_OperationDef22 is not None else set()
        self.iot2_OperationDef24 = iot2_OperationDef24 if iot2_OperationDef24 is not None else set()
        self.iot2_OperationDef26 = iot2_OperationDef26
        self.iot2_OperationDef243 = iot2_OperationDef243
        
    @property
    def isOneway(self) -> bool:
        return self.__isOneway

    @isOneway.setter
    def isOneway(self, isOneway: bool):
        self.__isOneway = isOneway

    @property
    def contexts(self) -> str:
        return self.__contexts

    @contexts.setter
    def contexts(self, contexts: str):
        self.__contexts = contexts

    @property
    def iot2_OperationDef(self):
        return self.__iot2_OperationDef

    @iot2_OperationDef.setter
    def iot2_OperationDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_OperationDef__iot2_OperationDef", None)
        self.__iot2_OperationDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_HWComponent11"):
                opp_val = getattr(old_value, "iot2_HWComponent11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_HWComponent11"):
                opp_val = getattr(value, "iot2_HWComponent11", None)
                if opp_val is None:
                    setattr(value, "iot2_HWComponent11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_OperationDef22(self):
        return self.__iot2_OperationDef22

    @iot2_OperationDef22.setter
    def iot2_OperationDef22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_OperationDef__iot2_OperationDef22", None)
        self.__iot2_OperationDef22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_ParameterDef"):
                    opp_val = getattr(item, "iot2_ParameterDef", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_ParameterDef", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_ParameterDef"):
                    opp_val = getattr(item, "iot2_ParameterDef", None)
                    
                    setattr(item, "iot2_ParameterDef", self)
                    

    @property
    def iot2_OperationDef243(self):
        return self.__iot2_OperationDef243

    @iot2_OperationDef243.setter
    def iot2_OperationDef243(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_OperationDef__iot2_OperationDef243", None)
        self.__iot2_OperationDef243 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_OpaqueAction242"):
                opp_val = getattr(old_value, "iot2_OpaqueAction242", None)
                if opp_val == self:
                    setattr(old_value, "iot2_OpaqueAction242", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_OpaqueAction242"):
                opp_val = getattr(value, "iot2_OpaqueAction242", None)
                setattr(value, "iot2_OpaqueAction242", self)

    @property
    def iot2_OperationDef26(self):
        return self.__iot2_OperationDef26

    @iot2_OperationDef26.setter
    def iot2_OperationDef26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_OperationDef__iot2_OperationDef26", None)
        self.__iot2_OperationDef26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Block"):
                opp_val = getattr(old_value, "iot2_Block", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Block", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Block"):
                opp_val = getattr(value, "iot2_Block", None)
                setattr(value, "iot2_Block", self)

    @property
    def iot2_OperationDef24(self):
        return self.__iot2_OperationDef24

    @iot2_OperationDef24.setter
    def iot2_OperationDef24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_OperationDef__iot2_OperationDef24", None)
        self.__iot2_OperationDef24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_ExceptionDef"):
                    opp_val = getattr(item, "iot2_ExceptionDef", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_ExceptionDef", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_ExceptionDef"):
                    opp_val = getattr(item, "iot2_ExceptionDef", None)
                    
                    setattr(item, "iot2_ExceptionDef", self)
                    

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class iot2_Activity(NamedElement):

    def __init__(self, iot2_Activity: "iot2_Sketch" = None, : set["iot2_ActivityNode"] = None, iot2_Activity15: set["iot2_ActivityEdge"] = None, iot2_Activity17: set["iot2_Variable"] = None, iot2_Activity19: set["iot2_Variable"] = None, 229: "iot2_ActivityNode" = None, iot2_Activity280: "iot2_Context" = None):
        self.iot2_Activity = iot2_Activity
        self. =  if  is not None else set()
        self.iot2_Activity15 = iot2_Activity15 if iot2_Activity15 is not None else set()
        self.iot2_Activity17 = iot2_Activity17 if iot2_Activity17 is not None else set()
        self.iot2_Activity19 = iot2_Activity19 if iot2_Activity19 is not None else set()
        self.229 = 229
        self.iot2_Activity280 = iot2_Activity280
        
    @property
    def iot2_Activity(self):
        return self.__iot2_Activity

    @iot2_Activity.setter
    def iot2_Activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Activity__iot2_Activity", None)
        self.__iot2_Activity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Sketch9"):
                opp_val = getattr(old_value, "iot2_Sketch9", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Sketch9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Sketch9"):
                opp_val = getattr(value, "iot2_Sketch9", None)
                setattr(value, "iot2_Sketch9", self)

    @property
    def iot2_Activity15(self):
        return self.__iot2_Activity15

    @iot2_Activity15.setter
    def iot2_Activity15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Activity__iot2_Activity15", None)
        self.__iot2_Activity15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_ActivityEdge"):
                    opp_val = getattr(item, "iot2_ActivityEdge", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_ActivityEdge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_ActivityEdge"):
                    opp_val = getattr(item, "iot2_ActivityEdge", None)
                    
                    setattr(item, "iot2_ActivityEdge", self)
                    

    @property
    def iot2_Activity19(self):
        return self.__iot2_Activity19

    @iot2_Activity19.setter
    def iot2_Activity19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Activity__iot2_Activity19", None)
        self.__iot2_Activity19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_Variable20"):
                    opp_val = getattr(item, "iot2_Variable20", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_Variable20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_Variable20"):
                    opp_val = getattr(item, "iot2_Variable20", None)
                    
                    setattr(item, "iot2_Variable20", self)
                    

    @property
    def iot2_Activity280(self):
        return self.__iot2_Activity280

    @iot2_Activity280.setter
    def iot2_Activity280(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Activity__iot2_Activity280", None)
        self.__iot2_Activity280 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Context279"):
                opp_val = getattr(old_value, "iot2_Context279", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Context279", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Context279"):
                opp_val = getattr(value, "iot2_Context279", None)
                setattr(value, "iot2_Context279", self)

    @property
    def 229(self):
        return self.__229

    @229.setter
    def 229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Activity__229", None)
        self.__229 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "228"):
                opp_val = getattr(old_value, "228", None)
                if opp_val == self:
                    setattr(old_value, "228", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "228"):
                opp_val = getattr(value, "228", None)
                setattr(value, "228", self)

    @property
    def iot2_Activity17(self):
        return self.__iot2_Activity17

    @iot2_Activity17.setter
    def iot2_Activity17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Activity__iot2_Activity17", None)
        self.__iot2_Activity17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_Variable"):
                    opp_val = getattr(item, "iot2_Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_Variable"):
                    opp_val = getattr(item, "iot2_Variable", None)
                    
                    setattr(item, "iot2_Variable", self)
                    

    @property
    def (self):
        return self.__

    @.setter
    def (self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Activity__", None)
        self.__ = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "13"):
                    opp_val = getattr(item, "13", None)
                    
                    if opp_val == self:
                        setattr(item, "13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "13"):
                    opp_val = getattr(item, "13", None)
                    
                    setattr(item, "13", self)
                    

    def getIntegerVariableValue(self, variableName: str):
        # TODO: Implement getIntegerVariableValue method
        pass

    def getBooleanVariableValue(self, variableName: str):
        # TODO: Implement getBooleanVariableValue method
        pass

    def getVariable(self, variableName: str) -> str:
        # TODO: Implement getVariable method
        pass

    def main(self, value: str):
        # TODO: Implement main method
        pass

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

    def writeTrace(self):
        # TODO: Implement writeTrace method
        pass

    def writeToFile(self):
        # TODO: Implement writeToFile method
        pass

    def reset(self):
        # TODO: Implement reset method
        pass

    def getVariableValue(self, variableName: str) -> str:
        # TODO: Implement getVariableValue method
        pass

    def printTrace(self):
        # TODO: Implement printTrace method
        pass

class iot2_Sketch:

    pass
class iot2_Board:

    def __init__(self, name: str, type: str, iot2_Board: "iot2_System" = None, iot2_Board6: set["iot2_HWComponent"] = None):
        self.name = name
        self.type = type
        self.iot2_Board = iot2_Board
        self.iot2_Board6 = iot2_Board6 if iot2_Board6 is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iot2_Board6(self):
        return self.__iot2_Board6

    @iot2_Board6.setter
    def iot2_Board6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Board__iot2_Board6", None)
        self.__iot2_Board6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_HWComponent7"):
                    opp_val = getattr(item, "iot2_HWComponent7", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_HWComponent7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_HWComponent7"):
                    opp_val = getattr(item, "iot2_HWComponent7", None)
                    
                    setattr(item, "iot2_HWComponent7", self)
                    

    @property
    def iot2_Board(self):
        return self.__iot2_Board

    @iot2_Board.setter
    def iot2_Board(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Board__iot2_Board", None)
        self.__iot2_Board = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_System2"):
                opp_val = getattr(old_value, "iot2_System2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_System2"):
                opp_val = getattr(value, "iot2_System2", None)
                if opp_val is None:
                    setattr(value, "iot2_System2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class iot2_System:

    def __init__(self, name: str, iot2_System: set["iot2_HWComponent"] = None, iot2_System2: set["iot2_Board"] = None, iot2_System4: "iot2_Sketch" = None):
        self.name = name
        self.iot2_System = iot2_System if iot2_System is not None else set()
        self.iot2_System2 = iot2_System2 if iot2_System2 is not None else set()
        self.iot2_System4 = iot2_System4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iot2_System4(self):
        return self.__iot2_System4

    @iot2_System4.setter
    def iot2_System4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_System__iot2_System4", None)
        self.__iot2_System4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Sketch"):
                opp_val = getattr(old_value, "iot2_Sketch", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Sketch", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Sketch"):
                opp_val = getattr(value, "iot2_Sketch", None)
                setattr(value, "iot2_Sketch", self)

    @property
    def iot2_System2(self):
        return self.__iot2_System2

    @iot2_System2.setter
    def iot2_System2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_System__iot2_System2", None)
        self.__iot2_System2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_Board"):
                    opp_val = getattr(item, "iot2_Board", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_Board", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_Board"):
                    opp_val = getattr(item, "iot2_Board", None)
                    
                    setattr(item, "iot2_Board", self)
                    

    @property
    def iot2_System(self):
        return self.__iot2_System

    @iot2_System.setter
    def iot2_System(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_System__iot2_System", None)
        self.__iot2_System = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_HWComponent"):
                    opp_val = getattr(item, "iot2_HWComponent", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_HWComponent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_HWComponent"):
                    opp_val = getattr(item, "iot2_HWComponent", None)
                    
                    setattr(item, "iot2_HWComponent", self)
                    

class iot2_HWComponent(ABC):

    def __init__(self, name: bool, iot2_HWComponent: "iot2_System" = None, iot2_HWComponent7: "iot2_Board" = None, iot2_HWComponent11: set["iot2_OperationDef"] = None):
        self.name = name
        self.iot2_HWComponent = iot2_HWComponent
        self.iot2_HWComponent7 = iot2_HWComponent7
        self.iot2_HWComponent11 = iot2_HWComponent11 if iot2_HWComponent11 is not None else set()
        
    @property
    def name(self) -> bool:
        return self.__name

    @name.setter
    def name(self, name: bool):
        self.__name = name

    @property
    def iot2_HWComponent(self):
        return self.__iot2_HWComponent

    @iot2_HWComponent.setter
    def iot2_HWComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_HWComponent__iot2_HWComponent", None)
        self.__iot2_HWComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_System"):
                opp_val = getattr(old_value, "iot2_System", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_System"):
                opp_val = getattr(value, "iot2_System", None)
                if opp_val is None:
                    setattr(value, "iot2_System", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_HWComponent11(self):
        return self.__iot2_HWComponent11

    @iot2_HWComponent11.setter
    def iot2_HWComponent11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_HWComponent__iot2_HWComponent11", None)
        self.__iot2_HWComponent11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_OperationDef"):
                    opp_val = getattr(item, "iot2_OperationDef", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_OperationDef", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_OperationDef"):
                    opp_val = getattr(item, "iot2_OperationDef", None)
                    
                    setattr(item, "iot2_OperationDef", self)
                    

    @property
    def iot2_HWComponent7(self):
        return self.__iot2_HWComponent7

    @iot2_HWComponent7.setter
    def iot2_HWComponent7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_HWComponent__iot2_HWComponent7", None)
        self.__iot2_HWComponent7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Board6"):
                opp_val = getattr(old_value, "iot2_Board6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Board6"):
                opp_val = getattr(value, "iot2_Board6", None)
                if opp_val is None:
                    setattr(value, "iot2_Board6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
