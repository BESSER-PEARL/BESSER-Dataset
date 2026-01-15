from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class restbehavior_MediaTypeLink:

    pass
class MTReference:

    pass
class restbehavior_MTLinkReference(MTReference):

    pass
class Reference:

    pass
class restbehavior_MTReference(Reference):

    pass
class restbehavior_InternalLink:

    pass
class restbehavior_Attribute:

    pass
class WritableReference:

    pass
class restbehavior_InternalLinkReference(WritableReference):

    pass
class restbehavior_AttributeReference(WritableReference):

    pass
class restbehavior_ExternalLink:

    pass
class restbehavior_ExternalLinkReference(WritableReference):

    pass
class State:

    pass
class restbehavior_DeletedState(State):

    pass
class restbehavior_MediaTypeElement:

    pass
class restbehavior_MtElementReference(MTReference):

    pass
class Operation:

    pass
class restbehavior_BinaryOperation(Operation):

    pass
class restbehavior_DataType:

    pass
class Value:

    pass
class restbehavior_Reference(Value):

    pass
class restbehavior_Operation(Value):

    pass
class restbehavior_Constant(Value):

    def __init__(self, stringRepresentation: str, restbehavior_Constant: "restbehavior_DataType" = None):
        self.stringRepresentation = stringRepresentation
        self.restbehavior_Constant = restbehavior_Constant
        
    @property
    def stringRepresentation(self) -> str:
        return self.__stringRepresentation

    @stringRepresentation.setter
    def stringRepresentation(self, stringRepresentation: str):
        self.__stringRepresentation = stringRepresentation

    @property
    def restbehavior_Constant(self):
        return self.__restbehavior_Constant

    @restbehavior_Constant.setter
    def restbehavior_Constant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_restbehavior_Constant__restbehavior_Constant", None)
        self.__restbehavior_Constant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "restbehavior_DataType"):
                opp_val = getattr(old_value, "restbehavior_DataType", None)
                if opp_val == self:
                    setattr(old_value, "restbehavior_DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "restbehavior_DataType"):
                opp_val = getattr(value, "restbehavior_DataType", None)
                setattr(value, "restbehavior_DataType", self)

class OpType:

    pass
class restbehavior_BinOpType(OpType):

    pass
class restbehavior_OpType(ABC):

    def __init__(self, name: str, restbehavior_OpType: "restbehavior_DataType" = None):
        self.name = name
        self.restbehavior_OpType = restbehavior_OpType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def restbehavior_OpType(self):
        return self.__restbehavior_OpType

    @restbehavior_OpType.setter
    def restbehavior_OpType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_restbehavior_OpType__restbehavior_OpType", None)
        self.__restbehavior_OpType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "restbehavior_DataType59"):
                opp_val = getattr(old_value, "restbehavior_DataType59", None)
                if opp_val == self:
                    setattr(old_value, "restbehavior_DataType59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "restbehavior_DataType59"):
                opp_val = getattr(value, "restbehavior_DataType59", None)
                setattr(value, "restbehavior_DataType59", self)

class restbehavior_WritableReference(Reference):

    pass
class restbehavior_Representation:

    pass
class restbehavior_Metadata:

    pass
class restbehavior_StatusCode:

    def __init__(self, number: int, restbehavior_StatusCode: "restbehavior_ReturnAction" = None):
        self.number = number
        self.restbehavior_StatusCode = restbehavior_StatusCode
        
    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def restbehavior_StatusCode(self):
        return self.__restbehavior_StatusCode

    @restbehavior_StatusCode.setter
    def restbehavior_StatusCode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_restbehavior_StatusCode__restbehavior_StatusCode", None)
        self.__restbehavior_StatusCode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "restbehavior_ReturnAction"):
                opp_val = getattr(old_value, "restbehavior_ReturnAction", None)
                if opp_val == self:
                    setattr(old_value, "restbehavior_ReturnAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "restbehavior_ReturnAction"):
                opp_val = getattr(value, "restbehavior_ReturnAction", None)
                setattr(value, "restbehavior_ReturnAction", self)

class Action:

    pass
class restbehavior_UpdateAction(Action):

    pass
class restbehavior_ActionSequence(Action):

    pass
class restbehavior_ListAddAction(Action):

    pass
class restbehavior_ReturnAction(Action):

    pass
class restbehavior_ConditionalAction(Action):

    pass
class restbehavior_CreateAction(Action):

    pass
class restbehavior_ListRemoveAction(Action):

    pass
class restbehavior_MessageAction(Action):

    pass
class Trigger:

    pass
class restbehavior_InternalMessage(Trigger):

    def __init__(self, name: str, restbehavior_InternalMessage: "restbehavior_MessageAction" = None):
        self.name = name
        self.restbehavior_InternalMessage = restbehavior_InternalMessage
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def restbehavior_InternalMessage(self):
        return self.__restbehavior_InternalMessage

    @restbehavior_InternalMessage.setter
    def restbehavior_InternalMessage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_restbehavior_InternalMessage__restbehavior_InternalMessage", None)
        self.__restbehavior_InternalMessage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "restbehavior_MessageAction"):
                opp_val = getattr(old_value, "restbehavior_MessageAction", None)
                if opp_val == self:
                    setattr(old_value, "restbehavior_MessageAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "restbehavior_MessageAction"):
                opp_val = getattr(value, "restbehavior_MessageAction", None)
                setattr(value, "restbehavior_MessageAction", self)

class restbehavior_Value(ABC):

    pass
class restbehavior_Condition:

    pass
class restbehavior_Trigger(ABC):

    pass
class restbehavior_Method:

    pass
class restbehavior_Transition:

    pass
class restbehavior_State:

    def __init__(self, name: str, restbehavior_State15: set["restbehavior_Method"] = None, restbehavior_State: "restbehavior_BehaviorSpecification" = None, restbehavior_State10: "restbehavior_BehaviorSpecification" = None, restbehavior_State13: set["restbehavior_Transition"] = None, restbehavior_State20: "restbehavior_Transition" = None):
        self.name = name
        self.restbehavior_State15 = restbehavior_State15 if restbehavior_State15 is not None else set()
        self.restbehavior_State = restbehavior_State
        self.restbehavior_State10 = restbehavior_State10
        self.restbehavior_State13 = restbehavior_State13 if restbehavior_State13 is not None else set()
        self.restbehavior_State20 = restbehavior_State20
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def restbehavior_State15(self):
        return self.__restbehavior_State15

    @restbehavior_State15.setter
    def restbehavior_State15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_restbehavior_State__restbehavior_State15", None)
        self.__restbehavior_State15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "restbehavior_Method"):
                    opp_val = getattr(item, "restbehavior_Method", None)
                    
                    if opp_val == self:
                        setattr(item, "restbehavior_Method", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "restbehavior_Method"):
                    opp_val = getattr(item, "restbehavior_Method", None)
                    
                    setattr(item, "restbehavior_Method", self)
                    

    @property
    def restbehavior_State13(self):
        return self.__restbehavior_State13

    @restbehavior_State13.setter
    def restbehavior_State13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_restbehavior_State__restbehavior_State13", None)
        self.__restbehavior_State13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "restbehavior_Transition"):
                    opp_val = getattr(item, "restbehavior_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "restbehavior_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "restbehavior_Transition"):
                    opp_val = getattr(item, "restbehavior_Transition", None)
                    
                    setattr(item, "restbehavior_Transition", self)
                    

    @property
    def restbehavior_State20(self):
        return self.__restbehavior_State20

    @restbehavior_State20.setter
    def restbehavior_State20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_restbehavior_State__restbehavior_State20", None)
        self.__restbehavior_State20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "restbehavior_Transition19"):
                opp_val = getattr(old_value, "restbehavior_Transition19", None)
                if opp_val == self:
                    setattr(old_value, "restbehavior_Transition19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "restbehavior_Transition19"):
                opp_val = getattr(value, "restbehavior_Transition19", None)
                setattr(value, "restbehavior_Transition19", self)

    @property
    def restbehavior_State10(self):
        return self.__restbehavior_State10

    @restbehavior_State10.setter
    def restbehavior_State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_restbehavior_State__restbehavior_State10", None)
        self.__restbehavior_State10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "restbehavior_BehaviorSpecification11"):
                opp_val = getattr(old_value, "restbehavior_BehaviorSpecification11", None)
                if opp_val == self:
                    setattr(old_value, "restbehavior_BehaviorSpecification11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "restbehavior_BehaviorSpecification11"):
                opp_val = getattr(value, "restbehavior_BehaviorSpecification11", None)
                setattr(value, "restbehavior_BehaviorSpecification11", self)

    @property
    def restbehavior_State(self):
        return self.__restbehavior_State

    @restbehavior_State.setter
    def restbehavior_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_restbehavior_State__restbehavior_State", None)
        self.__restbehavior_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "restbehavior_BehaviorSpecification8"):
                opp_val = getattr(old_value, "restbehavior_BehaviorSpecification8", None)
                if opp_val == self:
                    setattr(old_value, "restbehavior_BehaviorSpecification8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "restbehavior_BehaviorSpecification8"):
                opp_val = getattr(value, "restbehavior_BehaviorSpecification8", None)
                setattr(value, "restbehavior_BehaviorSpecification8", self)

class restbehavior_Action(ABC):

    pass
class restbehavior_BehaviorSpecification:

    pass
class restbehavior_Parameter:

    pass
class restbehavior_MediaType:

    pass
class restbehavior_Creator:

    pass