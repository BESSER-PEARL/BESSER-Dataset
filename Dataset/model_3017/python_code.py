from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class FunctionName(Enum):
    SIN = "SIN"
    COS = "COS"
    TAN = "TAN"
    EXP = "EXP"
    LN = "LN"
    ABS = "ABS"
    SQRT = "SQRT"
    LOG10 = "LOG10"
    ARCSIN = "ARCSIN"
    ARCCOS = "ARCCOS"
    ARCTAN = "ARCTAN"
    SIGN = "SIGN"
    FRAC = "FRAC"
    CEIL = "CEIL"
    TRUNK = "TRUNK"
    FLOOR = "FLOOR"
class Fixing(Enum):
    None = "None"
    Entry = "Entry"
    TopDown = "TopDown"
    BottomUp = "BottomUp"
class Language(Enum):
    DE = "DE"
    EL = "EL"
    EN = "EN"
    ES = "ES"
    ET = "ET"
    FI = "FI"
    FR = "FR"
    HE = "HE"
    HR = "HR"
    HU = "HU"
    ID = "ID"
    IS = "IS"
    AF = "AF"
    AR = "AR"
    BG = "BG"
    CA = "CA"
    CS = "CS"
    DA = "DA"
    SV = "SV"
    TH = "TH"
    TR = "TR"
    UK = "UK"
    Z1 = "Z1"
    ZF = "ZF"
    ZH = "ZH"
    IT = "IT"
    JA = "JA"
    KO = "KO"
    LT = "LT"
    LV = "LV"
    MS = "MS"
    NL = "NL"
    NO = "NO"
    PL = "PL"
    PT = "PT"
    RO = "RO"
    RU = "RU"
    SH = "SH"
    SK = "SK"
    SL = "SL"
    SR = "SR"
class ProcedureLocation(Enum):
    ROOT = "ROOT"
    SELF = "SELF"
    PARENT = "PARENT"
class ComparisonOperator(Enum):
    EQ = "EQ"
    NE = "NE"
    GT = "GT"
    GE = "GE"
    LT = "LT"
    LE = "LE"
class UnaryExpressionOperator(Enum):
    PLUS = "PLUS"
    MINUS = "MINUS"
    LC = "LC"
    UC = "UC"
class Status(Enum):
    InPreparation = "InPreparation"
    Locked = "Locked"
    Released = "Released"
class OptionType(Enum):
    ECM = "ECM"
    UPS = "UPS"
    KeyDate = "KeyDate"


############################################
# Definition of Classes
############################################

class vcml_List:

    pass
class List:

    pass
class vcml_SymbolList(List):

    pass
class vcml_NumberList(List):

    pass
class NumberListEntry:

    pass
class vcml_NumericInterval(NumberListEntry):

    def __init__(self, lowerBound: str, upperBound: str, lowerBoundOp: str, upperBoundOp: str):
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.lowerBoundOp = lowerBoundOp
        self.upperBoundOp = upperBoundOp
        
    @property
    def lowerBoundOp(self) -> str:
        return self.__lowerBoundOp

    @lowerBoundOp.setter
    def lowerBoundOp(self, lowerBoundOp: str):
        self.__lowerBoundOp = lowerBoundOp

    @property
    def upperBoundOp(self) -> str:
        return self.__upperBoundOp

    @upperBoundOp.setter
    def upperBoundOp(self, upperBoundOp: str):
        self.__upperBoundOp = upperBoundOp

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

class Expression:

    pass
class vcml_SumParts(Expression):

    def __init__(self, location: str, vcml_SumParts: "vcml_Characteristic" = None):
        self.location = location
        self.vcml_SumParts = vcml_SumParts
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def vcml_SumParts(self):
        return self.__vcml_SumParts

    @vcml_SumParts.setter
    def vcml_SumParts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_SumParts__vcml_SumParts", None)
        self.__vcml_SumParts = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_Characteristic229"):
                opp_val = getattr(old_value, "vcml_Characteristic229", None)
                if opp_val == self:
                    setattr(old_value, "vcml_Characteristic229", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_Characteristic229"):
                opp_val = getattr(value, "vcml_Characteristic229", None)
                setattr(value, "vcml_Characteristic229", self)

class vcml_FunctionCall(Expression):

    def __init__(self, function: str, vcml_FunctionCall: "vcml_Expression" = None):
        self.function = function
        self.vcml_FunctionCall = vcml_FunctionCall
        
    @property
    def function(self) -> str:
        return self.__function

    @function.setter
    def function(self, function: str):
        self.__function = function

    @property
    def vcml_FunctionCall(self):
        return self.__vcml_FunctionCall

    @vcml_FunctionCall.setter
    def vcml_FunctionCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_FunctionCall__vcml_FunctionCall", None)
        self.__vcml_FunctionCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_Expression227"):
                opp_val = getattr(old_value, "vcml_Expression227", None)
                if opp_val == self:
                    setattr(old_value, "vcml_Expression227", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_Expression227"):
                opp_val = getattr(value, "vcml_Expression227", None)
                setattr(value, "vcml_Expression227", self)

class vcml_BinaryExpression(Expression):

    def __init__(self, operator: str, vcml_BinaryExpression: "vcml_Expression" = None, vcml_BinaryExpression272: "vcml_Expression" = None):
        self.operator = operator
        self.vcml_BinaryExpression = vcml_BinaryExpression
        self.vcml_BinaryExpression272 = vcml_BinaryExpression272
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def vcml_BinaryExpression272(self):
        return self.__vcml_BinaryExpression272

    @vcml_BinaryExpression272.setter
    def vcml_BinaryExpression272(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_BinaryExpression__vcml_BinaryExpression272", None)
        self.__vcml_BinaryExpression272 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_Expression273"):
                opp_val = getattr(old_value, "vcml_Expression273", None)
                if opp_val == self:
                    setattr(old_value, "vcml_Expression273", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_Expression273"):
                opp_val = getattr(value, "vcml_Expression273", None)
                setattr(value, "vcml_Expression273", self)

    @property
    def vcml_BinaryExpression(self):
        return self.__vcml_BinaryExpression

    @vcml_BinaryExpression.setter
    def vcml_BinaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_BinaryExpression__vcml_BinaryExpression", None)
        self.__vcml_BinaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_Expression270"):
                opp_val = getattr(old_value, "vcml_Expression270", None)
                if opp_val == self:
                    setattr(old_value, "vcml_Expression270", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_Expression270"):
                opp_val = getattr(value, "vcml_Expression270", None)
                setattr(value, "vcml_Expression270", self)

class vcml_UnaryExpression(Expression):

    def __init__(self, operator: str, vcml_UnaryExpression: "vcml_Expression" = None):
        self.operator = operator
        self.vcml_UnaryExpression = vcml_UnaryExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def vcml_UnaryExpression(self):
        return self.__vcml_UnaryExpression

    @vcml_UnaryExpression.setter
    def vcml_UnaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_UnaryExpression__vcml_UnaryExpression", None)
        self.__vcml_UnaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_Expression225"):
                opp_val = getattr(old_value, "vcml_Expression225", None)
                if opp_val == self:
                    setattr(old_value, "vcml_Expression225", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_Expression225"):
                opp_val = getattr(value, "vcml_Expression225", None)
                setattr(value, "vcml_Expression225", self)

class vcml_CountParts(Expression):

    def __init__(self, location: str):
        self.location = location
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

class SetOrDelDefault:

    pass
class vcml_DelDefault(SetOrDelDefault):

    pass
class vcml_SetDefault(SetOrDelDefault):

    pass
class vcml_Expression:

    pass
class SimpleStatement:

    pass
class vcml_SetOrDelDefault(SimpleStatement):

    pass
class vcml_IsInvisible(SimpleStatement):

    pass
class vcml_SetPricingFactor(SimpleStatement):

    def __init__(self, location: str, vcml_SetPricingFactor: "vcml_Characteristic" = None, vcml_SetPricingFactor217: "vcml_Expression" = None, vcml_SetPricingFactor220: "vcml_Expression" = None):
        self.location = location
        self.vcml_SetPricingFactor = vcml_SetPricingFactor
        self.vcml_SetPricingFactor217 = vcml_SetPricingFactor217
        self.vcml_SetPricingFactor220 = vcml_SetPricingFactor220
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def vcml_SetPricingFactor(self):
        return self.__vcml_SetPricingFactor

    @vcml_SetPricingFactor.setter
    def vcml_SetPricingFactor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_SetPricingFactor__vcml_SetPricingFactor", None)
        self.__vcml_SetPricingFactor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_Characteristic215"):
                opp_val = getattr(old_value, "vcml_Characteristic215", None)
                if opp_val == self:
                    setattr(old_value, "vcml_Characteristic215", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_Characteristic215"):
                opp_val = getattr(value, "vcml_Characteristic215", None)
                setattr(value, "vcml_Characteristic215", self)

    @property
    def vcml_SetPricingFactor217(self):
        return self.__vcml_SetPricingFactor217

    @vcml_SetPricingFactor217.setter
    def vcml_SetPricingFactor217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_SetPricingFactor__vcml_SetPricingFactor217", None)
        self.__vcml_SetPricingFactor217 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_Expression218"):
                opp_val = getattr(old_value, "vcml_Expression218", None)
                if opp_val == self:
                    setattr(old_value, "vcml_Expression218", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_Expression218"):
                opp_val = getattr(value, "vcml_Expression218", None)
                setattr(value, "vcml_Expression218", self)

    @property
    def vcml_SetPricingFactor220(self):
        return self.__vcml_SetPricingFactor220

    @vcml_SetPricingFactor220.setter
    def vcml_SetPricingFactor220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_SetPricingFactor__vcml_SetPricingFactor220", None)
        self.__vcml_SetPricingFactor220 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_Expression221"):
                opp_val = getattr(old_value, "vcml_Expression221", None)
                if opp_val == self:
                    setattr(old_value, "vcml_Expression221", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_Expression221"):
                opp_val = getattr(value, "vcml_Expression221", None)
                setattr(value, "vcml_Expression221", self)

class vcml_Assignment(SimpleStatement):

    pass
class Statement:

    pass
class vcml_SimpleStatement(Statement):

    pass
class vcml_ConditionalStatement(Statement):

    pass
class vcml_CompoundStatement(Statement):

    pass
class vcml_Statement:

    pass
class FunctionOrTable:

    pass
class vcml_FunctionOrTable:

    pass
class vcml_EObject:

    pass
class CharacteristicReference_C:

    pass
class vcml_ShortVarReference(CharacteristicReference_C):

    pass
class vcml_ObjectCharacteristicReference(CharacteristicReference_C):

    pass
class Literal:

    pass
class vcml_MDataCharacteristic_C(Literal):

    pass
class vcml_MDataCharacteristic_P(Literal):

    pass
class vcml_NumericLiteral(Literal, NumberListEntry):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class vcml_SymbolicLiteral(Literal):

    def __init__(self, value: str, vcml_SymbolicLiteral: "vcml_SymbolList" = None):
        self.value = value
        self.vcml_SymbolicLiteral = vcml_SymbolicLiteral
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def vcml_SymbolicLiteral(self):
        return self.__vcml_SymbolicLiteral

    @vcml_SymbolicLiteral.setter
    def vcml_SymbolicLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_SymbolicLiteral__vcml_SymbolicLiteral", None)
        self.__vcml_SymbolicLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_SymbolList"):
                opp_val = getattr(old_value, "vcml_SymbolList", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_SymbolList"):
                opp_val = getattr(value, "vcml_SymbolList", None)
                if opp_val is None:
                    setattr(value, "vcml_SymbolList", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class vcml_CharacteristicReference_P(Literal):

    def __init__(self, location: str, vcml_CharacteristicReference_P: "vcml_Characteristic" = None, vcml_CharacteristicReference_P233: "vcml_MDataCharacteristic_P" = None, vcml_CharacteristicReference_P252: "vcml_InCondition_P" = None, vcml_CharacteristicReference_P244: "vcml_IsSpecified_P" = None):
        self.location = location
        self.vcml_CharacteristicReference_P = vcml_CharacteristicReference_P
        self.vcml_CharacteristicReference_P233 = vcml_CharacteristicReference_P233
        self.vcml_CharacteristicReference_P252 = vcml_CharacteristicReference_P252
        self.vcml_CharacteristicReference_P244 = vcml_CharacteristicReference_P244
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def vcml_CharacteristicReference_P233(self):
        return self.__vcml_CharacteristicReference_P233

    @vcml_CharacteristicReference_P233.setter
    def vcml_CharacteristicReference_P233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_CharacteristicReference_P__vcml_CharacteristicReference_P233", None)
        self.__vcml_CharacteristicReference_P233 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_MDataCharacteristic_P"):
                opp_val = getattr(old_value, "vcml_MDataCharacteristic_P", None)
                if opp_val == self:
                    setattr(old_value, "vcml_MDataCharacteristic_P", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_MDataCharacteristic_P"):
                opp_val = getattr(value, "vcml_MDataCharacteristic_P", None)
                setattr(value, "vcml_MDataCharacteristic_P", self)

    @property
    def vcml_CharacteristicReference_P244(self):
        return self.__vcml_CharacteristicReference_P244

    @vcml_CharacteristicReference_P244.setter
    def vcml_CharacteristicReference_P244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_CharacteristicReference_P__vcml_CharacteristicReference_P244", None)
        self.__vcml_CharacteristicReference_P244 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_IsSpecified_P"):
                opp_val = getattr(old_value, "vcml_IsSpecified_P", None)
                if opp_val == self:
                    setattr(old_value, "vcml_IsSpecified_P", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_IsSpecified_P"):
                opp_val = getattr(value, "vcml_IsSpecified_P", None)
                setattr(value, "vcml_IsSpecified_P", self)

    @property
    def vcml_CharacteristicReference_P252(self):
        return self.__vcml_CharacteristicReference_P252

    @vcml_CharacteristicReference_P252.setter
    def vcml_CharacteristicReference_P252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_CharacteristicReference_P__vcml_CharacteristicReference_P252", None)
        self.__vcml_CharacteristicReference_P252 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_InCondition_P"):
                opp_val = getattr(old_value, "vcml_InCondition_P", None)
                if opp_val == self:
                    setattr(old_value, "vcml_InCondition_P", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_InCondition_P"):
                opp_val = getattr(value, "vcml_InCondition_P", None)
                setattr(value, "vcml_InCondition_P", self)

    @property
    def vcml_CharacteristicReference_P(self):
        return self.__vcml_CharacteristicReference_P

    @vcml_CharacteristicReference_P.setter
    def vcml_CharacteristicReference_P(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_CharacteristicReference_P__vcml_CharacteristicReference_P", None)
        self.__vcml_CharacteristicReference_P = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_Characteristic223"):
                opp_val = getattr(old_value, "vcml_Characteristic223", None)
                if opp_val == self:
                    setattr(old_value, "vcml_Characteristic223", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_Characteristic223"):
                opp_val = getattr(value, "vcml_Characteristic223", None)
                setattr(value, "vcml_Characteristic223", self)

class vcml_PartialKey:

    def __init__(self, key: str, vcml_PartialKey153: "vcml_Material" = None, vcml_PartialKey: "vcml_ObjectType" = None):
        self.key = key
        self.vcml_PartialKey153 = vcml_PartialKey153
        self.vcml_PartialKey = vcml_PartialKey
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def vcml_PartialKey153(self):
        return self.__vcml_PartialKey153

    @vcml_PartialKey153.setter
    def vcml_PartialKey153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_PartialKey__vcml_PartialKey153", None)
        self.__vcml_PartialKey153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_Material154"):
                opp_val = getattr(old_value, "vcml_Material154", None)
                if opp_val == self:
                    setattr(old_value, "vcml_Material154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_Material154"):
                opp_val = getattr(value, "vcml_Material154", None)
                setattr(value, "vcml_Material154", self)

    @property
    def vcml_PartialKey(self):
        return self.__vcml_PartialKey

    @vcml_PartialKey.setter
    def vcml_PartialKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_PartialKey__vcml_PartialKey", None)
        self.__vcml_PartialKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_ObjectType151"):
                opp_val = getattr(old_value, "vcml_ObjectType151", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_ObjectType151"):
                opp_val = getattr(value, "vcml_ObjectType151", None)
                if opp_val is None:
                    setattr(value, "vcml_ObjectType151", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class vcml_ObjectType:

    def __init__(self, type: str, classType: int, vcml_ObjectType: "vcml_ConstraintMaterial" = None, vcml_ObjectType151: set["vcml_PartialKey"] = None, vcml_ObjectType246: "vcml_TypeOf" = None):
        self.type = type
        self.classType = classType
        self.vcml_ObjectType = vcml_ObjectType
        self.vcml_ObjectType151 = vcml_ObjectType151 if vcml_ObjectType151 is not None else set()
        self.vcml_ObjectType246 = vcml_ObjectType246
        
    @property
    def classType(self) -> int:
        return self.__classType

    @classType.setter
    def classType(self, classType: int):
        self.__classType = classType

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def vcml_ObjectType(self):
        return self.__vcml_ObjectType

    @vcml_ObjectType.setter
    def vcml_ObjectType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_ObjectType__vcml_ObjectType", None)
        self.__vcml_ObjectType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_ConstraintMaterial"):
                opp_val = getattr(old_value, "vcml_ConstraintMaterial", None)
                if opp_val == self:
                    setattr(old_value, "vcml_ConstraintMaterial", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_ConstraintMaterial"):
                opp_val = getattr(value, "vcml_ConstraintMaterial", None)
                setattr(value, "vcml_ConstraintMaterial", self)

    @property
    def vcml_ObjectType246(self):
        return self.__vcml_ObjectType246

    @vcml_ObjectType246.setter
    def vcml_ObjectType246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_ObjectType__vcml_ObjectType246", None)
        self.__vcml_ObjectType246 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_TypeOf"):
                opp_val = getattr(old_value, "vcml_TypeOf", None)
                if opp_val == self:
                    setattr(old_value, "vcml_TypeOf", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_TypeOf"):
                opp_val = getattr(value, "vcml_TypeOf", None)
                setattr(value, "vcml_TypeOf", self)

    @property
    def vcml_ObjectType151(self):
        return self.__vcml_ObjectType151

    @vcml_ObjectType151.setter
    def vcml_ObjectType151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_ObjectType__vcml_ObjectType151", None)
        self.__vcml_ObjectType151 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vcml_PartialKey"):
                    opp_val = getattr(item, "vcml_PartialKey", None)
                    
                    if opp_val == self:
                        setattr(item, "vcml_PartialKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vcml_PartialKey"):
                    opp_val = getattr(item, "vcml_PartialKey", None)
                    
                    setattr(item, "vcml_PartialKey", self)
                    

class ConstraintObject:

    pass
class vcml_ConstraintMaterial(ConstraintObject):

    pass
class vcml_ConstraintClass(ConstraintObject):

    pass
class Condition:

    pass
class vcml_UnaryCondition(Condition):

    pass
class vcml_TypeOf(Condition):

    def __init__(self, location: str, vcml_TypeOf: "vcml_ObjectType" = None):
        self.location = location
        self.vcml_TypeOf = vcml_TypeOf
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def vcml_TypeOf(self):
        return self.__vcml_TypeOf

    @vcml_TypeOf.setter
    def vcml_TypeOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_TypeOf__vcml_TypeOf", None)
        self.__vcml_TypeOf = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_ObjectType246"):
                opp_val = getattr(old_value, "vcml_ObjectType246", None)
                if opp_val == self:
                    setattr(old_value, "vcml_ObjectType246", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_ObjectType246"):
                opp_val = getattr(value, "vcml_ObjectType246", None)
                setattr(value, "vcml_ObjectType246", self)

class vcml_PFunction(FunctionOrTable, SimpleStatement, Condition):

    pass
class vcml_BinaryCondition(Condition):

    def __init__(self, operator: str, vcml_BinaryCondition277: "vcml_Condition" = None, vcml_BinaryCondition: "vcml_Condition" = None):
        self.operator = operator
        self.vcml_BinaryCondition277 = vcml_BinaryCondition277
        self.vcml_BinaryCondition = vcml_BinaryCondition
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def vcml_BinaryCondition277(self):
        return self.__vcml_BinaryCondition277

    @vcml_BinaryCondition277.setter
    def vcml_BinaryCondition277(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_BinaryCondition__vcml_BinaryCondition277", None)
        self.__vcml_BinaryCondition277 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_Condition278"):
                opp_val = getattr(old_value, "vcml_Condition278", None)
                if opp_val == self:
                    setattr(old_value, "vcml_Condition278", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_Condition278"):
                opp_val = getattr(value, "vcml_Condition278", None)
                setattr(value, "vcml_Condition278", self)

    @property
    def vcml_BinaryCondition(self):
        return self.__vcml_BinaryCondition

    @vcml_BinaryCondition.setter
    def vcml_BinaryCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_BinaryCondition__vcml_BinaryCondition", None)
        self.__vcml_BinaryCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_Condition275"):
                opp_val = getattr(old_value, "vcml_Condition275", None)
                if opp_val == self:
                    setattr(old_value, "vcml_Condition275", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_Condition275"):
                opp_val = getattr(value, "vcml_Condition275", None)
                setattr(value, "vcml_Condition275", self)

class vcml_InCondition_P(Condition):

    pass
class vcml_IsSpecified_P(Condition):

    pass
class ConstraintRestriction:

    pass
class vcml_Table(ConstraintRestriction, FunctionOrTable, SimpleStatement, Condition):

    pass
class vcml_InCondition_C(ConstraintRestriction, Condition):

    pass
class vcml_IsSpecified_C(ConstraintRestriction, Condition):

    pass
class vcml_Function(ConstraintRestriction, FunctionOrTable, SimpleStatement, Condition):

    pass
class vcml_NegatedConstraintRestrictionLHS(ConstraintRestriction):

    pass
class vcml_SubpartOfCondition(ConstraintRestriction, Condition):

    pass
class vcml_Comparison(ConstraintRestriction, Condition):

    def __init__(self, operator: str, vcml_Comparison: "vcml_Expression" = None, vcml_Comparison239: "vcml_Expression" = None):
        self.operator = operator
        self.vcml_Comparison = vcml_Comparison
        self.vcml_Comparison239 = vcml_Comparison239
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def vcml_Comparison(self):
        return self.__vcml_Comparison

    @vcml_Comparison.setter
    def vcml_Comparison(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Comparison__vcml_Comparison", None)
        self.__vcml_Comparison = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_Expression237"):
                opp_val = getattr(old_value, "vcml_Expression237", None)
                if opp_val == self:
                    setattr(old_value, "vcml_Expression237", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_Expression237"):
                opp_val = getattr(value, "vcml_Expression237", None)
                setattr(value, "vcml_Expression237", self)

    @property
    def vcml_Comparison239(self):
        return self.__vcml_Comparison239

    @vcml_Comparison239.setter
    def vcml_Comparison239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Comparison__vcml_Comparison239", None)
        self.__vcml_Comparison239 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_Expression240"):
                opp_val = getattr(old_value, "vcml_Expression240", None)
                if opp_val == self:
                    setattr(old_value, "vcml_Expression240", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_Expression240"):
                opp_val = getattr(value, "vcml_Expression240", None)
                setattr(value, "vcml_Expression240", self)

class vcml_ConditionalConstraintRestriction(ConstraintRestriction):

    pass
class vcml_ConstraintRestrictionFalse(ConstraintRestriction):

    pass
class vcml_PartOfCondition(ConstraintRestriction, Condition):

    pass
class vcml_ConstraintObject:

    def __init__(self, name: str, vcml_ConstraintObject146: set["vcml_ShortVarDefinition"] = None, vcml_ConstraintObject: "vcml_ConstraintSource" = None, vcml_ConstraintObject159: "vcml_PartOfCondition" = None, vcml_ConstraintObject170: "vcml_ObjectCharacteristicReference" = None, vcml_ConstraintObject162: "vcml_PartOfCondition" = None, vcml_ConstraintObject164: "vcml_SubpartOfCondition" = None, vcml_ConstraintObject167: "vcml_SubpartOfCondition" = None):
        self.name = name
        self.vcml_ConstraintObject146 = vcml_ConstraintObject146 if vcml_ConstraintObject146 is not None else set()
        self.vcml_ConstraintObject = vcml_ConstraintObject
        self.vcml_ConstraintObject159 = vcml_ConstraintObject159
        self.vcml_ConstraintObject170 = vcml_ConstraintObject170
        self.vcml_ConstraintObject162 = vcml_ConstraintObject162
        self.vcml_ConstraintObject164 = vcml_ConstraintObject164
        self.vcml_ConstraintObject167 = vcml_ConstraintObject167
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def vcml_ConstraintObject167(self):
        return self.__vcml_ConstraintObject167

    @vcml_ConstraintObject167.setter
    def vcml_ConstraintObject167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_ConstraintObject__vcml_ConstraintObject167", None)
        self.__vcml_ConstraintObject167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_SubpartOfCondition166"):
                opp_val = getattr(old_value, "vcml_SubpartOfCondition166", None)
                if opp_val == self:
                    setattr(old_value, "vcml_SubpartOfCondition166", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_SubpartOfCondition166"):
                opp_val = getattr(value, "vcml_SubpartOfCondition166", None)
                setattr(value, "vcml_SubpartOfCondition166", self)

    @property
    def vcml_ConstraintObject162(self):
        return self.__vcml_ConstraintObject162

    @vcml_ConstraintObject162.setter
    def vcml_ConstraintObject162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_ConstraintObject__vcml_ConstraintObject162", None)
        self.__vcml_ConstraintObject162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_PartOfCondition161"):
                opp_val = getattr(old_value, "vcml_PartOfCondition161", None)
                if opp_val == self:
                    setattr(old_value, "vcml_PartOfCondition161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_PartOfCondition161"):
                opp_val = getattr(value, "vcml_PartOfCondition161", None)
                setattr(value, "vcml_PartOfCondition161", self)

    @property
    def vcml_ConstraintObject164(self):
        return self.__vcml_ConstraintObject164

    @vcml_ConstraintObject164.setter
    def vcml_ConstraintObject164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_ConstraintObject__vcml_ConstraintObject164", None)
        self.__vcml_ConstraintObject164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_SubpartOfCondition"):
                opp_val = getattr(old_value, "vcml_SubpartOfCondition", None)
                if opp_val == self:
                    setattr(old_value, "vcml_SubpartOfCondition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_SubpartOfCondition"):
                opp_val = getattr(value, "vcml_SubpartOfCondition", None)
                setattr(value, "vcml_SubpartOfCondition", self)

    @property
    def vcml_ConstraintObject(self):
        return self.__vcml_ConstraintObject

    @vcml_ConstraintObject.setter
    def vcml_ConstraintObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_ConstraintObject__vcml_ConstraintObject", None)
        self.__vcml_ConstraintObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_ConstraintSource137"):
                opp_val = getattr(old_value, "vcml_ConstraintSource137", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_ConstraintSource137"):
                opp_val = getattr(value, "vcml_ConstraintSource137", None)
                if opp_val is None:
                    setattr(value, "vcml_ConstraintSource137", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vcml_ConstraintObject146(self):
        return self.__vcml_ConstraintObject146

    @vcml_ConstraintObject146.setter
    def vcml_ConstraintObject146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_ConstraintObject__vcml_ConstraintObject146", None)
        self.__vcml_ConstraintObject146 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vcml_ShortVarDefinition"):
                    opp_val = getattr(item, "vcml_ShortVarDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "vcml_ShortVarDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vcml_ShortVarDefinition"):
                    opp_val = getattr(item, "vcml_ShortVarDefinition", None)
                    
                    setattr(item, "vcml_ShortVarDefinition", self)
                    

    @property
    def vcml_ConstraintObject159(self):
        return self.__vcml_ConstraintObject159

    @vcml_ConstraintObject159.setter
    def vcml_ConstraintObject159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_ConstraintObject__vcml_ConstraintObject159", None)
        self.__vcml_ConstraintObject159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_PartOfCondition"):
                opp_val = getattr(old_value, "vcml_PartOfCondition", None)
                if opp_val == self:
                    setattr(old_value, "vcml_PartOfCondition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_PartOfCondition"):
                opp_val = getattr(value, "vcml_PartOfCondition", None)
                setattr(value, "vcml_PartOfCondition", self)

    @property
    def vcml_ConstraintObject170(self):
        return self.__vcml_ConstraintObject170

    @vcml_ConstraintObject170.setter
    def vcml_ConstraintObject170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_ConstraintObject__vcml_ConstraintObject170", None)
        self.__vcml_ConstraintObject170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_ObjectCharacteristicReference"):
                opp_val = getattr(old_value, "vcml_ObjectCharacteristicReference", None)
                if opp_val == self:
                    setattr(old_value, "vcml_ObjectCharacteristicReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_ObjectCharacteristicReference"):
                opp_val = getattr(value, "vcml_ObjectCharacteristicReference", None)
                setattr(value, "vcml_ObjectCharacteristicReference", self)

class vcml_FormattedDocumentationBlock:

    def __init__(self, value: str, format: str, vcml_FormattedDocumentationBlock: "vcml_MultipleLanguageDocumentation_LanguageBlock" = None):
        self.value = value
        self.format = format
        self.vcml_FormattedDocumentationBlock = vcml_FormattedDocumentationBlock
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def format(self) -> str:
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format

    @property
    def vcml_FormattedDocumentationBlock(self):
        return self.__vcml_FormattedDocumentationBlock

    @vcml_FormattedDocumentationBlock.setter
    def vcml_FormattedDocumentationBlock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_FormattedDocumentationBlock__vcml_FormattedDocumentationBlock", None)
        self.__vcml_FormattedDocumentationBlock = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_MultipleLanguageDocumentation_LanguageBlock135"):
                opp_val = getattr(old_value, "vcml_MultipleLanguageDocumentation_LanguageBlock135", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_MultipleLanguageDocumentation_LanguageBlock135"):
                opp_val = getattr(value, "vcml_MultipleLanguageDocumentation_LanguageBlock135", None)
                if opp_val is None:
                    setattr(value, "vcml_MultipleLanguageDocumentation_LanguageBlock135", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class vcml_MultipleLanguageDocumentation_LanguageBlock:

    def __init__(self, language: str, vcml_MultipleLanguageDocumentation_LanguageBlock: "vcml_MultipleLanguageDocumentation" = None, vcml_MultipleLanguageDocumentation_LanguageBlock135: set["vcml_FormattedDocumentationBlock"] = None):
        self.language = language
        self.vcml_MultipleLanguageDocumentation_LanguageBlock = vcml_MultipleLanguageDocumentation_LanguageBlock
        self.vcml_MultipleLanguageDocumentation_LanguageBlock135 = vcml_MultipleLanguageDocumentation_LanguageBlock135 if vcml_MultipleLanguageDocumentation_LanguageBlock135 is not None else set()
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def vcml_MultipleLanguageDocumentation_LanguageBlock135(self):
        return self.__vcml_MultipleLanguageDocumentation_LanguageBlock135

    @vcml_MultipleLanguageDocumentation_LanguageBlock135.setter
    def vcml_MultipleLanguageDocumentation_LanguageBlock135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_MultipleLanguageDocumentation_LanguageBlock__vcml_MultipleLanguageDocumentation_LanguageBlock135", None)
        self.__vcml_MultipleLanguageDocumentation_LanguageBlock135 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vcml_FormattedDocumentationBlock"):
                    opp_val = getattr(item, "vcml_FormattedDocumentationBlock", None)
                    
                    if opp_val == self:
                        setattr(item, "vcml_FormattedDocumentationBlock", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vcml_FormattedDocumentationBlock"):
                    opp_val = getattr(item, "vcml_FormattedDocumentationBlock", None)
                    
                    setattr(item, "vcml_FormattedDocumentationBlock", self)
                    

    @property
    def vcml_MultipleLanguageDocumentation_LanguageBlock(self):
        return self.__vcml_MultipleLanguageDocumentation_LanguageBlock

    @vcml_MultipleLanguageDocumentation_LanguageBlock.setter
    def vcml_MultipleLanguageDocumentation_LanguageBlock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_MultipleLanguageDocumentation_LanguageBlock__vcml_MultipleLanguageDocumentation_LanguageBlock", None)
        self.__vcml_MultipleLanguageDocumentation_LanguageBlock = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_MultipleLanguageDocumentation"):
                opp_val = getattr(old_value, "vcml_MultipleLanguageDocumentation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_MultipleLanguageDocumentation"):
                opp_val = getattr(value, "vcml_MultipleLanguageDocumentation", None)
                if opp_val is None:
                    setattr(value, "vcml_MultipleLanguageDocumentation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class vcml_ShortVarDefinition:

    def __init__(self, name: str, vcml_ShortVarDefinition: "vcml_ConstraintObject" = None, vcml_ShortVarDefinition156: "vcml_Characteristic" = None, vcml_ShortVarDefinition175: "vcml_ShortVarReference" = None):
        self.name = name
        self.vcml_ShortVarDefinition = vcml_ShortVarDefinition
        self.vcml_ShortVarDefinition156 = vcml_ShortVarDefinition156
        self.vcml_ShortVarDefinition175 = vcml_ShortVarDefinition175
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def vcml_ShortVarDefinition175(self):
        return self.__vcml_ShortVarDefinition175

    @vcml_ShortVarDefinition175.setter
    def vcml_ShortVarDefinition175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_ShortVarDefinition__vcml_ShortVarDefinition175", None)
        self.__vcml_ShortVarDefinition175 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_ShortVarReference"):
                opp_val = getattr(old_value, "vcml_ShortVarReference", None)
                if opp_val == self:
                    setattr(old_value, "vcml_ShortVarReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_ShortVarReference"):
                opp_val = getattr(value, "vcml_ShortVarReference", None)
                setattr(value, "vcml_ShortVarReference", self)

    @property
    def vcml_ShortVarDefinition156(self):
        return self.__vcml_ShortVarDefinition156

    @vcml_ShortVarDefinition156.setter
    def vcml_ShortVarDefinition156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_ShortVarDefinition__vcml_ShortVarDefinition156", None)
        self.__vcml_ShortVarDefinition156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_Characteristic157"):
                opp_val = getattr(old_value, "vcml_Characteristic157", None)
                if opp_val == self:
                    setattr(old_value, "vcml_Characteristic157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_Characteristic157"):
                opp_val = getattr(value, "vcml_Characteristic157", None)
                setattr(value, "vcml_Characteristic157", self)

    @property
    def vcml_ShortVarDefinition(self):
        return self.__vcml_ShortVarDefinition

    @vcml_ShortVarDefinition.setter
    def vcml_ShortVarDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_ShortVarDefinition__vcml_ShortVarDefinition", None)
        self.__vcml_ShortVarDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_ConstraintObject146"):
                opp_val = getattr(old_value, "vcml_ConstraintObject146", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_ConstraintObject146"):
                opp_val = getattr(value, "vcml_ConstraintObject146", None)
                if opp_val is None:
                    setattr(value, "vcml_ConstraintObject146", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class vcml_CharacteristicReference_C(Literal):

    pass
class vcml_ConstraintRestriction:

    pass
class Documentation:

    pass
class vcml_MultipleLanguageDocumentation(Documentation):

    pass
class vcml_SimpleDocumentation(Documentation):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class vcml_MultiLanguageDescription:

    def __init__(self, language: str, value: str, vcml_MultiLanguageDescription: "vcml_MultiLanguageDescriptions" = None):
        self.language = language
        self.value = value
        self.vcml_MultiLanguageDescription = vcml_MultiLanguageDescription
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def vcml_MultiLanguageDescription(self):
        return self.__vcml_MultiLanguageDescription

    @vcml_MultiLanguageDescription.setter
    def vcml_MultiLanguageDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_MultiLanguageDescription__vcml_MultiLanguageDescription", None)
        self.__vcml_MultiLanguageDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_MultiLanguageDescriptions"):
                opp_val = getattr(old_value, "vcml_MultiLanguageDescriptions", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_MultiLanguageDescriptions"):
                opp_val = getattr(value, "vcml_MultiLanguageDescriptions", None)
                if opp_val is None:
                    setattr(value, "vcml_MultiLanguageDescriptions", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class vcml_Row:

    pass
class Description:

    pass
class vcml_MultiLanguageDescriptions(Description):

    pass
class vcml_SimpleDescription(Description):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class vcml_ValueAssignment:

    pass
class vcml_VariantTableArgument:

    def __init__(self, key: bool, vcml_VariantTableArgument: "vcml_VariantTable" = None, vcml_VariantTableArgument123: "vcml_Characteristic" = None):
        self.key = key
        self.vcml_VariantTableArgument = vcml_VariantTableArgument
        self.vcml_VariantTableArgument123 = vcml_VariantTableArgument123
        
    @property
    def key(self) -> bool:
        return self.__key

    @key.setter
    def key(self, key: bool):
        self.__key = key

    @property
    def vcml_VariantTableArgument(self):
        return self.__vcml_VariantTableArgument

    @vcml_VariantTableArgument.setter
    def vcml_VariantTableArgument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_VariantTableArgument__vcml_VariantTableArgument", None)
        self.__vcml_VariantTableArgument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_VariantTable"):
                opp_val = getattr(old_value, "vcml_VariantTable", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_VariantTable"):
                opp_val = getattr(value, "vcml_VariantTable", None)
                if opp_val is None:
                    setattr(value, "vcml_VariantTable", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vcml_VariantTableArgument123(self):
        return self.__vcml_VariantTableArgument123

    @vcml_VariantTableArgument123.setter
    def vcml_VariantTableArgument123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_VariantTableArgument__vcml_VariantTableArgument123", None)
        self.__vcml_VariantTableArgument123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_Characteristic124"):
                opp_val = getattr(old_value, "vcml_Characteristic124", None)
                if opp_val == self:
                    setattr(old_value, "vcml_Characteristic124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_Characteristic124"):
                opp_val = getattr(value, "vcml_Characteristic124", None)
                setattr(value, "vcml_Characteristic124", self)

class vcml_VariantFunctionArgument:

    def __init__(self, in: bool, vcml_VariantFunctionArgument: "vcml_VariantFunction" = None, vcml_VariantFunctionArgument119: "vcml_Characteristic" = None):
        self.in = in
        self.vcml_VariantFunctionArgument = vcml_VariantFunctionArgument
        self.vcml_VariantFunctionArgument119 = vcml_VariantFunctionArgument119
        
    @property
    def in(self) -> bool:
        return self.__in

    @in.setter
    def in(self, in: bool):
        self.__in = in

    @property
    def vcml_VariantFunctionArgument(self):
        return self.__vcml_VariantFunctionArgument

    @vcml_VariantFunctionArgument.setter
    def vcml_VariantFunctionArgument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_VariantFunctionArgument__vcml_VariantFunctionArgument", None)
        self.__vcml_VariantFunctionArgument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_VariantFunction"):
                opp_val = getattr(old_value, "vcml_VariantFunction", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_VariantFunction"):
                opp_val = getattr(value, "vcml_VariantFunction", None)
                if opp_val is None:
                    setattr(value, "vcml_VariantFunction", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vcml_VariantFunctionArgument119(self):
        return self.__vcml_VariantFunctionArgument119

    @vcml_VariantFunctionArgument119.setter
    def vcml_VariantFunctionArgument119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_VariantFunctionArgument__vcml_VariantFunctionArgument119", None)
        self.__vcml_VariantFunctionArgument119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_Characteristic120"):
                opp_val = getattr(old_value, "vcml_Characteristic120", None)
                if opp_val == self:
                    setattr(old_value, "vcml_Characteristic120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_Characteristic120"):
                opp_val = getattr(value, "vcml_Characteristic120", None)
                setattr(value, "vcml_Characteristic120", self)

class vcml_Literal(Expression):

    pass
class vcml_Classification:

    pass
class vcml_CharacteristicGroup:

    def __init__(self, name: str, vcml_CharacteristicGroup: "vcml_InterfaceDesign" = None, vcml_CharacteristicGroup97: "vcml_Description" = None, vcml_CharacteristicGroup100: set["vcml_Characteristic"] = None):
        self.name = name
        self.vcml_CharacteristicGroup = vcml_CharacteristicGroup
        self.vcml_CharacteristicGroup97 = vcml_CharacteristicGroup97
        self.vcml_CharacteristicGroup100 = vcml_CharacteristicGroup100 if vcml_CharacteristicGroup100 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def vcml_CharacteristicGroup(self):
        return self.__vcml_CharacteristicGroup

    @vcml_CharacteristicGroup.setter
    def vcml_CharacteristicGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_CharacteristicGroup__vcml_CharacteristicGroup", None)
        self.__vcml_CharacteristicGroup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_InterfaceDesign95"):
                opp_val = getattr(old_value, "vcml_InterfaceDesign95", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_InterfaceDesign95"):
                opp_val = getattr(value, "vcml_InterfaceDesign95", None)
                if opp_val is None:
                    setattr(value, "vcml_InterfaceDesign95", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vcml_CharacteristicGroup97(self):
        return self.__vcml_CharacteristicGroup97

    @vcml_CharacteristicGroup97.setter
    def vcml_CharacteristicGroup97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_CharacteristicGroup__vcml_CharacteristicGroup97", None)
        self.__vcml_CharacteristicGroup97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_Description98"):
                opp_val = getattr(old_value, "vcml_Description98", None)
                if opp_val == self:
                    setattr(old_value, "vcml_Description98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_Description98"):
                opp_val = getattr(value, "vcml_Description98", None)
                setattr(value, "vcml_Description98", self)

    @property
    def vcml_CharacteristicGroup100(self):
        return self.__vcml_CharacteristicGroup100

    @vcml_CharacteristicGroup100.setter
    def vcml_CharacteristicGroup100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_CharacteristicGroup__vcml_CharacteristicGroup100", None)
        self.__vcml_CharacteristicGroup100 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vcml_Characteristic101"):
                    opp_val = getattr(item, "vcml_Characteristic101", None)
                    
                    if opp_val == self:
                        setattr(item, "vcml_Characteristic101", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vcml_Characteristic101"):
                    opp_val = getattr(item, "vcml_Characteristic101", None)
                    
                    setattr(item, "vcml_Characteristic101", self)
                    

class vcml_ConstraintSource:

    pass
class vcml_Condition:

    pass
class vcml_ConditionSource:

    pass
class vcml_ProcedureSource:

    pass
class Dependency:

    pass
class vcml_NumericCharacteristicValue:

    def __init__(self, default: bool, vcml_NumericCharacteristicValue36: "vcml_NumberListEntry" = None, vcml_NumericCharacteristicValue38: "vcml_Documentation" = None, vcml_NumericCharacteristicValue41: "vcml_CharacteristicOrValueDependencies" = None, vcml_NumericCharacteristicValue: "vcml_NumericType" = None):
        self.default = default
        self.vcml_NumericCharacteristicValue36 = vcml_NumericCharacteristicValue36
        self.vcml_NumericCharacteristicValue38 = vcml_NumericCharacteristicValue38
        self.vcml_NumericCharacteristicValue41 = vcml_NumericCharacteristicValue41
        self.vcml_NumericCharacteristicValue = vcml_NumericCharacteristicValue
        
    @property
    def default(self) -> bool:
        return self.__default

    @default.setter
    def default(self, default: bool):
        self.__default = default

    @property
    def vcml_NumericCharacteristicValue36(self):
        return self.__vcml_NumericCharacteristicValue36

    @vcml_NumericCharacteristicValue36.setter
    def vcml_NumericCharacteristicValue36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_NumericCharacteristicValue__vcml_NumericCharacteristicValue36", None)
        self.__vcml_NumericCharacteristicValue36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_NumberListEntry"):
                opp_val = getattr(old_value, "vcml_NumberListEntry", None)
                if opp_val == self:
                    setattr(old_value, "vcml_NumberListEntry", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_NumberListEntry"):
                opp_val = getattr(value, "vcml_NumberListEntry", None)
                setattr(value, "vcml_NumberListEntry", self)

    @property
    def vcml_NumericCharacteristicValue41(self):
        return self.__vcml_NumericCharacteristicValue41

    @vcml_NumericCharacteristicValue41.setter
    def vcml_NumericCharacteristicValue41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_NumericCharacteristicValue__vcml_NumericCharacteristicValue41", None)
        self.__vcml_NumericCharacteristicValue41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_CharacteristicOrValueDependencies42"):
                opp_val = getattr(old_value, "vcml_CharacteristicOrValueDependencies42", None)
                if opp_val == self:
                    setattr(old_value, "vcml_CharacteristicOrValueDependencies42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_CharacteristicOrValueDependencies42"):
                opp_val = getattr(value, "vcml_CharacteristicOrValueDependencies42", None)
                setattr(value, "vcml_CharacteristicOrValueDependencies42", self)

    @property
    def vcml_NumericCharacteristicValue(self):
        return self.__vcml_NumericCharacteristicValue

    @vcml_NumericCharacteristicValue.setter
    def vcml_NumericCharacteristicValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_NumericCharacteristicValue__vcml_NumericCharacteristicValue", None)
        self.__vcml_NumericCharacteristicValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_NumericType"):
                opp_val = getattr(old_value, "vcml_NumericType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_NumericType"):
                opp_val = getattr(value, "vcml_NumericType", None)
                if opp_val is None:
                    setattr(value, "vcml_NumericType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vcml_NumericCharacteristicValue38(self):
        return self.__vcml_NumericCharacteristicValue38

    @vcml_NumericCharacteristicValue38.setter
    def vcml_NumericCharacteristicValue38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_NumericCharacteristicValue__vcml_NumericCharacteristicValue38", None)
        self.__vcml_NumericCharacteristicValue38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_Documentation39"):
                opp_val = getattr(old_value, "vcml_Documentation39", None)
                if opp_val == self:
                    setattr(old_value, "vcml_Documentation39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_Documentation39"):
                opp_val = getattr(value, "vcml_Documentation39", None)
                setattr(value, "vcml_Documentation39", self)

class vcml_Dependency:

    pass
class vcml_NumberListEntry:

    pass
class vcml_DateCharacteristicValue:

    def __init__(self, from: str, to: str, default: bool, vcml_DateCharacteristicValue: "vcml_DateType" = None, vcml_DateCharacteristicValue44: "vcml_Documentation" = None, vcml_DateCharacteristicValue47: "vcml_CharacteristicOrValueDependencies" = None):
        self.from = from
        self.to = to
        self.default = default
        self.vcml_DateCharacteristicValue = vcml_DateCharacteristicValue
        self.vcml_DateCharacteristicValue44 = vcml_DateCharacteristicValue44
        self.vcml_DateCharacteristicValue47 = vcml_DateCharacteristicValue47
        
    @property
    def from(self) -> str:
        return self.__from

    @from.setter
    def from(self, from: str):
        self.__from = from

    @property
    def to(self) -> str:
        return self.__to

    @to.setter
    def to(self, to: str):
        self.__to = to

    @property
    def default(self) -> bool:
        return self.__default

    @default.setter
    def default(self, default: bool):
        self.__default = default

    @property
    def vcml_DateCharacteristicValue44(self):
        return self.__vcml_DateCharacteristicValue44

    @vcml_DateCharacteristicValue44.setter
    def vcml_DateCharacteristicValue44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_DateCharacteristicValue__vcml_DateCharacteristicValue44", None)
        self.__vcml_DateCharacteristicValue44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_Documentation45"):
                opp_val = getattr(old_value, "vcml_Documentation45", None)
                if opp_val == self:
                    setattr(old_value, "vcml_Documentation45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_Documentation45"):
                opp_val = getattr(value, "vcml_Documentation45", None)
                setattr(value, "vcml_Documentation45", self)

    @property
    def vcml_DateCharacteristicValue(self):
        return self.__vcml_DateCharacteristicValue

    @vcml_DateCharacteristicValue.setter
    def vcml_DateCharacteristicValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_DateCharacteristicValue__vcml_DateCharacteristicValue", None)
        self.__vcml_DateCharacteristicValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_DateType"):
                opp_val = getattr(old_value, "vcml_DateType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_DateType"):
                opp_val = getattr(value, "vcml_DateType", None)
                if opp_val is None:
                    setattr(value, "vcml_DateType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vcml_DateCharacteristicValue47(self):
        return self.__vcml_DateCharacteristicValue47

    @vcml_DateCharacteristicValue47.setter
    def vcml_DateCharacteristicValue47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_DateCharacteristicValue__vcml_DateCharacteristicValue47", None)
        self.__vcml_DateCharacteristicValue47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_CharacteristicOrValueDependencies48"):
                opp_val = getattr(old_value, "vcml_CharacteristicOrValueDependencies48", None)
                if opp_val == self:
                    setattr(old_value, "vcml_CharacteristicOrValueDependencies48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_CharacteristicOrValueDependencies48"):
                opp_val = getattr(value, "vcml_CharacteristicOrValueDependencies48", None)
                setattr(value, "vcml_CharacteristicOrValueDependencies48", self)

class vcml_CharacteristicValue:

    def __init__(self, name: str, default: bool, vcml_CharacteristicValue: "vcml_SymbolicType" = None, vcml_CharacteristicValue27: "vcml_Description" = None, vcml_CharacteristicValue30: "vcml_Documentation" = None, vcml_CharacteristicValue33: "vcml_CharacteristicOrValueDependencies" = None):
        self.name = name
        self.default = default
        self.vcml_CharacteristicValue = vcml_CharacteristicValue
        self.vcml_CharacteristicValue27 = vcml_CharacteristicValue27
        self.vcml_CharacteristicValue30 = vcml_CharacteristicValue30
        self.vcml_CharacteristicValue33 = vcml_CharacteristicValue33
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def default(self) -> bool:
        return self.__default

    @default.setter
    def default(self, default: bool):
        self.__default = default

    @property
    def vcml_CharacteristicValue(self):
        return self.__vcml_CharacteristicValue

    @vcml_CharacteristicValue.setter
    def vcml_CharacteristicValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_CharacteristicValue__vcml_CharacteristicValue", None)
        self.__vcml_CharacteristicValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_SymbolicType"):
                opp_val = getattr(old_value, "vcml_SymbolicType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_SymbolicType"):
                opp_val = getattr(value, "vcml_SymbolicType", None)
                if opp_val is None:
                    setattr(value, "vcml_SymbolicType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vcml_CharacteristicValue27(self):
        return self.__vcml_CharacteristicValue27

    @vcml_CharacteristicValue27.setter
    def vcml_CharacteristicValue27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_CharacteristicValue__vcml_CharacteristicValue27", None)
        self.__vcml_CharacteristicValue27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_Description28"):
                opp_val = getattr(old_value, "vcml_Description28", None)
                if opp_val == self:
                    setattr(old_value, "vcml_Description28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_Description28"):
                opp_val = getattr(value, "vcml_Description28", None)
                setattr(value, "vcml_Description28", self)

    @property
    def vcml_CharacteristicValue33(self):
        return self.__vcml_CharacteristicValue33

    @vcml_CharacteristicValue33.setter
    def vcml_CharacteristicValue33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_CharacteristicValue__vcml_CharacteristicValue33", None)
        self.__vcml_CharacteristicValue33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_CharacteristicOrValueDependencies34"):
                opp_val = getattr(old_value, "vcml_CharacteristicOrValueDependencies34", None)
                if opp_val == self:
                    setattr(old_value, "vcml_CharacteristicOrValueDependencies34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_CharacteristicOrValueDependencies34"):
                opp_val = getattr(value, "vcml_CharacteristicOrValueDependencies34", None)
                setattr(value, "vcml_CharacteristicOrValueDependencies34", self)

    @property
    def vcml_CharacteristicValue30(self):
        return self.__vcml_CharacteristicValue30

    @vcml_CharacteristicValue30.setter
    def vcml_CharacteristicValue30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_CharacteristicValue__vcml_CharacteristicValue30", None)
        self.__vcml_CharacteristicValue30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_Documentation31"):
                opp_val = getattr(old_value, "vcml_Documentation31", None)
                if opp_val == self:
                    setattr(old_value, "vcml_Documentation31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_Documentation31"):
                opp_val = getattr(value, "vcml_Documentation31", None)
                setattr(value, "vcml_Documentation31", self)

class VCObject:

    pass
class vcml_VariantTableContent(VCObject):

    pass
class vcml_VariantTable(VCObject):

    def __init__(self, status: str, group: str, vcml_VariantTable: set["vcml_VariantTableArgument"] = None, vcml_VariantTable126: "vcml_VariantTableContent" = None, vcml_VariantTable200: "vcml_Table" = None):
        self.status = status
        self.group = group
        self.vcml_VariantTable = vcml_VariantTable if vcml_VariantTable is not None else set()
        self.vcml_VariantTable126 = vcml_VariantTable126
        self.vcml_VariantTable200 = vcml_VariantTable200
        
    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def vcml_VariantTable(self):
        return self.__vcml_VariantTable

    @vcml_VariantTable.setter
    def vcml_VariantTable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_VariantTable__vcml_VariantTable", None)
        self.__vcml_VariantTable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vcml_VariantTableArgument"):
                    opp_val = getattr(item, "vcml_VariantTableArgument", None)
                    
                    if opp_val == self:
                        setattr(item, "vcml_VariantTableArgument", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vcml_VariantTableArgument"):
                    opp_val = getattr(item, "vcml_VariantTableArgument", None)
                    
                    setattr(item, "vcml_VariantTableArgument", self)
                    

    @property
    def vcml_VariantTable126(self):
        return self.__vcml_VariantTable126

    @vcml_VariantTable126.setter
    def vcml_VariantTable126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_VariantTable__vcml_VariantTable126", None)
        self.__vcml_VariantTable126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_VariantTableContent"):
                opp_val = getattr(old_value, "vcml_VariantTableContent", None)
                if opp_val == self:
                    setattr(old_value, "vcml_VariantTableContent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_VariantTableContent"):
                opp_val = getattr(value, "vcml_VariantTableContent", None)
                setattr(value, "vcml_VariantTableContent", self)

    @property
    def vcml_VariantTable200(self):
        return self.__vcml_VariantTable200

    @vcml_VariantTable200.setter
    def vcml_VariantTable200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_VariantTable__vcml_VariantTable200", None)
        self.__vcml_VariantTable200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_Table"):
                opp_val = getattr(old_value, "vcml_Table", None)
                if opp_val == self:
                    setattr(old_value, "vcml_Table", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_Table"):
                opp_val = getattr(value, "vcml_Table", None)
                setattr(value, "vcml_Table", self)

class vcml_InterfaceDesign(VCObject):

    pass
class vcml_ConfigurationProfile(VCObject):

    def __init__(self, fixing: str, status: str, bomapplication: str, vcml_ConfigurationProfile59: set["vcml_DependencyNet"] = None, vcml_ConfigurationProfile61: set["vcml_ConfigurationProfileEntry"] = None, configurationprofiles: "vcml_Material" = None, vcml_ConfigurationProfile: "vcml_InterfaceDesign" = None, ConfigurationProfile: "vcml_Material" = None):
        self.fixing = fixing
        self.status = status
        self.bomapplication = bomapplication
        self.vcml_ConfigurationProfile59 = vcml_ConfigurationProfile59 if vcml_ConfigurationProfile59 is not None else set()
        self.vcml_ConfigurationProfile61 = vcml_ConfigurationProfile61 if vcml_ConfigurationProfile61 is not None else set()
        self.configurationprofiles = configurationprofiles
        self.vcml_ConfigurationProfile = vcml_ConfigurationProfile
        self.ConfigurationProfile = ConfigurationProfile
        
    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def bomapplication(self) -> str:
        return self.__bomapplication

    @bomapplication.setter
    def bomapplication(self, bomapplication: str):
        self.__bomapplication = bomapplication

    @property
    def fixing(self) -> str:
        return self.__fixing

    @fixing.setter
    def fixing(self, fixing: str):
        self.__fixing = fixing

    @property
    def vcml_ConfigurationProfile(self):
        return self.__vcml_ConfigurationProfile

    @vcml_ConfigurationProfile.setter
    def vcml_ConfigurationProfile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_ConfigurationProfile__vcml_ConfigurationProfile", None)
        self.__vcml_ConfigurationProfile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_InterfaceDesign"):
                opp_val = getattr(old_value, "vcml_InterfaceDesign", None)
                if opp_val == self:
                    setattr(old_value, "vcml_InterfaceDesign", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_InterfaceDesign"):
                opp_val = getattr(value, "vcml_InterfaceDesign", None)
                setattr(value, "vcml_InterfaceDesign", self)

    @property
    def vcml_ConfigurationProfile61(self):
        return self.__vcml_ConfigurationProfile61

    @vcml_ConfigurationProfile61.setter
    def vcml_ConfigurationProfile61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_ConfigurationProfile__vcml_ConfigurationProfile61", None)
        self.__vcml_ConfigurationProfile61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vcml_ConfigurationProfileEntry62"):
                    opp_val = getattr(item, "vcml_ConfigurationProfileEntry62", None)
                    
                    if opp_val == self:
                        setattr(item, "vcml_ConfigurationProfileEntry62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vcml_ConfigurationProfileEntry62"):
                    opp_val = getattr(item, "vcml_ConfigurationProfileEntry62", None)
                    
                    setattr(item, "vcml_ConfigurationProfileEntry62", self)
                    

    @property
    def configurationprofiles(self):
        return self.__configurationprofiles

    @configurationprofiles.setter
    def configurationprofiles(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_ConfigurationProfile__configurationprofiles", None)
        self.__configurationprofiles = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Material64"):
                opp_val = getattr(old_value, "Material64", None)
                if opp_val == self:
                    setattr(old_value, "Material64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Material64"):
                opp_val = getattr(value, "Material64", None)
                setattr(value, "Material64", self)

    @property
    def vcml_ConfigurationProfile59(self):
        return self.__vcml_ConfigurationProfile59

    @vcml_ConfigurationProfile59.setter
    def vcml_ConfigurationProfile59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_ConfigurationProfile__vcml_ConfigurationProfile59", None)
        self.__vcml_ConfigurationProfile59 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vcml_DependencyNet"):
                    opp_val = getattr(item, "vcml_DependencyNet", None)
                    
                    if opp_val == self:
                        setattr(item, "vcml_DependencyNet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vcml_DependencyNet"):
                    opp_val = getattr(item, "vcml_DependencyNet", None)
                    
                    setattr(item, "vcml_DependencyNet", self)
                    

    @property
    def ConfigurationProfile(self):
        return self.__ConfigurationProfile

    @ConfigurationProfile.setter
    def ConfigurationProfile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_ConfigurationProfile__ConfigurationProfile", None)
        self.__ConfigurationProfile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "material106"):
                opp_val = getattr(old_value, "material106", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "material106"):
                opp_val = getattr(value, "material106", None)
                if opp_val is None:
                    setattr(value, "material106", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class vcml_Constraint(VCObject, Dependency):

    def __init__(self, status: str, group: str, vcml_Constraint87: "vcml_Documentation" = None, vcml_Constraint90: "vcml_ConstraintSource" = None, vcml_Constraint: "vcml_DependencyNet" = None):
        self.status = status
        self.group = group
        self.vcml_Constraint87 = vcml_Constraint87
        self.vcml_Constraint90 = vcml_Constraint90
        self.vcml_Constraint = vcml_Constraint
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def vcml_Constraint90(self):
        return self.__vcml_Constraint90

    @vcml_Constraint90.setter
    def vcml_Constraint90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Constraint__vcml_Constraint90", None)
        self.__vcml_Constraint90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_ConstraintSource"):
                opp_val = getattr(old_value, "vcml_ConstraintSource", None)
                if opp_val == self:
                    setattr(old_value, "vcml_ConstraintSource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_ConstraintSource"):
                opp_val = getattr(value, "vcml_ConstraintSource", None)
                setattr(value, "vcml_ConstraintSource", self)

    @property
    def vcml_Constraint(self):
        return self.__vcml_Constraint

    @vcml_Constraint.setter
    def vcml_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Constraint__vcml_Constraint", None)
        self.__vcml_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_DependencyNet85"):
                opp_val = getattr(old_value, "vcml_DependencyNet85", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_DependencyNet85"):
                opp_val = getattr(value, "vcml_DependencyNet85", None)
                if opp_val is None:
                    setattr(value, "vcml_DependencyNet85", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vcml_Constraint87(self):
        return self.__vcml_Constraint87

    @vcml_Constraint87.setter
    def vcml_Constraint87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Constraint__vcml_Constraint87", None)
        self.__vcml_Constraint87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_Documentation88"):
                opp_val = getattr(old_value, "vcml_Documentation88", None)
                if opp_val == self:
                    setattr(old_value, "vcml_Documentation88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_Documentation88"):
                opp_val = getattr(value, "vcml_Documentation88", None)
                setattr(value, "vcml_Documentation88", self)

class vcml_Procedure(VCObject, Dependency):

    def __init__(self, status: str, group: str, vcml_Procedure: "vcml_Documentation" = None, vcml_Procedure68: "vcml_ProcedureSource" = None, vcml_Procedure93: "vcml_ConfigurationProfileEntry" = None):
        self.status = status
        self.group = group
        self.vcml_Procedure = vcml_Procedure
        self.vcml_Procedure68 = vcml_Procedure68
        self.vcml_Procedure93 = vcml_Procedure93
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def vcml_Procedure93(self):
        return self.__vcml_Procedure93

    @vcml_Procedure93.setter
    def vcml_Procedure93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Procedure__vcml_Procedure93", None)
        self.__vcml_Procedure93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_ConfigurationProfileEntry92"):
                opp_val = getattr(old_value, "vcml_ConfigurationProfileEntry92", None)
                if opp_val == self:
                    setattr(old_value, "vcml_ConfigurationProfileEntry92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_ConfigurationProfileEntry92"):
                opp_val = getattr(value, "vcml_ConfigurationProfileEntry92", None)
                setattr(value, "vcml_ConfigurationProfileEntry92", self)

    @property
    def vcml_Procedure68(self):
        return self.__vcml_Procedure68

    @vcml_Procedure68.setter
    def vcml_Procedure68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Procedure__vcml_Procedure68", None)
        self.__vcml_Procedure68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_ProcedureSource"):
                opp_val = getattr(old_value, "vcml_ProcedureSource", None)
                if opp_val == self:
                    setattr(old_value, "vcml_ProcedureSource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_ProcedureSource"):
                opp_val = getattr(value, "vcml_ProcedureSource", None)
                setattr(value, "vcml_ProcedureSource", self)

    @property
    def vcml_Procedure(self):
        return self.__vcml_Procedure

    @vcml_Procedure.setter
    def vcml_Procedure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Procedure__vcml_Procedure", None)
        self.__vcml_Procedure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_Documentation66"):
                opp_val = getattr(old_value, "vcml_Documentation66", None)
                if opp_val == self:
                    setattr(old_value, "vcml_Documentation66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_Documentation66"):
                opp_val = getattr(value, "vcml_Documentation66", None)
                setattr(value, "vcml_Documentation66", self)

class vcml_Precondition(VCObject, Dependency):

    def __init__(self, status: str, group: str, vcml_Precondition: "vcml_Documentation" = None, vcml_Precondition77: "vcml_ConditionSource" = None):
        self.status = status
        self.group = group
        self.vcml_Precondition = vcml_Precondition
        self.vcml_Precondition77 = vcml_Precondition77
        
    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def vcml_Precondition(self):
        return self.__vcml_Precondition

    @vcml_Precondition.setter
    def vcml_Precondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Precondition__vcml_Precondition", None)
        self.__vcml_Precondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_Documentation75"):
                opp_val = getattr(old_value, "vcml_Documentation75", None)
                if opp_val == self:
                    setattr(old_value, "vcml_Documentation75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_Documentation75"):
                opp_val = getattr(value, "vcml_Documentation75", None)
                setattr(value, "vcml_Documentation75", self)

    @property
    def vcml_Precondition77(self):
        return self.__vcml_Precondition77

    @vcml_Precondition77.setter
    def vcml_Precondition77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Precondition__vcml_Precondition77", None)
        self.__vcml_Precondition77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_ConditionSource78"):
                opp_val = getattr(old_value, "vcml_ConditionSource78", None)
                if opp_val == self:
                    setattr(old_value, "vcml_ConditionSource78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_ConditionSource78"):
                opp_val = getattr(value, "vcml_ConditionSource78", None)
                setattr(value, "vcml_ConditionSource78", self)

class vcml_DependencyNet(VCObject):

    def __init__(self, status: str, group: str, vcml_DependencyNet: "vcml_ConfigurationProfile" = None, vcml_DependencyNet82: "vcml_Documentation" = None, vcml_DependencyNet85: set["vcml_Constraint"] = None):
        self.status = status
        self.group = group
        self.vcml_DependencyNet = vcml_DependencyNet
        self.vcml_DependencyNet82 = vcml_DependencyNet82
        self.vcml_DependencyNet85 = vcml_DependencyNet85 if vcml_DependencyNet85 is not None else set()
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def vcml_DependencyNet85(self):
        return self.__vcml_DependencyNet85

    @vcml_DependencyNet85.setter
    def vcml_DependencyNet85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_DependencyNet__vcml_DependencyNet85", None)
        self.__vcml_DependencyNet85 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vcml_Constraint"):
                    opp_val = getattr(item, "vcml_Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "vcml_Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vcml_Constraint"):
                    opp_val = getattr(item, "vcml_Constraint", None)
                    
                    setattr(item, "vcml_Constraint", self)
                    

    @property
    def vcml_DependencyNet(self):
        return self.__vcml_DependencyNet

    @vcml_DependencyNet.setter
    def vcml_DependencyNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_DependencyNet__vcml_DependencyNet", None)
        self.__vcml_DependencyNet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_ConfigurationProfile59"):
                opp_val = getattr(old_value, "vcml_ConfigurationProfile59", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_ConfigurationProfile59"):
                opp_val = getattr(value, "vcml_ConfigurationProfile59", None)
                if opp_val is None:
                    setattr(value, "vcml_ConfigurationProfile59", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vcml_DependencyNet82(self):
        return self.__vcml_DependencyNet82

    @vcml_DependencyNet82.setter
    def vcml_DependencyNet82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_DependencyNet__vcml_DependencyNet82", None)
        self.__vcml_DependencyNet82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_Documentation83"):
                opp_val = getattr(old_value, "vcml_Documentation83", None)
                if opp_val == self:
                    setattr(old_value, "vcml_Documentation83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_Documentation83"):
                opp_val = getattr(value, "vcml_Documentation83", None)
                setattr(value, "vcml_Documentation83", self)

class vcml_VariantFunction(VCObject):

    def __init__(self, status: str, group: str, vcml_VariantFunction: set["vcml_VariantFunctionArgument"] = None, vcml_VariantFunction184: "vcml_Function" = None, vcml_VariantFunction192: "vcml_PFunction" = None):
        self.status = status
        self.group = group
        self.vcml_VariantFunction = vcml_VariantFunction if vcml_VariantFunction is not None else set()
        self.vcml_VariantFunction184 = vcml_VariantFunction184
        self.vcml_VariantFunction192 = vcml_VariantFunction192
        
    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def vcml_VariantFunction(self):
        return self.__vcml_VariantFunction

    @vcml_VariantFunction.setter
    def vcml_VariantFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_VariantFunction__vcml_VariantFunction", None)
        self.__vcml_VariantFunction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vcml_VariantFunctionArgument"):
                    opp_val = getattr(item, "vcml_VariantFunctionArgument", None)
                    
                    if opp_val == self:
                        setattr(item, "vcml_VariantFunctionArgument", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vcml_VariantFunctionArgument"):
                    opp_val = getattr(item, "vcml_VariantFunctionArgument", None)
                    
                    setattr(item, "vcml_VariantFunctionArgument", self)
                    

    @property
    def vcml_VariantFunction192(self):
        return self.__vcml_VariantFunction192

    @vcml_VariantFunction192.setter
    def vcml_VariantFunction192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_VariantFunction__vcml_VariantFunction192", None)
        self.__vcml_VariantFunction192 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_PFunction"):
                opp_val = getattr(old_value, "vcml_PFunction", None)
                if opp_val == self:
                    setattr(old_value, "vcml_PFunction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_PFunction"):
                opp_val = getattr(value, "vcml_PFunction", None)
                setattr(value, "vcml_PFunction", self)

    @property
    def vcml_VariantFunction184(self):
        return self.__vcml_VariantFunction184

    @vcml_VariantFunction184.setter
    def vcml_VariantFunction184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_VariantFunction__vcml_VariantFunction184", None)
        self.__vcml_VariantFunction184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_Function"):
                opp_val = getattr(old_value, "vcml_Function", None)
                if opp_val == self:
                    setattr(old_value, "vcml_Function", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_Function"):
                opp_val = getattr(value, "vcml_Function", None)
                setattr(value, "vcml_Function", self)

class vcml_BillOfMaterial(VCObject):

    pass
class vcml_Description:

    pass
class CharacteristicType:

    pass
class vcml_DateType(CharacteristicType):

    def __init__(self, intervalValuesAllowed: bool, vcml_DateType: set["vcml_DateCharacteristicValue"] = None):
        self.intervalValuesAllowed = intervalValuesAllowed
        self.vcml_DateType = vcml_DateType if vcml_DateType is not None else set()
        
    @property
    def intervalValuesAllowed(self) -> bool:
        return self.__intervalValuesAllowed

    @intervalValuesAllowed.setter
    def intervalValuesAllowed(self, intervalValuesAllowed: bool):
        self.__intervalValuesAllowed = intervalValuesAllowed

    @property
    def vcml_DateType(self):
        return self.__vcml_DateType

    @vcml_DateType.setter
    def vcml_DateType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_DateType__vcml_DateType", None)
        self.__vcml_DateType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vcml_DateCharacteristicValue"):
                    opp_val = getattr(item, "vcml_DateCharacteristicValue", None)
                    
                    if opp_val == self:
                        setattr(item, "vcml_DateCharacteristicValue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vcml_DateCharacteristicValue"):
                    opp_val = getattr(item, "vcml_DateCharacteristicValue", None)
                    
                    setattr(item, "vcml_DateCharacteristicValue", self)
                    

class vcml_SymbolicType(CharacteristicType):

    def __init__(self, caseSensitive: bool, vcml_SymbolicType: set["vcml_CharacteristicValue"] = None):
        self.caseSensitive = caseSensitive
        self.vcml_SymbolicType = vcml_SymbolicType if vcml_SymbolicType is not None else set()
        
    @property
    def caseSensitive(self) -> bool:
        return self.__caseSensitive

    @caseSensitive.setter
    def caseSensitive(self, caseSensitive: bool):
        self.__caseSensitive = caseSensitive

    @property
    def vcml_SymbolicType(self):
        return self.__vcml_SymbolicType

    @vcml_SymbolicType.setter
    def vcml_SymbolicType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_SymbolicType__vcml_SymbolicType", None)
        self.__vcml_SymbolicType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vcml_CharacteristicValue"):
                    opp_val = getattr(item, "vcml_CharacteristicValue", None)
                    
                    if opp_val == self:
                        setattr(item, "vcml_CharacteristicValue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vcml_CharacteristicValue"):
                    opp_val = getattr(item, "vcml_CharacteristicValue", None)
                    
                    setattr(item, "vcml_CharacteristicValue", self)
                    

class vcml_NumericType(CharacteristicType):

    def __init__(self, decimalPlaces: int, unit: str, negativeValuesAllowed: bool, intervalValuesAllowed: bool, vcml_NumericType: set["vcml_NumericCharacteristicValue"] = None):
        self.decimalPlaces = decimalPlaces
        self.unit = unit
        self.negativeValuesAllowed = negativeValuesAllowed
        self.intervalValuesAllowed = intervalValuesAllowed
        self.vcml_NumericType = vcml_NumericType if vcml_NumericType is not None else set()
        
    @property
    def intervalValuesAllowed(self) -> bool:
        return self.__intervalValuesAllowed

    @intervalValuesAllowed.setter
    def intervalValuesAllowed(self, intervalValuesAllowed: bool):
        self.__intervalValuesAllowed = intervalValuesAllowed

    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

    @property
    def decimalPlaces(self) -> int:
        return self.__decimalPlaces

    @decimalPlaces.setter
    def decimalPlaces(self, decimalPlaces: int):
        self.__decimalPlaces = decimalPlaces

    @property
    def negativeValuesAllowed(self) -> bool:
        return self.__negativeValuesAllowed

    @negativeValuesAllowed.setter
    def negativeValuesAllowed(self, negativeValuesAllowed: bool):
        self.__negativeValuesAllowed = negativeValuesAllowed

    @property
    def vcml_NumericType(self):
        return self.__vcml_NumericType

    @vcml_NumericType.setter
    def vcml_NumericType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_NumericType__vcml_NumericType", None)
        self.__vcml_NumericType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vcml_NumericCharacteristicValue"):
                    opp_val = getattr(item, "vcml_NumericCharacteristicValue", None)
                    
                    if opp_val == self:
                        setattr(item, "vcml_NumericCharacteristicValue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vcml_NumericCharacteristicValue"):
                    opp_val = getattr(item, "vcml_NumericCharacteristicValue", None)
                    
                    setattr(item, "vcml_NumericCharacteristicValue", self)
                    

class vcml_CharacteristicOrValueDependencies:

    pass
class vcml_CharacteristicType:

    def __init__(self, numberOfChars: int, vcml_CharacteristicType: "vcml_Characteristic" = None):
        self.numberOfChars = numberOfChars
        self.vcml_CharacteristicType = vcml_CharacteristicType
        
    @property
    def numberOfChars(self) -> int:
        return self.__numberOfChars

    @numberOfChars.setter
    def numberOfChars(self, numberOfChars: int):
        self.__numberOfChars = numberOfChars

    @property
    def vcml_CharacteristicType(self):
        return self.__vcml_CharacteristicType

    @vcml_CharacteristicType.setter
    def vcml_CharacteristicType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_CharacteristicType__vcml_CharacteristicType", None)
        self.__vcml_CharacteristicType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_Characteristic20"):
                opp_val = getattr(old_value, "vcml_Characteristic20", None)
                if opp_val == self:
                    setattr(old_value, "vcml_Characteristic20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_Characteristic20"):
                opp_val = getattr(value, "vcml_Characteristic20", None)
                setattr(value, "vcml_Characteristic20", self)

class vcml_Documentation:

    pass
class vcml_Characteristic(VCObject):

    def __init__(self, status: str, group: str, additionalValues: bool, required: bool, restrictable: bool, noDisplay: bool, notReadyForInput: bool, multiValue: bool, displayAllowedValues: bool, table: str, field: str, vcml_Characteristic: "vcml_Documentation" = None, vcml_Characteristic20: "vcml_CharacteristicType" = None, vcml_Characteristic22: "vcml_CharacteristicOrValueDependencies" = None, vcml_Characteristic53: "vcml_Class" = None, vcml_Characteristic101: "vcml_CharacteristicGroup" = None, vcml_Characteristic114: "vcml_ValueAssignment" = None, vcml_Characteristic120: "vcml_VariantFunctionArgument" = None, vcml_Characteristic124: "vcml_VariantTableArgument" = None, vcml_Characteristic157: "vcml_ShortVarDefinition" = None, vcml_Characteristic173: "vcml_ObjectCharacteristicReference" = None, vcml_Characteristic187: "vcml_Function" = None, vcml_Characteristic180: "vcml_Assignment" = None, vcml_Characteristic203: "vcml_Table" = None, vcml_Characteristic195: "vcml_PFunction" = None, vcml_Characteristic215: "vcml_SetPricingFactor" = None, vcml_Characteristic223: "vcml_CharacteristicReference_P" = None, vcml_Characteristic208: "vcml_SetOrDelDefault" = None, vcml_Characteristic213: "vcml_IsInvisible" = None, vcml_Characteristic229: "vcml_SumParts" = None):
        self.status = status
        self.group = group
        self.additionalValues = additionalValues
        self.required = required
        self.restrictable = restrictable
        self.noDisplay = noDisplay
        self.notReadyForInput = notReadyForInput
        self.multiValue = multiValue
        self.displayAllowedValues = displayAllowedValues
        self.table = table
        self.field = field
        self.vcml_Characteristic = vcml_Characteristic
        self.vcml_Characteristic20 = vcml_Characteristic20
        self.vcml_Characteristic22 = vcml_Characteristic22
        self.vcml_Characteristic53 = vcml_Characteristic53
        self.vcml_Characteristic101 = vcml_Characteristic101
        self.vcml_Characteristic114 = vcml_Characteristic114
        self.vcml_Characteristic120 = vcml_Characteristic120
        self.vcml_Characteristic124 = vcml_Characteristic124
        self.vcml_Characteristic157 = vcml_Characteristic157
        self.vcml_Characteristic173 = vcml_Characteristic173
        self.vcml_Characteristic187 = vcml_Characteristic187
        self.vcml_Characteristic180 = vcml_Characteristic180
        self.vcml_Characteristic203 = vcml_Characteristic203
        self.vcml_Characteristic195 = vcml_Characteristic195
        self.vcml_Characteristic215 = vcml_Characteristic215
        self.vcml_Characteristic223 = vcml_Characteristic223
        self.vcml_Characteristic208 = vcml_Characteristic208
        self.vcml_Characteristic213 = vcml_Characteristic213
        self.vcml_Characteristic229 = vcml_Characteristic229
        
    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def required(self) -> bool:
        return self.__required

    @required.setter
    def required(self, required: bool):
        self.__required = required

    @property
    def additionalValues(self) -> bool:
        return self.__additionalValues

    @additionalValues.setter
    def additionalValues(self, additionalValues: bool):
        self.__additionalValues = additionalValues

    @property
    def field(self) -> str:
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field

    @property
    def restrictable(self) -> bool:
        return self.__restrictable

    @restrictable.setter
    def restrictable(self, restrictable: bool):
        self.__restrictable = restrictable

    @property
    def displayAllowedValues(self) -> bool:
        return self.__displayAllowedValues

    @displayAllowedValues.setter
    def displayAllowedValues(self, displayAllowedValues: bool):
        self.__displayAllowedValues = displayAllowedValues

    @property
    def table(self) -> str:
        return self.__table

    @table.setter
    def table(self, table: str):
        self.__table = table

    @property
    def multiValue(self) -> bool:
        return self.__multiValue

    @multiValue.setter
    def multiValue(self, multiValue: bool):
        self.__multiValue = multiValue

    @property
    def notReadyForInput(self) -> bool:
        return self.__notReadyForInput

    @notReadyForInput.setter
    def notReadyForInput(self, notReadyForInput: bool):
        self.__notReadyForInput = notReadyForInput

    @property
    def noDisplay(self) -> bool:
        return self.__noDisplay

    @noDisplay.setter
    def noDisplay(self, noDisplay: bool):
        self.__noDisplay = noDisplay

    @property
    def vcml_Characteristic157(self):
        return self.__vcml_Characteristic157

    @vcml_Characteristic157.setter
    def vcml_Characteristic157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Characteristic__vcml_Characteristic157", None)
        self.__vcml_Characteristic157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_ShortVarDefinition156"):
                opp_val = getattr(old_value, "vcml_ShortVarDefinition156", None)
                if opp_val == self:
                    setattr(old_value, "vcml_ShortVarDefinition156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_ShortVarDefinition156"):
                opp_val = getattr(value, "vcml_ShortVarDefinition156", None)
                setattr(value, "vcml_ShortVarDefinition156", self)

    @property
    def vcml_Characteristic124(self):
        return self.__vcml_Characteristic124

    @vcml_Characteristic124.setter
    def vcml_Characteristic124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Characteristic__vcml_Characteristic124", None)
        self.__vcml_Characteristic124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_VariantTableArgument123"):
                opp_val = getattr(old_value, "vcml_VariantTableArgument123", None)
                if opp_val == self:
                    setattr(old_value, "vcml_VariantTableArgument123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_VariantTableArgument123"):
                opp_val = getattr(value, "vcml_VariantTableArgument123", None)
                setattr(value, "vcml_VariantTableArgument123", self)

    @property
    def vcml_Characteristic180(self):
        return self.__vcml_Characteristic180

    @vcml_Characteristic180.setter
    def vcml_Characteristic180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Characteristic__vcml_Characteristic180", None)
        self.__vcml_Characteristic180 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_Assignment"):
                opp_val = getattr(old_value, "vcml_Assignment", None)
                if opp_val == self:
                    setattr(old_value, "vcml_Assignment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_Assignment"):
                opp_val = getattr(value, "vcml_Assignment", None)
                setattr(value, "vcml_Assignment", self)

    @property
    def vcml_Characteristic203(self):
        return self.__vcml_Characteristic203

    @vcml_Characteristic203.setter
    def vcml_Characteristic203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Characteristic__vcml_Characteristic203", None)
        self.__vcml_Characteristic203 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_Table202"):
                opp_val = getattr(old_value, "vcml_Table202", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_Table202"):
                opp_val = getattr(value, "vcml_Table202", None)
                if opp_val is None:
                    setattr(value, "vcml_Table202", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vcml_Characteristic22(self):
        return self.__vcml_Characteristic22

    @vcml_Characteristic22.setter
    def vcml_Characteristic22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Characteristic__vcml_Characteristic22", None)
        self.__vcml_Characteristic22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_CharacteristicOrValueDependencies"):
                opp_val = getattr(old_value, "vcml_CharacteristicOrValueDependencies", None)
                if opp_val == self:
                    setattr(old_value, "vcml_CharacteristicOrValueDependencies", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_CharacteristicOrValueDependencies"):
                opp_val = getattr(value, "vcml_CharacteristicOrValueDependencies", None)
                setattr(value, "vcml_CharacteristicOrValueDependencies", self)

    @property
    def vcml_Characteristic120(self):
        return self.__vcml_Characteristic120

    @vcml_Characteristic120.setter
    def vcml_Characteristic120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Characteristic__vcml_Characteristic120", None)
        self.__vcml_Characteristic120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_VariantFunctionArgument119"):
                opp_val = getattr(old_value, "vcml_VariantFunctionArgument119", None)
                if opp_val == self:
                    setattr(old_value, "vcml_VariantFunctionArgument119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_VariantFunctionArgument119"):
                opp_val = getattr(value, "vcml_VariantFunctionArgument119", None)
                setattr(value, "vcml_VariantFunctionArgument119", self)

    @property
    def vcml_Characteristic223(self):
        return self.__vcml_Characteristic223

    @vcml_Characteristic223.setter
    def vcml_Characteristic223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Characteristic__vcml_Characteristic223", None)
        self.__vcml_Characteristic223 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_CharacteristicReference_P"):
                opp_val = getattr(old_value, "vcml_CharacteristicReference_P", None)
                if opp_val == self:
                    setattr(old_value, "vcml_CharacteristicReference_P", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_CharacteristicReference_P"):
                opp_val = getattr(value, "vcml_CharacteristicReference_P", None)
                setattr(value, "vcml_CharacteristicReference_P", self)

    @property
    def vcml_Characteristic187(self):
        return self.__vcml_Characteristic187

    @vcml_Characteristic187.setter
    def vcml_Characteristic187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Characteristic__vcml_Characteristic187", None)
        self.__vcml_Characteristic187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_Function186"):
                opp_val = getattr(old_value, "vcml_Function186", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_Function186"):
                opp_val = getattr(value, "vcml_Function186", None)
                if opp_val is None:
                    setattr(value, "vcml_Function186", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vcml_Characteristic195(self):
        return self.__vcml_Characteristic195

    @vcml_Characteristic195.setter
    def vcml_Characteristic195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Characteristic__vcml_Characteristic195", None)
        self.__vcml_Characteristic195 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_PFunction194"):
                opp_val = getattr(old_value, "vcml_PFunction194", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_PFunction194"):
                opp_val = getattr(value, "vcml_PFunction194", None)
                if opp_val is None:
                    setattr(value, "vcml_PFunction194", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vcml_Characteristic208(self):
        return self.__vcml_Characteristic208

    @vcml_Characteristic208.setter
    def vcml_Characteristic208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Characteristic__vcml_Characteristic208", None)
        self.__vcml_Characteristic208 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_SetOrDelDefault"):
                opp_val = getattr(old_value, "vcml_SetOrDelDefault", None)
                if opp_val == self:
                    setattr(old_value, "vcml_SetOrDelDefault", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_SetOrDelDefault"):
                opp_val = getattr(value, "vcml_SetOrDelDefault", None)
                setattr(value, "vcml_SetOrDelDefault", self)

    @property
    def vcml_Characteristic20(self):
        return self.__vcml_Characteristic20

    @vcml_Characteristic20.setter
    def vcml_Characteristic20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Characteristic__vcml_Characteristic20", None)
        self.__vcml_Characteristic20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_CharacteristicType"):
                opp_val = getattr(old_value, "vcml_CharacteristicType", None)
                if opp_val == self:
                    setattr(old_value, "vcml_CharacteristicType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_CharacteristicType"):
                opp_val = getattr(value, "vcml_CharacteristicType", None)
                setattr(value, "vcml_CharacteristicType", self)

    @property
    def vcml_Characteristic173(self):
        return self.__vcml_Characteristic173

    @vcml_Characteristic173.setter
    def vcml_Characteristic173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Characteristic__vcml_Characteristic173", None)
        self.__vcml_Characteristic173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_ObjectCharacteristicReference172"):
                opp_val = getattr(old_value, "vcml_ObjectCharacteristicReference172", None)
                if opp_val == self:
                    setattr(old_value, "vcml_ObjectCharacteristicReference172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_ObjectCharacteristicReference172"):
                opp_val = getattr(value, "vcml_ObjectCharacteristicReference172", None)
                setattr(value, "vcml_ObjectCharacteristicReference172", self)

    @property
    def vcml_Characteristic229(self):
        return self.__vcml_Characteristic229

    @vcml_Characteristic229.setter
    def vcml_Characteristic229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Characteristic__vcml_Characteristic229", None)
        self.__vcml_Characteristic229 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_SumParts"):
                opp_val = getattr(old_value, "vcml_SumParts", None)
                if opp_val == self:
                    setattr(old_value, "vcml_SumParts", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_SumParts"):
                opp_val = getattr(value, "vcml_SumParts", None)
                setattr(value, "vcml_SumParts", self)

    @property
    def vcml_Characteristic215(self):
        return self.__vcml_Characteristic215

    @vcml_Characteristic215.setter
    def vcml_Characteristic215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Characteristic__vcml_Characteristic215", None)
        self.__vcml_Characteristic215 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_SetPricingFactor"):
                opp_val = getattr(old_value, "vcml_SetPricingFactor", None)
                if opp_val == self:
                    setattr(old_value, "vcml_SetPricingFactor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_SetPricingFactor"):
                opp_val = getattr(value, "vcml_SetPricingFactor", None)
                setattr(value, "vcml_SetPricingFactor", self)

    @property
    def vcml_Characteristic114(self):
        return self.__vcml_Characteristic114

    @vcml_Characteristic114.setter
    def vcml_Characteristic114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Characteristic__vcml_Characteristic114", None)
        self.__vcml_Characteristic114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_ValueAssignment113"):
                opp_val = getattr(old_value, "vcml_ValueAssignment113", None)
                if opp_val == self:
                    setattr(old_value, "vcml_ValueAssignment113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_ValueAssignment113"):
                opp_val = getattr(value, "vcml_ValueAssignment113", None)
                setattr(value, "vcml_ValueAssignment113", self)

    @property
    def vcml_Characteristic213(self):
        return self.__vcml_Characteristic213

    @vcml_Characteristic213.setter
    def vcml_Characteristic213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Characteristic__vcml_Characteristic213", None)
        self.__vcml_Characteristic213 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_IsInvisible"):
                opp_val = getattr(old_value, "vcml_IsInvisible", None)
                if opp_val == self:
                    setattr(old_value, "vcml_IsInvisible", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_IsInvisible"):
                opp_val = getattr(value, "vcml_IsInvisible", None)
                setattr(value, "vcml_IsInvisible", self)

    @property
    def vcml_Characteristic(self):
        return self.__vcml_Characteristic

    @vcml_Characteristic.setter
    def vcml_Characteristic(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Characteristic__vcml_Characteristic", None)
        self.__vcml_Characteristic = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_Documentation"):
                opp_val = getattr(old_value, "vcml_Documentation", None)
                if opp_val == self:
                    setattr(old_value, "vcml_Documentation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_Documentation"):
                opp_val = getattr(value, "vcml_Documentation", None)
                setattr(value, "vcml_Documentation", self)

    @property
    def vcml_Characteristic53(self):
        return self.__vcml_Characteristic53

    @vcml_Characteristic53.setter
    def vcml_Characteristic53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Characteristic__vcml_Characteristic53", None)
        self.__vcml_Characteristic53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_Class52"):
                opp_val = getattr(old_value, "vcml_Class52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_Class52"):
                opp_val = getattr(value, "vcml_Class52", None)
                if opp_val is None:
                    setattr(value, "vcml_Class52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vcml_Characteristic101(self):
        return self.__vcml_Characteristic101

    @vcml_Characteristic101.setter
    def vcml_Characteristic101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Characteristic__vcml_Characteristic101", None)
        self.__vcml_Characteristic101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_CharacteristicGroup100"):
                opp_val = getattr(old_value, "vcml_CharacteristicGroup100", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_CharacteristicGroup100"):
                opp_val = getattr(value, "vcml_CharacteristicGroup100", None)
                if opp_val is None:
                    setattr(value, "vcml_CharacteristicGroup100", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class vcml_Class(VCObject):

    def __init__(self, status: str, group: str, vcml_Class: "vcml_BOMItem_Class" = None, vcml_Class52: set["vcml_Characteristic"] = None, vcml_Class56: "vcml_Class" = None, vcml_Class54: set["vcml_Class"] = None, vcml_Class109: "vcml_Classification" = None, vcml_Class148: "vcml_ConstraintClass" = None):
        self.status = status
        self.group = group
        self.vcml_Class = vcml_Class
        self.vcml_Class52 = vcml_Class52 if vcml_Class52 is not None else set()
        self.vcml_Class56 = vcml_Class56
        self.vcml_Class54 = vcml_Class54 if vcml_Class54 is not None else set()
        self.vcml_Class109 = vcml_Class109
        self.vcml_Class148 = vcml_Class148
        
    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def vcml_Class(self):
        return self.__vcml_Class

    @vcml_Class.setter
    def vcml_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Class__vcml_Class", None)
        self.__vcml_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_BOMItem_Class"):
                opp_val = getattr(old_value, "vcml_BOMItem_Class", None)
                if opp_val == self:
                    setattr(old_value, "vcml_BOMItem_Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_BOMItem_Class"):
                opp_val = getattr(value, "vcml_BOMItem_Class", None)
                setattr(value, "vcml_BOMItem_Class", self)

    @property
    def vcml_Class148(self):
        return self.__vcml_Class148

    @vcml_Class148.setter
    def vcml_Class148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Class__vcml_Class148", None)
        self.__vcml_Class148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_ConstraintClass"):
                opp_val = getattr(old_value, "vcml_ConstraintClass", None)
                if opp_val == self:
                    setattr(old_value, "vcml_ConstraintClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_ConstraintClass"):
                opp_val = getattr(value, "vcml_ConstraintClass", None)
                setattr(value, "vcml_ConstraintClass", self)

    @property
    def vcml_Class52(self):
        return self.__vcml_Class52

    @vcml_Class52.setter
    def vcml_Class52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Class__vcml_Class52", None)
        self.__vcml_Class52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vcml_Characteristic53"):
                    opp_val = getattr(item, "vcml_Characteristic53", None)
                    
                    if opp_val == self:
                        setattr(item, "vcml_Characteristic53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vcml_Characteristic53"):
                    opp_val = getattr(item, "vcml_Characteristic53", None)
                    
                    setattr(item, "vcml_Characteristic53", self)
                    

    @property
    def vcml_Class109(self):
        return self.__vcml_Class109

    @vcml_Class109.setter
    def vcml_Class109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Class__vcml_Class109", None)
        self.__vcml_Class109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_Classification108"):
                opp_val = getattr(old_value, "vcml_Classification108", None)
                if opp_val == self:
                    setattr(old_value, "vcml_Classification108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_Classification108"):
                opp_val = getattr(value, "vcml_Classification108", None)
                setattr(value, "vcml_Classification108", self)

    @property
    def vcml_Class54(self):
        return self.__vcml_Class54

    @vcml_Class54.setter
    def vcml_Class54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Class__vcml_Class54", None)
        self.__vcml_Class54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vcml_Class56"):
                    opp_val = getattr(item, "vcml_Class56", None)
                    
                    if opp_val == self:
                        setattr(item, "vcml_Class56", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vcml_Class56"):
                    opp_val = getattr(item, "vcml_Class56", None)
                    
                    setattr(item, "vcml_Class56", self)
                    

    @property
    def vcml_Class56(self):
        return self.__vcml_Class56

    @vcml_Class56.setter
    def vcml_Class56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Class__vcml_Class56", None)
        self.__vcml_Class56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_Class54"):
                opp_val = getattr(old_value, "vcml_Class54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_Class54"):
                opp_val = getattr(value, "vcml_Class54", None)
                if opp_val is None:
                    setattr(value, "vcml_Class54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BOMItem:

    pass
class vcml_BOMItem_Class(BOMItem):

    pass
class vcml_BOMItem_Material(BOMItem):

    pass
class vcml_ConfigurationProfileEntry:

    def __init__(self, sequence: int, vcml_ConfigurationProfileEntry: "vcml_BOMItem" = None, vcml_ConfigurationProfileEntry62: "vcml_ConfigurationProfile" = None, vcml_ConfigurationProfileEntry92: "vcml_Procedure" = None):
        self.sequence = sequence
        self.vcml_ConfigurationProfileEntry = vcml_ConfigurationProfileEntry
        self.vcml_ConfigurationProfileEntry62 = vcml_ConfigurationProfileEntry62
        self.vcml_ConfigurationProfileEntry92 = vcml_ConfigurationProfileEntry92
        
    @property
    def sequence(self) -> int:
        return self.__sequence

    @sequence.setter
    def sequence(self, sequence: int):
        self.__sequence = sequence

    @property
    def vcml_ConfigurationProfileEntry62(self):
        return self.__vcml_ConfigurationProfileEntry62

    @vcml_ConfigurationProfileEntry62.setter
    def vcml_ConfigurationProfileEntry62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_ConfigurationProfileEntry__vcml_ConfigurationProfileEntry62", None)
        self.__vcml_ConfigurationProfileEntry62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_ConfigurationProfile61"):
                opp_val = getattr(old_value, "vcml_ConfigurationProfile61", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_ConfigurationProfile61"):
                opp_val = getattr(value, "vcml_ConfigurationProfile61", None)
                if opp_val is None:
                    setattr(value, "vcml_ConfigurationProfile61", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vcml_ConfigurationProfileEntry92(self):
        return self.__vcml_ConfigurationProfileEntry92

    @vcml_ConfigurationProfileEntry92.setter
    def vcml_ConfigurationProfileEntry92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_ConfigurationProfileEntry__vcml_ConfigurationProfileEntry92", None)
        self.__vcml_ConfigurationProfileEntry92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_Procedure93"):
                opp_val = getattr(old_value, "vcml_Procedure93", None)
                if opp_val == self:
                    setattr(old_value, "vcml_Procedure93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_Procedure93"):
                opp_val = getattr(value, "vcml_Procedure93", None)
                setattr(value, "vcml_Procedure93", self)

    @property
    def vcml_ConfigurationProfileEntry(self):
        return self.__vcml_ConfigurationProfileEntry

    @vcml_ConfigurationProfileEntry.setter
    def vcml_ConfigurationProfileEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_ConfigurationProfileEntry__vcml_ConfigurationProfileEntry", None)
        self.__vcml_ConfigurationProfileEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_BOMItem15"):
                opp_val = getattr(old_value, "vcml_BOMItem15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_BOMItem15"):
                opp_val = getattr(value, "vcml_BOMItem15", None)
                if opp_val is None:
                    setattr(value, "vcml_BOMItem15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class vcml_SelectionCondition(VCObject, Dependency):

    def __init__(self, status: str, group: str, vcml_SelectionCondition: "vcml_BOMItem" = None, vcml_SelectionCondition70: "vcml_Documentation" = None, vcml_SelectionCondition73: "vcml_ConditionSource" = None):
        self.status = status
        self.group = group
        self.vcml_SelectionCondition = vcml_SelectionCondition
        self.vcml_SelectionCondition70 = vcml_SelectionCondition70
        self.vcml_SelectionCondition73 = vcml_SelectionCondition73
        
    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def vcml_SelectionCondition(self):
        return self.__vcml_SelectionCondition

    @vcml_SelectionCondition.setter
    def vcml_SelectionCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_SelectionCondition__vcml_SelectionCondition", None)
        self.__vcml_SelectionCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_BOMItem13"):
                opp_val = getattr(old_value, "vcml_BOMItem13", None)
                if opp_val == self:
                    setattr(old_value, "vcml_BOMItem13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_BOMItem13"):
                opp_val = getattr(value, "vcml_BOMItem13", None)
                setattr(value, "vcml_BOMItem13", self)

    @property
    def vcml_SelectionCondition70(self):
        return self.__vcml_SelectionCondition70

    @vcml_SelectionCondition70.setter
    def vcml_SelectionCondition70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_SelectionCondition__vcml_SelectionCondition70", None)
        self.__vcml_SelectionCondition70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_Documentation71"):
                opp_val = getattr(old_value, "vcml_Documentation71", None)
                if opp_val == self:
                    setattr(old_value, "vcml_Documentation71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_Documentation71"):
                opp_val = getattr(value, "vcml_Documentation71", None)
                setattr(value, "vcml_Documentation71", self)

    @property
    def vcml_SelectionCondition73(self):
        return self.__vcml_SelectionCondition73

    @vcml_SelectionCondition73.setter
    def vcml_SelectionCondition73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_SelectionCondition__vcml_SelectionCondition73", None)
        self.__vcml_SelectionCondition73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_ConditionSource"):
                opp_val = getattr(old_value, "vcml_ConditionSource", None)
                if opp_val == self:
                    setattr(old_value, "vcml_ConditionSource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_ConditionSource"):
                opp_val = getattr(value, "vcml_ConditionSource", None)
                setattr(value, "vcml_ConditionSource", self)

class vcml_Material(VCObject):

    def __init__(self, type: str, Material: "vcml_BillOfMaterial" = None, vcml_Material: "vcml_BOMItem_Material" = None, Material64: "vcml_ConfigurationProfile" = None, material: set["vcml_BillOfMaterial"] = None, vcml_Material104: set["vcml_Classification"] = None, material106: set["vcml_ConfigurationProfile"] = None, vcml_Material154: "vcml_PartialKey" = None):
        self.type = type
        self.Material = Material
        self.vcml_Material = vcml_Material
        self.Material64 = Material64
        self.material = material if material is not None else set()
        self.vcml_Material104 = vcml_Material104 if vcml_Material104 is not None else set()
        self.material106 = material106 if material106 is not None else set()
        self.vcml_Material154 = vcml_Material154
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def Material64(self):
        return self.__Material64

    @Material64.setter
    def Material64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Material__Material64", None)
        self.__Material64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "configurationprofiles"):
                opp_val = getattr(old_value, "configurationprofiles", None)
                if opp_val == self:
                    setattr(old_value, "configurationprofiles", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "configurationprofiles"):
                opp_val = getattr(value, "configurationprofiles", None)
                setattr(value, "configurationprofiles", self)

    @property
    def vcml_Material(self):
        return self.__vcml_Material

    @vcml_Material.setter
    def vcml_Material(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Material__vcml_Material", None)
        self.__vcml_Material = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_BOMItem_Material"):
                opp_val = getattr(old_value, "vcml_BOMItem_Material", None)
                if opp_val == self:
                    setattr(old_value, "vcml_BOMItem_Material", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_BOMItem_Material"):
                opp_val = getattr(value, "vcml_BOMItem_Material", None)
                setattr(value, "vcml_BOMItem_Material", self)

    @property
    def vcml_Material154(self):
        return self.__vcml_Material154

    @vcml_Material154.setter
    def vcml_Material154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Material__vcml_Material154", None)
        self.__vcml_Material154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_PartialKey153"):
                opp_val = getattr(old_value, "vcml_PartialKey153", None)
                if opp_val == self:
                    setattr(old_value, "vcml_PartialKey153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_PartialKey153"):
                opp_val = getattr(value, "vcml_PartialKey153", None)
                setattr(value, "vcml_PartialKey153", self)

    @property
    def Material(self):
        return self.__Material

    @Material.setter
    def Material(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Material__Material", None)
        self.__Material = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "billofmaterials"):
                opp_val = getattr(old_value, "billofmaterials", None)
                if opp_val == self:
                    setattr(old_value, "billofmaterials", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "billofmaterials"):
                opp_val = getattr(value, "billofmaterials", None)
                setattr(value, "billofmaterials", self)

    @property
    def vcml_Material104(self):
        return self.__vcml_Material104

    @vcml_Material104.setter
    def vcml_Material104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Material__vcml_Material104", None)
        self.__vcml_Material104 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vcml_Classification"):
                    opp_val = getattr(item, "vcml_Classification", None)
                    
                    if opp_val == self:
                        setattr(item, "vcml_Classification", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vcml_Classification"):
                    opp_val = getattr(item, "vcml_Classification", None)
                    
                    setattr(item, "vcml_Classification", self)
                    

    @property
    def material(self):
        return self.__material

    @material.setter
    def material(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Material__material", None)
        self.__material = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BillOfMaterial"):
                    opp_val = getattr(item, "BillOfMaterial", None)
                    
                    if opp_val == self:
                        setattr(item, "BillOfMaterial", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BillOfMaterial"):
                    opp_val = getattr(item, "BillOfMaterial", None)
                    
                    setattr(item, "BillOfMaterial", self)
                    

    @property
    def material106(self):
        return self.__material106

    @material106.setter
    def material106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Material__material106", None)
        self.__material106 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ConfigurationProfile"):
                    opp_val = getattr(item, "ConfigurationProfile", None)
                    
                    if opp_val == self:
                        setattr(item, "ConfigurationProfile", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ConfigurationProfile"):
                    opp_val = getattr(item, "ConfigurationProfile", None)
                    
                    setattr(item, "ConfigurationProfile", self)
                    

class vcml_BOMItem(ABC):

    def __init__(self, itemnumber: int, vcml_BOMItem: "vcml_BillOfMaterial" = None, vcml_BOMItem13: "vcml_SelectionCondition" = None, vcml_BOMItem15: set["vcml_ConfigurationProfileEntry"] = None):
        self.itemnumber = itemnumber
        self.vcml_BOMItem = vcml_BOMItem
        self.vcml_BOMItem13 = vcml_BOMItem13
        self.vcml_BOMItem15 = vcml_BOMItem15 if vcml_BOMItem15 is not None else set()
        
    @property
    def itemnumber(self) -> int:
        return self.__itemnumber

    @itemnumber.setter
    def itemnumber(self, itemnumber: int):
        self.__itemnumber = itemnumber

    @property
    def vcml_BOMItem13(self):
        return self.__vcml_BOMItem13

    @vcml_BOMItem13.setter
    def vcml_BOMItem13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_BOMItem__vcml_BOMItem13", None)
        self.__vcml_BOMItem13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_SelectionCondition"):
                opp_val = getattr(old_value, "vcml_SelectionCondition", None)
                if opp_val == self:
                    setattr(old_value, "vcml_SelectionCondition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_SelectionCondition"):
                opp_val = getattr(value, "vcml_SelectionCondition", None)
                setattr(value, "vcml_SelectionCondition", self)

    @property
    def vcml_BOMItem(self):
        return self.__vcml_BOMItem

    @vcml_BOMItem.setter
    def vcml_BOMItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_BOMItem__vcml_BOMItem", None)
        self.__vcml_BOMItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_BillOfMaterial"):
                opp_val = getattr(old_value, "vcml_BillOfMaterial", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_BillOfMaterial"):
                opp_val = getattr(value, "vcml_BillOfMaterial", None)
                if opp_val is None:
                    setattr(value, "vcml_BillOfMaterial", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vcml_BOMItem15(self):
        return self.__vcml_BOMItem15

    @vcml_BOMItem15.setter
    def vcml_BOMItem15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_BOMItem__vcml_BOMItem15", None)
        self.__vcml_BOMItem15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vcml_ConfigurationProfileEntry"):
                    opp_val = getattr(item, "vcml_ConfigurationProfileEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "vcml_ConfigurationProfileEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vcml_ConfigurationProfileEntry"):
                    opp_val = getattr(item, "vcml_ConfigurationProfileEntry", None)
                    
                    setattr(item, "vcml_ConfigurationProfileEntry", self)
                    

class vcml_VCObject:

    def __init__(self, name: str, vcml_VCObject: "vcml_VcmlModel" = None, vcml_VCObject6: "vcml_Description" = None, vcml_VCObject8: set["vcml_Option"] = None):
        self.name = name
        self.vcml_VCObject = vcml_VCObject
        self.vcml_VCObject6 = vcml_VCObject6
        self.vcml_VCObject8 = vcml_VCObject8 if vcml_VCObject8 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def vcml_VCObject(self):
        return self.__vcml_VCObject

    @vcml_VCObject.setter
    def vcml_VCObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_VCObject__vcml_VCObject", None)
        self.__vcml_VCObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_VcmlModel4"):
                opp_val = getattr(old_value, "vcml_VcmlModel4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_VcmlModel4"):
                opp_val = getattr(value, "vcml_VcmlModel4", None)
                if opp_val is None:
                    setattr(value, "vcml_VcmlModel4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vcml_VCObject8(self):
        return self.__vcml_VCObject8

    @vcml_VCObject8.setter
    def vcml_VCObject8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_VCObject__vcml_VCObject8", None)
        self.__vcml_VCObject8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vcml_Option9"):
                    opp_val = getattr(item, "vcml_Option9", None)
                    
                    if opp_val == self:
                        setattr(item, "vcml_Option9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vcml_Option9"):
                    opp_val = getattr(item, "vcml_Option9", None)
                    
                    setattr(item, "vcml_Option9", self)
                    

    @property
    def vcml_VCObject6(self):
        return self.__vcml_VCObject6

    @vcml_VCObject6.setter
    def vcml_VCObject6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_VCObject__vcml_VCObject6", None)
        self.__vcml_VCObject6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_Description"):
                opp_val = getattr(old_value, "vcml_Description", None)
                if opp_val == self:
                    setattr(old_value, "vcml_Description", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_Description"):
                opp_val = getattr(value, "vcml_Description", None)
                setattr(value, "vcml_Description", self)

class vcml_Option:

    def __init__(self, name: str, value: str, vcml_Option: "vcml_VcmlModel" = None, vcml_Option9: "vcml_VCObject" = None):
        self.name = name
        self.value = value
        self.vcml_Option = vcml_Option
        self.vcml_Option9 = vcml_Option9
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def vcml_Option9(self):
        return self.__vcml_Option9

    @vcml_Option9.setter
    def vcml_Option9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Option__vcml_Option9", None)
        self.__vcml_Option9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_VCObject8"):
                opp_val = getattr(old_value, "vcml_VCObject8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_VCObject8"):
                opp_val = getattr(value, "vcml_VCObject8", None)
                if opp_val is None:
                    setattr(value, "vcml_VCObject8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vcml_Option(self):
        return self.__vcml_Option

    @vcml_Option.setter
    def vcml_Option(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Option__vcml_Option", None)
        self.__vcml_Option = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_VcmlModel2"):
                opp_val = getattr(old_value, "vcml_VcmlModel2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_VcmlModel2"):
                opp_val = getattr(value, "vcml_VcmlModel2", None)
                if opp_val is None:
                    setattr(value, "vcml_VcmlModel2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class vcml_Import:

    def __init__(self, importURI: str, vcml_Import: "vcml_VcmlModel" = None):
        self.importURI = importURI
        self.vcml_Import = vcml_Import
        
    @property
    def importURI(self) -> str:
        return self.__importURI

    @importURI.setter
    def importURI(self, importURI: str):
        self.__importURI = importURI

    @property
    def vcml_Import(self):
        return self.__vcml_Import

    @vcml_Import.setter
    def vcml_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcml_Import__vcml_Import", None)
        self.__vcml_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vcml_VcmlModel"):
                opp_val = getattr(old_value, "vcml_VcmlModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vcml_VcmlModel"):
                opp_val = getattr(value, "vcml_VcmlModel", None)
                if opp_val is None:
                    setattr(value, "vcml_VcmlModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class vcml_VcmlModel:

    pass