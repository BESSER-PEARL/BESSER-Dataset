from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ShiftOperator(Enum):
    left = "left"
    right = "right"
class UnaryOperator(Enum):
    positive = "positive"
    negative = "negative"
    complement = "complement"
    not_ = "not_"
class EqualityOperator(Enum):
    equals = "equals"
    notEquals = "notEquals"
class AdditiveOperator(Enum):
    plus = "plus"
    minus = "minus"
class TimeUnit(Enum):
    second = "second"
    millisecond = "millisecond"
    nanosecond = "nanosecond"
class AssignmentOperator(Enum):
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
    assign = "assign"
class MultiplicativeOperator(Enum):
    mul = "mul"
    div = "div"
    mod = "mod"
class RelationalOperator(Enum):
    smaller = "smaller"
    greater = "greater"
    smallerEqual = "smallerEqual"
    greaterEqual = "greaterEqual"


############################################
# Definition of Classes
############################################

class statechartexpressions_PrimaryExpression:

    pass
class statechartexpressions_MultiplicativeExpression:

    def __init__(self, operator: str, statechartexpressions_MultiplicativeExpression66: "statechartexpressions_AdditiveExpression" = None, statechartexpressions_MultiplicativeExpression68: "statechartexpressions_UnaryExpression" = None, statechartexpressions_MultiplicativeExpression70: "statechartexpressions_UnaryExpression" = None, statechartexpressions_MultiplicativeExpression: "statechartexpressions_AdditiveExpression" = None):
        self.operator = operator
        self.statechartexpressions_MultiplicativeExpression66 = statechartexpressions_MultiplicativeExpression66
        self.statechartexpressions_MultiplicativeExpression68 = statechartexpressions_MultiplicativeExpression68
        self.statechartexpressions_MultiplicativeExpression70 = statechartexpressions_MultiplicativeExpression70
        self.statechartexpressions_MultiplicativeExpression = statechartexpressions_MultiplicativeExpression
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def statechartexpressions_MultiplicativeExpression(self):
        return self.__statechartexpressions_MultiplicativeExpression

    @statechartexpressions_MultiplicativeExpression.setter
    def statechartexpressions_MultiplicativeExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechartexpressions_MultiplicativeExpression__statechartexpressions_MultiplicativeExpression", None)
        self.__statechartexpressions_MultiplicativeExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechartexpressions_AdditiveExpression63"):
                opp_val = getattr(old_value, "statechartexpressions_AdditiveExpression63", None)
                if opp_val == self:
                    setattr(old_value, "statechartexpressions_AdditiveExpression63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechartexpressions_AdditiveExpression63"):
                opp_val = getattr(value, "statechartexpressions_AdditiveExpression63", None)
                setattr(value, "statechartexpressions_AdditiveExpression63", self)

    @property
    def statechartexpressions_MultiplicativeExpression68(self):
        return self.__statechartexpressions_MultiplicativeExpression68

    @statechartexpressions_MultiplicativeExpression68.setter
    def statechartexpressions_MultiplicativeExpression68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechartexpressions_MultiplicativeExpression__statechartexpressions_MultiplicativeExpression68", None)
        self.__statechartexpressions_MultiplicativeExpression68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechartexpressions_UnaryExpression"):
                opp_val = getattr(old_value, "statechartexpressions_UnaryExpression", None)
                if opp_val == self:
                    setattr(old_value, "statechartexpressions_UnaryExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechartexpressions_UnaryExpression"):
                opp_val = getattr(value, "statechartexpressions_UnaryExpression", None)
                setattr(value, "statechartexpressions_UnaryExpression", self)

    @property
    def statechartexpressions_MultiplicativeExpression66(self):
        return self.__statechartexpressions_MultiplicativeExpression66

    @statechartexpressions_MultiplicativeExpression66.setter
    def statechartexpressions_MultiplicativeExpression66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechartexpressions_MultiplicativeExpression__statechartexpressions_MultiplicativeExpression66", None)
        self.__statechartexpressions_MultiplicativeExpression66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechartexpressions_AdditiveExpression65"):
                opp_val = getattr(old_value, "statechartexpressions_AdditiveExpression65", None)
                if opp_val == self:
                    setattr(old_value, "statechartexpressions_AdditiveExpression65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechartexpressions_AdditiveExpression65"):
                opp_val = getattr(value, "statechartexpressions_AdditiveExpression65", None)
                setattr(value, "statechartexpressions_AdditiveExpression65", self)

    @property
    def statechartexpressions_MultiplicativeExpression70(self):
        return self.__statechartexpressions_MultiplicativeExpression70

    @statechartexpressions_MultiplicativeExpression70.setter
    def statechartexpressions_MultiplicativeExpression70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechartexpressions_MultiplicativeExpression__statechartexpressions_MultiplicativeExpression70", None)
        self.__statechartexpressions_MultiplicativeExpression70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechartexpressions_UnaryExpression71"):
                opp_val = getattr(old_value, "statechartexpressions_UnaryExpression71", None)
                if opp_val == self:
                    setattr(old_value, "statechartexpressions_UnaryExpression71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechartexpressions_UnaryExpression71"):
                opp_val = getattr(value, "statechartexpressions_UnaryExpression71", None)
                setattr(value, "statechartexpressions_UnaryExpression71", self)

class statechartexpressions_UnaryExpression:

    def __init__(self, operator: str, statechartexpressions_UnaryExpression: "statechartexpressions_MultiplicativeExpression" = None, statechartexpressions_UnaryExpression71: "statechartexpressions_MultiplicativeExpression" = None, statechartexpressions_UnaryExpression73: "statechartexpressions_PrimaryExpression" = None):
        self.operator = operator
        self.statechartexpressions_UnaryExpression = statechartexpressions_UnaryExpression
        self.statechartexpressions_UnaryExpression71 = statechartexpressions_UnaryExpression71
        self.statechartexpressions_UnaryExpression73 = statechartexpressions_UnaryExpression73
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def statechartexpressions_UnaryExpression71(self):
        return self.__statechartexpressions_UnaryExpression71

    @statechartexpressions_UnaryExpression71.setter
    def statechartexpressions_UnaryExpression71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechartexpressions_UnaryExpression__statechartexpressions_UnaryExpression71", None)
        self.__statechartexpressions_UnaryExpression71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechartexpressions_MultiplicativeExpression70"):
                opp_val = getattr(old_value, "statechartexpressions_MultiplicativeExpression70", None)
                if opp_val == self:
                    setattr(old_value, "statechartexpressions_MultiplicativeExpression70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechartexpressions_MultiplicativeExpression70"):
                opp_val = getattr(value, "statechartexpressions_MultiplicativeExpression70", None)
                setattr(value, "statechartexpressions_MultiplicativeExpression70", self)

    @property
    def statechartexpressions_UnaryExpression73(self):
        return self.__statechartexpressions_UnaryExpression73

    @statechartexpressions_UnaryExpression73.setter
    def statechartexpressions_UnaryExpression73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechartexpressions_UnaryExpression__statechartexpressions_UnaryExpression73", None)
        self.__statechartexpressions_UnaryExpression73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechartexpressions_PrimaryExpression"):
                opp_val = getattr(old_value, "statechartexpressions_PrimaryExpression", None)
                if opp_val == self:
                    setattr(old_value, "statechartexpressions_PrimaryExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechartexpressions_PrimaryExpression"):
                opp_val = getattr(value, "statechartexpressions_PrimaryExpression", None)
                setattr(value, "statechartexpressions_PrimaryExpression", self)

    @property
    def statechartexpressions_UnaryExpression(self):
        return self.__statechartexpressions_UnaryExpression

    @statechartexpressions_UnaryExpression.setter
    def statechartexpressions_UnaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechartexpressions_UnaryExpression__statechartexpressions_UnaryExpression", None)
        self.__statechartexpressions_UnaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechartexpressions_MultiplicativeExpression68"):
                opp_val = getattr(old_value, "statechartexpressions_MultiplicativeExpression68", None)
                if opp_val == self:
                    setattr(old_value, "statechartexpressions_MultiplicativeExpression68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechartexpressions_MultiplicativeExpression68"):
                opp_val = getattr(value, "statechartexpressions_MultiplicativeExpression68", None)
                setattr(value, "statechartexpressions_MultiplicativeExpression68", self)

class statechartexpressions_AdditiveExpression:

    def __init__(self, operator: str, statechartexpressions_AdditiveExpression: "statechartexpressions_ShiftExpression" = None, statechartexpressions_AdditiveExpression65: "statechartexpressions_MultiplicativeExpression" = None, statechartexpressions_AdditiveExpression61: "statechartexpressions_ShiftExpression" = None, statechartexpressions_AdditiveExpression63: "statechartexpressions_MultiplicativeExpression" = None):
        self.operator = operator
        self.statechartexpressions_AdditiveExpression = statechartexpressions_AdditiveExpression
        self.statechartexpressions_AdditiveExpression65 = statechartexpressions_AdditiveExpression65
        self.statechartexpressions_AdditiveExpression61 = statechartexpressions_AdditiveExpression61
        self.statechartexpressions_AdditiveExpression63 = statechartexpressions_AdditiveExpression63
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def statechartexpressions_AdditiveExpression63(self):
        return self.__statechartexpressions_AdditiveExpression63

    @statechartexpressions_AdditiveExpression63.setter
    def statechartexpressions_AdditiveExpression63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechartexpressions_AdditiveExpression__statechartexpressions_AdditiveExpression63", None)
        self.__statechartexpressions_AdditiveExpression63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechartexpressions_MultiplicativeExpression"):
                opp_val = getattr(old_value, "statechartexpressions_MultiplicativeExpression", None)
                if opp_val == self:
                    setattr(old_value, "statechartexpressions_MultiplicativeExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechartexpressions_MultiplicativeExpression"):
                opp_val = getattr(value, "statechartexpressions_MultiplicativeExpression", None)
                setattr(value, "statechartexpressions_MultiplicativeExpression", self)

    @property
    def statechartexpressions_AdditiveExpression61(self):
        return self.__statechartexpressions_AdditiveExpression61

    @statechartexpressions_AdditiveExpression61.setter
    def statechartexpressions_AdditiveExpression61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechartexpressions_AdditiveExpression__statechartexpressions_AdditiveExpression61", None)
        self.__statechartexpressions_AdditiveExpression61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechartexpressions_ShiftExpression60"):
                opp_val = getattr(old_value, "statechartexpressions_ShiftExpression60", None)
                if opp_val == self:
                    setattr(old_value, "statechartexpressions_ShiftExpression60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechartexpressions_ShiftExpression60"):
                opp_val = getattr(value, "statechartexpressions_ShiftExpression60", None)
                setattr(value, "statechartexpressions_ShiftExpression60", self)

    @property
    def statechartexpressions_AdditiveExpression65(self):
        return self.__statechartexpressions_AdditiveExpression65

    @statechartexpressions_AdditiveExpression65.setter
    def statechartexpressions_AdditiveExpression65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechartexpressions_AdditiveExpression__statechartexpressions_AdditiveExpression65", None)
        self.__statechartexpressions_AdditiveExpression65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechartexpressions_MultiplicativeExpression66"):
                opp_val = getattr(old_value, "statechartexpressions_MultiplicativeExpression66", None)
                if opp_val == self:
                    setattr(old_value, "statechartexpressions_MultiplicativeExpression66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechartexpressions_MultiplicativeExpression66"):
                opp_val = getattr(value, "statechartexpressions_MultiplicativeExpression66", None)
                setattr(value, "statechartexpressions_MultiplicativeExpression66", self)

    @property
    def statechartexpressions_AdditiveExpression(self):
        return self.__statechartexpressions_AdditiveExpression

    @statechartexpressions_AdditiveExpression.setter
    def statechartexpressions_AdditiveExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechartexpressions_AdditiveExpression__statechartexpressions_AdditiveExpression", None)
        self.__statechartexpressions_AdditiveExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechartexpressions_ShiftExpression58"):
                opp_val = getattr(old_value, "statechartexpressions_ShiftExpression58", None)
                if opp_val == self:
                    setattr(old_value, "statechartexpressions_ShiftExpression58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechartexpressions_ShiftExpression58"):
                opp_val = getattr(value, "statechartexpressions_ShiftExpression58", None)
                setattr(value, "statechartexpressions_ShiftExpression58", self)

class statechartexpressions_EqualityExpression:

    def __init__(self, operator: str, statechartexpressions_EqualityExpression39: "statechartexpressions_RelationalExpression" = None, statechartexpressions_EqualityExpression41: "statechartexpressions_RelationalExpression" = None, statechartexpressions_EqualityExpression: "statechartexpressions_BitwiseAndExpression" = None, statechartexpressions_EqualityExpression37: "statechartexpressions_BitwiseAndExpression" = None):
        self.operator = operator
        self.statechartexpressions_EqualityExpression39 = statechartexpressions_EqualityExpression39
        self.statechartexpressions_EqualityExpression41 = statechartexpressions_EqualityExpression41
        self.statechartexpressions_EqualityExpression = statechartexpressions_EqualityExpression
        self.statechartexpressions_EqualityExpression37 = statechartexpressions_EqualityExpression37
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def statechartexpressions_EqualityExpression37(self):
        return self.__statechartexpressions_EqualityExpression37

    @statechartexpressions_EqualityExpression37.setter
    def statechartexpressions_EqualityExpression37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechartexpressions_EqualityExpression__statechartexpressions_EqualityExpression37", None)
        self.__statechartexpressions_EqualityExpression37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechartexpressions_BitwiseAndExpression36"):
                opp_val = getattr(old_value, "statechartexpressions_BitwiseAndExpression36", None)
                if opp_val == self:
                    setattr(old_value, "statechartexpressions_BitwiseAndExpression36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechartexpressions_BitwiseAndExpression36"):
                opp_val = getattr(value, "statechartexpressions_BitwiseAndExpression36", None)
                setattr(value, "statechartexpressions_BitwiseAndExpression36", self)

    @property
    def statechartexpressions_EqualityExpression41(self):
        return self.__statechartexpressions_EqualityExpression41

    @statechartexpressions_EqualityExpression41.setter
    def statechartexpressions_EqualityExpression41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechartexpressions_EqualityExpression__statechartexpressions_EqualityExpression41", None)
        self.__statechartexpressions_EqualityExpression41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechartexpressions_RelationalExpression42"):
                opp_val = getattr(old_value, "statechartexpressions_RelationalExpression42", None)
                if opp_val == self:
                    setattr(old_value, "statechartexpressions_RelationalExpression42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechartexpressions_RelationalExpression42"):
                opp_val = getattr(value, "statechartexpressions_RelationalExpression42", None)
                setattr(value, "statechartexpressions_RelationalExpression42", self)

    @property
    def statechartexpressions_EqualityExpression39(self):
        return self.__statechartexpressions_EqualityExpression39

    @statechartexpressions_EqualityExpression39.setter
    def statechartexpressions_EqualityExpression39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechartexpressions_EqualityExpression__statechartexpressions_EqualityExpression39", None)
        self.__statechartexpressions_EqualityExpression39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechartexpressions_RelationalExpression"):
                opp_val = getattr(old_value, "statechartexpressions_RelationalExpression", None)
                if opp_val == self:
                    setattr(old_value, "statechartexpressions_RelationalExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechartexpressions_RelationalExpression"):
                opp_val = getattr(value, "statechartexpressions_RelationalExpression", None)
                setattr(value, "statechartexpressions_RelationalExpression", self)

    @property
    def statechartexpressions_EqualityExpression(self):
        return self.__statechartexpressions_EqualityExpression

    @statechartexpressions_EqualityExpression.setter
    def statechartexpressions_EqualityExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechartexpressions_EqualityExpression__statechartexpressions_EqualityExpression", None)
        self.__statechartexpressions_EqualityExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechartexpressions_BitwiseAndExpression34"):
                opp_val = getattr(old_value, "statechartexpressions_BitwiseAndExpression34", None)
                if opp_val == self:
                    setattr(old_value, "statechartexpressions_BitwiseAndExpression34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechartexpressions_BitwiseAndExpression34"):
                opp_val = getattr(value, "statechartexpressions_BitwiseAndExpression34", None)
                setattr(value, "statechartexpressions_BitwiseAndExpression34", self)

class statechartexpressions_ShiftExpression:

    def __init__(self, operator: str, statechartexpressions_ShiftExpression53: "statechartexpressions_ConditionalExpression" = None, statechartexpressions_ShiftExpression56: "statechartexpressions_ConditionalExpression" = None, statechartexpressions_ShiftExpression58: "statechartexpressions_AdditiveExpression" = None, statechartexpressions_ShiftExpression: "statechartexpressions_RelationalExpression" = None, statechartexpressions_ShiftExpression47: "statechartexpressions_RelationalExpression" = None, statechartexpressions_ShiftExpression60: "statechartexpressions_AdditiveExpression" = None):
        self.operator = operator
        self.statechartexpressions_ShiftExpression53 = statechartexpressions_ShiftExpression53
        self.statechartexpressions_ShiftExpression56 = statechartexpressions_ShiftExpression56
        self.statechartexpressions_ShiftExpression58 = statechartexpressions_ShiftExpression58
        self.statechartexpressions_ShiftExpression = statechartexpressions_ShiftExpression
        self.statechartexpressions_ShiftExpression47 = statechartexpressions_ShiftExpression47
        self.statechartexpressions_ShiftExpression60 = statechartexpressions_ShiftExpression60
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def statechartexpressions_ShiftExpression47(self):
        return self.__statechartexpressions_ShiftExpression47

    @statechartexpressions_ShiftExpression47.setter
    def statechartexpressions_ShiftExpression47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechartexpressions_ShiftExpression__statechartexpressions_ShiftExpression47", None)
        self.__statechartexpressions_ShiftExpression47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechartexpressions_RelationalExpression46"):
                opp_val = getattr(old_value, "statechartexpressions_RelationalExpression46", None)
                if opp_val == self:
                    setattr(old_value, "statechartexpressions_RelationalExpression46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechartexpressions_RelationalExpression46"):
                opp_val = getattr(value, "statechartexpressions_RelationalExpression46", None)
                setattr(value, "statechartexpressions_RelationalExpression46", self)

    @property
    def statechartexpressions_ShiftExpression60(self):
        return self.__statechartexpressions_ShiftExpression60

    @statechartexpressions_ShiftExpression60.setter
    def statechartexpressions_ShiftExpression60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechartexpressions_ShiftExpression__statechartexpressions_ShiftExpression60", None)
        self.__statechartexpressions_ShiftExpression60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechartexpressions_AdditiveExpression61"):
                opp_val = getattr(old_value, "statechartexpressions_AdditiveExpression61", None)
                if opp_val == self:
                    setattr(old_value, "statechartexpressions_AdditiveExpression61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechartexpressions_AdditiveExpression61"):
                opp_val = getattr(value, "statechartexpressions_AdditiveExpression61", None)
                setattr(value, "statechartexpressions_AdditiveExpression61", self)

    @property
    def statechartexpressions_ShiftExpression58(self):
        return self.__statechartexpressions_ShiftExpression58

    @statechartexpressions_ShiftExpression58.setter
    def statechartexpressions_ShiftExpression58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechartexpressions_ShiftExpression__statechartexpressions_ShiftExpression58", None)
        self.__statechartexpressions_ShiftExpression58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechartexpressions_AdditiveExpression"):
                opp_val = getattr(old_value, "statechartexpressions_AdditiveExpression", None)
                if opp_val == self:
                    setattr(old_value, "statechartexpressions_AdditiveExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechartexpressions_AdditiveExpression"):
                opp_val = getattr(value, "statechartexpressions_AdditiveExpression", None)
                setattr(value, "statechartexpressions_AdditiveExpression", self)

    @property
    def statechartexpressions_ShiftExpression(self):
        return self.__statechartexpressions_ShiftExpression

    @statechartexpressions_ShiftExpression.setter
    def statechartexpressions_ShiftExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechartexpressions_ShiftExpression__statechartexpressions_ShiftExpression", None)
        self.__statechartexpressions_ShiftExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechartexpressions_RelationalExpression44"):
                opp_val = getattr(old_value, "statechartexpressions_RelationalExpression44", None)
                if opp_val == self:
                    setattr(old_value, "statechartexpressions_RelationalExpression44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechartexpressions_RelationalExpression44"):
                opp_val = getattr(value, "statechartexpressions_RelationalExpression44", None)
                setattr(value, "statechartexpressions_RelationalExpression44", self)

    @property
    def statechartexpressions_ShiftExpression53(self):
        return self.__statechartexpressions_ShiftExpression53

    @statechartexpressions_ShiftExpression53.setter
    def statechartexpressions_ShiftExpression53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechartexpressions_ShiftExpression__statechartexpressions_ShiftExpression53", None)
        self.__statechartexpressions_ShiftExpression53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechartexpressions_ConditionalExpression52"):
                opp_val = getattr(old_value, "statechartexpressions_ConditionalExpression52", None)
                if opp_val == self:
                    setattr(old_value, "statechartexpressions_ConditionalExpression52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechartexpressions_ConditionalExpression52"):
                opp_val = getattr(value, "statechartexpressions_ConditionalExpression52", None)
                setattr(value, "statechartexpressions_ConditionalExpression52", self)

    @property
    def statechartexpressions_ShiftExpression56(self):
        return self.__statechartexpressions_ShiftExpression56

    @statechartexpressions_ShiftExpression56.setter
    def statechartexpressions_ShiftExpression56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechartexpressions_ShiftExpression__statechartexpressions_ShiftExpression56", None)
        self.__statechartexpressions_ShiftExpression56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechartexpressions_ConditionalExpression55"):
                opp_val = getattr(old_value, "statechartexpressions_ConditionalExpression55", None)
                if opp_val == self:
                    setattr(old_value, "statechartexpressions_ConditionalExpression55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechartexpressions_ConditionalExpression55"):
                opp_val = getattr(value, "statechartexpressions_ConditionalExpression55", None)
                setattr(value, "statechartexpressions_ConditionalExpression55", self)

class statechartexpressions_RelationalExpression:

    def __init__(self, operator: str, statechartexpressions_RelationalExpression: "statechartexpressions_EqualityExpression" = None, statechartexpressions_RelationalExpression42: "statechartexpressions_EqualityExpression" = None, statechartexpressions_RelationalExpression44: "statechartexpressions_ShiftExpression" = None, statechartexpressions_RelationalExpression46: "statechartexpressions_ShiftExpression" = None):
        self.operator = operator
        self.statechartexpressions_RelationalExpression = statechartexpressions_RelationalExpression
        self.statechartexpressions_RelationalExpression42 = statechartexpressions_RelationalExpression42
        self.statechartexpressions_RelationalExpression44 = statechartexpressions_RelationalExpression44
        self.statechartexpressions_RelationalExpression46 = statechartexpressions_RelationalExpression46
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def statechartexpressions_RelationalExpression46(self):
        return self.__statechartexpressions_RelationalExpression46

    @statechartexpressions_RelationalExpression46.setter
    def statechartexpressions_RelationalExpression46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechartexpressions_RelationalExpression__statechartexpressions_RelationalExpression46", None)
        self.__statechartexpressions_RelationalExpression46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechartexpressions_ShiftExpression47"):
                opp_val = getattr(old_value, "statechartexpressions_ShiftExpression47", None)
                if opp_val == self:
                    setattr(old_value, "statechartexpressions_ShiftExpression47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechartexpressions_ShiftExpression47"):
                opp_val = getattr(value, "statechartexpressions_ShiftExpression47", None)
                setattr(value, "statechartexpressions_ShiftExpression47", self)

    @property
    def statechartexpressions_RelationalExpression42(self):
        return self.__statechartexpressions_RelationalExpression42

    @statechartexpressions_RelationalExpression42.setter
    def statechartexpressions_RelationalExpression42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechartexpressions_RelationalExpression__statechartexpressions_RelationalExpression42", None)
        self.__statechartexpressions_RelationalExpression42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechartexpressions_EqualityExpression41"):
                opp_val = getattr(old_value, "statechartexpressions_EqualityExpression41", None)
                if opp_val == self:
                    setattr(old_value, "statechartexpressions_EqualityExpression41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechartexpressions_EqualityExpression41"):
                opp_val = getattr(value, "statechartexpressions_EqualityExpression41", None)
                setattr(value, "statechartexpressions_EqualityExpression41", self)

    @property
    def statechartexpressions_RelationalExpression44(self):
        return self.__statechartexpressions_RelationalExpression44

    @statechartexpressions_RelationalExpression44.setter
    def statechartexpressions_RelationalExpression44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechartexpressions_RelationalExpression__statechartexpressions_RelationalExpression44", None)
        self.__statechartexpressions_RelationalExpression44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechartexpressions_ShiftExpression"):
                opp_val = getattr(old_value, "statechartexpressions_ShiftExpression", None)
                if opp_val == self:
                    setattr(old_value, "statechartexpressions_ShiftExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechartexpressions_ShiftExpression"):
                opp_val = getattr(value, "statechartexpressions_ShiftExpression", None)
                setattr(value, "statechartexpressions_ShiftExpression", self)

    @property
    def statechartexpressions_RelationalExpression(self):
        return self.__statechartexpressions_RelationalExpression

    @statechartexpressions_RelationalExpression.setter
    def statechartexpressions_RelationalExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechartexpressions_RelationalExpression__statechartexpressions_RelationalExpression", None)
        self.__statechartexpressions_RelationalExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechartexpressions_EqualityExpression39"):
                opp_val = getattr(old_value, "statechartexpressions_EqualityExpression39", None)
                if opp_val == self:
                    setattr(old_value, "statechartexpressions_EqualityExpression39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechartexpressions_EqualityExpression39"):
                opp_val = getattr(value, "statechartexpressions_EqualityExpression39", None)
                setattr(value, "statechartexpressions_EqualityExpression39", self)

class statechartexpressions_BitwiseXorExpression:

    pass
class statechartexpressions_BooleanAndExpression:

    pass
class statechartexpressions_BitwiseAndExpression:

    pass
class statechartexpressions_BitwiseOrExpression:

    pass
class statechartexpressions_Procedure:

    def __init__(self, identifier: str, statechartexpressions_Procedure: "statechartexpressions_ProcedureCall" = None):
        self.identifier = identifier
        self.statechartexpressions_Procedure = statechartexpressions_Procedure
        
        pass
    @property
    def identifier(self):
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier


    @property
    def statechartexpressions_Procedure(self):
        return self.__statechartexpressions_Procedure

    @statechartexpressions_Procedure.setter
    def statechartexpressions_Procedure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechartexpressions_Procedure__statechartexpressions_Procedure", None)
        self.__statechartexpressions_Procedure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechartexpressions_ProcedureCall"):
                opp_val = getattr(old_value, "statechartexpressions_ProcedureCall", None)
                if opp_val == self:
                    setattr(old_value, "statechartexpressions_ProcedureCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechartexpressions_ProcedureCall"):
                opp_val = getattr(value, "statechartexpressions_ProcedureCall", None)
                setattr(value, "statechartexpressions_ProcedureCall", self)

class statechartexpressions_ConditionalExpression:

    pass
class statechartexpressions_Variable:

    def __init__(self, identifier: str, statechartexpressions_Variable: "statechartexpressions_VariableReference" = None):
        self.identifier = identifier
        self.statechartexpressions_Variable = statechartexpressions_Variable
        
        pass
    @property
    def identifier(self):
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier


    @property
    def statechartexpressions_Variable(self):
        return self.__statechartexpressions_Variable

    @statechartexpressions_Variable.setter
    def statechartexpressions_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechartexpressions_Variable__statechartexpressions_Variable", None)
        self.__statechartexpressions_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechartexpressions_VariableReference"):
                opp_val = getattr(old_value, "statechartexpressions_VariableReference", None)
                if opp_val == self:
                    setattr(old_value, "statechartexpressions_VariableReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechartexpressions_VariableReference"):
                opp_val = getattr(value, "statechartexpressions_VariableReference", None)
                setattr(value, "statechartexpressions_VariableReference", self)

class PrimaryExpression:

    pass
class statechartexpressions_NestedExpression(PrimaryExpression):

    pass
class statechartexpressions_LiteralValue(PrimaryExpression):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class TimeExpression:

    pass
class statechartexpressions_TimeConstant(TimeExpression):

    def __init__(self, value: int, unit: str):
        self.value = value
        self.unit = unit
        
        pass
    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class Statement:

    pass
class statechartexpressions_ProcedureCall(Statement):

    pass
class statechartexpressions_EventRaising(Statement):

    pass
class statechartexpressions_VariableAssignment(Statement):

    def __init__(self, operator: str, statechartexpressions_VariableAssignment: "statechartexpressions_VariableReference" = None, statechartexpressions_VariableAssignment10: "statechartexpressions_ConditionalExpression" = None):
        self.operator = operator
        self.statechartexpressions_VariableAssignment = statechartexpressions_VariableAssignment
        self.statechartexpressions_VariableAssignment10 = statechartexpressions_VariableAssignment10
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def statechartexpressions_VariableAssignment10(self):
        return self.__statechartexpressions_VariableAssignment10

    @statechartexpressions_VariableAssignment10.setter
    def statechartexpressions_VariableAssignment10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechartexpressions_VariableAssignment__statechartexpressions_VariableAssignment10", None)
        self.__statechartexpressions_VariableAssignment10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechartexpressions_ConditionalExpression"):
                opp_val = getattr(old_value, "statechartexpressions_ConditionalExpression", None)
                if opp_val == self:
                    setattr(old_value, "statechartexpressions_ConditionalExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechartexpressions_ConditionalExpression"):
                opp_val = getattr(value, "statechartexpressions_ConditionalExpression", None)
                setattr(value, "statechartexpressions_ConditionalExpression", self)

    @property
    def statechartexpressions_VariableAssignment(self):
        return self.__statechartexpressions_VariableAssignment

    @statechartexpressions_VariableAssignment.setter
    def statechartexpressions_VariableAssignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechartexpressions_VariableAssignment__statechartexpressions_VariableAssignment", None)
        self.__statechartexpressions_VariableAssignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechartexpressions_VariableReference8"):
                opp_val = getattr(old_value, "statechartexpressions_VariableReference8", None)
                if opp_val == self:
                    setattr(old_value, "statechartexpressions_VariableReference8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechartexpressions_VariableReference8"):
                opp_val = getattr(value, "statechartexpressions_VariableReference8", None)
                setattr(value, "statechartexpressions_VariableReference8", self)

class statechartexpressions_Event:

    pass
class statechartexpressions_Statement:

    pass
class statechartexpressions_VariableReference(TimeExpression, PrimaryExpression):

    pass
class statechartexpressions_TimeExpression:

    pass
class Event:

    pass
class statechartexpressions_TimeEvent(Event):

    pass
class statechartexpressions_SignalEvent(Event):

    def __init__(self, identifier: str, statechartexpressions_SignalEvent: "statechartexpressions_EventRaising" = None):
        self.identifier = identifier
        self.statechartexpressions_SignalEvent = statechartexpressions_SignalEvent
        
        pass
    @property
    def identifier(self):
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier


    @property
    def statechartexpressions_SignalEvent(self):
        return self.__statechartexpressions_SignalEvent

    @statechartexpressions_SignalEvent.setter
    def statechartexpressions_SignalEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechartexpressions_SignalEvent__statechartexpressions_SignalEvent", None)
        self.__statechartexpressions_SignalEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechartexpressions_EventRaising"):
                opp_val = getattr(old_value, "statechartexpressions_EventRaising", None)
                if opp_val == self:
                    setattr(old_value, "statechartexpressions_EventRaising", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechartexpressions_EventRaising"):
                opp_val = getattr(value, "statechartexpressions_EventRaising", None)
                setattr(value, "statechartexpressions_EventRaising", self)

class statechartexpressions_BooleanOrExpression:

    pass
class statechartexpressions_Trigger:

    pass
class Expression:

    pass
class statechartexpressions_GuardExpression(Expression):

    pass
class statechartexpressions_ActionExpression(Expression):

    pass
class statechartexpressions_TriggerExpression(Expression):

    pass
class statechartexpressions_Expression:

    pass