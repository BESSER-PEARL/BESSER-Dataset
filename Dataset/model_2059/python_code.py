from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class BooleanUnaryOperator(Enum):
    NOT = "NOT"
class IntegerCalculationOperator(Enum):
    ADD = "ADD"
    SUBRACT = "SUBRACT"
class BooleanBinaryOperator(Enum):
    AND = "AND"
    OR = "OR"
class IntegerComparisonOperator(Enum):
    SMALLER = "SMALLER"
    SMALLER_EQUALS = "SMALLER_EQUALS"
    EQUALS = "EQUALS"
    GREATER_EQUALS = "GREATER_EQUALS"
    GREATER = "GREATER"


############################################
# Definition of Classes
############################################

class activitydiagram_Offer:

    pass
class VariableAssignment:

    pass
class activitydiagram_IntegerVariableAssignment(VariableAssignment):

    def __init__(self, activitydiagram_IntegerVariableAssignment: "activitydiagram_IntegerVariable" = None, activitydiagram_IntegerVariableAssignment78: "activitydiagram_IntegerExpression" = None):
        self.activitydiagram_IntegerVariableAssignment = activitydiagram_IntegerVariableAssignment
        self.activitydiagram_IntegerVariableAssignment78 = activitydiagram_IntegerVariableAssignment78
        
        pass
    @property
    def activitydiagram_IntegerVariableAssignment78(self):
        return self.__activitydiagram_IntegerVariableAssignment78

    @activitydiagram_IntegerVariableAssignment78.setter
    def activitydiagram_IntegerVariableAssignment78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_IntegerVariableAssignment__activitydiagram_IntegerVariableAssignment78", None)
        self.__activitydiagram_IntegerVariableAssignment78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_IntegerExpression79"):
                opp_val = getattr(old_value, "activitydiagram_IntegerExpression79", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_IntegerExpression79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_IntegerExpression79"):
                opp_val = getattr(value, "activitydiagram_IntegerExpression79", None)
                setattr(value, "activitydiagram_IntegerExpression79", self)

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

class activitydiagram_BooleanVariableAssignment(VariableAssignment):

    def __init__(self, activitydiagram_BooleanVariableAssignment: "activitydiagram_BooleanVariable" = None, activitydiagram_BooleanVariableAssignment74: "activitydiagram_BooleanExpression" = None):
        self.activitydiagram_BooleanVariableAssignment = activitydiagram_BooleanVariableAssignment
        self.activitydiagram_BooleanVariableAssignment74 = activitydiagram_BooleanVariableAssignment74
        
        pass
    @property
    def activitydiagram_BooleanVariableAssignment74(self):
        return self.__activitydiagram_BooleanVariableAssignment74

    @activitydiagram_BooleanVariableAssignment74.setter
    def activitydiagram_BooleanVariableAssignment74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanVariableAssignment__activitydiagram_BooleanVariableAssignment74", None)
        self.__activitydiagram_BooleanVariableAssignment74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_BooleanExpression75"):
                opp_val = getattr(old_value, "activitydiagram_BooleanExpression75", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanExpression75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanExpression75"):
                opp_val = getattr(value, "activitydiagram_BooleanExpression75", None)
                setattr(value, "activitydiagram_BooleanExpression75", self)

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
            if hasattr(old_value, "activitydiagram_BooleanVariable72"):
                opp_val = getattr(old_value, "activitydiagram_BooleanVariable72", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanVariable72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanVariable72"):
                opp_val = getattr(value, "activitydiagram_BooleanVariable72", None)
                setattr(value, "activitydiagram_BooleanVariable72", self)

    def execute(self):
        # TODO: Implement execute method
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
        
        pass
    @property
    def currentValue(self):
        return self.__currentValue

    @currentValue.setter
    def currentValue(self, currentValue: bool):
        self.__currentValue = currentValue


    @property
    def initialValue(self):
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue: int):
        self.__initialValue = initialValue


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

class Expression:

    pass
class activitydiagram_IntegerExpression(Expression):

    def __init__(self, activitydiagram_IntegerExpression: "activitydiagram_IntegerBinaryExpression" = None, activitydiagram_IntegerExpression59: "activitydiagram_IntegerBinaryExpression" = None, activitydiagram_IntegerExpression79: "activitydiagram_IntegerVariableAssignment" = None, activitydiagram_IntegerExpression61: "activitydiagram_IntegerComparisonExpression" = None, activitydiagram_IntegerExpression64: "activitydiagram_IntegerComparisonExpression" = None):
        self.activitydiagram_IntegerExpression = activitydiagram_IntegerExpression
        self.activitydiagram_IntegerExpression59 = activitydiagram_IntegerExpression59
        self.activitydiagram_IntegerExpression79 = activitydiagram_IntegerExpression79
        self.activitydiagram_IntegerExpression61 = activitydiagram_IntegerExpression61
        self.activitydiagram_IntegerExpression64 = activitydiagram_IntegerExpression64
        
        pass
    @property
    def activitydiagram_IntegerExpression59(self):
        return self.__activitydiagram_IntegerExpression59

    @activitydiagram_IntegerExpression59.setter
    def activitydiagram_IntegerExpression59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_IntegerExpression__activitydiagram_IntegerExpression59", None)
        self.__activitydiagram_IntegerExpression59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_IntegerBinaryExpression58"):
                opp_val = getattr(old_value, "activitydiagram_IntegerBinaryExpression58", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_IntegerBinaryExpression58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_IntegerBinaryExpression58"):
                opp_val = getattr(value, "activitydiagram_IntegerBinaryExpression58", None)
                setattr(value, "activitydiagram_IntegerBinaryExpression58", self)

    @property
    def activitydiagram_IntegerExpression79(self):
        return self.__activitydiagram_IntegerExpression79

    @activitydiagram_IntegerExpression79.setter
    def activitydiagram_IntegerExpression79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_IntegerExpression__activitydiagram_IntegerExpression79", None)
        self.__activitydiagram_IntegerExpression79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_IntegerVariableAssignment78"):
                opp_val = getattr(old_value, "activitydiagram_IntegerVariableAssignment78", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_IntegerVariableAssignment78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_IntegerVariableAssignment78"):
                opp_val = getattr(value, "activitydiagram_IntegerVariableAssignment78", None)
                setattr(value, "activitydiagram_IntegerVariableAssignment78", self)

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
            if hasattr(old_value, "activitydiagram_IntegerComparisonExpression63"):
                opp_val = getattr(old_value, "activitydiagram_IntegerComparisonExpression63", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_IntegerComparisonExpression63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_IntegerComparisonExpression63"):
                opp_val = getattr(value, "activitydiagram_IntegerComparisonExpression63", None)
                setattr(value, "activitydiagram_IntegerComparisonExpression63", self)

    @property
    def activitydiagram_IntegerExpression61(self):
        return self.__activitydiagram_IntegerExpression61

    @activitydiagram_IntegerExpression61.setter
    def activitydiagram_IntegerExpression61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_IntegerExpression__activitydiagram_IntegerExpression61", None)
        self.__activitydiagram_IntegerExpression61 = value
        
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

    def evaluate(self):
        # TODO: Implement evaluate method
        pass

class activitydiagram_Value(Expression):

    pass
class activitydiagram_BooleanExpression(Expression):

    def __init__(self, activitydiagram_BooleanExpression70: "activitydiagram_BooleanBinaryExpression" = None, activitydiagram_BooleanExpression75: "activitydiagram_BooleanVariableAssignment" = None, activitydiagram_BooleanExpression: "activitydiagram_BooleanUnaryExpression" = None, activitydiagram_BooleanExpression67: "activitydiagram_BooleanBinaryExpression" = None):
        self.activitydiagram_BooleanExpression70 = activitydiagram_BooleanExpression70
        self.activitydiagram_BooleanExpression75 = activitydiagram_BooleanExpression75
        self.activitydiagram_BooleanExpression = activitydiagram_BooleanExpression
        self.activitydiagram_BooleanExpression67 = activitydiagram_BooleanExpression67
        
        pass
    @property
    def activitydiagram_BooleanExpression67(self):
        return self.__activitydiagram_BooleanExpression67

    @activitydiagram_BooleanExpression67.setter
    def activitydiagram_BooleanExpression67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanExpression__activitydiagram_BooleanExpression67", None)
        self.__activitydiagram_BooleanExpression67 = value
        
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
    def activitydiagram_BooleanExpression70(self):
        return self.__activitydiagram_BooleanExpression70

    @activitydiagram_BooleanExpression70.setter
    def activitydiagram_BooleanExpression70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanExpression__activitydiagram_BooleanExpression70", None)
        self.__activitydiagram_BooleanExpression70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_BooleanBinaryExpression69"):
                opp_val = getattr(old_value, "activitydiagram_BooleanBinaryExpression69", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanBinaryExpression69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanBinaryExpression69"):
                opp_val = getattr(value, "activitydiagram_BooleanBinaryExpression69", None)
                setattr(value, "activitydiagram_BooleanBinaryExpression69", self)

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
    def activitydiagram_BooleanExpression75(self):
        return self.__activitydiagram_BooleanExpression75

    @activitydiagram_BooleanExpression75.setter
    def activitydiagram_BooleanExpression75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanExpression__activitydiagram_BooleanExpression75", None)
        self.__activitydiagram_BooleanExpression75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_BooleanVariableAssignment74"):
                opp_val = getattr(old_value, "activitydiagram_BooleanVariableAssignment74", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanVariableAssignment74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanVariableAssignment74"):
                opp_val = getattr(value, "activitydiagram_BooleanVariableAssignment74", None)
                setattr(value, "activitydiagram_BooleanVariableAssignment74", self)

    def evaluate(self):
        # TODO: Implement evaluate method
        pass

class activitydiagram_Expression(ABC):

    pass
class activitydiagram_IntegerBinaryExpression(IntegerExpression, Expression):

    def __init__(self, operator: bool, activitydiagram_IntegerBinaryExpression: "activitydiagram_IntegerExpression" = None, activitydiagram_IntegerBinaryExpression58: "activitydiagram_IntegerExpression" = None):
        self.operator = operator
        self.activitydiagram_IntegerBinaryExpression = activitydiagram_IntegerBinaryExpression
        self.activitydiagram_IntegerBinaryExpression58 = activitydiagram_IntegerBinaryExpression58
        
        pass
    @property
    def operator(self):
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
    def activitydiagram_IntegerBinaryExpression58(self):
        return self.__activitydiagram_IntegerBinaryExpression58

    @activitydiagram_IntegerBinaryExpression58.setter
    def activitydiagram_IntegerBinaryExpression58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_IntegerBinaryExpression__activitydiagram_IntegerBinaryExpression58", None)
        self.__activitydiagram_IntegerBinaryExpression58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_IntegerExpression59"):
                opp_val = getattr(old_value, "activitydiagram_IntegerExpression59", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_IntegerExpression59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_IntegerExpression59"):
                opp_val = getattr(value, "activitydiagram_IntegerExpression59", None)
                setattr(value, "activitydiagram_IntegerExpression59", self)

    def evaluate(self):
        # TODO: Implement evaluate method
        pass

class Value:

    pass
class activitydiagram_IntegerValue(IntegerExpression, Value):

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class BooleanExpression:

    pass
class activitydiagram_BooleanUnaryExpression(BooleanExpression):

    def __init__(self, operator: bool, activitydiagram_BooleanUnaryExpression: "activitydiagram_BooleanExpression" = None):
        self.operator = operator
        self.activitydiagram_BooleanUnaryExpression = activitydiagram_BooleanUnaryExpression
        
        pass
    @property
    def operator(self):
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

class activitydiagram_BooleanValue(BooleanExpression, Value):

    def __init__(self, value: bool):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value


class activitydiagram_BooleanBinaryExpression(BooleanExpression):

    def __init__(self, operator: bool, activitydiagram_BooleanBinaryExpression69: "activitydiagram_BooleanExpression" = None, activitydiagram_BooleanBinaryExpression: "activitydiagram_BooleanExpression" = None):
        self.operator = operator
        self.activitydiagram_BooleanBinaryExpression69 = activitydiagram_BooleanBinaryExpression69
        self.activitydiagram_BooleanBinaryExpression = activitydiagram_BooleanBinaryExpression
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: bool):
        self.__operator = operator


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
            if hasattr(old_value, "activitydiagram_BooleanExpression67"):
                opp_val = getattr(old_value, "activitydiagram_BooleanExpression67", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanExpression67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanExpression67"):
                opp_val = getattr(value, "activitydiagram_BooleanExpression67", None)
                setattr(value, "activitydiagram_BooleanExpression67", self)

    @property
    def activitydiagram_BooleanBinaryExpression69(self):
        return self.__activitydiagram_BooleanBinaryExpression69

    @activitydiagram_BooleanBinaryExpression69.setter
    def activitydiagram_BooleanBinaryExpression69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanBinaryExpression__activitydiagram_BooleanBinaryExpression69", None)
        self.__activitydiagram_BooleanBinaryExpression69 = value
        
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

class activitydiagram_IntegerComparisonExpression(BooleanExpression):

    def __init__(self, operator: bool, activitydiagram_IntegerComparisonExpression: "activitydiagram_IntegerExpression" = None, activitydiagram_IntegerComparisonExpression63: "activitydiagram_IntegerExpression" = None):
        self.operator = operator
        self.activitydiagram_IntegerComparisonExpression = activitydiagram_IntegerComparisonExpression
        self.activitydiagram_IntegerComparisonExpression63 = activitydiagram_IntegerComparisonExpression63
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: bool):
        self.__operator = operator


    @property
    def activitydiagram_IntegerComparisonExpression63(self):
        return self.__activitydiagram_IntegerComparisonExpression63

    @activitydiagram_IntegerComparisonExpression63.setter
    def activitydiagram_IntegerComparisonExpression63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_IntegerComparisonExpression__activitydiagram_IntegerComparisonExpression63", None)
        self.__activitydiagram_IntegerComparisonExpression63 = value
        
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
    def activitydiagram_IntegerComparisonExpression(self):
        return self.__activitydiagram_IntegerComparisonExpression

    @activitydiagram_IntegerComparisonExpression.setter
    def activitydiagram_IntegerComparisonExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_IntegerComparisonExpression__activitydiagram_IntegerComparisonExpression", None)
        self.__activitydiagram_IntegerComparisonExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_IntegerExpression61"):
                opp_val = getattr(old_value, "activitydiagram_IntegerExpression61", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_IntegerExpression61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_IntegerExpression61"):
                opp_val = getattr(value, "activitydiagram_IntegerExpression61", None)
                setattr(value, "activitydiagram_IntegerExpression61", self)

    def evaluate(self):
        # TODO: Implement evaluate method
        pass

class FinalNode:

    pass
class activitydiagram_FlowFinalNode(FinalNode):

    def __init__(self):
        
        pass
    def execute(self):
        # TODO: Implement execute method
        pass

class activitydiagram_ActivityFinalNode(FinalNode):

    def __init__(self):
        
        pass
    def execute(self):
        # TODO: Implement execute method
        pass

class ActivityNode:

    pass
class activitydiagram_Action(ActivityNode):

    pass
class ControlNode:

    pass
class activitydiagram_MergeNode(ControlNode):

    def __init__(self, activitydiagram_MergeNode: set["activitydiagram_ActivityEdge"] = None, activitydiagram_MergeNode42: "activitydiagram_ActivityEdge" = None):
        self.activitydiagram_MergeNode = activitydiagram_MergeNode if activitydiagram_MergeNode is not None else set()
        self.activitydiagram_MergeNode42 = activitydiagram_MergeNode42
        
        pass
    @property
    def activitydiagram_MergeNode42(self):
        return self.__activitydiagram_MergeNode42

    @activitydiagram_MergeNode42.setter
    def activitydiagram_MergeNode42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_MergeNode__activitydiagram_MergeNode42", None)
        self.__activitydiagram_MergeNode42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_ActivityEdge43"):
                opp_val = getattr(old_value, "activitydiagram_ActivityEdge43", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_ActivityEdge43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_ActivityEdge43"):
                opp_val = getattr(value, "activitydiagram_ActivityEdge43", None)
                setattr(value, "activitydiagram_ActivityEdge43", self)

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
                if hasattr(item, "activitydiagram_ActivityEdge40"):
                    opp_val = getattr(item, "activitydiagram_ActivityEdge40", None)
                    
                    if opp_val == self:
                        setattr(item, "activitydiagram_ActivityEdge40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activitydiagram_ActivityEdge40"):
                    opp_val = getattr(item, "activitydiagram_ActivityEdge40", None)
                    
                    setattr(item, "activitydiagram_ActivityEdge40", self)
                    

    def hasOffers(self):
        # TODO: Implement hasOffers method
        pass

    def execute(self):
        # TODO: Implement execute method
        pass

class activitydiagram_JoinNode(ControlNode):

    def __init__(self, activitydiagram_JoinNode: set["activitydiagram_ActivityEdge"] = None, activitydiagram_JoinNode52: "activitydiagram_ActivityEdge" = None):
        self.activitydiagram_JoinNode = activitydiagram_JoinNode if activitydiagram_JoinNode is not None else set()
        self.activitydiagram_JoinNode52 = activitydiagram_JoinNode52
        
        pass
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
                if hasattr(item, "activitydiagram_ActivityEdge50"):
                    opp_val = getattr(item, "activitydiagram_ActivityEdge50", None)
                    
                    if opp_val == self:
                        setattr(item, "activitydiagram_ActivityEdge50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activitydiagram_ActivityEdge50"):
                    opp_val = getattr(item, "activitydiagram_ActivityEdge50", None)
                    
                    setattr(item, "activitydiagram_ActivityEdge50", self)
                    

    @property
    def activitydiagram_JoinNode52(self):
        return self.__activitydiagram_JoinNode52

    @activitydiagram_JoinNode52.setter
    def activitydiagram_JoinNode52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_JoinNode__activitydiagram_JoinNode52", None)
        self.__activitydiagram_JoinNode52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_ActivityEdge53"):
                opp_val = getattr(old_value, "activitydiagram_ActivityEdge53", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_ActivityEdge53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_ActivityEdge53"):
                opp_val = getattr(value, "activitydiagram_ActivityEdge53", None)
                setattr(value, "activitydiagram_ActivityEdge53", self)

    def hasOffers(self):
        # TODO: Implement hasOffers method
        pass

    def execute(self):
        # TODO: Implement execute method
        pass

class activitydiagram_ForkNode(ControlNode):

    def __init__(self, activitydiagram_ForkNode: "activitydiagram_ActivityEdge" = None, activitydiagram_ForkNode47: set["activitydiagram_ActivityEdge"] = None):
        self.activitydiagram_ForkNode = activitydiagram_ForkNode
        self.activitydiagram_ForkNode47 = activitydiagram_ForkNode47 if activitydiagram_ForkNode47 is not None else set()
        
        pass
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
            if hasattr(old_value, "activitydiagram_ActivityEdge45"):
                opp_val = getattr(old_value, "activitydiagram_ActivityEdge45", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_ActivityEdge45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_ActivityEdge45"):
                opp_val = getattr(value, "activitydiagram_ActivityEdge45", None)
                setattr(value, "activitydiagram_ActivityEdge45", self)

    @property
    def activitydiagram_ForkNode47(self):
        return self.__activitydiagram_ForkNode47

    @activitydiagram_ForkNode47.setter
    def activitydiagram_ForkNode47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ForkNode__activitydiagram_ForkNode47", None)
        self.__activitydiagram_ForkNode47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activitydiagram_ActivityEdge48"):
                    opp_val = getattr(item, "activitydiagram_ActivityEdge48", None)
                    
                    if opp_val == self:
                        setattr(item, "activitydiagram_ActivityEdge48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activitydiagram_ActivityEdge48"):
                    opp_val = getattr(item, "activitydiagram_ActivityEdge48", None)
                    
                    setattr(item, "activitydiagram_ActivityEdge48", self)
                    

    def hasOffers(self):
        # TODO: Implement hasOffers method
        pass

    def execute(self):
        # TODO: Implement execute method
        pass

class activitydiagram_DecisionNode(ControlNode):

    def __init__(self, activitydiagram_DecisionNode: "activitydiagram_ActivityEdge" = None, activitydiagram_DecisionNode37: set["activitydiagram_ActivityEdge"] = None):
        self.activitydiagram_DecisionNode = activitydiagram_DecisionNode
        self.activitydiagram_DecisionNode37 = activitydiagram_DecisionNode37 if activitydiagram_DecisionNode37 is not None else set()
        
        pass
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
            if hasattr(old_value, "activitydiagram_ActivityEdge35"):
                opp_val = getattr(old_value, "activitydiagram_ActivityEdge35", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_ActivityEdge35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_ActivityEdge35"):
                opp_val = getattr(value, "activitydiagram_ActivityEdge35", None)
                setattr(value, "activitydiagram_ActivityEdge35", self)

    @property
    def activitydiagram_DecisionNode37(self):
        return self.__activitydiagram_DecisionNode37

    @activitydiagram_DecisionNode37.setter
    def activitydiagram_DecisionNode37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_DecisionNode__activitydiagram_DecisionNode37", None)
        self.__activitydiagram_DecisionNode37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activitydiagram_ActivityEdge38"):
                    opp_val = getattr(item, "activitydiagram_ActivityEdge38", None)
                    
                    if opp_val == self:
                        setattr(item, "activitydiagram_ActivityEdge38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activitydiagram_ActivityEdge38"):
                    opp_val = getattr(item, "activitydiagram_ActivityEdge38", None)
                    
                    setattr(item, "activitydiagram_ActivityEdge38", self)
                    

    def hasOffers(self):
        # TODO: Implement hasOffers method
        pass

    def execute(self):
        # TODO: Implement execute method
        pass

class activitydiagram_FinalNode(ControlNode):

    def __init__(self, activitydiagram_FinalNode: "activitydiagram_ActivityEdge" = None):
        self.activitydiagram_FinalNode = activitydiagram_FinalNode
        
        pass
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
            if hasattr(old_value, "activitydiagram_ActivityEdge55"):
                opp_val = getattr(old_value, "activitydiagram_ActivityEdge55", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_ActivityEdge55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_ActivityEdge55"):
                opp_val = getattr(value, "activitydiagram_ActivityEdge55", None)
                setattr(value, "activitydiagram_ActivityEdge55", self)

    def hasOffers(self):
        # TODO: Implement hasOffers method
        pass

    def execute(self):
        # TODO: Implement execute method
        pass

class activitydiagram_InitialNode(ControlNode):

    def __init__(self, activitydiagram_InitialNode: "activitydiagram_ActivityEdge" = None):
        self.activitydiagram_InitialNode = activitydiagram_InitialNode
        
        pass
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
            if hasattr(old_value, "activitydiagram_ActivityEdge33"):
                opp_val = getattr(old_value, "activitydiagram_ActivityEdge33", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_ActivityEdge33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_ActivityEdge33"):
                opp_val = getattr(value, "activitydiagram_ActivityEdge33", None)
                setattr(value, "activitydiagram_ActivityEdge33", self)

    def execute(self):
        # TODO: Implement execute method
        pass

    def sendOffer(self, activitydiagram_token):
        # TODO: Implement sendOffer method
        pass

class activitydiagram_ControlNode(ActivityNode):

    pass
class activitydiagram_AcceptEventAction(ActivityNode):

    def __init__(self, activitydiagram_AcceptEventAction: "activitydiagram_Event" = None, activitydiagram_AcceptEventAction27: "activitydiagram_ActivityEdge" = None, activitydiagram_AcceptEventAction30: "activitydiagram_ActivityEdge" = None):
        self.activitydiagram_AcceptEventAction = activitydiagram_AcceptEventAction
        self.activitydiagram_AcceptEventAction27 = activitydiagram_AcceptEventAction27
        self.activitydiagram_AcceptEventAction30 = activitydiagram_AcceptEventAction30
        
        pass
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

    @property
    def activitydiagram_AcceptEventAction27(self):
        return self.__activitydiagram_AcceptEventAction27

    @activitydiagram_AcceptEventAction27.setter
    def activitydiagram_AcceptEventAction27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_AcceptEventAction__activitydiagram_AcceptEventAction27", None)
        self.__activitydiagram_AcceptEventAction27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_ActivityEdge28"):
                opp_val = getattr(old_value, "activitydiagram_ActivityEdge28", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_ActivityEdge28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_ActivityEdge28"):
                opp_val = getattr(value, "activitydiagram_ActivityEdge28", None)
                setattr(value, "activitydiagram_ActivityEdge28", self)

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
            if hasattr(old_value, "activitydiagram_Event25"):
                opp_val = getattr(old_value, "activitydiagram_Event25", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_Event25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Event25"):
                opp_val = getattr(value, "activitydiagram_Event25", None)
                setattr(value, "activitydiagram_Event25", self)

    def execute(self):
        # TODO: Implement execute method
        pass

    def sendOffer(self, activitydiagram_token):
        # TODO: Implement sendOffer method
        pass

    def waitForEvent(self):
        # TODO: Implement waitForEvent method
        pass

    def hasOffers(self):
        # TODO: Implement hasOffers method
        pass

    def canAccept(self, activitydiagram_event):
        # TODO: Implement canAccept method
        pass

    def accept(self, activitydiagram_event):
        # TODO: Implement accept method
        pass

class activitydiagram_VariableAssignment(ABC):

    def __init__(self, activitydiagram_VariableAssignment: "activitydiagram_OpaqueAction" = None):
        self.activitydiagram_VariableAssignment = activitydiagram_VariableAssignment
        
        pass
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

class Action:

    pass
class activitydiagram_OpaqueAction(Action):

    def __init__(self, activitydiagram_OpaqueAction: set["activitydiagram_VariableAssignment"] = None):
        self.activitydiagram_OpaqueAction = activitydiagram_OpaqueAction if activitydiagram_OpaqueAction is not None else set()
        
        pass
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
                    

    def execute(self):
        # TODO: Implement execute method
        pass

    def sendOffer(self, activitydiagram_token):
        # TODO: Implement sendOffer method
        pass

    def hasOffers(self):
        # TODO: Implement hasOffers method
        pass

class NamedElement:

    pass
class activitydiagram_Event(NamedElement):

    pass
class activitydiagram_Activity(NamedElement):

    def __init__(self, activitydiagram_Activity: set["activitydiagram_Event"] = None, Activity: "activitydiagram_ActivityNode" = None, activity: set["activitydiagram_ActivityNode"] = None, activitydiagram_Activity3: set["activitydiagram_ActivityEdge"] = None, activitydiagram_Activity5: set["activitydiagram_Variable"] = None):
        self.activitydiagram_Activity = activitydiagram_Activity if activitydiagram_Activity is not None else set()
        self.Activity = Activity
        self.activity = activity if activity is not None else set()
        self.activitydiagram_Activity3 = activitydiagram_Activity3 if activitydiagram_Activity3 is not None else set()
        self.activitydiagram_Activity5 = activitydiagram_Activity5 if activitydiagram_Activity5 is not None else set()
        
        pass
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
    def activity(self):
        return self.__activity

    @activity.setter
    def activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Activity__activity", None)
        self.__activity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityNode"):
                    opp_val = getattr(item, "ActivityNode", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityNode"):
                    opp_val = getattr(item, "ActivityNode", None)
                    
                    setattr(item, "ActivityNode", self)
                    

    @property
    def Activity(self):
        return self.__Activity

    @Activity.setter
    def Activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Activity__Activity", None)
        self.__Activity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nodes"):
                opp_val = getattr(old_value, "nodes", None)
                if opp_val == self:
                    setattr(old_value, "nodes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nodes"):
                opp_val = getattr(value, "nodes", None)
                setattr(value, "nodes", self)

    @property
    def activitydiagram_Activity3(self):
        return self.__activitydiagram_Activity3

    @activitydiagram_Activity3.setter
    def activitydiagram_Activity3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Activity__activitydiagram_Activity3", None)
        self.__activitydiagram_Activity3 = value if value is not None else set()
        
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
    def activitydiagram_Activity5(self):
        return self.__activitydiagram_Activity5

    @activitydiagram_Activity5.setter
    def activitydiagram_Activity5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Activity__activitydiagram_Activity5", None)
        self.__activitydiagram_Activity5 = value if value is not None else set()
        
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
                    

    def execute(self):
        # TODO: Implement execute method
        pass

    def main(self):
        # TODO: Implement main method
        pass

    def initializeModel(self, activitydiagram_args):
        # TODO: Implement initializeModel method
        pass

class activitydiagram_NamedElement(ABC):

    def __init__(self, name: bool):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: bool):
        self.__name = name


    def execute(self):
        # TODO: Implement execute method
        pass

class activitydiagram_BooleanVariable(BooleanExpression, Variable):

    def __init__(self, initialValue: bool, currentValue: bool, activitydiagram_BooleanVariable: "activitydiagram_ControlFlow" = None, activitydiagram_BooleanVariable72: "activitydiagram_BooleanVariableAssignment" = None):
        self.initialValue = initialValue
        self.currentValue = currentValue
        self.activitydiagram_BooleanVariable = activitydiagram_BooleanVariable
        self.activitydiagram_BooleanVariable72 = activitydiagram_BooleanVariable72
        
        pass
    @property
    def currentValue(self):
        return self.__currentValue

    @currentValue.setter
    def currentValue(self, currentValue: bool):
        self.__currentValue = currentValue


    @property
    def initialValue(self):
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
    def activitydiagram_BooleanVariable72(self):
        return self.__activitydiagram_BooleanVariable72

    @activitydiagram_BooleanVariable72.setter
    def activitydiagram_BooleanVariable72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanVariable__activitydiagram_BooleanVariable72", None)
        self.__activitydiagram_BooleanVariable72 = value
        
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

    def evaluate(self):
        # TODO: Implement evaluate method
        pass

    def init(self):
        # TODO: Implement init method
        pass

class ActivityEdge:

    pass
class activitydiagram_ControlFlow(ActivityEdge):

    pass
class activitydiagram_ControlToken:

    def __init__(self, activitydiagram_ControlToken: "activitydiagram_ActivityEdge" = None, activitydiagram_ControlToken17: "activitydiagram_ActivityNode" = None):
        self.activitydiagram_ControlToken = activitydiagram_ControlToken
        self.activitydiagram_ControlToken17 = activitydiagram_ControlToken17
        
        pass
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
            if hasattr(old_value, "activitydiagram_ActivityEdge12"):
                opp_val = getattr(old_value, "activitydiagram_ActivityEdge12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_ActivityEdge12"):
                opp_val = getattr(value, "activitydiagram_ActivityEdge12", None)
                if opp_val is None:
                    setattr(value, "activitydiagram_ActivityEdge12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def activitydiagram_ControlToken17(self):
        return self.__activitydiagram_ControlToken17

    @activitydiagram_ControlToken17.setter
    def activitydiagram_ControlToken17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ControlToken__activitydiagram_ControlToken17", None)
        self.__activitydiagram_ControlToken17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_ActivityNode16"):
                opp_val = getattr(old_value, "activitydiagram_ActivityNode16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_ActivityNode16"):
                opp_val = getattr(value, "activitydiagram_ActivityNode16", None)
                if opp_val is None:
                    setattr(value, "activitydiagram_ActivityNode16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def isWithdrawn(self):
        # TODO: Implement isWithdrawn method
        pass

class activitydiagram_Variable(Expression):

    def __init__(self, name: int, activitydiagram_Variable: "activitydiagram_Activity" = None):
        self.name = name
        self.activitydiagram_Variable = activitydiagram_Variable
        
        pass
    @property
    def name(self):
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
            if hasattr(old_value, "activitydiagram_Activity5"):
                opp_val = getattr(old_value, "activitydiagram_Activity5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Activity5"):
                opp_val = getattr(value, "activitydiagram_Activity5", None)
                if opp_val is None:
                    setattr(value, "activitydiagram_Activity5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def init(self):
        # TODO: Implement init method
        pass

class activitydiagram_ActivityEdge(NamedElement):

    def __init__(self, activitydiagram_ActivityEdge9: "activitydiagram_ActivityNode" = None, activitydiagram_ActivityEdge12: set["activitydiagram_ControlToken"] = None, activitydiagram_ActivityEdge28: "activitydiagram_AcceptEventAction" = None, activitydiagram_ActivityEdge31: "activitydiagram_AcceptEventAction" = None, activitydiagram_ActivityEdge19: "activitydiagram_Action" = None, activitydiagram_ActivityEdge22: "activitydiagram_Action" = None, activitydiagram_ActivityEdge45: "activitydiagram_ForkNode" = None, activitydiagram_ActivityEdge48: "activitydiagram_ForkNode" = None, activitydiagram_ActivityEdge50: "activitydiagram_JoinNode" = None, activitydiagram_ActivityEdge53: "activitydiagram_JoinNode" = None, activitydiagram_ActivityEdge55: "activitydiagram_FinalNode" = None, activitydiagram_ActivityEdge33: "activitydiagram_InitialNode" = None, activitydiagram_ActivityEdge35: "activitydiagram_DecisionNode" = None, activitydiagram_ActivityEdge38: "activitydiagram_DecisionNode" = None, activitydiagram_ActivityEdge40: "activitydiagram_MergeNode" = None, activitydiagram_ActivityEdge43: "activitydiagram_MergeNode" = None, activitydiagram_ActivityEdge: "activitydiagram_Activity" = None, activitydiagram_ActivityEdge7: "activitydiagram_ActivityNode" = None):
        self.activitydiagram_ActivityEdge9 = activitydiagram_ActivityEdge9
        self.activitydiagram_ActivityEdge12 = activitydiagram_ActivityEdge12 if activitydiagram_ActivityEdge12 is not None else set()
        self.activitydiagram_ActivityEdge28 = activitydiagram_ActivityEdge28
        self.activitydiagram_ActivityEdge31 = activitydiagram_ActivityEdge31
        self.activitydiagram_ActivityEdge19 = activitydiagram_ActivityEdge19
        self.activitydiagram_ActivityEdge22 = activitydiagram_ActivityEdge22
        self.activitydiagram_ActivityEdge45 = activitydiagram_ActivityEdge45
        self.activitydiagram_ActivityEdge48 = activitydiagram_ActivityEdge48
        self.activitydiagram_ActivityEdge50 = activitydiagram_ActivityEdge50
        self.activitydiagram_ActivityEdge53 = activitydiagram_ActivityEdge53
        self.activitydiagram_ActivityEdge55 = activitydiagram_ActivityEdge55
        self.activitydiagram_ActivityEdge33 = activitydiagram_ActivityEdge33
        self.activitydiagram_ActivityEdge35 = activitydiagram_ActivityEdge35
        self.activitydiagram_ActivityEdge38 = activitydiagram_ActivityEdge38
        self.activitydiagram_ActivityEdge40 = activitydiagram_ActivityEdge40
        self.activitydiagram_ActivityEdge43 = activitydiagram_ActivityEdge43
        self.activitydiagram_ActivityEdge = activitydiagram_ActivityEdge
        self.activitydiagram_ActivityEdge7 = activitydiagram_ActivityEdge7
        
        pass
    @property
    def activitydiagram_ActivityEdge40(self):
        return self.__activitydiagram_ActivityEdge40

    @activitydiagram_ActivityEdge40.setter
    def activitydiagram_ActivityEdge40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__activitydiagram_ActivityEdge40", None)
        self.__activitydiagram_ActivityEdge40 = value
        
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
    def activitydiagram_ActivityEdge43(self):
        return self.__activitydiagram_ActivityEdge43

    @activitydiagram_ActivityEdge43.setter
    def activitydiagram_ActivityEdge43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__activitydiagram_ActivityEdge43", None)
        self.__activitydiagram_ActivityEdge43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_MergeNode42"):
                opp_val = getattr(old_value, "activitydiagram_MergeNode42", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_MergeNode42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_MergeNode42"):
                opp_val = getattr(value, "activitydiagram_MergeNode42", None)
                setattr(value, "activitydiagram_MergeNode42", self)

    @property
    def activitydiagram_ActivityEdge19(self):
        return self.__activitydiagram_ActivityEdge19

    @activitydiagram_ActivityEdge19.setter
    def activitydiagram_ActivityEdge19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__activitydiagram_ActivityEdge19", None)
        self.__activitydiagram_ActivityEdge19 = value
        
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
    def activitydiagram_ActivityEdge50(self):
        return self.__activitydiagram_ActivityEdge50

    @activitydiagram_ActivityEdge50.setter
    def activitydiagram_ActivityEdge50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__activitydiagram_ActivityEdge50", None)
        self.__activitydiagram_ActivityEdge50 = value
        
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
    def activitydiagram_ActivityEdge12(self):
        return self.__activitydiagram_ActivityEdge12

    @activitydiagram_ActivityEdge12.setter
    def activitydiagram_ActivityEdge12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__activitydiagram_ActivityEdge12", None)
        self.__activitydiagram_ActivityEdge12 = value if value is not None else set()
        
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
    def activitydiagram_ActivityEdge48(self):
        return self.__activitydiagram_ActivityEdge48

    @activitydiagram_ActivityEdge48.setter
    def activitydiagram_ActivityEdge48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__activitydiagram_ActivityEdge48", None)
        self.__activitydiagram_ActivityEdge48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_ForkNode47"):
                opp_val = getattr(old_value, "activitydiagram_ForkNode47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_ForkNode47"):
                opp_val = getattr(value, "activitydiagram_ForkNode47", None)
                if opp_val is None:
                    setattr(value, "activitydiagram_ForkNode47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def activitydiagram_ActivityEdge45(self):
        return self.__activitydiagram_ActivityEdge45

    @activitydiagram_ActivityEdge45.setter
    def activitydiagram_ActivityEdge45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__activitydiagram_ActivityEdge45", None)
        self.__activitydiagram_ActivityEdge45 = value
        
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
    def activitydiagram_ActivityEdge33(self):
        return self.__activitydiagram_ActivityEdge33

    @activitydiagram_ActivityEdge33.setter
    def activitydiagram_ActivityEdge33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__activitydiagram_ActivityEdge33", None)
        self.__activitydiagram_ActivityEdge33 = value
        
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
    def activitydiagram_ActivityEdge28(self):
        return self.__activitydiagram_ActivityEdge28

    @activitydiagram_ActivityEdge28.setter
    def activitydiagram_ActivityEdge28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__activitydiagram_ActivityEdge28", None)
        self.__activitydiagram_ActivityEdge28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_AcceptEventAction27"):
                opp_val = getattr(old_value, "activitydiagram_AcceptEventAction27", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_AcceptEventAction27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_AcceptEventAction27"):
                opp_val = getattr(value, "activitydiagram_AcceptEventAction27", None)
                setattr(value, "activitydiagram_AcceptEventAction27", self)

    @property
    def activitydiagram_ActivityEdge35(self):
        return self.__activitydiagram_ActivityEdge35

    @activitydiagram_ActivityEdge35.setter
    def activitydiagram_ActivityEdge35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__activitydiagram_ActivityEdge35", None)
        self.__activitydiagram_ActivityEdge35 = value
        
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
    def activitydiagram_ActivityEdge7(self):
        return self.__activitydiagram_ActivityEdge7

    @activitydiagram_ActivityEdge7.setter
    def activitydiagram_ActivityEdge7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__activitydiagram_ActivityEdge7", None)
        self.__activitydiagram_ActivityEdge7 = value
        
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
    def activitydiagram_ActivityEdge(self):
        return self.__activitydiagram_ActivityEdge

    @activitydiagram_ActivityEdge.setter
    def activitydiagram_ActivityEdge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__activitydiagram_ActivityEdge", None)
        self.__activitydiagram_ActivityEdge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_Activity3"):
                opp_val = getattr(old_value, "activitydiagram_Activity3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Activity3"):
                opp_val = getattr(value, "activitydiagram_Activity3", None)
                if opp_val is None:
                    setattr(value, "activitydiagram_Activity3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def activitydiagram_ActivityEdge9(self):
        return self.__activitydiagram_ActivityEdge9

    @activitydiagram_ActivityEdge9.setter
    def activitydiagram_ActivityEdge9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__activitydiagram_ActivityEdge9", None)
        self.__activitydiagram_ActivityEdge9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_ActivityNode10"):
                opp_val = getattr(old_value, "activitydiagram_ActivityNode10", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_ActivityNode10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_ActivityNode10"):
                opp_val = getattr(value, "activitydiagram_ActivityNode10", None)
                setattr(value, "activitydiagram_ActivityNode10", self)

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
            if hasattr(old_value, "activitydiagram_DecisionNode37"):
                opp_val = getattr(old_value, "activitydiagram_DecisionNode37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_DecisionNode37"):
                opp_val = getattr(value, "activitydiagram_DecisionNode37", None)
                if opp_val is None:
                    setattr(value, "activitydiagram_DecisionNode37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def activitydiagram_ActivityEdge55(self):
        return self.__activitydiagram_ActivityEdge55

    @activitydiagram_ActivityEdge55.setter
    def activitydiagram_ActivityEdge55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__activitydiagram_ActivityEdge55", None)
        self.__activitydiagram_ActivityEdge55 = value
        
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
    def activitydiagram_ActivityEdge22(self):
        return self.__activitydiagram_ActivityEdge22

    @activitydiagram_ActivityEdge22.setter
    def activitydiagram_ActivityEdge22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__activitydiagram_ActivityEdge22", None)
        self.__activitydiagram_ActivityEdge22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_Action21"):
                opp_val = getattr(old_value, "activitydiagram_Action21", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_Action21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Action21"):
                opp_val = getattr(value, "activitydiagram_Action21", None)
                setattr(value, "activitydiagram_Action21", self)

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
            if hasattr(old_value, "activitydiagram_JoinNode52"):
                opp_val = getattr(old_value, "activitydiagram_JoinNode52", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_JoinNode52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_JoinNode52"):
                opp_val = getattr(value, "activitydiagram_JoinNode52", None)
                setattr(value, "activitydiagram_JoinNode52", self)

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

    def takeOfferedToken(self) :
        # TODO: Implement takeOfferedToken method
        pass

    def sendOffer(self, activitydiagram_token):
        # TODO: Implement sendOffer method
        pass

    def hasOffer(self):
        # TODO: Implement hasOffer method
        pass

class activitydiagram_ActivityNode(NamedElement):

    def __init__(self, running: bool, nodes: "activitydiagram_Activity" = None, activitydiagram_ActivityNode16: set["activitydiagram_ControlToken"] = None, ActivityNode: "activitydiagram_Activity" = None, activitydiagram_ActivityNode: "activitydiagram_ActivityEdge" = None, activitydiagram_ActivityNode10: "activitydiagram_ActivityEdge" = None):
        self.running = running
        self.nodes = nodes
        self.activitydiagram_ActivityNode16 = activitydiagram_ActivityNode16 if activitydiagram_ActivityNode16 is not None else set()
        self.ActivityNode = ActivityNode
        self.activitydiagram_ActivityNode = activitydiagram_ActivityNode
        self.activitydiagram_ActivityNode10 = activitydiagram_ActivityNode10
        
        pass
    @property
    def running(self):
        return self.__running

    @running.setter
    def running(self, running: bool):
        self.__running = running


    @property
    def activitydiagram_ActivityNode10(self):
        return self.__activitydiagram_ActivityNode10

    @activitydiagram_ActivityNode10.setter
    def activitydiagram_ActivityNode10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__activitydiagram_ActivityNode10", None)
        self.__activitydiagram_ActivityNode10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_ActivityEdge9"):
                opp_val = getattr(old_value, "activitydiagram_ActivityEdge9", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_ActivityEdge9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_ActivityEdge9"):
                opp_val = getattr(value, "activitydiagram_ActivityEdge9", None)
                setattr(value, "activitydiagram_ActivityEdge9", self)

    @property
    def nodes(self):
        return self.__nodes

    @nodes.setter
    def nodes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__nodes", None)
        self.__nodes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Activity"):
                opp_val = getattr(old_value, "Activity", None)
                if opp_val == self:
                    setattr(old_value, "Activity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Activity"):
                opp_val = getattr(value, "Activity", None)
                setattr(value, "Activity", self)

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
            if hasattr(old_value, "activitydiagram_ActivityEdge7"):
                opp_val = getattr(old_value, "activitydiagram_ActivityEdge7", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_ActivityEdge7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_ActivityEdge7"):
                opp_val = getattr(value, "activitydiagram_ActivityEdge7", None)
                setattr(value, "activitydiagram_ActivityEdge7", self)

    @property
    def activitydiagram_ActivityNode16(self):
        return self.__activitydiagram_ActivityNode16

    @activitydiagram_ActivityNode16.setter
    def activitydiagram_ActivityNode16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__activitydiagram_ActivityNode16", None)
        self.__activitydiagram_ActivityNode16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activitydiagram_ControlToken17"):
                    opp_val = getattr(item, "activitydiagram_ControlToken17", None)
                    
                    if opp_val == self:
                        setattr(item, "activitydiagram_ControlToken17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activitydiagram_ControlToken17"):
                    opp_val = getattr(item, "activitydiagram_ControlToken17", None)
                    
                    setattr(item, "activitydiagram_ControlToken17", self)
                    

    @property
    def ActivityNode(self):
        return self.__ActivityNode

    @ActivityNode.setter
    def ActivityNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__ActivityNode", None)
        self.__ActivityNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activity"):
                opp_val = getattr(old_value, "activity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activity"):
                opp_val = getattr(value, "activity", None)
                if opp_val is None:
                    setattr(value, "activity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def addToken(self, activitydiagram_token):
        # TODO: Implement addToken method
        pass

    def hasOffers(self):
        # TODO: Implement hasOffers method
        pass

    def removeToken(self, activitydiagram_token):
        # TODO: Implement removeToken method
        pass

    def canAddToken(self, activitydiagram_token):
        # TODO: Implement canAddToken method
        pass

    def isReady(self):
        # TODO: Implement isReady method
        pass

    def execute(self):
        # TODO: Implement execute method
        pass

    def terminate(self):
        # TODO: Implement terminate method
        pass
