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
            if hasattr(old_value, "activitydiagram_Token68"):
                opp_val = getattr(old_value, "activitydiagram_Token68", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_Token68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Token68"):
                opp_val = getattr(value, "activitydiagram_Token68", None)
                setattr(value, "activitydiagram_Token68", self)

class activitydiagram_ControlToken(Token):

    pass
class Signal:

    pass
class activitydiagram_SignalEvent(Signal):

    pass
class FinalNode:

    pass
class activitydiagram_ActivityFinalNode(FinalNode):

    def __init__(self):
        
        pass
    def execute(self):
        # TODO: Implement execute method
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

    def __init__(self, activitydiagram_IntegerVariable38: "activitydiagram_IntegerCalculationExpression" = None, activitydiagram_IntegerVariable: "activitydiagram_IntegerExpression" = None, activitydiagram_IntegerVariable34: "activitydiagram_IntegerExpression" = None):
        self.activitydiagram_IntegerVariable38 = activitydiagram_IntegerVariable38
        self.activitydiagram_IntegerVariable = activitydiagram_IntegerVariable
        self.activitydiagram_IntegerVariable34 = activitydiagram_IntegerVariable34
        
        pass
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
            if hasattr(old_value, "activitydiagram_IntegerExpression33"):
                opp_val = getattr(old_value, "activitydiagram_IntegerExpression33", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_IntegerExpression33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_IntegerExpression33"):
                opp_val = getattr(value, "activitydiagram_IntegerExpression33", None)
                setattr(value, "activitydiagram_IntegerExpression33", self)

    @property
    def activitydiagram_IntegerVariable38(self):
        return self.__activitydiagram_IntegerVariable38

    @activitydiagram_IntegerVariable38.setter
    def activitydiagram_IntegerVariable38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_IntegerVariable__activitydiagram_IntegerVariable38", None)
        self.__activitydiagram_IntegerVariable38 = value
        
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

    def print(self):
        # TODO: Implement print method
        pass

    def execute(self):
        # TODO: Implement execute method
        pass

class activitydiagram_Value:

    pass
class activitydiagram_Token:

    pass
class ControlNode:

    pass
class activitydiagram_FinalNode(ControlNode):

    pass
class activitydiagram_DecisionNode(ControlNode):

    def __init__(self):
        
        pass
    def execute(self):
        # TODO: Implement execute method
        pass

class activitydiagram_InitialNode(ControlNode):

    def __init__(self):
        
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
class activitydiagram_SendSignalAction(Action):

    def __init__(self, activitydiagram_SendSignalAction: "activitydiagram_Signal" = None):
        self.activitydiagram_SendSignalAction = activitydiagram_SendSignalAction
        
        pass
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
            if hasattr(old_value, "activitydiagram_Signal56"):
                opp_val = getattr(old_value, "activitydiagram_Signal56", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_Signal56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Signal56"):
                opp_val = getattr(value, "activitydiagram_Signal56", None)
                setattr(value, "activitydiagram_Signal56", self)

    def execute(self):
        # TODO: Implement execute method
        pass

class activitydiagram_AcceptEventAction(Action):

    def __init__(self, activitydiagram_AcceptEventAction: "activitydiagram_SignalEvent" = None):
        self.activitydiagram_AcceptEventAction = activitydiagram_AcceptEventAction
        
        pass
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
class activitydiagram_Action(ExecutableNode):

    pass
class ActivityNode:

    pass
class activitydiagram_ExecutableNode(ActivityNode):

    pass
class activitydiagram_ControlNode(ActivityNode):

    pass
class activitydiagram_BooleanVariable(Variable):

    def __init__(self, activitydiagram_BooleanVariable: "activitydiagram_ControlFlow" = None, activitydiagram_BooleanVariable36: "activitydiagram_BooleanExpression" = None, activitydiagram_BooleanVariable40: "activitydiagram_IntegerComparisonExpression" = None, activitydiagram_BooleanVariable42: "activitydiagram_BooleanUnaryExpression" = None, activitydiagram_BooleanVariable44: "activitydiagram_BooleanBinaryExpression" = None, activitydiagram_BooleanVariable47: "activitydiagram_BooleanBinaryExpression" = None):
        self.activitydiagram_BooleanVariable = activitydiagram_BooleanVariable
        self.activitydiagram_BooleanVariable36 = activitydiagram_BooleanVariable36
        self.activitydiagram_BooleanVariable40 = activitydiagram_BooleanVariable40
        self.activitydiagram_BooleanVariable42 = activitydiagram_BooleanVariable42
        self.activitydiagram_BooleanVariable44 = activitydiagram_BooleanVariable44
        self.activitydiagram_BooleanVariable47 = activitydiagram_BooleanVariable47
        
        pass
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
    def activitydiagram_BooleanVariable47(self):
        return self.__activitydiagram_BooleanVariable47

    @activitydiagram_BooleanVariable47.setter
    def activitydiagram_BooleanVariable47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanVariable__activitydiagram_BooleanVariable47", None)
        self.__activitydiagram_BooleanVariable47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_BooleanBinaryExpression46"):
                opp_val = getattr(old_value, "activitydiagram_BooleanBinaryExpression46", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanBinaryExpression46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanBinaryExpression46"):
                opp_val = getattr(value, "activitydiagram_BooleanBinaryExpression46", None)
                setattr(value, "activitydiagram_BooleanBinaryExpression46", self)

    @property
    def activitydiagram_BooleanVariable42(self):
        return self.__activitydiagram_BooleanVariable42

    @activitydiagram_BooleanVariable42.setter
    def activitydiagram_BooleanVariable42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanVariable__activitydiagram_BooleanVariable42", None)
        self.__activitydiagram_BooleanVariable42 = value
        
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
    def activitydiagram_BooleanVariable44(self):
        return self.__activitydiagram_BooleanVariable44

    @activitydiagram_BooleanVariable44.setter
    def activitydiagram_BooleanVariable44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanVariable__activitydiagram_BooleanVariable44", None)
        self.__activitydiagram_BooleanVariable44 = value
        
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
    def activitydiagram_BooleanVariable40(self):
        return self.__activitydiagram_BooleanVariable40

    @activitydiagram_BooleanVariable40.setter
    def activitydiagram_BooleanVariable40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanVariable__activitydiagram_BooleanVariable40", None)
        self.__activitydiagram_BooleanVariable40 = value
        
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
    def activitydiagram_BooleanVariable36(self):
        return self.__activitydiagram_BooleanVariable36

    @activitydiagram_BooleanVariable36.setter
    def activitydiagram_BooleanVariable36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanVariable__activitydiagram_BooleanVariable36", None)
        self.__activitydiagram_BooleanVariable36 = value
        
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

    def execute(self):
        # TODO: Implement execute method
        pass

    def print(self):
        # TODO: Implement print method
        pass

class ActivityEdge:

    pass
class activitydiagram_ControlFlow(ActivityEdge):

    pass
class activitydiagram_Offer:

    pass
class activitydiagram_Context:

    pass
class activitydiagram_Trace:

    pass
class activitydiagram_Variable:

    def __init__(self, name: str, activitydiagram_Variable: "activitydiagram_Activity" = None, activitydiagram_Variable6: "activitydiagram_Activity" = None, activitydiagram_Variable27: "activitydiagram_Value" = None, activitydiagram_Variable29: "activitydiagram_Value" = None, activitydiagram_Variable52: "activitydiagram_InputValue" = None):
        self.name = name
        self.activitydiagram_Variable = activitydiagram_Variable
        self.activitydiagram_Variable6 = activitydiagram_Variable6
        self.activitydiagram_Variable27 = activitydiagram_Variable27
        self.activitydiagram_Variable29 = activitydiagram_Variable29
        self.activitydiagram_Variable52 = activitydiagram_Variable52
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def activitydiagram_Variable27(self):
        return self.__activitydiagram_Variable27

    @activitydiagram_Variable27.setter
    def activitydiagram_Variable27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Variable__activitydiagram_Variable27", None)
        self.__activitydiagram_Variable27 = value
        
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
    def activitydiagram_Variable29(self):
        return self.__activitydiagram_Variable29

    @activitydiagram_Variable29.setter
    def activitydiagram_Variable29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Variable__activitydiagram_Variable29", None)
        self.__activitydiagram_Variable29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_Value30"):
                opp_val = getattr(old_value, "activitydiagram_Value30", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_Value30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Value30"):
                opp_val = getattr(value, "activitydiagram_Value30", None)
                setattr(value, "activitydiagram_Value30", self)

    @property
    def activitydiagram_Variable52(self):
        return self.__activitydiagram_Variable52

    @activitydiagram_Variable52.setter
    def activitydiagram_Variable52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Variable__activitydiagram_Variable52", None)
        self.__activitydiagram_Variable52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_InputValue51"):
                opp_val = getattr(old_value, "activitydiagram_InputValue51", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_InputValue51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_InputValue51"):
                opp_val = getattr(value, "activitydiagram_InputValue51", None)
                setattr(value, "activitydiagram_InputValue51", self)

    def execute(self):
        # TODO: Implement execute method
        pass

    def init(self):
        # TODO: Implement init method
        pass

    def print(self):
        # TODO: Implement print method
        pass

class NamedElement:

    pass
class activitydiagram_Signal(NamedElement):

    pass
class activitydiagram_ActivityNode(NamedElement):

    def __init__(self, running: bool, ActivityNode: "activitydiagram_Activity" = None, source: set["activitydiagram_ActivityEdge"] = None, ActivityNode19: "activitydiagram_ActivityEdge" = None, ActivityNode21: "activitydiagram_ActivityEdge" = None, target: set["activitydiagram_ActivityEdge"] = None, nodes: "activitydiagram_Activity" = None, activitydiagram_ActivityNode: set["activitydiagram_Token"] = None, activitydiagram_ActivityNode60: "activitydiagram_Token" = None, activitydiagram_ActivityNode66: "activitydiagram_Trace" = None):
        self.running = running
        self.ActivityNode = ActivityNode
        self.source = source if source is not None else set()
        self.ActivityNode19 = ActivityNode19
        self.ActivityNode21 = ActivityNode21
        self.target = target if target is not None else set()
        self.nodes = nodes
        self.activitydiagram_ActivityNode = activitydiagram_ActivityNode if activitydiagram_ActivityNode is not None else set()
        self.activitydiagram_ActivityNode60 = activitydiagram_ActivityNode60
        self.activitydiagram_ActivityNode66 = activitydiagram_ActivityNode66
        
        pass
    @property
    def running(self):
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
                if hasattr(item, "ActivityEdge15"):
                    opp_val = getattr(item, "ActivityEdge15", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityEdge15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityEdge15"):
                    opp_val = getattr(item, "ActivityEdge15", None)
                    
                    setattr(item, "ActivityEdge15", self)
                    

    @property
    def ActivityNode21(self):
        return self.__ActivityNode21

    @ActivityNode21.setter
    def ActivityNode21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__ActivityNode21", None)
        self.__ActivityNode21 = value
        
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
    def ActivityNode19(self):
        return self.__ActivityNode19

    @ActivityNode19.setter
    def ActivityNode19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__ActivityNode19", None)
        self.__ActivityNode19 = value
        
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
    def activitydiagram_ActivityNode60(self):
        return self.__activitydiagram_ActivityNode60

    @activitydiagram_ActivityNode60.setter
    def activitydiagram_ActivityNode60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__activitydiagram_ActivityNode60", None)
        self.__activitydiagram_ActivityNode60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_Token59"):
                opp_val = getattr(old_value, "activitydiagram_Token59", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_Token59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Token59"):
                opp_val = getattr(value, "activitydiagram_Token59", None)
                setattr(value, "activitydiagram_Token59", self)

    @property
    def activitydiagram_ActivityNode66(self):
        return self.__activitydiagram_ActivityNode66

    @activitydiagram_ActivityNode66.setter
    def activitydiagram_ActivityNode66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__activitydiagram_ActivityNode66", None)
        self.__activitydiagram_ActivityNode66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_Trace65"):
                opp_val = getattr(old_value, "activitydiagram_Trace65", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Trace65"):
                opp_val = getattr(value, "activitydiagram_Trace65", None)
                if opp_val is None:
                    setattr(value, "activitydiagram_Trace65", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

    def execute(self):
        # TODO: Implement execute method
        pass

    def removeToken(self, activitydiagram_token):
        # TODO: Implement removeToken method
        pass

    def addTokens(self, activitydiagram_tokens):
        # TODO: Implement addTokens method
        pass

class activitydiagram_ActivityEdge(NamedElement):

    def __init__(self, activitydiagram_ActivityEdge: "activitydiagram_Activity" = None, ActivityEdge: "activitydiagram_ActivityNode" = None, outgoing: "activitydiagram_ActivityNode" = None, incoming: "activitydiagram_ActivityNode" = None, activitydiagram_ActivityEdge23: set["activitydiagram_Offer"] = None, ActivityEdge15: "activitydiagram_ActivityNode" = None):
        self.activitydiagram_ActivityEdge = activitydiagram_ActivityEdge
        self.ActivityEdge = ActivityEdge
        self.outgoing = outgoing
        self.incoming = incoming
        self.activitydiagram_ActivityEdge23 = activitydiagram_ActivityEdge23 if activitydiagram_ActivityEdge23 is not None else set()
        self.ActivityEdge15 = ActivityEdge15
        
        pass
    @property
    def ActivityEdge15(self):
        return self.__ActivityEdge15

    @ActivityEdge15.setter
    def ActivityEdge15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__ActivityEdge15", None)
        self.__ActivityEdge15 = value
        
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
            if hasattr(old_value, "ActivityNode19"):
                opp_val = getattr(old_value, "ActivityNode19", None)
                if opp_val == self:
                    setattr(old_value, "ActivityNode19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActivityNode19"):
                opp_val = getattr(value, "ActivityNode19", None)
                setattr(value, "ActivityNode19", self)

    @property
    def activitydiagram_ActivityEdge23(self):
        return self.__activitydiagram_ActivityEdge23

    @activitydiagram_ActivityEdge23.setter
    def activitydiagram_ActivityEdge23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__activitydiagram_ActivityEdge23", None)
        self.__activitydiagram_ActivityEdge23 = value if value is not None else set()
        
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
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActivityNode21"):
                opp_val = getattr(old_value, "ActivityNode21", None)
                if opp_val == self:
                    setattr(old_value, "ActivityNode21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActivityNode21"):
                opp_val = getattr(value, "ActivityNode21", None)
                setattr(value, "ActivityNode21", self)

    def transferTokens(self):
        # TODO: Implement transferTokens method
        pass

    def clearOffer(self):
        # TODO: Implement clearOffer method
        pass

    def takeOfferedTokens(self):
        # TODO: Implement takeOfferedTokens method
        pass

    def sendOffer(self):
        # TODO: Implement sendOffer method
        pass

    def evaluateGuard(self):
        # TODO: Implement evaluateGuard method
        pass

class activitydiagram_Activity(NamedElement):

    def __init__(self, activity: set["activitydiagram_ActivityNode"] = None, activitydiagram_Activity: set["activitydiagram_ActivityEdge"] = None, activitydiagram_Activity3: set["activitydiagram_Variable"] = None, activitydiagram_Activity5: set["activitydiagram_Variable"] = None, activitydiagram_Activity8: set["activitydiagram_Signal"] = None, activitydiagram_Activity10: "activitydiagram_Trace" = None, activitydiagram_Activity12: "activitydiagram_Context" = None, Activity: "activitydiagram_ActivityNode" = None, activitydiagram_Activity74: "activitydiagram_Context" = None):
        self.activity = activity if activity is not None else set()
        self.activitydiagram_Activity = activitydiagram_Activity if activitydiagram_Activity is not None else set()
        self.activitydiagram_Activity3 = activitydiagram_Activity3 if activitydiagram_Activity3 is not None else set()
        self.activitydiagram_Activity5 = activitydiagram_Activity5 if activitydiagram_Activity5 is not None else set()
        self.activitydiagram_Activity8 = activitydiagram_Activity8 if activitydiagram_Activity8 is not None else set()
        self.activitydiagram_Activity10 = activitydiagram_Activity10
        self.activitydiagram_Activity12 = activitydiagram_Activity12
        self.Activity = Activity
        self.activitydiagram_Activity74 = activitydiagram_Activity74
        
        pass
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
    def activitydiagram_Activity12(self):
        return self.__activitydiagram_Activity12

    @activitydiagram_Activity12.setter
    def activitydiagram_Activity12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Activity__activitydiagram_Activity12", None)
        self.__activitydiagram_Activity12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_Context"):
                opp_val = getattr(old_value, "activitydiagram_Context", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_Context", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Context"):
                opp_val = getattr(value, "activitydiagram_Context", None)
                setattr(value, "activitydiagram_Context", self)

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
    def activitydiagram_Activity74(self):
        return self.__activitydiagram_Activity74

    @activitydiagram_Activity74.setter
    def activitydiagram_Activity74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Activity__activitydiagram_Activity74", None)
        self.__activitydiagram_Activity74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_Context73"):
                opp_val = getattr(old_value, "activitydiagram_Context73", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_Context73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Context73"):
                opp_val = getattr(value, "activitydiagram_Context73", None)
                setattr(value, "activitydiagram_Context73", self)

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
    def activitydiagram_Activity8(self):
        return self.__activitydiagram_Activity8

    @activitydiagram_Activity8.setter
    def activitydiagram_Activity8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Activity__activitydiagram_Activity8", None)
        self.__activitydiagram_Activity8 = value if value is not None else set()
        
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
    def activitydiagram_Activity10(self):
        return self.__activitydiagram_Activity10

    @activitydiagram_Activity10.setter
    def activitydiagram_Activity10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Activity__activitydiagram_Activity10", None)
        self.__activitydiagram_Activity10 = value
        
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

    def reset(self):
        # TODO: Implement reset method
        pass

    def getIntegerVariableValue(self, activitydiagram_variableName):
        # TODO: Implement getIntegerVariableValue method
        pass

    def finish(self):
        # TODO: Implement finish method
        pass

    def getVariableValue(self, activitydiagram_variableName) :
        # TODO: Implement getVariableValue method
        pass

    def getBooleanVariableValue(self, activitydiagram_variableName):
        # TODO: Implement getBooleanVariableValue method
        pass

    def execute(self):
        # TODO: Implement execute method
        pass

    def getVariable(self, activitydiagram_variableName) :
        # TODO: Implement getVariable method
        pass

    def initializeModel(self, activitydiagram_args):
        # TODO: Implement initializeModel method
        pass

    def initialize(self):
        # TODO: Implement initialize method
        pass

class Expression:

    pass
class activitydiagram_IntegerExpression(Expression):

    pass
class BooleanExpression:

    pass
class activitydiagram_BooleanBinaryExpression(BooleanExpression):

    def __init__(self, operator: str, activitydiagram_BooleanBinaryExpression: "activitydiagram_BooleanVariable" = None, activitydiagram_BooleanBinaryExpression46: "activitydiagram_BooleanVariable" = None):
        self.operator = operator
        self.activitydiagram_BooleanBinaryExpression = activitydiagram_BooleanBinaryExpression
        self.activitydiagram_BooleanBinaryExpression46 = activitydiagram_BooleanBinaryExpression46
        
        pass
    @property
    def operator(self):
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
            if hasattr(old_value, "activitydiagram_BooleanVariable44"):
                opp_val = getattr(old_value, "activitydiagram_BooleanVariable44", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanVariable44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanVariable44"):
                opp_val = getattr(value, "activitydiagram_BooleanVariable44", None)
                setattr(value, "activitydiagram_BooleanVariable44", self)

    @property
    def activitydiagram_BooleanBinaryExpression46(self):
        return self.__activitydiagram_BooleanBinaryExpression46

    @activitydiagram_BooleanBinaryExpression46.setter
    def activitydiagram_BooleanBinaryExpression46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanBinaryExpression__activitydiagram_BooleanBinaryExpression46", None)
        self.__activitydiagram_BooleanBinaryExpression46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_BooleanVariable47"):
                opp_val = getattr(old_value, "activitydiagram_BooleanVariable47", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanVariable47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanVariable47"):
                opp_val = getattr(value, "activitydiagram_BooleanVariable47", None)
                setattr(value, "activitydiagram_BooleanVariable47", self)

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
            if hasattr(old_value, "activitydiagram_BooleanVariable42"):
                opp_val = getattr(old_value, "activitydiagram_BooleanVariable42", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanVariable42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanVariable42"):
                opp_val = getattr(value, "activitydiagram_BooleanVariable42", None)
                setattr(value, "activitydiagram_BooleanVariable42", self)

    def execute(self):
        # TODO: Implement execute method
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
            if hasattr(old_value, "activitydiagram_IntegerVariable38"):
                opp_val = getattr(old_value, "activitydiagram_IntegerVariable38", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_IntegerVariable38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_IntegerVariable38"):
                opp_val = getattr(value, "activitydiagram_IntegerVariable38", None)
                setattr(value, "activitydiagram_IntegerVariable38", self)

    def execute(self):
        # TODO: Implement execute method
        pass

class activitydiagram_BooleanExpression(Expression):

    pass
class activitydiagram_MergeNode(ControlNode):

    def __init__(self):
        
        pass
    def execute(self):
        # TODO: Implement execute method
        pass

class activitydiagram_JoinNode(ControlNode):

    def __init__(self, activitydiagram_JoinNode: "activitydiagram_Context" = None):
        self.activitydiagram_JoinNode = activitydiagram_JoinNode
        
        pass
    @property
    def activitydiagram_JoinNode(self):
        return self.__activitydiagram_JoinNode

    @activitydiagram_JoinNode.setter
    def activitydiagram_JoinNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_JoinNode__activitydiagram_JoinNode", None)
        self.__activitydiagram_JoinNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_Context79"):
                opp_val = getattr(old_value, "activitydiagram_Context79", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_Context79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Context79"):
                opp_val = getattr(value, "activitydiagram_Context79", None)
                setattr(value, "activitydiagram_Context79", self)

    def execute(self):
        # TODO: Implement execute method
        pass

class activitydiagram_ForkNode(ControlNode):

    def __init__(self):
        
        pass
    def execute(self):
        # TODO: Implement execute method
        pass
