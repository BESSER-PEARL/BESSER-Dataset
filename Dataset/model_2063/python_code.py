from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class BooleanUnaryOperator(Enum):
    NOT = "NOT"
class BooleanBinaryOperator(Enum):
    AND = "AND"
    OR = "OR"
class IntegerCalculationOperator(Enum):
    SUBRACT = "SUBRACT"
    ADD = "ADD"
class IntegerComparisonOperator(Enum):
    SMALLER = "SMALLER"
    SMALLER_EQUALS = "SMALLER_EQUALS"
    EQUALS = "EQUALS"
    GREATER_EQUALS = "GREATER_EQUALS"
    GREATER = "GREATER"


############################################
# Definition of Classes
############################################

class BooleanExpression:

    pass
class activitydiagram_BooleanBinaryExpression(BooleanExpression):

    def __init__(self, operator: str, activitydiagram_BooleanBinaryExpression: "activitydiagram_BooleanVariable" = None, activitydiagram_BooleanBinaryExpression36: "activitydiagram_BooleanVariable" = None):
        self.operator = operator
        self.activitydiagram_BooleanBinaryExpression = activitydiagram_BooleanBinaryExpression
        self.activitydiagram_BooleanBinaryExpression36 = activitydiagram_BooleanBinaryExpression36
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def activitydiagram_BooleanBinaryExpression36(self):
        return self.__activitydiagram_BooleanBinaryExpression36

    @activitydiagram_BooleanBinaryExpression36.setter
    def activitydiagram_BooleanBinaryExpression36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanBinaryExpression__activitydiagram_BooleanBinaryExpression36", None)
        self.__activitydiagram_BooleanBinaryExpression36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_BooleanVariable37"):
                opp_val = getattr(old_value, "activitydiagram_BooleanVariable37", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanVariable37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanVariable37"):
                opp_val = getattr(value, "activitydiagram_BooleanVariable37", None)
                setattr(value, "activitydiagram_BooleanVariable37", self)

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
            if hasattr(old_value, "activitydiagram_BooleanVariable34"):
                opp_val = getattr(old_value, "activitydiagram_BooleanVariable34", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanVariable34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanVariable34"):
                opp_val = getattr(value, "activitydiagram_BooleanVariable34", None)
                setattr(value, "activitydiagram_BooleanVariable34", self)

class activitydiagram_BooleanUnaryExpression(BooleanExpression):

    def __init__(self, operator: str, activitydiagram_BooleanUnaryExpression: "activitydiagram_BooleanVariable" = None):
        self.operator = operator
        self.activitydiagram_BooleanUnaryExpression = activitydiagram_BooleanUnaryExpression
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
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
            if hasattr(old_value, "activitydiagram_BooleanVariable32"):
                opp_val = getattr(old_value, "activitydiagram_BooleanVariable32", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanVariable32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanVariable32"):
                opp_val = getattr(value, "activitydiagram_BooleanVariable32", None)
                setattr(value, "activitydiagram_BooleanVariable32", self)

class Signal:

    pass
class activitydiagram_SignalEvent(Signal):

    pass
class activitydiagram_Input:

    pass
class activitydiagram_InputValue:

    pass
class FinalNode:

    pass
class activitydiagram_ActivityFinalNode(FinalNode):

    pass
class ControlNode:

    pass
class activitydiagram_JoinNode(ControlNode):

    pass
class activitydiagram_FinalNode(ControlNode):

    pass
class activitydiagram_ForkNode(ControlNode):

    pass
class activitydiagram_MergeNode(ControlNode):

    pass
class activitydiagram_DecisionNode(ControlNode):

    pass
class activitydiagram_InitialNode(ControlNode):

    pass
class activitydiagram_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class IntegerExpression:

    pass
class activitydiagram_IntegerComparisonExpression(IntegerExpression):

    def __init__(self, operator: str, activitydiagram_IntegerComparisonExpression: "activitydiagram_BooleanVariable" = None):
        self.operator = operator
        self.activitydiagram_IntegerComparisonExpression = activitydiagram_IntegerComparisonExpression
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
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
            if hasattr(old_value, "activitydiagram_BooleanVariable30"):
                opp_val = getattr(old_value, "activitydiagram_BooleanVariable30", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanVariable30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanVariable30"):
                opp_val = getattr(value, "activitydiagram_BooleanVariable30", None)
                setattr(value, "activitydiagram_BooleanVariable30", self)

class activitydiagram_IntegerCalculationExpression(IntegerExpression):

    def __init__(self, operator: str, activitydiagram_IntegerCalculationExpression: "activitydiagram_IntegerVariable" = None):
        self.operator = operator
        self.activitydiagram_IntegerCalculationExpression = activitydiagram_IntegerCalculationExpression
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def activitydiagram_IntegerCalculationExpression(self):
        return self.__activitydiagram_IntegerCalculationExpression

    @activitydiagram_IntegerCalculationExpression.setter
    def activitydiagram_IntegerCalculationExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_IntegerCalculationExpression__activitydiagram_IntegerCalculationExpression", None)
        self.__activitydiagram_IntegerCalculationExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_IntegerVariable28"):
                opp_val = getattr(old_value, "activitydiagram_IntegerVariable28", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_IntegerVariable28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_IntegerVariable28"):
                opp_val = getattr(value, "activitydiagram_IntegerVariable28", None)
                setattr(value, "activitydiagram_IntegerVariable28", self)

class Expression:

    pass
class activitydiagram_BooleanExpression(Expression):

    pass
class activitydiagram_IntegerExpression(Expression):

    pass
class Value:

    pass
class activitydiagram_IntegerValue(Value):

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class activitydiagram_BooleanValue(Value):

    def __init__(self, value: bool):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value


class Variable:

    pass
class activitydiagram_IntegerVariable(Variable):

    pass
class activitydiagram_Value(ABC):

    pass
class NamedElement:

    pass
class activitydiagram_ActivityNode(NamedElement):

    pass
class activitydiagram_Activity(NamedElement):

    pass
class activitydiagram_Expression(ABC):

    pass
class Action:

    pass
class activitydiagram_AcceptEventAction(Action):

    pass
class activitydiagram_SendSignalAction(Action):

    pass
class activitydiagram_OpaqueAction(Action):

    pass
class ExecutableNode:

    pass
class activitydiagram_Action(ExecutableNode):

    pass
class ActivityNode:

    pass
class activitydiagram_ExecutableNode(ActivityNode):

    pass
class activitydiagram_ControlNode(ActivityNode):

    pass
class activitydiagram_BooleanVariable(Variable):

    pass
class ActivityEdge:

    pass
class activitydiagram_ControlFlow(ActivityEdge):

    pass
class activitydiagram_Signal(NamedElement):

    pass
class activitydiagram_Variable(ABC):

    def __init__(self, name: str, activitydiagram_Variable: "activitydiagram_Activity" = None, activitydiagram_Variable6: "activitydiagram_Activity" = None, activitydiagram_Variable20: "activitydiagram_Value" = None, activitydiagram_Variable42: "activitydiagram_InputValue" = None):
        self.name = name
        self.activitydiagram_Variable = activitydiagram_Variable
        self.activitydiagram_Variable6 = activitydiagram_Variable6
        self.activitydiagram_Variable20 = activitydiagram_Variable20
        self.activitydiagram_Variable42 = activitydiagram_Variable42
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def activitydiagram_Variable20(self):
        return self.__activitydiagram_Variable20

    @activitydiagram_Variable20.setter
    def activitydiagram_Variable20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Variable__activitydiagram_Variable20", None)
        self.__activitydiagram_Variable20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_Value"):
                opp_val = getattr(old_value, "activitydiagram_Value", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_Value", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Value"):
                opp_val = getattr(value, "activitydiagram_Value", None)
                setattr(value, "activitydiagram_Value", self)

    @property
    def activitydiagram_Variable42(self):
        return self.__activitydiagram_Variable42

    @activitydiagram_Variable42.setter
    def activitydiagram_Variable42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Variable__activitydiagram_Variable42", None)
        self.__activitydiagram_Variable42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_InputValue41"):
                opp_val = getattr(old_value, "activitydiagram_InputValue41", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_InputValue41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_InputValue41"):
                opp_val = getattr(value, "activitydiagram_InputValue41", None)
                setattr(value, "activitydiagram_InputValue41", self)

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
    def activitydiagram_Variable6(self):
        return self.__activitydiagram_Variable6

    @activitydiagram_Variable6.setter
    def activitydiagram_Variable6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Variable__activitydiagram_Variable6", None)
        self.__activitydiagram_Variable6 = value
        
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

class activitydiagram_ActivityEdge(NamedElement):

    pass