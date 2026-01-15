from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class IntegerCalculationOperator(Enum):
    ADD = "ADD"
    SUBRACT = "SUBRACT"
class BooleanUnaryOperator(Enum):
    NOT = "NOT"
class IntegerComparisonOperator(Enum):
    SMALLER = "SMALLER"
    SMALLER_EQUALS = "SMALLER_EQUALS"
    EQUALS = "EQUALS"
    GREATER_EQUALS = "GREATER_EQUALS"
    GREATER = "GREATER"
class BooleanBinaryOperator(Enum):
    AND = "AND"
    OR = "OR"


############################################
# Definition of Classes
############################################

class VariableAssignment:

    pass
class activitydiagram_BooleanVariableAssignment(VariableAssignment):

    pass
class activitydiagram_IntegerVariableAssignment(VariableAssignment):

    pass
class BooleanExpression:

    pass
class activitydiagram_BooleanBinaryExpression(BooleanExpression):

    def __init__(self, operator: str, activitydiagram_BooleanBinaryExpression: "activitydiagram_BooleanExpression" = None, activitydiagram_BooleanBinaryExpression64: "activitydiagram_BooleanExpression" = None):
        self.operator = operator
        self.activitydiagram_BooleanBinaryExpression = activitydiagram_BooleanBinaryExpression
        self.activitydiagram_BooleanBinaryExpression64 = activitydiagram_BooleanBinaryExpression64
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def activitydiagram_BooleanBinaryExpression64(self):
        return self.__activitydiagram_BooleanBinaryExpression64

    @activitydiagram_BooleanBinaryExpression64.setter
    def activitydiagram_BooleanBinaryExpression64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanBinaryExpression__activitydiagram_BooleanBinaryExpression64", None)
        self.__activitydiagram_BooleanBinaryExpression64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_BooleanExpression65"):
                opp_val = getattr(old_value, "activitydiagram_BooleanExpression65", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanExpression65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanExpression65"):
                opp_val = getattr(value, "activitydiagram_BooleanExpression65", None)
                setattr(value, "activitydiagram_BooleanExpression65", self)

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
            if hasattr(old_value, "activitydiagram_BooleanExpression62"):
                opp_val = getattr(old_value, "activitydiagram_BooleanExpression62", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanExpression62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanExpression62"):
                opp_val = getattr(value, "activitydiagram_BooleanExpression62", None)
                setattr(value, "activitydiagram_BooleanExpression62", self)

class activitydiagram_IntegerComparisonExpression(BooleanExpression):

    def __init__(self, operator: str, activitydiagram_IntegerComparisonExpression58: "activitydiagram_IntegerExpression" = None, activitydiagram_IntegerComparisonExpression: "activitydiagram_IntegerExpression" = None):
        self.operator = operator
        self.activitydiagram_IntegerComparisonExpression58 = activitydiagram_IntegerComparisonExpression58
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
            if hasattr(old_value, "activitydiagram_IntegerExpression56"):
                opp_val = getattr(old_value, "activitydiagram_IntegerExpression56", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_IntegerExpression56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_IntegerExpression56"):
                opp_val = getattr(value, "activitydiagram_IntegerExpression56", None)
                setattr(value, "activitydiagram_IntegerExpression56", self)

    @property
    def activitydiagram_IntegerComparisonExpression58(self):
        return self.__activitydiagram_IntegerComparisonExpression58

    @activitydiagram_IntegerComparisonExpression58.setter
    def activitydiagram_IntegerComparisonExpression58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_IntegerComparisonExpression__activitydiagram_IntegerComparisonExpression58", None)
        self.__activitydiagram_IntegerComparisonExpression58 = value
        
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

class activitydiagram_BooleanUnaryExpression(BooleanExpression):

    def __init__(self, operator: str, activitydiagram_BooleanUnaryExpression: "activitydiagram_BooleanExpression" = None):
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
            if hasattr(old_value, "activitydiagram_BooleanExpression"):
                opp_val = getattr(old_value, "activitydiagram_BooleanExpression", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanExpression"):
                opp_val = getattr(value, "activitydiagram_BooleanExpression", None)
                setattr(value, "activitydiagram_BooleanExpression", self)

class IntegerExpression:

    pass
class Variable:

    pass
class activitydiagram_IntegerVariable(Variable, IntegerExpression):

    def __init__(self, initialValue: int, activitydiagram_IntegerVariable: "activitydiagram_IntegerVariableAssignment" = None):
        self.initialValue = initialValue
        self.activitydiagram_IntegerVariable = activitydiagram_IntegerVariable
        
    @property
    def initialValue(self) -> int:
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

class Expression:

    pass
class activitydiagram_IntegerBinaryExpression(Expression, IntegerExpression):

    def __init__(self, operator: str, activitydiagram_IntegerBinaryExpression: "activitydiagram_IntegerExpression" = None, activitydiagram_IntegerBinaryExpression53: "activitydiagram_IntegerExpression" = None):
        self.operator = operator
        self.activitydiagram_IntegerBinaryExpression = activitydiagram_IntegerBinaryExpression
        self.activitydiagram_IntegerBinaryExpression53 = activitydiagram_IntegerBinaryExpression53
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
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
    def activitydiagram_IntegerBinaryExpression53(self):
        return self.__activitydiagram_IntegerBinaryExpression53

    @activitydiagram_IntegerBinaryExpression53.setter
    def activitydiagram_IntegerBinaryExpression53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_IntegerBinaryExpression__activitydiagram_IntegerBinaryExpression53", None)
        self.__activitydiagram_IntegerBinaryExpression53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_IntegerExpression54"):
                opp_val = getattr(old_value, "activitydiagram_IntegerExpression54", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_IntegerExpression54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_IntegerExpression54"):
                opp_val = getattr(value, "activitydiagram_IntegerExpression54", None)
                setattr(value, "activitydiagram_IntegerExpression54", self)

class activitydiagram_Value(Expression):

    pass
class activitydiagram_IntegerExpression(Expression):

    pass
class activitydiagram_BooleanExpression(Expression):

    pass
class activitydiagram_Expression(ABC):

    pass
class FinalNode:

    pass
class activitydiagram_FlowFinalNode(FinalNode):

    pass
class Value:

    pass
class activitydiagram_IntegerValue(Value, IntegerExpression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class activitydiagram_BooleanValue(BooleanExpression, Value):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class activitydiagram_ActivityFinalNode(FinalNode):

    pass
class ControlNode:

    pass
class activitydiagram_JoinNode(ControlNode):

    pass
class activitydiagram_DecisionNode(ControlNode):

    pass
class activitydiagram_ForkNode(ControlNode):

    pass
class activitydiagram_FinalNode(ControlNode):

    pass
class activitydiagram_InitialNode(ControlNode):

    pass
class activitydiagram_MergeNode(ControlNode):

    pass
class ActivityNode:

    pass
class activitydiagram_ControlNode(ActivityNode):

    pass
class activitydiagram_Action(ActivityNode):

    pass
class activitydiagram_BooleanVariable(Variable, BooleanExpression):

    def __init__(self, initialValue: bool, activitydiagram_BooleanVariable: "activitydiagram_ControlFlow" = None, activitydiagram_BooleanVariable67: "activitydiagram_BooleanVariableAssignment" = None):
        self.initialValue = initialValue
        self.activitydiagram_BooleanVariable = activitydiagram_BooleanVariable
        self.activitydiagram_BooleanVariable67 = activitydiagram_BooleanVariable67
        
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
    def activitydiagram_BooleanVariable67(self):
        return self.__activitydiagram_BooleanVariable67

    @activitydiagram_BooleanVariable67.setter
    def activitydiagram_BooleanVariable67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanVariable__activitydiagram_BooleanVariable67", None)
        self.__activitydiagram_BooleanVariable67 = value
        
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

class ActivityEdge:

    pass
class activitydiagram_ControlFlow(ActivityEdge):

    pass
class activitydiagram_AcceptEventAction(ActivityNode):

    pass
class activitydiagram_VariableAssignment(ABC):

    pass
class Action:

    pass
class activitydiagram_OpaqueAction(Action):

    pass
class activitydiagram_Variable(Expression):

    def __init__(self, name: str, activitydiagram_Variable: "activitydiagram_Activity" = None):
        self.name = name
        self.activitydiagram_Variable = activitydiagram_Variable
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
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

class NamedElement:

    pass
class activitydiagram_ActivityNode(NamedElement):

    def __init__(self, running: bool, activitydiagram_ActivityNode: "activitydiagram_ActivityEdge" = None, activitydiagram_ActivityNode10: "activitydiagram_ActivityEdge" = None, ActivityNode: "activitydiagram_Activity" = None, nodes: "activitydiagram_Activity" = None):
        self.running = running
        self.activitydiagram_ActivityNode = activitydiagram_ActivityNode
        self.activitydiagram_ActivityNode10 = activitydiagram_ActivityNode10
        self.ActivityNode = ActivityNode
        self.nodes = nodes
        
    @property
    def running(self) -> bool:
        return self.__running

    @running.setter
    def running(self, running: bool):
        self.__running = running

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

class activitydiagram_ActivityEdge(NamedElement):

    pass
class activitydiagram_Event(NamedElement):

    pass
class activitydiagram_Activity(NamedElement):

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
