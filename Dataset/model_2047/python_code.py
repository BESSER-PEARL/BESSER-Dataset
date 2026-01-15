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
class activitydiagram_InputValue:

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
class activitydiagram_Value(ABC):

    pass
class activitydiagram_IntegerVariable(Variable):

    pass
class ControlNode:

    pass
class activitydiagram_JoinNode(ControlNode):

    def __init__(self):
        
    def execute(self):
        # TODO: Implement execute method
        pass

class activitydiagram_MergeNode(ControlNode):

    def __init__(self):
        
    def execute(self):
        # TODO: Implement execute method
        pass

class activitydiagram_DecisionNode(ControlNode):

    def __init__(self):
        
    def execute(self):
        # TODO: Implement execute method
        pass

class activitydiagram_ForkNode(ControlNode):

    def __init__(self):
        
    def execute(self):
        # TODO: Implement execute method
        pass

class activitydiagram_InitialNode(ControlNode):

    def __init__(self):
        
    def execute(self):
        # TODO: Implement execute method
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

    def __init__(self, activitydiagram_OpaqueAction: set["activitydiagram_Expression"] = None):
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
                if hasattr(item, "activitydiagram_Expression"):
                    opp_val = getattr(item, "activitydiagram_Expression", None)
                    
                    if opp_val == self:
                        setattr(item, "activitydiagram_Expression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activitydiagram_Expression"):
                    opp_val = getattr(item, "activitydiagram_Expression", None)
                    
                    setattr(item, "activitydiagram_Expression", self)
                    

    def execute(self):
        # TODO: Implement execute method
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
class FinalNode:

    pass
class activitydiagram_ActivityFinalNode(FinalNode):

    def __init__(self):
        
    def execute(self):
        # TODO: Implement execute method
        pass

class activitydiagram_FinalNode(ControlNode):

    pass
class activitydiagram_Offer:

    pass
class activitydiagram_Token(ABC):

    pass
class activitydiagram_BooleanVariable(Variable):

    pass
class ActivityEdge:

    pass
class activitydiagram_ControlFlow(ActivityEdge):

    pass
class activitydiagram_Trace:

    pass
class NamedElement:

    pass
class activitydiagram_ActivityNode(NamedElement):

    def __init__(self, running: bool, ActivityNode: "activitydiagram_Activity" = None, nodes: "activitydiagram_Activity" = None, source: set["activitydiagram_ActivityEdge"] = None, target: set["activitydiagram_ActivityEdge"] = None, holder: set["activitydiagram_Token"] = None, ActivityNode15: "activitydiagram_ActivityEdge" = None, ActivityNode17: "activitydiagram_ActivityEdge" = None, ActivityNode47: "activitydiagram_Token" = None, activitydiagram_ActivityNode: "activitydiagram_Trace" = None):
        self.running = running
        self.ActivityNode = ActivityNode
        self.nodes = nodes
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.holder = holder if holder is not None else set()
        self.ActivityNode15 = ActivityNode15
        self.ActivityNode17 = ActivityNode17
        self.ActivityNode47 = ActivityNode47
        self.activitydiagram_ActivityNode = activitydiagram_ActivityNode
        
    @property
    def running(self) -> bool:
        return self.__running

    @running.setter
    def running(self, running: bool):
        self.__running = running

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

    def terminate(self):
        # TODO: Implement terminate method
        pass

    def execute(self):
        # TODO: Implement execute method
        pass

class activitydiagram_ActivityEdge(NamedElement):

    def __init__(self, activitydiagram_ActivityEdge: "activitydiagram_Activity" = None, ActivityEdge: "activitydiagram_ActivityNode" = None, ActivityEdge11: "activitydiagram_ActivityNode" = None, outgoing: "activitydiagram_ActivityNode" = None, incoming: "activitydiagram_ActivityNode" = None, activitydiagram_ActivityEdge19: set["activitydiagram_Offer"] = None):
        self.activitydiagram_ActivityEdge = activitydiagram_ActivityEdge
        self.ActivityEdge = ActivityEdge
        self.ActivityEdge11 = ActivityEdge11
        self.outgoing = outgoing
        self.incoming = incoming
        self.activitydiagram_ActivityEdge19 = activitydiagram_ActivityEdge19 if activitydiagram_ActivityEdge19 is not None else set()
        
    @property
    def ActivityEdge11(self):
        return self.__ActivityEdge11

    @ActivityEdge11.setter
    def ActivityEdge11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__ActivityEdge11", None)
        self.__ActivityEdge11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
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
            if hasattr(old_value, "activitydiagram_Activity"):
                opp_val = getattr(old_value, "activitydiagram_Activity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Activity"):
                opp_val = getattr(value, "activitydiagram_Activity", None)
                if opp_val is None:
                    setattr(value, "activitydiagram_Activity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActivityNode15"):
                opp_val = getattr(old_value, "ActivityNode15", None)
                if opp_val == self:
                    setattr(old_value, "ActivityNode15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActivityNode15"):
                opp_val = getattr(value, "ActivityNode15", None)
                setattr(value, "ActivityNode15", self)

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActivityNode17"):
                opp_val = getattr(old_value, "ActivityNode17", None)
                if opp_val == self:
                    setattr(old_value, "ActivityNode17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActivityNode17"):
                opp_val = getattr(value, "ActivityNode17", None)
                setattr(value, "ActivityNode17", self)

    @property
    def ActivityEdge(self):
        return self.__ActivityEdge

    @ActivityEdge.setter
    def ActivityEdge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__ActivityEdge", None)
        self.__ActivityEdge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def activitydiagram_ActivityEdge19(self):
        return self.__activitydiagram_ActivityEdge19

    @activitydiagram_ActivityEdge19.setter
    def activitydiagram_ActivityEdge19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__activitydiagram_ActivityEdge19", None)
        self.__activitydiagram_ActivityEdge19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activitydiagram_Offer"):
                    opp_val = getattr(item, "activitydiagram_Offer", None)
                    
                    if opp_val == self:
                        setattr(item, "activitydiagram_Offer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activitydiagram_Offer"):
                    opp_val = getattr(item, "activitydiagram_Offer", None)
                    
                    setattr(item, "activitydiagram_Offer", self)
                    

    def evaluateGuard(self) -> bool:
        # TODO: Implement evaluateGuard method
        pass

    def clearOffer(self):
        # TODO: Implement clearOffer method
        pass

class activitydiagram_Activity(NamedElement):

    def __init__(self, inputValuePath: str, activitydiagram_Activity: set["activitydiagram_ActivityEdge"] = None, activitydiagram_Activity3: set["activitydiagram_Variable"] = None, activity: set["activitydiagram_ActivityNode"] = None, Activity: "activitydiagram_ActivityNode" = None, activitydiagram_Activity5: set["activitydiagram_Variable"] = None, activitydiagram_Activity8: "activitydiagram_Trace" = None):
        self.inputValuePath = inputValuePath
        self.activitydiagram_Activity = activitydiagram_Activity if activitydiagram_Activity is not None else set()
        self.activitydiagram_Activity3 = activitydiagram_Activity3 if activitydiagram_Activity3 is not None else set()
        self.activity = activity if activity is not None else set()
        self.Activity = Activity
        self.activitydiagram_Activity5 = activitydiagram_Activity5 if activitydiagram_Activity5 is not None else set()
        self.activitydiagram_Activity8 = activitydiagram_Activity8
        
    @property
    def inputValuePath(self) -> str:
        return self.__inputValuePath

    @inputValuePath.setter
    def inputValuePath(self, inputValuePath: str):
        self.__inputValuePath = inputValuePath

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
                if hasattr(item, "activitydiagram_Variable6"):
                    opp_val = getattr(item, "activitydiagram_Variable6", None)
                    
                    if opp_val == self:
                        setattr(item, "activitydiagram_Variable6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activitydiagram_Variable6"):
                    opp_val = getattr(item, "activitydiagram_Variable6", None)
                    
                    setattr(item, "activitydiagram_Variable6", self)
                    

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
    def activitydiagram_Activity8(self):
        return self.__activitydiagram_Activity8

    @activitydiagram_Activity8.setter
    def activitydiagram_Activity8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Activity__activitydiagram_Activity8", None)
        self.__activitydiagram_Activity8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_Trace"):
                opp_val = getattr(old_value, "activitydiagram_Trace", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_Trace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Trace"):
                opp_val = getattr(value, "activitydiagram_Trace", None)
                setattr(value, "activitydiagram_Trace", self)

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

    def initialize(self):
        # TODO: Implement initialize method
        pass

    def finish(self):
        # TODO: Implement finish method
        pass

class activitydiagram_Variable(ABC):

    def __init__(self, name: str, activitydiagram_Variable: "activitydiagram_Activity" = None, activitydiagram_Variable6: "activitydiagram_Activity" = None, activitydiagram_Variable23: "activitydiagram_Value" = None, activitydiagram_Variable25: "activitydiagram_Value" = None, activitydiagram_Variable54: "activitydiagram_InputValue" = None):
        self.name = name
        self.activitydiagram_Variable = activitydiagram_Variable
        self.activitydiagram_Variable6 = activitydiagram_Variable6
        self.activitydiagram_Variable23 = activitydiagram_Variable23
        self.activitydiagram_Variable25 = activitydiagram_Variable25
        self.activitydiagram_Variable54 = activitydiagram_Variable54
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
