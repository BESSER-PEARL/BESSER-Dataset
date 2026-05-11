from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

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
class BooleanBinaryOperator(Enum):
    AND = "AND"
    OR = "OR"


############################################
# Definition of Classes
############################################

class FinalNode:

    pass
class activitydiagram_ActivityFinalNode(FinalNode):

    def __init__(self):
        
        pass
    def execute(self):
        # TODO: Implement execute method
        pass

class ControlNode:

    pass
class activitydiagram_ForkNode(ControlNode):

    def __init__(self):
        
        pass
    def execute(self):
        # TODO: Implement execute method
        pass

class activitydiagram_FinalNode(ControlNode):

    pass
class activitydiagram_InitialNode(ControlNode):

    def __init__(self):
        
        pass
    def hasOffers(self):
        # TODO: Implement hasOffers method
        pass

    def execute(self):
        # TODO: Implement execute method
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


    def execute(self):
        # TODO: Implement execute method
        pass

class activitydiagram_Expression(ABC):

    def __init__(self, activitydiagram_Expression: "activitydiagram_OpaqueAction" = None):
        self.activitydiagram_Expression = activitydiagram_Expression
        
        pass
    @property
    def activitydiagram_Expression(self):
        return self.__activitydiagram_Expression

    @activitydiagram_Expression.setter
    def activitydiagram_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Expression__activitydiagram_Expression", None)
        self.__activitydiagram_Expression = value
        
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

    def __init__(self, activitydiagram_OpaqueAction: set["activitydiagram_Expression"] = None):
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
class Variable:

    pass
class activitydiagram_IntegerVariable(Variable):

    def __init__(self, activitydiagram_IntegerVariable: "activitydiagram_IntegerExpression" = None, activitydiagram_IntegerVariable30: "activitydiagram_IntegerExpression" = None, activitydiagram_IntegerVariable34: "activitydiagram_IntegerCalculationExpression" = None):
        self.activitydiagram_IntegerVariable = activitydiagram_IntegerVariable
        self.activitydiagram_IntegerVariable30 = activitydiagram_IntegerVariable30
        self.activitydiagram_IntegerVariable34 = activitydiagram_IntegerVariable34
        
        pass
    @property
    def activitydiagram_IntegerVariable30(self):
        return self.__activitydiagram_IntegerVariable30

    @activitydiagram_IntegerVariable30.setter
    def activitydiagram_IntegerVariable30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_IntegerVariable__activitydiagram_IntegerVariable30", None)
        self.__activitydiagram_IntegerVariable30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_IntegerExpression29"):
                opp_val = getattr(old_value, "activitydiagram_IntegerExpression29", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_IntegerExpression29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_IntegerExpression29"):
                opp_val = getattr(value, "activitydiagram_IntegerExpression29", None)
                setattr(value, "activitydiagram_IntegerExpression29", self)

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
    def activitydiagram_IntegerVariable34(self):
        return self.__activitydiagram_IntegerVariable34

    @activitydiagram_IntegerVariable34.setter
    def activitydiagram_IntegerVariable34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_IntegerVariable__activitydiagram_IntegerVariable34", None)
        self.__activitydiagram_IntegerVariable34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_IntegerCalculationExpression"):
                opp_val = getattr(old_value, "activitydiagram_IntegerCalculationExpression", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_IntegerCalculationExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_IntegerCalculationExpression"):
                opp_val = getattr(value, "activitydiagram_IntegerCalculationExpression", None)
                setattr(value, "activitydiagram_IntegerCalculationExpression", self)

    def execute(self):
        # TODO: Implement execute method
        pass

    def print(self):
        # TODO: Implement print method
        pass

    def init(self):
        # TODO: Implement init method
        pass

class activitydiagram_Value:

    pass
class activitydiagram_Token:

    def __init__(self, activitydiagram_Token: "activitydiagram_ActivityNode" = None, activitydiagram_Token55: "activitydiagram_ForkedToken" = None, activitydiagram_Token46: "activitydiagram_Offer" = None):
        self.activitydiagram_Token = activitydiagram_Token
        self.activitydiagram_Token55 = activitydiagram_Token55
        self.activitydiagram_Token46 = activitydiagram_Token46
        
        pass
    @property
    def activitydiagram_Token(self):
        return self.__activitydiagram_Token

    @activitydiagram_Token.setter
    def activitydiagram_Token(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Token__activitydiagram_Token", None)
        self.__activitydiagram_Token = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_ActivityNode"):
                opp_val = getattr(old_value, "activitydiagram_ActivityNode", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_ActivityNode"):
                opp_val = getattr(value, "activitydiagram_ActivityNode", None)
                if opp_val is None:
                    setattr(value, "activitydiagram_ActivityNode", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def activitydiagram_Token46(self):
        return self.__activitydiagram_Token46

    @activitydiagram_Token46.setter
    def activitydiagram_Token46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Token__activitydiagram_Token46", None)
        self.__activitydiagram_Token46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_Offer45"):
                opp_val = getattr(old_value, "activitydiagram_Offer45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Offer45"):
                opp_val = getattr(value, "activitydiagram_Offer45", None)
                if opp_val is None:
                    setattr(value, "activitydiagram_Offer45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def activitydiagram_Token55(self):
        return self.__activitydiagram_Token55

    @activitydiagram_Token55.setter
    def activitydiagram_Token55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Token__activitydiagram_Token55", None)
        self.__activitydiagram_Token55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_ForkedToken"):
                opp_val = getattr(old_value, "activitydiagram_ForkedToken", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_ForkedToken", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_ForkedToken"):
                opp_val = getattr(value, "activitydiagram_ForkedToken", None)
                setattr(value, "activitydiagram_ForkedToken", self)

    def isWithdrawn(self):
        # TODO: Implement isWithdrawn method
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

    def __init__(self, activitydiagram_BooleanVariable: "activitydiagram_ControlFlow" = None, activitydiagram_BooleanVariable36: "activitydiagram_IntegerComparisonExpression" = None, activitydiagram_BooleanVariable38: "activitydiagram_BooleanUnaryExpression" = None, activitydiagram_BooleanVariable32: "activitydiagram_BooleanExpression" = None, activitydiagram_BooleanVariable40: "activitydiagram_BooleanBinaryExpression" = None, activitydiagram_BooleanVariable43: "activitydiagram_BooleanBinaryExpression" = None):
        self.activitydiagram_BooleanVariable = activitydiagram_BooleanVariable
        self.activitydiagram_BooleanVariable36 = activitydiagram_BooleanVariable36
        self.activitydiagram_BooleanVariable38 = activitydiagram_BooleanVariable38
        self.activitydiagram_BooleanVariable32 = activitydiagram_BooleanVariable32
        self.activitydiagram_BooleanVariable40 = activitydiagram_BooleanVariable40
        self.activitydiagram_BooleanVariable43 = activitydiagram_BooleanVariable43
        
        pass
    @property
    def activitydiagram_BooleanVariable40(self):
        return self.__activitydiagram_BooleanVariable40

    @activitydiagram_BooleanVariable40.setter
    def activitydiagram_BooleanVariable40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanVariable__activitydiagram_BooleanVariable40", None)
        self.__activitydiagram_BooleanVariable40 = value
        
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
    def activitydiagram_BooleanVariable43(self):
        return self.__activitydiagram_BooleanVariable43

    @activitydiagram_BooleanVariable43.setter
    def activitydiagram_BooleanVariable43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanVariable__activitydiagram_BooleanVariable43", None)
        self.__activitydiagram_BooleanVariable43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_BooleanBinaryExpression42"):
                opp_val = getattr(old_value, "activitydiagram_BooleanBinaryExpression42", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanBinaryExpression42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanBinaryExpression42"):
                opp_val = getattr(value, "activitydiagram_BooleanBinaryExpression42", None)
                setattr(value, "activitydiagram_BooleanBinaryExpression42", self)

    @property
    def activitydiagram_BooleanVariable36(self):
        return self.__activitydiagram_BooleanVariable36

    @activitydiagram_BooleanVariable36.setter
    def activitydiagram_BooleanVariable36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanVariable__activitydiagram_BooleanVariable36", None)
        self.__activitydiagram_BooleanVariable36 = value
        
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
    def activitydiagram_BooleanVariable38(self):
        return self.__activitydiagram_BooleanVariable38

    @activitydiagram_BooleanVariable38.setter
    def activitydiagram_BooleanVariable38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanVariable__activitydiagram_BooleanVariable38", None)
        self.__activitydiagram_BooleanVariable38 = value
        
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
    def activitydiagram_BooleanVariable32(self):
        return self.__activitydiagram_BooleanVariable32

    @activitydiagram_BooleanVariable32.setter
    def activitydiagram_BooleanVariable32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanVariable__activitydiagram_BooleanVariable32", None)
        self.__activitydiagram_BooleanVariable32 = value
        
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

    def print(self):
        # TODO: Implement print method
        pass

    def execute(self):
        # TODO: Implement execute method
        pass

    def init(self):
        # TODO: Implement init method
        pass

class ActivityEdge:

    pass
class activitydiagram_ControlFlow(ActivityEdge):

    pass
class activitydiagram_Offer:

    def __init__(self, activitydiagram_Offer: "activitydiagram_ActivityEdge" = None, activitydiagram_Offer45: set["activitydiagram_Token"] = None):
        self.activitydiagram_Offer = activitydiagram_Offer
        self.activitydiagram_Offer45 = activitydiagram_Offer45 if activitydiagram_Offer45 is not None else set()
        
        pass
    @property
    def activitydiagram_Offer(self):
        return self.__activitydiagram_Offer

    @activitydiagram_Offer.setter
    def activitydiagram_Offer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Offer__activitydiagram_Offer", None)
        self.__activitydiagram_Offer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_ActivityEdge19"):
                opp_val = getattr(old_value, "activitydiagram_ActivityEdge19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_ActivityEdge19"):
                opp_val = getattr(value, "activitydiagram_ActivityEdge19", None)
                if opp_val is None:
                    setattr(value, "activitydiagram_ActivityEdge19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def activitydiagram_Offer45(self):
        return self.__activitydiagram_Offer45

    @activitydiagram_Offer45.setter
    def activitydiagram_Offer45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Offer__activitydiagram_Offer45", None)
        self.__activitydiagram_Offer45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activitydiagram_Token46"):
                    opp_val = getattr(item, "activitydiagram_Token46", None)
                    
                    if opp_val == self:
                        setattr(item, "activitydiagram_Token46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activitydiagram_Token46"):
                    opp_val = getattr(item, "activitydiagram_Token46", None)
                    
                    setattr(item, "activitydiagram_Token46", self)
                    

    def removeWithdrawnTokens(self):
        # TODO: Implement removeWithdrawnTokens method
        pass

    def hasTokens(self):
        # TODO: Implement hasTokens method
        pass

class NamedElement:

    pass
class activitydiagram_ActivityNode(NamedElement):

    def __init__(self, running: bool, ActivityNode: "activitydiagram_Activity" = None, ActivityNode15: "activitydiagram_ActivityEdge" = None, ActivityNode17: "activitydiagram_ActivityEdge" = None, source: set["activitydiagram_ActivityEdge"] = None, target: set["activitydiagram_ActivityEdge"] = None, nodes: "activitydiagram_Activity" = None, activitydiagram_ActivityNode: set["activitydiagram_Token"] = None, activitydiagram_ActivityNode58: "activitydiagram_Trace" = None):
        self.running = running
        self.ActivityNode = ActivityNode
        self.ActivityNode15 = ActivityNode15
        self.ActivityNode17 = ActivityNode17
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.nodes = nodes
        self.activitydiagram_ActivityNode = activitydiagram_ActivityNode if activitydiagram_ActivityNode is not None else set()
        self.activitydiagram_ActivityNode58 = activitydiagram_ActivityNode58
        
        pass
    @property
    def running(self):
        return self.__running

    @running.setter
    def running(self, running: bool):
        self.__running = running


    @property
    def activitydiagram_ActivityNode58(self):
        return self.__activitydiagram_ActivityNode58

    @activitydiagram_ActivityNode58.setter
    def activitydiagram_ActivityNode58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__activitydiagram_ActivityNode58", None)
        self.__activitydiagram_ActivityNode58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_Trace57"):
                opp_val = getattr(old_value, "activitydiagram_Trace57", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Trace57"):
                opp_val = getattr(value, "activitydiagram_Trace57", None)
                if opp_val is None:
                    setattr(value, "activitydiagram_Trace57", set([self]))
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
    def activitydiagram_ActivityNode(self):
        return self.__activitydiagram_ActivityNode

    @activitydiagram_ActivityNode.setter
    def activitydiagram_ActivityNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__activitydiagram_ActivityNode", None)
        self.__activitydiagram_ActivityNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activitydiagram_Token"):
                    opp_val = getattr(item, "activitydiagram_Token", None)
                    
                    if opp_val == self:
                        setattr(item, "activitydiagram_Token", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activitydiagram_Token"):
                    opp_val = getattr(item, "activitydiagram_Token", None)
                    
                    setattr(item, "activitydiagram_Token", self)
                    

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
                    

    def terminate(self):
        # TODO: Implement terminate method
        pass

    def sendOffers(self, activitydiagram_tokens):
        # TODO: Implement sendOffers method
        pass

    def addTokens(self, activitydiagram_tokens):
        # TODO: Implement addTokens method
        pass

    def isReady(self):
        # TODO: Implement isReady method
        pass

    def takeOfferdTokens(self) :
        # TODO: Implement takeOfferdTokens method
        pass

    def hasOffers(self):
        # TODO: Implement hasOffers method
        pass

    def execute(self):
        # TODO: Implement execute method
        pass

    def removeToken1(self, activitydiagram_token):
        # TODO: Implement removeToken1 method
        pass

class activitydiagram_Activity(NamedElement):

    def __init__(self, activity: set["activitydiagram_ActivityNode"] = None, activitydiagram_Activity: set["activitydiagram_ActivityEdge"] = None, activitydiagram_Activity3: set["activitydiagram_Variable"] = None, activitydiagram_Activity5: set["activitydiagram_Variable"] = None, activitydiagram_Activity8: "activitydiagram_Trace" = None, Activity: "activitydiagram_ActivityNode" = None):
        self.activity = activity if activity is not None else set()
        self.activitydiagram_Activity = activitydiagram_Activity if activitydiagram_Activity is not None else set()
        self.activitydiagram_Activity3 = activitydiagram_Activity3 if activitydiagram_Activity3 is not None else set()
        self.activitydiagram_Activity5 = activitydiagram_Activity5 if activitydiagram_Activity5 is not None else set()
        self.activitydiagram_Activity8 = activitydiagram_Activity8
        self.Activity = Activity
        
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
                    

    def initializeModel(self, activitydiagram_args):
        # TODO: Implement initializeModel method
        pass

    def main(self):
        # TODO: Implement main method
        pass

    def getBooleanVariableValue(self, activitydiagram_variableName):
        # TODO: Implement getBooleanVariableValue method
        pass

    def getVariableValue(self, activitydiagram_variableName) :
        # TODO: Implement getVariableValue method
        pass

    def reset(self):
        # TODO: Implement reset method
        pass

    def getVariable(self, activitydiagram_variableName) :
        # TODO: Implement getVariable method
        pass

    def getIntegerVariableValue(self, activitydiagram_variableName):
        # TODO: Implement getIntegerVariableValue method
        pass

    def execute(self):
        # TODO: Implement execute method
        pass

class activitydiagram_Trace:

    pass
class activitydiagram_Variable:

    def __init__(self, name: str, activitydiagram_Variable48: "activitydiagram_InputValue" = None, activitydiagram_Variable: "activitydiagram_Activity" = None, activitydiagram_Variable6: "activitydiagram_Activity" = None, activitydiagram_Variable23: "activitydiagram_Value" = None, activitydiagram_Variable25: "activitydiagram_Value" = None):
        self.name = name
        self.activitydiagram_Variable48 = activitydiagram_Variable48
        self.activitydiagram_Variable = activitydiagram_Variable
        self.activitydiagram_Variable6 = activitydiagram_Variable6
        self.activitydiagram_Variable23 = activitydiagram_Variable23
        self.activitydiagram_Variable25 = activitydiagram_Variable25
        
        pass
    @property
    def name(self):
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
    def activitydiagram_Variable48(self):
        return self.__activitydiagram_Variable48

    @activitydiagram_Variable48.setter
    def activitydiagram_Variable48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Variable__activitydiagram_Variable48", None)
        self.__activitydiagram_Variable48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_InputValue"):
                opp_val = getattr(old_value, "activitydiagram_InputValue", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_InputValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_InputValue"):
                opp_val = getattr(value, "activitydiagram_InputValue", None)
                setattr(value, "activitydiagram_InputValue", self)

    def print(self):
        # TODO: Implement print method
        pass

    def execute(self):
        # TODO: Implement execute method
        pass

    def init(self):
        # TODO: Implement init method
        pass

class activitydiagram_ActivityEdge(NamedElement):

    def __init__(self, activitydiagram_ActivityEdge: "activitydiagram_Activity" = None, outgoing: "activitydiagram_ActivityNode" = None, incoming: "activitydiagram_ActivityNode" = None, activitydiagram_ActivityEdge19: set["activitydiagram_Offer"] = None, ActivityEdge: "activitydiagram_ActivityNode" = None, ActivityEdge11: "activitydiagram_ActivityNode" = None):
        self.activitydiagram_ActivityEdge = activitydiagram_ActivityEdge
        self.outgoing = outgoing
        self.incoming = incoming
        self.activitydiagram_ActivityEdge19 = activitydiagram_ActivityEdge19 if activitydiagram_ActivityEdge19 is not None else set()
        self.ActivityEdge = ActivityEdge
        self.ActivityEdge11 = ActivityEdge11
        
        pass
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

    def hasOffer(self):
        # TODO: Implement hasOffer method
        pass

    def takeOfferedTokens(self) :
        # TODO: Implement takeOfferedTokens method
        pass

    def sendOffer(self, activitydiagram_tokens):
        # TODO: Implement sendOffer method
        pass

class activitydiagram_Input:

    pass
class activitydiagram_InputValue:

    pass
class Token:

    pass
class activitydiagram_ForkedToken(Token):

    def __init__(self, remainingOffersCount: int, activitydiagram_ForkedToken: "activitydiagram_Token" = None):
        self.remainingOffersCount = remainingOffersCount
        self.activitydiagram_ForkedToken = activitydiagram_ForkedToken
        
        pass
    @property
    def remainingOffersCount(self):
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
            if hasattr(old_value, "activitydiagram_Token55"):
                opp_val = getattr(old_value, "activitydiagram_Token55", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_Token55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Token55"):
                opp_val = getattr(value, "activitydiagram_Token55", None)
                setattr(value, "activitydiagram_Token55", self)

class activitydiagram_ControlToken(Token):

    pass
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
            if hasattr(old_value, "activitydiagram_BooleanVariable36"):
                opp_val = getattr(old_value, "activitydiagram_BooleanVariable36", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanVariable36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanVariable36"):
                opp_val = getattr(value, "activitydiagram_BooleanVariable36", None)
                setattr(value, "activitydiagram_BooleanVariable36", self)

    def execute(self):
        # TODO: Implement execute method
        pass

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
            if hasattr(old_value, "activitydiagram_IntegerVariable34"):
                opp_val = getattr(old_value, "activitydiagram_IntegerVariable34", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_IntegerVariable34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_IntegerVariable34"):
                opp_val = getattr(value, "activitydiagram_IntegerVariable34", None)
                setattr(value, "activitydiagram_IntegerVariable34", self)

    def execute(self):
        # TODO: Implement execute method
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


class BooleanExpression:

    pass
class activitydiagram_BooleanBinaryExpression(BooleanExpression):

    def __init__(self, operator: bool, activitydiagram_BooleanBinaryExpression: "activitydiagram_BooleanVariable" = None, activitydiagram_BooleanBinaryExpression42: "activitydiagram_BooleanVariable" = None):
        self.operator = operator
        self.activitydiagram_BooleanBinaryExpression = activitydiagram_BooleanBinaryExpression
        self.activitydiagram_BooleanBinaryExpression42 = activitydiagram_BooleanBinaryExpression42
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: bool):
        self.__operator = operator


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

    def execute(self):
        # TODO: Implement execute method
        pass

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
            if hasattr(old_value, "activitydiagram_BooleanVariable38"):
                opp_val = getattr(old_value, "activitydiagram_BooleanVariable38", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanVariable38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanVariable38"):
                opp_val = getattr(value, "activitydiagram_BooleanVariable38", None)
                setattr(value, "activitydiagram_BooleanVariable38", self)

    def execute(self):
        # TODO: Implement execute method
        pass

class activitydiagram_DecisionNode(ControlNode):

    def __init__(self):
        
        pass
    def execute(self):
        # TODO: Implement execute method
        pass

    def sendOffers(self, activitydiagram_tokens):
        # TODO: Implement sendOffers method
        pass

class activitydiagram_MergeNode(ControlNode):

    def __init__(self):
        
        pass
    def execute(self):
        # TODO: Implement execute method
        pass

    def hasOffers(self):
        # TODO: Implement hasOffers method
        pass

class activitydiagram_JoinNode(ControlNode):

    def __init__(self):
        
        pass
    def execute(self):
        # TODO: Implement execute method
        pass
