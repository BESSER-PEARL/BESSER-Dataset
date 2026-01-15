from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class FSMActions_HALL_Component:

    pass
class HALL_FSMActions_ActionExpression(ABC):

    pass
class ActionExpressionElement:

    pass
class HALL_FSMActions_BinaryOperator(ActionExpressionElement):

    def __init__(self, operatorname: str, HALL_FSMActions_BinaryOperator: "FSMActions_ActionExpressionElement" = None, HALL_FSMActions_BinaryOperator357: "FSMActions_ActionExpressionElement" = None):
        self.operatorname = operatorname
        self.HALL_FSMActions_BinaryOperator = HALL_FSMActions_BinaryOperator
        self.HALL_FSMActions_BinaryOperator357 = HALL_FSMActions_BinaryOperator357
        
    @property
    def operatorname(self) -> str:
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
            if hasattr(old_value, "FSMActions_ActionExpressionElement355"):
                opp_val = getattr(old_value, "FSMActions_ActionExpressionElement355", None)
                if opp_val == self:
                    setattr(old_value, "FSMActions_ActionExpressionElement355", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMActions_ActionExpressionElement355"):
                opp_val = getattr(value, "FSMActions_ActionExpressionElement355", None)
                setattr(value, "FSMActions_ActionExpressionElement355", self)

    @property
    def HALL_FSMActions_BinaryOperator357(self):
        return self.__HALL_FSMActions_BinaryOperator357

    @HALL_FSMActions_BinaryOperator357.setter
    def HALL_FSMActions_BinaryOperator357(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMActions_BinaryOperator__HALL_FSMActions_BinaryOperator357", None)
        self.__HALL_FSMActions_BinaryOperator357 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMActions_ActionExpressionElement358"):
                opp_val = getattr(old_value, "FSMActions_ActionExpressionElement358", None)
                if opp_val == self:
                    setattr(old_value, "FSMActions_ActionExpressionElement358", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMActions_ActionExpressionElement358"):
                opp_val = getattr(value, "FSMActions_ActionExpressionElement358", None)
                setattr(value, "FSMActions_ActionExpressionElement358", self)

class HALL_FSMActions_Let(ActionExpressionElement):

    def __init__(self, namevar: str, HALL_FSMActions_Let: "FSMActions_ActionExpressionElement" = None, HALL_FSMActions_Let342: "FSMActions_ActionExpressionElement" = None):
        self.namevar = namevar
        self.HALL_FSMActions_Let = HALL_FSMActions_Let
        self.HALL_FSMActions_Let342 = HALL_FSMActions_Let342
        
    @property
    def namevar(self) -> str:
        return self.__namevar

    @namevar.setter
    def namevar(self, namevar: str):
        self.__namevar = namevar

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
            if hasattr(old_value, "FSMActions_ActionExpressionElement"):
                opp_val = getattr(old_value, "FSMActions_ActionExpressionElement", None)
                if opp_val == self:
                    setattr(old_value, "FSMActions_ActionExpressionElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMActions_ActionExpressionElement"):
                opp_val = getattr(value, "FSMActions_ActionExpressionElement", None)
                setattr(value, "FSMActions_ActionExpressionElement", self)

    @property
    def HALL_FSMActions_Let342(self):
        return self.__HALL_FSMActions_Let342

    @HALL_FSMActions_Let342.setter
    def HALL_FSMActions_Let342(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMActions_Let__HALL_FSMActions_Let342", None)
        self.__HALL_FSMActions_Let342 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMActions_ActionExpressionElement343"):
                opp_val = getattr(old_value, "FSMActions_ActionExpressionElement343", None)
                if opp_val == self:
                    setattr(old_value, "FSMActions_ActionExpressionElement343", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMActions_ActionExpressionElement343"):
                opp_val = getattr(value, "FSMActions_ActionExpressionElement343", None)
                setattr(value, "FSMActions_ActionExpressionElement343", self)

class HALL_FSMActions_DomainPropertyGet(ActionExpressionElement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class HALL_FSMActions_GetData(ActionExpressionElement):

    def __init__(self, field: str, HALL_FSMActions_GetData: "FSMActions_HALL_Component" = None):
        self.field = field
        self.HALL_FSMActions_GetData = HALL_FSMActions_GetData
        
    @property
    def field(self) -> str:
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field

    @property
    def HALL_FSMActions_GetData(self):
        return self.__HALL_FSMActions_GetData

    @HALL_FSMActions_GetData.setter
    def HALL_FSMActions_GetData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMActions_GetData__HALL_FSMActions_GetData", None)
        self.__HALL_FSMActions_GetData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMActions_HALL_Component"):
                opp_val = getattr(old_value, "FSMActions_HALL_Component", None)
                if opp_val == self:
                    setattr(old_value, "FSMActions_HALL_Component", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMActions_HALL_Component"):
                opp_val = getattr(value, "FSMActions_HALL_Component", None)
                setattr(value, "FSMActions_HALL_Component", self)

class HALL_FSMActions_Literal(ActionExpressionElement):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class HALL_FSMActions_MessageInvocation(ActionExpressionElement):

    def __init__(self, name: str, isTopDown: bool, HALL_FSMActions_MessageInvocation: set["FSMActions_ActionExpressionElement"] = None):
        self.name = name
        self.isTopDown = isTopDown
        self.HALL_FSMActions_MessageInvocation = HALL_FSMActions_MessageInvocation if HALL_FSMActions_MessageInvocation is not None else set()
        
    @property
    def isTopDown(self) -> bool:
        return self.__isTopDown

    @isTopDown.setter
    def isTopDown(self, isTopDown: bool):
        self.__isTopDown = isTopDown

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def HALL_FSMActions_MessageInvocation(self):
        return self.__HALL_FSMActions_MessageInvocation

    @HALL_FSMActions_MessageInvocation.setter
    def HALL_FSMActions_MessageInvocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMActions_MessageInvocation__HALL_FSMActions_MessageInvocation", None)
        self.__HALL_FSMActions_MessageInvocation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FSMActions_ActionExpressionElement345"):
                    opp_val = getattr(item, "FSMActions_ActionExpressionElement345", None)
                    
                    if opp_val == self:
                        setattr(item, "FSMActions_ActionExpressionElement345", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FSMActions_ActionExpressionElement345"):
                    opp_val = getattr(item, "FSMActions_ActionExpressionElement345", None)
                    
                    setattr(item, "FSMActions_ActionExpressionElement345", self)
                    

class HALL_FSMActions_DomainPropertySet(ActionExpressionElement):

    def __init__(self, name: str, HALL_FSMActions_DomainPropertySet: "FSMActions_ActionExpressionElement" = None):
        self.name = name
        self.HALL_FSMActions_DomainPropertySet = HALL_FSMActions_DomainPropertySet
        
    @property
    def name(self) -> str:
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
            if hasattr(old_value, "FSMActions_ActionExpressionElement352"):
                opp_val = getattr(old_value, "FSMActions_ActionExpressionElement352", None)
                if opp_val == self:
                    setattr(old_value, "FSMActions_ActionExpressionElement352", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMActions_ActionExpressionElement352"):
                opp_val = getattr(value, "FSMActions_ActionExpressionElement352", None)
                setattr(value, "FSMActions_ActionExpressionElement352", self)

class HALL_FSMActions_UnaryOperator(ActionExpressionElement):

    def __init__(self, operatorname: str, HALL_FSMActions_UnaryOperator: "FSMActions_ActionExpressionElement" = None):
        self.operatorname = operatorname
        self.HALL_FSMActions_UnaryOperator = HALL_FSMActions_UnaryOperator
        
    @property
    def operatorname(self) -> str:
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
            if hasattr(old_value, "FSMActions_ActionExpressionElement360"):
                opp_val = getattr(old_value, "FSMActions_ActionExpressionElement360", None)
                if opp_val == self:
                    setattr(old_value, "FSMActions_ActionExpressionElement360", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMActions_ActionExpressionElement360"):
                opp_val = getattr(value, "FSMActions_ActionExpressionElement360", None)
                setattr(value, "FSMActions_ActionExpressionElement360", self)

class HALL_FSMActions_VarRef(ActionExpressionElement):

    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class HALL_FSMActions_ActionExpressionElement(ABC):

    pass
class FSMActions_ActionExpressionElement:

    pass
class PreConditionExpressionElement:

    pass
class HALL_FSMConditions_VarRef(PreConditionExpressionElement):

    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class HALL_FSMConditions_BinaryOperator(PreConditionExpressionElement):

    def __init__(self, operatorname: str, HALL_FSMConditions_BinaryOperator319: "FSMConditions_PreConditionExpressionElement" = None, HALL_FSMConditions_BinaryOperator: "FSMConditions_PreConditionExpressionElement" = None):
        self.operatorname = operatorname
        self.HALL_FSMConditions_BinaryOperator319 = HALL_FSMConditions_BinaryOperator319
        self.HALL_FSMConditions_BinaryOperator = HALL_FSMConditions_BinaryOperator
        
    @property
    def operatorname(self) -> str:
        return self.__operatorname

    @operatorname.setter
    def operatorname(self, operatorname: str):
        self.__operatorname = operatorname

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
            if hasattr(old_value, "FSMConditions_PreConditionExpressionElement"):
                opp_val = getattr(old_value, "FSMConditions_PreConditionExpressionElement", None)
                if opp_val == self:
                    setattr(old_value, "FSMConditions_PreConditionExpressionElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMConditions_PreConditionExpressionElement"):
                opp_val = getattr(value, "FSMConditions_PreConditionExpressionElement", None)
                setattr(value, "FSMConditions_PreConditionExpressionElement", self)

    @property
    def HALL_FSMConditions_BinaryOperator319(self):
        return self.__HALL_FSMConditions_BinaryOperator319

    @HALL_FSMConditions_BinaryOperator319.setter
    def HALL_FSMConditions_BinaryOperator319(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMConditions_BinaryOperator__HALL_FSMConditions_BinaryOperator319", None)
        self.__HALL_FSMConditions_BinaryOperator319 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMConditions_PreConditionExpressionElement320"):
                opp_val = getattr(old_value, "FSMConditions_PreConditionExpressionElement320", None)
                if opp_val == self:
                    setattr(old_value, "FSMConditions_PreConditionExpressionElement320", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMConditions_PreConditionExpressionElement320"):
                opp_val = getattr(value, "FSMConditions_PreConditionExpressionElement320", None)
                setattr(value, "FSMConditions_PreConditionExpressionElement320", self)

class HALL_FSMConditions_DomainPropertyGet(PreConditionExpressionElement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class HALL_FSMConditions_Let(PreConditionExpressionElement):

    def __init__(self, namevar: str, HALL_FSMConditions_Let: "FSMConditions_PreConditionExpressionElement" = None, HALL_FSMConditions_Let329: "FSMConditions_PreConditionExpressionElement" = None):
        self.namevar = namevar
        self.HALL_FSMConditions_Let = HALL_FSMConditions_Let
        self.HALL_FSMConditions_Let329 = HALL_FSMConditions_Let329
        
    @property
    def namevar(self) -> str:
        return self.__namevar

    @namevar.setter
    def namevar(self, namevar: str):
        self.__namevar = namevar

    @property
    def HALL_FSMConditions_Let329(self):
        return self.__HALL_FSMConditions_Let329

    @HALL_FSMConditions_Let329.setter
    def HALL_FSMConditions_Let329(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMConditions_Let__HALL_FSMConditions_Let329", None)
        self.__HALL_FSMConditions_Let329 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMConditions_PreConditionExpressionElement330"):
                opp_val = getattr(old_value, "FSMConditions_PreConditionExpressionElement330", None)
                if opp_val == self:
                    setattr(old_value, "FSMConditions_PreConditionExpressionElement330", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMConditions_PreConditionExpressionElement330"):
                opp_val = getattr(value, "FSMConditions_PreConditionExpressionElement330", None)
                setattr(value, "FSMConditions_PreConditionExpressionElement330", self)

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
            if hasattr(old_value, "FSMConditions_PreConditionExpressionElement327"):
                opp_val = getattr(old_value, "FSMConditions_PreConditionExpressionElement327", None)
                if opp_val == self:
                    setattr(old_value, "FSMConditions_PreConditionExpressionElement327", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMConditions_PreConditionExpressionElement327"):
                opp_val = getattr(value, "FSMConditions_PreConditionExpressionElement327", None)
                setattr(value, "FSMConditions_PreConditionExpressionElement327", self)

class HALL_FSMConditions_GetData(PreConditionExpressionElement):

    def __init__(self, field: str, HALL_FSMConditions_GetData: "FSMConditions_HALL_Component" = None):
        self.field = field
        self.HALL_FSMConditions_GetData = HALL_FSMConditions_GetData
        
    @property
    def field(self) -> str:
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field

    @property
    def HALL_FSMConditions_GetData(self):
        return self.__HALL_FSMConditions_GetData

    @HALL_FSMConditions_GetData.setter
    def HALL_FSMConditions_GetData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMConditions_GetData__HALL_FSMConditions_GetData", None)
        self.__HALL_FSMConditions_GetData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMConditions_HALL_Component325"):
                opp_val = getattr(old_value, "FSMConditions_HALL_Component325", None)
                if opp_val == self:
                    setattr(old_value, "FSMConditions_HALL_Component325", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMConditions_HALL_Component325"):
                opp_val = getattr(value, "FSMConditions_HALL_Component325", None)
                setattr(value, "FSMConditions_HALL_Component325", self)

class HALL_FSMConditions_Literal(PreConditionExpressionElement):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class HALL_FSMConditions_PreConditionExpressionElement(ABC):

    pass
class FSMConditions_PreConditionExpressionElement:

    pass
class HALL_FSMConditions_PreConditionExpression(ABC):

    pass
class FSMConditions_HALL_Component:

    pass
class HALL_FSMConditions_GetState(PreConditionExpressionElement):

    pass
class HALL_FSMConditions_UnaryOperator(PreConditionExpressionElement):

    def __init__(self, operatorname: str, HALL_FSMConditions_UnaryOperator: "FSMConditions_PreConditionExpressionElement" = None):
        self.operatorname = operatorname
        self.HALL_FSMConditions_UnaryOperator = HALL_FSMConditions_UnaryOperator
        
    @property
    def operatorname(self) -> str:
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
            if hasattr(old_value, "FSMConditions_PreConditionExpressionElement322"):
                opp_val = getattr(old_value, "FSMConditions_PreConditionExpressionElement322", None)
                if opp_val == self:
                    setattr(old_value, "FSMConditions_PreConditionExpressionElement322", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMConditions_PreConditionExpressionElement322"):
                opp_val = getattr(value, "FSMConditions_PreConditionExpressionElement322", None)
                setattr(value, "FSMConditions_PreConditionExpressionElement322", self)

class FSMInstructions_HALL_Component:

    pass
class Trigger_TriggerExpressionElement:

    pass
class HALL_Trigger_TriggerExpression:

    pass
class Transition:

    pass
class HALL_FSM_State(ABC):

    def __init__(self, isActive: bool, Transition: set["Transition"] = None):
        self.isActive = isActive
        self.Transition = Transition if Transition is not None else set()
        
    @property
    def isActive(self) -> bool:
        return self.__isActive

    @isActive.setter
    def isActive(self, isActive: bool):
        self.__isActive = isActive

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSM_State__Transition", None)
        self.__Transition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FSM268"):
                    opp_val = getattr(item, "FSM268", None)
                    
                    if opp_val == self:
                        setattr(item, "FSM268", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FSM268"):
                    opp_val = getattr(item, "FSM268", None)
                    
                    setattr(item, "FSM268", self)
                    

class Trigger_TriggerExpression:

    pass
class FSMActions_ActionExpression:

    pass
class FSMInstructions_PosConditionExpression:

    pass
class FSMConditions_PreConditionExpression:

    pass
class PosConditionExpressionElement:

    pass
class HALL_FSMInstructions_SetData(PosConditionExpressionElement):

    def __init__(self, field: str, HALL_FSMInstructions_SetData: "FSMInstructions_PosConditionExpressionElement" = None, HALL_FSMInstructions_SetData301: "FSMInstructions_HALL_Component" = None):
        self.field = field
        self.HALL_FSMInstructions_SetData = HALL_FSMInstructions_SetData
        self.HALL_FSMInstructions_SetData301 = HALL_FSMInstructions_SetData301
        
    @property
    def field(self) -> str:
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field

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
            if hasattr(old_value, "FSMInstructions_PosConditionExpressionElement299"):
                opp_val = getattr(old_value, "FSMInstructions_PosConditionExpressionElement299", None)
                if opp_val == self:
                    setattr(old_value, "FSMInstructions_PosConditionExpressionElement299", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMInstructions_PosConditionExpressionElement299"):
                opp_val = getattr(value, "FSMInstructions_PosConditionExpressionElement299", None)
                setattr(value, "FSMInstructions_PosConditionExpressionElement299", self)

    @property
    def HALL_FSMInstructions_SetData301(self):
        return self.__HALL_FSMInstructions_SetData301

    @HALL_FSMInstructions_SetData301.setter
    def HALL_FSMInstructions_SetData301(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMInstructions_SetData__HALL_FSMInstructions_SetData301", None)
        self.__HALL_FSMInstructions_SetData301 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMInstructions_HALL_Component302"):
                opp_val = getattr(old_value, "FSMInstructions_HALL_Component302", None)
                if opp_val == self:
                    setattr(old_value, "FSMInstructions_HALL_Component302", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMInstructions_HALL_Component302"):
                opp_val = getattr(value, "FSMInstructions_HALL_Component302", None)
                setattr(value, "FSMInstructions_HALL_Component302", self)

class HALL_FSMInstructions_Let(PosConditionExpressionElement):

    def __init__(self, namevar: str, HALL_FSMInstructions_Let: "FSMInstructions_PosConditionExpressionElement" = None, HALL_FSMInstructions_Let306: "FSMInstructions_PosConditionExpressionElement" = None):
        self.namevar = namevar
        self.HALL_FSMInstructions_Let = HALL_FSMInstructions_Let
        self.HALL_FSMInstructions_Let306 = HALL_FSMInstructions_Let306
        
    @property
    def namevar(self) -> str:
        return self.__namevar

    @namevar.setter
    def namevar(self, namevar: str):
        self.__namevar = namevar

    @property
    def HALL_FSMInstructions_Let306(self):
        return self.__HALL_FSMInstructions_Let306

    @HALL_FSMInstructions_Let306.setter
    def HALL_FSMInstructions_Let306(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMInstructions_Let__HALL_FSMInstructions_Let306", None)
        self.__HALL_FSMInstructions_Let306 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMInstructions_PosConditionExpressionElement307"):
                opp_val = getattr(old_value, "FSMInstructions_PosConditionExpressionElement307", None)
                if opp_val == self:
                    setattr(old_value, "FSMInstructions_PosConditionExpressionElement307", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMInstructions_PosConditionExpressionElement307"):
                opp_val = getattr(value, "FSMInstructions_PosConditionExpressionElement307", None)
                setattr(value, "FSMInstructions_PosConditionExpressionElement307", self)

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
            if hasattr(old_value, "FSMInstructions_PosConditionExpressionElement304"):
                opp_val = getattr(old_value, "FSMInstructions_PosConditionExpressionElement304", None)
                if opp_val == self:
                    setattr(old_value, "FSMInstructions_PosConditionExpressionElement304", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMInstructions_PosConditionExpressionElement304"):
                opp_val = getattr(value, "FSMInstructions_PosConditionExpressionElement304", None)
                setattr(value, "FSMInstructions_PosConditionExpressionElement304", self)

class HALL_FSMInstructions_DomainPropertyGet(PosConditionExpressionElement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class HALL_FSMInstructions_GetState(PosConditionExpressionElement):

    pass
class HALL_FSMInstructions_Literal(PosConditionExpressionElement):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class HALL_FSMInstructions_UnaryOperator(PosConditionExpressionElement):

    def __init__(self, operatorname: str, HALL_FSMInstructions_UnaryOperator: "FSMInstructions_PosConditionExpressionElement" = None):
        self.operatorname = operatorname
        self.HALL_FSMInstructions_UnaryOperator = HALL_FSMInstructions_UnaryOperator
        
    @property
    def operatorname(self) -> str:
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
            if hasattr(old_value, "FSMInstructions_PosConditionExpressionElement292"):
                opp_val = getattr(old_value, "FSMInstructions_PosConditionExpressionElement292", None)
                if opp_val == self:
                    setattr(old_value, "FSMInstructions_PosConditionExpressionElement292", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMInstructions_PosConditionExpressionElement292"):
                opp_val = getattr(value, "FSMInstructions_PosConditionExpressionElement292", None)
                setattr(value, "FSMInstructions_PosConditionExpressionElement292", self)

class HALL_FSMInstructions_SetState(PosConditionExpressionElement):

    def __init__(self, name: str, HALL_FSMInstructions_SetState: "FSMInstructions_HALL_Component" = None):
        self.name = name
        self.HALL_FSMInstructions_SetState = HALL_FSMInstructions_SetState
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def HALL_FSMInstructions_SetState(self):
        return self.__HALL_FSMInstructions_SetState

    @HALL_FSMInstructions_SetState.setter
    def HALL_FSMInstructions_SetState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMInstructions_SetState__HALL_FSMInstructions_SetState", None)
        self.__HALL_FSMInstructions_SetState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMInstructions_HALL_Component297"):
                opp_val = getattr(old_value, "FSMInstructions_HALL_Component297", None)
                if opp_val == self:
                    setattr(old_value, "FSMInstructions_HALL_Component297", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMInstructions_HALL_Component297"):
                opp_val = getattr(value, "FSMInstructions_HALL_Component297", None)
                setattr(value, "FSMInstructions_HALL_Component297", self)

class HALL_FSMInstructions_GetData(PosConditionExpressionElement):

    def __init__(self, field: str, HALL_FSMInstructions_GetData: "FSMInstructions_HALL_Component" = None):
        self.field = field
        self.HALL_FSMInstructions_GetData = HALL_FSMInstructions_GetData
        
    @property
    def field(self) -> str:
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

class HALL_FSMInstructions_BinaryOperator(PosConditionExpressionElement):

    def __init__(self, operatorname: str, HALL_FSMInstructions_BinaryOperator: "FSMInstructions_PosConditionExpressionElement" = None, HALL_FSMInstructions_BinaryOperator289: "FSMInstructions_PosConditionExpressionElement" = None):
        self.operatorname = operatorname
        self.HALL_FSMInstructions_BinaryOperator = HALL_FSMInstructions_BinaryOperator
        self.HALL_FSMInstructions_BinaryOperator289 = HALL_FSMInstructions_BinaryOperator289
        
    @property
    def operatorname(self) -> str:
        return self.__operatorname

    @operatorname.setter
    def operatorname(self, operatorname: str):
        self.__operatorname = operatorname

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
            if hasattr(old_value, "FSMInstructions_PosConditionExpressionElement"):
                opp_val = getattr(old_value, "FSMInstructions_PosConditionExpressionElement", None)
                if opp_val == self:
                    setattr(old_value, "FSMInstructions_PosConditionExpressionElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMInstructions_PosConditionExpressionElement"):
                opp_val = getattr(value, "FSMInstructions_PosConditionExpressionElement", None)
                setattr(value, "FSMInstructions_PosConditionExpressionElement", self)

    @property
    def HALL_FSMInstructions_BinaryOperator289(self):
        return self.__HALL_FSMInstructions_BinaryOperator289

    @HALL_FSMInstructions_BinaryOperator289.setter
    def HALL_FSMInstructions_BinaryOperator289(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMInstructions_BinaryOperator__HALL_FSMInstructions_BinaryOperator289", None)
        self.__HALL_FSMInstructions_BinaryOperator289 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMInstructions_PosConditionExpressionElement290"):
                opp_val = getattr(old_value, "FSMInstructions_PosConditionExpressionElement290", None)
                if opp_val == self:
                    setattr(old_value, "FSMInstructions_PosConditionExpressionElement290", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMInstructions_PosConditionExpressionElement290"):
                opp_val = getattr(value, "FSMInstructions_PosConditionExpressionElement290", None)
                setattr(value, "FSMInstructions_PosConditionExpressionElement290", self)

class HALL_FSMInstructions_VarRef(PosConditionExpressionElement):

    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class HALL_FSMInstructions_PosConditionExpressionElement(ABC):

    pass
class FSMInstructions_PosConditionExpressionElement:

    pass
class HALL_FSMInstructions_PosConditionExpression(ABC):

    pass
class TriggerExpressionElement:

    pass
class HALL_Trigger_DomainEventFired(TriggerExpressionElement):

    pass
class HALL_Trigger_MessageNotification(TriggerExpressionElement):

    pass
class HALL_Trigger_TriggerExpressionElement(ABC):

    def __init__(self, String: str, Trigger276: "Trigger_TriggerExpression" = None):
        self.String = String
        self.Trigger276 = Trigger276
        
    @property
    def String(self) -> str:
        return self.__String

    @String.setter
    def String(self, String: str):
        self.__String = String

    @property
    def Trigger276(self):
        return self.__Trigger276

    @Trigger276.setter
    def Trigger276(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Trigger_TriggerExpressionElement__Trigger276", None)
        self.__Trigger276 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM277"):
                opp_val = getattr(old_value, "FSM277", None)
                if opp_val == self:
                    setattr(old_value, "FSM277", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM277"):
                opp_val = getattr(value, "FSM277", None)
                setattr(value, "FSM277", self)

class Actions_HALL_Component:

    pass
class HALL_FSM_Transition:

    def __init__(self, name: str, State: "State" = None, HALL_FSM_Transition: "State" = None, FSMConditions: "FSMConditions_PreConditionExpression" = None, FSMInstructions: "FSMInstructions_PosConditionExpression" = None, FSMActions: "FSMActions_ActionExpression" = None, Trigger: "Trigger_TriggerExpression" = None):
        self.name = name
        self.State = State
        self.HALL_FSM_Transition = HALL_FSM_Transition
        self.FSMConditions = FSMConditions
        self.FSMInstructions = FSMInstructions
        self.FSMActions = FSMActions
        self.Trigger = Trigger
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def FSMActions(self):
        return self.__FSMActions

    @FSMActions.setter
    def FSMActions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSM_Transition__FSMActions", None)
        self.__FSMActions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM264"):
                opp_val = getattr(old_value, "FSM264", None)
                if opp_val == self:
                    setattr(old_value, "FSM264", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM264"):
                opp_val = getattr(value, "FSM264", None)
                setattr(value, "FSM264", self)

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSM_Transition__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM256"):
                opp_val = getattr(old_value, "FSM256", None)
                if opp_val == self:
                    setattr(old_value, "FSM256", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM256"):
                opp_val = getattr(value, "FSM256", None)
                setattr(value, "FSM256", self)

    @property
    def FSMInstructions(self):
        return self.__FSMInstructions

    @FSMInstructions.setter
    def FSMInstructions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSM_Transition__FSMInstructions", None)
        self.__FSMInstructions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM262"):
                opp_val = getattr(old_value, "FSM262", None)
                if opp_val == self:
                    setattr(old_value, "FSM262", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM262"):
                opp_val = getattr(value, "FSM262", None)
                setattr(value, "FSM262", self)

    @property
    def Trigger(self):
        return self.__Trigger

    @Trigger.setter
    def Trigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSM_Transition__Trigger", None)
        self.__Trigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM266"):
                opp_val = getattr(old_value, "FSM266", None)
                if opp_val == self:
                    setattr(old_value, "FSM266", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM266"):
                opp_val = getattr(value, "FSM266", None)
                setattr(value, "FSM266", self)

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
            if hasattr(old_value, "State258"):
                opp_val = getattr(old_value, "State258", None)
                if opp_val == self:
                    setattr(old_value, "State258", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State258"):
                opp_val = getattr(value, "State258", None)
                setattr(value, "State258", self)

    @property
    def FSMConditions(self):
        return self.__FSMConditions

    @FSMConditions.setter
    def FSMConditions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSM_Transition__FSMConditions", None)
        self.__FSMConditions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM260"):
                opp_val = getattr(old_value, "FSM260", None)
                if opp_val == self:
                    setattr(old_value, "FSM260", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM260"):
                opp_val = getattr(value, "FSM260", None)
                setattr(value, "FSM260", self)

class State:

    pass
class HALL_FSM_InitialState(State):

    pass
class HALL_FSM_NamedState(State):

    def __init__(self, name: str, FSM250: "FSM" = None, State258: "HALL_FSM_Transition", FSM256: "HALL_FSM_Transition"):
        self.name = name
        self.FSM250 = FSM250
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def FSM250(self):
        return self.__FSM250

    @FSM250.setter
    def FSM250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSM_NamedState__FSM250", None)
        self.__FSM250 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM251"):
                opp_val = getattr(old_value, "FSM251", None)
                if opp_val == self:
                    setattr(old_value, "FSM251", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM251"):
                opp_val = getattr(value, "FSM251", None)
                setattr(value, "FSM251", self)

class NamedState:

    pass
class InitialState:

    pass
class FSM_HALL_Component:

    pass
class HALL_FSM_FSM:

    pass
class ActionMessageExpressionElement:

    pass
class HALL_Actions_GetData(ActionMessageExpressionElement):

    def __init__(self, field: str, HALL_Actions_GetData: "Actions_HALL_Component" = None):
        self.field = field
        self.HALL_Actions_GetData = HALL_Actions_GetData
        
    @property
    def field(self) -> str:
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field

    @property
    def HALL_Actions_GetData(self):
        return self.__HALL_Actions_GetData

    @HALL_Actions_GetData.setter
    def HALL_Actions_GetData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Actions_GetData__HALL_Actions_GetData", None)
        self.__HALL_Actions_GetData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Actions_HALL_Component"):
                opp_val = getattr(old_value, "Actions_HALL_Component", None)
                if opp_val == self:
                    setattr(old_value, "Actions_HALL_Component", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Actions_HALL_Component"):
                opp_val = getattr(value, "Actions_HALL_Component", None)
                setattr(value, "Actions_HALL_Component", self)

class HALL_Actions_Literal(ActionMessageExpressionElement):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class HALL_FSMActions_Enable(ActionMessageExpressionElement):

    pass
class HALL_Actions_UnaryOperator(ActionMessageExpressionElement):

    def __init__(self, operatorname: str, HALL_Actions_UnaryOperator: "Actions_ActionMessageExpressionElement" = None):
        self.operatorname = operatorname
        self.HALL_Actions_UnaryOperator = HALL_Actions_UnaryOperator
        
    @property
    def operatorname(self) -> str:
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
            if hasattr(old_value, "Actions_ActionMessageExpressionElement233"):
                opp_val = getattr(old_value, "Actions_ActionMessageExpressionElement233", None)
                if opp_val == self:
                    setattr(old_value, "Actions_ActionMessageExpressionElement233", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Actions_ActionMessageExpressionElement233"):
                opp_val = getattr(value, "Actions_ActionMessageExpressionElement233", None)
                setattr(value, "Actions_ActionMessageExpressionElement233", self)

class HALL_Actions_MessageInvocation(ActionMessageExpressionElement):

    def __init__(self, name: str, isTopDown: bool, HALL_Actions_MessageInvocation: "Actions_ActionMessageExpressionElement" = None):
        self.name = name
        self.isTopDown = isTopDown
        self.HALL_Actions_MessageInvocation = HALL_Actions_MessageInvocation
        
    @property
    def isTopDown(self) -> bool:
        return self.__isTopDown

    @isTopDown.setter
    def isTopDown(self, isTopDown: bool):
        self.__isTopDown = isTopDown

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "Actions_ActionMessageExpressionElement231"):
                opp_val = getattr(old_value, "Actions_ActionMessageExpressionElement231", None)
                if opp_val == self:
                    setattr(old_value, "Actions_ActionMessageExpressionElement231", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Actions_ActionMessageExpressionElement231"):
                opp_val = getattr(value, "Actions_ActionMessageExpressionElement231", None)
                setattr(value, "Actions_ActionMessageExpressionElement231", self)

class HALL_Actions_DomainPropertySet(ActionMessageExpressionElement):

    def __init__(self, name: str, HALL_Actions_DomainPropertySet: "Actions_ActionMessageExpressionElement" = None):
        self.name = name
        self.HALL_Actions_DomainPropertySet = HALL_Actions_DomainPropertySet
        
    @property
    def name(self) -> str:
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
            if hasattr(old_value, "Actions_ActionMessageExpressionElement236"):
                opp_val = getattr(old_value, "Actions_ActionMessageExpressionElement236", None)
                if opp_val == self:
                    setattr(old_value, "Actions_ActionMessageExpressionElement236", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Actions_ActionMessageExpressionElement236"):
                opp_val = getattr(value, "Actions_ActionMessageExpressionElement236", None)
                setattr(value, "Actions_ActionMessageExpressionElement236", self)

class HALL_Actions_BinaryOperator(ActionMessageExpressionElement):

    def __init__(self, operatorname: str, HALL_Actions_BinaryOperator: "Actions_ActionMessageExpressionElement" = None, HALL_Actions_BinaryOperator223: "Actions_ActionMessageExpressionElement" = None):
        self.operatorname = operatorname
        self.HALL_Actions_BinaryOperator = HALL_Actions_BinaryOperator
        self.HALL_Actions_BinaryOperator223 = HALL_Actions_BinaryOperator223
        
    @property
    def operatorname(self) -> str:
        return self.__operatorname

    @operatorname.setter
    def operatorname(self, operatorname: str):
        self.__operatorname = operatorname

    @property
    def HALL_Actions_BinaryOperator223(self):
        return self.__HALL_Actions_BinaryOperator223

    @HALL_Actions_BinaryOperator223.setter
    def HALL_Actions_BinaryOperator223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Actions_BinaryOperator__HALL_Actions_BinaryOperator223", None)
        self.__HALL_Actions_BinaryOperator223 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Actions_ActionMessageExpressionElement224"):
                opp_val = getattr(old_value, "Actions_ActionMessageExpressionElement224", None)
                if opp_val == self:
                    setattr(old_value, "Actions_ActionMessageExpressionElement224", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Actions_ActionMessageExpressionElement224"):
                opp_val = getattr(value, "Actions_ActionMessageExpressionElement224", None)
                setattr(value, "Actions_ActionMessageExpressionElement224", self)

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
            if hasattr(old_value, "Actions_ActionMessageExpressionElement"):
                opp_val = getattr(old_value, "Actions_ActionMessageExpressionElement", None)
                if opp_val == self:
                    setattr(old_value, "Actions_ActionMessageExpressionElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Actions_ActionMessageExpressionElement"):
                opp_val = getattr(value, "Actions_ActionMessageExpressionElement", None)
                setattr(value, "Actions_ActionMessageExpressionElement", self)

class HALL_Actions_Enable(ActionMessageExpressionElement):

    pass
class HALL_Actions_VarRef(ActionMessageExpressionElement):

    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class HALL_Actions_ActionMessageExpressionElement(ABC):

    pass
class Actions_ActionMessageExpressionElement:

    pass
class HALL_Actions_ActionMessageExpression(ABC):

    pass
class HALL_Actions_GetMessageParameter(ActionMessageExpressionElement):

    def __init__(self, field: str):
        self.field = field
        
    @property
    def field(self) -> str:
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field

class HALL_Actions_GetMessageData(ActionMessageExpressionElement):

    def __init__(self, field: str):
        self.field = field
        
    @property
    def field(self) -> str:
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field

class HALL_Actions_DomainPropertyGet(ActionMessageExpressionElement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class HALL_Actions_Let(ActionMessageExpressionElement):

    def __init__(self, namevar: str, HALL_Actions_Let: "Actions_ActionMessageExpressionElement" = None, HALL_Actions_Let228: "Actions_ActionMessageExpressionElement" = None):
        self.namevar = namevar
        self.HALL_Actions_Let = HALL_Actions_Let
        self.HALL_Actions_Let228 = HALL_Actions_Let228
        
    @property
    def namevar(self) -> str:
        return self.__namevar

    @namevar.setter
    def namevar(self, namevar: str):
        self.__namevar = namevar

    @property
    def HALL_Actions_Let(self):
        return self.__HALL_Actions_Let

    @HALL_Actions_Let.setter
    def HALL_Actions_Let(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Actions_Let__HALL_Actions_Let", None)
        self.__HALL_Actions_Let = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Actions_ActionMessageExpressionElement226"):
                opp_val = getattr(old_value, "Actions_ActionMessageExpressionElement226", None)
                if opp_val == self:
                    setattr(old_value, "Actions_ActionMessageExpressionElement226", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Actions_ActionMessageExpressionElement226"):
                opp_val = getattr(value, "Actions_ActionMessageExpressionElement226", None)
                setattr(value, "Actions_ActionMessageExpressionElement226", self)

    @property
    def HALL_Actions_Let228(self):
        return self.__HALL_Actions_Let228

    @HALL_Actions_Let228.setter
    def HALL_Actions_Let228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Actions_Let__HALL_Actions_Let228", None)
        self.__HALL_Actions_Let228 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Actions_ActionMessageExpressionElement229"):
                opp_val = getattr(old_value, "Actions_ActionMessageExpressionElement229", None)
                if opp_val == self:
                    setattr(old_value, "Actions_ActionMessageExpressionElement229", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Actions_ActionMessageExpressionElement229"):
                opp_val = getattr(value, "Actions_ActionMessageExpressionElement229", None)
                setattr(value, "Actions_ActionMessageExpressionElement229", self)

class PreConditionMessageExpressionElement:

    pass
class HALL_Conditions_Literal(PreConditionMessageExpressionElement):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class HALL_Conditions_GetState(PreConditionMessageExpressionElement):

    pass
class HALL_Conditions_GetMessageData(PreConditionMessageExpressionElement):

    def __init__(self, field: str):
        self.field = field
        
    @property
    def field(self) -> str:
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field

class HALL_Conditions_DomainPropertyGet(PreConditionMessageExpressionElement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class HALL_Conditions_GetMessageParameter(PreConditionMessageExpressionElement):

    def __init__(self, field: str):
        self.field = field
        
    @property
    def field(self) -> str:
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field

class HALL_Conditions_VarRef(PreConditionMessageExpressionElement):

    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class HALL_Conditions_PreConditionMessageExpressionElement(ABC):

    pass
class Conditions_PreConditionMessageExpressionElement:

    pass
class HALL_Conditions_PreConditionMessageExpression(ABC):

    pass
class HALL_Conditions_BinaryOperator(PreConditionMessageExpressionElement):

    def __init__(self, operatorname: str, HALL_Conditions_BinaryOperator: "Conditions_PreConditionMessageExpressionElement" = None, HALL_Conditions_BinaryOperator210: "Conditions_PreConditionMessageExpressionElement" = None):
        self.operatorname = operatorname
        self.HALL_Conditions_BinaryOperator = HALL_Conditions_BinaryOperator
        self.HALL_Conditions_BinaryOperator210 = HALL_Conditions_BinaryOperator210
        
    @property
    def operatorname(self) -> str:
        return self.__operatorname

    @operatorname.setter
    def operatorname(self, operatorname: str):
        self.__operatorname = operatorname

    @property
    def HALL_Conditions_BinaryOperator210(self):
        return self.__HALL_Conditions_BinaryOperator210

    @HALL_Conditions_BinaryOperator210.setter
    def HALL_Conditions_BinaryOperator210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Conditions_BinaryOperator__HALL_Conditions_BinaryOperator210", None)
        self.__HALL_Conditions_BinaryOperator210 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Conditions_PreConditionMessageExpressionElement211"):
                opp_val = getattr(old_value, "Conditions_PreConditionMessageExpressionElement211", None)
                if opp_val == self:
                    setattr(old_value, "Conditions_PreConditionMessageExpressionElement211", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Conditions_PreConditionMessageExpressionElement211"):
                opp_val = getattr(value, "Conditions_PreConditionMessageExpressionElement211", None)
                setattr(value, "Conditions_PreConditionMessageExpressionElement211", self)

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
            if hasattr(old_value, "Conditions_PreConditionMessageExpressionElement208"):
                opp_val = getattr(old_value, "Conditions_PreConditionMessageExpressionElement208", None)
                if opp_val == self:
                    setattr(old_value, "Conditions_PreConditionMessageExpressionElement208", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Conditions_PreConditionMessageExpressionElement208"):
                opp_val = getattr(value, "Conditions_PreConditionMessageExpressionElement208", None)
                setattr(value, "Conditions_PreConditionMessageExpressionElement208", self)

class HALL_Conditions_UnaryOperator(PreConditionMessageExpressionElement):

    def __init__(self, operatorname: str, HALL_Conditions_UnaryOperator: "Conditions_PreConditionMessageExpressionElement" = None):
        self.operatorname = operatorname
        self.HALL_Conditions_UnaryOperator = HALL_Conditions_UnaryOperator
        
    @property
    def operatorname(self) -> str:
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
            if hasattr(old_value, "Conditions_PreConditionMessageExpressionElement206"):
                opp_val = getattr(old_value, "Conditions_PreConditionMessageExpressionElement206", None)
                if opp_val == self:
                    setattr(old_value, "Conditions_PreConditionMessageExpressionElement206", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Conditions_PreConditionMessageExpressionElement206"):
                opp_val = getattr(value, "Conditions_PreConditionMessageExpressionElement206", None)
                setattr(value, "Conditions_PreConditionMessageExpressionElement206", self)

class HALL_Conditions_Let(PreConditionMessageExpressionElement):

    def __init__(self, namevar: str, HALL_Conditions_Let: "Conditions_PreConditionMessageExpressionElement" = None, HALL_Conditions_Let203: "Conditions_PreConditionMessageExpressionElement" = None):
        self.namevar = namevar
        self.HALL_Conditions_Let = HALL_Conditions_Let
        self.HALL_Conditions_Let203 = HALL_Conditions_Let203
        
    @property
    def namevar(self) -> str:
        return self.__namevar

    @namevar.setter
    def namevar(self, namevar: str):
        self.__namevar = namevar

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
            if hasattr(old_value, "Conditions_PreConditionMessageExpressionElement"):
                opp_val = getattr(old_value, "Conditions_PreConditionMessageExpressionElement", None)
                if opp_val == self:
                    setattr(old_value, "Conditions_PreConditionMessageExpressionElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Conditions_PreConditionMessageExpressionElement"):
                opp_val = getattr(value, "Conditions_PreConditionMessageExpressionElement", None)
                setattr(value, "Conditions_PreConditionMessageExpressionElement", self)

    @property
    def HALL_Conditions_Let203(self):
        return self.__HALL_Conditions_Let203

    @HALL_Conditions_Let203.setter
    def HALL_Conditions_Let203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Conditions_Let__HALL_Conditions_Let203", None)
        self.__HALL_Conditions_Let203 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Conditions_PreConditionMessageExpressionElement204"):
                opp_val = getattr(old_value, "Conditions_PreConditionMessageExpressionElement204", None)
                if opp_val == self:
                    setattr(old_value, "Conditions_PreConditionMessageExpressionElement204", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Conditions_PreConditionMessageExpressionElement204"):
                opp_val = getattr(value, "Conditions_PreConditionMessageExpressionElement204", None)
                setattr(value, "Conditions_PreConditionMessageExpressionElement204", self)

class HALL_Conditions_GetData(PreConditionMessageExpressionElement):

    def __init__(self, field: str, HALL_Conditions_GetData: "Conditions_HALL_Component" = None):
        self.field = field
        self.HALL_Conditions_GetData = HALL_Conditions_GetData
        
    @property
    def field(self) -> str:
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field

    @property
    def HALL_Conditions_GetData(self):
        return self.__HALL_Conditions_GetData

    @HALL_Conditions_GetData.setter
    def HALL_Conditions_GetData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Conditions_GetData__HALL_Conditions_GetData", None)
        self.__HALL_Conditions_GetData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Conditions_HALL_Component200"):
                opp_val = getattr(old_value, "Conditions_HALL_Component200", None)
                if opp_val == self:
                    setattr(old_value, "Conditions_HALL_Component200", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Conditions_HALL_Component200"):
                opp_val = getattr(value, "Conditions_HALL_Component200", None)
                setattr(value, "Conditions_HALL_Component200", self)

class Conditions_HALL_Component:

    pass
class Instructions_HALL_Component:

    pass
class HALL_Instructions_PosConditionMessageExpressionElement(ABC):

    pass
class Instructions_PosConditionMessageExpressionElement:

    pass
class HALL_Instructions_PosConditionMessageExpression(ABC):

    pass
class MessageTransition:

    pass
class HALL_Messages_MessageState:

    def __init__(self, isEnd: bool, isContinue: bool, isActive: bool, MessageTransition: set["MessageTransition"] = None):
        self.isEnd = isEnd
        self.isContinue = isContinue
        self.isActive = isActive
        self.MessageTransition = MessageTransition if MessageTransition is not None else set()
        
    @property
    def isContinue(self) -> bool:
        return self.__isContinue

    @isContinue.setter
    def isContinue(self, isContinue: bool):
        self.__isContinue = isContinue

    @property
    def isActive(self) -> bool:
        return self.__isActive

    @isActive.setter
    def isActive(self, isActive: bool):
        self.__isActive = isActive

    @property
    def isEnd(self) -> bool:
        return self.__isEnd

    @isEnd.setter
    def isEnd(self, isEnd: bool):
        self.__isEnd = isEnd

    @property
    def MessageTransition(self):
        return self.__MessageTransition

    @MessageTransition.setter
    def MessageTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Messages_MessageState__MessageTransition", None)
        self.__MessageTransition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Messages149"):
                    opp_val = getattr(item, "Messages149", None)
                    
                    if opp_val == self:
                        setattr(item, "Messages149", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Messages149"):
                    opp_val = getattr(item, "Messages149", None)
                    
                    setattr(item, "Messages149", self)
                    

class Messages_HALL_Component:

    pass
class InitialMessageState:

    pass
class NamedMessageState:

    pass
class PosConditionMessageExpressionElement:

    pass
class HALL_Instructions_SetData(PosConditionMessageExpressionElement):

    def __init__(self, field: str, HALL_Instructions_SetData: "Instructions_PosConditionMessageExpressionElement" = None, HALL_Instructions_SetData176: "Instructions_HALL_Component" = None):
        self.field = field
        self.HALL_Instructions_SetData = HALL_Instructions_SetData
        self.HALL_Instructions_SetData176 = HALL_Instructions_SetData176
        
    @property
    def field(self) -> str:
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field

    @property
    def HALL_Instructions_SetData(self):
        return self.__HALL_Instructions_SetData

    @HALL_Instructions_SetData.setter
    def HALL_Instructions_SetData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Instructions_SetData__HALL_Instructions_SetData", None)
        self.__HALL_Instructions_SetData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Instructions_PosConditionMessageExpressionElement174"):
                opp_val = getattr(old_value, "Instructions_PosConditionMessageExpressionElement174", None)
                if opp_val == self:
                    setattr(old_value, "Instructions_PosConditionMessageExpressionElement174", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instructions_PosConditionMessageExpressionElement174"):
                opp_val = getattr(value, "Instructions_PosConditionMessageExpressionElement174", None)
                setattr(value, "Instructions_PosConditionMessageExpressionElement174", self)

    @property
    def HALL_Instructions_SetData176(self):
        return self.__HALL_Instructions_SetData176

    @HALL_Instructions_SetData176.setter
    def HALL_Instructions_SetData176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Instructions_SetData__HALL_Instructions_SetData176", None)
        self.__HALL_Instructions_SetData176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Instructions_HALL_Component177"):
                opp_val = getattr(old_value, "Instructions_HALL_Component177", None)
                if opp_val == self:
                    setattr(old_value, "Instructions_HALL_Component177", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instructions_HALL_Component177"):
                opp_val = getattr(value, "Instructions_HALL_Component177", None)
                setattr(value, "Instructions_HALL_Component177", self)

class HALL_Instructions_Let(PosConditionMessageExpressionElement):

    def __init__(self, namevar: str, HALL_Instructions_Let: "Instructions_PosConditionMessageExpressionElement" = None, HALL_Instructions_Let185: "Instructions_PosConditionMessageExpressionElement" = None):
        self.namevar = namevar
        self.HALL_Instructions_Let = HALL_Instructions_Let
        self.HALL_Instructions_Let185 = HALL_Instructions_Let185
        
    @property
    def namevar(self) -> str:
        return self.__namevar

    @namevar.setter
    def namevar(self, namevar: str):
        self.__namevar = namevar

    @property
    def HALL_Instructions_Let185(self):
        return self.__HALL_Instructions_Let185

    @HALL_Instructions_Let185.setter
    def HALL_Instructions_Let185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Instructions_Let__HALL_Instructions_Let185", None)
        self.__HALL_Instructions_Let185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Instructions_PosConditionMessageExpressionElement186"):
                opp_val = getattr(old_value, "Instructions_PosConditionMessageExpressionElement186", None)
                if opp_val == self:
                    setattr(old_value, "Instructions_PosConditionMessageExpressionElement186", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instructions_PosConditionMessageExpressionElement186"):
                opp_val = getattr(value, "Instructions_PosConditionMessageExpressionElement186", None)
                setattr(value, "Instructions_PosConditionMessageExpressionElement186", self)

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
            if hasattr(old_value, "Instructions_PosConditionMessageExpressionElement183"):
                opp_val = getattr(old_value, "Instructions_PosConditionMessageExpressionElement183", None)
                if opp_val == self:
                    setattr(old_value, "Instructions_PosConditionMessageExpressionElement183", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instructions_PosConditionMessageExpressionElement183"):
                opp_val = getattr(value, "Instructions_PosConditionMessageExpressionElement183", None)
                setattr(value, "Instructions_PosConditionMessageExpressionElement183", self)

class HALL_Instructions_Literal(PosConditionMessageExpressionElement):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class HALL_Instructions_SetMessageData(PosConditionMessageExpressionElement):

    def __init__(self, field: str, HALL_Instructions_SetMessageData: "Instructions_PosConditionMessageExpressionElement" = None):
        self.field = field
        self.HALL_Instructions_SetMessageData = HALL_Instructions_SetMessageData
        
    @property
    def field(self) -> str:
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
            if hasattr(old_value, "Instructions_PosConditionMessageExpressionElement179"):
                opp_val = getattr(old_value, "Instructions_PosConditionMessageExpressionElement179", None)
                if opp_val == self:
                    setattr(old_value, "Instructions_PosConditionMessageExpressionElement179", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instructions_PosConditionMessageExpressionElement179"):
                opp_val = getattr(value, "Instructions_PosConditionMessageExpressionElement179", None)
                setattr(value, "Instructions_PosConditionMessageExpressionElement179", self)

class HALL_Instructions_GetState(PosConditionMessageExpressionElement):

    pass
class HALL_Instructions_DomainPropertyGet(PosConditionMessageExpressionElement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class HALL_Instructions_SetMessageParameter(PosConditionMessageExpressionElement):

    def __init__(self, field: str, HALL_Instructions_SetMessageParameter: "Instructions_PosConditionMessageExpressionElement" = None):
        self.field = field
        self.HALL_Instructions_SetMessageParameter = HALL_Instructions_SetMessageParameter
        
    @property
    def field(self) -> str:
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
            if hasattr(old_value, "Instructions_PosConditionMessageExpressionElement181"):
                opp_val = getattr(old_value, "Instructions_PosConditionMessageExpressionElement181", None)
                if opp_val == self:
                    setattr(old_value, "Instructions_PosConditionMessageExpressionElement181", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instructions_PosConditionMessageExpressionElement181"):
                opp_val = getattr(value, "Instructions_PosConditionMessageExpressionElement181", None)
                setattr(value, "Instructions_PosConditionMessageExpressionElement181", self)

class HALL_Instructions_UnaryOperator(PosConditionMessageExpressionElement):

    def __init__(self, operatorname: str, HALL_Instructions_UnaryOperator: "Instructions_PosConditionMessageExpressionElement" = None):
        self.operatorname = operatorname
        self.HALL_Instructions_UnaryOperator = HALL_Instructions_UnaryOperator
        
    @property
    def operatorname(self) -> str:
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
            if hasattr(old_value, "Instructions_PosConditionMessageExpressionElement167"):
                opp_val = getattr(old_value, "Instructions_PosConditionMessageExpressionElement167", None)
                if opp_val == self:
                    setattr(old_value, "Instructions_PosConditionMessageExpressionElement167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instructions_PosConditionMessageExpressionElement167"):
                opp_val = getattr(value, "Instructions_PosConditionMessageExpressionElement167", None)
                setattr(value, "Instructions_PosConditionMessageExpressionElement167", self)

class HALL_Instructions_GetData(PosConditionMessageExpressionElement):

    def __init__(self, field: str, HALL_Instructions_GetData: "Instructions_HALL_Component" = None):
        self.field = field
        self.HALL_Instructions_GetData = HALL_Instructions_GetData
        
    @property
    def field(self) -> str:
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field

    @property
    def HALL_Instructions_GetData(self):
        return self.__HALL_Instructions_GetData

    @HALL_Instructions_GetData.setter
    def HALL_Instructions_GetData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Instructions_GetData__HALL_Instructions_GetData", None)
        self.__HALL_Instructions_GetData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Instructions_HALL_Component"):
                opp_val = getattr(old_value, "Instructions_HALL_Component", None)
                if opp_val == self:
                    setattr(old_value, "Instructions_HALL_Component", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instructions_HALL_Component"):
                opp_val = getattr(value, "Instructions_HALL_Component", None)
                setattr(value, "Instructions_HALL_Component", self)

class HALL_Instructions_BinaryOperator(PosConditionMessageExpressionElement):

    def __init__(self, operatorname: str, HALL_Instructions_BinaryOperator: "Instructions_PosConditionMessageExpressionElement" = None, HALL_Instructions_BinaryOperator164: "Instructions_PosConditionMessageExpressionElement" = None):
        self.operatorname = operatorname
        self.HALL_Instructions_BinaryOperator = HALL_Instructions_BinaryOperator
        self.HALL_Instructions_BinaryOperator164 = HALL_Instructions_BinaryOperator164
        
    @property
    def operatorname(self) -> str:
        return self.__operatorname

    @operatorname.setter
    def operatorname(self, operatorname: str):
        self.__operatorname = operatorname

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
            if hasattr(old_value, "Instructions_PosConditionMessageExpressionElement"):
                opp_val = getattr(old_value, "Instructions_PosConditionMessageExpressionElement", None)
                if opp_val == self:
                    setattr(old_value, "Instructions_PosConditionMessageExpressionElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instructions_PosConditionMessageExpressionElement"):
                opp_val = getattr(value, "Instructions_PosConditionMessageExpressionElement", None)
                setattr(value, "Instructions_PosConditionMessageExpressionElement", self)

    @property
    def HALL_Instructions_BinaryOperator164(self):
        return self.__HALL_Instructions_BinaryOperator164

    @HALL_Instructions_BinaryOperator164.setter
    def HALL_Instructions_BinaryOperator164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Instructions_BinaryOperator__HALL_Instructions_BinaryOperator164", None)
        self.__HALL_Instructions_BinaryOperator164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Instructions_PosConditionMessageExpressionElement165"):
                opp_val = getattr(old_value, "Instructions_PosConditionMessageExpressionElement165", None)
                if opp_val == self:
                    setattr(old_value, "Instructions_PosConditionMessageExpressionElement165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instructions_PosConditionMessageExpressionElement165"):
                opp_val = getattr(value, "Instructions_PosConditionMessageExpressionElement165", None)
                setattr(value, "Instructions_PosConditionMessageExpressionElement165", self)

class HALL_Instructions_SetTopDown(PosConditionMessageExpressionElement):

    pass
class HALL_Instructions_SetState(PosConditionMessageExpressionElement):

    def __init__(self, name: str, HALL_Instructions_SetState: "Instructions_HALL_Component" = None):
        self.name = name
        self.HALL_Instructions_SetState = HALL_Instructions_SetState
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def HALL_Instructions_SetState(self):
        return self.__HALL_Instructions_SetState

    @HALL_Instructions_SetState.setter
    def HALL_Instructions_SetState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Instructions_SetState__HALL_Instructions_SetState", None)
        self.__HALL_Instructions_SetState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Instructions_HALL_Component172"):
                opp_val = getattr(old_value, "Instructions_HALL_Component172", None)
                if opp_val == self:
                    setattr(old_value, "Instructions_HALL_Component172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instructions_HALL_Component172"):
                opp_val = getattr(value, "Instructions_HALL_Component172", None)
                setattr(value, "Instructions_HALL_Component172", self)

class HALL_Instructions_GetMessageParameter(PosConditionMessageExpressionElement):

    def __init__(self, field: str):
        self.field = field
        
    @property
    def field(self) -> str:
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field

class HALL_Instructions_GetMessageData(PosConditionMessageExpressionElement):

    def __init__(self, field: str):
        self.field = field
        
    @property
    def field(self) -> str:
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field

class HALL_Instructions_VarRef(PosConditionMessageExpressionElement):

    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class Conditions_PreConditionMessageExpression:

    pass
class MessageState:

    pass
class HALL_Messages_InitialMessageState(MessageState):

    pass
class HALL_Messages_MessageTransition:

    def __init__(self, name: str, Instructions: "Instructions_PosConditionMessageExpression" = None, Actions: "Actions_ActionMessageExpression" = None, MessageState: "MessageState" = None, HALL_Messages_MessageTransition: "MessageState" = None, Conditions: "Conditions_PreConditionMessageExpression" = None):
        self.name = name
        self.Instructions = Instructions
        self.Actions = Actions
        self.MessageState = MessageState
        self.HALL_Messages_MessageTransition = HALL_Messages_MessageTransition
        self.Conditions = Conditions
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Actions(self):
        return self.__Actions

    @Actions.setter
    def Actions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Messages_MessageTransition__Actions", None)
        self.__Actions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Messages133"):
                opp_val = getattr(old_value, "Messages133", None)
                if opp_val == self:
                    setattr(old_value, "Messages133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Messages133"):
                opp_val = getattr(value, "Messages133", None)
                setattr(value, "Messages133", self)

    @property
    def MessageState(self):
        return self.__MessageState

    @MessageState.setter
    def MessageState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Messages_MessageTransition__MessageState", None)
        self.__MessageState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Messages125"):
                opp_val = getattr(old_value, "Messages125", None)
                if opp_val == self:
                    setattr(old_value, "Messages125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Messages125"):
                opp_val = getattr(value, "Messages125", None)
                setattr(value, "Messages125", self)

    @property
    def Instructions(self):
        return self.__Instructions

    @Instructions.setter
    def Instructions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Messages_MessageTransition__Instructions", None)
        self.__Instructions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Messages131"):
                opp_val = getattr(old_value, "Messages131", None)
                if opp_val == self:
                    setattr(old_value, "Messages131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Messages131"):
                opp_val = getattr(value, "Messages131", None)
                setattr(value, "Messages131", self)

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
            if hasattr(old_value, "MessageState127"):
                opp_val = getattr(old_value, "MessageState127", None)
                if opp_val == self:
                    setattr(old_value, "MessageState127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MessageState127"):
                opp_val = getattr(value, "MessageState127", None)
                setattr(value, "MessageState127", self)

    @property
    def Conditions(self):
        return self.__Conditions

    @Conditions.setter
    def Conditions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Messages_MessageTransition__Conditions", None)
        self.__Conditions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Messages129"):
                opp_val = getattr(old_value, "Messages129", None)
                if opp_val == self:
                    setattr(old_value, "Messages129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Messages129"):
                opp_val = getattr(value, "Messages129", None)
                setattr(value, "Messages129", self)

class HALL_Geometry_Point:

    def __init__(self, xCoord: int, yCoord: int):
        self.xCoord = xCoord
        self.yCoord = yCoord
        
    @property
    def xCoord(self) -> int:
        return self.__xCoord

    @xCoord.setter
    def xCoord(self, xCoord: int):
        self.__xCoord = xCoord

    @property
    def yCoord(self) -> int:
        return self.__yCoord

    @yCoord.setter
    def yCoord(self, yCoord: int):
        self.__yCoord = yCoord

class GeometryData2D:

    pass
class Point:

    pass
class HALL_Geometry_Point2D(Point):

    pass
class HALL_Geometry_Point3D(Point):

    def __init__(self, zCoord: int, Face120: "Face" = None):
        self.zCoord = zCoord
        self.Face120 = Face120
        
    @property
    def zCoord(self) -> int:
        return self.__zCoord

    @zCoord.setter
    def zCoord(self, zCoord: int):
        self.__zCoord = zCoord

    @property
    def Face120(self):
        return self.__Face120

    @Face120.setter
    def Face120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Geometry_Point3D__Face120", None)
        self.__Face120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Geometry121"):
                opp_val = getattr(old_value, "Geometry121", None)
                if opp_val == self:
                    setattr(old_value, "Geometry121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Geometry121"):
                opp_val = getattr(value, "Geometry121", None)
                setattr(value, "Geometry121", self)

class GeometryData3D:

    pass
class HALL_Messages_MessageHandler:

    def __init__(self, name: str, NamedMessageState: set["NamedMessageState"] = None, InitialMessageState: "InitialMessageState" = None, messageHandlerSet: "Messages_HALL_Component" = None):
        self.name = name
        self.NamedMessageState = NamedMessageState if NamedMessageState is not None else set()
        self.InitialMessageState = InitialMessageState
        self.messageHandlerSet = messageHandlerSet
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def messageHandlerSet(self):
        return self.__messageHandlerSet

    @messageHandlerSet.setter
    def messageHandlerSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Messages_MessageHandler__messageHandlerSet", None)
        self.__messageHandlerSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Component147"):
                opp_val = getattr(old_value, "Component147", None)
                if opp_val == self:
                    setattr(old_value, "Component147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Component147"):
                opp_val = getattr(value, "Component147", None)
                setattr(value, "Component147", self)

    @property
    def NamedMessageState(self):
        return self.__NamedMessageState

    @NamedMessageState.setter
    def NamedMessageState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Messages_MessageHandler__NamedMessageState", None)
        self.__NamedMessageState = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Messages143"):
                    opp_val = getattr(item, "Messages143", None)
                    
                    if opp_val == self:
                        setattr(item, "Messages143", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Messages143"):
                    opp_val = getattr(item, "Messages143", None)
                    
                    setattr(item, "Messages143", self)
                    

    @property
    def InitialMessageState(self):
        return self.__InitialMessageState

    @InitialMessageState.setter
    def InitialMessageState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Messages_MessageHandler__InitialMessageState", None)
        self.__InitialMessageState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Messages145"):
                opp_val = getattr(old_value, "Messages145", None)
                if opp_val == self:
                    setattr(old_value, "Messages145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Messages145"):
                opp_val = getattr(value, "Messages145", None)
                setattr(value, "Messages145", self)

class Messages_HALL_Data:

    pass
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
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "Model138"):
                opp_val = getattr(old_value, "Model138", None)
                if opp_val == self:
                    setattr(old_value, "Model138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model138"):
                opp_val = getattr(value, "Model138", None)
                setattr(value, "Model138", self)

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
                if hasattr(item, "Data141"):
                    opp_val = getattr(item, "Data141", None)
                    
                    if opp_val == self:
                        setattr(item, "Data141", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Data141"):
                    opp_val = getattr(item, "Data141", None)
                    
                    setattr(item, "Data141", self)
                    

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
                    

class HALL_Messages_NamedMessageState(MessageState):

    def __init__(self, name: str, MessageHandler135: "MessageHandler" = None, MessageState127: "HALL_Messages_MessageTransition", Messages125: "HALL_Messages_MessageTransition"):
        self.name = name
        self.MessageHandler135 = MessageHandler135
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MessageHandler135(self):
        return self.__MessageHandler135

    @MessageHandler135.setter
    def MessageHandler135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Messages_NamedMessageState__MessageHandler135", None)
        self.__MessageHandler135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Messages136"):
                opp_val = getattr(old_value, "Messages136", None)
                if opp_val == self:
                    setattr(old_value, "Messages136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Messages136"):
                opp_val = getattr(value, "Messages136", None)
                setattr(value, "Messages136", self)

class Actions_ActionMessageExpression:

    pass
class Instructions_PosConditionMessageExpression:

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
class HALL_Geometry_AlphaTransparency:

    def __init__(self, value: int, ColorState90: "ColorState" = None):
        self.value = value
        self.ColorState90 = ColorState90
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def ColorState90(self):
        return self.__ColorState90

    @ColorState90.setter
    def ColorState90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Geometry_AlphaTransparency__ColorState90", None)
        self.__ColorState90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Geometry91"):
                opp_val = getattr(old_value, "Geometry91", None)
                if opp_val == self:
                    setattr(old_value, "Geometry91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Geometry91"):
                opp_val = getattr(value, "Geometry91", None)
                setattr(value, "Geometry91", self)

class Point3D:

    pass
class HALL_Geometry_Face:

    def __init__(self, labelText: str, Point3D: set["Point3D"] = None, GeometryData3D: "GeometryData3D" = None):
        self.labelText = labelText
        self.Point3D = Point3D if Point3D is not None else set()
        self.GeometryData3D = GeometryData3D
        
    @property
    def labelText(self) -> str:
        return self.__labelText

    @labelText.setter
    def labelText(self, labelText: str):
        self.__labelText = labelText

    @property
    def Point3D(self):
        return self.__Point3D

    @Point3D.setter
    def Point3D(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Geometry_Face__Point3D", None)
        self.__Point3D = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Geometry116"):
                    opp_val = getattr(item, "Geometry116", None)
                    
                    if opp_val == self:
                        setattr(item, "Geometry116", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Geometry116"):
                    opp_val = getattr(item, "Geometry116", None)
                    
                    setattr(item, "Geometry116", self)
                    

    @property
    def GeometryData3D(self):
        return self.__GeometryData3D

    @GeometryData3D.setter
    def GeometryData3D(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Geometry_Face__GeometryData3D", None)
        self.__GeometryData3D = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Geometry118"):
                opp_val = getattr(old_value, "Geometry118", None)
                if opp_val == self:
                    setattr(old_value, "Geometry118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Geometry118"):
                opp_val = getattr(value, "Geometry118", None)
                setattr(value, "Geometry118", self)

class Point2D:

    pass
class Face:

    pass
class HALL_Geometry_GeometryData(ABC):

    pass
class ColorState:

    pass
class HALL_Geometry_DisabledColors(ColorState):

    pass
class HALL_Geometry_SelectedColors(ColorState):

    pass
class HALL_Geometry_NormalColors(ColorState):

    pass
class RGBColor:

    pass
class HALL_Geometry_Color:

    pass
class HALL_Parameter:

    def __init__(self, name: str, type: str, MessageDefinition54: "MessageDefinition" = None):
        self.name = name
        self.type = type
        self.MessageDefinition54 = MessageDefinition54
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MessageDefinition54(self):
        return self.__MessageDefinition54

    @MessageDefinition54.setter
    def MessageDefinition54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Parameter__MessageDefinition54", None)
        self.__MessageDefinition54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Messages55"):
                opp_val = getattr(old_value, "Messages55", None)
                if opp_val == self:
                    setattr(old_value, "Messages55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Messages55"):
                opp_val = getattr(value, "Messages55", None)
                setattr(value, "Messages55", self)

class AlphaTransparency:

    pass
class HALL_Geometry_ColorState(ABC):

    pass
class Color:

    pass
class HALL_Geometry_RGBColor:

    def __init__(self, redValue: int, greenValue: int, blueValue: int, Color: "Color" = None, Color76: "Color" = None, Color79: "Color" = None):
        self.redValue = redValue
        self.greenValue = greenValue
        self.blueValue = blueValue
        self.Color = Color
        self.Color76 = Color76
        self.Color79 = Color79
        
    @property
    def redValue(self) -> int:
        return self.__redValue

    @redValue.setter
    def redValue(self, redValue: int):
        self.__redValue = redValue

    @property
    def blueValue(self) -> int:
        return self.__blueValue

    @blueValue.setter
    def blueValue(self, blueValue: int):
        self.__blueValue = blueValue

    @property
    def greenValue(self) -> int:
        return self.__greenValue

    @greenValue.setter
    def greenValue(self, greenValue: int):
        self.__greenValue = greenValue

    @property
    def Color(self):
        return self.__Color

    @Color.setter
    def Color(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Geometry_RGBColor__Color", None)
        self.__Color = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Geometry74"):
                opp_val = getattr(old_value, "Geometry74", None)
                if opp_val == self:
                    setattr(old_value, "Geometry74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Geometry74"):
                opp_val = getattr(value, "Geometry74", None)
                setattr(value, "Geometry74", self)

    @property
    def Color79(self):
        return self.__Color79

    @Color79.setter
    def Color79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Geometry_RGBColor__Color79", None)
        self.__Color79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Geometry80"):
                opp_val = getattr(old_value, "Geometry80", None)
                if opp_val == self:
                    setattr(old_value, "Geometry80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Geometry80"):
                opp_val = getattr(value, "Geometry80", None)
                setattr(value, "Geometry80", self)

    @property
    def Color76(self):
        return self.__Color76

    @Color76.setter
    def Color76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Geometry_RGBColor__Color76", None)
        self.__Color76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Geometry77"):
                opp_val = getattr(old_value, "Geometry77", None)
                if opp_val == self:
                    setattr(old_value, "Geometry77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Geometry77"):
                opp_val = getattr(value, "Geometry77", None)
                setattr(value, "Geometry77", self)

class MessageDefinition:

    pass
class HALL_Goal:

    def __init__(self, condition: str, Goal: "HALL_TaskObject" = None, goal: "HALL_TaskObject" = None):
        self.condition = condition
        self.Goal = Goal
        self.goal = goal
        
    @property
    def condition(self) -> str:
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition

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
            if hasattr(old_value, "TaskObject52"):
                opp_val = getattr(old_value, "TaskObject52", None)
                if opp_val == self:
                    setattr(old_value, "TaskObject52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TaskObject52"):
                opp_val = getattr(value, "TaskObject52", None)
                setattr(value, "TaskObject52", self)

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

class GeometryData:

    pass
class HALL_Geometry_GeometryData2D(GeometryData):

    def __init__(self, labelText: str, Point2D: set["Point2D"] = None, Geometry2: "HALL_VisualObject"):
        self.labelText = labelText
        self.Point2D = Point2D if Point2D is not None else set()
        
    @property
    def labelText(self) -> str:
        return self.__labelText

    @labelText.setter
    def labelText(self, labelText: str):
        self.__labelText = labelText

    @property
    def Point2D(self):
        return self.__Point2D

    @Point2D.setter
    def Point2D(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Geometry_GeometryData2D__Point2D", None)
        self.__Point2D = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Geometry114"):
                    opp_val = getattr(item, "Geometry114", None)
                    
                    if opp_val == self:
                        setattr(item, "Geometry114", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Geometry114"):
                    opp_val = getattr(item, "Geometry114", None)
                    
                    setattr(item, "Geometry114", self)
                    

class HALL_Geometry_GeometryData3D(GeometryData):

    pass
class ColorData:

    pass
class Component:

    pass
class HALL_TaskObject(Component):

    def __init__(self, completionTime: int, numberofgoalscompleted: int, goalInv: set["HALL_Goal"] = None, taskObject: "HALL_UserProfile" = None, TaskObject46: "HALL_TaskObject" = None, componentSetInv45: set["HALL_TaskObject"] = None, TaskObject50: "HALL_TaskObject" = None, componentSet49: "HALL_TaskObject" = None, TaskObject52: "HALL_Goal" = None, TaskObject: "HALL_UserProfile" = None):
        self.completionTime = completionTime
        self.numberofgoalscompleted = numberofgoalscompleted
        self.goalInv = goalInv if goalInv is not None else set()
        self.taskObject = taskObject
        self.TaskObject46 = TaskObject46
        self.componentSetInv45 = componentSetInv45 if componentSetInv45 is not None else set()
        self.TaskObject50 = TaskObject50
        self.componentSet49 = componentSet49
        self.TaskObject52 = TaskObject52
        self.TaskObject = TaskObject
        
    @property
    def numberofgoalscompleted(self) -> int:
        return self.__numberofgoalscompleted

    @numberofgoalscompleted.setter
    def numberofgoalscompleted(self, numberofgoalscompleted: int):
        self.__numberofgoalscompleted = numberofgoalscompleted

    @property
    def completionTime(self) -> int:
        return self.__completionTime

    @completionTime.setter
    def completionTime(self, completionTime: int):
        self.__completionTime = completionTime

    @property
    def componentSet49(self):
        return self.__componentSet49

    @componentSet49.setter
    def componentSet49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_TaskObject__componentSet49", None)
        self.__componentSet49 = value
        
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

    @property
    def TaskObject52(self):
        return self.__TaskObject52

    @TaskObject52.setter
    def TaskObject52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_TaskObject__TaskObject52", None)
        self.__TaskObject52 = value
        
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
    def componentSetInv45(self):
        return self.__componentSetInv45

    @componentSetInv45.setter
    def componentSetInv45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_TaskObject__componentSetInv45", None)
        self.__componentSetInv45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TaskObject46"):
                    opp_val = getattr(item, "TaskObject46", None)
                    
                    if opp_val == self:
                        setattr(item, "TaskObject46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TaskObject46"):
                    opp_val = getattr(item, "TaskObject46", None)
                    
                    setattr(item, "TaskObject46", self)
                    

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
            if hasattr(old_value, "UserProfile42"):
                opp_val = getattr(old_value, "UserProfile42", None)
                if opp_val == self:
                    setattr(old_value, "UserProfile42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UserProfile42"):
                opp_val = getattr(value, "UserProfile42", None)
                setattr(value, "UserProfile42", self)

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
            if hasattr(old_value, "componentSet49"):
                opp_val = getattr(old_value, "componentSet49", None)
                if opp_val == self:
                    setattr(old_value, "componentSet49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentSet49"):
                opp_val = getattr(value, "componentSet49", None)
                setattr(value, "componentSet49", self)

    @property
    def TaskObject46(self):
        return self.__TaskObject46

    @TaskObject46.setter
    def TaskObject46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_TaskObject__TaskObject46", None)
        self.__TaskObject46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentSetInv45"):
                opp_val = getattr(old_value, "componentSetInv45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentSetInv45"):
                opp_val = getattr(value, "componentSetInv45", None)
                if opp_val is None:
                    setattr(value, "componentSetInv45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class HALL_UserProfile(Component):

    def __init__(self, numberofcompletedtasks: int, UserProfile: "HALL_VisualObject" = None, UserProfile39: "HALL_UserProfile" = None, componentSet38: "HALL_UserProfile" = None, UserProfile42: "HALL_TaskObject" = None, UserProfile22: "HALL_Model" = None, visualObjectInv: set["HALL_VisualObject"] = None, taskObjectInv: set["HALL_TaskObject"] = None, userProfile: "HALL_Model" = None, UserProfile35: "HALL_UserProfile" = None, componentSetInv34: set["HALL_UserProfile"] = None):
        self.numberofcompletedtasks = numberofcompletedtasks
        self.UserProfile = UserProfile
        self.UserProfile39 = UserProfile39
        self.componentSet38 = componentSet38
        self.UserProfile42 = UserProfile42
        self.UserProfile22 = UserProfile22
        self.visualObjectInv = visualObjectInv if visualObjectInv is not None else set()
        self.taskObjectInv = taskObjectInv if taskObjectInv is not None else set()
        self.userProfile = userProfile
        self.UserProfile35 = UserProfile35
        self.componentSetInv34 = componentSetInv34 if componentSetInv34 is not None else set()
        
    @property
    def numberofcompletedtasks(self) -> int:
        return self.__numberofcompletedtasks

    @numberofcompletedtasks.setter
    def numberofcompletedtasks(self, numberofcompletedtasks: int):
        self.__numberofcompletedtasks = numberofcompletedtasks

    @property
    def UserProfile39(self):
        return self.__UserProfile39

    @UserProfile39.setter
    def UserProfile39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_UserProfile__UserProfile39", None)
        self.__UserProfile39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentSet38"):
                opp_val = getattr(old_value, "componentSet38", None)
                if opp_val == self:
                    setattr(old_value, "componentSet38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentSet38"):
                opp_val = getattr(value, "componentSet38", None)
                setattr(value, "componentSet38", self)

    @property
    def UserProfile42(self):
        return self.__UserProfile42

    @UserProfile42.setter
    def UserProfile42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_UserProfile__UserProfile42", None)
        self.__UserProfile42 = value
        
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

    @property
    def UserProfile35(self):
        return self.__UserProfile35

    @UserProfile35.setter
    def UserProfile35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_UserProfile__UserProfile35", None)
        self.__UserProfile35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentSetInv34"):
                opp_val = getattr(old_value, "componentSetInv34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentSetInv34"):
                opp_val = getattr(value, "componentSetInv34", None)
                if opp_val is None:
                    setattr(value, "componentSetInv34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def componentSet38(self):
        return self.__componentSet38

    @componentSet38.setter
    def componentSet38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_UserProfile__componentSet38", None)
        self.__componentSet38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UserProfile39"):
                opp_val = getattr(old_value, "UserProfile39", None)
                if opp_val == self:
                    setattr(old_value, "UserProfile39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UserProfile39"):
                opp_val = getattr(value, "UserProfile39", None)
                setattr(value, "UserProfile39", self)

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
            if hasattr(old_value, "Model31"):
                opp_val = getattr(old_value, "Model31", None)
                if opp_val == self:
                    setattr(old_value, "Model31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model31"):
                opp_val = getattr(value, "Model31", None)
                setattr(value, "Model31", self)

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
    def componentSetInv34(self):
        return self.__componentSetInv34

    @componentSetInv34.setter
    def componentSetInv34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_UserProfile__componentSetInv34", None)
        self.__componentSetInv34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UserProfile35"):
                    opp_val = getattr(item, "UserProfile35", None)
                    
                    if opp_val == self:
                        setattr(item, "UserProfile35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UserProfile35"):
                    opp_val = getattr(item, "UserProfile35", None)
                    
                    setattr(item, "UserProfile35", self)
                    

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
                if hasattr(item, "VisualObject28"):
                    opp_val = getattr(item, "VisualObject28", None)
                    
                    if opp_val == self:
                        setattr(item, "VisualObject28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VisualObject28"):
                    opp_val = getattr(item, "VisualObject28", None)
                    
                    setattr(item, "VisualObject28", self)
                    

    @property
    def UserProfile22(self):
        return self.__UserProfile22

    @UserProfile22.setter
    def UserProfile22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_UserProfile__UserProfile22", None)
        self.__UserProfile22 = value
        
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

class HALL_VisualObject(Component):

    pass
class HALL_Model:

    pass
class HALL_SystemComponent(Component):

    pass
class MessageHandler:

    pass
class FSM:

    pass
class HALL_Data:

    def __init__(self, name: str, type: str, initValue: str, currentValue: str, Data: "HALL_Component" = None, MessageDefinition57: "MessageDefinition" = None, data: "HALL_Component" = None):
        self.name = name
        self.type = type
        self.initValue = initValue
        self.currentValue = currentValue
        self.Data = Data
        self.MessageDefinition57 = MessageDefinition57
        self.data = data
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def initValue(self) -> str:
        return self.__initValue

    @initValue.setter
    def initValue(self, initValue: str):
        self.__initValue = initValue

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def currentValue(self) -> str:
        return self.__currentValue

    @currentValue.setter
    def currentValue(self, currentValue: str):
        self.__currentValue = currentValue

    @property
    def MessageDefinition57(self):
        return self.__MessageDefinition57

    @MessageDefinition57.setter
    def MessageDefinition57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Data__MessageDefinition57", None)
        self.__MessageDefinition57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Messages58"):
                opp_val = getattr(old_value, "Messages58", None)
                if opp_val == self:
                    setattr(old_value, "Messages58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Messages58"):
                opp_val = getattr(value, "Messages58", None)
                setattr(value, "Messages58", self)

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

class HALL_Component(ABC):

    def __init__(self, name: str, dataInvComponent: set["HALL_Data"] = None, FSM: "FSM" = None, MessageHandler: set["MessageHandler"] = None, Component: "HALL_Data" = None):
        self.name = name
        self.dataInvComponent = dataInvComponent if dataInvComponent is not None else set()
        self.FSM = FSM
        self.MessageHandler = MessageHandler if MessageHandler is not None else set()
        self.Component = Component
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
                    

    @property
    def FSM(self):
        return self.__FSM

    @FSM.setter
    def FSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Component__FSM", None)
        self.__FSM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM11"):
                opp_val = getattr(old_value, "FSM11", None)
                if opp_val == self:
                    setattr(old_value, "FSM11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM11"):
                opp_val = getattr(value, "FSM11", None)
                setattr(value, "FSM11", self)

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
            if hasattr(old_value, "data"):
                opp_val = getattr(old_value, "data", None)
                if opp_val == self:
                    setattr(old_value, "data", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "data"):
                opp_val = getattr(value, "data", None)
                setattr(value, "data", self)

    @property
    def MessageHandler(self):
        return self.__MessageHandler

    @MessageHandler.setter
    def MessageHandler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Component__MessageHandler", None)
        self.__MessageHandler = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Messages"):
                    opp_val = getattr(item, "Messages", None)
                    
                    if opp_val == self:
                        setattr(item, "Messages", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Messages"):
                    opp_val = getattr(item, "Messages", None)
                    
                    setattr(item, "Messages", self)
                    
