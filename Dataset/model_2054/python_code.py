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

class activitydiagram_Input:

    pass
class Token:

    pass
class activitydiagram_ControlToken(Token):

    pass
class activitydiagram_ForkedToken(Token):

    def __init__(self, remainingOffersCount: str, activitydiagram_ForkedToken: "activitydiagram_Token" = None):
        self.remainingOffersCount = remainingOffersCount
        self.activitydiagram_ForkedToken = activitydiagram_ForkedToken
        
        pass
    @property
    def remainingOffersCount(self):
        return self.__remainingOffersCount

    @remainingOffersCount.setter
    def remainingOffersCount(self, remainingOffersCount: str):
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

class activitydiagram_Trace:

    pass
class activitydiagram_Context:

    pass
class activitydiagram_Token:

    def __init__(self, activitydiagram_Token: "activitydiagram_Offer" = None, activitydiagram_Token51: "activitydiagram_ActivityNode" = None, activitydiagram_Token68: "activitydiagram_ForkedToken" = None):
        self.activitydiagram_Token = activitydiagram_Token
        self.activitydiagram_Token51 = activitydiagram_Token51
        self.activitydiagram_Token68 = activitydiagram_Token68
        
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
            if hasattr(old_value, "activitydiagram_Offer49"):
                opp_val = getattr(old_value, "activitydiagram_Offer49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Offer49"):
                opp_val = getattr(value, "activitydiagram_Offer49", None)
                if opp_val is None:
                    setattr(value, "activitydiagram_Offer49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def activitydiagram_Token51(self):
        return self.__activitydiagram_Token51

    @activitydiagram_Token51.setter
    def activitydiagram_Token51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Token__activitydiagram_Token51", None)
        self.__activitydiagram_Token51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_ActivityNode"):
                opp_val = getattr(old_value, "activitydiagram_ActivityNode", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_ActivityNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_ActivityNode"):
                opp_val = getattr(value, "activitydiagram_ActivityNode", None)
                setattr(value, "activitydiagram_ActivityNode", self)

    @property
    def activitydiagram_Token68(self):
        return self.__activitydiagram_Token68

    @activitydiagram_Token68.setter
    def activitydiagram_Token68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Token__activitydiagram_Token68", None)
        self.__activitydiagram_Token68 = value
        
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

    def transfer(self, activitydiagram_holder) :
        # TODO: Implement transfer method
        pass

    def withdraw(self):
        # TODO: Implement withdraw method
        pass

    def isWithdrawn(self):
        # TODO: Implement isWithdrawn method
        pass

class IntegerExpression:

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
            if hasattr(old_value, "activitydiagram_IntegerVariable31"):
                opp_val = getattr(old_value, "activitydiagram_IntegerVariable31", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_IntegerVariable31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_IntegerVariable31"):
                opp_val = getattr(value, "activitydiagram_IntegerVariable31", None)
                setattr(value, "activitydiagram_IntegerVariable31", self)

    def execute(self, activitydiagram_c):
        # TODO: Implement execute method
        pass

class activitydiagram_InputValue:

    pass
class BooleanExpression:

    pass
class activitydiagram_BooleanBinaryExpression(BooleanExpression):

    def __init__(self, operator: bool, activitydiagram_BooleanBinaryExpression: "activitydiagram_BooleanVariable" = None, activitydiagram_BooleanBinaryExpression39: "activitydiagram_BooleanVariable" = None):
        self.operator = operator
        self.activitydiagram_BooleanBinaryExpression = activitydiagram_BooleanBinaryExpression
        self.activitydiagram_BooleanBinaryExpression39 = activitydiagram_BooleanBinaryExpression39
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: bool):
        self.__operator = operator


    @property
    def activitydiagram_BooleanBinaryExpression39(self):
        return self.__activitydiagram_BooleanBinaryExpression39

    @activitydiagram_BooleanBinaryExpression39.setter
    def activitydiagram_BooleanBinaryExpression39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanBinaryExpression__activitydiagram_BooleanBinaryExpression39", None)
        self.__activitydiagram_BooleanBinaryExpression39 = value
        
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
    def activitydiagram_BooleanBinaryExpression(self):
        return self.__activitydiagram_BooleanBinaryExpression

    @activitydiagram_BooleanBinaryExpression.setter
    def activitydiagram_BooleanBinaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanBinaryExpression__activitydiagram_BooleanBinaryExpression", None)
        self.__activitydiagram_BooleanBinaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_BooleanVariable37"):
                opp_val = getattr(old_value, "activitydiagram_BooleanVariable37", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanVariable37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanVariable37"):
                opp_val = getattr(value, "activitydiagram_BooleanVariable37", None)
                setattr(value, "activitydiagram_BooleanVariable37", self)

    def execute(self, activitydiagram_c):
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
            if hasattr(old_value, "activitydiagram_BooleanVariable35"):
                opp_val = getattr(old_value, "activitydiagram_BooleanVariable35", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanVariable35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanVariable35"):
                opp_val = getattr(value, "activitydiagram_BooleanVariable35", None)
                setattr(value, "activitydiagram_BooleanVariable35", self)

    def execute(self, activitydiagram_c):
        # TODO: Implement execute method
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
            if hasattr(old_value, "activitydiagram_BooleanVariable33"):
                opp_val = getattr(old_value, "activitydiagram_BooleanVariable33", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanVariable33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanVariable33"):
                opp_val = getattr(value, "activitydiagram_BooleanVariable33", None)
                setattr(value, "activitydiagram_BooleanVariable33", self)

    def execute(self, activitydiagram_c):
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


class Variable:

    pass
class activitydiagram_IntegerVariable(Variable):

    def __init__(self, activitydiagram_IntegerVariable: "activitydiagram_IntegerExpression" = None, activitydiagram_IntegerVariable27: "activitydiagram_IntegerExpression" = None, activitydiagram_IntegerVariable31: "activitydiagram_IntegerCalculationExpression" = None):
        self.activitydiagram_IntegerVariable = activitydiagram_IntegerVariable
        self.activitydiagram_IntegerVariable27 = activitydiagram_IntegerVariable27
        self.activitydiagram_IntegerVariable31 = activitydiagram_IntegerVariable31
        
        pass
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
    def activitydiagram_IntegerVariable31(self):
        return self.__activitydiagram_IntegerVariable31

    @activitydiagram_IntegerVariable31.setter
    def activitydiagram_IntegerVariable31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_IntegerVariable__activitydiagram_IntegerVariable31", None)
        self.__activitydiagram_IntegerVariable31 = value
        
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
    def activitydiagram_IntegerVariable27(self):
        return self.__activitydiagram_IntegerVariable27

    @activitydiagram_IntegerVariable27.setter
    def activitydiagram_IntegerVariable27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_IntegerVariable__activitydiagram_IntegerVariable27", None)
        self.__activitydiagram_IntegerVariable27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_IntegerExpression26"):
                opp_val = getattr(old_value, "activitydiagram_IntegerExpression26", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_IntegerExpression26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_IntegerExpression26"):
                opp_val = getattr(value, "activitydiagram_IntegerExpression26", None)
                setattr(value, "activitydiagram_IntegerExpression26", self)

    def execute(self, activitydiagram_c):
        # TODO: Implement execute method
        pass

    def print(self):
        # TODO: Implement print method
        pass

class activitydiagram_Value:

    pass
class FinalNode:

    pass
class activitydiagram_ActivityFinalNode(FinalNode):

    def __init__(self):
        
        pass
    def execute(self, activitydiagram_c):
        # TODO: Implement execute method
        pass

class ControlNode:

    pass
class activitydiagram_MergeNode(ControlNode):

    def __init__(self):
        
        pass
    def hasOffers(self):
        # TODO: Implement hasOffers method
        pass

    def execute(self, activitydiagram_c):
        # TODO: Implement execute method
        pass

class activitydiagram_FinalNode(ControlNode):

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
            if hasattr(old_value, "activitydiagram_Context63"):
                opp_val = getattr(old_value, "activitydiagram_Context63", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_Context63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Context63"):
                opp_val = getattr(value, "activitydiagram_Context63", None)
                setattr(value, "activitydiagram_Context63", self)

    def execute(self, activitydiagram_c):
        # TODO: Implement execute method
        pass

class activitydiagram_ForkNode(ControlNode):

    def __init__(self):
        
        pass
    def execute(self, activitydiagram_c):
        # TODO: Implement execute method
        pass

class activitydiagram_DecisionNode(ControlNode):

    def __init__(self):
        
        pass
    def execute(self, activitydiagram_c):
        # TODO: Implement execute method
        pass

    def sendOffers(self, activitydiagram_tokens):
        # TODO: Implement sendOffers method
        pass

class activitydiagram_InitialNode(ControlNode):

    def __init__(self):
        
        pass
    def hasOffers(self):
        # TODO: Implement hasOffers method
        pass

    def execute(self, activitydiagram_c):
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


    def execute(self, activitydiagram_c):
        # TODO: Implement execute method
        pass

class activitydiagram_Expression:

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

    def execute(self, activitydiagram_c):
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
                    

    def execute(self, activitydiagram_c):
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

    def __init__(self, activitydiagram_BooleanVariable: "activitydiagram_ControlFlow" = None, activitydiagram_BooleanVariable33: "activitydiagram_IntegerComparisonExpression" = None, activitydiagram_BooleanVariable35: "activitydiagram_BooleanUnaryExpression" = None, activitydiagram_BooleanVariable37: "activitydiagram_BooleanBinaryExpression" = None, activitydiagram_BooleanVariable40: "activitydiagram_BooleanBinaryExpression" = None, activitydiagram_BooleanVariable29: "activitydiagram_BooleanExpression" = None):
        self.activitydiagram_BooleanVariable = activitydiagram_BooleanVariable
        self.activitydiagram_BooleanVariable33 = activitydiagram_BooleanVariable33
        self.activitydiagram_BooleanVariable35 = activitydiagram_BooleanVariable35
        self.activitydiagram_BooleanVariable37 = activitydiagram_BooleanVariable37
        self.activitydiagram_BooleanVariable40 = activitydiagram_BooleanVariable40
        self.activitydiagram_BooleanVariable29 = activitydiagram_BooleanVariable29
        
        pass
    @property
    def activitydiagram_BooleanVariable37(self):
        return self.__activitydiagram_BooleanVariable37

    @activitydiagram_BooleanVariable37.setter
    def activitydiagram_BooleanVariable37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanVariable__activitydiagram_BooleanVariable37", None)
        self.__activitydiagram_BooleanVariable37 = value
        
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
    def activitydiagram_BooleanVariable29(self):
        return self.__activitydiagram_BooleanVariable29

    @activitydiagram_BooleanVariable29.setter
    def activitydiagram_BooleanVariable29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanVariable__activitydiagram_BooleanVariable29", None)
        self.__activitydiagram_BooleanVariable29 = value
        
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
    def activitydiagram_BooleanVariable40(self):
        return self.__activitydiagram_BooleanVariable40

    @activitydiagram_BooleanVariable40.setter
    def activitydiagram_BooleanVariable40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanVariable__activitydiagram_BooleanVariable40", None)
        self.__activitydiagram_BooleanVariable40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_BooleanBinaryExpression39"):
                opp_val = getattr(old_value, "activitydiagram_BooleanBinaryExpression39", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_BooleanBinaryExpression39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_BooleanBinaryExpression39"):
                opp_val = getattr(value, "activitydiagram_BooleanBinaryExpression39", None)
                setattr(value, "activitydiagram_BooleanBinaryExpression39", self)

    @property
    def activitydiagram_BooleanVariable35(self):
        return self.__activitydiagram_BooleanVariable35

    @activitydiagram_BooleanVariable35.setter
    def activitydiagram_BooleanVariable35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanVariable__activitydiagram_BooleanVariable35", None)
        self.__activitydiagram_BooleanVariable35 = value
        
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
    def activitydiagram_BooleanVariable33(self):
        return self.__activitydiagram_BooleanVariable33

    @activitydiagram_BooleanVariable33.setter
    def activitydiagram_BooleanVariable33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_BooleanVariable__activitydiagram_BooleanVariable33", None)
        self.__activitydiagram_BooleanVariable33 = value
        
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

    def print(self):
        # TODO: Implement print method
        pass

    def execute(self, activitydiagram_c):
        # TODO: Implement execute method
        pass

class ActivityEdge:

    pass
class activitydiagram_ControlFlow(ActivityEdge):

    pass
class activitydiagram_Offer:

    def __init__(self, activitydiagram_Offer: "activitydiagram_ActivityEdge" = None, activitydiagram_Offer49: set["activitydiagram_Token"] = None):
        self.activitydiagram_Offer = activitydiagram_Offer
        self.activitydiagram_Offer49 = activitydiagram_Offer49 if activitydiagram_Offer49 is not None else set()
        
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
            if hasattr(old_value, "activitydiagram_ActivityEdge16"):
                opp_val = getattr(old_value, "activitydiagram_ActivityEdge16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_ActivityEdge16"):
                opp_val = getattr(value, "activitydiagram_ActivityEdge16", None)
                if opp_val is None:
                    setattr(value, "activitydiagram_ActivityEdge16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def activitydiagram_Offer49(self):
        return self.__activitydiagram_Offer49

    @activitydiagram_Offer49.setter
    def activitydiagram_Offer49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Offer__activitydiagram_Offer49", None)
        self.__activitydiagram_Offer49 = value if value is not None else set()
        
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
                    

    def hasTokens(self):
        # TODO: Implement hasTokens method
        pass

    def removeWithdrawnTokens(self):
        # TODO: Implement removeWithdrawnTokens method
        pass

class activitydiagram_Variable:

    def __init__(self, name: str, activitydiagram_Variable6: "activitydiagram_Activity" = None, activitydiagram_Variable: "activitydiagram_Activity" = None, activitydiagram_Variable20: "activitydiagram_Value" = None, activitydiagram_Variable22: "activitydiagram_Value" = None, activitydiagram_Variable45: "activitydiagram_InputValue" = None):
        self.name = name
        self.activitydiagram_Variable6 = activitydiagram_Variable6
        self.activitydiagram_Variable = activitydiagram_Variable
        self.activitydiagram_Variable20 = activitydiagram_Variable20
        self.activitydiagram_Variable22 = activitydiagram_Variable22
        self.activitydiagram_Variable45 = activitydiagram_Variable45
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def activitydiagram_Variable45(self):
        return self.__activitydiagram_Variable45

    @activitydiagram_Variable45.setter
    def activitydiagram_Variable45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Variable__activitydiagram_Variable45", None)
        self.__activitydiagram_Variable45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_InputValue44"):
                opp_val = getattr(old_value, "activitydiagram_InputValue44", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_InputValue44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_InputValue44"):
                opp_val = getattr(value, "activitydiagram_InputValue44", None)
                setattr(value, "activitydiagram_InputValue44", self)

    @property
    def activitydiagram_Variable22(self):
        return self.__activitydiagram_Variable22

    @activitydiagram_Variable22.setter
    def activitydiagram_Variable22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Variable__activitydiagram_Variable22", None)
        self.__activitydiagram_Variable22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_Value23"):
                opp_val = getattr(old_value, "activitydiagram_Value23", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_Value23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Value23"):
                opp_val = getattr(value, "activitydiagram_Value23", None)
                setattr(value, "activitydiagram_Value23", self)

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
            if hasattr(old_value, "activitydiagram_Value"):
                opp_val = getattr(old_value, "activitydiagram_Value", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_Value", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Value"):
                opp_val = getattr(value, "activitydiagram_Value", None)
                setattr(value, "activitydiagram_Value", self)

    def print(self):
        # TODO: Implement print method
        pass

    def execute(self, activitydiagram_c):
        # TODO: Implement execute method
        pass

    def init(self, activitydiagram_c):
        # TODO: Implement init method
        pass

class NamedElement:

    pass
class activitydiagram_ActivityEdge(NamedElement):

    def __init__(self, ActivityEdge: "activitydiagram_ActivityNode" = None, ActivityEdge9: "activitydiagram_ActivityNode" = None, outgoing: "activitydiagram_ActivityNode" = None, incoming: "activitydiagram_ActivityNode" = None, activitydiagram_ActivityEdge: "activitydiagram_Activity" = None, activitydiagram_ActivityEdge16: set["activitydiagram_Offer"] = None):
        self.ActivityEdge = ActivityEdge
        self.ActivityEdge9 = ActivityEdge9
        self.outgoing = outgoing
        self.incoming = incoming
        self.activitydiagram_ActivityEdge = activitydiagram_ActivityEdge
        self.activitydiagram_ActivityEdge16 = activitydiagram_ActivityEdge16 if activitydiagram_ActivityEdge16 is not None else set()
        
        pass
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
            if hasattr(old_value, "ActivityNode12"):
                opp_val = getattr(old_value, "ActivityNode12", None)
                if opp_val == self:
                    setattr(old_value, "ActivityNode12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActivityNode12"):
                opp_val = getattr(value, "ActivityNode12", None)
                setattr(value, "ActivityNode12", self)

    @property
    def ActivityEdge9(self):
        return self.__ActivityEdge9

    @ActivityEdge9.setter
    def ActivityEdge9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__ActivityEdge9", None)
        self.__ActivityEdge9 = value
        
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
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActivityNode14"):
                opp_val = getattr(old_value, "ActivityNode14", None)
                if opp_val == self:
                    setattr(old_value, "ActivityNode14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActivityNode14"):
                opp_val = getattr(value, "ActivityNode14", None)
                setattr(value, "ActivityNode14", self)

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
    def activitydiagram_ActivityEdge16(self):
        return self.__activitydiagram_ActivityEdge16

    @activitydiagram_ActivityEdge16.setter
    def activitydiagram_ActivityEdge16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityEdge__activitydiagram_ActivityEdge16", None)
        self.__activitydiagram_ActivityEdge16 = value if value is not None else set()
        
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

    def sendOffer(self, activitydiagram_tokens):
        # TODO: Implement sendOffer method
        pass

    def takeOfferedTokens(self) :
        # TODO: Implement takeOfferedTokens method
        pass

    def hasOffer(self):
        # TODO: Implement hasOffer method
        pass

class activitydiagram_ActivityNode(NamedElement):

    def __init__(self, running: bool, ActivityNode: "activitydiagram_Activity" = None, source: set["activitydiagram_ActivityEdge"] = None, target: set["activitydiagram_ActivityEdge"] = None, nodes: "activitydiagram_Activity" = None, ActivityNode12: "activitydiagram_ActivityEdge" = None, ActivityNode14: "activitydiagram_ActivityEdge" = None, activitydiagram_ActivityNode: "activitydiagram_Token" = None, activitydiagram_ActivityNode66: "activitydiagram_Trace" = None):
        self.running = running
        self.ActivityNode = ActivityNode
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.nodes = nodes
        self.ActivityNode12 = ActivityNode12
        self.ActivityNode14 = ActivityNode14
        self.activitydiagram_ActivityNode = activitydiagram_ActivityNode
        self.activitydiagram_ActivityNode66 = activitydiagram_ActivityNode66
        
        pass
    @property
    def running(self):
        return self.__running

    @running.setter
    def running(self, running: bool):
        self.__running = running


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
    def activitydiagram_ActivityNode(self):
        return self.__activitydiagram_ActivityNode

    @activitydiagram_ActivityNode.setter
    def activitydiagram_ActivityNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_ActivityNode__activitydiagram_ActivityNode", None)
        self.__activitydiagram_ActivityNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_Token51"):
                opp_val = getattr(old_value, "activitydiagram_Token51", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_Token51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Token51"):
                opp_val = getattr(value, "activitydiagram_Token51", None)
                setattr(value, "activitydiagram_Token51", self)

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

    def addTokens(self, activitydiagram_tokens):
        # TODO: Implement addTokens method
        pass

    def sendOffers(self, activitydiagram_tokens):
        # TODO: Implement sendOffers method
        pass

    def execute(self, activitydiagram_c):
        # TODO: Implement execute method
        pass

    def removeToken(self, activitydiagram_token):
        # TODO: Implement removeToken method
        pass

    def isReady(self):
        # TODO: Implement isReady method
        pass

    def terminate(self):
        # TODO: Implement terminate method
        pass

    def takeOfferdTokens(self) :
        # TODO: Implement takeOfferdTokens method
        pass

    def hasOffers(self):
        # TODO: Implement hasOffers method
        pass

class activitydiagram_Activity(NamedElement):

    def __init__(self, activitydiagram_Activity55: "activitydiagram_Context" = None, activity: set["activitydiagram_ActivityNode"] = None, activitydiagram_Activity5: set["activitydiagram_Variable"] = None, Activity: "activitydiagram_ActivityNode" = None, activitydiagram_Activity: set["activitydiagram_ActivityEdge"] = None, activitydiagram_Activity3: set["activitydiagram_Variable"] = None):
        self.activitydiagram_Activity55 = activitydiagram_Activity55
        self.activity = activity if activity is not None else set()
        self.activitydiagram_Activity5 = activitydiagram_Activity5 if activitydiagram_Activity5 is not None else set()
        self.Activity = Activity
        self.activitydiagram_Activity = activitydiagram_Activity if activitydiagram_Activity is not None else set()
        self.activitydiagram_Activity3 = activitydiagram_Activity3 if activitydiagram_Activity3 is not None else set()
        
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
    def activitydiagram_Activity55(self):
        return self.__activitydiagram_Activity55

    @activitydiagram_Activity55.setter
    def activitydiagram_Activity55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activitydiagram_Activity__activitydiagram_Activity55", None)
        self.__activitydiagram_Activity55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activitydiagram_Context54"):
                opp_val = getattr(old_value, "activitydiagram_Context54", None)
                if opp_val == self:
                    setattr(old_value, "activitydiagram_Context54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activitydiagram_Context54"):
                opp_val = getattr(value, "activitydiagram_Context54", None)
                setattr(value, "activitydiagram_Context54", self)

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
                    

    def writeToFile(self):
        # TODO: Implement writeToFile method
        pass

    def getBooleanVariableValue(self, activitydiagram_variableName):
        # TODO: Implement getBooleanVariableValue method
        pass

    def execute(self, activitydiagram_c):
        # TODO: Implement execute method
        pass

    def getIntegerVariableValue(self, activitydiagram_variableName):
        # TODO: Implement getIntegerVariableValue method
        pass

    def reset(self):
        # TODO: Implement reset method
        pass

    def main(self, activitydiagram_value):
        # TODO: Implement main method
        pass

    def getVariableValue(self, activitydiagram_variableName) :
        # TODO: Implement getVariableValue method
        pass

    def getVariable(self, activitydiagram_variableName) :
        # TODO: Implement getVariable method
        pass

    def writeTrace(self):
        # TODO: Implement writeTrace method
        pass

    def printTrace(self):
        # TODO: Implement printTrace method
        pass
