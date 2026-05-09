from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Actions_Let:

    pass
class ActionMessageExpression:

    pass
class HALL_Actions_Literal(ActionMessageExpression):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class HALL_Actions_BinaryOperator(ActionMessageExpression):

    def __init__(self, operatorname: str, HALL_Actions_BinaryOperator: "Actions_ActionMessageExpression" = None, HALL_Actions_BinaryOperator182: "Actions_ActionMessageExpression" = None):
        self.operatorname = operatorname
        self.HALL_Actions_BinaryOperator = HALL_Actions_BinaryOperator
        self.HALL_Actions_BinaryOperator182 = HALL_Actions_BinaryOperator182
        
        pass
    @property
    def operatorname(self):
        return self.__operatorname

    @operatorname.setter
    def operatorname(self, operatorname: str):
        self.__operatorname = operatorname


    @property
    def HALL_Actions_BinaryOperator(self):
        return self.__HALL_Actions_BinaryOperator

    @HALL_Actions_BinaryOperator.setter
    def HALL_Actions_BinaryOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Actions_BinaryOperator__HALL_Actions_BinaryOperator", None)
        self.__HALL_Actions_BinaryOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Actions_ActionMessageExpression180"):
                opp_val = getattr(old_value, "Actions_ActionMessageExpression180", None)
                if opp_val == self:
                    setattr(old_value, "Actions_ActionMessageExpression180", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Actions_ActionMessageExpression180"):
                opp_val = getattr(value, "Actions_ActionMessageExpression180", None)
                setattr(value, "Actions_ActionMessageExpression180", self)

    @property
    def HALL_Actions_BinaryOperator182(self):
        return self.__HALL_Actions_BinaryOperator182

    @HALL_Actions_BinaryOperator182.setter
    def HALL_Actions_BinaryOperator182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Actions_BinaryOperator__HALL_Actions_BinaryOperator182", None)
        self.__HALL_Actions_BinaryOperator182 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Actions_ActionMessageExpression183"):
                opp_val = getattr(old_value, "Actions_ActionMessageExpression183", None)
                if opp_val == self:
                    setattr(old_value, "Actions_ActionMessageExpression183", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Actions_ActionMessageExpression183"):
                opp_val = getattr(value, "Actions_ActionMessageExpression183", None)
                setattr(value, "Actions_ActionMessageExpression183", self)

class HALL_Actions_Let(ActionMessageExpression):

    pass
class FSMActions_Let:

    pass
class SimpleType:

    pass
class HALL_Types_Boolean(SimpleType):

    pass
class HALL_Types_String(SimpleType):

    pass
class HALL_Types_Number(SimpleType):

    pass
class Set:

    pass
class HALL_Types_Type(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class FSMActions_HALL_Data:

    pass
class HALL_FSMActions_Enable(ActionMessageExpression):

    pass
class FSMConditions_HALL_Component:

    pass
class ActionExpression:

    pass
class HALL_FSMActions_UnaryOperator(ActionExpression):

    def __init__(self, operatorname: str, HALL_FSMActions_UnaryOperator: "FSMActions_ActionExpression" = None):
        self.operatorname = operatorname
        self.HALL_FSMActions_UnaryOperator = HALL_FSMActions_UnaryOperator
        
        pass
    @property
    def operatorname(self):
        return self.__operatorname

    @operatorname.setter
    def operatorname(self, operatorname: str):
        self.__operatorname = operatorname


    @property
    def HALL_FSMActions_UnaryOperator(self):
        return self.__HALL_FSMActions_UnaryOperator

    @HALL_FSMActions_UnaryOperator.setter
    def HALL_FSMActions_UnaryOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMActions_UnaryOperator__HALL_FSMActions_UnaryOperator", None)
        self.__HALL_FSMActions_UnaryOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMActions_ActionExpression308"):
                opp_val = getattr(old_value, "FSMActions_ActionExpression308", None)
                if opp_val == self:
                    setattr(old_value, "FSMActions_ActionExpression308", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMActions_ActionExpression308"):
                opp_val = getattr(value, "FSMActions_ActionExpression308", None)
                setattr(value, "FSMActions_ActionExpression308", self)

class HALL_FSMActions_DomainPropertySet(ActionExpression):

    def __init__(self, name: str, HALL_FSMActions_DomainPropertySet: "FSMActions_ActionExpression" = None):
        self.name = name
        self.HALL_FSMActions_DomainPropertySet = HALL_FSMActions_DomainPropertySet
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def HALL_FSMActions_DomainPropertySet(self):
        return self.__HALL_FSMActions_DomainPropertySet

    @HALL_FSMActions_DomainPropertySet.setter
    def HALL_FSMActions_DomainPropertySet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMActions_DomainPropertySet__HALL_FSMActions_DomainPropertySet", None)
        self.__HALL_FSMActions_DomainPropertySet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMActions_ActionExpression300"):
                opp_val = getattr(old_value, "FSMActions_ActionExpression300", None)
                if opp_val == self:
                    setattr(old_value, "FSMActions_ActionExpression300", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMActions_ActionExpression300"):
                opp_val = getattr(value, "FSMActions_ActionExpression300", None)
                setattr(value, "FSMActions_ActionExpression300", self)

class HALL_FSMActions_DomainPropertyGet(ActionExpression):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class HALL_FSMActions_VarRef(ActionExpression):

    pass
class HALL_FSMActions_BinaryOperator(ActionExpression):

    def __init__(self, operatorname: str, HALL_FSMActions_BinaryOperator: "FSMActions_ActionExpression" = None, HALL_FSMActions_BinaryOperator305: "FSMActions_ActionExpression" = None):
        self.operatorname = operatorname
        self.HALL_FSMActions_BinaryOperator = HALL_FSMActions_BinaryOperator
        self.HALL_FSMActions_BinaryOperator305 = HALL_FSMActions_BinaryOperator305
        
        pass
    @property
    def operatorname(self):
        return self.__operatorname

    @operatorname.setter
    def operatorname(self, operatorname: str):
        self.__operatorname = operatorname


    @property
    def HALL_FSMActions_BinaryOperator(self):
        return self.__HALL_FSMActions_BinaryOperator

    @HALL_FSMActions_BinaryOperator.setter
    def HALL_FSMActions_BinaryOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMActions_BinaryOperator__HALL_FSMActions_BinaryOperator", None)
        self.__HALL_FSMActions_BinaryOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMActions_ActionExpression303"):
                opp_val = getattr(old_value, "FSMActions_ActionExpression303", None)
                if opp_val == self:
                    setattr(old_value, "FSMActions_ActionExpression303", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMActions_ActionExpression303"):
                opp_val = getattr(value, "FSMActions_ActionExpression303", None)
                setattr(value, "FSMActions_ActionExpression303", self)

    @property
    def HALL_FSMActions_BinaryOperator305(self):
        return self.__HALL_FSMActions_BinaryOperator305

    @HALL_FSMActions_BinaryOperator305.setter
    def HALL_FSMActions_BinaryOperator305(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMActions_BinaryOperator__HALL_FSMActions_BinaryOperator305", None)
        self.__HALL_FSMActions_BinaryOperator305 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMActions_ActionExpression306"):
                opp_val = getattr(old_value, "FSMActions_ActionExpression306", None)
                if opp_val == self:
                    setattr(old_value, "FSMActions_ActionExpression306", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMActions_ActionExpression306"):
                opp_val = getattr(value, "FSMActions_ActionExpression306", None)
                setattr(value, "FSMActions_ActionExpression306", self)

class HALL_FSMActions_MessageInvocation(ActionExpression):

    def __init__(self, isTopDown: bool, HALL_FSMActions_MessageInvocation: "MessageDefinition" = None, HALL_FSMActions_MessageInvocation292: set["FSMActions_ActionExpression"] = None):
        self.isTopDown = isTopDown
        self.HALL_FSMActions_MessageInvocation = HALL_FSMActions_MessageInvocation
        self.HALL_FSMActions_MessageInvocation292 = HALL_FSMActions_MessageInvocation292 if HALL_FSMActions_MessageInvocation292 is not None else set()
        
        pass
    @property
    def isTopDown(self):
        return self.__isTopDown

    @isTopDown.setter
    def isTopDown(self, isTopDown: bool):
        self.__isTopDown = isTopDown


    @property
    def HALL_FSMActions_MessageInvocation292(self):
        return self.__HALL_FSMActions_MessageInvocation292

    @HALL_FSMActions_MessageInvocation292.setter
    def HALL_FSMActions_MessageInvocation292(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMActions_MessageInvocation__HALL_FSMActions_MessageInvocation292", None)
        self.__HALL_FSMActions_MessageInvocation292 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FSMActions_ActionExpression293"):
                    opp_val = getattr(item, "FSMActions_ActionExpression293", None)
                    
                    if opp_val == self:
                        setattr(item, "FSMActions_ActionExpression293", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FSMActions_ActionExpression293"):
                    opp_val = getattr(item, "FSMActions_ActionExpression293", None)
                    
                    setattr(item, "FSMActions_ActionExpression293", self)
                    

    @property
    def HALL_FSMActions_MessageInvocation(self):
        return self.__HALL_FSMActions_MessageInvocation

    @HALL_FSMActions_MessageInvocation.setter
    def HALL_FSMActions_MessageInvocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMActions_MessageInvocation__HALL_FSMActions_MessageInvocation", None)
        self.__HALL_FSMActions_MessageInvocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MessageDefinition290"):
                opp_val = getattr(old_value, "MessageDefinition290", None)
                if opp_val == self:
                    setattr(old_value, "MessageDefinition290", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MessageDefinition290"):
                opp_val = getattr(value, "MessageDefinition290", None)
                setattr(value, "MessageDefinition290", self)

class HALL_FSMActions_GetData(ActionExpression):

    pass
class HALL_FSMActions_Let(ActionExpression):

    def __init__(self, name: str, HALL_FSMActions_Let: "FSMActions_ActionExpression" = None, HALL_FSMActions_Let284: "FSMActions_ActionExpression" = None, HALL_FSMActions_Let287: "Type" = None):
        self.name = name
        self.HALL_FSMActions_Let = HALL_FSMActions_Let
        self.HALL_FSMActions_Let284 = HALL_FSMActions_Let284
        self.HALL_FSMActions_Let287 = HALL_FSMActions_Let287
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def HALL_FSMActions_Let287(self):
        return self.__HALL_FSMActions_Let287

    @HALL_FSMActions_Let287.setter
    def HALL_FSMActions_Let287(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMActions_Let__HALL_FSMActions_Let287", None)
        self.__HALL_FSMActions_Let287 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type288"):
                opp_val = getattr(old_value, "Type288", None)
                if opp_val == self:
                    setattr(old_value, "Type288", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type288"):
                opp_val = getattr(value, "Type288", None)
                setattr(value, "Type288", self)

    @property
    def HALL_FSMActions_Let(self):
        return self.__HALL_FSMActions_Let

    @HALL_FSMActions_Let.setter
    def HALL_FSMActions_Let(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMActions_Let__HALL_FSMActions_Let", None)
        self.__HALL_FSMActions_Let = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMActions_ActionExpression282"):
                opp_val = getattr(old_value, "FSMActions_ActionExpression282", None)
                if opp_val == self:
                    setattr(old_value, "FSMActions_ActionExpression282", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMActions_ActionExpression282"):
                opp_val = getattr(value, "FSMActions_ActionExpression282", None)
                setattr(value, "FSMActions_ActionExpression282", self)

    @property
    def HALL_FSMActions_Let284(self):
        return self.__HALL_FSMActions_Let284

    @HALL_FSMActions_Let284.setter
    def HALL_FSMActions_Let284(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMActions_Let__HALL_FSMActions_Let284", None)
        self.__HALL_FSMActions_Let284 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMActions_ActionExpression285"):
                opp_val = getattr(old_value, "FSMActions_ActionExpression285", None)
                if opp_val == self:
                    setattr(old_value, "FSMActions_ActionExpression285", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMActions_ActionExpression285"):
                opp_val = getattr(value, "FSMActions_ActionExpression285", None)
                setattr(value, "FSMActions_ActionExpression285", self)

class HALL_FSMActions_Literal(ActionExpression):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class HALL_FSMActions_ActionExpression:

    pass
class FSMActions_ActionExpression:

    pass
class HALL_FSMActions_Action:

    pass
class FSMConditions_Let:

    pass
class FSMConditions_HALL_Data:

    pass
class PreConditionExpression:

    pass
class HALL_FSMConditions_UnaryOperator(PreConditionExpression):

    def __init__(self, operatorname: str, HALL_FSMConditions_UnaryOperator: "FSMConditions_PreConditionExpression" = None):
        self.operatorname = operatorname
        self.HALL_FSMConditions_UnaryOperator = HALL_FSMConditions_UnaryOperator
        
        pass
    @property
    def operatorname(self):
        return self.__operatorname

    @operatorname.setter
    def operatorname(self, operatorname: str):
        self.__operatorname = operatorname


    @property
    def HALL_FSMConditions_UnaryOperator(self):
        return self.__HALL_FSMConditions_UnaryOperator

    @HALL_FSMConditions_UnaryOperator.setter
    def HALL_FSMConditions_UnaryOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMConditions_UnaryOperator__HALL_FSMConditions_UnaryOperator", None)
        self.__HALL_FSMConditions_UnaryOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMConditions_PreConditionExpression268"):
                opp_val = getattr(old_value, "FSMConditions_PreConditionExpression268", None)
                if opp_val == self:
                    setattr(old_value, "FSMConditions_PreConditionExpression268", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMConditions_PreConditionExpression268"):
                opp_val = getattr(value, "FSMConditions_PreConditionExpression268", None)
                setattr(value, "FSMConditions_PreConditionExpression268", self)

class HALL_FSMConditions_GetState(PreConditionExpression):

    pass
class HALL_FSMConditions_BinaryOperator(PreConditionExpression):

    def __init__(self, operatorname: str, HALL_FSMConditions_BinaryOperator: "FSMConditions_PreConditionExpression" = None, HALL_FSMConditions_BinaryOperator265: "FSMConditions_PreConditionExpression" = None):
        self.operatorname = operatorname
        self.HALL_FSMConditions_BinaryOperator = HALL_FSMConditions_BinaryOperator
        self.HALL_FSMConditions_BinaryOperator265 = HALL_FSMConditions_BinaryOperator265
        
        pass
    @property
    def operatorname(self):
        return self.__operatorname

    @operatorname.setter
    def operatorname(self, operatorname: str):
        self.__operatorname = operatorname


    @property
    def HALL_FSMConditions_BinaryOperator265(self):
        return self.__HALL_FSMConditions_BinaryOperator265

    @HALL_FSMConditions_BinaryOperator265.setter
    def HALL_FSMConditions_BinaryOperator265(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMConditions_BinaryOperator__HALL_FSMConditions_BinaryOperator265", None)
        self.__HALL_FSMConditions_BinaryOperator265 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMConditions_PreConditionExpression266"):
                opp_val = getattr(old_value, "FSMConditions_PreConditionExpression266", None)
                if opp_val == self:
                    setattr(old_value, "FSMConditions_PreConditionExpression266", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMConditions_PreConditionExpression266"):
                opp_val = getattr(value, "FSMConditions_PreConditionExpression266", None)
                setattr(value, "FSMConditions_PreConditionExpression266", self)

    @property
    def HALL_FSMConditions_BinaryOperator(self):
        return self.__HALL_FSMConditions_BinaryOperator

    @HALL_FSMConditions_BinaryOperator.setter
    def HALL_FSMConditions_BinaryOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMConditions_BinaryOperator__HALL_FSMConditions_BinaryOperator", None)
        self.__HALL_FSMConditions_BinaryOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMConditions_PreConditionExpression263"):
                opp_val = getattr(old_value, "FSMConditions_PreConditionExpression263", None)
                if opp_val == self:
                    setattr(old_value, "FSMConditions_PreConditionExpression263", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMConditions_PreConditionExpression263"):
                opp_val = getattr(value, "FSMConditions_PreConditionExpression263", None)
                setattr(value, "FSMConditions_PreConditionExpression263", self)

class HALL_FSMConditions_GetData(PreConditionExpression):

    pass
class HALL_FSMConditions_VarRef(PreConditionExpression):

    pass
class HALL_FSMConditions_DomainPropertyGet(PreConditionExpression):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class HALL_FSMConditions_Let(PreConditionExpression):

    def __init__(self, name: str, HALL_FSMConditions_Let: "FSMConditions_PreConditionExpression" = None, HALL_FSMConditions_Let274: "FSMConditions_PreConditionExpression" = None, HALL_FSMConditions_Let277: "Type" = None):
        self.name = name
        self.HALL_FSMConditions_Let = HALL_FSMConditions_Let
        self.HALL_FSMConditions_Let274 = HALL_FSMConditions_Let274
        self.HALL_FSMConditions_Let277 = HALL_FSMConditions_Let277
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def HALL_FSMConditions_Let(self):
        return self.__HALL_FSMConditions_Let

    @HALL_FSMConditions_Let.setter
    def HALL_FSMConditions_Let(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMConditions_Let__HALL_FSMConditions_Let", None)
        self.__HALL_FSMConditions_Let = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMConditions_PreConditionExpression272"):
                opp_val = getattr(old_value, "FSMConditions_PreConditionExpression272", None)
                if opp_val == self:
                    setattr(old_value, "FSMConditions_PreConditionExpression272", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMConditions_PreConditionExpression272"):
                opp_val = getattr(value, "FSMConditions_PreConditionExpression272", None)
                setattr(value, "FSMConditions_PreConditionExpression272", self)

    @property
    def HALL_FSMConditions_Let274(self):
        return self.__HALL_FSMConditions_Let274

    @HALL_FSMConditions_Let274.setter
    def HALL_FSMConditions_Let274(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMConditions_Let__HALL_FSMConditions_Let274", None)
        self.__HALL_FSMConditions_Let274 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMConditions_PreConditionExpression275"):
                opp_val = getattr(old_value, "FSMConditions_PreConditionExpression275", None)
                if opp_val == self:
                    setattr(old_value, "FSMConditions_PreConditionExpression275", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMConditions_PreConditionExpression275"):
                opp_val = getattr(value, "FSMConditions_PreConditionExpression275", None)
                setattr(value, "FSMConditions_PreConditionExpression275", self)

    @property
    def HALL_FSMConditions_Let277(self):
        return self.__HALL_FSMConditions_Let277

    @HALL_FSMConditions_Let277.setter
    def HALL_FSMConditions_Let277(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMConditions_Let__HALL_FSMConditions_Let277", None)
        self.__HALL_FSMConditions_Let277 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type278"):
                opp_val = getattr(old_value, "Type278", None)
                if opp_val == self:
                    setattr(old_value, "Type278", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type278"):
                opp_val = getattr(value, "Type278", None)
                setattr(value, "Type278", self)

class HALL_FSMConditions_Literal(PreConditionExpression):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class HALL_FSMConditions_PreConditionExpression(ABC):

    pass
class FSMConditions_PreConditionExpression:

    pass
class HALL_FSMConditions_PreCondition:

    pass
class FSMInstructions_Let:

    pass
class FSMInstructions_HALL_Data:

    pass
class TriggerExpression:

    pass
class HALL_Trigger_MessageNotification(TriggerExpression):

    pass
class HALL_Trigger_TriggerExpression(ABC):

    pass
class Trigger_TriggerExpression:

    pass
class HALL_Trigger_Trigger:

    pass
class FSMInstructions_HALL_Component:

    pass
class PosConditionExpression:

    pass
class HALL_FSMInstructions_SetState(PosConditionExpression):

    pass
class HALL_FSMInstructions_GetState(PosConditionExpression):

    pass
class HALL_FSMInstructions_UnaryOperator(PosConditionExpression):

    def __init__(self, operatorname: str, HALL_FSMInstructions_UnaryOperator: "FSMInstructions_PosConditionExpression" = None):
        self.operatorname = operatorname
        self.HALL_FSMInstructions_UnaryOperator = HALL_FSMInstructions_UnaryOperator
        
        pass
    @property
    def operatorname(self):
        return self.__operatorname

    @operatorname.setter
    def operatorname(self, operatorname: str):
        self.__operatorname = operatorname


    @property
    def HALL_FSMInstructions_UnaryOperator(self):
        return self.__HALL_FSMInstructions_UnaryOperator

    @HALL_FSMInstructions_UnaryOperator.setter
    def HALL_FSMInstructions_UnaryOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMInstructions_UnaryOperator__HALL_FSMInstructions_UnaryOperator", None)
        self.__HALL_FSMInstructions_UnaryOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMInstructions_PosConditionExpression239"):
                opp_val = getattr(old_value, "FSMInstructions_PosConditionExpression239", None)
                if opp_val == self:
                    setattr(old_value, "FSMInstructions_PosConditionExpression239", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMInstructions_PosConditionExpression239"):
                opp_val = getattr(value, "FSMInstructions_PosConditionExpression239", None)
                setattr(value, "FSMInstructions_PosConditionExpression239", self)

class HALL_FSMInstructions_GetData(PosConditionExpression):

    def __init__(self, field: str, HALL_FSMInstructions_GetData: "FSMInstructions_HALL_Component" = None):
        self.field = field
        self.HALL_FSMInstructions_GetData = HALL_FSMInstructions_GetData
        
        pass
    @property
    def field(self):
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field


    @property
    def HALL_FSMInstructions_GetData(self):
        return self.__HALL_FSMInstructions_GetData

    @HALL_FSMInstructions_GetData.setter
    def HALL_FSMInstructions_GetData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMInstructions_GetData__HALL_FSMInstructions_GetData", None)
        self.__HALL_FSMInstructions_GetData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMInstructions_HALL_Component"):
                opp_val = getattr(old_value, "FSMInstructions_HALL_Component", None)
                if opp_val == self:
                    setattr(old_value, "FSMInstructions_HALL_Component", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMInstructions_HALL_Component"):
                opp_val = getattr(value, "FSMInstructions_HALL_Component", None)
                setattr(value, "FSMInstructions_HALL_Component", self)

class HALL_FSMInstructions_DomainPropertyGet(PosConditionExpression):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class HALL_FSMInstructions_VarRef(PosConditionExpression):

    pass
class HALL_FSMInstructions_Let(PosConditionExpression):

    def __init__(self, name: str, HALL_FSMInstructions_Let: "FSMInstructions_PosConditionExpression" = None, HALL_FSMInstructions_Let255: "FSMInstructions_PosConditionExpression" = None, HALL_FSMInstructions_Let258: "Type" = None):
        self.name = name
        self.HALL_FSMInstructions_Let = HALL_FSMInstructions_Let
        self.HALL_FSMInstructions_Let255 = HALL_FSMInstructions_Let255
        self.HALL_FSMInstructions_Let258 = HALL_FSMInstructions_Let258
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def HALL_FSMInstructions_Let(self):
        return self.__HALL_FSMInstructions_Let

    @HALL_FSMInstructions_Let.setter
    def HALL_FSMInstructions_Let(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMInstructions_Let__HALL_FSMInstructions_Let", None)
        self.__HALL_FSMInstructions_Let = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMInstructions_PosConditionExpression253"):
                opp_val = getattr(old_value, "FSMInstructions_PosConditionExpression253", None)
                if opp_val == self:
                    setattr(old_value, "FSMInstructions_PosConditionExpression253", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMInstructions_PosConditionExpression253"):
                opp_val = getattr(value, "FSMInstructions_PosConditionExpression253", None)
                setattr(value, "FSMInstructions_PosConditionExpression253", self)

    @property
    def HALL_FSMInstructions_Let255(self):
        return self.__HALL_FSMInstructions_Let255

    @HALL_FSMInstructions_Let255.setter
    def HALL_FSMInstructions_Let255(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMInstructions_Let__HALL_FSMInstructions_Let255", None)
        self.__HALL_FSMInstructions_Let255 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMInstructions_PosConditionExpression256"):
                opp_val = getattr(old_value, "FSMInstructions_PosConditionExpression256", None)
                if opp_val == self:
                    setattr(old_value, "FSMInstructions_PosConditionExpression256", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMInstructions_PosConditionExpression256"):
                opp_val = getattr(value, "FSMInstructions_PosConditionExpression256", None)
                setattr(value, "FSMInstructions_PosConditionExpression256", self)

    @property
    def HALL_FSMInstructions_Let258(self):
        return self.__HALL_FSMInstructions_Let258

    @HALL_FSMInstructions_Let258.setter
    def HALL_FSMInstructions_Let258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMInstructions_Let__HALL_FSMInstructions_Let258", None)
        self.__HALL_FSMInstructions_Let258 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type259"):
                opp_val = getattr(old_value, "Type259", None)
                if opp_val == self:
                    setattr(old_value, "Type259", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type259"):
                opp_val = getattr(value, "Type259", None)
                setattr(value, "Type259", self)

class HALL_FSMInstructions_SetData(PosConditionExpression):

    def __init__(self, field: str, HALL_FSMInstructions_SetData251: "FSMInstructions_HALL_Data" = None, HALL_FSMInstructions_SetData: "FSMInstructions_PosConditionExpression" = None):
        self.field = field
        self.HALL_FSMInstructions_SetData251 = HALL_FSMInstructions_SetData251
        self.HALL_FSMInstructions_SetData = HALL_FSMInstructions_SetData
        
        pass
    @property
    def field(self):
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field


    @property
    def HALL_FSMInstructions_SetData251(self):
        return self.__HALL_FSMInstructions_SetData251

    @HALL_FSMInstructions_SetData251.setter
    def HALL_FSMInstructions_SetData251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMInstructions_SetData__HALL_FSMInstructions_SetData251", None)
        self.__HALL_FSMInstructions_SetData251 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMInstructions_HALL_Data"):
                opp_val = getattr(old_value, "FSMInstructions_HALL_Data", None)
                if opp_val == self:
                    setattr(old_value, "FSMInstructions_HALL_Data", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMInstructions_HALL_Data"):
                opp_val = getattr(value, "FSMInstructions_HALL_Data", None)
                setattr(value, "FSMInstructions_HALL_Data", self)

    @property
    def HALL_FSMInstructions_SetData(self):
        return self.__HALL_FSMInstructions_SetData

    @HALL_FSMInstructions_SetData.setter
    def HALL_FSMInstructions_SetData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMInstructions_SetData__HALL_FSMInstructions_SetData", None)
        self.__HALL_FSMInstructions_SetData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMInstructions_PosConditionExpression249"):
                opp_val = getattr(old_value, "FSMInstructions_PosConditionExpression249", None)
                if opp_val == self:
                    setattr(old_value, "FSMInstructions_PosConditionExpression249", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMInstructions_PosConditionExpression249"):
                opp_val = getattr(value, "FSMInstructions_PosConditionExpression249", None)
                setattr(value, "FSMInstructions_PosConditionExpression249", self)

class HALL_FSMInstructions_BinaryOperator(PosConditionExpression):

    def __init__(self, operatorname: str, HALL_FSMInstructions_BinaryOperator: "FSMInstructions_PosConditionExpression" = None, HALL_FSMInstructions_BinaryOperator236: "FSMInstructions_PosConditionExpression" = None):
        self.operatorname = operatorname
        self.HALL_FSMInstructions_BinaryOperator = HALL_FSMInstructions_BinaryOperator
        self.HALL_FSMInstructions_BinaryOperator236 = HALL_FSMInstructions_BinaryOperator236
        
        pass
    @property
    def operatorname(self):
        return self.__operatorname

    @operatorname.setter
    def operatorname(self, operatorname: str):
        self.__operatorname = operatorname


    @property
    def HALL_FSMInstructions_BinaryOperator236(self):
        return self.__HALL_FSMInstructions_BinaryOperator236

    @HALL_FSMInstructions_BinaryOperator236.setter
    def HALL_FSMInstructions_BinaryOperator236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMInstructions_BinaryOperator__HALL_FSMInstructions_BinaryOperator236", None)
        self.__HALL_FSMInstructions_BinaryOperator236 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMInstructions_PosConditionExpression237"):
                opp_val = getattr(old_value, "FSMInstructions_PosConditionExpression237", None)
                if opp_val == self:
                    setattr(old_value, "FSMInstructions_PosConditionExpression237", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMInstructions_PosConditionExpression237"):
                opp_val = getattr(value, "FSMInstructions_PosConditionExpression237", None)
                setattr(value, "FSMInstructions_PosConditionExpression237", self)

    @property
    def HALL_FSMInstructions_BinaryOperator(self):
        return self.__HALL_FSMInstructions_BinaryOperator

    @HALL_FSMInstructions_BinaryOperator.setter
    def HALL_FSMInstructions_BinaryOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMInstructions_BinaryOperator__HALL_FSMInstructions_BinaryOperator", None)
        self.__HALL_FSMInstructions_BinaryOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMInstructions_PosConditionExpression234"):
                opp_val = getattr(old_value, "FSMInstructions_PosConditionExpression234", None)
                if opp_val == self:
                    setattr(old_value, "FSMInstructions_PosConditionExpression234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMInstructions_PosConditionExpression234"):
                opp_val = getattr(value, "FSMInstructions_PosConditionExpression234", None)
                setattr(value, "FSMInstructions_PosConditionExpression234", self)

class HALL_FSMInstructions_Literal(PosConditionExpression):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class HALL_FSMInstructions_PosConditionExpression(ABC):

    pass
class FSMInstructions_PosConditionExpression:

    pass
class HALL_FSMInstructions_PosCondition:

    pass
class HALL_Trigger_DomainEventFired(TriggerExpression):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class RegularState:

    pass
class InitialState:

    pass
class FSM_HALL_Component:

    pass
class HALL_FSM_FSM:

    pass
class Transition:

    pass
class HALL_FSM_State(ABC):

    def __init__(self, isActive: bool, name: str, source: set["Transition"] = None, HALL_FSM_State: "FSM" = None):
        self.isActive = isActive
        self.name = name
        self.source = source if source is not None else set()
        self.HALL_FSM_State = HALL_FSM_State
        
        pass
    @property
    def isActive(self):
        return self.__isActive

    @isActive.setter
    def isActive(self, isActive: bool):
        self.__isActive = isActive


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def HALL_FSM_State(self):
        return self.__HALL_FSM_State

    @HALL_FSM_State.setter
    def HALL_FSM_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSM_State__HALL_FSM_State", None)
        self.__HALL_FSM_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM228"):
                opp_val = getattr(old_value, "FSM228", None)
                if opp_val == self:
                    setattr(old_value, "FSM228", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM228"):
                opp_val = getattr(value, "FSM228", None)
                setattr(value, "FSM228", self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSM_State__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    setattr(item, "Transition", self)
                    

class Trigger_Trigger:

    pass
class FSMActions_Action:

    pass
class FSMInstructions_PosCondition:

    pass
class FSMConditions_PreCondition:

    pass
class HALL_FSM_Transition:

    def __init__(self, name: str, transitions214: "State" = None, HALL_FSM_Transition: "State" = None, HALL_FSM_Transition219: "FSMConditions_PreCondition" = None, HALL_FSM_Transition221: "FSMInstructions_PosCondition" = None, HALL_FSM_Transition223: "FSMActions_Action" = None, HALL_FSM_Transition225: "Trigger_Trigger" = None):
        self.name = name
        self.transitions214 = transitions214
        self.HALL_FSM_Transition = HALL_FSM_Transition
        self.HALL_FSM_Transition219 = HALL_FSM_Transition219
        self.HALL_FSM_Transition221 = HALL_FSM_Transition221
        self.HALL_FSM_Transition223 = HALL_FSM_Transition223
        self.HALL_FSM_Transition225 = HALL_FSM_Transition225
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def HALL_FSM_Transition223(self):
        return self.__HALL_FSM_Transition223

    @HALL_FSM_Transition223.setter
    def HALL_FSM_Transition223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSM_Transition__HALL_FSM_Transition223", None)
        self.__HALL_FSM_Transition223 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMActions_Action"):
                opp_val = getattr(old_value, "FSMActions_Action", None)
                if opp_val == self:
                    setattr(old_value, "FSMActions_Action", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMActions_Action"):
                opp_val = getattr(value, "FSMActions_Action", None)
                setattr(value, "FSMActions_Action", self)

    @property
    def transitions214(self):
        return self.__transitions214

    @transitions214.setter
    def transitions214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSM_Transition__transitions214", None)
        self.__transitions214 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State215"):
                opp_val = getattr(old_value, "State215", None)
                if opp_val == self:
                    setattr(old_value, "State215", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State215"):
                opp_val = getattr(value, "State215", None)
                setattr(value, "State215", self)

    @property
    def HALL_FSM_Transition221(self):
        return self.__HALL_FSM_Transition221

    @HALL_FSM_Transition221.setter
    def HALL_FSM_Transition221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSM_Transition__HALL_FSM_Transition221", None)
        self.__HALL_FSM_Transition221 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMInstructions_PosCondition"):
                opp_val = getattr(old_value, "FSMInstructions_PosCondition", None)
                if opp_val == self:
                    setattr(old_value, "FSMInstructions_PosCondition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMInstructions_PosCondition"):
                opp_val = getattr(value, "FSMInstructions_PosCondition", None)
                setattr(value, "FSMInstructions_PosCondition", self)

    @property
    def HALL_FSM_Transition(self):
        return self.__HALL_FSM_Transition

    @HALL_FSM_Transition.setter
    def HALL_FSM_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSM_Transition__HALL_FSM_Transition", None)
        self.__HALL_FSM_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State217"):
                opp_val = getattr(old_value, "State217", None)
                if opp_val == self:
                    setattr(old_value, "State217", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State217"):
                opp_val = getattr(value, "State217", None)
                setattr(value, "State217", self)

    @property
    def HALL_FSM_Transition225(self):
        return self.__HALL_FSM_Transition225

    @HALL_FSM_Transition225.setter
    def HALL_FSM_Transition225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSM_Transition__HALL_FSM_Transition225", None)
        self.__HALL_FSM_Transition225 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Trigger_Trigger"):
                opp_val = getattr(old_value, "Trigger_Trigger", None)
                if opp_val == self:
                    setattr(old_value, "Trigger_Trigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Trigger_Trigger"):
                opp_val = getattr(value, "Trigger_Trigger", None)
                setattr(value, "Trigger_Trigger", self)

    @property
    def HALL_FSM_Transition219(self):
        return self.__HALL_FSM_Transition219

    @HALL_FSM_Transition219.setter
    def HALL_FSM_Transition219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSM_Transition__HALL_FSM_Transition219", None)
        self.__HALL_FSM_Transition219 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMConditions_PreCondition"):
                opp_val = getattr(old_value, "FSMConditions_PreCondition", None)
                if opp_val == self:
                    setattr(old_value, "FSMConditions_PreCondition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMConditions_PreCondition"):
                opp_val = getattr(value, "FSMConditions_PreCondition", None)
                setattr(value, "FSMConditions_PreCondition", self)

class HALL_Actions_GetMessageParameter(ActionMessageExpression):

    def __init__(self, field: str):
        self.field = field
        
        pass
    @property
    def field(self):
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field


class HALL_Actions_GetMessageData(ActionMessageExpression):

    def __init__(self, field: str):
        self.field = field
        
        pass
    @property
    def field(self):
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field


class HALL_Actions_DomainPropertyGet(ActionMessageExpression):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class HALL_Actions_Enable(ActionMessageExpression):

    pass
class HALL_Actions_DomainPropertySet(ActionMessageExpression):

    def __init__(self, name: str, HALL_Actions_DomainPropertySet: "Actions_ActionMessageExpression" = None):
        self.name = name
        self.HALL_Actions_DomainPropertySet = HALL_Actions_DomainPropertySet
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def HALL_Actions_DomainPropertySet(self):
        return self.__HALL_Actions_DomainPropertySet

    @HALL_Actions_DomainPropertySet.setter
    def HALL_Actions_DomainPropertySet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Actions_DomainPropertySet__HALL_Actions_DomainPropertySet", None)
        self.__HALL_Actions_DomainPropertySet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Actions_ActionMessageExpression201"):
                opp_val = getattr(old_value, "Actions_ActionMessageExpression201", None)
                if opp_val == self:
                    setattr(old_value, "Actions_ActionMessageExpression201", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Actions_ActionMessageExpression201"):
                opp_val = getattr(value, "Actions_ActionMessageExpression201", None)
                setattr(value, "Actions_ActionMessageExpression201", self)

class Actions_HALL_Component:

    pass
class HALL_Actions_GetData(ActionMessageExpression):

    pass
class HALL_Actions_UnaryOperator(ActionMessageExpression):

    def __init__(self, operatorname: str, HALL_Actions_UnaryOperator: "Actions_ActionMessageExpression" = None):
        self.operatorname = operatorname
        self.HALL_Actions_UnaryOperator = HALL_Actions_UnaryOperator
        
        pass
    @property
    def operatorname(self):
        return self.__operatorname

    @operatorname.setter
    def operatorname(self, operatorname: str):
        self.__operatorname = operatorname


    @property
    def HALL_Actions_UnaryOperator(self):
        return self.__HALL_Actions_UnaryOperator

    @HALL_Actions_UnaryOperator.setter
    def HALL_Actions_UnaryOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Actions_UnaryOperator__HALL_Actions_UnaryOperator", None)
        self.__HALL_Actions_UnaryOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Actions_ActionMessageExpression198"):
                opp_val = getattr(old_value, "Actions_ActionMessageExpression198", None)
                if opp_val == self:
                    setattr(old_value, "Actions_ActionMessageExpression198", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Actions_ActionMessageExpression198"):
                opp_val = getattr(value, "Actions_ActionMessageExpression198", None)
                setattr(value, "Actions_ActionMessageExpression198", self)

class HALL_Actions_MessageInvocation(ActionMessageExpression):

    def __init__(self, isTopDown: bool, HALL_Actions_MessageInvocation: "MessageDefinition" = None, HALL_Actions_MessageInvocation195: set["Actions_ActionMessageExpression"] = None):
        self.isTopDown = isTopDown
        self.HALL_Actions_MessageInvocation = HALL_Actions_MessageInvocation
        self.HALL_Actions_MessageInvocation195 = HALL_Actions_MessageInvocation195 if HALL_Actions_MessageInvocation195 is not None else set()
        
        pass
    @property
    def isTopDown(self):
        return self.__isTopDown

    @isTopDown.setter
    def isTopDown(self, isTopDown: bool):
        self.__isTopDown = isTopDown


    @property
    def HALL_Actions_MessageInvocation195(self):
        return self.__HALL_Actions_MessageInvocation195

    @HALL_Actions_MessageInvocation195.setter
    def HALL_Actions_MessageInvocation195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Actions_MessageInvocation__HALL_Actions_MessageInvocation195", None)
        self.__HALL_Actions_MessageInvocation195 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Actions_ActionMessageExpression196"):
                    opp_val = getattr(item, "Actions_ActionMessageExpression196", None)
                    
                    if opp_val == self:
                        setattr(item, "Actions_ActionMessageExpression196", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Actions_ActionMessageExpression196"):
                    opp_val = getattr(item, "Actions_ActionMessageExpression196", None)
                    
                    setattr(item, "Actions_ActionMessageExpression196", self)
                    

    @property
    def HALL_Actions_MessageInvocation(self):
        return self.__HALL_Actions_MessageInvocation

    @HALL_Actions_MessageInvocation.setter
    def HALL_Actions_MessageInvocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Actions_MessageInvocation__HALL_Actions_MessageInvocation", None)
        self.__HALL_Actions_MessageInvocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MessageDefinition193"):
                opp_val = getattr(old_value, "MessageDefinition193", None)
                if opp_val == self:
                    setattr(old_value, "MessageDefinition193", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MessageDefinition193"):
                opp_val = getattr(value, "MessageDefinition193", None)
                setattr(value, "MessageDefinition193", self)

class HALL_Actions_VarRef(ActionMessageExpression):

    pass
class HALL_Actions_ActionMessageExpression(ABC):

    pass
class Actions_ActionMessageExpression:

    pass
class HALL_Actions_ActionMessage:

    pass
class Conditions_Let:

    pass
class Conditions_HALL_Data:

    pass
class Conditions_HALL_Component:

    pass
class PreConditionMessageExpression:

    pass
class HALL_Conditions_GetState(PreConditionMessageExpression):

    pass
class HALL_Conditions_Let(PreConditionMessageExpression):

    def __init__(self, name: str, HALL_Conditions_Let: "Type" = None, HALL_Conditions_Let164: "Conditions_PreConditionMessageExpression" = None, HALL_Conditions_Let167: "Conditions_PreConditionMessageExpression" = None):
        self.name = name
        self.HALL_Conditions_Let = HALL_Conditions_Let
        self.HALL_Conditions_Let164 = HALL_Conditions_Let164
        self.HALL_Conditions_Let167 = HALL_Conditions_Let167
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def HALL_Conditions_Let164(self):
        return self.__HALL_Conditions_Let164

    @HALL_Conditions_Let164.setter
    def HALL_Conditions_Let164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Conditions_Let__HALL_Conditions_Let164", None)
        self.__HALL_Conditions_Let164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Conditions_PreConditionMessageExpression165"):
                opp_val = getattr(old_value, "Conditions_PreConditionMessageExpression165", None)
                if opp_val == self:
                    setattr(old_value, "Conditions_PreConditionMessageExpression165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Conditions_PreConditionMessageExpression165"):
                opp_val = getattr(value, "Conditions_PreConditionMessageExpression165", None)
                setattr(value, "Conditions_PreConditionMessageExpression165", self)

    @property
    def HALL_Conditions_Let(self):
        return self.__HALL_Conditions_Let

    @HALL_Conditions_Let.setter
    def HALL_Conditions_Let(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Conditions_Let__HALL_Conditions_Let", None)
        self.__HALL_Conditions_Let = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type162"):
                opp_val = getattr(old_value, "Type162", None)
                if opp_val == self:
                    setattr(old_value, "Type162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type162"):
                opp_val = getattr(value, "Type162", None)
                setattr(value, "Type162", self)

    @property
    def HALL_Conditions_Let167(self):
        return self.__HALL_Conditions_Let167

    @HALL_Conditions_Let167.setter
    def HALL_Conditions_Let167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Conditions_Let__HALL_Conditions_Let167", None)
        self.__HALL_Conditions_Let167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Conditions_PreConditionMessageExpression168"):
                opp_val = getattr(old_value, "Conditions_PreConditionMessageExpression168", None)
                if opp_val == self:
                    setattr(old_value, "Conditions_PreConditionMessageExpression168", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Conditions_PreConditionMessageExpression168"):
                opp_val = getattr(value, "Conditions_PreConditionMessageExpression168", None)
                setattr(value, "Conditions_PreConditionMessageExpression168", self)

class HALL_Conditions_GetData(PreConditionMessageExpression):

    pass
class HALL_Conditions_GetMessageParameter(PreConditionMessageExpression):

    def __init__(self, field: str):
        self.field = field
        
        pass
    @property
    def field(self):
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field


class HALL_Conditions_UnaryOperator(PreConditionMessageExpression):

    def __init__(self, operatorname: str, HALL_Conditions_UnaryOperator: "Conditions_PreConditionMessageExpression" = None):
        self.operatorname = operatorname
        self.HALL_Conditions_UnaryOperator = HALL_Conditions_UnaryOperator
        
        pass
    @property
    def operatorname(self):
        return self.__operatorname

    @operatorname.setter
    def operatorname(self, operatorname: str):
        self.__operatorname = operatorname


    @property
    def HALL_Conditions_UnaryOperator(self):
        return self.__HALL_Conditions_UnaryOperator

    @HALL_Conditions_UnaryOperator.setter
    def HALL_Conditions_UnaryOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Conditions_UnaryOperator__HALL_Conditions_UnaryOperator", None)
        self.__HALL_Conditions_UnaryOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Conditions_PreConditionMessageExpression170"):
                opp_val = getattr(old_value, "Conditions_PreConditionMessageExpression170", None)
                if opp_val == self:
                    setattr(old_value, "Conditions_PreConditionMessageExpression170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Conditions_PreConditionMessageExpression170"):
                opp_val = getattr(value, "Conditions_PreConditionMessageExpression170", None)
                setattr(value, "Conditions_PreConditionMessageExpression170", self)

class HALL_Conditions_VarRef(PreConditionMessageExpression):

    pass
class HALL_Conditions_GetMessageData(PreConditionMessageExpression):

    def __init__(self, field: str):
        self.field = field
        
        pass
    @property
    def field(self):
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field


class HALL_Conditions_DomainPropertyGet(PreConditionMessageExpression):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class HALL_Conditions_BinaryOperator(PreConditionMessageExpression):

    def __init__(self, operatorname: str, HALL_Conditions_BinaryOperator: "Conditions_PreConditionMessageExpression" = None, HALL_Conditions_BinaryOperator174: "Conditions_PreConditionMessageExpression" = None):
        self.operatorname = operatorname
        self.HALL_Conditions_BinaryOperator = HALL_Conditions_BinaryOperator
        self.HALL_Conditions_BinaryOperator174 = HALL_Conditions_BinaryOperator174
        
        pass
    @property
    def operatorname(self):
        return self.__operatorname

    @operatorname.setter
    def operatorname(self, operatorname: str):
        self.__operatorname = operatorname


    @property
    def HALL_Conditions_BinaryOperator(self):
        return self.__HALL_Conditions_BinaryOperator

    @HALL_Conditions_BinaryOperator.setter
    def HALL_Conditions_BinaryOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Conditions_BinaryOperator__HALL_Conditions_BinaryOperator", None)
        self.__HALL_Conditions_BinaryOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Conditions_PreConditionMessageExpression172"):
                opp_val = getattr(old_value, "Conditions_PreConditionMessageExpression172", None)
                if opp_val == self:
                    setattr(old_value, "Conditions_PreConditionMessageExpression172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Conditions_PreConditionMessageExpression172"):
                opp_val = getattr(value, "Conditions_PreConditionMessageExpression172", None)
                setattr(value, "Conditions_PreConditionMessageExpression172", self)

    @property
    def HALL_Conditions_BinaryOperator174(self):
        return self.__HALL_Conditions_BinaryOperator174

    @HALL_Conditions_BinaryOperator174.setter
    def HALL_Conditions_BinaryOperator174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Conditions_BinaryOperator__HALL_Conditions_BinaryOperator174", None)
        self.__HALL_Conditions_BinaryOperator174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Conditions_PreConditionMessageExpression175"):
                opp_val = getattr(old_value, "Conditions_PreConditionMessageExpression175", None)
                if opp_val == self:
                    setattr(old_value, "Conditions_PreConditionMessageExpression175", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Conditions_PreConditionMessageExpression175"):
                opp_val = getattr(value, "Conditions_PreConditionMessageExpression175", None)
                setattr(value, "Conditions_PreConditionMessageExpression175", self)

class HALL_Conditions_Literal(PreConditionMessageExpression):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class HALL_Conditions_PreConditionMessageExpression(ABC):

    pass
class Conditions_PreConditionMessageExpression:

    pass
class HALL_Conditions_PreConditionMessage:

    pass
class Instructions_Let:

    pass
class Instructions_HALL_Component:

    pass
class Instructions_HALL_Data:

    pass
class State:

    pass
class HALL_FSM_RegularState(State):

    pass
class HALL_FSM_InitialState(State):

    pass
class RegularMessageState:

    pass
class HALL_Messages_MessageHandler:

    pass
class Messages_HALL_Data:

    pass
class PosConditionMessageExpression:

    pass
class HALL_Instructions_VarRef(PosConditionMessageExpression):

    pass
class HALL_Instructions_DomainPropertyGet(PosConditionMessageExpression):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class HALL_Instructions_SetMessageParameter(PosConditionMessageExpression):

    def __init__(self, field: str, HALL_Instructions_SetMessageParameter: "Instructions_PosConditionMessageExpression" = None):
        self.field = field
        self.HALL_Instructions_SetMessageParameter = HALL_Instructions_SetMessageParameter
        
        pass
    @property
    def field(self):
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field


    @property
    def HALL_Instructions_SetMessageParameter(self):
        return self.__HALL_Instructions_SetMessageParameter

    @HALL_Instructions_SetMessageParameter.setter
    def HALL_Instructions_SetMessageParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Instructions_SetMessageParameter__HALL_Instructions_SetMessageParameter", None)
        self.__HALL_Instructions_SetMessageParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Instructions_PosConditionMessageExpression146"):
                opp_val = getattr(old_value, "Instructions_PosConditionMessageExpression146", None)
                if opp_val == self:
                    setattr(old_value, "Instructions_PosConditionMessageExpression146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instructions_PosConditionMessageExpression146"):
                opp_val = getattr(value, "Instructions_PosConditionMessageExpression146", None)
                setattr(value, "Instructions_PosConditionMessageExpression146", self)

class HALL_Instructions_GetData(PosConditionMessageExpression):

    pass
class HALL_Instructions_GetMessageData(PosConditionMessageExpression):

    def __init__(self, field: str):
        self.field = field
        
        pass
    @property
    def field(self):
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field


class HALL_Instructions_BinaryOperator(PosConditionMessageExpression):

    def __init__(self, operatorname: str, HALL_Instructions_BinaryOperator: "Instructions_PosConditionMessageExpression" = None, HALL_Instructions_BinaryOperator131: "Instructions_PosConditionMessageExpression" = None):
        self.operatorname = operatorname
        self.HALL_Instructions_BinaryOperator = HALL_Instructions_BinaryOperator
        self.HALL_Instructions_BinaryOperator131 = HALL_Instructions_BinaryOperator131
        
        pass
    @property
    def operatorname(self):
        return self.__operatorname

    @operatorname.setter
    def operatorname(self, operatorname: str):
        self.__operatorname = operatorname


    @property
    def HALL_Instructions_BinaryOperator131(self):
        return self.__HALL_Instructions_BinaryOperator131

    @HALL_Instructions_BinaryOperator131.setter
    def HALL_Instructions_BinaryOperator131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Instructions_BinaryOperator__HALL_Instructions_BinaryOperator131", None)
        self.__HALL_Instructions_BinaryOperator131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Instructions_PosConditionMessageExpression132"):
                opp_val = getattr(old_value, "Instructions_PosConditionMessageExpression132", None)
                if opp_val == self:
                    setattr(old_value, "Instructions_PosConditionMessageExpression132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instructions_PosConditionMessageExpression132"):
                opp_val = getattr(value, "Instructions_PosConditionMessageExpression132", None)
                setattr(value, "Instructions_PosConditionMessageExpression132", self)

    @property
    def HALL_Instructions_BinaryOperator(self):
        return self.__HALL_Instructions_BinaryOperator

    @HALL_Instructions_BinaryOperator.setter
    def HALL_Instructions_BinaryOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Instructions_BinaryOperator__HALL_Instructions_BinaryOperator", None)
        self.__HALL_Instructions_BinaryOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Instructions_PosConditionMessageExpression129"):
                opp_val = getattr(old_value, "Instructions_PosConditionMessageExpression129", None)
                if opp_val == self:
                    setattr(old_value, "Instructions_PosConditionMessageExpression129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instructions_PosConditionMessageExpression129"):
                opp_val = getattr(value, "Instructions_PosConditionMessageExpression129", None)
                setattr(value, "Instructions_PosConditionMessageExpression129", self)

class HALL_Instructions_SetState(PosConditionMessageExpression):

    pass
class HALL_Instructions_Let(PosConditionMessageExpression):

    def __init__(self, name: str, HALL_Instructions_Let: "Instructions_PosConditionMessageExpression" = None, HALL_Instructions_Let153: "Type" = None, HALL_Instructions_Let150: "Instructions_PosConditionMessageExpression" = None):
        self.name = name
        self.HALL_Instructions_Let = HALL_Instructions_Let
        self.HALL_Instructions_Let153 = HALL_Instructions_Let153
        self.HALL_Instructions_Let150 = HALL_Instructions_Let150
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def HALL_Instructions_Let153(self):
        return self.__HALL_Instructions_Let153

    @HALL_Instructions_Let153.setter
    def HALL_Instructions_Let153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Instructions_Let__HALL_Instructions_Let153", None)
        self.__HALL_Instructions_Let153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type154"):
                opp_val = getattr(old_value, "Type154", None)
                if opp_val == self:
                    setattr(old_value, "Type154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type154"):
                opp_val = getattr(value, "Type154", None)
                setattr(value, "Type154", self)

    @property
    def HALL_Instructions_Let150(self):
        return self.__HALL_Instructions_Let150

    @HALL_Instructions_Let150.setter
    def HALL_Instructions_Let150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Instructions_Let__HALL_Instructions_Let150", None)
        self.__HALL_Instructions_Let150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Instructions_PosConditionMessageExpression151"):
                opp_val = getattr(old_value, "Instructions_PosConditionMessageExpression151", None)
                if opp_val == self:
                    setattr(old_value, "Instructions_PosConditionMessageExpression151", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instructions_PosConditionMessageExpression151"):
                opp_val = getattr(value, "Instructions_PosConditionMessageExpression151", None)
                setattr(value, "Instructions_PosConditionMessageExpression151", self)

    @property
    def HALL_Instructions_Let(self):
        return self.__HALL_Instructions_Let

    @HALL_Instructions_Let.setter
    def HALL_Instructions_Let(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Instructions_Let__HALL_Instructions_Let", None)
        self.__HALL_Instructions_Let = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Instructions_PosConditionMessageExpression148"):
                opp_val = getattr(old_value, "Instructions_PosConditionMessageExpression148", None)
                if opp_val == self:
                    setattr(old_value, "Instructions_PosConditionMessageExpression148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instructions_PosConditionMessageExpression148"):
                opp_val = getattr(value, "Instructions_PosConditionMessageExpression148", None)
                setattr(value, "Instructions_PosConditionMessageExpression148", self)

class HALL_Instructions_SetMessageData(PosConditionMessageExpression):

    def __init__(self, field: str, HALL_Instructions_SetMessageData: "Instructions_PosConditionMessageExpression" = None):
        self.field = field
        self.HALL_Instructions_SetMessageData = HALL_Instructions_SetMessageData
        
        pass
    @property
    def field(self):
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field


    @property
    def HALL_Instructions_SetMessageData(self):
        return self.__HALL_Instructions_SetMessageData

    @HALL_Instructions_SetMessageData.setter
    def HALL_Instructions_SetMessageData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Instructions_SetMessageData__HALL_Instructions_SetMessageData", None)
        self.__HALL_Instructions_SetMessageData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Instructions_PosConditionMessageExpression144"):
                opp_val = getattr(old_value, "Instructions_PosConditionMessageExpression144", None)
                if opp_val == self:
                    setattr(old_value, "Instructions_PosConditionMessageExpression144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instructions_PosConditionMessageExpression144"):
                opp_val = getattr(value, "Instructions_PosConditionMessageExpression144", None)
                setattr(value, "Instructions_PosConditionMessageExpression144", self)

class HALL_Instructions_GetMessageParameter(PosConditionMessageExpression):

    def __init__(self, field: str):
        self.field = field
        
        pass
    @property
    def field(self):
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field


class HALL_Instructions_GetState(PosConditionMessageExpression):

    pass
class HALL_Instructions_SetTopDown(PosConditionMessageExpression):

    pass
class HALL_Instructions_UnaryOperator(PosConditionMessageExpression):

    def __init__(self, operatorname: str, HALL_Instructions_UnaryOperator: "Instructions_PosConditionMessageExpression" = None):
        self.operatorname = operatorname
        self.HALL_Instructions_UnaryOperator = HALL_Instructions_UnaryOperator
        
        pass
    @property
    def operatorname(self):
        return self.__operatorname

    @operatorname.setter
    def operatorname(self, operatorname: str):
        self.__operatorname = operatorname


    @property
    def HALL_Instructions_UnaryOperator(self):
        return self.__HALL_Instructions_UnaryOperator

    @HALL_Instructions_UnaryOperator.setter
    def HALL_Instructions_UnaryOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Instructions_UnaryOperator__HALL_Instructions_UnaryOperator", None)
        self.__HALL_Instructions_UnaryOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Instructions_PosConditionMessageExpression134"):
                opp_val = getattr(old_value, "Instructions_PosConditionMessageExpression134", None)
                if opp_val == self:
                    setattr(old_value, "Instructions_PosConditionMessageExpression134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instructions_PosConditionMessageExpression134"):
                opp_val = getattr(value, "Instructions_PosConditionMessageExpression134", None)
                setattr(value, "Instructions_PosConditionMessageExpression134", self)

class HALL_Instructions_SetData(PosConditionMessageExpression):

    pass
class HALL_Instructions_Literal(PosConditionMessageExpression):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class HALL_Instructions_PosConditionMessageExpression(ABC):

    pass
class Instructions_PosConditionMessageExpression:

    pass
class HALL_Instructions_PosConditionMessage:

    pass
class MessageTransition:

    pass
class HALL_Messages_MessageState:

    def __init__(self, name: str, isEnd: bool, isContinue: bool, isActive: bool, transitionsInvMessageState: set["MessageTransition"] = None):
        self.name = name
        self.isEnd = isEnd
        self.isContinue = isContinue
        self.isActive = isActive
        self.transitionsInvMessageState = transitionsInvMessageState if transitionsInvMessageState is not None else set()
        
        pass
    @property
    def isEnd(self):
        return self.__isEnd

    @isEnd.setter
    def isEnd(self, isEnd: bool):
        self.__isEnd = isEnd


    @property
    def isActive(self):
        return self.__isActive

    @isActive.setter
    def isActive(self, isActive: bool):
        self.__isActive = isActive


    @property
    def isContinue(self):
        return self.__isContinue

    @isContinue.setter
    def isContinue(self, isContinue: bool):
        self.__isContinue = isContinue


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def transitionsInvMessageState(self):
        return self.__transitionsInvMessageState

    @transitionsInvMessageState.setter
    def transitionsInvMessageState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Messages_MessageState__transitionsInvMessageState", None)
        self.__transitionsInvMessageState = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MessageTransition"):
                    opp_val = getattr(item, "MessageTransition", None)
                    
                    if opp_val == self:
                        setattr(item, "MessageTransition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MessageTransition"):
                    opp_val = getattr(item, "MessageTransition", None)
                    
                    setattr(item, "MessageTransition", self)
                    

class Messages_HALL_Component:

    pass
class InitialMessageState:

    pass
class Point:

    pass
class HALL_Geometry_Point3D(Point):

    def __init__(self, zCoord: int, point3d: "Face" = None):
        self.zCoord = zCoord
        self.point3d = point3d
        
        pass
    @property
    def zCoord(self):
        return self.__zCoord

    @zCoord.setter
    def zCoord(self, zCoord: int):
        self.__zCoord = zCoord


    @property
    def point3d(self):
        return self.__point3d

    @point3d.setter
    def point3d(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Geometry_Point3D__point3d", None)
        self.__point3d = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Face100"):
                opp_val = getattr(old_value, "Face100", None)
                if opp_val == self:
                    setattr(old_value, "Face100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Face100"):
                opp_val = getattr(value, "Face100", None)
                setattr(value, "Face100", self)

class GeometryData3D:

    pass
class Point3D:

    pass
class HALL_Geometry_Face:

    def __init__(self, labelText: str, point2dInv97: set["Point3D"] = None, face: "GeometryData3D" = None):
        self.labelText = labelText
        self.point2dInv97 = point2dInv97 if point2dInv97 is not None else set()
        self.face = face
        
        pass
    @property
    def labelText(self):
        return self.__labelText

    @labelText.setter
    def labelText(self, labelText: str):
        self.__labelText = labelText


    @property
    def point2dInv97(self):
        return self.__point2dInv97

    @point2dInv97.setter
    def point2dInv97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Geometry_Face__point2dInv97", None)
        self.__point2dInv97 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Point3D"):
                    opp_val = getattr(item, "Point3D", None)
                    
                    if opp_val == self:
                        setattr(item, "Point3D", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Point3D"):
                    opp_val = getattr(item, "Point3D", None)
                    
                    setattr(item, "Point3D", self)
                    

    @property
    def face(self):
        return self.__face

    @face.setter
    def face(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Geometry_Face__face", None)
        self.__face = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GeometryData3D"):
                opp_val = getattr(old_value, "GeometryData3D", None)
                if opp_val == self:
                    setattr(old_value, "GeometryData3D", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GeometryData3D"):
                opp_val = getattr(value, "GeometryData3D", None)
                setattr(value, "GeometryData3D", self)

class Messages_HALL_Parameter:

    pass
class Messages_HALL_Model:

    pass
class HALL_Messages_MessageDefinition:

    def __init__(self, name: str, messageDefinition: "Messages_HALL_Model" = None, parameterInv: set["Messages_HALL_Parameter"] = None, dataInvMessageDefinition: set["Messages_HALL_Data"] = None):
        self.name = name
        self.messageDefinition = messageDefinition
        self.parameterInv = parameterInv if parameterInv is not None else set()
        self.dataInvMessageDefinition = dataInvMessageDefinition if dataInvMessageDefinition is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def parameterInv(self):
        return self.__parameterInv

    @parameterInv.setter
    def parameterInv(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Messages_MessageDefinition__parameterInv", None)
        self.__parameterInv = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    setattr(item, "Parameter", self)
                    

    @property
    def dataInvMessageDefinition(self):
        return self.__dataInvMessageDefinition

    @dataInvMessageDefinition.setter
    def dataInvMessageDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Messages_MessageDefinition__dataInvMessageDefinition", None)
        self.__dataInvMessageDefinition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Data117"):
                    opp_val = getattr(item, "Data117", None)
                    
                    if opp_val == self:
                        setattr(item, "Data117", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Data117"):
                    opp_val = getattr(item, "Data117", None)
                    
                    setattr(item, "Data117", self)
                    

    @property
    def messageDefinition(self):
        return self.__messageDefinition

    @messageDefinition.setter
    def messageDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Messages_MessageDefinition__messageDefinition", None)
        self.__messageDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model114"):
                opp_val = getattr(old_value, "Model114", None)
                if opp_val == self:
                    setattr(old_value, "Model114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model114"):
                opp_val = getattr(value, "Model114", None)
                setattr(value, "Model114", self)

class Actions_ActionMessage:

    pass
class Instructions_PosConditionMessage:

    pass
class Conditions_PreConditionMessage:

    pass
class MessageState:

    pass
class HALL_Messages_RegularMessageState(MessageState):

    pass
class HALL_Messages_InitialMessageState(MessageState):

    pass
class HALL_Messages_MessageTransition:

    def __init__(self, name: str, transitions: "MessageState" = None, HALL_Messages_MessageTransition: "MessageState" = None, HALL_Messages_MessageTransition106: "Conditions_PreConditionMessage" = None, HALL_Messages_MessageTransition108: "Instructions_PosConditionMessage" = None, HALL_Messages_MessageTransition110: "Actions_ActionMessage" = None):
        self.name = name
        self.transitions = transitions
        self.HALL_Messages_MessageTransition = HALL_Messages_MessageTransition
        self.HALL_Messages_MessageTransition106 = HALL_Messages_MessageTransition106
        self.HALL_Messages_MessageTransition108 = HALL_Messages_MessageTransition108
        self.HALL_Messages_MessageTransition110 = HALL_Messages_MessageTransition110
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def HALL_Messages_MessageTransition106(self):
        return self.__HALL_Messages_MessageTransition106

    @HALL_Messages_MessageTransition106.setter
    def HALL_Messages_MessageTransition106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Messages_MessageTransition__HALL_Messages_MessageTransition106", None)
        self.__HALL_Messages_MessageTransition106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Conditions_PreConditionMessage"):
                opp_val = getattr(old_value, "Conditions_PreConditionMessage", None)
                if opp_val == self:
                    setattr(old_value, "Conditions_PreConditionMessage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Conditions_PreConditionMessage"):
                opp_val = getattr(value, "Conditions_PreConditionMessage", None)
                setattr(value, "Conditions_PreConditionMessage", self)

    @property
    def HALL_Messages_MessageTransition110(self):
        return self.__HALL_Messages_MessageTransition110

    @HALL_Messages_MessageTransition110.setter
    def HALL_Messages_MessageTransition110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Messages_MessageTransition__HALL_Messages_MessageTransition110", None)
        self.__HALL_Messages_MessageTransition110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Actions_ActionMessage"):
                opp_val = getattr(old_value, "Actions_ActionMessage", None)
                if opp_val == self:
                    setattr(old_value, "Actions_ActionMessage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Actions_ActionMessage"):
                opp_val = getattr(value, "Actions_ActionMessage", None)
                setattr(value, "Actions_ActionMessage", self)

    @property
    def HALL_Messages_MessageTransition108(self):
        return self.__HALL_Messages_MessageTransition108

    @HALL_Messages_MessageTransition108.setter
    def HALL_Messages_MessageTransition108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Messages_MessageTransition__HALL_Messages_MessageTransition108", None)
        self.__HALL_Messages_MessageTransition108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Instructions_PosConditionMessage"):
                opp_val = getattr(old_value, "Instructions_PosConditionMessage", None)
                if opp_val == self:
                    setattr(old_value, "Instructions_PosConditionMessage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instructions_PosConditionMessage"):
                opp_val = getattr(value, "Instructions_PosConditionMessage", None)
                setattr(value, "Instructions_PosConditionMessage", self)

    @property
    def HALL_Messages_MessageTransition(self):
        return self.__HALL_Messages_MessageTransition

    @HALL_Messages_MessageTransition.setter
    def HALL_Messages_MessageTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Messages_MessageTransition__HALL_Messages_MessageTransition", None)
        self.__HALL_Messages_MessageTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MessageState104"):
                opp_val = getattr(old_value, "MessageState104", None)
                if opp_val == self:
                    setattr(old_value, "MessageState104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MessageState104"):
                opp_val = getattr(value, "MessageState104", None)
                setattr(value, "MessageState104", self)

    @property
    def transitions(self):
        return self.__transitions

    @transitions.setter
    def transitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Messages_MessageTransition__transitions", None)
        self.__transitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MessageState"):
                opp_val = getattr(old_value, "MessageState", None)
                if opp_val == self:
                    setattr(old_value, "MessageState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MessageState"):
                opp_val = getattr(value, "MessageState", None)
                setattr(value, "MessageState", self)

class HALL_Geometry_Point:

    def __init__(self, xCoord: int, yCoord: int):
        self.xCoord = xCoord
        self.yCoord = yCoord
        
        pass
    @property
    def yCoord(self):
        return self.__yCoord

    @yCoord.setter
    def yCoord(self, yCoord: int):
        self.__yCoord = yCoord


    @property
    def xCoord(self):
        return self.__xCoord

    @xCoord.setter
    def xCoord(self, xCoord: int):
        self.__xCoord = xCoord


class GeometryData2D:

    pass
class HALL_Geometry_Point2D(Point):

    pass
class HALL_Geometry_AlphaTransparency:

    def __init__(self, value: int, alphaTransparency: "ColorState" = None):
        self.value = value
        self.alphaTransparency = alphaTransparency
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


    @property
    def alphaTransparency(self):
        return self.__alphaTransparency

    @alphaTransparency.setter
    def alphaTransparency(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Geometry_AlphaTransparency__alphaTransparency", None)
        self.__alphaTransparency = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColorState80"):
                opp_val = getattr(old_value, "ColorState80", None)
                if opp_val == self:
                    setattr(old_value, "ColorState80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorState80"):
                opp_val = getattr(value, "ColorState80", None)
                setattr(value, "ColorState80", self)

class AlphaTransparency:

    pass
class Point2D:

    pass
class Face:

    pass
class HALL_Geometry_GeometryData(ABC):

    pass
class Geometry_HALL_VisualObject:

    pass
class NormalColors:

    pass
class DisabledColors:

    pass
class SelectedColors:

    pass
class HALL_Geometry_ColorData:

    pass
class HALL_Parameter:

    def __init__(self, name: str, HALL_Parameter: "Type" = None, parameter: "MessageDefinition" = None):
        self.name = name
        self.HALL_Parameter = HALL_Parameter
        self.parameter = parameter
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def HALL_Parameter(self):
        return self.__HALL_Parameter

    @HALL_Parameter.setter
    def HALL_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Parameter__HALL_Parameter", None)
        self.__HALL_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type52"):
                opp_val = getattr(old_value, "Type52", None)
                if opp_val == self:
                    setattr(old_value, "Type52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type52"):
                opp_val = getattr(value, "Type52", None)
                setattr(value, "Type52", self)

    @property
    def parameter(self):
        return self.__parameter

    @parameter.setter
    def parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Parameter__parameter", None)
        self.__parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MessageDefinition54"):
                opp_val = getattr(old_value, "MessageDefinition54", None)
                if opp_val == self:
                    setattr(old_value, "MessageDefinition54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MessageDefinition54"):
                opp_val = getattr(value, "MessageDefinition54", None)
                setattr(value, "MessageDefinition54", self)

class HALL_Geometry_ColorState(ABC):

    pass
class Color:

    pass
class HALL_Geometry_RGBColor:

    def __init__(self, redValue: int, greenValue: int, blueValue: int, ambianceColor: "Color" = None, difuseColor: "Color" = None, specularColor: "Color" = None):
        self.redValue = redValue
        self.greenValue = greenValue
        self.blueValue = blueValue
        self.ambianceColor = ambianceColor
        self.difuseColor = difuseColor
        self.specularColor = specularColor
        
        pass
    @property
    def blueValue(self):
        return self.__blueValue

    @blueValue.setter
    def blueValue(self, blueValue: int):
        self.__blueValue = blueValue


    @property
    def redValue(self):
        return self.__redValue

    @redValue.setter
    def redValue(self, redValue: int):
        self.__redValue = redValue


    @property
    def greenValue(self):
        return self.__greenValue

    @greenValue.setter
    def greenValue(self, greenValue: int):
        self.__greenValue = greenValue


    @property
    def ambianceColor(self):
        return self.__ambianceColor

    @ambianceColor.setter
    def ambianceColor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Geometry_RGBColor__ambianceColor", None)
        self.__ambianceColor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Color"):
                opp_val = getattr(old_value, "Color", None)
                if opp_val == self:
                    setattr(old_value, "Color", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Color"):
                opp_val = getattr(value, "Color", None)
                setattr(value, "Color", self)

    @property
    def difuseColor(self):
        return self.__difuseColor

    @difuseColor.setter
    def difuseColor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Geometry_RGBColor__difuseColor", None)
        self.__difuseColor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Color71"):
                opp_val = getattr(old_value, "Color71", None)
                if opp_val == self:
                    setattr(old_value, "Color71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Color71"):
                opp_val = getattr(value, "Color71", None)
                setattr(value, "Color71", self)

    @property
    def specularColor(self):
        return self.__specularColor

    @specularColor.setter
    def specularColor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Geometry_RGBColor__specularColor", None)
        self.__specularColor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Color73"):
                opp_val = getattr(old_value, "Color73", None)
                if opp_val == self:
                    setattr(old_value, "Color73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Color73"):
                opp_val = getattr(value, "Color73", None)
                setattr(value, "Color73", self)

class ColorState:

    pass
class HALL_Geometry_DisabledColors(ColorState):

    pass
class HALL_Geometry_NormalColors(ColorState):

    pass
class HALL_Geometry_SelectedColors(ColorState):

    pass
class RGBColor:

    pass
class HALL_Geometry_Color:

    pass
class Type:

    pass
class HALL_Types_Set(Type):

    pass
class HALL_Types_SimpleType(Type):

    pass
class MessageDefinition:

    pass
class HALL_Goal:

    def __init__(self, condition: str, Goal: "HALL_TaskObject" = None, goal: "HALL_TaskObject" = None):
        self.condition = condition
        self.Goal = Goal
        self.goal = goal
        
        pass
    @property
    def condition(self):
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition


    @property
    def Goal(self):
        return self.__Goal

    @Goal.setter
    def Goal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Goal__Goal", None)
        self.__Goal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "goalInv"):
                opp_val = getattr(old_value, "goalInv", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "goalInv"):
                opp_val = getattr(value, "goalInv", None)
                if opp_val is None:
                    setattr(value, "goalInv", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def goal(self):
        return self.__goal

    @goal.setter
    def goal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Goal__goal", None)
        self.__goal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TaskObject50"):
                opp_val = getattr(old_value, "TaskObject50", None)
                if opp_val == self:
                    setattr(old_value, "TaskObject50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TaskObject50"):
                opp_val = getattr(value, "TaskObject50", None)
                setattr(value, "TaskObject50", self)

class ColorData:

    pass
class Component:

    pass
class HALL_TaskObject(Component):

    def __init__(self, completionTime: int, numberofgoalscompleted: int, TaskObject: "HALL_UserProfile" = None, goalInv: set["HALL_Goal"] = None, taskObject: "HALL_UserProfile" = None, TaskObject44: "HALL_TaskObject" = None, componentSetInv43: set["HALL_TaskObject"] = None, TaskObject48: "HALL_TaskObject" = None, componentSet47: "HALL_TaskObject" = None, TaskObject50: "HALL_Goal" = None):
        self.completionTime = completionTime
        self.numberofgoalscompleted = numberofgoalscompleted
        self.TaskObject = TaskObject
        self.goalInv = goalInv if goalInv is not None else set()
        self.taskObject = taskObject
        self.TaskObject44 = TaskObject44
        self.componentSetInv43 = componentSetInv43 if componentSetInv43 is not None else set()
        self.TaskObject48 = TaskObject48
        self.componentSet47 = componentSet47
        self.TaskObject50 = TaskObject50
        
        pass
    @property
    def completionTime(self):
        return self.__completionTime

    @completionTime.setter
    def completionTime(self, completionTime: int):
        self.__completionTime = completionTime


    @property
    def numberofgoalscompleted(self):
        return self.__numberofgoalscompleted

    @numberofgoalscompleted.setter
    def numberofgoalscompleted(self, numberofgoalscompleted: int):
        self.__numberofgoalscompleted = numberofgoalscompleted


    @property
    def TaskObject48(self):
        return self.__TaskObject48

    @TaskObject48.setter
    def TaskObject48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_TaskObject__TaskObject48", None)
        self.__TaskObject48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentSet47"):
                opp_val = getattr(old_value, "componentSet47", None)
                if opp_val == self:
                    setattr(old_value, "componentSet47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentSet47"):
                opp_val = getattr(value, "componentSet47", None)
                setattr(value, "componentSet47", self)

    @property
    def taskObject(self):
        return self.__taskObject

    @taskObject.setter
    def taskObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_TaskObject__taskObject", None)
        self.__taskObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UserProfile40"):
                opp_val = getattr(old_value, "UserProfile40", None)
                if opp_val == self:
                    setattr(old_value, "UserProfile40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UserProfile40"):
                opp_val = getattr(value, "UserProfile40", None)
                setattr(value, "UserProfile40", self)

    @property
    def componentSetInv43(self):
        return self.__componentSetInv43

    @componentSetInv43.setter
    def componentSetInv43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_TaskObject__componentSetInv43", None)
        self.__componentSetInv43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TaskObject44"):
                    opp_val = getattr(item, "TaskObject44", None)
                    
                    if opp_val == self:
                        setattr(item, "TaskObject44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TaskObject44"):
                    opp_val = getattr(item, "TaskObject44", None)
                    
                    setattr(item, "TaskObject44", self)
                    

    @property
    def componentSet47(self):
        return self.__componentSet47

    @componentSet47.setter
    def componentSet47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_TaskObject__componentSet47", None)
        self.__componentSet47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TaskObject48"):
                opp_val = getattr(old_value, "TaskObject48", None)
                if opp_val == self:
                    setattr(old_value, "TaskObject48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TaskObject48"):
                opp_val = getattr(value, "TaskObject48", None)
                setattr(value, "TaskObject48", self)

    @property
    def TaskObject44(self):
        return self.__TaskObject44

    @TaskObject44.setter
    def TaskObject44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_TaskObject__TaskObject44", None)
        self.__TaskObject44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentSetInv43"):
                opp_val = getattr(old_value, "componentSetInv43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentSetInv43"):
                opp_val = getattr(value, "componentSetInv43", None)
                if opp_val is None:
                    setattr(value, "componentSetInv43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TaskObject50(self):
        return self.__TaskObject50

    @TaskObject50.setter
    def TaskObject50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_TaskObject__TaskObject50", None)
        self.__TaskObject50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "goal"):
                opp_val = getattr(old_value, "goal", None)
                if opp_val == self:
                    setattr(old_value, "goal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "goal"):
                opp_val = getattr(value, "goal", None)
                setattr(value, "goal", self)

    @property
    def TaskObject(self):
        return self.__TaskObject

    @TaskObject.setter
    def TaskObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_TaskObject__TaskObject", None)
        self.__TaskObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "taskObjectInv"):
                opp_val = getattr(old_value, "taskObjectInv", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "taskObjectInv"):
                opp_val = getattr(value, "taskObjectInv", None)
                if opp_val is None:
                    setattr(value, "taskObjectInv", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def goalInv(self):
        return self.__goalInv

    @goalInv.setter
    def goalInv(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_TaskObject__goalInv", None)
        self.__goalInv = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Goal"):
                    opp_val = getattr(item, "Goal", None)
                    
                    if opp_val == self:
                        setattr(item, "Goal", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Goal"):
                    opp_val = getattr(item, "Goal", None)
                    
                    setattr(item, "Goal", self)
                    

class HALL_VisualObject(Component):

    def __init__(self, vtype: str, geometryDataInv: "GeometryData" = None, visualObject: "HALL_UserProfile" = None, VisualObject: "HALL_VisualObject" = None, componentSetInv: set["HALL_VisualObject"] = None, VisualObject7: "HALL_VisualObject" = None, componentSet: "HALL_VisualObject" = None, colorDataInv: "ColorData" = None, VisualObject26: "HALL_UserProfile" = None):
        self.vtype = vtype
        self.geometryDataInv = geometryDataInv
        self.visualObject = visualObject
        self.VisualObject = VisualObject
        self.componentSetInv = componentSetInv if componentSetInv is not None else set()
        self.VisualObject7 = VisualObject7
        self.componentSet = componentSet
        self.colorDataInv = colorDataInv
        self.VisualObject26 = VisualObject26
        
        pass
    @property
    def vtype(self):
        return self.__vtype

    @vtype.setter
    def vtype(self, vtype: str):
        self.__vtype = vtype


    @property
    def VisualObject7(self):
        return self.__VisualObject7

    @VisualObject7.setter
    def VisualObject7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_VisualObject__VisualObject7", None)
        self.__VisualObject7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentSet"):
                opp_val = getattr(old_value, "componentSet", None)
                if opp_val == self:
                    setattr(old_value, "componentSet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentSet"):
                opp_val = getattr(value, "componentSet", None)
                setattr(value, "componentSet", self)

    @property
    def visualObject(self):
        return self.__visualObject

    @visualObject.setter
    def visualObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_VisualObject__visualObject", None)
        self.__visualObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UserProfile"):
                opp_val = getattr(old_value, "UserProfile", None)
                if opp_val == self:
                    setattr(old_value, "UserProfile", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UserProfile"):
                opp_val = getattr(value, "UserProfile", None)
                setattr(value, "UserProfile", self)

    @property
    def VisualObject26(self):
        return self.__VisualObject26

    @VisualObject26.setter
    def VisualObject26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_VisualObject__VisualObject26", None)
        self.__VisualObject26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "visualObjectInv"):
                opp_val = getattr(old_value, "visualObjectInv", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "visualObjectInv"):
                opp_val = getattr(value, "visualObjectInv", None)
                if opp_val is None:
                    setattr(value, "visualObjectInv", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def VisualObject(self):
        return self.__VisualObject

    @VisualObject.setter
    def VisualObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_VisualObject__VisualObject", None)
        self.__VisualObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentSetInv"):
                opp_val = getattr(old_value, "componentSetInv", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentSetInv"):
                opp_val = getattr(value, "componentSetInv", None)
                if opp_val is None:
                    setattr(value, "componentSetInv", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def geometryDataInv(self):
        return self.__geometryDataInv

    @geometryDataInv.setter
    def geometryDataInv(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_VisualObject__geometryDataInv", None)
        self.__geometryDataInv = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GeometryData"):
                opp_val = getattr(old_value, "GeometryData", None)
                if opp_val == self:
                    setattr(old_value, "GeometryData", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GeometryData"):
                opp_val = getattr(value, "GeometryData", None)
                setattr(value, "GeometryData", self)

    @property
    def colorDataInv(self):
        return self.__colorDataInv

    @colorDataInv.setter
    def colorDataInv(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_VisualObject__colorDataInv", None)
        self.__colorDataInv = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColorData"):
                opp_val = getattr(old_value, "ColorData", None)
                if opp_val == self:
                    setattr(old_value, "ColorData", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorData"):
                opp_val = getattr(value, "ColorData", None)
                setattr(value, "ColorData", self)

    @property
    def componentSet(self):
        return self.__componentSet

    @componentSet.setter
    def componentSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_VisualObject__componentSet", None)
        self.__componentSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VisualObject7"):
                opp_val = getattr(old_value, "VisualObject7", None)
                if opp_val == self:
                    setattr(old_value, "VisualObject7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VisualObject7"):
                opp_val = getattr(value, "VisualObject7", None)
                setattr(value, "VisualObject7", self)

    @property
    def componentSetInv(self):
        return self.__componentSetInv

    @componentSetInv.setter
    def componentSetInv(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_VisualObject__componentSetInv", None)
        self.__componentSetInv = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VisualObject"):
                    opp_val = getattr(item, "VisualObject", None)
                    
                    if opp_val == self:
                        setattr(item, "VisualObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VisualObject"):
                    opp_val = getattr(item, "VisualObject", None)
                    
                    setattr(item, "VisualObject", self)
                    

class HALL_Model:

    pass
class HALL_SystemComponent(Component):

    pass
class MessageHandler:

    pass
class FSM:

    pass
class HALL_Data:

    def __init__(self, currentValue: str, name: str, initValue: str, Data: "HALL_Component" = None, data: "MessageDefinition" = None, data60: "HALL_Component" = None, HALL_Data: "Type" = None):
        self.currentValue = currentValue
        self.name = name
        self.initValue = initValue
        self.Data = Data
        self.data = data
        self.data60 = data60
        self.HALL_Data = HALL_Data
        
        pass
    @property
    def currentValue(self):
        return self.__currentValue

    @currentValue.setter
    def currentValue(self, currentValue: str):
        self.__currentValue = currentValue


    @property
    def initValue(self):
        return self.__initValue

    @initValue.setter
    def initValue(self, initValue: str):
        self.__initValue = initValue


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def data60(self):
        return self.__data60

    @data60.setter
    def data60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Data__data60", None)
        self.__data60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Component"):
                opp_val = getattr(old_value, "Component", None)
                if opp_val == self:
                    setattr(old_value, "Component", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Component"):
                opp_val = getattr(value, "Component", None)
                setattr(value, "Component", self)

    @property
    def Data(self):
        return self.__Data

    @Data.setter
    def Data(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Data__Data", None)
        self.__Data = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataInvComponent"):
                opp_val = getattr(old_value, "dataInvComponent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataInvComponent"):
                opp_val = getattr(value, "dataInvComponent", None)
                if opp_val is None:
                    setattr(value, "dataInvComponent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def HALL_Data(self):
        return self.__HALL_Data

    @HALL_Data.setter
    def HALL_Data(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Data__HALL_Data", None)
        self.__HALL_Data = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type56"):
                opp_val = getattr(old_value, "Type56", None)
                if opp_val == self:
                    setattr(old_value, "Type56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type56"):
                opp_val = getattr(value, "Type56", None)
                setattr(value, "Type56", self)

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Data__data", None)
        self.__data = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MessageDefinition58"):
                opp_val = getattr(old_value, "MessageDefinition58", None)
                if opp_val == self:
                    setattr(old_value, "MessageDefinition58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MessageDefinition58"):
                opp_val = getattr(value, "MessageDefinition58", None)
                setattr(value, "MessageDefinition58", self)

class HALL_Component(ABC):

    def __init__(self, name: str, dataInvComponent: set["HALL_Data"] = None, FSMInv: "FSM" = None, messageHandlerSetInv: set["MessageHandler"] = None, Component: "HALL_Data" = None):
        self.name = name
        self.dataInvComponent = dataInvComponent if dataInvComponent is not None else set()
        self.FSMInv = FSMInv
        self.messageHandlerSetInv = messageHandlerSetInv if messageHandlerSetInv is not None else set()
        self.Component = Component
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def FSMInv(self):
        return self.__FSMInv

    @FSMInv.setter
    def FSMInv(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Component__FSMInv", None)
        self.__FSMInv = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM"):
                opp_val = getattr(old_value, "FSM", None)
                if opp_val == self:
                    setattr(old_value, "FSM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM"):
                opp_val = getattr(value, "FSM", None)
                setattr(value, "FSM", self)

    @property
    def Component(self):
        return self.__Component

    @Component.setter
    def Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Component__Component", None)
        self.__Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "data60"):
                opp_val = getattr(old_value, "data60", None)
                if opp_val == self:
                    setattr(old_value, "data60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "data60"):
                opp_val = getattr(value, "data60", None)
                setattr(value, "data60", self)

    @property
    def messageHandlerSetInv(self):
        return self.__messageHandlerSetInv

    @messageHandlerSetInv.setter
    def messageHandlerSetInv(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Component__messageHandlerSetInv", None)
        self.__messageHandlerSetInv = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MessageHandler"):
                    opp_val = getattr(item, "MessageHandler", None)
                    
                    if opp_val == self:
                        setattr(item, "MessageHandler", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MessageHandler"):
                    opp_val = getattr(item, "MessageHandler", None)
                    
                    setattr(item, "MessageHandler", self)
                    

    @property
    def dataInvComponent(self):
        return self.__dataInvComponent

    @dataInvComponent.setter
    def dataInvComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Component__dataInvComponent", None)
        self.__dataInvComponent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Data"):
                    opp_val = getattr(item, "Data", None)
                    
                    if opp_val == self:
                        setattr(item, "Data", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Data"):
                    opp_val = getattr(item, "Data", None)
                    
                    setattr(item, "Data", self)
                    

class HALL_UserProfile(Component):

    def __init__(self, numberofcompletedtasks: int, UserProfile: "HALL_VisualObject" = None, visualObjectInv: set["HALL_VisualObject"] = None, taskObjectInv: set["HALL_TaskObject"] = None, userProfile: "HALL_Model" = None, UserProfile33: "HALL_UserProfile" = None, componentSetInv32: set["HALL_UserProfile"] = None, UserProfile37: "HALL_UserProfile" = None, componentSet36: "HALL_UserProfile" = None, UserProfile40: "HALL_TaskObject" = None, UserProfile20: "HALL_Model" = None):
        self.numberofcompletedtasks = numberofcompletedtasks
        self.UserProfile = UserProfile
        self.visualObjectInv = visualObjectInv if visualObjectInv is not None else set()
        self.taskObjectInv = taskObjectInv if taskObjectInv is not None else set()
        self.userProfile = userProfile
        self.UserProfile33 = UserProfile33
        self.componentSetInv32 = componentSetInv32 if componentSetInv32 is not None else set()
        self.UserProfile37 = UserProfile37
        self.componentSet36 = componentSet36
        self.UserProfile40 = UserProfile40
        self.UserProfile20 = UserProfile20
        
        pass
    @property
    def numberofcompletedtasks(self):
        return self.__numberofcompletedtasks

    @numberofcompletedtasks.setter
    def numberofcompletedtasks(self, numberofcompletedtasks: int):
        self.__numberofcompletedtasks = numberofcompletedtasks


    @property
    def UserProfile37(self):
        return self.__UserProfile37

    @UserProfile37.setter
    def UserProfile37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_UserProfile__UserProfile37", None)
        self.__UserProfile37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentSet36"):
                opp_val = getattr(old_value, "componentSet36", None)
                if opp_val == self:
                    setattr(old_value, "componentSet36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentSet36"):
                opp_val = getattr(value, "componentSet36", None)
                setattr(value, "componentSet36", self)

    @property
    def taskObjectInv(self):
        return self.__taskObjectInv

    @taskObjectInv.setter
    def taskObjectInv(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_UserProfile__taskObjectInv", None)
        self.__taskObjectInv = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TaskObject"):
                    opp_val = getattr(item, "TaskObject", None)
                    
                    if opp_val == self:
                        setattr(item, "TaskObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TaskObject"):
                    opp_val = getattr(item, "TaskObject", None)
                    
                    setattr(item, "TaskObject", self)
                    

    @property
    def userProfile(self):
        return self.__userProfile

    @userProfile.setter
    def userProfile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_UserProfile__userProfile", None)
        self.__userProfile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model29"):
                opp_val = getattr(old_value, "Model29", None)
                if opp_val == self:
                    setattr(old_value, "Model29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model29"):
                opp_val = getattr(value, "Model29", None)
                setattr(value, "Model29", self)

    @property
    def UserProfile(self):
        return self.__UserProfile

    @UserProfile.setter
    def UserProfile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_UserProfile__UserProfile", None)
        self.__UserProfile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "visualObject"):
                opp_val = getattr(old_value, "visualObject", None)
                if opp_val == self:
                    setattr(old_value, "visualObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "visualObject"):
                opp_val = getattr(value, "visualObject", None)
                setattr(value, "visualObject", self)

    @property
    def UserProfile33(self):
        return self.__UserProfile33

    @UserProfile33.setter
    def UserProfile33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_UserProfile__UserProfile33", None)
        self.__UserProfile33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentSetInv32"):
                opp_val = getattr(old_value, "componentSetInv32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentSetInv32"):
                opp_val = getattr(value, "componentSetInv32", None)
                if opp_val is None:
                    setattr(value, "componentSetInv32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def componentSetInv32(self):
        return self.__componentSetInv32

    @componentSetInv32.setter
    def componentSetInv32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_UserProfile__componentSetInv32", None)
        self.__componentSetInv32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UserProfile33"):
                    opp_val = getattr(item, "UserProfile33", None)
                    
                    if opp_val == self:
                        setattr(item, "UserProfile33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UserProfile33"):
                    opp_val = getattr(item, "UserProfile33", None)
                    
                    setattr(item, "UserProfile33", self)
                    

    @property
    def componentSet36(self):
        return self.__componentSet36

    @componentSet36.setter
    def componentSet36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_UserProfile__componentSet36", None)
        self.__componentSet36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UserProfile37"):
                opp_val = getattr(old_value, "UserProfile37", None)
                if opp_val == self:
                    setattr(old_value, "UserProfile37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UserProfile37"):
                opp_val = getattr(value, "UserProfile37", None)
                setattr(value, "UserProfile37", self)

    @property
    def visualObjectInv(self):
        return self.__visualObjectInv

    @visualObjectInv.setter
    def visualObjectInv(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_UserProfile__visualObjectInv", None)
        self.__visualObjectInv = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VisualObject26"):
                    opp_val = getattr(item, "VisualObject26", None)
                    
                    if opp_val == self:
                        setattr(item, "VisualObject26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VisualObject26"):
                    opp_val = getattr(item, "VisualObject26", None)
                    
                    setattr(item, "VisualObject26", self)
                    

    @property
    def UserProfile20(self):
        return self.__UserProfile20

    @UserProfile20.setter
    def UserProfile20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_UserProfile__UserProfile20", None)
        self.__UserProfile20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "userProfileInv"):
                opp_val = getattr(old_value, "userProfileInv", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "userProfileInv"):
                opp_val = getattr(value, "userProfileInv", None)
                if opp_val is None:
                    setattr(value, "userProfileInv", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UserProfile40(self):
        return self.__UserProfile40

    @UserProfile40.setter
    def UserProfile40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_UserProfile__UserProfile40", None)
        self.__UserProfile40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "taskObject"):
                opp_val = getattr(old_value, "taskObject", None)
                if opp_val == self:
                    setattr(old_value, "taskObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "taskObject"):
                opp_val = getattr(value, "taskObject", None)
                setattr(value, "taskObject", self)

class GeometryData:

    pass
class HALL_Geometry_GeometryData3D(GeometryData):

    pass
class HALL_Geometry_GeometryData2D(GeometryData):

    def __init__(self, labelText: str, point2dInv: set["Point2D"] = None, GeometryData: "HALL_VisualObject" = None):
        self.labelText = labelText
        self.point2dInv = point2dInv if point2dInv is not None else set()
        
        pass
    @property
    def labelText(self):
        return self.__labelText

    @labelText.setter
    def labelText(self, labelText: str):
        self.__labelText = labelText


    @property
    def point2dInv(self):
        return self.__point2dInv

    @point2dInv.setter
    def point2dInv(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Geometry_GeometryData2D__point2dInv", None)
        self.__point2dInv = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Point2D"):
                    opp_val = getattr(item, "Point2D", None)
                    
                    if opp_val == self:
                        setattr(item, "Point2D", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Point2D"):
                    opp_val = getattr(item, "Point2D", None)
                    
                    setattr(item, "Point2D", self)
                    
