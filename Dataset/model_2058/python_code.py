from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class BooleanBinaryOperator(Enum):
    AND = "AND"
    OR = "OR"
class IntegerComparisonOperator(Enum):
    SMALLER = "SMALLER"
    SMALLER_EQUALS = "SMALLER_EQUALS"
    EQUALS = "EQUALS"
    GREATER_EQUALS = "GREATER_EQUALS"
    GREATER = "GREATER"
class BooleanUnaryOperator(Enum):
    NOT = "NOT"
class IntegerCalculationOperator(Enum):
    ADD = "ADD"
    SUBRACT = "SUBRACT"


############################################
# Definition of Classes
############################################

class activitydiagram_Offer:

    pass
class VariableAssignment:

    pass
class activitydiagram_BooleanVariableAssignment(VariableAssignment):

    def __init__(self, activitydiagram_BooleanVariableAssignment77: "activitydiagram_BooleanExpression" = None, activitydiagram_BooleanVariableAssignment: "activitydiagram_BooleanVariable" = None):
        self.activitydiagram_BooleanVariableAssignment77 = activitydiagram_BooleanVariableAssignment77
        self.activitydiagram_BooleanVariableAssignment = activitydiagram_BooleanVariableAssignment
        
    @property
    def activitydiagram_BooleanVariableAssignment(self):
        return self.__activitydiagram_BooleanVariableAssignment

    @activitydiagram_BooleanVariableAssignment.setter
    def activitydiagram_BooleanVariableAssignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanVariableAssignment__activitydiagram_BooleanVariableAssignment", None)
        self.__activitydiagram_BooleanVariableAssignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_BooleanVariable75"):
                opp_val = getattr(old_value, "activitydiagram_BooleanVariable75", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanVariable75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanVariable75"):
                opp_val = getattr(value, "activitydiagram_BooleanVariable75", None)
                setattr(value, "activitydiagram_BooleanVariable75", self)

    @property
    def activitydiagram_BooleanVariableAssignment77(self):
        return self.__activitydiagram_BooleanVariableAssignment77

    @activitydiagram_BooleanVariableAssignment77.setter
    def activitydiagram_BooleanVariableAssignment77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanVariableAssignment__activitydiagram_BooleanVariableAssignment77", None)
        self.__activitydiagram_BooleanVariableAssignment77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_BooleanExpression78"):
                opp_val = getattr(old_value, "activitydiagram_BooleanExpression78", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanExpression78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanExpression78"):
                opp_val = getattr(value, "activitydiagram_BooleanExpression78", None)
                setattr(value, "activitydiagram_BooleanExpression78", self)

    def execute(self):
        # TODO: Implement execute method
        pass

class activitydiagram_IntegerVariableAssignment(VariableAssignment):

    def __init__(self, activitydiagram_IntegerVariableAssignment: "activitydiagram_IntegerVariable" = None, activitydiagram_IntegerVariableAssignment81: "activitydiagram_IntegerExpression" = None):
        self.activitydiagram_IntegerVariableAssignment = activitydiagram_IntegerVariableAssignment
        self.activitydiagram_IntegerVariableAssignment81 = activitydiagram_IntegerVariableAssignment81
        
    @property
    def activitydiagram_IntegerVariableAssignment81(self):
        return self.__activitydiagram_IntegerVariableAssignment81

    @activitydiagram_IntegerVariableAssignment81.setter
    def activitydiagram_IntegerVariableAssignment81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_IntegerVariableAssignment__activitydiagram_IntegerVariableAssignment81", None)
        self.__activitydiagram_IntegerVariableAssignment81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_IntegerExpression82"):
                opp_val = getattr(old_value, "activitydiagram_IntegerExpression82", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_IntegerExpression82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_IntegerExpression82"):
                opp_val = getattr(value, "activitydiagram_IntegerExpression82", None)
                setattr(value, "activitydiagram_IntegerExpression82", self)

    @property
    def activitydiagram_IntegerVariableAssignment(self):
        return self.__activitydiagram_IntegerVariableAssignment

    @activitydiagram_IntegerVariableAssignment.setter
    def activitydiagram_IntegerVariableAssignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_IntegerVariableAssignment__activitydiagram_IntegerVariableAssignment", None)
        self.__activitydiagram_IntegerVariableAssignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_IntegerVariable"):
                opp_val = getattr(old_value, "activitydiagram_IntegerVariable", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_IntegerVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_IntegerVariable"):
                opp_val = getattr(value, "activitydiagram_IntegerVariable", None)
                setattr(value, "activitydiagram_IntegerVariable", self)

    def execute(self):
        # TODO: Implement execute method
        pass

class BooleanExpression:

    pass
class activitydiagram_IntegerComparisonExpression(BooleanExpression):

    def __init__(self, operator: bool, activitydiagram_IntegerComparisonExpression66: "activitydiagram_IntegerExpression" = None, activitydiagram_IntegerComparisonExpression: "activitydiagram_IntegerExpression" = None):
        self.operator = operator
        self.activitydiagram_IntegerComparisonExpression66 = activitydiagram_IntegerComparisonExpression66
        self.activitydiagram_IntegerComparisonExpression = activitydiagram_IntegerComparisonExpression
        
    @property
    def operator(self) -> bool:
        return self.__operator

    @operator.setter
    def operator(self, operator: bool):
        self.__operator = operator

    @property
    def activitydiagram_IntegerComparisonExpression(self):
        return self.__activitydiagram_IntegerComparisonExpression

    @activitydiagram_IntegerComparisonExpression.setter
    def activitydiagram_IntegerComparisonExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_IntegerComparisonExpression__activitydiagram_IntegerComparisonExpression", None)
        self.__activitydiagram_IntegerComparisonExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_IntegerExpression64"):
                opp_val = getattr(old_value, "activitydiagram_IntegerExpression64", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_IntegerExpression64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_IntegerExpression64"):
                opp_val = getattr(value, "activitydiagram_IntegerExpression64", None)
                setattr(value, "activitydiagram_IntegerExpression64", self)

    @property
    def activitydiagram_IntegerComparisonExpression66(self):
        return self.__activitydiagram_IntegerComparisonExpression66

    @activitydiagram_IntegerComparisonExpression66.setter
    def activitydiagram_IntegerComparisonExpression66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_IntegerComparisonExpression__activitydiagram_IntegerComparisonExpression66", None)
        self.__activitydiagram_IntegerComparisonExpression66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_IntegerExpression67"):
                opp_val = getattr(old_value, "activitydiagram_IntegerExpression67", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_IntegerExpression67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_IntegerExpression67"):
                opp_val = getattr(value, "activitydiagram_IntegerExpression67", None)
                setattr(value, "activitydiagram_IntegerExpression67", self)

    def evaluate(self):
        # TODO: Implement evaluate method
        pass

class activitydiagram_BooleanUnaryExpression(BooleanExpression):

    def __init__(self, operator: bool, activitydiagram_BooleanUnaryExpression: "activitydiagram_BooleanExpression" = None):
        self.operator = operator
        self.activitydiagram_BooleanUnaryExpression = activitydiagram_BooleanUnaryExpression
        
    @property
    def operator(self) -> bool:
        return self.__operator

    @operator.setter
    def operator(self, operator: bool):
        self.__operator = operator

    @property
    def activitydiagram_BooleanUnaryExpression(self):
        return self.__activitydiagram_BooleanUnaryExpression

    @activitydiagram_BooleanUnaryExpression.setter
    def activitydiagram_BooleanUnaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanUnaryExpression__activitydiagram_BooleanUnaryExpression", None)
        self.__activitydiagram_BooleanUnaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_BooleanExpression"):
                opp_val = getattr(old_value, "activitydiagram_BooleanExpression", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanExpression"):
                opp_val = getattr(value, "activitydiagram_BooleanExpression", None)
                setattr(value, "activitydiagram_BooleanExpression", self)

    def evaluate(self):
        # TODO: Implement evaluate method
        pass

class activitydiagram_BooleanBinaryExpression(BooleanExpression):

    def __init__(self, operator: bool, activitydiagram_BooleanBinaryExpression: "activitydiagram_BooleanExpression" = None, activitydiagram_BooleanBinaryExpression72: "activitydiagram_BooleanExpression" = None):
        self.operator = operator
        self.activitydiagram_BooleanBinaryExpression = activitydiagram_BooleanBinaryExpression
        self.activitydiagram_BooleanBinaryExpression72 = activitydiagram_BooleanBinaryExpression72
        
    @property
    def operator(self) -> bool:
        return self.__operator

    @operator.setter
    def operator(self, operator: bool):
        self.__operator = operator

    @property
    def activitydiagram_BooleanBinaryExpression72(self):
        return self.__activitydiagram_BooleanBinaryExpression72

    @activitydiagram_BooleanBinaryExpression72.setter
    def activitydiagram_BooleanBinaryExpression72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanBinaryExpression__activitydiagram_BooleanBinaryExpression72", None)
        self.__activitydiagram_BooleanBinaryExpression72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_BooleanExpression73"):
                opp_val = getattr(old_value, "activitydiagram_BooleanExpression73", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanExpression73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanExpression73"):
                opp_val = getattr(value, "activitydiagram_BooleanExpression73", None)
                setattr(value, "activitydiagram_BooleanExpression73", self)

    @property
    def activitydiagram_BooleanBinaryExpression(self):
        return self.__activitydiagram_BooleanBinaryExpression

    @activitydiagram_BooleanBinaryExpression.setter
    def activitydiagram_BooleanBinaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanBinaryExpression__activitydiagram_BooleanBinaryExpression", None)
        self.__activitydiagram_BooleanBinaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_BooleanExpression70"):
                opp_val = getattr(old_value, "activitydiagram_BooleanExpression70", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanExpression70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanExpression70"):
                opp_val = getattr(value, "activitydiagram_BooleanExpression70", None)
                setattr(value, "activitydiagram_BooleanExpression70", self)

    def evaluate(self):
        # TODO: Implement evaluate method
        pass

class IntegerExpression:

    pass
class Variable:

    pass
class activitydiagram_IntegerVariable(IntegerExpression, Variable):

    def __init__(self, initialValue: int, currentValue: bool, activitydiagram_IntegerVariable: "activitydiagram_IntegerVariableAssignment" = None):
        self.initialValue = initialValue
        self.currentValue = currentValue
        self.activitydiagram_IntegerVariable = activitydiagram_IntegerVariable
        
    @property
    def initialValue(self) -> int:
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue: int):
        self.__initialValue = initialValue

    @property
    def currentValue(self) -> bool:
        return self.__currentValue

    @currentValue.setter
    def currentValue(self, currentValue: bool):
        self.__currentValue = currentValue

    @property
    def activitydiagram_IntegerVariable(self):
        return self.__activitydiagram_IntegerVariable

    @activitydiagram_IntegerVariable.setter
    def activitydiagram_IntegerVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_IntegerVariable__activitydiagram_IntegerVariable", None)
        self.__activitydiagram_IntegerVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_IntegerVariableAssignment"):
                opp_val = getattr(old_value, "activitydiagram_IntegerVariableAssignment", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_IntegerVariableAssignment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_IntegerVariableAssignment"):
                opp_val = getattr(value, "activitydiagram_IntegerVariableAssignment", None)
                setattr(value, "activitydiagram_IntegerVariableAssignment", self)

    def init(self):
        # TODO: Implement init method
        pass

    def evaluate(self):
        # TODO: Implement evaluate method
        pass

class Value:

    pass
class activitydiagram_IntegerValue(IntegerExpression, Value):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class activitydiagram_BooleanValue(Value, BooleanExpression):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class Expression:

    pass
class activitydiagram_IntegerBinaryExpression(IntegerExpression, Expression):

    def __init__(self, operator: bool, activitydiagram_IntegerBinaryExpression: "activitydiagram_IntegerExpression" = None, activitydiagram_IntegerBinaryExpression61: "activitydiagram_IntegerExpression" = None):
        self.operator = operator
        self.activitydiagram_IntegerBinaryExpression = activitydiagram_IntegerBinaryExpression
        self.activitydiagram_IntegerBinaryExpression61 = activitydiagram_IntegerBinaryExpression61
        
    @property
    def operator(self) -> bool:
        return self.__operator

    @operator.setter
    def operator(self, operator: bool):
        self.__operator = operator

    @property
    def activitydiagram_IntegerBinaryExpression(self):
        return self.__activitydiagram_IntegerBinaryExpression

    @activitydiagram_IntegerBinaryExpression.setter
    def activitydiagram_IntegerBinaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_IntegerBinaryExpression__activitydiagram_IntegerBinaryExpression", None)
        self.__activitydiagram_IntegerBinaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_IntegerExpression"):
                opp_val = getattr(old_value, "activitydiagram_IntegerExpression", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_IntegerExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_IntegerExpression"):
                opp_val = getattr(value, "activitydiagram_IntegerExpression", None)
                setattr(value, "activitydiagram_IntegerExpression", self)

    @property
    def activitydiagram_IntegerBinaryExpression61(self):
        return self.__activitydiagram_IntegerBinaryExpression61

    @activitydiagram_IntegerBinaryExpression61.setter
    def activitydiagram_IntegerBinaryExpression61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_IntegerBinaryExpression__activitydiagram_IntegerBinaryExpression61", None)
        self.__activitydiagram_IntegerBinaryExpression61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_IntegerExpression62"):
                opp_val = getattr(old_value, "activitydiagram_IntegerExpression62", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_IntegerExpression62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_IntegerExpression62"):
                opp_val = getattr(value, "activitydiagram_IntegerExpression62", None)
                setattr(value, "activitydiagram_IntegerExpression62", self)

    def evaluate(self):
        # TODO: Implement evaluate method
        pass

class activitydiagram_Expression(ABC):

    pass
class FinalNode:

    pass
class activitydiagram_FlowFinalNode(FinalNode):

    def __init__(self):
        
    def execute(self):
        # TODO: Implement execute method
        pass

class activitydiagram_ActivityFinalNode(FinalNode):

    def __init__(self):
        
    def execute(self):
        # TODO: Implement execute method
        pass

class activitydiagram_BooleanExpression(Expression):

    def __init__(self, activitydiagram_BooleanExpression: "activitydiagram_BooleanUnaryExpression" = None, activitydiagram_BooleanExpression78: "activitydiagram_BooleanVariableAssignment" = None, activitydiagram_BooleanExpression70: "activitydiagram_BooleanBinaryExpression" = None, activitydiagram_BooleanExpression73: "activitydiagram_BooleanBinaryExpression" = None):
        self.activitydiagram_BooleanExpression = activitydiagram_BooleanExpression
        self.activitydiagram_BooleanExpression78 = activitydiagram_BooleanExpression78
        self.activitydiagram_BooleanExpression70 = activitydiagram_BooleanExpression70
        self.activitydiagram_BooleanExpression73 = activitydiagram_BooleanExpression73
        
    @property
    def activitydiagram_BooleanExpression78(self):
        return self.__activitydiagram_BooleanExpression78

    @activitydiagram_BooleanExpression78.setter
    def activitydiagram_BooleanExpression78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanExpression__activitydiagram_BooleanExpression78", None)
        self.__activitydiagram_BooleanExpression78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_BooleanVariableAssignment77"):
                opp_val = getattr(old_value, "activitydiagram_BooleanVariableAssignment77", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanVariableAssignment77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanVariableAssignment77"):
                opp_val = getattr(value, "activitydiagram_BooleanVariableAssignment77", None)
                setattr(value, "activitydiagram_BooleanVariableAssignment77", self)

    @property
    def activitydiagram_BooleanExpression70(self):
        return self.__activitydiagram_BooleanExpression70

    @activitydiagram_BooleanExpression70.setter
    def activitydiagram_BooleanExpression70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanExpression__activitydiagram_BooleanExpression70", None)
        self.__activitydiagram_BooleanExpression70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_BooleanBinaryExpression"):
                opp_val = getattr(old_value, "activitydiagram_BooleanBinaryExpression", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanBinaryExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanBinaryExpression"):
                opp_val = getattr(value, "activitydiagram_BooleanBinaryExpression", None)
                setattr(value, "activitydiagram_BooleanBinaryExpression", self)

    @property
    def activitydiagram_BooleanExpression(self):
        return self.__activitydiagram_BooleanExpression

    @activitydiagram_BooleanExpression.setter
    def activitydiagram_BooleanExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanExpression__activitydiagram_BooleanExpression", None)
        self.__activitydiagram_BooleanExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_BooleanUnaryExpression"):
                opp_val = getattr(old_value, "activitydiagram_BooleanUnaryExpression", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanUnaryExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanUnaryExpression"):
                opp_val = getattr(value, "activitydiagram_BooleanUnaryExpression", None)
                setattr(value, "activitydiagram_BooleanUnaryExpression", self)

    @property
    def activitydiagram_BooleanExpression73(self):
        return self.__activitydiagram_BooleanExpression73

    @activitydiagram_BooleanExpression73.setter
    def activitydiagram_BooleanExpression73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanExpression__activitydiagram_BooleanExpression73", None)
        self.__activitydiagram_BooleanExpression73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_BooleanBinaryExpression72"):
                opp_val = getattr(old_value, "activitydiagram_BooleanBinaryExpression72", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanBinaryExpression72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanBinaryExpression72"):
                opp_val = getattr(value, "activitydiagram_BooleanBinaryExpression72", None)
                setattr(value, "activitydiagram_BooleanBinaryExpression72", self)

    def evaluate(self):
        # TODO: Implement evaluate method
        pass

class activitydiagram_IntegerExpression(Expression):

    def __init__(self, activitydiagram_IntegerExpression67: "activitydiagram_IntegerComparisonExpression" = None, activitydiagram_IntegerExpression: "activitydiagram_IntegerBinaryExpression" = None, activitydiagram_IntegerExpression62: "activitydiagram_IntegerBinaryExpression" = None, activitydiagram_IntegerExpression64: "activitydiagram_IntegerComparisonExpression" = None, activitydiagram_IntegerExpression82: "activitydiagram_IntegerVariableAssignment" = None):
        self.activitydiagram_IntegerExpression67 = activitydiagram_IntegerExpression67
        self.activitydiagram_IntegerExpression = activitydiagram_IntegerExpression
        self.activitydiagram_IntegerExpression62 = activitydiagram_IntegerExpression62
        self.activitydiagram_IntegerExpression64 = activitydiagram_IntegerExpression64
        self.activitydiagram_IntegerExpression82 = activitydiagram_IntegerExpression82
        
    @property
    def activitydiagram_IntegerExpression(self):
        return self.__activitydiagram_IntegerExpression

    @activitydiagram_IntegerExpression.setter
    def activitydiagram_IntegerExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_IntegerExpression__activitydiagram_IntegerExpression", None)
        self.__activitydiagram_IntegerExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_IntegerBinaryExpression"):
                opp_val = getattr(old_value, "activitydiagram_IntegerBinaryExpression", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_IntegerBinaryExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_IntegerBinaryExpression"):
                opp_val = getattr(value, "activitydiagram_IntegerBinaryExpression", None)
                setattr(value, "activitydiagram_IntegerBinaryExpression", self)

    @property
    def activitydiagram_IntegerExpression64(self):
        return self.__activitydiagram_IntegerExpression64

    @activitydiagram_IntegerExpression64.setter
    def activitydiagram_IntegerExpression64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_IntegerExpression__activitydiagram_IntegerExpression64", None)
        self.__activitydiagram_IntegerExpression64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_IntegerComparisonExpression"):
                opp_val = getattr(old_value, "activitydiagram_IntegerComparisonExpression", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_IntegerComparisonExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_IntegerComparisonExpression"):
                opp_val = getattr(value, "activitydiagram_IntegerComparisonExpression", None)
                setattr(value, "activitydiagram_IntegerComparisonExpression", self)

    @property
    def activitydiagram_IntegerExpression62(self):
        return self.__activitydiagram_IntegerExpression62

    @activitydiagram_IntegerExpression62.setter
    def activitydiagram_IntegerExpression62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_IntegerExpression__activitydiagram_IntegerExpression62", None)
        self.__activitydiagram_IntegerExpression62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_IntegerBinaryExpression61"):
                opp_val = getattr(old_value, "activitydiagram_IntegerBinaryExpression61", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_IntegerBinaryExpression61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_IntegerBinaryExpression61"):
                opp_val = getattr(value, "activitydiagram_IntegerBinaryExpression61", None)
                setattr(value, "activitydiagram_IntegerBinaryExpression61", self)

    @property
    def activitydiagram_IntegerExpression82(self):
        return self.__activitydiagram_IntegerExpression82

    @activitydiagram_IntegerExpression82.setter
    def activitydiagram_IntegerExpression82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_IntegerExpression__activitydiagram_IntegerExpression82", None)
        self.__activitydiagram_IntegerExpression82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_IntegerVariableAssignment81"):
                opp_val = getattr(old_value, "activitydiagram_IntegerVariableAssignment81", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_IntegerVariableAssignment81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_IntegerVariableAssignment81"):
                opp_val = getattr(value, "activitydiagram_IntegerVariableAssignment81", None)
                setattr(value, "activitydiagram_IntegerVariableAssignment81", self)

    @property
    def activitydiagram_IntegerExpression67(self):
        return self.__activitydiagram_IntegerExpression67

    @activitydiagram_IntegerExpression67.setter
    def activitydiagram_IntegerExpression67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_IntegerExpression__activitydiagram_IntegerExpression67", None)
        self.__activitydiagram_IntegerExpression67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_IntegerComparisonExpression66"):
                opp_val = getattr(old_value, "activitydiagram_IntegerComparisonExpression66", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_IntegerComparisonExpression66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_IntegerComparisonExpression66"):
                opp_val = getattr(value, "activitydiagram_IntegerComparisonExpression66", None)
                setattr(value, "activitydiagram_IntegerComparisonExpression66", self)

    def evaluate(self):
        # TODO: Implement evaluate method
        pass

class activitydiagram_Value(Expression):

    pass
class ControlNode:

    pass
class activitydiagram_DecisionNode(ControlNode):

    def __init__(self, activitydiagram_DecisionNode: "activitydiagram_ActivityEdge" = None, activitydiagram_DecisionNode40: set["activitydiagram_ActivityEdge"] = None):
        self.activitydiagram_DecisionNode = activitydiagram_DecisionNode
        self.activitydiagram_DecisionNode40 = activitydiagram_DecisionNode40 if activitydiagram_DecisionNode40 is not None else set()
        
    @property
    def activitydiagram_DecisionNode40(self):
        return self.__activitydiagram_DecisionNode40

    @activitydiagram_DecisionNode40.setter
    def activitydiagram_DecisionNode40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_DecisionNode__activitydiagram_DecisionNode40", None)
        self.__activitydiagram_DecisionNode40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activitydiagram_ActivityEdge41"):
                    opp_val = getattr(item, "activitydiagram_ActivityEdge41", None)
                    
                    if opp_val == self:
                        setattr(item, "activitydiagram_ActivityEdge41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activitydiagram_ActivityEdge41"):
                    opp_val = getattr(item, "activitydiagram_ActivityEdge41", None)
                    
                    setattr(item, "activitydiagram_ActivityEdge41", self)
                    

    @property
    def activitydiagram_DecisionNode(self):
        return self.__activitydiagram_DecisionNode

    @activitydiagram_DecisionNode.setter
    def activitydiagram_DecisionNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_DecisionNode__activitydiagram_DecisionNode", None)
        self.__activitydiagram_DecisionNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_ActivityEdge38"):
                opp_val = getattr(old_value, "activitydiagram_ActivityEdge38", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_ActivityEdge38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_ActivityEdge38"):
                opp_val = getattr(value, "activitydiagram_ActivityEdge38", None)
                setattr(value, "activitydiagram_ActivityEdge38", self)

    def execute(self):
        # TODO: Implement execute method
        pass

    def hasOffers(self):
        # TODO: Implement hasOffers method
        pass

class activitydiagram_JoinNode(ControlNode):

    def __init__(self, activitydiagram_JoinNode: set["activitydiagram_ActivityEdge"] = None, activitydiagram_JoinNode55: "activitydiagram_ActivityEdge" = None):
        self.activitydiagram_JoinNode = activitydiagram_JoinNode if activitydiagram_JoinNode is not None else set()
        self.activitydiagram_JoinNode55 = activitydiagram_JoinNode55
        
    @property
    def activitydiagram_JoinNode55(self):
        return self.__activitydiagram_JoinNode55

    @activitydiagram_JoinNode55.setter
    def activitydiagram_JoinNode55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_JoinNode__activitydiagram_JoinNode55", None)
        self.__activitydiagram_JoinNode55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_ActivityEdge56"):
                opp_val = getattr(old_value, "activitydiagram_ActivityEdge56", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_ActivityEdge56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_ActivityEdge56"):
                opp_val = getattr(value, "activitydiagram_ActivityEdge56", None)
                setattr(value, "activitydiagram_ActivityEdge56", self)

    @property
    def activitydiagram_JoinNode(self):
        return self.__activitydiagram_JoinNode

    @activitydiagram_JoinNode.setter
    def activitydiagram_JoinNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_JoinNode__activitydiagram_JoinNode", None)
        self.__activitydiagram_JoinNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activitydiagram_ActivityEdge53"):
                    opp_val = getattr(item, "activitydiagram_ActivityEdge53", None)
                    
                    if opp_val == self:
                        setattr(item, "activitydiagram_ActivityEdge53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activitydiagram_ActivityEdge53"):
                    opp_val = getattr(item, "activitydiagram_ActivityEdge53", None)
                    
                    setattr(item, "activitydiagram_ActivityEdge53", self)
                    

    def hasOffers(self):
        # TODO: Implement hasOffers method
        pass

    def execute(self):
        # TODO: Implement execute method
        pass

class activitydiagram_FinalNode(ControlNode):

    def __init__(self, activitydiagram_FinalNode: "activitydiagram_ActivityEdge" = None):
        self.activitydiagram_FinalNode = activitydiagram_FinalNode
        
    @property
    def activitydiagram_FinalNode(self):
        return self.__activitydiagram_FinalNode

    @activitydiagram_FinalNode.setter
    def activitydiagram_FinalNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_FinalNode__activitydiagram_FinalNode", None)
        self.__activitydiagram_FinalNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_ActivityEdge58"):
                opp_val = getattr(old_value, "activitydiagram_ActivityEdge58", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_ActivityEdge58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_ActivityEdge58"):
                opp_val = getattr(value, "activitydiagram_ActivityEdge58", None)
                setattr(value, "activitydiagram_ActivityEdge58", self)

    def hasOffers(self):
        # TODO: Implement hasOffers method
        pass

    def execute(self):
        # TODO: Implement execute method
        pass

class activitydiagram_ForkNode(ControlNode):

    def __init__(self, activitydiagram_ForkNode: "activitydiagram_ActivityEdge" = None, activitydiagram_ForkNode50: set["activitydiagram_ActivityEdge"] = None):
        self.activitydiagram_ForkNode = activitydiagram_ForkNode
        self.activitydiagram_ForkNode50 = activitydiagram_ForkNode50 if activitydiagram_ForkNode50 is not None else set()
        
    @property
    def activitydiagram_ForkNode50(self):
        return self.__activitydiagram_ForkNode50

    @activitydiagram_ForkNode50.setter
    def activitydiagram_ForkNode50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ForkNode__activitydiagram_ForkNode50", None)
        self.__activitydiagram_ForkNode50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activitydiagram_ActivityEdge51"):
                    opp_val = getattr(item, "activitydiagram_ActivityEdge51", None)
                    
                    if opp_val == self:
                        setattr(item, "activitydiagram_ActivityEdge51", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activitydiagram_ActivityEdge51"):
                    opp_val = getattr(item, "activitydiagram_ActivityEdge51", None)
                    
                    setattr(item, "activitydiagram_ActivityEdge51", self)
                    

    @property
    def activitydiagram_ForkNode(self):
        return self.__activitydiagram_ForkNode

    @activitydiagram_ForkNode.setter
    def activitydiagram_ForkNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ForkNode__activitydiagram_ForkNode", None)
        self.__activitydiagram_ForkNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_ActivityEdge48"):
                opp_val = getattr(old_value, "activitydiagram_ActivityEdge48", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_ActivityEdge48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_ActivityEdge48"):
                opp_val = getattr(value, "activitydiagram_ActivityEdge48", None)
                setattr(value, "activitydiagram_ActivityEdge48", self)

    def execute(self):
        # TODO: Implement execute method
        pass

    def hasOffers(self):
        # TODO: Implement hasOffers method
        pass

class activitydiagram_InitialNode(ControlNode):

    def __init__(self, activitydiagram_InitialNode: "activitydiagram_ActivityEdge" = None):
        self.activitydiagram_InitialNode = activitydiagram_InitialNode
        
    @property
    def activitydiagram_InitialNode(self):
        return self.__activitydiagram_InitialNode

    @activitydiagram_InitialNode.setter
    def activitydiagram_InitialNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_InitialNode__activitydiagram_InitialNode", None)
        self.__activitydiagram_InitialNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_ActivityEdge36"):
                opp_val = getattr(old_value, "activitydiagram_ActivityEdge36", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_ActivityEdge36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_ActivityEdge36"):
                opp_val = getattr(value, "activitydiagram_ActivityEdge36", None)
                setattr(value, "activitydiagram_ActivityEdge36", self)

    def execute(self):
        # TODO: Implement execute method
        pass

    def sendOffer(self, token: str):
        # TODO: Implement sendOffer method
        pass

class activitydiagram_MergeNode(ControlNode):

    def __init__(self, activitydiagram_MergeNode: set["activitydiagram_ActivityEdge"] = None, activitydiagram_MergeNode45: "activitydiagram_ActivityEdge" = None):
        self.activitydiagram_MergeNode = activitydiagram_MergeNode if activitydiagram_MergeNode is not None else set()
        self.activitydiagram_MergeNode45 = activitydiagram_MergeNode45
        
    @property
    def activitydiagram_MergeNode(self):
        return self.__activitydiagram_MergeNode

    @activitydiagram_MergeNode.setter
    def activitydiagram_MergeNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_MergeNode__activitydiagram_MergeNode", None)
        self.__activitydiagram_MergeNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activitydiagram_ActivityEdge43"):
                    opp_val = getattr(item, "activitydiagram_ActivityEdge43", None)
                    
                    if opp_val == self:
                        setattr(item, "activitydiagram_ActivityEdge43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activitydiagram_ActivityEdge43"):
                    opp_val = getattr(item, "activitydiagram_ActivityEdge43", None)
                    
                    setattr(item, "activitydiagram_ActivityEdge43", self)
                    

    @property
    def activitydiagram_MergeNode45(self):
        return self.__activitydiagram_MergeNode45

    @activitydiagram_MergeNode45.setter
    def activitydiagram_MergeNode45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_MergeNode__activitydiagram_MergeNode45", None)
        self.__activitydiagram_MergeNode45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_ActivityEdge46"):
                opp_val = getattr(old_value, "activitydiagram_ActivityEdge46", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_ActivityEdge46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_ActivityEdge46"):
                opp_val = getattr(value, "activitydiagram_ActivityEdge46", None)
                setattr(value, "activitydiagram_ActivityEdge46", self)

    def execute(self):
        # TODO: Implement execute method
        pass

    def hasOffers(self):
        # TODO: Implement hasOffers method
        pass

class activitydiagram_VariableAssignment(ABC):

    def __init__(self, activitydiagram_VariableAssignment: "activitydiagram_OpaqueAction" = None):
        self.activitydiagram_VariableAssignment = activitydiagram_VariableAssignment
        
    @property
    def activitydiagram_VariableAssignment(self):
        return self.__activitydiagram_VariableAssignment

    @activitydiagram_VariableAssignment.setter
    def activitydiagram_VariableAssignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_VariableAssignment__activitydiagram_VariableAssignment", None)
        self.__activitydiagram_VariableAssignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_OpaqueAction"):
                opp_val = getattr(old_value, "activitydiagram_OpaqueAction", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_OpaqueAction"):
                opp_val = getattr(value, "activitydiagram_OpaqueAction", None)
                if opp_val is None:
                    setattr(value, "activitydiagram_OpaqueAction", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def execute(self):
        # TODO: Implement execute method
        pass

class ActivityNode:

    pass
class activitydiagram_AcceptEventAction(ActivityNode):

    def __init__(self, activitydiagram_AcceptEventAction: "activitydiagram_Event" = None, activitydiagram_AcceptEventAction30: "activitydiagram_ActivityEdge" = None, activitydiagram_AcceptEventAction33: "activitydiagram_ActivityEdge" = None):
        self.activitydiagram_AcceptEventAction = activitydiagram_AcceptEventAction
        self.activitydiagram_AcceptEventAction30 = activitydiagram_AcceptEventAction30
        self.activitydiagram_AcceptEventAction33 = activitydiagram_AcceptEventAction33
        
    @property
    def activitydiagram_AcceptEventAction33(self):
        return self.__activitydiagram_AcceptEventAction33

    @activitydiagram_AcceptEventAction33.setter
    def activitydiagram_AcceptEventAction33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_AcceptEventAction__activitydiagram_AcceptEventAction33", None)
        self.__activitydiagram_AcceptEventAction33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_ActivityEdge34"):
                opp_val = getattr(old_value, "activitydiagram_ActivityEdge34", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_ActivityEdge34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_ActivityEdge34"):
                opp_val = getattr(value, "activitydiagram_ActivityEdge34", None)
                setattr(value, "activitydiagram_ActivityEdge34", self)

    @property
    def activitydiagram_AcceptEventAction(self):
        return self.__activitydiagram_AcceptEventAction

    @activitydiagram_AcceptEventAction.setter
    def activitydiagram_AcceptEventAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_AcceptEventAction__activitydiagram_AcceptEventAction", None)
        self.__activitydiagram_AcceptEventAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_Event28"):
                opp_val = getattr(old_value, "activitydiagram_Event28", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_Event28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Event28"):
                opp_val = getattr(value, "activitydiagram_Event28", None)
                setattr(value, "activitydiagram_Event28", self)

    @property
    def activitydiagram_AcceptEventAction30(self):
        return self.__activitydiagram_AcceptEventAction30

    @activitydiagram_AcceptEventAction30.setter
    def activitydiagram_AcceptEventAction30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_AcceptEventAction__activitydiagram_AcceptEventAction30", None)
        self.__activitydiagram_AcceptEventAction30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_ActivityEdge31"):
                opp_val = getattr(old_value, "activitydiagram_ActivityEdge31", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_ActivityEdge31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_ActivityEdge31"):
                opp_val = getattr(value, "activitydiagram_ActivityEdge31", None)
                setattr(value, "activitydiagram_ActivityEdge31", self)

    def accept(self, event: str):
        # TODO: Implement accept method
        pass

    def hasOffers(self):
        # TODO: Implement hasOffers method
        pass

    def execute(self):
        # TODO: Implement execute method
        pass

    def waitForEvent(self):
        # TODO: Implement waitForEvent method
        pass

    def canAccept(self, event: str):
        # TODO: Implement canAccept method
        pass

    def sendOffer(self, token: str):
        # TODO: Implement sendOffer method
        pass

class activitydiagram_ControlNode(ActivityNode):

    pass
class activitydiagram_Action(ActivityNode):

    pass
class Action:

    pass
class activitydiagram_OpaqueAction(Action):

    def __init__(self, activitydiagram_OpaqueAction: set["activitydiagram_VariableAssignment"] = None):
        self.activitydiagram_OpaqueAction = activitydiagram_OpaqueAction if activitydiagram_OpaqueAction is not None else set()
        
    @property
    def activitydiagram_OpaqueAction(self):
        return self.__activitydiagram_OpaqueAction

    @activitydiagram_OpaqueAction.setter
    def activitydiagram_OpaqueAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_OpaqueAction__activitydiagram_OpaqueAction", None)
        self.__activitydiagram_OpaqueAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activitydiagram_VariableAssignment"):
                    opp_val = getattr(item, "activitydiagram_VariableAssignment", None)
                    
                    if opp_val == self:
                        setattr(item, "activitydiagram_VariableAssignment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activitydiagram_VariableAssignment"):
                    opp_val = getattr(item, "activitydiagram_VariableAssignment", None)
                    
                    setattr(item, "activitydiagram_VariableAssignment", self)
                    

    def sendOffer(self, token: str):
        # TODO: Implement sendOffer method
        pass

    def execute(self):
        # TODO: Implement execute method
        pass

    def hasOffers(self):
        # TODO: Implement hasOffers method
        pass

class activitydiagram_BooleanVariable(Variable, BooleanExpression):

    def __init__(self, currentValue: bool, initialValue: bool, activitydiagram_BooleanVariable: "activitydiagram_ControlFlow" = None, activitydiagram_BooleanVariable75: "activitydiagram_BooleanVariableAssignment" = None):
        self.currentValue = currentValue
        self.initialValue = initialValue
        self.activitydiagram_BooleanVariable = activitydiagram_BooleanVariable
        self.activitydiagram_BooleanVariable75 = activitydiagram_BooleanVariable75
        
    @property
    def currentValue(self) -> bool:
        return self.__currentValue

    @currentValue.setter
    def currentValue(self, currentValue: bool):
        self.__currentValue = currentValue

    @property
    def initialValue(self) -> bool:
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue: bool):
        self.__initialValue = initialValue

    @property
    def activitydiagram_BooleanVariable(self):
        return self.__activitydiagram_BooleanVariable

    @activitydiagram_BooleanVariable.setter
    def activitydiagram_BooleanVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanVariable__activitydiagram_BooleanVariable", None)
        self.__activitydiagram_BooleanVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_ControlFlow"):
                opp_val = getattr(old_value, "activitydiagram_ControlFlow", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_ControlFlow", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_ControlFlow"):
                opp_val = getattr(value, "activitydiagram_ControlFlow", None)
                setattr(value, "activitydiagram_ControlFlow", self)

    @property
    def activitydiagram_BooleanVariable75(self):
        return self.__activitydiagram_BooleanVariable75

    @activitydiagram_BooleanVariable75.setter
    def activitydiagram_BooleanVariable75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanVariable__activitydiagram_BooleanVariable75", None)
        self.__activitydiagram_BooleanVariable75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_BooleanVariableAssignment"):
                opp_val = getattr(old_value, "activitydiagram_BooleanVariableAssignment", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanVariableAssignment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanVariableAssignment"):
                opp_val = getattr(value, "activitydiagram_BooleanVariableAssignment", None)
                setattr(value, "activitydiagram_BooleanVariableAssignment", self)

    def init(self):
        # TODO: Implement init method
        pass

    def evaluate(self):
        # TODO: Implement evaluate method
        pass

class ActivityEdge:

    pass
class activitydiagram_ControlFlow(ActivityEdge):

    pass
class activitydiagram_ControlToken:

    def __init__(self, activitydiagram_ControlToken: "activitydiagram_ActivityEdge" = None, activitydiagram_ControlToken20: "activitydiagram_ActivityNode" = None):
        self.activitydiagram_ControlToken = activitydiagram_ControlToken
        self.activitydiagram_ControlToken20 = activitydiagram_ControlToken20
        
    @property
    def activitydiagram_ControlToken20(self):
        return self.__activitydiagram_ControlToken20

    @activitydiagram_ControlToken20.setter
    def activitydiagram_ControlToken20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ControlToken__activitydiagram_ControlToken20", None)
        self.__activitydiagram_ControlToken20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_ActivityNode19"):
                opp_val = getattr(old_value, "activitydiagram_ActivityNode19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_ActivityNode19"):
                opp_val = getattr(value, "activitydiagram_ActivityNode19", None)
                if opp_val is None:
                    setattr(value, "activitydiagram_ActivityNode19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def activitydiagram_ControlToken(self):
        return self.__activitydiagram_ControlToken

    @activitydiagram_ControlToken.setter
    def activitydiagram_ControlToken(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ControlToken__activitydiagram_ControlToken", None)
        self.__activitydiagram_ControlToken = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_ActivityEdge13"):
                opp_val = getattr(old_value, "activitydiagram_ActivityEdge13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_ActivityEdge13"):
                opp_val = getattr(value, "activitydiagram_ActivityEdge13", None)
                if opp_val is None:
                    setattr(value, "activitydiagram_ActivityEdge13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def isWithdrawn(self):
        # TODO: Implement isWithdrawn method
        pass

class activitydiagram_Variable(Expression):

    def __init__(self, name: int, activitydiagram_Variable: "activitydiagram_Activity" = None):
        self.name = name
        self.activitydiagram_Variable = activitydiagram_Variable
        
    @property
    def name(self) -> int:
        return self.__name

    @name.setter
    def name(self, name: int):
        self.__name = name

    @property
    def activitydiagram_Variable(self):
        return self.__activitydiagram_Variable

    @activitydiagram_Variable.setter
    def activitydiagram_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Variable__activitydiagram_Variable", None)
        self.__activitydiagram_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_Activity6"):
                opp_val = getattr(old_value, "activitydiagram_Activity6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Activity6"):
                opp_val = getattr(value, "activitydiagram_Activity6", None)
                if opp_val is None:
                    setattr(value, "activitydiagram_Activity6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def init(self):
        # TODO: Implement init method
        pass

class activitydiagram_NamedElement(ABC):

    def __init__(self, name: bool):
        self.name = name
        
    @property
    def name(self) -> bool:
        return self.__name

    @name.setter
    def name(self, name: bool):
        self.__name = name

    def execute(self):
        # TODO: Implement execute method
        pass

class NamedElement:

    pass
class activitydiagram_ActivityNode(NamedElement):

    def __init__(self, running: bool, 2: "activitydiagram_Activity" = None, activitydiagram_ActivityNode: "activitydiagram_ActivityEdge" = None, activitydiagram_ActivityNode11: "activitydiagram_ActivityEdge" = None, 16: "activitydiagram_Activity" = None, activitydiagram_ActivityNode19: set["activitydiagram_ControlToken"] = None):
        self.running = running
        self.2 = 2
        self.activitydiagram_ActivityNode = activitydiagram_ActivityNode
        self.activitydiagram_ActivityNode11 = activitydiagram_ActivityNode11
        self.16 = 16
        self.activitydiagram_ActivityNode19 = activitydiagram_ActivityNode19 if activitydiagram_ActivityNode19 is not None else set()
        
    @property
    def running(self) -> bool:
        return self.__running

    @running.setter
    def running(self, running: bool):
        self.__running = running

    @property
    def activitydiagram_ActivityNode19(self):
        return self.__activitydiagram_ActivityNode19

    @activitydiagram_ActivityNode19.setter
    def activitydiagram_ActivityNode19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__activitydiagram_ActivityNode19", None)
        self.__activitydiagram_ActivityNode19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activitydiagram_ControlToken20"):
                    opp_val = getattr(item, "activitydiagram_ControlToken20", None)
                    
                    if opp_val == self:
                        setattr(item, "activitydiagram_ControlToken20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activitydiagram_ControlToken20"):
                    opp_val = getattr(item, "activitydiagram_ControlToken20", None)
                    
                    setattr(item, "activitydiagram_ControlToken20", self)
                    

    @property
    def activitydiagram_ActivityNode11(self):
        return self.__activitydiagram_ActivityNode11

    @activitydiagram_ActivityNode11.setter
    def activitydiagram_ActivityNode11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__activitydiagram_ActivityNode11", None)
        self.__activitydiagram_ActivityNode11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_ActivityEdge10"):
                opp_val = getattr(old_value, "activitydiagram_ActivityEdge10", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_ActivityEdge10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_ActivityEdge10"):
                opp_val = getattr(value, "activitydiagram_ActivityEdge10", None)
                setattr(value, "activitydiagram_ActivityEdge10", self)

    @property
    def activitydiagram_ActivityNode(self):
        return self.__activitydiagram_ActivityNode

    @activitydiagram_ActivityNode.setter
    def activitydiagram_ActivityNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__activitydiagram_ActivityNode", None)
        self.__activitydiagram_ActivityNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_ActivityEdge8"):
                opp_val = getattr(old_value, "activitydiagram_ActivityEdge8", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_ActivityEdge8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_ActivityEdge8"):
                opp_val = getattr(value, "activitydiagram_ActivityEdge8", None)
                setattr(value, "activitydiagram_ActivityEdge8", self)

    @property
    def 2(self):
        return self.__2

    @2.setter
    def 2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__2", None)
        self.__2 = value
        
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
    def 16(self):
        return self.__16

    @16.setter
    def 16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__16", None)
        self.__16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "17"):
                opp_val = getattr(old_value, "17", None)
                if opp_val == self:
                    setattr(old_value, "17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "17"):
                opp_val = getattr(value, "17", None)
                setattr(value, "17", self)

    def addToken(self, token: str):
        # TODO: Implement addToken method
        pass

    def terminate(self):
        # TODO: Implement terminate method
        pass

    def isReady(self):
        # TODO: Implement isReady method
        pass

    def hasOffers(self):
        # TODO: Implement hasOffers method
        pass

    def removeToken(self, token: str):
        # TODO: Implement removeToken method
        pass

    def canAddToken(self, token: str):
        # TODO: Implement canAddToken method
        pass

    def execute(self):
        # TODO: Implement execute method
        pass

class activitydiagram_Event(NamedElement):

    pass
class activitydiagram_ActivityEdge(NamedElement):

    def __init__(self, activitydiagram_ActivityEdge: "activitydiagram_Activity" = None, activitydiagram_ActivityEdge8: "activitydiagram_ActivityNode" = None, activitydiagram_ActivityEdge10: "activitydiagram_ActivityNode" = None, activitydiagram_ActivityEdge13: set["activitydiagram_ControlToken"] = None, activitydiagram_ActivityEdge25: "activitydiagram_Action" = None, activitydiagram_ActivityEdge22: "activitydiagram_Action" = None, activitydiagram_ActivityEdge31: "activitydiagram_AcceptEventAction" = None, activitydiagram_ActivityEdge34: "activitydiagram_AcceptEventAction" = None, activitydiagram_ActivityEdge41: "activitydiagram_DecisionNode" = None, activitydiagram_ActivityEdge36: "activitydiagram_InitialNode" = None, activitydiagram_ActivityEdge38: "activitydiagram_DecisionNode" = None, activitydiagram_ActivityEdge53: "activitydiagram_JoinNode" = None, activitydiagram_ActivityEdge56: "activitydiagram_JoinNode" = None, activitydiagram_ActivityEdge43: "activitydiagram_MergeNode" = None, activitydiagram_ActivityEdge46: "activitydiagram_MergeNode" = None, activitydiagram_ActivityEdge48: "activitydiagram_ForkNode" = None, activitydiagram_ActivityEdge51: "activitydiagram_ForkNode" = None, activitydiagram_ActivityEdge58: "activitydiagram_FinalNode" = None):
        self.activitydiagram_ActivityEdge = activitydiagram_ActivityEdge
        self.activitydiagram_ActivityEdge8 = activitydiagram_ActivityEdge8
        self.activitydiagram_ActivityEdge10 = activitydiagram_ActivityEdge10
        self.activitydiagram_ActivityEdge13 = activitydiagram_ActivityEdge13 if activitydiagram_ActivityEdge13 is not None else set()
        self.activitydiagram_ActivityEdge25 = activitydiagram_ActivityEdge25
        self.activitydiagram_ActivityEdge22 = activitydiagram_ActivityEdge22
        self.activitydiagram_ActivityEdge31 = activitydiagram_ActivityEdge31
        self.activitydiagram_ActivityEdge34 = activitydiagram_ActivityEdge34
        self.activitydiagram_ActivityEdge41 = activitydiagram_ActivityEdge41
        self.activitydiagram_ActivityEdge36 = activitydiagram_ActivityEdge36
        self.activitydiagram_ActivityEdge38 = activitydiagram_ActivityEdge38
        self.activitydiagram_ActivityEdge53 = activitydiagram_ActivityEdge53
        self.activitydiagram_ActivityEdge56 = activitydiagram_ActivityEdge56
        self.activitydiagram_ActivityEdge43 = activitydiagram_ActivityEdge43
        self.activitydiagram_ActivityEdge46 = activitydiagram_ActivityEdge46
        self.activitydiagram_ActivityEdge48 = activitydiagram_ActivityEdge48
        self.activitydiagram_ActivityEdge51 = activitydiagram_ActivityEdge51
        self.activitydiagram_ActivityEdge58 = activitydiagram_ActivityEdge58
        
    @property
    def activitydiagram_ActivityEdge13(self):
        return self.__activitydiagram_ActivityEdge13

    @activitydiagram_ActivityEdge13.setter
    def activitydiagram_ActivityEdge13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__activitydiagram_ActivityEdge13", None)
        self.__activitydiagram_ActivityEdge13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activitydiagram_ControlToken"):
                    opp_val = getattr(item, "activitydiagram_ControlToken", None)
                    
                    if opp_val == self:
                        setattr(item, "activitydiagram_ControlToken", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activitydiagram_ControlToken"):
                    opp_val = getattr(item, "activitydiagram_ControlToken", None)
                    
                    setattr(item, "activitydiagram_ControlToken", self)
                    

    @property
    def activitydiagram_ActivityEdge53(self):
        return self.__activitydiagram_ActivityEdge53

    @activitydiagram_ActivityEdge53.setter
    def activitydiagram_ActivityEdge53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__activitydiagram_ActivityEdge53", None)
        self.__activitydiagram_ActivityEdge53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_JoinNode"):
                opp_val = getattr(old_value, "activitydiagram_JoinNode", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_JoinNode"):
                opp_val = getattr(value, "activitydiagram_JoinNode", None)
                if opp_val is None:
                    setattr(value, "activitydiagram_JoinNode", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def activitydiagram_ActivityEdge(self):
        return self.__activitydiagram_ActivityEdge

    @activitydiagram_ActivityEdge.setter
    def activitydiagram_ActivityEdge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__activitydiagram_ActivityEdge", None)
        self.__activitydiagram_ActivityEdge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_Activity4"):
                opp_val = getattr(old_value, "activitydiagram_Activity4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Activity4"):
                opp_val = getattr(value, "activitydiagram_Activity4", None)
                if opp_val is None:
                    setattr(value, "activitydiagram_Activity4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def activitydiagram_ActivityEdge38(self):
        return self.__activitydiagram_ActivityEdge38

    @activitydiagram_ActivityEdge38.setter
    def activitydiagram_ActivityEdge38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__activitydiagram_ActivityEdge38", None)
        self.__activitydiagram_ActivityEdge38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_DecisionNode"):
                opp_val = getattr(old_value, "activitydiagram_DecisionNode", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_DecisionNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_DecisionNode"):
                opp_val = getattr(value, "activitydiagram_DecisionNode", None)
                setattr(value, "activitydiagram_DecisionNode", self)

    @property
    def activitydiagram_ActivityEdge58(self):
        return self.__activitydiagram_ActivityEdge58

    @activitydiagram_ActivityEdge58.setter
    def activitydiagram_ActivityEdge58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__activitydiagram_ActivityEdge58", None)
        self.__activitydiagram_ActivityEdge58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_FinalNode"):
                opp_val = getattr(old_value, "activitydiagram_FinalNode", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_FinalNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_FinalNode"):
                opp_val = getattr(value, "activitydiagram_FinalNode", None)
                setattr(value, "activitydiagram_FinalNode", self)

    @property
    def activitydiagram_ActivityEdge31(self):
        return self.__activitydiagram_ActivityEdge31

    @activitydiagram_ActivityEdge31.setter
    def activitydiagram_ActivityEdge31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__activitydiagram_ActivityEdge31", None)
        self.__activitydiagram_ActivityEdge31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_AcceptEventAction30"):
                opp_val = getattr(old_value, "activitydiagram_AcceptEventAction30", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_AcceptEventAction30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_AcceptEventAction30"):
                opp_val = getattr(value, "activitydiagram_AcceptEventAction30", None)
                setattr(value, "activitydiagram_AcceptEventAction30", self)

    @property
    def activitydiagram_ActivityEdge8(self):
        return self.__activitydiagram_ActivityEdge8

    @activitydiagram_ActivityEdge8.setter
    def activitydiagram_ActivityEdge8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__activitydiagram_ActivityEdge8", None)
        self.__activitydiagram_ActivityEdge8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_ActivityNode"):
                opp_val = getattr(old_value, "activitydiagram_ActivityNode", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_ActivityNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_ActivityNode"):
                opp_val = getattr(value, "activitydiagram_ActivityNode", None)
                setattr(value, "activitydiagram_ActivityNode", self)

    @property
    def activitydiagram_ActivityEdge56(self):
        return self.__activitydiagram_ActivityEdge56

    @activitydiagram_ActivityEdge56.setter
    def activitydiagram_ActivityEdge56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__activitydiagram_ActivityEdge56", None)
        self.__activitydiagram_ActivityEdge56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_JoinNode55"):
                opp_val = getattr(old_value, "activitydiagram_JoinNode55", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_JoinNode55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_JoinNode55"):
                opp_val = getattr(value, "activitydiagram_JoinNode55", None)
                setattr(value, "activitydiagram_JoinNode55", self)

    @property
    def activitydiagram_ActivityEdge22(self):
        return self.__activitydiagram_ActivityEdge22

    @activitydiagram_ActivityEdge22.setter
    def activitydiagram_ActivityEdge22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__activitydiagram_ActivityEdge22", None)
        self.__activitydiagram_ActivityEdge22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_Action"):
                opp_val = getattr(old_value, "activitydiagram_Action", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_Action", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Action"):
                opp_val = getattr(value, "activitydiagram_Action", None)
                setattr(value, "activitydiagram_Action", self)

    @property
    def activitydiagram_ActivityEdge43(self):
        return self.__activitydiagram_ActivityEdge43

    @activitydiagram_ActivityEdge43.setter
    def activitydiagram_ActivityEdge43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__activitydiagram_ActivityEdge43", None)
        self.__activitydiagram_ActivityEdge43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_MergeNode"):
                opp_val = getattr(old_value, "activitydiagram_MergeNode", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_MergeNode"):
                opp_val = getattr(value, "activitydiagram_MergeNode", None)
                if opp_val is None:
                    setattr(value, "activitydiagram_MergeNode", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def activitydiagram_ActivityEdge46(self):
        return self.__activitydiagram_ActivityEdge46

    @activitydiagram_ActivityEdge46.setter
    def activitydiagram_ActivityEdge46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__activitydiagram_ActivityEdge46", None)
        self.__activitydiagram_ActivityEdge46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_MergeNode45"):
                opp_val = getattr(old_value, "activitydiagram_MergeNode45", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_MergeNode45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_MergeNode45"):
                opp_val = getattr(value, "activitydiagram_MergeNode45", None)
                setattr(value, "activitydiagram_MergeNode45", self)

    @property
    def activitydiagram_ActivityEdge25(self):
        return self.__activitydiagram_ActivityEdge25

    @activitydiagram_ActivityEdge25.setter
    def activitydiagram_ActivityEdge25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__activitydiagram_ActivityEdge25", None)
        self.__activitydiagram_ActivityEdge25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_Action24"):
                opp_val = getattr(old_value, "activitydiagram_Action24", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_Action24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Action24"):
                opp_val = getattr(value, "activitydiagram_Action24", None)
                setattr(value, "activitydiagram_Action24", self)

    @property
    def activitydiagram_ActivityEdge36(self):
        return self.__activitydiagram_ActivityEdge36

    @activitydiagram_ActivityEdge36.setter
    def activitydiagram_ActivityEdge36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__activitydiagram_ActivityEdge36", None)
        self.__activitydiagram_ActivityEdge36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_InitialNode"):
                opp_val = getattr(old_value, "activitydiagram_InitialNode", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_InitialNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_InitialNode"):
                opp_val = getattr(value, "activitydiagram_InitialNode", None)
                setattr(value, "activitydiagram_InitialNode", self)

    @property
    def activitydiagram_ActivityEdge41(self):
        return self.__activitydiagram_ActivityEdge41

    @activitydiagram_ActivityEdge41.setter
    def activitydiagram_ActivityEdge41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__activitydiagram_ActivityEdge41", None)
        self.__activitydiagram_ActivityEdge41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_DecisionNode40"):
                opp_val = getattr(old_value, "activitydiagram_DecisionNode40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_DecisionNode40"):
                opp_val = getattr(value, "activitydiagram_DecisionNode40", None)
                if opp_val is None:
                    setattr(value, "activitydiagram_DecisionNode40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def activitydiagram_ActivityEdge48(self):
        return self.__activitydiagram_ActivityEdge48

    @activitydiagram_ActivityEdge48.setter
    def activitydiagram_ActivityEdge48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__activitydiagram_ActivityEdge48", None)
        self.__activitydiagram_ActivityEdge48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_ForkNode"):
                opp_val = getattr(old_value, "activitydiagram_ForkNode", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_ForkNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_ForkNode"):
                opp_val = getattr(value, "activitydiagram_ForkNode", None)
                setattr(value, "activitydiagram_ForkNode", self)

    @property
    def activitydiagram_ActivityEdge51(self):
        return self.__activitydiagram_ActivityEdge51

    @activitydiagram_ActivityEdge51.setter
    def activitydiagram_ActivityEdge51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__activitydiagram_ActivityEdge51", None)
        self.__activitydiagram_ActivityEdge51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_ForkNode50"):
                opp_val = getattr(old_value, "activitydiagram_ForkNode50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_ForkNode50"):
                opp_val = getattr(value, "activitydiagram_ForkNode50", None)
                if opp_val is None:
                    setattr(value, "activitydiagram_ForkNode50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def activitydiagram_ActivityEdge10(self):
        return self.__activitydiagram_ActivityEdge10

    @activitydiagram_ActivityEdge10.setter
    def activitydiagram_ActivityEdge10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__activitydiagram_ActivityEdge10", None)
        self.__activitydiagram_ActivityEdge10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_ActivityNode11"):
                opp_val = getattr(old_value, "activitydiagram_ActivityNode11", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_ActivityNode11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_ActivityNode11"):
                opp_val = getattr(value, "activitydiagram_ActivityNode11", None)
                setattr(value, "activitydiagram_ActivityNode11", self)

    @property
    def activitydiagram_ActivityEdge34(self):
        return self.__activitydiagram_ActivityEdge34

    @activitydiagram_ActivityEdge34.setter
    def activitydiagram_ActivityEdge34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__activitydiagram_ActivityEdge34", None)
        self.__activitydiagram_ActivityEdge34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_AcceptEventAction33"):
                opp_val = getattr(old_value, "activitydiagram_AcceptEventAction33", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_AcceptEventAction33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_AcceptEventAction33"):
                opp_val = getattr(value, "activitydiagram_AcceptEventAction33", None)
                setattr(value, "activitydiagram_AcceptEventAction33", self)

    def sendOffer(self, token: str):
        # TODO: Implement sendOffer method
        pass

    def takeOfferedToken(self) -> str:
        # TODO: Implement takeOfferedToken method
        pass

    def hasOffer(self):
        # TODO: Implement hasOffer method
        pass

class activitydiagram_Activity(NamedElement):

    def __init__(self, activitydiagram_Activity6: set["activitydiagram_Variable"] = None, activitydiagram_Activity: set["activitydiagram_Event"] = None, : set["activitydiagram_ActivityNode"] = None, activitydiagram_Activity4: set["activitydiagram_ActivityEdge"] = None, 17: "activitydiagram_ActivityNode" = None):
        self.activitydiagram_Activity6 = activitydiagram_Activity6 if activitydiagram_Activity6 is not None else set()
        self.activitydiagram_Activity = activitydiagram_Activity if activitydiagram_Activity is not None else set()
        self. =  if  is not None else set()
        self.activitydiagram_Activity4 = activitydiagram_Activity4 if activitydiagram_Activity4 is not None else set()
        self.17 = 17
        
    @property
    def activitydiagram_Activity4(self):
        return self.__activitydiagram_Activity4

    @activitydiagram_Activity4.setter
    def activitydiagram_Activity4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Activity__activitydiagram_Activity4", None)
        self.__activitydiagram_Activity4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activitydiagram_ActivityEdge"):
                    opp_val = getattr(item, "activitydiagram_ActivityEdge", None)
                    
                    if opp_val == self:
                        setattr(item, "activitydiagram_ActivityEdge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activitydiagram_ActivityEdge"):
                    opp_val = getattr(item, "activitydiagram_ActivityEdge", None)
                    
                    setattr(item, "activitydiagram_ActivityEdge", self)
                    

    @property
    def (self):
        return self.__

    @.setter
    def (self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Activity__", None)
        self.__ = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "2"):
                    opp_val = getattr(item, "2", None)
                    
                    if opp_val == self:
                        setattr(item, "2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "2"):
                    opp_val = getattr(item, "2", None)
                    
                    setattr(item, "2", self)
                    

    @property
    def activitydiagram_Activity6(self):
        return self.__activitydiagram_Activity6

    @activitydiagram_Activity6.setter
    def activitydiagram_Activity6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Activity__activitydiagram_Activity6", None)
        self.__activitydiagram_Activity6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activitydiagram_Variable"):
                    opp_val = getattr(item, "activitydiagram_Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "activitydiagram_Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activitydiagram_Variable"):
                    opp_val = getattr(item, "activitydiagram_Variable", None)
                    
                    setattr(item, "activitydiagram_Variable", self)
                    

    @property
    def activitydiagram_Activity(self):
        return self.__activitydiagram_Activity

    @activitydiagram_Activity.setter
    def activitydiagram_Activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Activity__activitydiagram_Activity", None)
        self.__activitydiagram_Activity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activitydiagram_Event"):
                    opp_val = getattr(item, "activitydiagram_Event", None)
                    
                    if opp_val == self:
                        setattr(item, "activitydiagram_Event", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activitydiagram_Event"):
                    opp_val = getattr(item, "activitydiagram_Event", None)
                    
                    setattr(item, "activitydiagram_Event", self)
                    

    @property
    def 17(self):
        return self.__17

    @17.setter
    def 17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Activity__17", None)
        self.__17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "16"):
                opp_val = getattr(old_value, "16", None)
                if opp_val == self:
                    setattr(old_value, "16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "16"):
                opp_val = getattr(value, "16", None)
                setattr(value, "16", self)

    def execute(self):
        # TODO: Implement execute method
        pass

    def main(self):
        # TODO: Implement main method
        pass

    def initializeModel(self, args: str):
        # TODO: Implement initializeModel method
        pass
