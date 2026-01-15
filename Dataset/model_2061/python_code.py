from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class activitydiagram_Context:

    pass
class Value:

    pass
class activitydiagram_IntegerValue(Value):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
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

class activitydiagram_Trace:

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
            if hasattr(old_value, "activitydiagram_Token37"):
                opp_val = getattr(old_value, "activitydiagram_Token37", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_Token37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Token37"):
                opp_val = getattr(value, "activitydiagram_Token37", None)
                setattr(value, "activitydiagram_Token37", self)

class activitydiagram_ControlToken(Token):

    pass
class activitydiagram_InputValue:

    pass
class activitydiagram_Value(ABC):

    pass
class Variable:

    pass
class activitydiagram_IntegerVariable(Variable):

    pass
class activitydiagram_Input:

    pass
class ControlNode:

    pass
class activitydiagram_FinalNode(ControlNode):

    pass
class activitydiagram_InitialNode(ControlNode):

    pass
class activitydiagram_NamedActivity(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class activitydiagram_Exp(ABC):

    pass
class Action:

    pass
class activitydiagram_OpaqueAction(Action):

    pass
class ExecutableNode:

    pass
class activitydiagram_Action(ExecutableNode):

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
class activitydiagram_Offer:

    pass
class activitydiagram_Token:

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

    pass
class NamedActivity:

    pass
class activitydiagram_ActivityEdge(NamedActivity):

    pass
class activitydiagram_ActivityNode(NamedActivity):

    def __init__(self, running: bool, source: set["activitydiagram_ActivityEdge"] = None, target: set["activitydiagram_ActivityEdge"] = None, nodes: "activitydiagram_Activity" = None, ActivityNode: "activitydiagram_Activity" = None, holder: set["activitydiagram_Token"] = None, ActivityNode13: "activitydiagram_ActivityEdge" = None, ActivityNode15: "activitydiagram_ActivityEdge" = None, ActivityNode33: "activitydiagram_Token" = None, activitydiagram_ActivityNode: "activitydiagram_Trace" = None):
        self.running = running
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.nodes = nodes
        self.ActivityNode = ActivityNode
        self.holder = holder if holder is not None else set()
        self.ActivityNode13 = ActivityNode13
        self.ActivityNode15 = ActivityNode15
        self.ActivityNode33 = ActivityNode33
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
    def ActivityNode15(self):
        return self.__ActivityNode15

    @ActivityNode15.setter
    def ActivityNode15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__ActivityNode15", None)
        self.__ActivityNode15 = value
        
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
    def ActivityNode33(self):
        return self.__ActivityNode33

    @ActivityNode33.setter
    def ActivityNode33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__ActivityNode33", None)
        self.__ActivityNode33 = value
        
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
            if hasattr(old_value, "activitydiagram_Trace"):
                opp_val = getattr(old_value, "activitydiagram_Trace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Trace"):
                opp_val = getattr(value, "activitydiagram_Trace", None)
                if opp_val is None:
                    setattr(value, "activitydiagram_Trace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ActivityNode13(self):
        return self.__ActivityNode13

    @ActivityNode13.setter
    def ActivityNode13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__ActivityNode13", None)
        self.__ActivityNode13 = value
        
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

class activitydiagram_Activity(NamedActivity):

    pass