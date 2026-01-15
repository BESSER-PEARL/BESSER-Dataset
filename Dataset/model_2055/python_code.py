from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

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
class BooleanUnaryOperator(Enum):
    NOT = "NOT"


############################################
# Definition of Classes
############################################

class activitydiagram_InputValue:

    pass
class Token:

    pass
class activitydiagram_ForkedToken(Token):

    def __init__(self, remainingOffersCount: int, activitydiagram_ForkedToken: "activitydiagram_Token" = None):
        self.remainingOffersCount = remainingOffersCount
        self.activitydiagram_ForkedToken = activitydiagram_ForkedToken
        
    @property
    def remainingOffersCount(self) -> int:
        return self.__remainingOffersCount

    @remainingOffersCount.setter
    def remainingOffersCount(self, remainingOffersCount: int):
        self.__remainingOffersCount = remainingOffersCount

    @property
    def activitydiagram_ForkedToken(self):
        return self.__activitydiagram_ForkedToken

    @activitydiagram_ForkedToken.setter
    def activitydiagram_ForkedToken(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ForkedToken__activitydiagram_ForkedToken", None)
        self.__activitydiagram_ForkedToken = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_Token58"):
                opp_val = getattr(old_value, "activitydiagram_Token58", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_Token58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Token58"):
                opp_val = getattr(value, "activitydiagram_Token58", None)
                setattr(value, "activitydiagram_Token58", self)

class activitydiagram_ControlToken(Token):

    pass
class activitydiagram_Input:

    pass
class BooleanExpression:

    pass
class activitydiagram_BooleanBinaryExpression(BooleanExpression):

    def __init__(self, operator: str, activitydiagram_BooleanBinaryExpression: "activitydiagram_BooleanVariable" = None, activitydiagram_BooleanBinaryExpression42: "activitydiagram_BooleanVariable" = None):
        self.operator = operator
        self.activitydiagram_BooleanBinaryExpression = activitydiagram_BooleanBinaryExpression
        self.activitydiagram_BooleanBinaryExpression42 = activitydiagram_BooleanBinaryExpression42
        
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
            if hasattr(old_value, "activitydiagram_BooleanVariable40"):
                opp_val = getattr(old_value, "activitydiagram_BooleanVariable40", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanVariable40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanVariable40"):
                opp_val = getattr(value, "activitydiagram_BooleanVariable40", None)
                setattr(value, "activitydiagram_BooleanVariable40", self)

    @property
    def activitydiagram_BooleanBinaryExpression42(self):
        return self.__activitydiagram_BooleanBinaryExpression42

    @activitydiagram_BooleanBinaryExpression42.setter
    def activitydiagram_BooleanBinaryExpression42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanBinaryExpression__activitydiagram_BooleanBinaryExpression42", None)
        self.__activitydiagram_BooleanBinaryExpression42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_BooleanVariable43"):
                opp_val = getattr(old_value, "activitydiagram_BooleanVariable43", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanVariable43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanVariable43"):
                opp_val = getattr(value, "activitydiagram_BooleanVariable43", None)
                setattr(value, "activitydiagram_BooleanVariable43", self)

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
            if hasattr(old_value, "activitydiagram_BooleanVariable38"):
                opp_val = getattr(old_value, "activitydiagram_BooleanVariable38", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanVariable38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanVariable38"):
                opp_val = getattr(value, "activitydiagram_BooleanVariable38", None)
                setattr(value, "activitydiagram_BooleanVariable38", self)

class IntegerExpression:

    pass
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
            if hasattr(old_value, "activitydiagram_IntegerVariable34"):
                opp_val = getattr(old_value, "activitydiagram_IntegerVariable34", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_IntegerVariable34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_IntegerVariable34"):
                opp_val = getattr(value, "activitydiagram_IntegerVariable34", None)
                setattr(value, "activitydiagram_IntegerVariable34", self)

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
            if hasattr(old_value, "activitydiagram_BooleanVariable36"):
                opp_val = getattr(old_value, "activitydiagram_BooleanVariable36", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanVariable36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanVariable36"):
                opp_val = getattr(value, "activitydiagram_BooleanVariable36", None)
                setattr(value, "activitydiagram_BooleanVariable36", self)

class activitydiagram_Value(ABC):

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

class Variable:

    pass
class activitydiagram_IntegerVariable(Variable):

    pass
class ActivityNode:

    pass
class activitydiagram_ControlNode(ActivityNode):

    pass
class activitydiagram_BooleanVariable(Variable):

    pass
class ActivityEdge:

    pass
class activitydiagram_ControlFlow(ActivityEdge):

    pass
class activitydiagram_Offer:

    pass
class FinalNode:

    pass
class activitydiagram_ActivityFinalNode(FinalNode):

    pass
class ControlNode:

    pass
class activitydiagram_FinalNode(ControlNode):

    pass
class activitydiagram_MergeNode(ControlNode):

    pass
class activitydiagram_DecisionNode(ControlNode):

    pass
class activitydiagram_ForkNode(ControlNode):

    pass
class activitydiagram_JoinNode(ControlNode):

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
class activitydiagram_ExecutableNode(ActivityNode):

    pass
class activitydiagram_Trace:

    pass
class activitydiagram_Token(ABC):

    pass
class activitydiagram_Variable(ABC):

    def __init__(self, name: str, activitydiagram_Variable: "activitydiagram_Activity" = None, activitydiagram_Variable6: "activitydiagram_Activity" = None, activitydiagram_Variable25: "activitydiagram_Value" = None, activitydiagram_Variable23: "activitydiagram_Value" = None, activitydiagram_Variable54: "activitydiagram_InputValue" = None):
        self.name = name
        self.activitydiagram_Variable = activitydiagram_Variable
        self.activitydiagram_Variable6 = activitydiagram_Variable6
        self.activitydiagram_Variable25 = activitydiagram_Variable25
        self.activitydiagram_Variable23 = activitydiagram_Variable23
        self.activitydiagram_Variable54 = activitydiagram_Variable54
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def activitydiagram_Variable23(self):
        return self.__activitydiagram_Variable23

    @activitydiagram_Variable23.setter
    def activitydiagram_Variable23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Variable__activitydiagram_Variable23", None)
        self.__activitydiagram_Variable23 = value
        
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
    def activitydiagram_Variable54(self):
        return self.__activitydiagram_Variable54

    @activitydiagram_Variable54.setter
    def activitydiagram_Variable54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Variable__activitydiagram_Variable54", None)
        self.__activitydiagram_Variable54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_InputValue53"):
                opp_val = getattr(old_value, "activitydiagram_InputValue53", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_InputValue53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_InputValue53"):
                opp_val = getattr(value, "activitydiagram_InputValue53", None)
                setattr(value, "activitydiagram_InputValue53", self)

    @property
    def activitydiagram_Variable25(self):
        return self.__activitydiagram_Variable25

    @activitydiagram_Variable25.setter
    def activitydiagram_Variable25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Variable__activitydiagram_Variable25", None)
        self.__activitydiagram_Variable25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_Value26"):
                opp_val = getattr(old_value, "activitydiagram_Value26", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_Value26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Value26"):
                opp_val = getattr(value, "activitydiagram_Value26", None)
                setattr(value, "activitydiagram_Value26", self)

class NamedElement:

    pass
class activitydiagram_ActivityEdge(NamedElement):

    pass
class activitydiagram_ActivityNode(NamedElement):

    def __init__(self, running: bool, ActivityNode: "activitydiagram_Activity" = None, target: set["activitydiagram_ActivityEdge"] = None, nodes: "activitydiagram_Activity" = None, holder: set["activitydiagram_Token"] = None, ActivityNode15: "activitydiagram_ActivityEdge" = None, ActivityNode17: "activitydiagram_ActivityEdge" = None, source: set["activitydiagram_ActivityEdge"] = None, ActivityNode47: "activitydiagram_Token" = None, activitydiagram_ActivityNode: "activitydiagram_Trace" = None):
        self.running = running
        self.ActivityNode = ActivityNode
        self.target = target if target is not None else set()
        self.nodes = nodes
        self.holder = holder if holder is not None else set()
        self.ActivityNode15 = ActivityNode15
        self.ActivityNode17 = ActivityNode17
        self.source = source if source is not None else set()
        self.ActivityNode47 = ActivityNode47
        self.activitydiagram_ActivityNode = activitydiagram_ActivityNode
        
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
                if hasattr(item, "ActivityEdge11"):
                    opp_val = getattr(item, "ActivityEdge11", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityEdge11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityEdge11"):
                    opp_val = getattr(item, "ActivityEdge11", None)
                    
                    setattr(item, "ActivityEdge11", self)
                    

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
    def ActivityNode15(self):
        return self.__ActivityNode15

    @ActivityNode15.setter
    def ActivityNode15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__ActivityNode15", None)
        self.__ActivityNode15 = value
        
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
    def ActivityNode47(self):
        return self.__ActivityNode47

    @ActivityNode47.setter
    def ActivityNode47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__ActivityNode47", None)
        self.__ActivityNode47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "heldTokens"):
                opp_val = getattr(old_value, "heldTokens", None)
                if opp_val == self:
                    setattr(old_value, "heldTokens", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "heldTokens"):
                opp_val = getattr(value, "heldTokens", None)
                setattr(value, "heldTokens", self)

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
            if hasattr(old_value, "activitydiagram_Trace49"):
                opp_val = getattr(old_value, "activitydiagram_Trace49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Trace49"):
                opp_val = getattr(value, "activitydiagram_Trace49", None)
                if opp_val is None:
                    setattr(value, "activitydiagram_Trace49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def holder(self):
        return self.__holder

    @holder.setter
    def holder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__holder", None)
        self.__holder = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Token"):
                    opp_val = getattr(item, "Token", None)
                    
                    if opp_val == self:
                        setattr(item, "Token", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Token"):
                    opp_val = getattr(item, "Token", None)
                    
                    setattr(item, "Token", self)
                    

    @property
    def ActivityNode17(self):
        return self.__ActivityNode17

    @ActivityNode17.setter
    def ActivityNode17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__ActivityNode17", None)
        self.__ActivityNode17 = value
        
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

class activitydiagram_Activity(NamedElement):

    pass