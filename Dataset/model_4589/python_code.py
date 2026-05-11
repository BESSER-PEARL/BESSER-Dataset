from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class BooleanUnaryOperator(Enum):
    NOT = "NOT"
class IntegerComparisonOperator(Enum):
    SMALLER = "SMALLER"
    SMALLER_EQUALS = "SMALLER_EQUALS"
    EQUALS = "EQUALS"
    GREATER_EQUALS = "GREATER_EQUALS"
    GREATER = "GREATER"
class IntegerCalculationOperator(Enum):
    ADD = "ADD"
    SUBRACT = "SUBRACT"
class BooleanBinaryOperator(Enum):
    AND = "AND"
    OR = "OR"


############################################
# Definition of Classes
############################################

class IntegerExpression:

    pass
class adwithoutruntime_IntegerCalculationExpression(IntegerExpression):

    def __init__(self, operator: str, adwithoutruntime_IntegerCalculationExpression: "adwithoutruntime_IntegerVariable" = None):
        self.operator = operator
        self.adwithoutruntime_IntegerCalculationExpression = adwithoutruntime_IntegerCalculationExpression
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def adwithoutruntime_IntegerCalculationExpression(self):
        return self.__adwithoutruntime_IntegerCalculationExpression

    @adwithoutruntime_IntegerCalculationExpression.setter
    def adwithoutruntime_IntegerCalculationExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adwithoutruntime_IntegerCalculationExpression__adwithoutruntime_IntegerCalculationExpression", None)
        self.__adwithoutruntime_IntegerCalculationExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adwithoutruntime_IntegerVariable29"):
                opp_val = getattr(old_value, "adwithoutruntime_IntegerVariable29", None)
                if opp_val == self:
                    setattr(old_value, "adwithoutruntime_IntegerVariable29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adwithoutruntime_IntegerVariable29"):
                opp_val = getattr(value, "adwithoutruntime_IntegerVariable29", None)
                setattr(value, "adwithoutruntime_IntegerVariable29", self)

class BooleanExpression:

    pass
class adwithoutruntime_BooleanBinaryExpression(BooleanExpression):

    def __init__(self, operator: str, adwithoutruntime_BooleanBinaryExpression: "adwithoutruntime_BooleanVariable" = None, adwithoutruntime_BooleanBinaryExpression37: "adwithoutruntime_BooleanVariable" = None):
        self.operator = operator
        self.adwithoutruntime_BooleanBinaryExpression = adwithoutruntime_BooleanBinaryExpression
        self.adwithoutruntime_BooleanBinaryExpression37 = adwithoutruntime_BooleanBinaryExpression37
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def adwithoutruntime_BooleanBinaryExpression37(self):
        return self.__adwithoutruntime_BooleanBinaryExpression37

    @adwithoutruntime_BooleanBinaryExpression37.setter
    def adwithoutruntime_BooleanBinaryExpression37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adwithoutruntime_BooleanBinaryExpression__adwithoutruntime_BooleanBinaryExpression37", None)
        self.__adwithoutruntime_BooleanBinaryExpression37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adwithoutruntime_BooleanVariable38"):
                opp_val = getattr(old_value, "adwithoutruntime_BooleanVariable38", None)
                if opp_val == self:
                    setattr(old_value, "adwithoutruntime_BooleanVariable38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adwithoutruntime_BooleanVariable38"):
                opp_val = getattr(value, "adwithoutruntime_BooleanVariable38", None)
                setattr(value, "adwithoutruntime_BooleanVariable38", self)

    @property
    def adwithoutruntime_BooleanBinaryExpression(self):
        return self.__adwithoutruntime_BooleanBinaryExpression

    @adwithoutruntime_BooleanBinaryExpression.setter
    def adwithoutruntime_BooleanBinaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adwithoutruntime_BooleanBinaryExpression__adwithoutruntime_BooleanBinaryExpression", None)
        self.__adwithoutruntime_BooleanBinaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adwithoutruntime_BooleanVariable35"):
                opp_val = getattr(old_value, "adwithoutruntime_BooleanVariable35", None)
                if opp_val == self:
                    setattr(old_value, "adwithoutruntime_BooleanVariable35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adwithoutruntime_BooleanVariable35"):
                opp_val = getattr(value, "adwithoutruntime_BooleanVariable35", None)
                setattr(value, "adwithoutruntime_BooleanVariable35", self)

class adwithoutruntime_BooleanUnaryExpression(BooleanExpression):

    def __init__(self, operator: str, adwithoutruntime_BooleanUnaryExpression: "adwithoutruntime_BooleanVariable" = None):
        self.operator = operator
        self.adwithoutruntime_BooleanUnaryExpression = adwithoutruntime_BooleanUnaryExpression
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def adwithoutruntime_BooleanUnaryExpression(self):
        return self.__adwithoutruntime_BooleanUnaryExpression

    @adwithoutruntime_BooleanUnaryExpression.setter
    def adwithoutruntime_BooleanUnaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adwithoutruntime_BooleanUnaryExpression__adwithoutruntime_BooleanUnaryExpression", None)
        self.__adwithoutruntime_BooleanUnaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adwithoutruntime_BooleanVariable33"):
                opp_val = getattr(old_value, "adwithoutruntime_BooleanVariable33", None)
                if opp_val == self:
                    setattr(old_value, "adwithoutruntime_BooleanVariable33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adwithoutruntime_BooleanVariable33"):
                opp_val = getattr(value, "adwithoutruntime_BooleanVariable33", None)
                setattr(value, "adwithoutruntime_BooleanVariable33", self)

class adwithoutruntime_IntegerComparisonExpression(IntegerExpression):

    def __init__(self, operator: str, adwithoutruntime_IntegerComparisonExpression: "adwithoutruntime_BooleanVariable" = None):
        self.operator = operator
        self.adwithoutruntime_IntegerComparisonExpression = adwithoutruntime_IntegerComparisonExpression
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def adwithoutruntime_IntegerComparisonExpression(self):
        return self.__adwithoutruntime_IntegerComparisonExpression

    @adwithoutruntime_IntegerComparisonExpression.setter
    def adwithoutruntime_IntegerComparisonExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adwithoutruntime_IntegerComparisonExpression__adwithoutruntime_IntegerComparisonExpression", None)
        self.__adwithoutruntime_IntegerComparisonExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adwithoutruntime_BooleanVariable31"):
                opp_val = getattr(old_value, "adwithoutruntime_BooleanVariable31", None)
                if opp_val == self:
                    setattr(old_value, "adwithoutruntime_BooleanVariable31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adwithoutruntime_BooleanVariable31"):
                opp_val = getattr(value, "adwithoutruntime_BooleanVariable31", None)
                setattr(value, "adwithoutruntime_BooleanVariable31", self)

class adwithoutruntime_Expression(ABC):

    pass
class Action:

    pass
class adwithoutruntime_OpaqueAction(Action):

    pass
class Expression:

    pass
class adwithoutruntime_BooleanExpression(Expression):

    pass
class adwithoutruntime_IntegerExpression(Expression):

    pass
class Value:

    pass
class adwithoutruntime_IntegerValue(Value):

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class adwithoutruntime_BooleanValue(Value):

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
class adwithoutruntime_IntegerVariable(Variable):

    pass
class adwithoutruntime_Value(ABC):

    pass
class FinalNode:

    pass
class adwithoutruntime_ActivityFinalNode(FinalNode):

    pass
class ControlNode:

    pass
class adwithoutruntime_FinalNode(ControlNode):

    pass
class adwithoutruntime_ForkNode(ControlNode):

    pass
class adwithoutruntime_DecisionNode(ControlNode):

    pass
class adwithoutruntime_MergeNode(ControlNode):

    pass
class adwithoutruntime_JoinNode(ControlNode):

    pass
class adwithoutruntime_InitialNode(ControlNode):

    pass
class adwithoutruntime_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class NamedElement:

    pass
class adwithoutruntime_Activity(NamedElement):

    pass
class ExecutableNode:

    pass
class adwithoutruntime_Action(ExecutableNode):

    pass
class ActivityNode:

    pass
class adwithoutruntime_ExecutableNode(ActivityNode):

    pass
class adwithoutruntime_ControlNode(ActivityNode):

    pass
class adwithoutruntime_BooleanVariable(Variable):

    pass
class ActivityEdge:

    pass
class adwithoutruntime_ControlFlow(ActivityEdge):

    pass
class adwithoutruntime_Variable(ABC):

    def __init__(self, name: str, adwithoutruntime_Variable18: "adwithoutruntime_Value" = None, adwithoutruntime_Variable20: "adwithoutruntime_Value" = None, adwithoutruntime_Variable: "adwithoutruntime_Activity" = None, adwithoutruntime_Variable6: "adwithoutruntime_Activity" = None):
        self.name = name
        self.adwithoutruntime_Variable18 = adwithoutruntime_Variable18
        self.adwithoutruntime_Variable20 = adwithoutruntime_Variable20
        self.adwithoutruntime_Variable = adwithoutruntime_Variable
        self.adwithoutruntime_Variable6 = adwithoutruntime_Variable6
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def adwithoutruntime_Variable6(self):
        return self.__adwithoutruntime_Variable6

    @adwithoutruntime_Variable6.setter
    def adwithoutruntime_Variable6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adwithoutruntime_Variable__adwithoutruntime_Variable6", None)
        self.__adwithoutruntime_Variable6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adwithoutruntime_Activity5"):
                opp_val = getattr(old_value, "adwithoutruntime_Activity5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adwithoutruntime_Activity5"):
                opp_val = getattr(value, "adwithoutruntime_Activity5", None)
                if opp_val is None:
                    setattr(value, "adwithoutruntime_Activity5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def adwithoutruntime_Variable(self):
        return self.__adwithoutruntime_Variable

    @adwithoutruntime_Variable.setter
    def adwithoutruntime_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adwithoutruntime_Variable__adwithoutruntime_Variable", None)
        self.__adwithoutruntime_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adwithoutruntime_Activity3"):
                opp_val = getattr(old_value, "adwithoutruntime_Activity3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adwithoutruntime_Activity3"):
                opp_val = getattr(value, "adwithoutruntime_Activity3", None)
                if opp_val is None:
                    setattr(value, "adwithoutruntime_Activity3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def adwithoutruntime_Variable20(self):
        return self.__adwithoutruntime_Variable20

    @adwithoutruntime_Variable20.setter
    def adwithoutruntime_Variable20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adwithoutruntime_Variable__adwithoutruntime_Variable20", None)
        self.__adwithoutruntime_Variable20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adwithoutruntime_Value21"):
                opp_val = getattr(old_value, "adwithoutruntime_Value21", None)
                if opp_val == self:
                    setattr(old_value, "adwithoutruntime_Value21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adwithoutruntime_Value21"):
                opp_val = getattr(value, "adwithoutruntime_Value21", None)
                setattr(value, "adwithoutruntime_Value21", self)

    @property
    def adwithoutruntime_Variable18(self):
        return self.__adwithoutruntime_Variable18

    @adwithoutruntime_Variable18.setter
    def adwithoutruntime_Variable18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adwithoutruntime_Variable__adwithoutruntime_Variable18", None)
        self.__adwithoutruntime_Variable18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adwithoutruntime_Value"):
                opp_val = getattr(old_value, "adwithoutruntime_Value", None)
                if opp_val == self:
                    setattr(old_value, "adwithoutruntime_Value", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adwithoutruntime_Value"):
                opp_val = getattr(value, "adwithoutruntime_Value", None)
                setattr(value, "adwithoutruntime_Value", self)

class adwithoutruntime_ActivityEdge(NamedElement):

    pass
class adwithoutruntime_ActivityNode(NamedElement):

    pass