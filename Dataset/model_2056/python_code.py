from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class IntegerCalculationOperator(Enum):
    ADD = "ADD"
    SUBRACT = "SUBRACT"
class BooleanBinaryOperator(Enum):
    AND = "AND"
    OR = "OR"
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
            if hasattr(old_value, "activitydiagram_Token69"):
                opp_val = getattr(old_value, "activitydiagram_Token69", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_Token69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Token69"):
                opp_val = getattr(value, "activitydiagram_Token69", None)
                setattr(value, "activitydiagram_Token69", self)

class activitydiagram_ControlToken(Token):

    pass
class activitydiagram_Input:

    pass
class activitydiagram_InputValue:

    pass
class BooleanExpression:

    pass
class activitydiagram_BooleanBinaryExpression(BooleanExpression):

    def __init__(self, operator: str, activitydiagram_BooleanBinaryExpression: "activitydiagram_BooleanVariable" = None, activitydiagram_BooleanBinaryExpression52: "activitydiagram_BooleanVariable" = None):
        self.operator = operator
        self.activitydiagram_BooleanBinaryExpression = activitydiagram_BooleanBinaryExpression
        self.activitydiagram_BooleanBinaryExpression52 = activitydiagram_BooleanBinaryExpression52
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def activitydiagram_BooleanBinaryExpression52(self):
        return self.__activitydiagram_BooleanBinaryExpression52

    @activitydiagram_BooleanBinaryExpression52.setter
    def activitydiagram_BooleanBinaryExpression52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanBinaryExpression__activitydiagram_BooleanBinaryExpression52", None)
        self.__activitydiagram_BooleanBinaryExpression52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_BooleanVariable53"):
                opp_val = getattr(old_value, "activitydiagram_BooleanVariable53", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanVariable53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanVariable53"):
                opp_val = getattr(value, "activitydiagram_BooleanVariable53", None)
                setattr(value, "activitydiagram_BooleanVariable53", self)

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
            if hasattr(old_value, "activitydiagram_BooleanVariable50"):
                opp_val = getattr(old_value, "activitydiagram_BooleanVariable50", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanVariable50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanVariable50"):
                opp_val = getattr(value, "activitydiagram_BooleanVariable50", None)
                setattr(value, "activitydiagram_BooleanVariable50", self)

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
            if hasattr(old_value, "activitydiagram_BooleanVariable48"):
                opp_val = getattr(old_value, "activitydiagram_BooleanVariable48", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanVariable48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanVariable48"):
                opp_val = getattr(value, "activitydiagram_BooleanVariable48", None)
                setattr(value, "activitydiagram_BooleanVariable48", self)

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
            if hasattr(old_value, "activitydiagram_BooleanVariable46"):
                opp_val = getattr(old_value, "activitydiagram_BooleanVariable46", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanVariable46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanVariable46"):
                opp_val = getattr(value, "activitydiagram_BooleanVariable46", None)
                setattr(value, "activitydiagram_BooleanVariable46", self)

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
            if hasattr(old_value, "activitydiagram_IntegerVariable44"):
                opp_val = getattr(old_value, "activitydiagram_IntegerVariable44", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_IntegerVariable44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_IntegerVariable44"):
                opp_val = getattr(value, "activitydiagram_IntegerVariable44", None)
                setattr(value, "activitydiagram_IntegerVariable44", self)

class Expression:

    pass
class activitydiagram_BooleanExpression(Expression):

    pass
class activitydiagram_IntegerExpression(Expression):

    pass
class Value:

    pass
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
class activitydiagram_IntegerValue(Value):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class FinalNode:

    pass
class activitydiagram_ActivityFinalNode(FinalNode):

    pass
class ControlNode:

    pass
class activitydiagram_DecisionNode(ControlNode):

    pass
class activitydiagram_FinalNode(ControlNode):

    pass
class activitydiagram_ForkNode(ControlNode):

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
class activitydiagram_MergeNode(ControlNode):

    pass
class activitydiagram_JoinNode(ControlNode):

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
class ExecutableNode:

    pass
class activitydiagram_Action(ExecutableNode):

    pass
class activitydiagram_ExecutableNode(ActivityNode):

    pass
class activitydiagram_Token(ABC):

    pass
class activitydiagram_Variable(ABC):

    def __init__(self, name: str, activitydiagram_Variable: "activitydiagram_Activity" = None, activitydiagram_Variable7: "activitydiagram_Activity" = None, activitydiagram_Variable33: "activitydiagram_Value" = None, activitydiagram_Variable35: "activitydiagram_Value" = None, activitydiagram_Variable65: "activitydiagram_InputValue" = None):
        self.name = name
        self.activitydiagram_Variable = activitydiagram_Variable
        self.activitydiagram_Variable7 = activitydiagram_Variable7
        self.activitydiagram_Variable33 = activitydiagram_Variable33
        self.activitydiagram_Variable35 = activitydiagram_Variable35
        self.activitydiagram_Variable65 = activitydiagram_Variable65
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def activitydiagram_Variable65(self):
        return self.__activitydiagram_Variable65

    @activitydiagram_Variable65.setter
    def activitydiagram_Variable65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Variable__activitydiagram_Variable65", None)
        self.__activitydiagram_Variable65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_InputValue64"):
                opp_val = getattr(old_value, "activitydiagram_InputValue64", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_InputValue64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_InputValue64"):
                opp_val = getattr(value, "activitydiagram_InputValue64", None)
                setattr(value, "activitydiagram_InputValue64", self)

    @property
    def activitydiagram_Variable33(self):
        return self.__activitydiagram_Variable33

    @activitydiagram_Variable33.setter
    def activitydiagram_Variable33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Variable__activitydiagram_Variable33", None)
        self.__activitydiagram_Variable33 = value
        
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
    def activitydiagram_Variable35(self):
        return self.__activitydiagram_Variable35

    @activitydiagram_Variable35.setter
    def activitydiagram_Variable35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Variable__activitydiagram_Variable35", None)
        self.__activitydiagram_Variable35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_Value36"):
                opp_val = getattr(old_value, "activitydiagram_Value36", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_Value36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Value36"):
                opp_val = getattr(value, "activitydiagram_Value36", None)
                setattr(value, "activitydiagram_Value36", self)

class NamedElement:

    pass
class activitydiagram_ActivityNode(NamedElement):

    def __init__(self, running: bool, 1: "activitydiagram_Activity" = None, 11: set["activitydiagram_ActivityEdge"] = None, 14: set["activitydiagram_ActivityEdge"] = None, 17: "activitydiagram_Activity" = None, 20: set["activitydiagram_Token"] = None, 24: "activitydiagram_ActivityEdge" = None, 27: "activitydiagram_ActivityEdge" = None, 58: "activitydiagram_Token" = None, activitydiagram_ActivityNode: "activitydiagram_Trace" = None):
        self.running = running
        self.1 = 1
        self.11 = 11 if 11 is not None else set()
        self.14 = 14 if 14 is not None else set()
        self.17 = 17
        self.20 = 20 if 20 is not None else set()
        self.24 = 24
        self.27 = 27
        self.58 = 58
        self.activitydiagram_ActivityNode = activitydiagram_ActivityNode
        
    @property
    def running(self) -> bool:
        return self.__running

    @running.setter
    def running(self, running: bool):
        self.__running = running

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
            if hasattr(old_value, "activitydiagram_Trace60"):
                opp_val = getattr(old_value, "activitydiagram_Trace60", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Trace60"):
                opp_val = getattr(value, "activitydiagram_Trace60", None)
                if opp_val is None:
                    setattr(value, "activitydiagram_Trace60", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 24(self):
        return self.__24

    @24.setter
    def 24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__24", None)
        self.__24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "23"):
                opp_val = getattr(old_value, "23", None)
                if opp_val == self:
                    setattr(old_value, "23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "23"):
                opp_val = getattr(value, "23", None)
                setattr(value, "23", self)

    @property
    def 20(self):
        return self.__20

    @20.setter
    def 20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__20", None)
        self.__20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "21"):
                    opp_val = getattr(item, "21", None)
                    
                    if opp_val == self:
                        setattr(item, "21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "21"):
                    opp_val = getattr(item, "21", None)
                    
                    setattr(item, "21", self)
                    

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
    def 27(self):
        return self.__27

    @27.setter
    def 27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__27", None)
        self.__27 = value
        
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
    def 17(self):
        return self.__17

    @17.setter
    def 17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__17", None)
        self.__17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "18"):
                opp_val = getattr(old_value, "18", None)
                if opp_val == self:
                    setattr(old_value, "18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "18"):
                opp_val = getattr(value, "18", None)
                setattr(value, "18", self)

    @property
    def 14(self):
        return self.__14

    @14.setter
    def 14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__14", None)
        self.__14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "15"):
                    opp_val = getattr(item, "15", None)
                    
                    if opp_val == self:
                        setattr(item, "15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "15"):
                    opp_val = getattr(item, "15", None)
                    
                    setattr(item, "15", self)
                    

    @property
    def 11(self):
        return self.__11

    @11.setter
    def 11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__11", None)
        self.__11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "12"):
                    opp_val = getattr(item, "12", None)
                    
                    if opp_val == self:
                        setattr(item, "12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "12"):
                    opp_val = getattr(item, "12", None)
                    
                    setattr(item, "12", self)
                    

    @property
    def 58(self):
        return self.__58

    @58.setter
    def 58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__58", None)
        self.__58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "57"):
                opp_val = getattr(old_value, "57", None)
                if opp_val == self:
                    setattr(old_value, "57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "57"):
                opp_val = getattr(value, "57", None)
                setattr(value, "57", self)

class activitydiagram_ActivityEdge(NamedElement):

    pass
class activitydiagram_Activity(NamedElement):

    pass
class activitydiagram_Trace:

    pass