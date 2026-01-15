from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AssignmentOperator(Enum):
    assign = "assign"
    multAssign = "multAssign"
    divAssign = "divAssign"
    modAssign = "modAssign"
    addAssign = "addAssign"
    subAssign = "subAssign"
    leftShiftAssign = "leftShiftAssign"
    rightShiftAssign = "rightShiftAssign"
    andAssign = "andAssign"
    xorAssign = "xorAssign"
    orAssign = "orAssign"
class ShiftOperator(Enum):
    left = "left"
    right = "right"
class UnaryOperator(Enum):
    positive = "positive"
    negative = "negative"
    complement = "complement"
class AdditiveOperator(Enum):
    plus = "plus"
    minus = "minus"
class RelationalOperator(Enum):
    smaller = "smaller"
    smallerEqual = "smallerEqual"
    greater = "greater"
    greaterEqual = "greaterEqual"
    equals = "equals"
    notEquals = "notEquals"
class LogicalOperator(Enum):
    and = "and"
    or = "or"
    not = "not"
class BitwiseOperator(Enum):
    xor = "xor"
    and = "and"
    or = "or"
class MultiplicativeOperator(Enum):
    mul = "mul"
    div = "div"
    mod = "mod"


############################################
# Definition of Classes
############################################

class expressions_Type:

    pass
class expressions_EObject:

    pass
class ArgumentExpression:

    pass
class expressions_ElementReferenceExpression(ArgumentExpression):

    def __init__(self, operationCall: bool, arrayAccess: bool, expressions_ElementReferenceExpression32: set["expressions_Expression"] = None, expressions_ElementReferenceExpression: "expressions_EObject" = None):
        self.operationCall = operationCall
        self.arrayAccess = arrayAccess
        self.expressions_ElementReferenceExpression32 = expressions_ElementReferenceExpression32 if expressions_ElementReferenceExpression32 is not None else set()
        self.expressions_ElementReferenceExpression = expressions_ElementReferenceExpression
        
    @property
    def operationCall(self) -> bool:
        return self.__operationCall

    @operationCall.setter
    def operationCall(self, operationCall: bool):
        self.__operationCall = operationCall

    @property
    def arrayAccess(self) -> bool:
        return self.__arrayAccess

    @arrayAccess.setter
    def arrayAccess(self, arrayAccess: bool):
        self.__arrayAccess = arrayAccess

    @property
    def expressions_ElementReferenceExpression(self):
        return self.__expressions_ElementReferenceExpression

    @expressions_ElementReferenceExpression.setter
    def expressions_ElementReferenceExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_ElementReferenceExpression__expressions_ElementReferenceExpression", None)
        self.__expressions_ElementReferenceExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_EObject30"):
                opp_val = getattr(old_value, "expressions_EObject30", None)
                if opp_val == self:
                    setattr(old_value, "expressions_EObject30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_EObject30"):
                opp_val = getattr(value, "expressions_EObject30", None)
                setattr(value, "expressions_EObject30", self)

    @property
    def expressions_ElementReferenceExpression32(self):
        return self.__expressions_ElementReferenceExpression32

    @expressions_ElementReferenceExpression32.setter
    def expressions_ElementReferenceExpression32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_ElementReferenceExpression__expressions_ElementReferenceExpression32", None)
        self.__expressions_ElementReferenceExpression32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "expressions_Expression33"):
                    opp_val = getattr(item, "expressions_Expression33", None)
                    
                    if opp_val == self:
                        setattr(item, "expressions_Expression33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "expressions_Expression33"):
                    opp_val = getattr(item, "expressions_Expression33", None)
                    
                    setattr(item, "expressions_Expression33", self)
                    

class expressions_FeatureCall(ArgumentExpression):

    def __init__(self, operationCall: bool, arrayAccess: bool, expressions_FeatureCall: "expressions_Expression" = None, expressions_FeatureCall25: "expressions_EObject" = None, expressions_FeatureCall27: set["expressions_Expression"] = None):
        self.operationCall = operationCall
        self.arrayAccess = arrayAccess
        self.expressions_FeatureCall = expressions_FeatureCall
        self.expressions_FeatureCall25 = expressions_FeatureCall25
        self.expressions_FeatureCall27 = expressions_FeatureCall27 if expressions_FeatureCall27 is not None else set()
        
    @property
    def operationCall(self) -> bool:
        return self.__operationCall

    @operationCall.setter
    def operationCall(self, operationCall: bool):
        self.__operationCall = operationCall

    @property
    def arrayAccess(self) -> bool:
        return self.__arrayAccess

    @arrayAccess.setter
    def arrayAccess(self, arrayAccess: bool):
        self.__arrayAccess = arrayAccess

    @property
    def expressions_FeatureCall27(self):
        return self.__expressions_FeatureCall27

    @expressions_FeatureCall27.setter
    def expressions_FeatureCall27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_FeatureCall__expressions_FeatureCall27", None)
        self.__expressions_FeatureCall27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "expressions_Expression28"):
                    opp_val = getattr(item, "expressions_Expression28", None)
                    
                    if opp_val == self:
                        setattr(item, "expressions_Expression28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "expressions_Expression28"):
                    opp_val = getattr(item, "expressions_Expression28", None)
                    
                    setattr(item, "expressions_Expression28", self)
                    

    @property
    def expressions_FeatureCall25(self):
        return self.__expressions_FeatureCall25

    @expressions_FeatureCall25.setter
    def expressions_FeatureCall25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_FeatureCall__expressions_FeatureCall25", None)
        self.__expressions_FeatureCall25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_EObject"):
                opp_val = getattr(old_value, "expressions_EObject", None)
                if opp_val == self:
                    setattr(old_value, "expressions_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_EObject"):
                opp_val = getattr(value, "expressions_EObject", None)
                setattr(value, "expressions_EObject", self)

    @property
    def expressions_FeatureCall(self):
        return self.__expressions_FeatureCall

    @expressions_FeatureCall.setter
    def expressions_FeatureCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_FeatureCall__expressions_FeatureCall", None)
        self.__expressions_FeatureCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_Expression23"):
                opp_val = getattr(old_value, "expressions_Expression23", None)
                if opp_val == self:
                    setattr(old_value, "expressions_Expression23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_Expression23"):
                opp_val = getattr(value, "expressions_Expression23", None)
                setattr(value, "expressions_Expression23", self)

class UnaryExpression:

    pass
class expressions_NumericalUnaryExpression(UnaryExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class expressions_LogicalNotExpression(UnaryExpression):

    pass
class BinaryExpression:

    pass
class expressions_BitwiseXorExpression(BinaryExpression):

    pass
class expressions_LogicalAndExpression(BinaryExpression):

    pass
class expressions_BitwiseOrExpression(BinaryExpression):

    pass
class expressions_ShiftExpression(BinaryExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class expressions_LogicalRelationExpression(BinaryExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class expressions_NumericalMultiplyDivideExpression(BinaryExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class expressions_BitwiseAndExpression(BinaryExpression):

    pass
class expressions_NumericalAddSubtractExpression(BinaryExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class expressions_LogicalOrExpression(BinaryExpression):

    pass
class Literal:

    pass
class expressions_BoolLiteral(Literal):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class expressions_Literal(ABC):

    pass
class expressions_NullLiteral(Literal):

    pass
class expressions_StringLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class expressions_HexLiteral(Literal):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class expressions_FloatLiteral(Literal):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class expressions_DoubleLiteral(Literal):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class expressions_IntLiteral(Literal):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class Expression:

    pass
class expressions_PrimitiveValueExpression(Expression):

    pass
class expressions_ArgumentExpression(Expression):

    pass
class expressions_ConditionalExpression(Expression):

    pass
class expressions_UnaryExpression(Expression):

    def __init__(self, expressions_UnaryExpression: "expressions_Expression" = None):
        self.expressions_UnaryExpression = expressions_UnaryExpression
        
    @property
    def expressions_UnaryExpression(self):
        return self.__expressions_UnaryExpression

    @expressions_UnaryExpression.setter
    def expressions_UnaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_UnaryExpression__expressions_UnaryExpression", None)
        self.__expressions_UnaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_Expression5"):
                opp_val = getattr(old_value, "expressions_Expression5", None)
                if opp_val == self:
                    setattr(old_value, "expressions_Expression5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_Expression5"):
                opp_val = getattr(value, "expressions_Expression5", None)
                setattr(value, "expressions_Expression5", self)

    def getOperator(self) -> str:
        # TODO: Implement getOperator method
        pass

class expressions_ParenthesizedExpression(Expression):

    pass
class expressions_TypeCastExpression(Expression):

    pass
class expressions_AssignmentExpression(Expression):

    def __init__(self, operator: str, expressions_AssignmentExpression: "expressions_Expression" = None, expressions_AssignmentExpression11: "expressions_Expression" = None):
        self.operator = operator
        self.expressions_AssignmentExpression = expressions_AssignmentExpression
        self.expressions_AssignmentExpression11 = expressions_AssignmentExpression11
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def expressions_AssignmentExpression11(self):
        return self.__expressions_AssignmentExpression11

    @expressions_AssignmentExpression11.setter
    def expressions_AssignmentExpression11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_AssignmentExpression__expressions_AssignmentExpression11", None)
        self.__expressions_AssignmentExpression11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_Expression12"):
                opp_val = getattr(old_value, "expressions_Expression12", None)
                if opp_val == self:
                    setattr(old_value, "expressions_Expression12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_Expression12"):
                opp_val = getattr(value, "expressions_Expression12", None)
                setattr(value, "expressions_Expression12", self)

    @property
    def expressions_AssignmentExpression(self):
        return self.__expressions_AssignmentExpression

    @expressions_AssignmentExpression.setter
    def expressions_AssignmentExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_AssignmentExpression__expressions_AssignmentExpression", None)
        self.__expressions_AssignmentExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_Expression9"):
                opp_val = getattr(old_value, "expressions_Expression9", None)
                if opp_val == self:
                    setattr(old_value, "expressions_Expression9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_Expression9"):
                opp_val = getattr(value, "expressions_Expression9", None)
                setattr(value, "expressions_Expression9", self)

class expressions_BinaryExpression(Expression):

    def __init__(self, expressions_BinaryExpression: "expressions_Expression" = None, expressions_BinaryExpression2: "expressions_Expression" = None):
        self.expressions_BinaryExpression = expressions_BinaryExpression
        self.expressions_BinaryExpression2 = expressions_BinaryExpression2
        
    @property
    def expressions_BinaryExpression2(self):
        return self.__expressions_BinaryExpression2

    @expressions_BinaryExpression2.setter
    def expressions_BinaryExpression2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_BinaryExpression__expressions_BinaryExpression2", None)
        self.__expressions_BinaryExpression2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_Expression3"):
                opp_val = getattr(old_value, "expressions_Expression3", None)
                if opp_val == self:
                    setattr(old_value, "expressions_Expression3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_Expression3"):
                opp_val = getattr(value, "expressions_Expression3", None)
                setattr(value, "expressions_Expression3", self)

    @property
    def expressions_BinaryExpression(self):
        return self.__expressions_BinaryExpression

    @expressions_BinaryExpression.setter
    def expressions_BinaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_BinaryExpression__expressions_BinaryExpression", None)
        self.__expressions_BinaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_Expression"):
                opp_val = getattr(old_value, "expressions_Expression", None)
                if opp_val == self:
                    setattr(old_value, "expressions_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_Expression"):
                opp_val = getattr(value, "expressions_Expression", None)
                setattr(value, "expressions_Expression", self)

    def getOperator(self) -> str:
        # TODO: Implement getOperator method
        pass

class expressions_Expression(ABC):

    pass