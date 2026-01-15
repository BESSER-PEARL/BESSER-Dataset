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
            if hasattr(old_value, "activitydiagram_Token71"):
                opp_val = getattr(old_value, "activitydiagram_Token71", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_Token71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Token71"):
                opp_val = getattr(value, "activitydiagram_Token71", None)
                setattr(value, "activitydiagram_Token71", self)

class activitydiagram_ControlToken(Token):

    pass
class activitydiagram_Input:

    pass
class Signal:

    pass
class activitydiagram_SignalEvent(Signal):

    pass
class activitydiagram_InputValue:

    pass
class BooleanExpression:

    pass
class activitydiagram_BooleanBinaryExpression(BooleanExpression):

    def __init__(self, operator: str, activitydiagram_BooleanBinaryExpression: "activitydiagram_BooleanVariable" = None, activitydiagram_BooleanBinaryExpression54: "activitydiagram_BooleanVariable" = None):
        self.operator = operator
        self.activitydiagram_BooleanBinaryExpression = activitydiagram_BooleanBinaryExpression
        self.activitydiagram_BooleanBinaryExpression54 = activitydiagram_BooleanBinaryExpression54
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def activitydiagram_BooleanBinaryExpression54(self):
        return self.__activitydiagram_BooleanBinaryExpression54

    @activitydiagram_BooleanBinaryExpression54.setter
    def activitydiagram_BooleanBinaryExpression54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanBinaryExpression__activitydiagram_BooleanBinaryExpression54", None)
        self.__activitydiagram_BooleanBinaryExpression54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_BooleanVariable55"):
                opp_val = getattr(old_value, "activitydiagram_BooleanVariable55", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanVariable55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanVariable55"):
                opp_val = getattr(value, "activitydiagram_BooleanVariable55", None)
                setattr(value, "activitydiagram_BooleanVariable55", self)

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
            if hasattr(old_value, "activitydiagram_BooleanVariable52"):
                opp_val = getattr(old_value, "activitydiagram_BooleanVariable52", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanVariable52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanVariable52"):
                opp_val = getattr(value, "activitydiagram_BooleanVariable52", None)
                setattr(value, "activitydiagram_BooleanVariable52", self)

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
            if hasattr(old_value, "activitydiagram_BooleanVariable50"):
                opp_val = getattr(old_value, "activitydiagram_BooleanVariable50", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanVariable50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanVariable50"):
                opp_val = getattr(value, "activitydiagram_BooleanVariable50", None)
                setattr(value, "activitydiagram_BooleanVariable50", self)

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
            if hasattr(old_value, "activitydiagram_BooleanVariable48"):
                opp_val = getattr(old_value, "activitydiagram_BooleanVariable48", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanVariable48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanVariable48"):
                opp_val = getattr(value, "activitydiagram_BooleanVariable48", None)
                setattr(value, "activitydiagram_BooleanVariable48", self)

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
            if hasattr(old_value, "activitydiagram_IntegerVariable46"):
                opp_val = getattr(old_value, "activitydiagram_IntegerVariable46", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_IntegerVariable46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_IntegerVariable46"):
                opp_val = getattr(value, "activitydiagram_IntegerVariable46", None)
                setattr(value, "activitydiagram_IntegerVariable46", self)

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
class activitydiagram_Value(ABC):

    pass
class Action:

    pass
class activitydiagram_AcceptEventAction(Action):

    def __init__(self, activitydiagram_AcceptEventAction: "activitydiagram_SignalEvent" = None):
        self.activitydiagram_AcceptEventAction = activitydiagram_AcceptEventAction
        
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
            if hasattr(old_value, "activitydiagram_SignalEvent"):
                opp_val = getattr(old_value, "activitydiagram_SignalEvent", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_SignalEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_SignalEvent"):
                opp_val = getattr(value, "activitydiagram_SignalEvent", None)
                setattr(value, "activitydiagram_SignalEvent", self)

    def execute(self):
        # TODO: Implement execute method
        pass

class activitydiagram_SendSignalAction(Action):

    def __init__(self, activitydiagram_SendSignalAction: "activitydiagram_Signal" = None):
        self.activitydiagram_SendSignalAction = activitydiagram_SendSignalAction
        
    @property
    def activitydiagram_SendSignalAction(self):
        return self.__activitydiagram_SendSignalAction

    @activitydiagram_SendSignalAction.setter
    def activitydiagram_SendSignalAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_SendSignalAction__activitydiagram_SendSignalAction", None)
        self.__activitydiagram_SendSignalAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_Signal73"):
                opp_val = getattr(old_value, "activitydiagram_Signal73", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_Signal73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Signal73"):
                opp_val = getattr(value, "activitydiagram_Signal73", None)
                setattr(value, "activitydiagram_Signal73", self)

    def execute(self):
        # TODO: Implement execute method
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
class FinalNode:

    pass
class activitydiagram_ActivityFinalNode(FinalNode):

    def __init__(self):
        
    def execute(self):
        # TODO: Implement execute method
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

class activitydiagram_FinalNode(ControlNode):

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
class activitydiagram_Token(ABC):

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
class activitydiagram_Offer:

    pass
class activitydiagram_Trace:

    pass
class activitydiagram_Variable(ABC):

    def __init__(self, name: str, activitydiagram_Variable: "activitydiagram_Activity" = None, activitydiagram_Variable7: "activitydiagram_Activity" = None, activitydiagram_Variable35: "activitydiagram_Value" = None, activitydiagram_Variable37: "activitydiagram_Value" = None, activitydiagram_Variable67: "activitydiagram_InputValue" = None):
        self.name = name
        self.activitydiagram_Variable = activitydiagram_Variable
        self.activitydiagram_Variable7 = activitydiagram_Variable7
        self.activitydiagram_Variable35 = activitydiagram_Variable35
        self.activitydiagram_Variable37 = activitydiagram_Variable37
        self.activitydiagram_Variable67 = activitydiagram_Variable67
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def activitydiagram_Variable35(self):
        return self.__activitydiagram_Variable35

    @activitydiagram_Variable35.setter
    def activitydiagram_Variable35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Variable__activitydiagram_Variable35", None)
        self.__activitydiagram_Variable35 = value
        
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
    def activitydiagram_Variable67(self):
        return self.__activitydiagram_Variable67

    @activitydiagram_Variable67.setter
    def activitydiagram_Variable67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Variable__activitydiagram_Variable67", None)
        self.__activitydiagram_Variable67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_InputValue66"):
                opp_val = getattr(old_value, "activitydiagram_InputValue66", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_InputValue66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_InputValue66"):
                opp_val = getattr(value, "activitydiagram_InputValue66", None)
                setattr(value, "activitydiagram_InputValue66", self)

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
    def activitydiagram_Variable37(self):
        return self.__activitydiagram_Variable37

    @activitydiagram_Variable37.setter
    def activitydiagram_Variable37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Variable__activitydiagram_Variable37", None)
        self.__activitydiagram_Variable37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_Value38"):
                opp_val = getattr(old_value, "activitydiagram_Value38", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_Value38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Value38"):
                opp_val = getattr(value, "activitydiagram_Value38", None)
                setattr(value, "activitydiagram_Value38", self)

class NamedElement:

    pass
class activitydiagram_ActivityNode(NamedElement):

    def __init__(self, running: bool, 13: set["activitydiagram_ActivityEdge"] = None, 16: set["activitydiagram_ActivityEdge"] = None, 1: "activitydiagram_Activity" = None, 22: set["activitydiagram_Token"] = None, 26: "activitydiagram_ActivityEdge" = None, 29: "activitydiagram_ActivityEdge" = None, 19: "activitydiagram_Activity" = None, 60: "activitydiagram_Token" = None, activitydiagram_ActivityNode: "activitydiagram_Trace" = None):
        self.running = running
        self.13 = 13 if 13 is not None else set()
        self.16 = 16 if 16 is not None else set()
        self.1 = 1
        self.22 = 22 if 22 is not None else set()
        self.26 = 26
        self.29 = 29
        self.19 = 19
        self.60 = 60
        self.activitydiagram_ActivityNode = activitydiagram_ActivityNode
        
    @property
    def running(self) -> bool:
        return self.__running

    @running.setter
    def running(self, running: bool):
        self.__running = running

    @property
    def 19(self):
        return self.__19

    @19.setter
    def 19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__19", None)
        self.__19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "20"):
                opp_val = getattr(old_value, "20", None)
                if opp_val == self:
                    setattr(old_value, "20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "20"):
                opp_val = getattr(value, "20", None)
                setattr(value, "20", self)

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
            if hasattr(old_value, "activitydiagram_Trace62"):
                opp_val = getattr(old_value, "activitydiagram_Trace62", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Trace62"):
                opp_val = getattr(value, "activitydiagram_Trace62", None)
                if opp_val is None:
                    setattr(value, "activitydiagram_Trace62", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 26(self):
        return self.__26

    @26.setter
    def 26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__26", None)
        self.__26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "25"):
                opp_val = getattr(old_value, "25", None)
                if opp_val == self:
                    setattr(old_value, "25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "25"):
                opp_val = getattr(value, "25", None)
                setattr(value, "25", self)

    @property
    def 16(self):
        return self.__16

    @16.setter
    def 16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__16", None)
        self.__16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "17"):
                    opp_val = getattr(item, "17", None)
                    
                    if opp_val == self:
                        setattr(item, "17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "17"):
                    opp_val = getattr(item, "17", None)
                    
                    setattr(item, "17", self)
                    

    @property
    def 60(self):
        return self.__60

    @60.setter
    def 60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__60", None)
        self.__60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "59"):
                opp_val = getattr(old_value, "59", None)
                if opp_val == self:
                    setattr(old_value, "59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "59"):
                opp_val = getattr(value, "59", None)
                setattr(value, "59", self)

    @property
    def 29(self):
        return self.__29

    @29.setter
    def 29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__29", None)
        self.__29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "28"):
                opp_val = getattr(old_value, "28", None)
                if opp_val == self:
                    setattr(old_value, "28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "28"):
                opp_val = getattr(value, "28", None)
                setattr(value, "28", self)

    @property
    def 22(self):
        return self.__22

    @22.setter
    def 22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__22", None)
        self.__22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "23"):
                    opp_val = getattr(item, "23", None)
                    
                    if opp_val == self:
                        setattr(item, "23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "23"):
                    opp_val = getattr(item, "23", None)
                    
                    setattr(item, "23", self)
                    

    @property
    def 1(self):
        return self.__1

    @1.setter
    def 1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__1", None)
        self.__1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, ""):
                opp_val = getattr(old_value, "", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, ""):
                opp_val = getattr(value, "", None)
                if opp_val is None:
                    setattr(value, "", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 13(self):
        return self.__13

    @13.setter
    def 13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__13", None)
        self.__13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "14"):
                    opp_val = getattr(item, "14", None)
                    
                    if opp_val == self:
                        setattr(item, "14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "14"):
                    opp_val = getattr(item, "14", None)
                    
                    setattr(item, "14", self)
                    

    def execute(self):
        # TODO: Implement execute method
        pass

    def terminate(self):
        # TODO: Implement terminate method
        pass

class activitydiagram_Signal(NamedElement):

    pass
class activitydiagram_ActivityEdge(NamedElement):

    def __init__(self, 14: "activitydiagram_ActivityNode" = None, 17: "activitydiagram_ActivityNode" = None, activitydiagram_ActivityEdge: "activitydiagram_Activity" = None, 25: "activitydiagram_ActivityNode" = None, 28: "activitydiagram_ActivityNode" = None, activitydiagram_ActivityEdge31: set["activitydiagram_Offer"] = None):
        self.14 = 14
        self.17 = 17
        self.activitydiagram_ActivityEdge = activitydiagram_ActivityEdge
        self.25 = 25
        self.28 = 28
        self.activitydiagram_ActivityEdge31 = activitydiagram_ActivityEdge31 if activitydiagram_ActivityEdge31 is not None else set()
        
    @property
    def activitydiagram_ActivityEdge31(self):
        return self.__activitydiagram_ActivityEdge31

    @activitydiagram_ActivityEdge31.setter
    def activitydiagram_ActivityEdge31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__activitydiagram_ActivityEdge31", None)
        self.__activitydiagram_ActivityEdge31 = value if value is not None else set()
        
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
    def 25(self):
        return self.__25

    @25.setter
    def 25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__25", None)
        self.__25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "26"):
                opp_val = getattr(old_value, "26", None)
                if opp_val == self:
                    setattr(old_value, "26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "26"):
                opp_val = getattr(value, "26", None)
                setattr(value, "26", self)

    @property
    def 28(self):
        return self.__28

    @28.setter
    def 28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__28", None)
        self.__28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "29"):
                opp_val = getattr(old_value, "29", None)
                if opp_val == self:
                    setattr(old_value, "29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "29"):
                opp_val = getattr(value, "29", None)
                setattr(value, "29", self)

    @property
    def 17(self):
        return self.__17

    @17.setter
    def 17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__17", None)
        self.__17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "16"):
                opp_val = getattr(old_value, "16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "16"):
                opp_val = getattr(value, "16", None)
                if opp_val is None:
                    setattr(value, "16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 14(self):
        return self.__14

    @14.setter
    def 14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__14", None)
        self.__14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "13"):
                opp_val = getattr(old_value, "13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "13"):
                opp_val = getattr(value, "13", None)
                if opp_val is None:
                    setattr(value, "13", set([self]))
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

    def clearOffer(self):
        # TODO: Implement clearOffer method
        pass

    def evaluateGuard(self):
        # TODO: Implement evaluateGuard method
        pass

class activitydiagram_Activity(NamedElement):

    def __init__(self, inputValuePath: str, activitydiagram_Activity4: set["activitydiagram_Variable"] = None, activitydiagram_Activity6: set["activitydiagram_Variable"] = None, activitydiagram_Activity9: "activitydiagram_Trace" = None, activitydiagram_Activity11: set["activitydiagram_Signal"] = None, : set["activitydiagram_ActivityNode"] = None, activitydiagram_Activity: set["activitydiagram_ActivityEdge"] = None, 20: "activitydiagram_ActivityNode" = None):
        self.inputValuePath = inputValuePath
        self.activitydiagram_Activity4 = activitydiagram_Activity4 if activitydiagram_Activity4 is not None else set()
        self.activitydiagram_Activity6 = activitydiagram_Activity6 if activitydiagram_Activity6 is not None else set()
        self.activitydiagram_Activity9 = activitydiagram_Activity9
        self.activitydiagram_Activity11 = activitydiagram_Activity11 if activitydiagram_Activity11 is not None else set()
        self. =  if  is not None else set()
        self.activitydiagram_Activity = activitydiagram_Activity if activitydiagram_Activity is not None else set()
        self.20 = 20
        
    @property
    def inputValuePath(self) -> str:
        return self.__inputValuePath

    @inputValuePath.setter
    def inputValuePath(self, inputValuePath: str):
        self.__inputValuePath = inputValuePath

    @property
    def 20(self):
        return self.__20

    @20.setter
    def 20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Activity__20", None)
        self.__20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "19"):
                opp_val = getattr(old_value, "19", None)
                if opp_val == self:
                    setattr(old_value, "19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "19"):
                opp_val = getattr(value, "19", None)
                setattr(value, "19", self)

    @property
    def activitydiagram_Activity9(self):
        return self.__activitydiagram_Activity9

    @activitydiagram_Activity9.setter
    def activitydiagram_Activity9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Activity__activitydiagram_Activity9", None)
        self.__activitydiagram_Activity9 = value
        
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
    def activitydiagram_Activity4(self):
        return self.__activitydiagram_Activity4

    @activitydiagram_Activity4.setter
    def activitydiagram_Activity4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Activity__activitydiagram_Activity4", None)
        self.__activitydiagram_Activity4 = value if value is not None else set()
        
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
    def activitydiagram_Activity11(self):
        return self.__activitydiagram_Activity11

    @activitydiagram_Activity11.setter
    def activitydiagram_Activity11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Activity__activitydiagram_Activity11", None)
        self.__activitydiagram_Activity11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activitydiagram_Signal"):
                    opp_val = getattr(item, "activitydiagram_Signal", None)
                    
                    if opp_val == self:
                        setattr(item, "activitydiagram_Signal", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activitydiagram_Signal"):
                    opp_val = getattr(item, "activitydiagram_Signal", None)
                    
                    setattr(item, "activitydiagram_Signal", self)
                    

    @property
    def (self):
        return self.__

    @.setter
    def (self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Activity__", None)
        self.__ = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "1"):
                    opp_val = getattr(item, "1", None)
                    
                    if opp_val == self:
                        setattr(item, "1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "1"):
                    opp_val = getattr(item, "1", None)
                    
                    setattr(item, "1", self)
                    

    @property
    def activitydiagram_Activity6(self):
        return self.__activitydiagram_Activity6

    @activitydiagram_Activity6.setter
    def activitydiagram_Activity6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Activity__activitydiagram_Activity6", None)
        self.__activitydiagram_Activity6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activitydiagram_Variable7"):
                    opp_val = getattr(item, "activitydiagram_Variable7", None)
                    
                    if opp_val == self:
                        setattr(item, "activitydiagram_Variable7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activitydiagram_Variable7"):
                    opp_val = getattr(item, "activitydiagram_Variable7", None)
                    
                    setattr(item, "activitydiagram_Variable7", self)
                    

    def finish(self):
        # TODO: Implement finish method
        pass

    def initialize(self):
        # TODO: Implement initialize method
        pass
