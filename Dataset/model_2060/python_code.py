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

class activitydiagram_InputValue:

    pass
class activitydiagram_Input:

    pass
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
            if hasattr(old_value, "activitydiagram_BooleanVariable31"):
                opp_val = getattr(old_value, "activitydiagram_BooleanVariable31", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanVariable31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanVariable31"):
                opp_val = getattr(value, "activitydiagram_BooleanVariable31", None)
                setattr(value, "activitydiagram_BooleanVariable31", self)

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
            if hasattr(old_value, "activitydiagram_IntegerVariable29"):
                opp_val = getattr(old_value, "activitydiagram_IntegerVariable29", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_IntegerVariable29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_IntegerVariable29"):
                opp_val = getattr(value, "activitydiagram_IntegerVariable29", None)
                setattr(value, "activitydiagram_IntegerVariable29", self)

class BooleanExpression:

    pass
class activitydiagram_BooleanBinaryExpression(BooleanExpression):

    def __init__(self, operator: str, activitydiagram_BooleanBinaryExpression: "activitydiagram_BooleanVariable" = None, activitydiagram_BooleanBinaryExpression37: "activitydiagram_BooleanVariable" = None):
        self.operator = operator
        self.activitydiagram_BooleanBinaryExpression = activitydiagram_BooleanBinaryExpression
        self.activitydiagram_BooleanBinaryExpression37 = activitydiagram_BooleanBinaryExpression37
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def activitydiagram_BooleanBinaryExpression37(self):
        return self.__activitydiagram_BooleanBinaryExpression37

    @activitydiagram_BooleanBinaryExpression37.setter
    def activitydiagram_BooleanBinaryExpression37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanBinaryExpression__activitydiagram_BooleanBinaryExpression37", None)
        self.__activitydiagram_BooleanBinaryExpression37 = value
        
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
            if hasattr(old_value, "activitydiagram_BooleanVariable35"):
                opp_val = getattr(old_value, "activitydiagram_BooleanVariable35", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanVariable35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanVariable35"):
                opp_val = getattr(value, "activitydiagram_BooleanVariable35", None)
                setattr(value, "activitydiagram_BooleanVariable35", self)

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
            if hasattr(old_value, "activitydiagram_BooleanVariable33"):
                opp_val = getattr(old_value, "activitydiagram_BooleanVariable33", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanVariable33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanVariable33"):
                opp_val = getattr(value, "activitydiagram_BooleanVariable33", None)
                setattr(value, "activitydiagram_BooleanVariable33", self)

class Variable:

    pass
class activitydiagram_IntegerVariable(Variable):

    pass
class activitydiagram_Value(ABC):

    pass
class FinalNode:

    pass
class activitydiagram_ActivityFinalNode(FinalNode):

    pass
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
class Action:

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
class ControlNode:

    pass
class activitydiagram_DecisionNode(ControlNode):

    pass
class activitydiagram_FinalNode(ControlNode):

    pass
class activitydiagram_ForkNode(ControlNode):

    pass
class activitydiagram_JoinNode(ControlNode):

    pass
class activitydiagram_MergeNode(ControlNode):

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

class activitydiagram_Variable(ABC):

    def __init__(self, name: str, activitydiagram_Variable: "activitydiagram_Activity" = None, activitydiagram_Variable6: "activitydiagram_Activity" = None, activitydiagram_Variable18: "activitydiagram_Value" = None, activitydiagram_Variable20: "activitydiagram_Value" = None, activitydiagram_Variable43: "activitydiagram_InputValue" = None):
        self.name = name
        self.activitydiagram_Variable = activitydiagram_Variable
        self.activitydiagram_Variable6 = activitydiagram_Variable6
        self.activitydiagram_Variable18 = activitydiagram_Variable18
        self.activitydiagram_Variable20 = activitydiagram_Variable20
        self.activitydiagram_Variable43 = activitydiagram_Variable43
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def activitydiagram_Variable43(self):
        return self.__activitydiagram_Variable43

    @activitydiagram_Variable43.setter
    def activitydiagram_Variable43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Variable__activitydiagram_Variable43", None)
        self.__activitydiagram_Variable43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_InputValue42"):
                opp_val = getattr(old_value, "activitydiagram_InputValue42", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_InputValue42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_InputValue42"):
                opp_val = getattr(value, "activitydiagram_InputValue42", None)
                setattr(value, "activitydiagram_InputValue42", self)

    @property
    def activitydiagram_Variable18(self):
        return self.__activitydiagram_Variable18

    @activitydiagram_Variable18.setter
    def activitydiagram_Variable18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Variable__activitydiagram_Variable18", None)
        self.__activitydiagram_Variable18 = value
        
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
    def activitydiagram_Variable20(self):
        return self.__activitydiagram_Variable20

    @activitydiagram_Variable20.setter
    def activitydiagram_Variable20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Variable__activitydiagram_Variable20", None)
        self.__activitydiagram_Variable20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_Value21"):
                opp_val = getattr(old_value, "activitydiagram_Value21", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_Value21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Value21"):
                opp_val = getattr(value, "activitydiagram_Value21", None)
                setattr(value, "activitydiagram_Value21", self)

class NamedElement:

    pass
class activitydiagram_ActivityNode(NamedElement):

    def __init__(self, running: bool, nodes: "activitydiagram_Activity" = None, ActivityNode: "activitydiagram_Activity" = None, source: set["activitydiagram_ActivityEdge"] = None, target: set["activitydiagram_ActivityEdge"] = None, ActivityNode12: "activitydiagram_ActivityEdge" = None, ActivityNode14: "activitydiagram_ActivityEdge" = None):
        self.running = running
        self.nodes = nodes
        self.ActivityNode = ActivityNode
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.ActivityNode12 = ActivityNode12
        self.ActivityNode14 = ActivityNode14
        
    @property
    def running(self) -> bool:
        return self.__running

    @running.setter
    def running(self, running: bool):
        self.__running = running

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityEdge"):
                    opp_val = getattr(item, "ActivityEdge", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityEdge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityEdge"):
                    opp_val = getattr(item, "ActivityEdge", None)
                    
                    setattr(item, "ActivityEdge", self)
                    

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityEdge9"):
                    opp_val = getattr(item, "ActivityEdge9", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityEdge9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityEdge9"):
                    opp_val = getattr(item, "ActivityEdge9", None)
                    
                    setattr(item, "ActivityEdge9", self)
                    

    @property
    def ActivityNode14(self):
        return self.__ActivityNode14

    @ActivityNode14.setter
    def ActivityNode14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__ActivityNode14", None)
        self.__ActivityNode14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incoming"):
                opp_val = getattr(old_value, "incoming", None)
                if opp_val == self:
                    setattr(old_value, "incoming", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incoming"):
                opp_val = getattr(value, "incoming", None)
                setattr(value, "incoming", self)

    @property
    def ActivityNode12(self):
        return self.__ActivityNode12

    @ActivityNode12.setter
    def ActivityNode12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__ActivityNode12", None)
        self.__ActivityNode12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoing"):
                opp_val = getattr(old_value, "outgoing", None)
                if opp_val == self:
                    setattr(old_value, "outgoing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoing"):
                opp_val = getattr(value, "outgoing", None)
                setattr(value, "outgoing", self)

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

class activitydiagram_ActivityEdge(NamedElement):

    pass
class activitydiagram_Activity(NamedElement):

    pass