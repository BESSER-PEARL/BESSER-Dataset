from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class operators(Enum):
    equal = "equal"
    dis = "dis"
    l = "l"
    g = "g"
    le = "le"
    ge = "ge"
    or = "or"
    xor = "xor"
    xnor = "xnor"
    and = "and"
    u = "u"
    v = "v"
    s = "s"
    t = "t"


############################################
# Definition of Classes
############################################

class RTCTLExpression:

    pass
class nuSMV_UnaryRTCTLExpression(RTCTLExpression):

    def __init__(self, unary: str, nuSMV_UnaryRTCTLExpression: "nuSMV_RangeExpression" = None, nuSMV_UnaryRTCTLExpression105: "nuSMV_RTCTLExpression" = None):
        self.unary = unary
        self.nuSMV_UnaryRTCTLExpression = nuSMV_UnaryRTCTLExpression
        self.nuSMV_UnaryRTCTLExpression105 = nuSMV_UnaryRTCTLExpression105
        
    @property
    def unary(self) -> str:
        return self.__unary

    @unary.setter
    def unary(self, unary: str):
        self.__unary = unary

    @property
    def nuSMV_UnaryRTCTLExpression(self):
        return self.__nuSMV_UnaryRTCTLExpression

    @nuSMV_UnaryRTCTLExpression.setter
    def nuSMV_UnaryRTCTLExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nuSMV_UnaryRTCTLExpression__nuSMV_UnaryRTCTLExpression", None)
        self.__nuSMV_UnaryRTCTLExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nuSMV_RangeExpression"):
                opp_val = getattr(old_value, "nuSMV_RangeExpression", None)
                if opp_val == self:
                    setattr(old_value, "nuSMV_RangeExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nuSMV_RangeExpression"):
                opp_val = getattr(value, "nuSMV_RangeExpression", None)
                setattr(value, "nuSMV_RangeExpression", self)

    @property
    def nuSMV_UnaryRTCTLExpression105(self):
        return self.__nuSMV_UnaryRTCTLExpression105

    @nuSMV_UnaryRTCTLExpression105.setter
    def nuSMV_UnaryRTCTLExpression105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nuSMV_UnaryRTCTLExpression__nuSMV_UnaryRTCTLExpression105", None)
        self.__nuSMV_UnaryRTCTLExpression105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nuSMV_RTCTLExpression106"):
                opp_val = getattr(old_value, "nuSMV_RTCTLExpression106", None)
                if opp_val == self:
                    setattr(old_value, "nuSMV_RTCTLExpression106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nuSMV_RTCTLExpression106"):
                opp_val = getattr(value, "nuSMV_RTCTLExpression106", None)
                setattr(value, "nuSMV_RTCTLExpression106", self)

class nuSMV_SingleRTCTLExpression(RTCTLExpression):

    pass
class ModuleType:

    pass
class nuSMV_SyncrProcessType(ModuleType):

    pass
class nuSMV_AsyncrProcessType(ModuleType):

    pass
class SimpleType:

    pass
class nuSMV_IntervalType(SimpleType):

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

class nuSMV_ArrayType(SimpleType):

    def __init__(self, lowerBound: str, upperBound: str, nuSMV_ArrayType: "nuSMV_SimpleType" = None):
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.nuSMV_ArrayType = nuSMV_ArrayType
        
    @property
    def upperBound(self) -> str:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: str):
        self.__upperBound = upperBound

    @property
    def lowerBound(self) -> str:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: str):
        self.__lowerBound = lowerBound

    @property
    def nuSMV_ArrayType(self):
        return self.__nuSMV_ArrayType

    @nuSMV_ArrayType.setter
    def nuSMV_ArrayType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nuSMV_ArrayType__nuSMV_ArrayType", None)
        self.__nuSMV_ArrayType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nuSMV_SimpleType"):
                opp_val = getattr(old_value, "nuSMV_SimpleType", None)
                if opp_val == self:
                    setattr(old_value, "nuSMV_SimpleType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nuSMV_SimpleType"):
                opp_val = getattr(value, "nuSMV_SimpleType", None)
                setattr(value, "nuSMV_SimpleType", self)

class nuSMV_UnsignedWordType(SimpleType):

    def __init__(self, uWordNumber: str):
        self.uWordNumber = uWordNumber
        
    @property
    def uWordNumber(self) -> str:
        return self.__uWordNumber

    @uWordNumber.setter
    def uWordNumber(self, uWordNumber: str):
        self.__uWordNumber = uWordNumber

class nuSMV_EnumType(SimpleType):

    pass
class nuSMV_SignedWordType(SimpleType):

    def __init__(self, signedNumber: str):
        self.signedNumber = signedNumber
        
    @property
    def signedNumber(self) -> str:
        return self.__signedNumber

    @signedNumber.setter
    def signedNumber(self, signedNumber: str):
        self.__signedNumber = signedNumber

class nuSMV_WordType(SimpleType):

    def __init__(self, wordNumber: str):
        self.wordNumber = wordNumber
        
    @property
    def wordNumber(self) -> str:
        return self.__wordNumber

    @wordNumber.setter
    def wordNumber(self, wordNumber: str):
        self.__wordNumber = wordNumber

class nuSMV_BooleanType(SimpleType):

    pass
class nuSMV_RTCTLExpression:

    pass
class nuSMV_RangeExpression:

    def __init__(self, lower: str, upper: str, nuSMV_RangeExpression: "nuSMV_UnaryRTCTLExpression" = None):
        self.lower = lower
        self.upper = upper
        self.nuSMV_RangeExpression = nuSMV_RangeExpression
        
    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

    @property
    def lower(self) -> str:
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower

    @property
    def nuSMV_RangeExpression(self):
        return self.__nuSMV_RangeExpression

    @nuSMV_RangeExpression.setter
    def nuSMV_RangeExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nuSMV_RangeExpression__nuSMV_RangeExpression", None)
        self.__nuSMV_RangeExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nuSMV_UnaryRTCTLExpression"):
                opp_val = getattr(old_value, "nuSMV_UnaryRTCTLExpression", None)
                if opp_val == self:
                    setattr(old_value, "nuSMV_UnaryRTCTLExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nuSMV_UnaryRTCTLExpression"):
                opp_val = getattr(value, "nuSMV_UnaryRTCTLExpression", None)
                setattr(value, "nuSMV_UnaryRTCTLExpression", self)

class nuSMV_CaseSimpleAssignementExpression:

    pass
class SimpleExpression:

    pass
class nuSMV_SetValueParameter(SimpleExpression):

    pass
class nuSMV_BinaryExpression(SimpleExpression):

    def __init__(self, operator: str, op: str, nuSMV_BinaryExpression: "nuSMV_SimpleExpression" = None, nuSMV_BinaryExpression78: "nuSMV_SimpleExpression" = None):
        self.operator = operator
        self.op = op
        self.nuSMV_BinaryExpression = nuSMV_BinaryExpression
        self.nuSMV_BinaryExpression78 = nuSMV_BinaryExpression78
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def nuSMV_BinaryExpression78(self):
        return self.__nuSMV_BinaryExpression78

    @nuSMV_BinaryExpression78.setter
    def nuSMV_BinaryExpression78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nuSMV_BinaryExpression__nuSMV_BinaryExpression78", None)
        self.__nuSMV_BinaryExpression78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nuSMV_SimpleExpression79"):
                opp_val = getattr(old_value, "nuSMV_SimpleExpression79", None)
                if opp_val == self:
                    setattr(old_value, "nuSMV_SimpleExpression79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nuSMV_SimpleExpression79"):
                opp_val = getattr(value, "nuSMV_SimpleExpression79", None)
                setattr(value, "nuSMV_SimpleExpression79", self)

    @property
    def nuSMV_BinaryExpression(self):
        return self.__nuSMV_BinaryExpression

    @nuSMV_BinaryExpression.setter
    def nuSMV_BinaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nuSMV_BinaryExpression__nuSMV_BinaryExpression", None)
        self.__nuSMV_BinaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nuSMV_SimpleExpression76"):
                opp_val = getattr(old_value, "nuSMV_SimpleExpression76", None)
                if opp_val == self:
                    setattr(old_value, "nuSMV_SimpleExpression76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nuSMV_SimpleExpression76"):
                opp_val = getattr(value, "nuSMV_SimpleExpression76", None)
                setattr(value, "nuSMV_SimpleExpression76", self)

class nuSMV_IntervalExpression(SimpleExpression):

    def __init__(self, lowerBound: str, upperBound: str):
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        
    @property
    def upperBound(self) -> str:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: str):
        self.__upperBound = upperBound

    @property
    def lowerBound(self) -> str:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: str):
        self.__lowerBound = lowerBound

class nuSMV_ParsExpression(SimpleExpression):

    def __init__(self, isNext: bool, nuSMV_ParsExpression: "nuSMV_SimpleExpression" = None):
        self.isNext = isNext
        self.nuSMV_ParsExpression = nuSMV_ParsExpression
        
    @property
    def isNext(self) -> bool:
        return self.__isNext

    @isNext.setter
    def isNext(self, isNext: bool):
        self.__isNext = isNext

    @property
    def nuSMV_ParsExpression(self):
        return self.__nuSMV_ParsExpression

    @nuSMV_ParsExpression.setter
    def nuSMV_ParsExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nuSMV_ParsExpression__nuSMV_ParsExpression", None)
        self.__nuSMV_ParsExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nuSMV_SimpleExpression83"):
                opp_val = getattr(old_value, "nuSMV_SimpleExpression83", None)
                if opp_val == self:
                    setattr(old_value, "nuSMV_SimpleExpression83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nuSMV_SimpleExpression83"):
                opp_val = getattr(value, "nuSMV_SimpleExpression83", None)
                setattr(value, "nuSMV_SimpleExpression83", self)

class nuSMV_WordExpression(SimpleExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class nuSMV_Var(SimpleExpression):

    pass
class nuSMV_UntilCTLexpression(SimpleExpression):

    def __init__(self, ea: str, nuSMV_UntilCTLexpression: "nuSMV_SimpleExpression" = None):
        self.ea = ea
        self.nuSMV_UntilCTLexpression = nuSMV_UntilCTLexpression
        
    @property
    def ea(self) -> str:
        return self.__ea

    @ea.setter
    def ea(self, ea: str):
        self.__ea = ea

    @property
    def nuSMV_UntilCTLexpression(self):
        return self.__nuSMV_UntilCTLexpression

    @nuSMV_UntilCTLexpression.setter
    def nuSMV_UntilCTLexpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nuSMV_UntilCTLexpression__nuSMV_UntilCTLexpression", None)
        self.__nuSMV_UntilCTLexpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nuSMV_SimpleExpression98"):
                opp_val = getattr(old_value, "nuSMV_SimpleExpression98", None)
                if opp_val == self:
                    setattr(old_value, "nuSMV_SimpleExpression98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nuSMV_SimpleExpression98"):
                opp_val = getattr(value, "nuSMV_SimpleExpression98", None)
                setattr(value, "nuSMV_SimpleExpression98", self)

class nuSMV_ValueExpression(SimpleExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class nuSMV_UnaryExpression(SimpleExpression):

    def __init__(self, operator: str, nuSMV_UnaryExpression: "nuSMV_SimpleExpression" = None):
        self.operator = operator
        self.nuSMV_UnaryExpression = nuSMV_UnaryExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def nuSMV_UnaryExpression(self):
        return self.__nuSMV_UnaryExpression

    @nuSMV_UnaryExpression.setter
    def nuSMV_UnaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nuSMV_UnaryExpression__nuSMV_UnaryExpression", None)
        self.__nuSMV_UnaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nuSMV_SimpleExpression85"):
                opp_val = getattr(old_value, "nuSMV_SimpleExpression85", None)
                if opp_val == self:
                    setattr(old_value, "nuSMV_SimpleExpression85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nuSMV_SimpleExpression85"):
                opp_val = getattr(value, "nuSMV_SimpleExpression85", None)
                setattr(value, "nuSMV_SimpleExpression85", self)

class nuSMV_UnaryFunctionExpression(SimpleExpression):

    def __init__(self, function: str, nuSMV_UnaryFunctionExpression: "nuSMV_SimpleExpression" = None):
        self.function = function
        self.nuSMV_UnaryFunctionExpression = nuSMV_UnaryFunctionExpression
        
    @property
    def function(self) -> str:
        return self.__function

    @function.setter
    def function(self, function: str):
        self.__function = function

    @property
    def nuSMV_UnaryFunctionExpression(self):
        return self.__nuSMV_UnaryFunctionExpression

    @nuSMV_UnaryFunctionExpression.setter
    def nuSMV_UnaryFunctionExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nuSMV_UnaryFunctionExpression__nuSMV_UnaryFunctionExpression", None)
        self.__nuSMV_UnaryFunctionExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nuSMV_SimpleExpression100"):
                opp_val = getattr(old_value, "nuSMV_SimpleExpression100", None)
                if opp_val == self:
                    setattr(old_value, "nuSMV_SimpleExpression100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nuSMV_SimpleExpression100"):
                opp_val = getattr(value, "nuSMV_SimpleExpression100", None)
                setattr(value, "nuSMV_SimpleExpression100", self)

class nuSMV_SetExpression(SimpleExpression):

    pass
class nuSMV_Not(SimpleExpression):

    pass
class nuSMV_SetElementExpression(SimpleExpression):

    pass
class nuSMV_CaseSimpleExpression(SimpleExpression):

    pass
class nuSMV_Val:

    def __init__(self, name: str, num: str, nuSMV_Val: "nuSMV_EnumType" = None, nuSMV_Val92: "nuSMV_SetElementExpression" = None):
        self.name = name
        self.num = num
        self.nuSMV_Val = nuSMV_Val
        self.nuSMV_Val92 = nuSMV_Val92
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def num(self) -> str:
        return self.__num

    @num.setter
    def num(self, num: str):
        self.__num = num

    @property
    def nuSMV_Val92(self):
        return self.__nuSMV_Val92

    @nuSMV_Val92.setter
    def nuSMV_Val92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nuSMV_Val__nuSMV_Val92", None)
        self.__nuSMV_Val92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nuSMV_SetElementExpression"):
                opp_val = getattr(old_value, "nuSMV_SetElementExpression", None)
                if opp_val == self:
                    setattr(old_value, "nuSMV_SetElementExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nuSMV_SetElementExpression"):
                opp_val = getattr(value, "nuSMV_SetElementExpression", None)
                setattr(value, "nuSMV_SetElementExpression", self)

    @property
    def nuSMV_Val(self):
        return self.__nuSMV_Val

    @nuSMV_Val.setter
    def nuSMV_Val(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nuSMV_Val__nuSMV_Val", None)
        self.__nuSMV_Val = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nuSMV_EnumType"):
                opp_val = getattr(old_value, "nuSMV_EnumType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nuSMV_EnumType"):
                opp_val = getattr(value, "nuSMV_EnumType", None)
                if opp_val is None:
                    setattr(value, "nuSMV_EnumType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Type:

    pass
class nuSMV_ModuleType(Type):

    pass
class nuSMV_SimpleType(Type):

    pass
class nuSMV_LTLExpression:

    pass
class nuSMV_CTLExpression:

    pass
class FairnessConstraint:

    pass
class nuSMV_CompassionExpression(FairnessConstraint):

    pass
class nuSMV_JusticeExpression(FairnessConstraint):

    pass
class nuSMV_FairnessExpression(FairnessConstraint):

    pass
class nuSMV_NextExpression:

    pass
class AssignBody:

    pass
class nuSMV_NextBody(AssignBody):

    pass
class nuSMV_InitBody(AssignBody):

    pass
class nuSMV_VarBodyAssign(AssignBody):

    pass
class nuSMV_EObject:

    pass
class nuSMV_AssignBody:

    def __init__(self, array: str, semicolon: bool, nuSMV_AssignBody: "nuSMV_AssignConstraintElement" = None, nuSMV_AssignBody17: "nuSMV_EObject" = None, nuSMV_AssignBody19: "nuSMV_SimpleExpression" = None):
        self.array = array
        self.semicolon = semicolon
        self.nuSMV_AssignBody = nuSMV_AssignBody
        self.nuSMV_AssignBody17 = nuSMV_AssignBody17
        self.nuSMV_AssignBody19 = nuSMV_AssignBody19
        
    @property
    def semicolon(self) -> bool:
        return self.__semicolon

    @semicolon.setter
    def semicolon(self, semicolon: bool):
        self.__semicolon = semicolon

    @property
    def array(self) -> str:
        return self.__array

    @array.setter
    def array(self, array: str):
        self.__array = array

    @property
    def nuSMV_AssignBody17(self):
        return self.__nuSMV_AssignBody17

    @nuSMV_AssignBody17.setter
    def nuSMV_AssignBody17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nuSMV_AssignBody__nuSMV_AssignBody17", None)
        self.__nuSMV_AssignBody17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nuSMV_EObject"):
                opp_val = getattr(old_value, "nuSMV_EObject", None)
                if opp_val == self:
                    setattr(old_value, "nuSMV_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nuSMV_EObject"):
                opp_val = getattr(value, "nuSMV_EObject", None)
                setattr(value, "nuSMV_EObject", self)

    @property
    def nuSMV_AssignBody19(self):
        return self.__nuSMV_AssignBody19

    @nuSMV_AssignBody19.setter
    def nuSMV_AssignBody19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nuSMV_AssignBody__nuSMV_AssignBody19", None)
        self.__nuSMV_AssignBody19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nuSMV_SimpleExpression20"):
                opp_val = getattr(old_value, "nuSMV_SimpleExpression20", None)
                if opp_val == self:
                    setattr(old_value, "nuSMV_SimpleExpression20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nuSMV_SimpleExpression20"):
                opp_val = getattr(value, "nuSMV_SimpleExpression20", None)
                setattr(value, "nuSMV_SimpleExpression20", self)

    @property
    def nuSMV_AssignBody(self):
        return self.__nuSMV_AssignBody

    @nuSMV_AssignBody.setter
    def nuSMV_AssignBody(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nuSMV_AssignBody__nuSMV_AssignBody", None)
        self.__nuSMV_AssignBody = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nuSMV_AssignConstraintElement"):
                opp_val = getattr(old_value, "nuSMV_AssignConstraintElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nuSMV_AssignConstraintElement"):
                opp_val = getattr(value, "nuSMV_AssignConstraintElement", None)
                if opp_val is None:
                    setattr(value, "nuSMV_AssignConstraintElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class nuSMV_SimpleExpression:

    pass
class nuSMV_DefineBody:

    def __init__(self, var: str, semicolon: bool, nuSMV_DefineBody: "nuSMV_DefineDeclaration" = None, nuSMV_DefineBody14: "nuSMV_SimpleExpression" = None):
        self.var = var
        self.semicolon = semicolon
        self.nuSMV_DefineBody = nuSMV_DefineBody
        self.nuSMV_DefineBody14 = nuSMV_DefineBody14
        
    @property
    def var(self) -> str:
        return self.__var

    @var.setter
    def var(self, var: str):
        self.__var = var

    @property
    def semicolon(self) -> bool:
        return self.__semicolon

    @semicolon.setter
    def semicolon(self, semicolon: bool):
        self.__semicolon = semicolon

    @property
    def nuSMV_DefineBody14(self):
        return self.__nuSMV_DefineBody14

    @nuSMV_DefineBody14.setter
    def nuSMV_DefineBody14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nuSMV_DefineBody__nuSMV_DefineBody14", None)
        self.__nuSMV_DefineBody14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nuSMV_SimpleExpression"):
                opp_val = getattr(old_value, "nuSMV_SimpleExpression", None)
                if opp_val == self:
                    setattr(old_value, "nuSMV_SimpleExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nuSMV_SimpleExpression"):
                opp_val = getattr(value, "nuSMV_SimpleExpression", None)
                setattr(value, "nuSMV_SimpleExpression", self)

    @property
    def nuSMV_DefineBody(self):
        return self.__nuSMV_DefineBody

    @nuSMV_DefineBody.setter
    def nuSMV_DefineBody(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nuSMV_DefineBody__nuSMV_DefineBody", None)
        self.__nuSMV_DefineBody = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nuSMV_DefineDeclaration"):
                opp_val = getattr(old_value, "nuSMV_DefineDeclaration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nuSMV_DefineDeclaration"):
                opp_val = getattr(value, "nuSMV_DefineDeclaration", None)
                if opp_val is None:
                    setattr(value, "nuSMV_DefineDeclaration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class nuSMV_Type:

    pass
class nuSMV_VarBody:

    def __init__(self, name: str, semicolon: bool, nuSMV_VarBody: "nuSMV_VariableDeclaration" = None, nuSMV_VarBody9: "nuSMV_FrozenVariableDeclaration" = None, nuSMV_VarBody11: "nuSMV_Type" = None, nuSMV_VarBody7: "nuSMV_IVariableDeclaration" = None, nuSMV_VarBody52: "nuSMV_ModuleType" = None, nuSMV_VarBody87: "nuSMV_Var" = None):
        self.name = name
        self.semicolon = semicolon
        self.nuSMV_VarBody = nuSMV_VarBody
        self.nuSMV_VarBody9 = nuSMV_VarBody9
        self.nuSMV_VarBody11 = nuSMV_VarBody11
        self.nuSMV_VarBody7 = nuSMV_VarBody7
        self.nuSMV_VarBody52 = nuSMV_VarBody52
        self.nuSMV_VarBody87 = nuSMV_VarBody87
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def semicolon(self) -> bool:
        return self.__semicolon

    @semicolon.setter
    def semicolon(self, semicolon: bool):
        self.__semicolon = semicolon

    @property
    def nuSMV_VarBody9(self):
        return self.__nuSMV_VarBody9

    @nuSMV_VarBody9.setter
    def nuSMV_VarBody9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nuSMV_VarBody__nuSMV_VarBody9", None)
        self.__nuSMV_VarBody9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nuSMV_FrozenVariableDeclaration"):
                opp_val = getattr(old_value, "nuSMV_FrozenVariableDeclaration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nuSMV_FrozenVariableDeclaration"):
                opp_val = getattr(value, "nuSMV_FrozenVariableDeclaration", None)
                if opp_val is None:
                    setattr(value, "nuSMV_FrozenVariableDeclaration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def nuSMV_VarBody7(self):
        return self.__nuSMV_VarBody7

    @nuSMV_VarBody7.setter
    def nuSMV_VarBody7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nuSMV_VarBody__nuSMV_VarBody7", None)
        self.__nuSMV_VarBody7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nuSMV_IVariableDeclaration"):
                opp_val = getattr(old_value, "nuSMV_IVariableDeclaration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nuSMV_IVariableDeclaration"):
                opp_val = getattr(value, "nuSMV_IVariableDeclaration", None)
                if opp_val is None:
                    setattr(value, "nuSMV_IVariableDeclaration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def nuSMV_VarBody(self):
        return self.__nuSMV_VarBody

    @nuSMV_VarBody.setter
    def nuSMV_VarBody(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nuSMV_VarBody__nuSMV_VarBody", None)
        self.__nuSMV_VarBody = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nuSMV_VariableDeclaration"):
                opp_val = getattr(old_value, "nuSMV_VariableDeclaration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nuSMV_VariableDeclaration"):
                opp_val = getattr(value, "nuSMV_VariableDeclaration", None)
                if opp_val is None:
                    setattr(value, "nuSMV_VariableDeclaration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def nuSMV_VarBody52(self):
        return self.__nuSMV_VarBody52

    @nuSMV_VarBody52.setter
    def nuSMV_VarBody52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nuSMV_VarBody__nuSMV_VarBody52", None)
        self.__nuSMV_VarBody52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nuSMV_ModuleType51"):
                opp_val = getattr(old_value, "nuSMV_ModuleType51", None)
                if opp_val == self:
                    setattr(old_value, "nuSMV_ModuleType51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nuSMV_ModuleType51"):
                opp_val = getattr(value, "nuSMV_ModuleType51", None)
                setattr(value, "nuSMV_ModuleType51", self)

    @property
    def nuSMV_VarBody87(self):
        return self.__nuSMV_VarBody87

    @nuSMV_VarBody87.setter
    def nuSMV_VarBody87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nuSMV_VarBody__nuSMV_VarBody87", None)
        self.__nuSMV_VarBody87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nuSMV_Var"):
                opp_val = getattr(old_value, "nuSMV_Var", None)
                if opp_val == self:
                    setattr(old_value, "nuSMV_Var", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nuSMV_Var"):
                opp_val = getattr(value, "nuSMV_Var", None)
                setattr(value, "nuSMV_Var", self)

    @property
    def nuSMV_VarBody11(self):
        return self.__nuSMV_VarBody11

    @nuSMV_VarBody11.setter
    def nuSMV_VarBody11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nuSMV_VarBody__nuSMV_VarBody11", None)
        self.__nuSMV_VarBody11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nuSMV_Type"):
                opp_val = getattr(old_value, "nuSMV_Type", None)
                if opp_val == self:
                    setattr(old_value, "nuSMV_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nuSMV_Type"):
                opp_val = getattr(value, "nuSMV_Type", None)
                setattr(value, "nuSMV_Type", self)

class ModuleElement:

    pass
class nuSMV_InitConstraint(ModuleElement):

    def __init__(self, semicolon: bool, nuSMV_InitConstraint: "nuSMV_SimpleExpression" = None):
        self.semicolon = semicolon
        self.nuSMV_InitConstraint = nuSMV_InitConstraint
        
    @property
    def semicolon(self) -> bool:
        return self.__semicolon

    @semicolon.setter
    def semicolon(self, semicolon: bool):
        self.__semicolon = semicolon

    @property
    def nuSMV_InitConstraint(self):
        return self.__nuSMV_InitConstraint

    @nuSMV_InitConstraint.setter
    def nuSMV_InitConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nuSMV_InitConstraint__nuSMV_InitConstraint", None)
        self.__nuSMV_InitConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nuSMV_SimpleExpression29"):
                opp_val = getattr(old_value, "nuSMV_SimpleExpression29", None)
                if opp_val == self:
                    setattr(old_value, "nuSMV_SimpleExpression29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nuSMV_SimpleExpression29"):
                opp_val = getattr(value, "nuSMV_SimpleExpression29", None)
                setattr(value, "nuSMV_SimpleExpression29", self)

class nuSMV_AssignConstraintElement(ModuleElement):

    def __init__(self, assign: str, nuSMV_AssignConstraintElement: set["nuSMV_AssignBody"] = None):
        self.assign = assign
        self.nuSMV_AssignConstraintElement = nuSMV_AssignConstraintElement if nuSMV_AssignConstraintElement is not None else set()
        
    @property
    def assign(self) -> str:
        return self.__assign

    @assign.setter
    def assign(self, assign: str):
        self.__assign = assign

    @property
    def nuSMV_AssignConstraintElement(self):
        return self.__nuSMV_AssignConstraintElement

    @nuSMV_AssignConstraintElement.setter
    def nuSMV_AssignConstraintElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nuSMV_AssignConstraintElement__nuSMV_AssignConstraintElement", None)
        self.__nuSMV_AssignConstraintElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nuSMV_AssignBody"):
                    opp_val = getattr(item, "nuSMV_AssignBody", None)
                    
                    if opp_val == self:
                        setattr(item, "nuSMV_AssignBody", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nuSMV_AssignBody"):
                    opp_val = getattr(item, "nuSMV_AssignBody", None)
                    
                    setattr(item, "nuSMV_AssignBody", self)
                    

class nuSMV_ComputeSpecification(ModuleElement):

    def __init__(self, minMax: str, nuSMV_ComputeSpecification: "nuSMV_RTCTLExpression" = None, nuSMV_ComputeSpecification71: "nuSMV_RTCTLExpression" = None):
        self.minMax = minMax
        self.nuSMV_ComputeSpecification = nuSMV_ComputeSpecification
        self.nuSMV_ComputeSpecification71 = nuSMV_ComputeSpecification71
        
    @property
    def minMax(self) -> str:
        return self.__minMax

    @minMax.setter
    def minMax(self, minMax: str):
        self.__minMax = minMax

    @property
    def nuSMV_ComputeSpecification(self):
        return self.__nuSMV_ComputeSpecification

    @nuSMV_ComputeSpecification.setter
    def nuSMV_ComputeSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nuSMV_ComputeSpecification__nuSMV_ComputeSpecification", None)
        self.__nuSMV_ComputeSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nuSMV_RTCTLExpression"):
                opp_val = getattr(old_value, "nuSMV_RTCTLExpression", None)
                if opp_val == self:
                    setattr(old_value, "nuSMV_RTCTLExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nuSMV_RTCTLExpression"):
                opp_val = getattr(value, "nuSMV_RTCTLExpression", None)
                setattr(value, "nuSMV_RTCTLExpression", self)

    @property
    def nuSMV_ComputeSpecification71(self):
        return self.__nuSMV_ComputeSpecification71

    @nuSMV_ComputeSpecification71.setter
    def nuSMV_ComputeSpecification71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nuSMV_ComputeSpecification__nuSMV_ComputeSpecification71", None)
        self.__nuSMV_ComputeSpecification71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nuSMV_RTCTLExpression72"):
                opp_val = getattr(old_value, "nuSMV_RTCTLExpression72", None)
                if opp_val == self:
                    setattr(old_value, "nuSMV_RTCTLExpression72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nuSMV_RTCTLExpression72"):
                opp_val = getattr(value, "nuSMV_RTCTLExpression72", None)
                setattr(value, "nuSMV_RTCTLExpression72", self)

class nuSMV_IsaDeclaration(ModuleElement):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class nuSMV_InvarSpecification(ModuleElement):

    def __init__(self, name: str, semicolon: bool, nuSMV_InvarSpecification: "nuSMV_NextExpression" = None):
        self.name = name
        self.semicolon = semicolon
        self.nuSMV_InvarSpecification = nuSMV_InvarSpecification
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def semicolon(self) -> bool:
        return self.__semicolon

    @semicolon.setter
    def semicolon(self, semicolon: bool):
        self.__semicolon = semicolon

    @property
    def nuSMV_InvarSpecification(self):
        return self.__nuSMV_InvarSpecification

    @nuSMV_InvarSpecification.setter
    def nuSMV_InvarSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nuSMV_InvarSpecification__nuSMV_InvarSpecification", None)
        self.__nuSMV_InvarSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nuSMV_NextExpression43"):
                opp_val = getattr(old_value, "nuSMV_NextExpression43", None)
                if opp_val == self:
                    setattr(old_value, "nuSMV_NextExpression43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nuSMV_NextExpression43"):
                opp_val = getattr(value, "nuSMV_NextExpression43", None)
                setattr(value, "nuSMV_NextExpression43", self)

class nuSMV_InvarConstraint(ModuleElement):

    def __init__(self, semicolon: bool, nuSMV_InvarConstraint: "nuSMV_SimpleExpression" = None):
        self.semicolon = semicolon
        self.nuSMV_InvarConstraint = nuSMV_InvarConstraint
        
    @property
    def semicolon(self) -> bool:
        return self.__semicolon

    @semicolon.setter
    def semicolon(self, semicolon: bool):
        self.__semicolon = semicolon

    @property
    def nuSMV_InvarConstraint(self):
        return self.__nuSMV_InvarConstraint

    @nuSMV_InvarConstraint.setter
    def nuSMV_InvarConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nuSMV_InvarConstraint__nuSMV_InvarConstraint", None)
        self.__nuSMV_InvarConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nuSMV_SimpleExpression31"):
                opp_val = getattr(old_value, "nuSMV_SimpleExpression31", None)
                if opp_val == self:
                    setattr(old_value, "nuSMV_SimpleExpression31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nuSMV_SimpleExpression31"):
                opp_val = getattr(value, "nuSMV_SimpleExpression31", None)
                setattr(value, "nuSMV_SimpleExpression31", self)

class nuSMV_CtlSpecification(ModuleElement):

    def __init__(self, specKeyWord: str, nameKeyWord: bool, name: str, semicolon: bool, nuSMV_CtlSpecification: "nuSMV_CTLExpression" = None):
        self.specKeyWord = specKeyWord
        self.nameKeyWord = nameKeyWord
        self.name = name
        self.semicolon = semicolon
        self.nuSMV_CtlSpecification = nuSMV_CtlSpecification
        
    @property
    def nameKeyWord(self) -> bool:
        return self.__nameKeyWord

    @nameKeyWord.setter
    def nameKeyWord(self, nameKeyWord: bool):
        self.__nameKeyWord = nameKeyWord

    @property
    def semicolon(self) -> bool:
        return self.__semicolon

    @semicolon.setter
    def semicolon(self, semicolon: bool):
        self.__semicolon = semicolon

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def specKeyWord(self) -> str:
        return self.__specKeyWord

    @specKeyWord.setter
    def specKeyWord(self, specKeyWord: str):
        self.__specKeyWord = specKeyWord

    @property
    def nuSMV_CtlSpecification(self):
        return self.__nuSMV_CtlSpecification

    @nuSMV_CtlSpecification.setter
    def nuSMV_CtlSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nuSMV_CtlSpecification__nuSMV_CtlSpecification", None)
        self.__nuSMV_CtlSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nuSMV_CTLExpression"):
                opp_val = getattr(old_value, "nuSMV_CTLExpression", None)
                if opp_val == self:
                    setattr(old_value, "nuSMV_CTLExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nuSMV_CTLExpression"):
                opp_val = getattr(value, "nuSMV_CTLExpression", None)
                setattr(value, "nuSMV_CTLExpression", self)

class nuSMV_FairnessConstraint(ModuleElement):

    def __init__(self, semicolon: bool):
        self.semicolon = semicolon
        
    @property
    def semicolon(self) -> bool:
        return self.__semicolon

    @semicolon.setter
    def semicolon(self, semicolon: bool):
        self.__semicolon = semicolon

class nuSMV_FrozenVariableDeclaration(ModuleElement):

    pass
class nuSMV_LtlSpecification(ModuleElement):

    def __init__(self, nameId: bool, name: str, semicolon: bool, nuSMV_LtlSpecification: "nuSMV_LTLExpression" = None):
        self.nameId = nameId
        self.name = name
        self.semicolon = semicolon
        self.nuSMV_LtlSpecification = nuSMV_LtlSpecification
        
    @property
    def semicolon(self) -> bool:
        return self.__semicolon

    @semicolon.setter
    def semicolon(self, semicolon: bool):
        self.__semicolon = semicolon

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def nameId(self) -> bool:
        return self.__nameId

    @nameId.setter
    def nameId(self, nameId: bool):
        self.__nameId = nameId

    @property
    def nuSMV_LtlSpecification(self):
        return self.__nuSMV_LtlSpecification

    @nuSMV_LtlSpecification.setter
    def nuSMV_LtlSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nuSMV_LtlSpecification__nuSMV_LtlSpecification", None)
        self.__nuSMV_LtlSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nuSMV_LTLExpression"):
                opp_val = getattr(old_value, "nuSMV_LTLExpression", None)
                if opp_val == self:
                    setattr(old_value, "nuSMV_LTLExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nuSMV_LTLExpression"):
                opp_val = getattr(value, "nuSMV_LTLExpression", None)
                setattr(value, "nuSMV_LTLExpression", self)

class nuSMV_IVariableDeclaration(ModuleElement):

    pass
class nuSMV_ConstantsDeclaration(ModuleElement):

    def __init__(self, constants: str, semicolon: bool):
        self.constants = constants
        self.semicolon = semicolon
        
    @property
    def constants(self) -> str:
        return self.__constants

    @constants.setter
    def constants(self, constants: str):
        self.__constants = constants

    @property
    def semicolon(self) -> bool:
        return self.__semicolon

    @semicolon.setter
    def semicolon(self, semicolon: bool):
        self.__semicolon = semicolon

class nuSMV_TransConstraint(ModuleElement):

    def __init__(self, semicolon: bool, nuSMV_TransConstraint: "nuSMV_SimpleExpression" = None):
        self.semicolon = semicolon
        self.nuSMV_TransConstraint = nuSMV_TransConstraint
        
    @property
    def semicolon(self) -> bool:
        return self.__semicolon

    @semicolon.setter
    def semicolon(self, semicolon: bool):
        self.__semicolon = semicolon

    @property
    def nuSMV_TransConstraint(self):
        return self.__nuSMV_TransConstraint

    @nuSMV_TransConstraint.setter
    def nuSMV_TransConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nuSMV_TransConstraint__nuSMV_TransConstraint", None)
        self.__nuSMV_TransConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nuSMV_SimpleExpression27"):
                opp_val = getattr(old_value, "nuSMV_SimpleExpression27", None)
                if opp_val == self:
                    setattr(old_value, "nuSMV_SimpleExpression27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nuSMV_SimpleExpression27"):
                opp_val = getattr(value, "nuSMV_SimpleExpression27", None)
                setattr(value, "nuSMV_SimpleExpression27", self)

class nuSMV_DefineDeclaration(ModuleElement):

    def __init__(self, define: str, nuSMV_DefineDeclaration: set["nuSMV_DefineBody"] = None):
        self.define = define
        self.nuSMV_DefineDeclaration = nuSMV_DefineDeclaration if nuSMV_DefineDeclaration is not None else set()
        
    @property
    def define(self) -> str:
        return self.__define

    @define.setter
    def define(self, define: str):
        self.__define = define

    @property
    def nuSMV_DefineDeclaration(self):
        return self.__nuSMV_DefineDeclaration

    @nuSMV_DefineDeclaration.setter
    def nuSMV_DefineDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nuSMV_DefineDeclaration__nuSMV_DefineDeclaration", None)
        self.__nuSMV_DefineDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nuSMV_DefineBody"):
                    opp_val = getattr(item, "nuSMV_DefineBody", None)
                    
                    if opp_val == self:
                        setattr(item, "nuSMV_DefineBody", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nuSMV_DefineBody"):
                    opp_val = getattr(item, "nuSMV_DefineBody", None)
                    
                    setattr(item, "nuSMV_DefineBody", self)
                    

class nuSMV_VariableDeclaration(ModuleElement):

    pass
class nuSMV_ModuleElement:

    pass
class nuSMV_FormalParameter:

    def __init__(self, name: str, nuSMV_FormalParameter: "nuSMV_Module" = None, nuSMV_FormalParameter94: "nuSMV_SetValueParameter" = None):
        self.name = name
        self.nuSMV_FormalParameter = nuSMV_FormalParameter
        self.nuSMV_FormalParameter94 = nuSMV_FormalParameter94
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def nuSMV_FormalParameter(self):
        return self.__nuSMV_FormalParameter

    @nuSMV_FormalParameter.setter
    def nuSMV_FormalParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nuSMV_FormalParameter__nuSMV_FormalParameter", None)
        self.__nuSMV_FormalParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nuSMV_Module2"):
                opp_val = getattr(old_value, "nuSMV_Module2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nuSMV_Module2"):
                opp_val = getattr(value, "nuSMV_Module2", None)
                if opp_val is None:
                    setattr(value, "nuSMV_Module2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def nuSMV_FormalParameter94(self):
        return self.__nuSMV_FormalParameter94

    @nuSMV_FormalParameter94.setter
    def nuSMV_FormalParameter94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nuSMV_FormalParameter__nuSMV_FormalParameter94", None)
        self.__nuSMV_FormalParameter94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nuSMV_SetValueParameter"):
                opp_val = getattr(old_value, "nuSMV_SetValueParameter", None)
                if opp_val == self:
                    setattr(old_value, "nuSMV_SetValueParameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nuSMV_SetValueParameter"):
                opp_val = getattr(value, "nuSMV_SetValueParameter", None)
                setattr(value, "nuSMV_SetValueParameter", self)

class nuSMV_Module:

    def __init__(self, name: str, nuSMV_Module: "nuSMV_NuSmvModel" = None, nuSMV_Module2: set["nuSMV_FormalParameter"] = None, nuSMV_Module4: set["nuSMV_ModuleElement"] = None, nuSMV_Module46: "nuSMV_ModuleType" = None):
        self.name = name
        self.nuSMV_Module = nuSMV_Module
        self.nuSMV_Module2 = nuSMV_Module2 if nuSMV_Module2 is not None else set()
        self.nuSMV_Module4 = nuSMV_Module4 if nuSMV_Module4 is not None else set()
        self.nuSMV_Module46 = nuSMV_Module46
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def nuSMV_Module2(self):
        return self.__nuSMV_Module2

    @nuSMV_Module2.setter
    def nuSMV_Module2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nuSMV_Module__nuSMV_Module2", None)
        self.__nuSMV_Module2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nuSMV_FormalParameter"):
                    opp_val = getattr(item, "nuSMV_FormalParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "nuSMV_FormalParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nuSMV_FormalParameter"):
                    opp_val = getattr(item, "nuSMV_FormalParameter", None)
                    
                    setattr(item, "nuSMV_FormalParameter", self)
                    

    @property
    def nuSMV_Module(self):
        return self.__nuSMV_Module

    @nuSMV_Module.setter
    def nuSMV_Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nuSMV_Module__nuSMV_Module", None)
        self.__nuSMV_Module = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nuSMV_NuSmvModel"):
                opp_val = getattr(old_value, "nuSMV_NuSmvModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nuSMV_NuSmvModel"):
                opp_val = getattr(value, "nuSMV_NuSmvModel", None)
                if opp_val is None:
                    setattr(value, "nuSMV_NuSmvModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def nuSMV_Module4(self):
        return self.__nuSMV_Module4

    @nuSMV_Module4.setter
    def nuSMV_Module4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nuSMV_Module__nuSMV_Module4", None)
        self.__nuSMV_Module4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nuSMV_ModuleElement"):
                    opp_val = getattr(item, "nuSMV_ModuleElement", None)
                    
                    if opp_val == self:
                        setattr(item, "nuSMV_ModuleElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nuSMV_ModuleElement"):
                    opp_val = getattr(item, "nuSMV_ModuleElement", None)
                    
                    setattr(item, "nuSMV_ModuleElement", self)
                    

    @property
    def nuSMV_Module46(self):
        return self.__nuSMV_Module46

    @nuSMV_Module46.setter
    def nuSMV_Module46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nuSMV_Module__nuSMV_Module46", None)
        self.__nuSMV_Module46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nuSMV_ModuleType"):
                opp_val = getattr(old_value, "nuSMV_ModuleType", None)
                if opp_val == self:
                    setattr(old_value, "nuSMV_ModuleType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nuSMV_ModuleType"):
                opp_val = getattr(value, "nuSMV_ModuleType", None)
                setattr(value, "nuSMV_ModuleType", self)

class nuSMV_NuSmvModel:

    pass