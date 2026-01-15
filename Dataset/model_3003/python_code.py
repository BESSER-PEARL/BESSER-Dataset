from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class BSPrimitiveType(Enum):
    NONE = "NONE"
    STRING = "STRING"
    TAGGED_STRING = "TAGGED_STRING"
    NUMBER = "NUMBER"
    OBJECT = "OBJECT"
    VOID = "VOID"


############################################
# Definition of Classes
############################################

class BSExpression:

    pass
class blorqueScript_BSBitwiseAndExpression(BSExpression):

    pass
class blorqueScript_BSEqualityExpression(BSExpression):

    def __init__(self, operator: str, blorqueScript_BSEqualityExpression: "blorqueScript_BSExpression" = None, blorqueScript_BSEqualityExpression101: "blorqueScript_BSExpression" = None):
        self.operator = operator
        self.blorqueScript_BSEqualityExpression = blorqueScript_BSEqualityExpression
        self.blorqueScript_BSEqualityExpression101 = blorqueScript_BSEqualityExpression101
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def blorqueScript_BSEqualityExpression(self):
        return self.__blorqueScript_BSEqualityExpression

    @blorqueScript_BSEqualityExpression.setter
    def blorqueScript_BSEqualityExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_blorqueScript_BSEqualityExpression__blorqueScript_BSEqualityExpression", None)
        self.__blorqueScript_BSEqualityExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blorqueScript_BSExpression99"):
                opp_val = getattr(old_value, "blorqueScript_BSExpression99", None)
                if opp_val == self:
                    setattr(old_value, "blorqueScript_BSExpression99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blorqueScript_BSExpression99"):
                opp_val = getattr(value, "blorqueScript_BSExpression99", None)
                setattr(value, "blorqueScript_BSExpression99", self)

    @property
    def blorqueScript_BSEqualityExpression101(self):
        return self.__blorqueScript_BSEqualityExpression101

    @blorqueScript_BSEqualityExpression101.setter
    def blorqueScript_BSEqualityExpression101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_blorqueScript_BSEqualityExpression__blorqueScript_BSEqualityExpression101", None)
        self.__blorqueScript_BSEqualityExpression101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blorqueScript_BSExpression102"):
                opp_val = getattr(old_value, "blorqueScript_BSExpression102", None)
                if opp_val == self:
                    setattr(old_value, "blorqueScript_BSExpression102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blorqueScript_BSExpression102"):
                opp_val = getattr(value, "blorqueScript_BSExpression102", None)
                setattr(value, "blorqueScript_BSExpression102", self)

class blorqueScript_BSRealConstant(BSExpression):

    def __init__(self, right: int, blorqueScript_BSRealConstant: "blorqueScript_BSNumberConstant" = None):
        self.right = right
        self.blorqueScript_BSRealConstant = blorqueScript_BSRealConstant
        
    @property
    def right(self) -> int:
        return self.__right

    @right.setter
    def right(self, right: int):
        self.__right = right

    @property
    def blorqueScript_BSRealConstant(self):
        return self.__blorqueScript_BSRealConstant

    @blorqueScript_BSRealConstant.setter
    def blorqueScript_BSRealConstant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_blorqueScript_BSRealConstant__blorqueScript_BSRealConstant", None)
        self.__blorqueScript_BSRealConstant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blorqueScript_BSNumberConstant"):
                opp_val = getattr(old_value, "blorqueScript_BSNumberConstant", None)
                if opp_val == self:
                    setattr(old_value, "blorqueScript_BSNumberConstant", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blorqueScript_BSNumberConstant"):
                opp_val = getattr(value, "blorqueScript_BSNumberConstant", None)
                setattr(value, "blorqueScript_BSNumberConstant", self)

class blorqueScript_BSBooleanOrExpression(BSExpression):

    pass
class blorqueScript_BSTernaryExpression(BSExpression):

    pass
class blorqueScript_BSArrayAccessExpression(BSExpression):

    pass
class blorqueScript_BSParentLiteral(BSExpression):

    pass
class blorqueScript_BSBooleanAndExpression(BSExpression):

    pass
class blorqueScript_BSThisLiteral(BSExpression):

    pass
class blorqueScript_BSNumberConstant(BSExpression):

    def __init__(self, value: int, blorqueScript_BSNumberConstant: "blorqueScript_BSRealConstant" = None):
        self.value = value
        self.blorqueScript_BSNumberConstant = blorqueScript_BSNumberConstant
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def blorqueScript_BSNumberConstant(self):
        return self.__blorqueScript_BSNumberConstant

    @blorqueScript_BSNumberConstant.setter
    def blorqueScript_BSNumberConstant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_blorqueScript_BSNumberConstant__blorqueScript_BSNumberConstant", None)
        self.__blorqueScript_BSNumberConstant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blorqueScript_BSRealConstant"):
                opp_val = getattr(old_value, "blorqueScript_BSRealConstant", None)
                if opp_val == self:
                    setattr(old_value, "blorqueScript_BSRealConstant", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blorqueScript_BSRealConstant"):
                opp_val = getattr(value, "blorqueScript_BSRealConstant", None)
                setattr(value, "blorqueScript_BSRealConstant", self)

class blorqueScript_BSNewExpression(BSExpression):

    def __init__(self, isArray: bool, blorqueScript_BSNewExpression128: set["blorqueScript_BSExpression"] = None, blorqueScript_BSNewExpression: "blorqueScript_BSClass" = None):
        self.isArray = isArray
        self.blorqueScript_BSNewExpression128 = blorqueScript_BSNewExpression128 if blorqueScript_BSNewExpression128 is not None else set()
        self.blorqueScript_BSNewExpression = blorqueScript_BSNewExpression
        
    @property
    def isArray(self) -> bool:
        return self.__isArray

    @isArray.setter
    def isArray(self, isArray: bool):
        self.__isArray = isArray

    @property
    def blorqueScript_BSNewExpression128(self):
        return self.__blorqueScript_BSNewExpression128

    @blorqueScript_BSNewExpression128.setter
    def blorqueScript_BSNewExpression128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_blorqueScript_BSNewExpression__blorqueScript_BSNewExpression128", None)
        self.__blorqueScript_BSNewExpression128 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "blorqueScript_BSExpression129"):
                    opp_val = getattr(item, "blorqueScript_BSExpression129", None)
                    
                    if opp_val == self:
                        setattr(item, "blorqueScript_BSExpression129", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "blorqueScript_BSExpression129"):
                    opp_val = getattr(item, "blorqueScript_BSExpression129", None)
                    
                    setattr(item, "blorqueScript_BSExpression129", self)
                    

    @property
    def blorqueScript_BSNewExpression(self):
        return self.__blorqueScript_BSNewExpression

    @blorqueScript_BSNewExpression.setter
    def blorqueScript_BSNewExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_blorqueScript_BSNewExpression__blorqueScript_BSNewExpression", None)
        self.__blorqueScript_BSNewExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blorqueScript_BSClass126"):
                opp_val = getattr(old_value, "blorqueScript_BSClass126", None)
                if opp_val == self:
                    setattr(old_value, "blorqueScript_BSClass126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blorqueScript_BSClass126"):
                opp_val = getattr(value, "blorqueScript_BSClass126", None)
                setattr(value, "blorqueScript_BSClass126", self)

class blorqueScript_BSParentheticalExpression(BSExpression):

    pass
class blorqueScript_BSPostfixArithmeticExpression(BSExpression):

    def __init__(self, operator: str, blorqueScript_BSPostfixArithmeticExpression: "blorqueScript_BSExpression" = None):
        self.operator = operator
        self.blorqueScript_BSPostfixArithmeticExpression = blorqueScript_BSPostfixArithmeticExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def blorqueScript_BSPostfixArithmeticExpression(self):
        return self.__blorqueScript_BSPostfixArithmeticExpression

    @blorqueScript_BSPostfixArithmeticExpression.setter
    def blorqueScript_BSPostfixArithmeticExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_blorqueScript_BSPostfixArithmeticExpression__blorqueScript_BSPostfixArithmeticExpression", None)
        self.__blorqueScript_BSPostfixArithmeticExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blorqueScript_BSExpression148"):
                opp_val = getattr(old_value, "blorqueScript_BSExpression148", None)
                if opp_val == self:
                    setattr(old_value, "blorqueScript_BSExpression148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blorqueScript_BSExpression148"):
                opp_val = getattr(value, "blorqueScript_BSExpression148", None)
                setattr(value, "blorqueScript_BSExpression148", self)

class blorqueScript_BSMemberSelectionExpression(BSExpression):

    pass
class blorqueScript_BSNullLiteral(BSExpression):

    pass
class blorqueScript_BSBitwiseOrExpression(BSExpression):

    pass
class blorqueScript_BSOrderedRelationExpression(BSExpression):

    def __init__(self, operator: str, blorqueScript_BSOrderedRelationExpression: "blorqueScript_BSExpression" = None, blorqueScript_BSOrderedRelationExpression106: "blorqueScript_BSExpression" = None):
        self.operator = operator
        self.blorqueScript_BSOrderedRelationExpression = blorqueScript_BSOrderedRelationExpression
        self.blorqueScript_BSOrderedRelationExpression106 = blorqueScript_BSOrderedRelationExpression106
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def blorqueScript_BSOrderedRelationExpression(self):
        return self.__blorqueScript_BSOrderedRelationExpression

    @blorqueScript_BSOrderedRelationExpression.setter
    def blorqueScript_BSOrderedRelationExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_blorqueScript_BSOrderedRelationExpression__blorqueScript_BSOrderedRelationExpression", None)
        self.__blorqueScript_BSOrderedRelationExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blorqueScript_BSExpression104"):
                opp_val = getattr(old_value, "blorqueScript_BSExpression104", None)
                if opp_val == self:
                    setattr(old_value, "blorqueScript_BSExpression104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blorqueScript_BSExpression104"):
                opp_val = getattr(value, "blorqueScript_BSExpression104", None)
                setattr(value, "blorqueScript_BSExpression104", self)

    @property
    def blorqueScript_BSOrderedRelationExpression106(self):
        return self.__blorqueScript_BSOrderedRelationExpression106

    @blorqueScript_BSOrderedRelationExpression106.setter
    def blorqueScript_BSOrderedRelationExpression106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_blorqueScript_BSOrderedRelationExpression__blorqueScript_BSOrderedRelationExpression106", None)
        self.__blorqueScript_BSOrderedRelationExpression106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blorqueScript_BSExpression107"):
                opp_val = getattr(old_value, "blorqueScript_BSExpression107", None)
                if opp_val == self:
                    setattr(old_value, "blorqueScript_BSExpression107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blorqueScript_BSExpression107"):
                opp_val = getattr(value, "blorqueScript_BSExpression107", None)
                setattr(value, "blorqueScript_BSExpression107", self)

class blorqueScript_BSBitwiseShiftExpression(BSExpression):

    def __init__(self, operator: str, blorqueScript_BSBitwiseShiftExpression: "blorqueScript_BSExpression" = None, blorqueScript_BSBitwiseShiftExpression111: "blorqueScript_BSExpression" = None):
        self.operator = operator
        self.blorqueScript_BSBitwiseShiftExpression = blorqueScript_BSBitwiseShiftExpression
        self.blorqueScript_BSBitwiseShiftExpression111 = blorqueScript_BSBitwiseShiftExpression111
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def blorqueScript_BSBitwiseShiftExpression(self):
        return self.__blorqueScript_BSBitwiseShiftExpression

    @blorqueScript_BSBitwiseShiftExpression.setter
    def blorqueScript_BSBitwiseShiftExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_blorqueScript_BSBitwiseShiftExpression__blorqueScript_BSBitwiseShiftExpression", None)
        self.__blorqueScript_BSBitwiseShiftExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blorqueScript_BSExpression109"):
                opp_val = getattr(old_value, "blorqueScript_BSExpression109", None)
                if opp_val == self:
                    setattr(old_value, "blorqueScript_BSExpression109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blorqueScript_BSExpression109"):
                opp_val = getattr(value, "blorqueScript_BSExpression109", None)
                setattr(value, "blorqueScript_BSExpression109", self)

    @property
    def blorqueScript_BSBitwiseShiftExpression111(self):
        return self.__blorqueScript_BSBitwiseShiftExpression111

    @blorqueScript_BSBitwiseShiftExpression111.setter
    def blorqueScript_BSBitwiseShiftExpression111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_blorqueScript_BSBitwiseShiftExpression__blorqueScript_BSBitwiseShiftExpression111", None)
        self.__blorqueScript_BSBitwiseShiftExpression111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blorqueScript_BSExpression112"):
                opp_val = getattr(old_value, "blorqueScript_BSExpression112", None)
                if opp_val == self:
                    setattr(old_value, "blorqueScript_BSExpression112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blorqueScript_BSExpression112"):
                opp_val = getattr(value, "blorqueScript_BSExpression112", None)
                setattr(value, "blorqueScript_BSExpression112", self)

class blorqueScript_BSMethodInvokationExpression(BSExpression):

    pass
class blorqueScript_BSMulDivOrModExpression(BSExpression):

    def __init__(self, operator: str, blorqueScript_BSMulDivOrModExpression: "blorqueScript_BSExpression" = None, blorqueScript_BSMulDivOrModExpression121: "blorqueScript_BSExpression" = None):
        self.operator = operator
        self.blorqueScript_BSMulDivOrModExpression = blorqueScript_BSMulDivOrModExpression
        self.blorqueScript_BSMulDivOrModExpression121 = blorqueScript_BSMulDivOrModExpression121
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def blorqueScript_BSMulDivOrModExpression(self):
        return self.__blorqueScript_BSMulDivOrModExpression

    @blorqueScript_BSMulDivOrModExpression.setter
    def blorqueScript_BSMulDivOrModExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_blorqueScript_BSMulDivOrModExpression__blorqueScript_BSMulDivOrModExpression", None)
        self.__blorqueScript_BSMulDivOrModExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blorqueScript_BSExpression119"):
                opp_val = getattr(old_value, "blorqueScript_BSExpression119", None)
                if opp_val == self:
                    setattr(old_value, "blorqueScript_BSExpression119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blorqueScript_BSExpression119"):
                opp_val = getattr(value, "blorqueScript_BSExpression119", None)
                setattr(value, "blorqueScript_BSExpression119", self)

    @property
    def blorqueScript_BSMulDivOrModExpression121(self):
        return self.__blorqueScript_BSMulDivOrModExpression121

    @blorqueScript_BSMulDivOrModExpression121.setter
    def blorqueScript_BSMulDivOrModExpression121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_blorqueScript_BSMulDivOrModExpression__blorqueScript_BSMulDivOrModExpression121", None)
        self.__blorqueScript_BSMulDivOrModExpression121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blorqueScript_BSExpression122"):
                opp_val = getattr(old_value, "blorqueScript_BSExpression122", None)
                if opp_val == self:
                    setattr(old_value, "blorqueScript_BSExpression122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blorqueScript_BSExpression122"):
                opp_val = getattr(value, "blorqueScript_BSExpression122", None)
                setattr(value, "blorqueScript_BSExpression122", self)

class blorqueScript_BSClientLiteral(BSExpression):

    pass
class blorqueScript_BSUnaryModifierExpression(BSExpression):

    def __init__(self, operator: str, blorqueScript_BSUnaryModifierExpression: "blorqueScript_BSExpression" = None):
        self.operator = operator
        self.blorqueScript_BSUnaryModifierExpression = blorqueScript_BSUnaryModifierExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def blorqueScript_BSUnaryModifierExpression(self):
        return self.__blorqueScript_BSUnaryModifierExpression

    @blorqueScript_BSUnaryModifierExpression.setter
    def blorqueScript_BSUnaryModifierExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_blorqueScript_BSUnaryModifierExpression__blorqueScript_BSUnaryModifierExpression", None)
        self.__blorqueScript_BSUnaryModifierExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blorqueScript_BSExpression131"):
                opp_val = getattr(old_value, "blorqueScript_BSExpression131", None)
                if opp_val == self:
                    setattr(old_value, "blorqueScript_BSExpression131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blorqueScript_BSExpression131"):
                opp_val = getattr(value, "blorqueScript_BSExpression131", None)
                setattr(value, "blorqueScript_BSExpression131", self)

class blorqueScript_BSBooleanConstant(BSExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class blorqueScript_BSPlusMinusOrStringConcatExpression(BSExpression):

    def __init__(self, operator: str, blorqueScript_BSPlusMinusOrStringConcatExpression116: "blorqueScript_BSExpression" = None, blorqueScript_BSPlusMinusOrStringConcatExpression: "blorqueScript_BSExpression" = None):
        self.operator = operator
        self.blorqueScript_BSPlusMinusOrStringConcatExpression116 = blorqueScript_BSPlusMinusOrStringConcatExpression116
        self.blorqueScript_BSPlusMinusOrStringConcatExpression = blorqueScript_BSPlusMinusOrStringConcatExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def blorqueScript_BSPlusMinusOrStringConcatExpression(self):
        return self.__blorqueScript_BSPlusMinusOrStringConcatExpression

    @blorqueScript_BSPlusMinusOrStringConcatExpression.setter
    def blorqueScript_BSPlusMinusOrStringConcatExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_blorqueScript_BSPlusMinusOrStringConcatExpression__blorqueScript_BSPlusMinusOrStringConcatExpression", None)
        self.__blorqueScript_BSPlusMinusOrStringConcatExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blorqueScript_BSExpression114"):
                opp_val = getattr(old_value, "blorqueScript_BSExpression114", None)
                if opp_val == self:
                    setattr(old_value, "blorqueScript_BSExpression114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blorqueScript_BSExpression114"):
                opp_val = getattr(value, "blorqueScript_BSExpression114", None)
                setattr(value, "blorqueScript_BSExpression114", self)

    @property
    def blorqueScript_BSPlusMinusOrStringConcatExpression116(self):
        return self.__blorqueScript_BSPlusMinusOrStringConcatExpression116

    @blorqueScript_BSPlusMinusOrStringConcatExpression116.setter
    def blorqueScript_BSPlusMinusOrStringConcatExpression116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_blorqueScript_BSPlusMinusOrStringConcatExpression__blorqueScript_BSPlusMinusOrStringConcatExpression116", None)
        self.__blorqueScript_BSPlusMinusOrStringConcatExpression116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blorqueScript_BSExpression117"):
                opp_val = getattr(old_value, "blorqueScript_BSExpression117", None)
                if opp_val == self:
                    setattr(old_value, "blorqueScript_BSExpression117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blorqueScript_BSExpression117"):
                opp_val = getattr(value, "blorqueScript_BSExpression117", None)
                setattr(value, "blorqueScript_BSExpression117", self)

class blorqueScript_BSBitwiseXorExpression(BSExpression):

    pass
class blorqueScript_BSStringConstant(BSExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class blorqueScript_BSHexadecimalConstant(BSExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class blorqueScript_BSSymbolRef(BSExpression):

    pass
class blorqueScript_BSCastExpression(BSExpression):

    def __init__(self, pType: str, isArray: bool, blorqueScript_BSCastExpression: "blorqueScript_BSExpression" = None):
        self.pType = pType
        self.isArray = isArray
        self.blorqueScript_BSCastExpression = blorqueScript_BSCastExpression
        
    @property
    def isArray(self) -> bool:
        return self.__isArray

    @isArray.setter
    def isArray(self, isArray: bool):
        self.__isArray = isArray

    @property
    def pType(self) -> str:
        return self.__pType

    @pType.setter
    def pType(self, pType: str):
        self.__pType = pType

    @property
    def blorqueScript_BSCastExpression(self):
        return self.__blorqueScript_BSCastExpression

    @blorqueScript_BSCastExpression.setter
    def blorqueScript_BSCastExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_blorqueScript_BSCastExpression__blorqueScript_BSCastExpression", None)
        self.__blorqueScript_BSCastExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blorqueScript_BSExpression124"):
                opp_val = getattr(old_value, "blorqueScript_BSExpression124", None)
                if opp_val == self:
                    setattr(old_value, "blorqueScript_BSExpression124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blorqueScript_BSExpression124"):
                opp_val = getattr(value, "blorqueScript_BSExpression124", None)
                setattr(value, "blorqueScript_BSExpression124", self)

class blorqueScript_BSAssignmentExpression(BSExpression):

    def __init__(self, assignmentOperator: str, blorqueScript_BSAssignmentExpression: "blorqueScript_BSExpression" = None, blorqueScript_BSAssignmentExpression63: "blorqueScript_BSExpression" = None):
        self.assignmentOperator = assignmentOperator
        self.blorqueScript_BSAssignmentExpression = blorqueScript_BSAssignmentExpression
        self.blorqueScript_BSAssignmentExpression63 = blorqueScript_BSAssignmentExpression63
        
    @property
    def assignmentOperator(self) -> str:
        return self.__assignmentOperator

    @assignmentOperator.setter
    def assignmentOperator(self, assignmentOperator: str):
        self.__assignmentOperator = assignmentOperator

    @property
    def blorqueScript_BSAssignmentExpression(self):
        return self.__blorqueScript_BSAssignmentExpression

    @blorqueScript_BSAssignmentExpression.setter
    def blorqueScript_BSAssignmentExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_blorqueScript_BSAssignmentExpression__blorqueScript_BSAssignmentExpression", None)
        self.__blorqueScript_BSAssignmentExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blorqueScript_BSExpression61"):
                opp_val = getattr(old_value, "blorqueScript_BSExpression61", None)
                if opp_val == self:
                    setattr(old_value, "blorqueScript_BSExpression61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blorqueScript_BSExpression61"):
                opp_val = getattr(value, "blorqueScript_BSExpression61", None)
                setattr(value, "blorqueScript_BSExpression61", self)

    @property
    def blorqueScript_BSAssignmentExpression63(self):
        return self.__blorqueScript_BSAssignmentExpression63

    @blorqueScript_BSAssignmentExpression63.setter
    def blorqueScript_BSAssignmentExpression63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_blorqueScript_BSAssignmentExpression__blorqueScript_BSAssignmentExpression63", None)
        self.__blorqueScript_BSAssignmentExpression63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blorqueScript_BSExpression64"):
                opp_val = getattr(old_value, "blorqueScript_BSExpression64", None)
                if opp_val == self:
                    setattr(old_value, "blorqueScript_BSExpression64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blorqueScript_BSExpression64"):
                opp_val = getattr(value, "blorqueScript_BSExpression64", None)
                setattr(value, "blorqueScript_BSExpression64", self)

class blorqueScript_BSSymbol:

    def __init__(self, pType: str, name: str, blorqueScript_BSSymbol: "blorqueScript_BSClass" = None, blorqueScript_BSSymbol151: "blorqueScript_BSSymbolRef" = None):
        self.pType = pType
        self.name = name
        self.blorqueScript_BSSymbol = blorqueScript_BSSymbol
        self.blorqueScript_BSSymbol151 = blorqueScript_BSSymbol151
        
    @property
    def pType(self) -> str:
        return self.__pType

    @pType.setter
    def pType(self, pType: str):
        self.__pType = pType

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def blorqueScript_BSSymbol151(self):
        return self.__blorqueScript_BSSymbol151

    @blorqueScript_BSSymbol151.setter
    def blorqueScript_BSSymbol151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_blorqueScript_BSSymbol__blorqueScript_BSSymbol151", None)
        self.__blorqueScript_BSSymbol151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blorqueScript_BSSymbolRef"):
                opp_val = getattr(old_value, "blorqueScript_BSSymbolRef", None)
                if opp_val == self:
                    setattr(old_value, "blorqueScript_BSSymbolRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blorqueScript_BSSymbolRef"):
                opp_val = getattr(value, "blorqueScript_BSSymbolRef", None)
                setattr(value, "blorqueScript_BSSymbolRef", self)

    @property
    def blorqueScript_BSSymbol(self):
        return self.__blorqueScript_BSSymbol

    @blorqueScript_BSSymbol.setter
    def blorqueScript_BSSymbol(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_blorqueScript_BSSymbol__blorqueScript_BSSymbol", None)
        self.__blorqueScript_BSSymbol = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blorqueScript_BSClass59"):
                opp_val = getattr(old_value, "blorqueScript_BSClass59", None)
                if opp_val == self:
                    setattr(old_value, "blorqueScript_BSClass59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blorqueScript_BSClass59"):
                opp_val = getattr(value, "blorqueScript_BSClass59", None)
                setattr(value, "blorqueScript_BSClass59", self)

class blorqueScript_BSBlock:

    pass
class blorqueScript_BSCase:

    pass
class blorqueScript_BSStatement:

    pass
class BSBlock:

    pass
class blorqueScript_BSSwitchBlock(BSBlock):

    pass
class blorqueScript_BSIfBlock(BSBlock):

    pass
class blorqueScript_BSLoopBlock(BSBlock):

    pass
class blorqueScript_BSCaseBlock(BSBlock):

    pass
class blorqueScript_BSMethodBody(BSBlock):

    pass
class BSMember:

    pass
class blorqueScript_BSMethod(BSMember):

    pass
class blorqueScript_BSField(BSMember):

    pass
class BSSymbol:

    pass
class blorqueScript_BSParameter(BSSymbol):

    def __init__(self, isArray: bool, blorqueScript_BSParameter: "blorqueScript_BSMethod" = None):
        self.isArray = isArray
        self.blorqueScript_BSParameter = blorqueScript_BSParameter
        
    @property
    def isArray(self) -> bool:
        return self.__isArray

    @isArray.setter
    def isArray(self, isArray: bool):
        self.__isArray = isArray

    @property
    def blorqueScript_BSParameter(self):
        return self.__blorqueScript_BSParameter

    @blorqueScript_BSParameter.setter
    def blorqueScript_BSParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_blorqueScript_BSParameter__blorqueScript_BSParameter", None)
        self.__blorqueScript_BSParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blorqueScript_BSMethod"):
                opp_val = getattr(old_value, "blorqueScript_BSMethod", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blorqueScript_BSMethod"):
                opp_val = getattr(value, "blorqueScript_BSMethod", None)
                if opp_val is None:
                    setattr(value, "blorqueScript_BSMethod", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BSStatement:

    pass
class blorqueScript_BSWhileLoop(BSStatement):

    pass
class blorqueScript_BSBreak(BSStatement):

    pass
class blorqueScript_BSIfStatement(BSStatement):

    pass
class blorqueScript_BSForLoop(BSStatement):

    pass
class blorqueScript_BSSwitchStatement(BSStatement):

    def __init__(self, stringSwitch: bool, blorqueScript_BSSwitchStatement: "blorqueScript_BSExpression" = None, blorqueScript_BSSwitchStatement41: "blorqueScript_BSSwitchBlock" = None):
        self.stringSwitch = stringSwitch
        self.blorqueScript_BSSwitchStatement = blorqueScript_BSSwitchStatement
        self.blorqueScript_BSSwitchStatement41 = blorqueScript_BSSwitchStatement41
        
    @property
    def stringSwitch(self) -> bool:
        return self.__stringSwitch

    @stringSwitch.setter
    def stringSwitch(self, stringSwitch: bool):
        self.__stringSwitch = stringSwitch

    @property
    def blorqueScript_BSSwitchStatement41(self):
        return self.__blorqueScript_BSSwitchStatement41

    @blorqueScript_BSSwitchStatement41.setter
    def blorqueScript_BSSwitchStatement41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_blorqueScript_BSSwitchStatement__blorqueScript_BSSwitchStatement41", None)
        self.__blorqueScript_BSSwitchStatement41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blorqueScript_BSSwitchBlock"):
                opp_val = getattr(old_value, "blorqueScript_BSSwitchBlock", None)
                if opp_val == self:
                    setattr(old_value, "blorqueScript_BSSwitchBlock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blorqueScript_BSSwitchBlock"):
                opp_val = getattr(value, "blorqueScript_BSSwitchBlock", None)
                setattr(value, "blorqueScript_BSSwitchBlock", self)

    @property
    def blorqueScript_BSSwitchStatement(self):
        return self.__blorqueScript_BSSwitchStatement

    @blorqueScript_BSSwitchStatement.setter
    def blorqueScript_BSSwitchStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_blorqueScript_BSSwitchStatement__blorqueScript_BSSwitchStatement", None)
        self.__blorqueScript_BSSwitchStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blorqueScript_BSExpression39"):
                opp_val = getattr(old_value, "blorqueScript_BSExpression39", None)
                if opp_val == self:
                    setattr(old_value, "blorqueScript_BSExpression39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blorqueScript_BSExpression39"):
                opp_val = getattr(value, "blorqueScript_BSExpression39", None)
                setattr(value, "blorqueScript_BSExpression39", self)

class blorqueScript_BSContinue(BSStatement):

    pass
class blorqueScript_BSVariableDeclaration(BSSymbol, BSStatement):

    pass
class blorqueScript_BSExpression(BSStatement):

    pass
class blorqueScript_BSReturn(BSStatement):

    pass
class blorqueScript_BSClass:

    def __init__(self, name: str, blorqueScript_BSClass7: set["blorqueScript_BSMember"] = None, blorqueScript_BSClass: "blorqueScript_BSFile" = None, blorqueScript_BSClass5: "blorqueScript_BSClass" = None, blorqueScript_BSClass3: "blorqueScript_BSClass" = None, blorqueScript_BSClass59: "blorqueScript_BSSymbol" = None, blorqueScript_BSClass126: "blorqueScript_BSNewExpression" = None):
        self.name = name
        self.blorqueScript_BSClass7 = blorqueScript_BSClass7 if blorqueScript_BSClass7 is not None else set()
        self.blorqueScript_BSClass = blorqueScript_BSClass
        self.blorqueScript_BSClass5 = blorqueScript_BSClass5
        self.blorqueScript_BSClass3 = blorqueScript_BSClass3
        self.blorqueScript_BSClass59 = blorqueScript_BSClass59
        self.blorqueScript_BSClass126 = blorqueScript_BSClass126
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def blorqueScript_BSClass7(self):
        return self.__blorqueScript_BSClass7

    @blorqueScript_BSClass7.setter
    def blorqueScript_BSClass7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_blorqueScript_BSClass__blorqueScript_BSClass7", None)
        self.__blorqueScript_BSClass7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "blorqueScript_BSMember"):
                    opp_val = getattr(item, "blorqueScript_BSMember", None)
                    
                    if opp_val == self:
                        setattr(item, "blorqueScript_BSMember", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "blorqueScript_BSMember"):
                    opp_val = getattr(item, "blorqueScript_BSMember", None)
                    
                    setattr(item, "blorqueScript_BSMember", self)
                    

    @property
    def blorqueScript_BSClass3(self):
        return self.__blorqueScript_BSClass3

    @blorqueScript_BSClass3.setter
    def blorqueScript_BSClass3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_blorqueScript_BSClass__blorqueScript_BSClass3", None)
        self.__blorqueScript_BSClass3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blorqueScript_BSClass5"):
                opp_val = getattr(old_value, "blorqueScript_BSClass5", None)
                if opp_val == self:
                    setattr(old_value, "blorqueScript_BSClass5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blorqueScript_BSClass5"):
                opp_val = getattr(value, "blorqueScript_BSClass5", None)
                setattr(value, "blorqueScript_BSClass5", self)

    @property
    def blorqueScript_BSClass(self):
        return self.__blorqueScript_BSClass

    @blorqueScript_BSClass.setter
    def blorqueScript_BSClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_blorqueScript_BSClass__blorqueScript_BSClass", None)
        self.__blorqueScript_BSClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blorqueScript_BSFile2"):
                opp_val = getattr(old_value, "blorqueScript_BSFile2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blorqueScript_BSFile2"):
                opp_val = getattr(value, "blorqueScript_BSFile2", None)
                if opp_val is None:
                    setattr(value, "blorqueScript_BSFile2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def blorqueScript_BSClass59(self):
        return self.__blorqueScript_BSClass59

    @blorqueScript_BSClass59.setter
    def blorqueScript_BSClass59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_blorqueScript_BSClass__blorqueScript_BSClass59", None)
        self.__blorqueScript_BSClass59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blorqueScript_BSSymbol"):
                opp_val = getattr(old_value, "blorqueScript_BSSymbol", None)
                if opp_val == self:
                    setattr(old_value, "blorqueScript_BSSymbol", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blorqueScript_BSSymbol"):
                opp_val = getattr(value, "blorqueScript_BSSymbol", None)
                setattr(value, "blorqueScript_BSSymbol", self)

    @property
    def blorqueScript_BSClass126(self):
        return self.__blorqueScript_BSClass126

    @blorqueScript_BSClass126.setter
    def blorqueScript_BSClass126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_blorqueScript_BSClass__blorqueScript_BSClass126", None)
        self.__blorqueScript_BSClass126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blorqueScript_BSNewExpression"):
                opp_val = getattr(old_value, "blorqueScript_BSNewExpression", None)
                if opp_val == self:
                    setattr(old_value, "blorqueScript_BSNewExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blorqueScript_BSNewExpression"):
                opp_val = getattr(value, "blorqueScript_BSNewExpression", None)
                setattr(value, "blorqueScript_BSNewExpression", self)

    @property
    def blorqueScript_BSClass5(self):
        return self.__blorqueScript_BSClass5

    @blorqueScript_BSClass5.setter
    def blorqueScript_BSClass5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_blorqueScript_BSClass__blorqueScript_BSClass5", None)
        self.__blorqueScript_BSClass5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blorqueScript_BSClass3"):
                opp_val = getattr(old_value, "blorqueScript_BSClass3", None)
                if opp_val == self:
                    setattr(old_value, "blorqueScript_BSClass3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blorqueScript_BSClass3"):
                opp_val = getattr(value, "blorqueScript_BSClass3", None)
                setattr(value, "blorqueScript_BSClass3", self)

class blorqueScript_BSImport:

    def __init__(self, importedNamespace: str, blorqueScript_BSImport: "blorqueScript_BSFile" = None):
        self.importedNamespace = importedNamespace
        self.blorqueScript_BSImport = blorqueScript_BSImport
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

    @property
    def blorqueScript_BSImport(self):
        return self.__blorqueScript_BSImport

    @blorqueScript_BSImport.setter
    def blorqueScript_BSImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_blorqueScript_BSImport__blorqueScript_BSImport", None)
        self.__blorqueScript_BSImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blorqueScript_BSFile"):
                opp_val = getattr(old_value, "blorqueScript_BSFile", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blorqueScript_BSFile"):
                opp_val = getattr(value, "blorqueScript_BSFile", None)
                if opp_val is None:
                    setattr(value, "blorqueScript_BSFile", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class blorqueScript_BSFile:

    def __init__(self, name: str, blorqueScript_BSFile: set["blorqueScript_BSImport"] = None, blorqueScript_BSFile2: set["blorqueScript_BSClass"] = None):
        self.name = name
        self.blorqueScript_BSFile = blorqueScript_BSFile if blorqueScript_BSFile is not None else set()
        self.blorqueScript_BSFile2 = blorqueScript_BSFile2 if blorqueScript_BSFile2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def blorqueScript_BSFile(self):
        return self.__blorqueScript_BSFile

    @blorqueScript_BSFile.setter
    def blorqueScript_BSFile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_blorqueScript_BSFile__blorqueScript_BSFile", None)
        self.__blorqueScript_BSFile = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "blorqueScript_BSImport"):
                    opp_val = getattr(item, "blorqueScript_BSImport", None)
                    
                    if opp_val == self:
                        setattr(item, "blorqueScript_BSImport", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "blorqueScript_BSImport"):
                    opp_val = getattr(item, "blorqueScript_BSImport", None)
                    
                    setattr(item, "blorqueScript_BSImport", self)
                    

    @property
    def blorqueScript_BSFile2(self):
        return self.__blorqueScript_BSFile2

    @blorqueScript_BSFile2.setter
    def blorqueScript_BSFile2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_blorqueScript_BSFile__blorqueScript_BSFile2", None)
        self.__blorqueScript_BSFile2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "blorqueScript_BSClass"):
                    opp_val = getattr(item, "blorqueScript_BSClass", None)
                    
                    if opp_val == self:
                        setattr(item, "blorqueScript_BSClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "blorqueScript_BSClass"):
                    opp_val = getattr(item, "blorqueScript_BSClass", None)
                    
                    setattr(item, "blorqueScript_BSClass", self)
                    

class blorqueScript_BSMember(BSSymbol):

    def __init__(self, isArray: bool, blorqueScript_BSMember: "blorqueScript_BSClass" = None):
        self.isArray = isArray
        self.blorqueScript_BSMember = blorqueScript_BSMember
        
    @property
    def isArray(self) -> bool:
        return self.__isArray

    @isArray.setter
    def isArray(self, isArray: bool):
        self.__isArray = isArray

    @property
    def blorqueScript_BSMember(self):
        return self.__blorqueScript_BSMember

    @blorqueScript_BSMember.setter
    def blorqueScript_BSMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_blorqueScript_BSMember__blorqueScript_BSMember", None)
        self.__blorqueScript_BSMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blorqueScript_BSClass7"):
                opp_val = getattr(old_value, "blorqueScript_BSClass7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blorqueScript_BSClass7"):
                opp_val = getattr(value, "blorqueScript_BSClass7", None)
                if opp_val is None:
                    setattr(value, "blorqueScript_BSClass7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
