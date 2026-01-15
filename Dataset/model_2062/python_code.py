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
    ADD = "ADD"
    SUBRACT = "SUBRACT"
class IntegerComparisonOperator(Enum):
    SMALLER = "SMALLER"
    SMALLER_EQUALS = "SMALLER_EQUALS"
    EQUALS = "EQUALS"
    GREATER_EQUALS = "GREATER_EQUALS"
    GREATER = "GREATER"


############################################
# Definition of Classes
############################################

class activitydiagram_InputValue:

    pass
class Signal:

    pass
class activitydiagram_SignalEvent(Signal):

    pass
class activitydiagram_Input:

    pass
class BooleanExpression:

    pass
class activitydiagram_BooleanBinaryExpression(BooleanExpression):

    def __init__(self, operator: str, activitydiagram_BooleanBinaryExpression: "activitydiagram_BooleanVariable" = None, activitydiagram_BooleanBinaryExpression44: "activitydiagram_BooleanVariable" = None):
        self.operator = operator
        self.activitydiagram_BooleanBinaryExpression = activitydiagram_BooleanBinaryExpression
        self.activitydiagram_BooleanBinaryExpression44 = activitydiagram_BooleanBinaryExpression44
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
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
            if hasattr(old_value, "activitydiagram_BooleanVariable42"):
                opp_val = getattr(old_value, "activitydiagram_BooleanVariable42", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanVariable42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanVariable42"):
                opp_val = getattr(value, "activitydiagram_BooleanVariable42", None)
                setattr(value, "activitydiagram_BooleanVariable42", self)

    @property
    def activitydiagram_BooleanBinaryExpression44(self):
        return self.__activitydiagram_BooleanBinaryExpression44

    @activitydiagram_BooleanBinaryExpression44.setter
    def activitydiagram_BooleanBinaryExpression44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanBinaryExpression__activitydiagram_BooleanBinaryExpression44", None)
        self.__activitydiagram_BooleanBinaryExpression44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_BooleanVariable45"):
                opp_val = getattr(old_value, "activitydiagram_BooleanVariable45", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanVariable45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanVariable45"):
                opp_val = getattr(value, "activitydiagram_BooleanVariable45", None)
                setattr(value, "activitydiagram_BooleanVariable45", self)

class activitydiagram_BooleanUnaryExpression(BooleanExpression):

    def __init__(self, operator: str, activitydiagram_BooleanUnaryExpression: "activitydiagram_BooleanVariable" = None):
        self.operator = operator
        self.activitydiagram_BooleanUnaryExpression = activitydiagram_BooleanUnaryExpression
        
    @property
    def operator(self) -> str:
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
            if hasattr(old_value, "activitydiagram_BooleanVariable40"):
                opp_val = getattr(old_value, "activitydiagram_BooleanVariable40", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanVariable40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanVariable40"):
                opp_val = getattr(value, "activitydiagram_BooleanVariable40", None)
                setattr(value, "activitydiagram_BooleanVariable40", self)

class IntegerExpression:

    pass
class activitydiagram_IntegerComparisonExpression(IntegerExpression):

    def __init__(self, operator: str, activitydiagram_IntegerComparisonExpression: "activitydiagram_BooleanVariable" = None):
        self.operator = operator
        self.activitydiagram_IntegerComparisonExpression = activitydiagram_IntegerComparisonExpression
        
    @property
    def operator(self) -> str:
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
            if hasattr(old_value, "activitydiagram_BooleanVariable38"):
                opp_val = getattr(old_value, "activitydiagram_BooleanVariable38", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanVariable38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanVariable38"):
                opp_val = getattr(value, "activitydiagram_BooleanVariable38", None)
                setattr(value, "activitydiagram_BooleanVariable38", self)

class activitydiagram_IntegerCalculationExpression(IntegerExpression):

    def __init__(self, operator: str, activitydiagram_IntegerCalculationExpression: "activitydiagram_IntegerVariable" = None):
        self.operator = operator
        self.activitydiagram_IntegerCalculationExpression = activitydiagram_IntegerCalculationExpression
        
    @property
    def operator(self) -> str:
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
            if hasattr(old_value, "activitydiagram_IntegerVariable36"):
                opp_val = getattr(old_value, "activitydiagram_IntegerVariable36", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_IntegerVariable36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_IntegerVariable36"):
                opp_val = getattr(value, "activitydiagram_IntegerVariable36", None)
                setattr(value, "activitydiagram_IntegerVariable36", self)

class Expression:

    pass
class activitydiagram_BooleanExpression(Expression):

    pass
class activitydiagram_IntegerExpression(Expression):

    pass
class ControlNode:

    pass
class activitydiagram_InitialNode(ControlNode):

    pass
class activitydiagram_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Value:

    pass
class activitydiagram_IntegerValue(Value):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class activitydiagram_BooleanValue(Value):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class activitydiagram_Expression(ABC):

    pass
class Variable:

    pass
class activitydiagram_IntegerVariable(Variable):

    pass
class activitydiagram_Value(ABC):

    pass
class activitydiagram_DecisionNode(ControlNode):

    pass
class activitydiagram_MergeNode(ControlNode):

    pass
class activitydiagram_JoinNode(ControlNode):

    pass
class activitydiagram_ForkNode(ControlNode):

    pass
class FinalNode:

    pass
class activitydiagram_ActivityFinalNode(FinalNode):

    pass
class activitydiagram_FinalNode(ControlNode):

    pass
class Action:

    pass
class activitydiagram_SendSignalAction(Action):

    pass
class activitydiagram_AcceptEventAction(Action):

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
class activitydiagram_Variable(ABC):

    def __init__(self, name: str, activitydiagram_Variable: "activitydiagram_Activity" = None, activitydiagram_Variable7: "activitydiagram_Activity" = None, activitydiagram_Variable28: "activitydiagram_Value" = None, activitydiagram_Variable50: "activitydiagram_InputValue" = None):
        self.name = name
        self.activitydiagram_Variable = activitydiagram_Variable
        self.activitydiagram_Variable7 = activitydiagram_Variable7
        self.activitydiagram_Variable28 = activitydiagram_Variable28
        self.activitydiagram_Variable50 = activitydiagram_Variable50
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def activitydiagram_Variable7(self):
        return self.__activitydiagram_Variable7

    @activitydiagram_Variable7.setter
    def activitydiagram_Variable7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Variable__activitydiagram_Variable7", None)
        self.__activitydiagram_Variable7 = value
        
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
    def activitydiagram_Variable50(self):
        return self.__activitydiagram_Variable50

    @activitydiagram_Variable50.setter
    def activitydiagram_Variable50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Variable__activitydiagram_Variable50", None)
        self.__activitydiagram_Variable50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_InputValue49"):
                opp_val = getattr(old_value, "activitydiagram_InputValue49", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_InputValue49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_InputValue49"):
                opp_val = getattr(value, "activitydiagram_InputValue49", None)
                setattr(value, "activitydiagram_InputValue49", self)

    @property
    def activitydiagram_Variable28(self):
        return self.__activitydiagram_Variable28

    @activitydiagram_Variable28.setter
    def activitydiagram_Variable28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Variable__activitydiagram_Variable28", None)
        self.__activitydiagram_Variable28 = value
        
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

class NamedElement:

    pass
class activitydiagram_ActivityEdge(NamedElement):

    pass
class activitydiagram_ActivityNode(NamedElement):

    pass
class activitydiagram_Signal(NamedElement):

    pass
class activitydiagram_Activity(NamedElement):

    pass