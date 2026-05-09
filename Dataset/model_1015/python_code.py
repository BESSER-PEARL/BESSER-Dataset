from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class HALL_Trigger_TriggerExpression:

    pass
class Transition:

    pass
class HALL_FSM_State(ABC):

    def __init__(self, isActive: bool, source: set["Transition"] = None):
        self.isActive = isActive
        self.source = source if source is not None else set()
        
        pass
    @property
    def isActive(self):
        return self.__isActive

    @isActive.setter
    def isActive(self, isActive: bool):
        self.__isActive = isActive


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
                    

class Trigger_TriggerExpression:

    pass
class FSMActions_ActionExpression:

    pass
class FSMInstructions_PosConditionExpression:

    pass
class FSMConditions_PreConditionExpression:

    pass
class HALL_FSM_Transition:

    def __init__(self, name: str, transitions205: "State" = None, HALL_FSM_Transition: "State" = None, PreConditionInv209: "FSMConditions_PreConditionExpression" = None, PosConditionInv211: "FSMInstructions_PosConditionExpression" = None, ActionInv: "FSMActions_ActionExpression" = None, TriggerInv: "Trigger_TriggerExpression" = None):
        self.name = name
        self.transitions205 = transitions205
        self.HALL_FSM_Transition = HALL_FSM_Transition
        self.PreConditionInv209 = PreConditionInv209
        self.PosConditionInv211 = PosConditionInv211
        self.ActionInv = ActionInv
        self.TriggerInv = TriggerInv
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def transitions205(self):
        return self.__transitions205

    @transitions205.setter
    def transitions205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSM_Transition__transitions205", None)
        self.__transitions205 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State"):
                opp_val = getattr(old_value, "State", None)
                if opp_val == self:
                    setattr(old_value, "State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State"):
                opp_val = getattr(value, "State", None)
                setattr(value, "State", self)

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
            if hasattr(old_value, "State207"):
                opp_val = getattr(old_value, "State207", None)
                if opp_val == self:
                    setattr(old_value, "State207", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State207"):
                opp_val = getattr(value, "State207", None)
                setattr(value, "State207", self)

    @property
    def PosConditionInv211(self):
        return self.__PosConditionInv211

    @PosConditionInv211.setter
    def PosConditionInv211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSM_Transition__PosConditionInv211", None)
        self.__PosConditionInv211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PosConditionExpression"):
                opp_val = getattr(old_value, "PosConditionExpression", None)
                if opp_val == self:
                    setattr(old_value, "PosConditionExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PosConditionExpression"):
                opp_val = getattr(value, "PosConditionExpression", None)
                setattr(value, "PosConditionExpression", self)

    @property
    def PreConditionInv209(self):
        return self.__PreConditionInv209

    @PreConditionInv209.setter
    def PreConditionInv209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSM_Transition__PreConditionInv209", None)
        self.__PreConditionInv209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PreConditionExpression"):
                opp_val = getattr(old_value, "PreConditionExpression", None)
                if opp_val == self:
                    setattr(old_value, "PreConditionExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PreConditionExpression"):
                opp_val = getattr(value, "PreConditionExpression", None)
                setattr(value, "PreConditionExpression", self)

    @property
    def ActionInv(self):
        return self.__ActionInv

    @ActionInv.setter
    def ActionInv(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSM_Transition__ActionInv", None)
        self.__ActionInv = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActionExpression"):
                opp_val = getattr(old_value, "ActionExpression", None)
                if opp_val == self:
                    setattr(old_value, "ActionExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActionExpression"):
                opp_val = getattr(value, "ActionExpression", None)
                setattr(value, "ActionExpression", self)

    @property
    def TriggerInv(self):
        return self.__TriggerInv

    @TriggerInv.setter
    def TriggerInv(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSM_Transition__TriggerInv", None)
        self.__TriggerInv = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TriggerExpression"):
                opp_val = getattr(old_value, "TriggerExpression", None)
                if opp_val == self:
                    setattr(old_value, "TriggerExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TriggerExpression"):
                opp_val = getattr(value, "TriggerExpression", None)
                setattr(value, "TriggerExpression", self)

class State:

    pass
class HALL_FSM_InitialState(State):

    pass
class HALL_FSM_NamedState(State):

    def __init__(self, name: str, state: "FSM" = None, State: "HALL_FSM_Transition" = None, State207: "HALL_FSM_Transition" = None):
        self.name = name
        self.state = state
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSM_NamedState__state", None)
        self.__state = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM201"):
                opp_val = getattr(old_value, "FSM201", None)
                if opp_val == self:
                    setattr(old_value, "FSM201", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM201"):
                opp_val = getattr(value, "FSM201", None)
                setattr(value, "FSM201", self)

class NamedState:

    pass
class InitialState:

    pass
class FSM_HALL_Component:

    pass
class HALL_FSM_FSM:

    pass
class HALL_Actions_ActionMessageExpression(ABC):

    pass
class ActionMessageExpressionElement:

    pass
class HALL_Actions_BinaryOperator(ActionMessageExpressionElement):

    def __init__(self, operatorname: str, HALL_Actions_BinaryOperator: "Actions_ActionMessageExpressionElement" = None, HALL_Actions_BinaryOperator175: "Actions_ActionMessageExpressionElement" = None):
        self.operatorname = operatorname
        self.HALL_Actions_BinaryOperator = HALL_Actions_BinaryOperator
        self.HALL_Actions_BinaryOperator175 = HALL_Actions_BinaryOperator175
        
        pass
    @property
    def operatorname(self):
        return self.__operatorname

    @operatorname.setter
    def operatorname(self, operatorname: str):
        self.__operatorname = operatorname


    @property
    def HALL_Actions_BinaryOperator175(self):
        return self.__HALL_Actions_BinaryOperator175

    @HALL_Actions_BinaryOperator175.setter
    def HALL_Actions_BinaryOperator175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Actions_BinaryOperator__HALL_Actions_BinaryOperator175", None)
        self.__HALL_Actions_BinaryOperator175 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Actions_ActionMessageExpressionElement176"):
                opp_val = getattr(old_value, "Actions_ActionMessageExpressionElement176", None)
                if opp_val == self:
                    setattr(old_value, "Actions_ActionMessageExpressionElement176", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Actions_ActionMessageExpressionElement176"):
                opp_val = getattr(value, "Actions_ActionMessageExpressionElement176", None)
                setattr(value, "Actions_ActionMessageExpressionElement176", self)

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

class HALL_Actions_GetData(ActionMessageExpressionElement):

    def __init__(self, field: str, HALL_Actions_GetData: "Actions_HALL_Component" = None):
        self.field = field
        self.HALL_Actions_GetData = HALL_Actions_GetData
        
        pass
    @property
    def field(self):
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

class HALL_Actions_GetMessageParameter(ActionMessageExpressionElement):

    def __init__(self, field: str):
        self.field = field
        
        pass
    @property
    def field(self):
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field


class HALL_Actions_DomainPropertyGet(ActionMessageExpressionElement):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class HALL_Actions_MessageInvocation(ActionMessageExpressionElement):

    def __init__(self, name: str, isTopDown: bool, HALL_Actions_MessageInvocation: "Actions_ActionMessageExpressionElement" = None):
        self.name = name
        self.isTopDown = isTopDown
        self.HALL_Actions_MessageInvocation = HALL_Actions_MessageInvocation
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def isTopDown(self):
        return self.__isTopDown

    @isTopDown.setter
    def isTopDown(self, isTopDown: bool):
        self.__isTopDown = isTopDown


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
            if hasattr(old_value, "Actions_ActionMessageExpressionElement183"):
                opp_val = getattr(old_value, "Actions_ActionMessageExpressionElement183", None)
                if opp_val == self:
                    setattr(old_value, "Actions_ActionMessageExpressionElement183", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Actions_ActionMessageExpressionElement183"):
                opp_val = getattr(value, "Actions_ActionMessageExpressionElement183", None)
                setattr(value, "Actions_ActionMessageExpressionElement183", self)

class HALL_Actions_Literal(ActionMessageExpressionElement):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class HALL_Actions_GetMessageData(ActionMessageExpressionElement):

    def __init__(self, field: str):
        self.field = field
        
        pass
    @property
    def field(self):
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field


class HALL_Actions_UnaryOperator(ActionMessageExpressionElement):

    def __init__(self, operatorname: str, HALL_Actions_UnaryOperator: "Actions_ActionMessageExpressionElement" = None):
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
            if hasattr(old_value, "Actions_ActionMessageExpressionElement185"):
                opp_val = getattr(old_value, "Actions_ActionMessageExpressionElement185", None)
                if opp_val == self:
                    setattr(old_value, "Actions_ActionMessageExpressionElement185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Actions_ActionMessageExpressionElement185"):
                opp_val = getattr(value, "Actions_ActionMessageExpressionElement185", None)
                setattr(value, "Actions_ActionMessageExpressionElement185", self)

class HALL_Actions_Let(ActionMessageExpressionElement):

    def __init__(self, namevar: str, HALL_Actions_Let: "Actions_ActionMessageExpressionElement" = None, HALL_Actions_Let180: "Actions_ActionMessageExpressionElement" = None):
        self.namevar = namevar
        self.HALL_Actions_Let = HALL_Actions_Let
        self.HALL_Actions_Let180 = HALL_Actions_Let180
        
        pass
    @property
    def namevar(self):
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
            if hasattr(old_value, "Actions_ActionMessageExpressionElement178"):
                opp_val = getattr(old_value, "Actions_ActionMessageExpressionElement178", None)
                if opp_val == self:
                    setattr(old_value, "Actions_ActionMessageExpressionElement178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Actions_ActionMessageExpressionElement178"):
                opp_val = getattr(value, "Actions_ActionMessageExpressionElement178", None)
                setattr(value, "Actions_ActionMessageExpressionElement178", self)

    @property
    def HALL_Actions_Let180(self):
        return self.__HALL_Actions_Let180

    @HALL_Actions_Let180.setter
    def HALL_Actions_Let180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Actions_Let__HALL_Actions_Let180", None)
        self.__HALL_Actions_Let180 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Actions_ActionMessageExpressionElement181"):
                opp_val = getattr(old_value, "Actions_ActionMessageExpressionElement181", None)
                if opp_val == self:
                    setattr(old_value, "Actions_ActionMessageExpressionElement181", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Actions_ActionMessageExpressionElement181"):
                opp_val = getattr(value, "Actions_ActionMessageExpressionElement181", None)
                setattr(value, "Actions_ActionMessageExpressionElement181", self)

class HALL_Actions_VarRef(ActionMessageExpressionElement):

    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class HALL_Actions_ActionMessageExpressionElement(ABC):

    pass
class Actions_ActionMessageExpressionElement:

    pass
class Conditions_HALL_Component:

    pass
class PreConditionMessageExpressionElement:

    pass
class HALL_Conditions_DomainPropertyGet(PreConditionMessageExpressionElement):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class HALL_Conditions_GetMessageParameter(PreConditionMessageExpressionElement):

    def __init__(self, field: str):
        self.field = field
        
        pass
    @property
    def field(self):
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field


class HALL_Conditions_Literal(PreConditionMessageExpressionElement):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class HALL_Conditions_Let(PreConditionMessageExpressionElement):

    def __init__(self, namevar: str, HALL_Conditions_Let: "Conditions_PreConditionMessageExpressionElement" = None, HALL_Conditions_Let159: "Conditions_PreConditionMessageExpressionElement" = None):
        self.namevar = namevar
        self.HALL_Conditions_Let = HALL_Conditions_Let
        self.HALL_Conditions_Let159 = HALL_Conditions_Let159
        
        pass
    @property
    def namevar(self):
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
    def HALL_Conditions_Let159(self):
        return self.__HALL_Conditions_Let159

    @HALL_Conditions_Let159.setter
    def HALL_Conditions_Let159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Conditions_Let__HALL_Conditions_Let159", None)
        self.__HALL_Conditions_Let159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Conditions_PreConditionMessageExpressionElement160"):
                opp_val = getattr(old_value, "Conditions_PreConditionMessageExpressionElement160", None)
                if opp_val == self:
                    setattr(old_value, "Conditions_PreConditionMessageExpressionElement160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Conditions_PreConditionMessageExpressionElement160"):
                opp_val = getattr(value, "Conditions_PreConditionMessageExpressionElement160", None)
                setattr(value, "Conditions_PreConditionMessageExpressionElement160", self)

class HALL_Conditions_BinaryOperator(PreConditionMessageExpressionElement):

    def __init__(self, operatorname: str, HALL_Conditions_BinaryOperator: "Conditions_PreConditionMessageExpressionElement" = None, HALL_Conditions_BinaryOperator166: "Conditions_PreConditionMessageExpressionElement" = None):
        self.operatorname = operatorname
        self.HALL_Conditions_BinaryOperator = HALL_Conditions_BinaryOperator
        self.HALL_Conditions_BinaryOperator166 = HALL_Conditions_BinaryOperator166
        
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
            if hasattr(old_value, "Conditions_PreConditionMessageExpressionElement164"):
                opp_val = getattr(old_value, "Conditions_PreConditionMessageExpressionElement164", None)
                if opp_val == self:
                    setattr(old_value, "Conditions_PreConditionMessageExpressionElement164", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Conditions_PreConditionMessageExpressionElement164"):
                opp_val = getattr(value, "Conditions_PreConditionMessageExpressionElement164", None)
                setattr(value, "Conditions_PreConditionMessageExpressionElement164", self)

    @property
    def HALL_Conditions_BinaryOperator166(self):
        return self.__HALL_Conditions_BinaryOperator166

    @HALL_Conditions_BinaryOperator166.setter
    def HALL_Conditions_BinaryOperator166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Conditions_BinaryOperator__HALL_Conditions_BinaryOperator166", None)
        self.__HALL_Conditions_BinaryOperator166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Conditions_PreConditionMessageExpressionElement167"):
                opp_val = getattr(old_value, "Conditions_PreConditionMessageExpressionElement167", None)
                if opp_val == self:
                    setattr(old_value, "Conditions_PreConditionMessageExpressionElement167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Conditions_PreConditionMessageExpressionElement167"):
                opp_val = getattr(value, "Conditions_PreConditionMessageExpressionElement167", None)
                setattr(value, "Conditions_PreConditionMessageExpressionElement167", self)

class HALL_Conditions_GetData(PreConditionMessageExpressionElement):

    def __init__(self, field: str, HALL_Conditions_GetData: "Conditions_HALL_Component" = None):
        self.field = field
        self.HALL_Conditions_GetData = HALL_Conditions_GetData
        
        pass
    @property
    def field(self):
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
            if hasattr(old_value, "Conditions_HALL_Component156"):
                opp_val = getattr(old_value, "Conditions_HALL_Component156", None)
                if opp_val == self:
                    setattr(old_value, "Conditions_HALL_Component156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Conditions_HALL_Component156"):
                opp_val = getattr(value, "Conditions_HALL_Component156", None)
                setattr(value, "Conditions_HALL_Component156", self)

class HALL_Conditions_GetMessageData(PreConditionMessageExpressionElement):

    def __init__(self, field: str):
        self.field = field
        
        pass
    @property
    def field(self):
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field


class HALL_Conditions_GetState(PreConditionMessageExpressionElement):

    pass
class HALL_Conditions_UnaryOperator(PreConditionMessageExpressionElement):

    def __init__(self, operatorname: str, HALL_Conditions_UnaryOperator: "Conditions_PreConditionMessageExpressionElement" = None):
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
            if hasattr(old_value, "Conditions_PreConditionMessageExpressionElement162"):
                opp_val = getattr(old_value, "Conditions_PreConditionMessageExpressionElement162", None)
                if opp_val == self:
                    setattr(old_value, "Conditions_PreConditionMessageExpressionElement162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Conditions_PreConditionMessageExpressionElement162"):
                opp_val = getattr(value, "Conditions_PreConditionMessageExpressionElement162", None)
                setattr(value, "Conditions_PreConditionMessageExpressionElement162", self)

class HALL_Conditions_VarRef(PreConditionMessageExpressionElement):

    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class HALL_Conditions_PreConditionMessageExpressionElement(ABC):

    pass
class Conditions_PreConditionMessageExpressionElement:

    pass
class HALL_Conditions_PreConditionMessageExpression(ABC):

    pass
class PosConditionMessageExpressionElement:

    pass
class HALL_Instructions_GetMessageData(PosConditionMessageExpressionElement):

    def __init__(self, field: str):
        self.field = field
        
        pass
    @property
    def field(self):
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field


class HALL_Instructions_DomainPropertyGet(PosConditionMessageExpressionElement):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class HALL_Instructions_SetTopDown(PosConditionMessageExpressionElement):

    pass
class HALL_Instructions_GetMessageParameter(PosConditionMessageExpressionElement):

    def __init__(self, field: str):
        self.field = field
        
        pass
    @property
    def field(self):
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field


class HALL_Instructions_VarRef(PosConditionMessageExpressionElement):

    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


class HALL_Instructions_PosConditionMessageExpressionElement(ABC):

    pass
class Instructions_PosConditionMessageExpressionElement:

    pass
class HALL_Instructions_PosConditionMessageExpression(ABC):

    pass
class HALL_Instructions_Let(PosConditionMessageExpressionElement):

    def __init__(self, namevar: str, HALL_Instructions_Let: "Instructions_PosConditionMessageExpressionElement" = None, HALL_Instructions_Let145: "Instructions_PosConditionMessageExpressionElement" = None):
        self.namevar = namevar
        self.HALL_Instructions_Let = HALL_Instructions_Let
        self.HALL_Instructions_Let145 = HALL_Instructions_Let145
        
        pass
    @property
    def namevar(self):
        return self.__namevar

    @namevar.setter
    def namevar(self, namevar: str):
        self.__namevar = namevar


    @property
    def HALL_Instructions_Let145(self):
        return self.__HALL_Instructions_Let145

    @HALL_Instructions_Let145.setter
    def HALL_Instructions_Let145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Instructions_Let__HALL_Instructions_Let145", None)
        self.__HALL_Instructions_Let145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Instructions_PosConditionMessageExpressionElement146"):
                opp_val = getattr(old_value, "Instructions_PosConditionMessageExpressionElement146", None)
                if opp_val == self:
                    setattr(old_value, "Instructions_PosConditionMessageExpressionElement146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instructions_PosConditionMessageExpressionElement146"):
                opp_val = getattr(value, "Instructions_PosConditionMessageExpressionElement146", None)
                setattr(value, "Instructions_PosConditionMessageExpressionElement146", self)

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
            if hasattr(old_value, "Instructions_PosConditionMessageExpressionElement143"):
                opp_val = getattr(old_value, "Instructions_PosConditionMessageExpressionElement143", None)
                if opp_val == self:
                    setattr(old_value, "Instructions_PosConditionMessageExpressionElement143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instructions_PosConditionMessageExpressionElement143"):
                opp_val = getattr(value, "Instructions_PosConditionMessageExpressionElement143", None)
                setattr(value, "Instructions_PosConditionMessageExpressionElement143", self)

class HALL_Instructions_SetMessageParameter(PosConditionMessageExpressionElement):

    def __init__(self, field: str, HALL_Instructions_SetMessageParameter: "Instructions_PosConditionMessageExpressionElement" = None):
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
            if hasattr(old_value, "Instructions_PosConditionMessageExpressionElement141"):
                opp_val = getattr(old_value, "Instructions_PosConditionMessageExpressionElement141", None)
                if opp_val == self:
                    setattr(old_value, "Instructions_PosConditionMessageExpressionElement141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instructions_PosConditionMessageExpressionElement141"):
                opp_val = getattr(value, "Instructions_PosConditionMessageExpressionElement141", None)
                setattr(value, "Instructions_PosConditionMessageExpressionElement141", self)

class HALL_Instructions_SetMessageData(PosConditionMessageExpressionElement):

    def __init__(self, field: str, HALL_Instructions_SetMessageData: "Instructions_PosConditionMessageExpressionElement" = None):
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
            if hasattr(old_value, "Instructions_PosConditionMessageExpressionElement139"):
                opp_val = getattr(old_value, "Instructions_PosConditionMessageExpressionElement139", None)
                if opp_val == self:
                    setattr(old_value, "Instructions_PosConditionMessageExpressionElement139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instructions_PosConditionMessageExpressionElement139"):
                opp_val = getattr(value, "Instructions_PosConditionMessageExpressionElement139", None)
                setattr(value, "Instructions_PosConditionMessageExpressionElement139", self)

class HALL_Instructions_SetData(PosConditionMessageExpressionElement):

    def __init__(self, field: str, HALL_Instructions_SetData: "Instructions_PosConditionMessageExpressionElement" = None, HALL_Instructions_SetData136: "Instructions_HALL_Component" = None):
        self.field = field
        self.HALL_Instructions_SetData = HALL_Instructions_SetData
        self.HALL_Instructions_SetData136 = HALL_Instructions_SetData136
        
        pass
    @property
    def field(self):
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
            if hasattr(old_value, "Instructions_PosConditionMessageExpressionElement134"):
                opp_val = getattr(old_value, "Instructions_PosConditionMessageExpressionElement134", None)
                if opp_val == self:
                    setattr(old_value, "Instructions_PosConditionMessageExpressionElement134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instructions_PosConditionMessageExpressionElement134"):
                opp_val = getattr(value, "Instructions_PosConditionMessageExpressionElement134", None)
                setattr(value, "Instructions_PosConditionMessageExpressionElement134", self)

    @property
    def HALL_Instructions_SetData136(self):
        return self.__HALL_Instructions_SetData136

    @HALL_Instructions_SetData136.setter
    def HALL_Instructions_SetData136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Instructions_SetData__HALL_Instructions_SetData136", None)
        self.__HALL_Instructions_SetData136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Instructions_HALL_Component137"):
                opp_val = getattr(old_value, "Instructions_HALL_Component137", None)
                if opp_val == self:
                    setattr(old_value, "Instructions_HALL_Component137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instructions_HALL_Component137"):
                opp_val = getattr(value, "Instructions_HALL_Component137", None)
                setattr(value, "Instructions_HALL_Component137", self)

class HALL_Instructions_SetState(PosConditionMessageExpressionElement):

    def __init__(self, name: str, HALL_Instructions_SetState: "Instructions_HALL_Component" = None):
        self.name = name
        self.HALL_Instructions_SetState = HALL_Instructions_SetState
        
        pass
    @property
    def name(self):
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
            if hasattr(old_value, "Instructions_HALL_Component132"):
                opp_val = getattr(old_value, "Instructions_HALL_Component132", None)
                if opp_val == self:
                    setattr(old_value, "Instructions_HALL_Component132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instructions_HALL_Component132"):
                opp_val = getattr(value, "Instructions_HALL_Component132", None)
                setattr(value, "Instructions_HALL_Component132", self)

class HALL_Instructions_GetState(PosConditionMessageExpressionElement):

    pass
class Instructions_HALL_Component:

    pass
class HALL_Instructions_GetData(PosConditionMessageExpressionElement):

    def __init__(self, field: str, HALL_Instructions_GetData: "Instructions_HALL_Component" = None):
        self.field = field
        self.HALL_Instructions_GetData = HALL_Instructions_GetData
        
        pass
    @property
    def field(self):
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

class HALL_Instructions_UnaryOperator(PosConditionMessageExpressionElement):

    def __init__(self, operatorname: str, HALL_Instructions_UnaryOperator: "Instructions_PosConditionMessageExpressionElement" = None):
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
            if hasattr(old_value, "Instructions_PosConditionMessageExpressionElement127"):
                opp_val = getattr(old_value, "Instructions_PosConditionMessageExpressionElement127", None)
                if opp_val == self:
                    setattr(old_value, "Instructions_PosConditionMessageExpressionElement127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instructions_PosConditionMessageExpressionElement127"):
                opp_val = getattr(value, "Instructions_PosConditionMessageExpressionElement127", None)
                setattr(value, "Instructions_PosConditionMessageExpressionElement127", self)

class HALL_Instructions_BinaryOperator(PosConditionMessageExpressionElement):

    def __init__(self, operatorname: str, HALL_Instructions_BinaryOperator: "Instructions_PosConditionMessageExpressionElement" = None, HALL_Instructions_BinaryOperator124: "Instructions_PosConditionMessageExpressionElement" = None):
        self.operatorname = operatorname
        self.HALL_Instructions_BinaryOperator = HALL_Instructions_BinaryOperator
        self.HALL_Instructions_BinaryOperator124 = HALL_Instructions_BinaryOperator124
        
        pass
    @property
    def operatorname(self):
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
    def HALL_Instructions_BinaryOperator124(self):
        return self.__HALL_Instructions_BinaryOperator124

    @HALL_Instructions_BinaryOperator124.setter
    def HALL_Instructions_BinaryOperator124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Instructions_BinaryOperator__HALL_Instructions_BinaryOperator124", None)
        self.__HALL_Instructions_BinaryOperator124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Instructions_PosConditionMessageExpressionElement125"):
                opp_val = getattr(old_value, "Instructions_PosConditionMessageExpressionElement125", None)
                if opp_val == self:
                    setattr(old_value, "Instructions_PosConditionMessageExpressionElement125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instructions_PosConditionMessageExpressionElement125"):
                opp_val = getattr(value, "Instructions_PosConditionMessageExpressionElement125", None)
                setattr(value, "Instructions_PosConditionMessageExpressionElement125", self)

class HALL_Instructions_Literal(PosConditionMessageExpressionElement):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class HALL_Geometry_Point:

    def __init__(self, xCoord: int, yCoord: int):
        self.xCoord = xCoord
        self.yCoord = yCoord
        
        pass
    @property
    def xCoord(self):
        return self.__xCoord

    @xCoord.setter
    def xCoord(self, xCoord: int):
        self.__xCoord = xCoord


    @property
    def yCoord(self):
        return self.__yCoord

    @yCoord.setter
    def yCoord(self, yCoord: int):
        self.__yCoord = yCoord


class GeometryData2D:

    pass
class MessageTransition:

    pass
class HALL_Messages_MessageState:

    def __init__(self, isEnd: bool, isContinue: bool, isActive: bool, transitionsInvMessageState: set["MessageTransition"] = None):
        self.isEnd = isEnd
        self.isContinue = isContinue
        self.isActive = isActive
        self.transitionsInvMessageState = transitionsInvMessageState if transitionsInvMessageState is not None else set()
        
        pass
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
    def isEnd(self):
        return self.__isEnd

    @isEnd.setter
    def isEnd(self, isEnd: bool):
        self.__isEnd = isEnd


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
class NamedMessageState:

    pass
class HALL_Messages_MessageHandler:

    def __init__(self, name: str, messageStateInv: set["NamedMessageState"] = None, initialMessageStateInv: "InitialMessageState" = None, messageHandlerSet: "Messages_HALL_Component" = None):
        self.name = name
        self.messageStateInv = messageStateInv if messageStateInv is not None else set()
        self.initialMessageStateInv = initialMessageStateInv
        self.messageHandlerSet = messageHandlerSet
        
        pass
    @property
    def name(self):
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
            if hasattr(old_value, "Component113"):
                opp_val = getattr(old_value, "Component113", None)
                if opp_val == self:
                    setattr(old_value, "Component113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Component113"):
                opp_val = getattr(value, "Component113", None)
                setattr(value, "Component113", self)

    @property
    def initialMessageStateInv(self):
        return self.__initialMessageStateInv

    @initialMessageStateInv.setter
    def initialMessageStateInv(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Messages_MessageHandler__initialMessageStateInv", None)
        self.__initialMessageStateInv = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InitialMessageState"):
                opp_val = getattr(old_value, "InitialMessageState", None)
                if opp_val == self:
                    setattr(old_value, "InitialMessageState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InitialMessageState"):
                opp_val = getattr(value, "InitialMessageState", None)
                setattr(value, "InitialMessageState", self)

    @property
    def messageStateInv(self):
        return self.__messageStateInv

    @messageStateInv.setter
    def messageStateInv(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Messages_MessageHandler__messageStateInv", None)
        self.__messageStateInv = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NamedMessageState"):
                    opp_val = getattr(item, "NamedMessageState", None)
                    
                    if opp_val == self:
                        setattr(item, "NamedMessageState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NamedMessageState"):
                    opp_val = getattr(item, "NamedMessageState", None)
                    
                    setattr(item, "NamedMessageState", self)
                    

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
        
        pass
    @property
    def name(self):
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
            if hasattr(old_value, "Model106"):
                opp_val = getattr(old_value, "Model106", None)
                if opp_val == self:
                    setattr(old_value, "Model106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model106"):
                opp_val = getattr(value, "Model106", None)
                setattr(value, "Model106", self)

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
                if hasattr(item, "Data109"):
                    opp_val = getattr(item, "Data109", None)
                    
                    if opp_val == self:
                        setattr(item, "Data109", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Data109"):
                    opp_val = getattr(item, "Data109", None)
                    
                    setattr(item, "Data109", self)
                    

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
                    

class Actions_ActionMessageExpression:

    pass
class Instructions_PosConditionMessageExpression:

    pass
class Conditions_PreConditionMessageExpression:

    pass
class MessageState:

    pass
class HALL_Messages_InitialMessageState(MessageState):

    pass
class HALL_Messages_NamedMessageState(MessageState):

    def __init__(self, name: str, messageState: "MessageHandler" = None, MessageState: "HALL_Messages_MessageTransition" = None, MessageState99: "HALL_Messages_MessageTransition" = None):
        self.name = name
        self.messageState = messageState
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def messageState(self):
        return self.__messageState

    @messageState.setter
    def messageState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Messages_NamedMessageState__messageState", None)
        self.__messageState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MessageHandler104"):
                opp_val = getattr(old_value, "MessageHandler104", None)
                if opp_val == self:
                    setattr(old_value, "MessageHandler104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MessageHandler104"):
                opp_val = getattr(value, "MessageHandler104", None)
                setattr(value, "MessageHandler104", self)

class HALL_Messages_MessageTransition:

    def __init__(self, name: str, transitions: "MessageState" = None, HALL_Messages_MessageTransition: "MessageState" = None, PreConditionInv: "Conditions_PreConditionMessageExpression" = None, PosConditionInv: "Instructions_PosConditionMessageExpression" = None, ActionMessageInv: "Actions_ActionMessageExpression" = None):
        self.name = name
        self.transitions = transitions
        self.HALL_Messages_MessageTransition = HALL_Messages_MessageTransition
        self.PreConditionInv = PreConditionInv
        self.PosConditionInv = PosConditionInv
        self.ActionMessageInv = ActionMessageInv
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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

    @property
    def ActionMessageInv(self):
        return self.__ActionMessageInv

    @ActionMessageInv.setter
    def ActionMessageInv(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Messages_MessageTransition__ActionMessageInv", None)
        self.__ActionMessageInv = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActionMessageExpression"):
                opp_val = getattr(old_value, "ActionMessageExpression", None)
                if opp_val == self:
                    setattr(old_value, "ActionMessageExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActionMessageExpression"):
                opp_val = getattr(value, "ActionMessageExpression", None)
                setattr(value, "ActionMessageExpression", self)

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
            if hasattr(old_value, "MessageState99"):
                opp_val = getattr(old_value, "MessageState99", None)
                if opp_val == self:
                    setattr(old_value, "MessageState99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MessageState99"):
                opp_val = getattr(value, "MessageState99", None)
                setattr(value, "MessageState99", self)

    @property
    def PreConditionInv(self):
        return self.__PreConditionInv

    @PreConditionInv.setter
    def PreConditionInv(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Messages_MessageTransition__PreConditionInv", None)
        self.__PreConditionInv = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PreConditionMessageExpression"):
                opp_val = getattr(old_value, "PreConditionMessageExpression", None)
                if opp_val == self:
                    setattr(old_value, "PreConditionMessageExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PreConditionMessageExpression"):
                opp_val = getattr(value, "PreConditionMessageExpression", None)
                setattr(value, "PreConditionMessageExpression", self)

    @property
    def PosConditionInv(self):
        return self.__PosConditionInv

    @PosConditionInv.setter
    def PosConditionInv(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Messages_MessageTransition__PosConditionInv", None)
        self.__PosConditionInv = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PosConditionMessageExpression"):
                opp_val = getattr(old_value, "PosConditionMessageExpression", None)
                if opp_val == self:
                    setattr(old_value, "PosConditionMessageExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PosConditionMessageExpression"):
                opp_val = getattr(value, "PosConditionMessageExpression", None)
                setattr(value, "PosConditionMessageExpression", self)

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
            if hasattr(old_value, "ColorState75"):
                opp_val = getattr(old_value, "ColorState75", None)
                if opp_val == self:
                    setattr(old_value, "ColorState75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorState75"):
                opp_val = getattr(value, "ColorState75", None)
                setattr(value, "ColorState75", self)

class AlphaTransparency:

    pass
class HALL_Geometry_ColorState(ABC):

    pass
class Point:

    pass
class HALL_Geometry_Point2D(Point):

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
            if hasattr(old_value, "Face95"):
                opp_val = getattr(old_value, "Face95", None)
                if opp_val == self:
                    setattr(old_value, "Face95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Face95"):
                opp_val = getattr(value, "Face95", None)
                setattr(value, "Face95", self)

class GeometryData3D:

    pass
class Point3D:

    pass
class HALL_Geometry_Face:

    def __init__(self, labelText: str, point2dInv92: set["Point3D"] = None, face: "GeometryData3D" = None):
        self.labelText = labelText
        self.point2dInv92 = point2dInv92 if point2dInv92 is not None else set()
        self.face = face
        
        pass
    @property
    def labelText(self):
        return self.__labelText

    @labelText.setter
    def labelText(self, labelText: str):
        self.__labelText = labelText


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

    @property
    def point2dInv92(self):
        return self.__point2dInv92

    @point2dInv92.setter
    def point2dInv92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Geometry_Face__point2dInv92", None)
        self.__point2dInv92 = value if value is not None else set()
        
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
    def goal(self):
        return self.__goal

    @goal.setter
    def goal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Goal__goal", None)
        self.__goal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TaskObject49"):
                opp_val = getattr(old_value, "TaskObject49", None)
                if opp_val == self:
                    setattr(old_value, "TaskObject49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TaskObject49"):
                opp_val = getattr(value, "TaskObject49", None)
                setattr(value, "TaskObject49", self)

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
    def greenValue(self):
        return self.__greenValue

    @greenValue.setter
    def greenValue(self, greenValue: int):
        self.__greenValue = greenValue


    @property
    def redValue(self):
        return self.__redValue

    @redValue.setter
    def redValue(self, redValue: int):
        self.__redValue = redValue


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
    def specularColor(self):
        return self.__specularColor

    @specularColor.setter
    def specularColor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Geometry_RGBColor__specularColor", None)
        self.__specularColor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Color68"):
                opp_val = getattr(old_value, "Color68", None)
                if opp_val == self:
                    setattr(old_value, "Color68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Color68"):
                opp_val = getattr(value, "Color68", None)
                setattr(value, "Color68", self)

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
            if hasattr(old_value, "Color66"):
                opp_val = getattr(old_value, "Color66", None)
                if opp_val == self:
                    setattr(old_value, "Color66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Color66"):
                opp_val = getattr(value, "Color66", None)
                setattr(value, "Color66", self)

class ColorState:

    pass
class HALL_Geometry_SelectedColors(ColorState):

    pass
class HALL_Geometry_NormalColors(ColorState):

    pass
class HALL_Geometry_DisabledColors(ColorState):

    pass
class RGBColor:

    pass
class HALL_Geometry_Color:

    pass
class HALL_Parameter:

    def __init__(self, name: str, type: str, parameter: "MessageDefinition" = None):
        self.name = name
        self.type = type
        self.parameter = parameter
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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
            if hasattr(old_value, "MessageDefinition51"):
                opp_val = getattr(old_value, "MessageDefinition51", None)
                if opp_val == self:
                    setattr(old_value, "MessageDefinition51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MessageDefinition51"):
                opp_val = getattr(value, "MessageDefinition51", None)
                setattr(value, "MessageDefinition51", self)

class GeometryData:

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
                    

class HALL_Geometry_GeometryData3D(GeometryData):

    pass
class ColorData:

    pass
class Component:

    pass
class HALL_VisualObject(Component):

    pass
class HALL_TaskObject(Component):

    def __init__(self, numberofgoalscompleted: int, completionTime: int, goalInv: set["HALL_Goal"] = None, taskObject: "HALL_UserProfile" = None, TaskObject: "HALL_UserProfile" = None, TaskObject43: "HALL_TaskObject" = None, componentSetInv42: set["HALL_TaskObject"] = None, TaskObject47: "HALL_TaskObject" = None, componentSet46: "HALL_TaskObject" = None, TaskObject49: "HALL_Goal" = None):
        self.numberofgoalscompleted = numberofgoalscompleted
        self.completionTime = completionTime
        self.goalInv = goalInv if goalInv is not None else set()
        self.taskObject = taskObject
        self.TaskObject = TaskObject
        self.TaskObject43 = TaskObject43
        self.componentSetInv42 = componentSetInv42 if componentSetInv42 is not None else set()
        self.TaskObject47 = TaskObject47
        self.componentSet46 = componentSet46
        self.TaskObject49 = TaskObject49
        
        pass
    @property
    def numberofgoalscompleted(self):
        return self.__numberofgoalscompleted

    @numberofgoalscompleted.setter
    def numberofgoalscompleted(self, numberofgoalscompleted: int):
        self.__numberofgoalscompleted = numberofgoalscompleted


    @property
    def completionTime(self):
        return self.__completionTime

    @completionTime.setter
    def completionTime(self, completionTime: int):
        self.__completionTime = completionTime


    @property
    def TaskObject49(self):
        return self.__TaskObject49

    @TaskObject49.setter
    def TaskObject49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_TaskObject__TaskObject49", None)
        self.__TaskObject49 = value
        
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
    def componentSet46(self):
        return self.__componentSet46

    @componentSet46.setter
    def componentSet46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_TaskObject__componentSet46", None)
        self.__componentSet46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TaskObject47"):
                opp_val = getattr(old_value, "TaskObject47", None)
                if opp_val == self:
                    setattr(old_value, "TaskObject47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TaskObject47"):
                opp_val = getattr(value, "TaskObject47", None)
                setattr(value, "TaskObject47", self)

    @property
    def TaskObject43(self):
        return self.__TaskObject43

    @TaskObject43.setter
    def TaskObject43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_TaskObject__TaskObject43", None)
        self.__TaskObject43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentSetInv42"):
                opp_val = getattr(old_value, "componentSetInv42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentSetInv42"):
                opp_val = getattr(value, "componentSetInv42", None)
                if opp_val is None:
                    setattr(value, "componentSetInv42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TaskObject47(self):
        return self.__TaskObject47

    @TaskObject47.setter
    def TaskObject47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_TaskObject__TaskObject47", None)
        self.__TaskObject47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentSet46"):
                opp_val = getattr(old_value, "componentSet46", None)
                if opp_val == self:
                    setattr(old_value, "componentSet46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentSet46"):
                opp_val = getattr(value, "componentSet46", None)
                setattr(value, "componentSet46", self)

    @property
    def componentSetInv42(self):
        return self.__componentSetInv42

    @componentSetInv42.setter
    def componentSetInv42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_TaskObject__componentSetInv42", None)
        self.__componentSetInv42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TaskObject43"):
                    opp_val = getattr(item, "TaskObject43", None)
                    
                    if opp_val == self:
                        setattr(item, "TaskObject43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TaskObject43"):
                    opp_val = getattr(item, "TaskObject43", None)
                    
                    setattr(item, "TaskObject43", self)
                    

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
    def taskObject(self):
        return self.__taskObject

    @taskObject.setter
    def taskObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_TaskObject__taskObject", None)
        self.__taskObject = value
        
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
                    

class MessageDefinition:

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

    def __init__(self, name: str, type: str, initValue: str, currentValue: str, Data: "HALL_Component" = None, data: "MessageDefinition" = None, data55: "HALL_Component" = None):
        self.name = name
        self.type = type
        self.initValue = initValue
        self.currentValue = currentValue
        self.Data = Data
        self.data = data
        self.data55 = data55
        
        pass
    @property
    def currentValue(self):
        return self.__currentValue

    @currentValue.setter
    def currentValue(self, currentValue: str):
        self.__currentValue = currentValue


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def initValue(self):
        return self.__initValue

    @initValue.setter
    def initValue(self, initValue: str):
        self.__initValue = initValue


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


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
            if hasattr(old_value, "MessageDefinition53"):
                opp_val = getattr(old_value, "MessageDefinition53", None)
                if opp_val == self:
                    setattr(old_value, "MessageDefinition53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MessageDefinition53"):
                opp_val = getattr(value, "MessageDefinition53", None)
                setattr(value, "MessageDefinition53", self)

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
    def data55(self):
        return self.__data55

    @data55.setter
    def data55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Data__data55", None)
        self.__data55 = value
        
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
    def Component(self):
        return self.__Component

    @Component.setter
    def Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Component__Component", None)
        self.__Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "data55"):
                opp_val = getattr(old_value, "data55", None)
                if opp_val == self:
                    setattr(old_value, "data55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "data55"):
                opp_val = getattr(value, "data55", None)
                setattr(value, "data55", self)

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

class HALL_UserProfile(Component):

    def __init__(self, numberofcompletedtasks: int, UserProfile32: "HALL_UserProfile" = None, componentSetInv31: set["HALL_UserProfile"] = None, UserProfile36: "HALL_UserProfile" = None, componentSet35: "HALL_UserProfile" = None, UserProfile39: "HALL_TaskObject" = None, UserProfile: "HALL_VisualObject" = None, UserProfile20: "HALL_Model" = None, visualObjectInv: set["HALL_VisualObject"] = None, taskObjectInv: set["HALL_TaskObject"] = None, userProfile: "HALL_Model" = None):
        self.numberofcompletedtasks = numberofcompletedtasks
        self.UserProfile32 = UserProfile32
        self.componentSetInv31 = componentSetInv31 if componentSetInv31 is not None else set()
        self.UserProfile36 = UserProfile36
        self.componentSet35 = componentSet35
        self.UserProfile39 = UserProfile39
        self.UserProfile = UserProfile
        self.UserProfile20 = UserProfile20
        self.visualObjectInv = visualObjectInv if visualObjectInv is not None else set()
        self.taskObjectInv = taskObjectInv if taskObjectInv is not None else set()
        self.userProfile = userProfile
        
        pass
    @property
    def numberofcompletedtasks(self):
        return self.__numberofcompletedtasks

    @numberofcompletedtasks.setter
    def numberofcompletedtasks(self, numberofcompletedtasks: int):
        self.__numberofcompletedtasks = numberofcompletedtasks


    @property
    def componentSet35(self):
        return self.__componentSet35

    @componentSet35.setter
    def componentSet35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_UserProfile__componentSet35", None)
        self.__componentSet35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UserProfile36"):
                opp_val = getattr(old_value, "UserProfile36", None)
                if opp_val == self:
                    setattr(old_value, "UserProfile36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UserProfile36"):
                opp_val = getattr(value, "UserProfile36", None)
                setattr(value, "UserProfile36", self)

    @property
    def componentSetInv31(self):
        return self.__componentSetInv31

    @componentSetInv31.setter
    def componentSetInv31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_UserProfile__componentSetInv31", None)
        self.__componentSetInv31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UserProfile32"):
                    opp_val = getattr(item, "UserProfile32", None)
                    
                    if opp_val == self:
                        setattr(item, "UserProfile32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UserProfile32"):
                    opp_val = getattr(item, "UserProfile32", None)
                    
                    setattr(item, "UserProfile32", self)
                    

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
            if hasattr(old_value, "Model28"):
                opp_val = getattr(old_value, "Model28", None)
                if opp_val == self:
                    setattr(old_value, "Model28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model28"):
                opp_val = getattr(value, "Model28", None)
                setattr(value, "Model28", self)

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
                if hasattr(item, "VisualObject25"):
                    opp_val = getattr(item, "VisualObject25", None)
                    
                    if opp_val == self:
                        setattr(item, "VisualObject25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VisualObject25"):
                    opp_val = getattr(item, "VisualObject25", None)
                    
                    setattr(item, "VisualObject25", self)
                    

    @property
    def UserProfile32(self):
        return self.__UserProfile32

    @UserProfile32.setter
    def UserProfile32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_UserProfile__UserProfile32", None)
        self.__UserProfile32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentSetInv31"):
                opp_val = getattr(old_value, "componentSetInv31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentSetInv31"):
                opp_val = getattr(value, "componentSetInv31", None)
                if opp_val is None:
                    setattr(value, "componentSetInv31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UserProfile36(self):
        return self.__UserProfile36

    @UserProfile36.setter
    def UserProfile36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_UserProfile__UserProfile36", None)
        self.__UserProfile36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentSet35"):
                opp_val = getattr(old_value, "componentSet35", None)
                if opp_val == self:
                    setattr(old_value, "componentSet35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentSet35"):
                opp_val = getattr(value, "componentSet35", None)
                setattr(value, "componentSet35", self)

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
            if hasattr(old_value, "taskObject"):
                opp_val = getattr(old_value, "taskObject", None)
                if opp_val == self:
                    setattr(old_value, "taskObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "taskObject"):
                opp_val = getattr(value, "taskObject", None)
                setattr(value, "taskObject", self)

class FSMActions_HALL_Component:

    pass
class ActionExpressionElement:

    pass
class HALL_FSMActions_UnaryOperator(ActionExpressionElement):

    def __init__(self, operatorname: str, HALL_FSMActions_UnaryOperator: "FSMActions_ActionExpressionElement" = None):
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
            if hasattr(old_value, "FSMActions_ActionExpressionElement296"):
                opp_val = getattr(old_value, "FSMActions_ActionExpressionElement296", None)
                if opp_val == self:
                    setattr(old_value, "FSMActions_ActionExpressionElement296", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMActions_ActionExpressionElement296"):
                opp_val = getattr(value, "FSMActions_ActionExpressionElement296", None)
                setattr(value, "FSMActions_ActionExpressionElement296", self)

class HALL_FSMActions_BinaryOperator(ActionExpressionElement):

    def __init__(self, operatorname: str, HALL_FSMActions_BinaryOperator: "FSMActions_ActionExpressionElement" = None, HALL_FSMActions_BinaryOperator293: "FSMActions_ActionExpressionElement" = None):
        self.operatorname = operatorname
        self.HALL_FSMActions_BinaryOperator = HALL_FSMActions_BinaryOperator
        self.HALL_FSMActions_BinaryOperator293 = HALL_FSMActions_BinaryOperator293
        
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
            if hasattr(old_value, "FSMActions_ActionExpressionElement291"):
                opp_val = getattr(old_value, "FSMActions_ActionExpressionElement291", None)
                if opp_val == self:
                    setattr(old_value, "FSMActions_ActionExpressionElement291", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMActions_ActionExpressionElement291"):
                opp_val = getattr(value, "FSMActions_ActionExpressionElement291", None)
                setattr(value, "FSMActions_ActionExpressionElement291", self)

    @property
    def HALL_FSMActions_BinaryOperator293(self):
        return self.__HALL_FSMActions_BinaryOperator293

    @HALL_FSMActions_BinaryOperator293.setter
    def HALL_FSMActions_BinaryOperator293(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMActions_BinaryOperator__HALL_FSMActions_BinaryOperator293", None)
        self.__HALL_FSMActions_BinaryOperator293 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMActions_ActionExpressionElement294"):
                opp_val = getattr(old_value, "FSMActions_ActionExpressionElement294", None)
                if opp_val == self:
                    setattr(old_value, "FSMActions_ActionExpressionElement294", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMActions_ActionExpressionElement294"):
                opp_val = getattr(value, "FSMActions_ActionExpressionElement294", None)
                setattr(value, "FSMActions_ActionExpressionElement294", self)

class HALL_FSMActions_VarRef(ActionExpressionElement):

    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


class HALL_FSMActions_ActionExpressionElement(ABC):

    pass
class FSMActions_ActionExpressionElement:

    pass
class HALL_FSMActions_ActionExpression(ABC):

    pass
class HALL_FSMActions_GetData(ActionExpressionElement):

    def __init__(self, field: str, HALL_FSMActions_GetData: "FSMActions_HALL_Component" = None):
        self.field = field
        self.HALL_FSMActions_GetData = HALL_FSMActions_GetData
        
        pass
    @property
    def field(self):
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

class FSMConditions_HALL_Component:

    pass
class HALL_FSMActions_DomainPropertySet(ActionExpressionElement):

    def __init__(self, name: str, HALL_FSMActions_DomainPropertySet: "FSMActions_ActionExpressionElement" = None):
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
            if hasattr(old_value, "FSMActions_ActionExpressionElement288"):
                opp_val = getattr(old_value, "FSMActions_ActionExpressionElement288", None)
                if opp_val == self:
                    setattr(old_value, "FSMActions_ActionExpressionElement288", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMActions_ActionExpressionElement288"):
                opp_val = getattr(value, "FSMActions_ActionExpressionElement288", None)
                setattr(value, "FSMActions_ActionExpressionElement288", self)

class HALL_FSMActions_Enable(ActionMessageExpressionElement):

    pass
class HALL_FSMActions_MessageInvocation(ActionExpressionElement):

    def __init__(self, name: str, isTopDown: bool, HALL_FSMActions_MessageInvocation: set["FSMActions_ActionExpressionElement"] = None):
        self.name = name
        self.isTopDown = isTopDown
        self.HALL_FSMActions_MessageInvocation = HALL_FSMActions_MessageInvocation if HALL_FSMActions_MessageInvocation is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def isTopDown(self):
        return self.__isTopDown

    @isTopDown.setter
    def isTopDown(self, isTopDown: bool):
        self.__isTopDown = isTopDown


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
                if hasattr(item, "FSMActions_ActionExpressionElement281"):
                    opp_val = getattr(item, "FSMActions_ActionExpressionElement281", None)
                    
                    if opp_val == self:
                        setattr(item, "FSMActions_ActionExpressionElement281", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FSMActions_ActionExpressionElement281"):
                    opp_val = getattr(item, "FSMActions_ActionExpressionElement281", None)
                    
                    setattr(item, "FSMActions_ActionExpressionElement281", self)
                    

class HALL_FSMActions_Let(ActionExpressionElement):

    def __init__(self, namevar: str, HALL_FSMActions_Let278: "FSMActions_ActionExpressionElement" = None, HALL_FSMActions_Let: "FSMActions_ActionExpressionElement" = None):
        self.namevar = namevar
        self.HALL_FSMActions_Let278 = HALL_FSMActions_Let278
        self.HALL_FSMActions_Let = HALL_FSMActions_Let
        
        pass
    @property
    def namevar(self):
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
    def HALL_FSMActions_Let278(self):
        return self.__HALL_FSMActions_Let278

    @HALL_FSMActions_Let278.setter
    def HALL_FSMActions_Let278(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMActions_Let__HALL_FSMActions_Let278", None)
        self.__HALL_FSMActions_Let278 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMActions_ActionExpressionElement279"):
                opp_val = getattr(old_value, "FSMActions_ActionExpressionElement279", None)
                if opp_val == self:
                    setattr(old_value, "FSMActions_ActionExpressionElement279", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMActions_ActionExpressionElement279"):
                opp_val = getattr(value, "FSMActions_ActionExpressionElement279", None)
                setattr(value, "FSMActions_ActionExpressionElement279", self)

class HALL_FSMActions_DomainPropertyGet(ActionExpressionElement):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class HALL_FSMActions_Literal(ActionExpressionElement):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class PreConditionExpressionElement:

    pass
class HALL_FSMConditions_BinaryOperator(PreConditionExpressionElement):

    def __init__(self, operatorname: str, HALL_FSMConditions_BinaryOperator: "FSMConditions_PreConditionExpressionElement" = None, HALL_FSMConditions_BinaryOperator259: "FSMConditions_PreConditionExpressionElement" = None):
        self.operatorname = operatorname
        self.HALL_FSMConditions_BinaryOperator = HALL_FSMConditions_BinaryOperator
        self.HALL_FSMConditions_BinaryOperator259 = HALL_FSMConditions_BinaryOperator259
        
        pass
    @property
    def operatorname(self):
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
    def HALL_FSMConditions_BinaryOperator259(self):
        return self.__HALL_FSMConditions_BinaryOperator259

    @HALL_FSMConditions_BinaryOperator259.setter
    def HALL_FSMConditions_BinaryOperator259(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMConditions_BinaryOperator__HALL_FSMConditions_BinaryOperator259", None)
        self.__HALL_FSMConditions_BinaryOperator259 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMConditions_PreConditionExpressionElement260"):
                opp_val = getattr(old_value, "FSMConditions_PreConditionExpressionElement260", None)
                if opp_val == self:
                    setattr(old_value, "FSMConditions_PreConditionExpressionElement260", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMConditions_PreConditionExpressionElement260"):
                opp_val = getattr(value, "FSMConditions_PreConditionExpressionElement260", None)
                setattr(value, "FSMConditions_PreConditionExpressionElement260", self)

class HALL_FSMConditions_DomainPropertyGet(PreConditionExpressionElement):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class HALL_FSMConditions_Let(PreConditionExpressionElement):

    def __init__(self, namevar: str, HALL_FSMConditions_Let: "FSMConditions_PreConditionExpressionElement" = None, HALL_FSMConditions_Let269: "FSMConditions_PreConditionExpressionElement" = None):
        self.namevar = namevar
        self.HALL_FSMConditions_Let = HALL_FSMConditions_Let
        self.HALL_FSMConditions_Let269 = HALL_FSMConditions_Let269
        
        pass
    @property
    def namevar(self):
        return self.__namevar

    @namevar.setter
    def namevar(self, namevar: str):
        self.__namevar = namevar


    @property
    def HALL_FSMConditions_Let269(self):
        return self.__HALL_FSMConditions_Let269

    @HALL_FSMConditions_Let269.setter
    def HALL_FSMConditions_Let269(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMConditions_Let__HALL_FSMConditions_Let269", None)
        self.__HALL_FSMConditions_Let269 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMConditions_PreConditionExpressionElement270"):
                opp_val = getattr(old_value, "FSMConditions_PreConditionExpressionElement270", None)
                if opp_val == self:
                    setattr(old_value, "FSMConditions_PreConditionExpressionElement270", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMConditions_PreConditionExpressionElement270"):
                opp_val = getattr(value, "FSMConditions_PreConditionExpressionElement270", None)
                setattr(value, "FSMConditions_PreConditionExpressionElement270", self)

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
            if hasattr(old_value, "FSMConditions_PreConditionExpressionElement267"):
                opp_val = getattr(old_value, "FSMConditions_PreConditionExpressionElement267", None)
                if opp_val == self:
                    setattr(old_value, "FSMConditions_PreConditionExpressionElement267", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMConditions_PreConditionExpressionElement267"):
                opp_val = getattr(value, "FSMConditions_PreConditionExpressionElement267", None)
                setattr(value, "FSMConditions_PreConditionExpressionElement267", self)

class HALL_FSMConditions_VarRef(PreConditionExpressionElement):

    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class HALL_FSMConditions_UnaryOperator(PreConditionExpressionElement):

    def __init__(self, operatorname: str, HALL_FSMConditions_UnaryOperator: "FSMConditions_PreConditionExpressionElement" = None):
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
            if hasattr(old_value, "FSMConditions_PreConditionExpressionElement262"):
                opp_val = getattr(old_value, "FSMConditions_PreConditionExpressionElement262", None)
                if opp_val == self:
                    setattr(old_value, "FSMConditions_PreConditionExpressionElement262", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMConditions_PreConditionExpressionElement262"):
                opp_val = getattr(value, "FSMConditions_PreConditionExpressionElement262", None)
                setattr(value, "FSMConditions_PreConditionExpressionElement262", self)

class HALL_FSMConditions_GetData(PreConditionExpressionElement):

    def __init__(self, field: str, HALL_FSMConditions_GetData: "FSMConditions_HALL_Component" = None):
        self.field = field
        self.HALL_FSMConditions_GetData = HALL_FSMConditions_GetData
        
        pass
    @property
    def field(self):
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
            if hasattr(old_value, "FSMConditions_HALL_Component265"):
                opp_val = getattr(old_value, "FSMConditions_HALL_Component265", None)
                if opp_val == self:
                    setattr(old_value, "FSMConditions_HALL_Component265", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMConditions_HALL_Component265"):
                opp_val = getattr(value, "FSMConditions_HALL_Component265", None)
                setattr(value, "FSMConditions_HALL_Component265", self)

class HALL_FSMConditions_GetState(PreConditionExpressionElement):

    pass
class HALL_FSMConditions_Literal(PreConditionExpressionElement):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
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
class HALL_FSMInstructions_PosConditionExpression(ABC):

    pass
class TriggerExpressionElement:

    pass
class HALL_Trigger_DomainEventFired(TriggerExpressionElement):

    pass
class HALL_Trigger_MessageNotification(TriggerExpressionElement):

    pass
class HALL_Trigger_TriggerExpressionElement(ABC):

    def __init__(self, String: str, TriggerExpressionSet: "Trigger_TriggerExpression" = None):
        self.String = String
        self.TriggerExpressionSet = TriggerExpressionSet
        
        pass
    @property
    def String(self):
        return self.__String

    @String.setter
    def String(self, String: str):
        self.__String = String


    @property
    def TriggerExpressionSet(self):
        return self.__TriggerExpressionSet

    @TriggerExpressionSet.setter
    def TriggerExpressionSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Trigger_TriggerExpressionElement__TriggerExpressionSet", None)
        self.__TriggerExpressionSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TriggerExpression219"):
                opp_val = getattr(old_value, "TriggerExpression219", None)
                if opp_val == self:
                    setattr(old_value, "TriggerExpression219", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TriggerExpression219"):
                opp_val = getattr(value, "TriggerExpression219", None)
                setattr(value, "TriggerExpression219", self)

class FSMInstructions_HALL_Component:

    pass
class PosConditionExpressionElement:

    pass
class HALL_FSMInstructions_DomainPropertyGet(PosConditionExpressionElement):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class HALL_FSMInstructions_GetData(PosConditionExpressionElement):

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

class HALL_FSMInstructions_SetState(PosConditionExpressionElement):

    def __init__(self, name: str, HALL_FSMInstructions_SetState: "FSMInstructions_HALL_Component" = None):
        self.name = name
        self.HALL_FSMInstructions_SetState = HALL_FSMInstructions_SetState
        
        pass
    @property
    def name(self):
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
            if hasattr(old_value, "FSMInstructions_HALL_Component238"):
                opp_val = getattr(old_value, "FSMInstructions_HALL_Component238", None)
                if opp_val == self:
                    setattr(old_value, "FSMInstructions_HALL_Component238", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMInstructions_HALL_Component238"):
                opp_val = getattr(value, "FSMInstructions_HALL_Component238", None)
                setattr(value, "FSMInstructions_HALL_Component238", self)

class HALL_FSMInstructions_UnaryOperator(PosConditionExpressionElement):

    def __init__(self, operatorname: str, HALL_FSMInstructions_UnaryOperator: "FSMInstructions_PosConditionExpressionElement" = None):
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
            if hasattr(old_value, "FSMInstructions_PosConditionExpressionElement233"):
                opp_val = getattr(old_value, "FSMInstructions_PosConditionExpressionElement233", None)
                if opp_val == self:
                    setattr(old_value, "FSMInstructions_PosConditionExpressionElement233", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMInstructions_PosConditionExpressionElement233"):
                opp_val = getattr(value, "FSMInstructions_PosConditionExpressionElement233", None)
                setattr(value, "FSMInstructions_PosConditionExpressionElement233", self)

class HALL_FSMInstructions_SetData(PosConditionExpressionElement):

    def __init__(self, field: str, HALL_FSMInstructions_SetData: "FSMInstructions_PosConditionExpressionElement" = None, HALL_FSMInstructions_SetData242: "FSMInstructions_HALL_Component" = None):
        self.field = field
        self.HALL_FSMInstructions_SetData = HALL_FSMInstructions_SetData
        self.HALL_FSMInstructions_SetData242 = HALL_FSMInstructions_SetData242
        
        pass
    @property
    def field(self):
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field


    @property
    def HALL_FSMInstructions_SetData242(self):
        return self.__HALL_FSMInstructions_SetData242

    @HALL_FSMInstructions_SetData242.setter
    def HALL_FSMInstructions_SetData242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMInstructions_SetData__HALL_FSMInstructions_SetData242", None)
        self.__HALL_FSMInstructions_SetData242 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMInstructions_HALL_Component243"):
                opp_val = getattr(old_value, "FSMInstructions_HALL_Component243", None)
                if opp_val == self:
                    setattr(old_value, "FSMInstructions_HALL_Component243", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMInstructions_HALL_Component243"):
                opp_val = getattr(value, "FSMInstructions_HALL_Component243", None)
                setattr(value, "FSMInstructions_HALL_Component243", self)

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
            if hasattr(old_value, "FSMInstructions_PosConditionExpressionElement240"):
                opp_val = getattr(old_value, "FSMInstructions_PosConditionExpressionElement240", None)
                if opp_val == self:
                    setattr(old_value, "FSMInstructions_PosConditionExpressionElement240", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMInstructions_PosConditionExpressionElement240"):
                opp_val = getattr(value, "FSMInstructions_PosConditionExpressionElement240", None)
                setattr(value, "FSMInstructions_PosConditionExpressionElement240", self)

class HALL_FSMInstructions_Let(PosConditionExpressionElement):

    def __init__(self, namevar: str, HALL_FSMInstructions_Let: "FSMInstructions_PosConditionExpressionElement" = None, HALL_FSMInstructions_Let247: "FSMInstructions_PosConditionExpressionElement" = None):
        self.namevar = namevar
        self.HALL_FSMInstructions_Let = HALL_FSMInstructions_Let
        self.HALL_FSMInstructions_Let247 = HALL_FSMInstructions_Let247
        
        pass
    @property
    def namevar(self):
        return self.__namevar

    @namevar.setter
    def namevar(self, namevar: str):
        self.__namevar = namevar


    @property
    def HALL_FSMInstructions_Let247(self):
        return self.__HALL_FSMInstructions_Let247

    @HALL_FSMInstructions_Let247.setter
    def HALL_FSMInstructions_Let247(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMInstructions_Let__HALL_FSMInstructions_Let247", None)
        self.__HALL_FSMInstructions_Let247 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMInstructions_PosConditionExpressionElement248"):
                opp_val = getattr(old_value, "FSMInstructions_PosConditionExpressionElement248", None)
                if opp_val == self:
                    setattr(old_value, "FSMInstructions_PosConditionExpressionElement248", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMInstructions_PosConditionExpressionElement248"):
                opp_val = getattr(value, "FSMInstructions_PosConditionExpressionElement248", None)
                setattr(value, "FSMInstructions_PosConditionExpressionElement248", self)

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
            if hasattr(old_value, "FSMInstructions_PosConditionExpressionElement245"):
                opp_val = getattr(old_value, "FSMInstructions_PosConditionExpressionElement245", None)
                if opp_val == self:
                    setattr(old_value, "FSMInstructions_PosConditionExpressionElement245", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMInstructions_PosConditionExpressionElement245"):
                opp_val = getattr(value, "FSMInstructions_PosConditionExpressionElement245", None)
                setattr(value, "FSMInstructions_PosConditionExpressionElement245", self)

class HALL_FSMInstructions_GetState(PosConditionExpressionElement):

    pass
class HALL_FSMInstructions_Literal(PosConditionExpressionElement):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class HALL_FSMInstructions_BinaryOperator(PosConditionExpressionElement):

    def __init__(self, operatorname: str, HALL_FSMInstructions_BinaryOperator: "FSMInstructions_PosConditionExpressionElement" = None, HALL_FSMInstructions_BinaryOperator230: "FSMInstructions_PosConditionExpressionElement" = None):
        self.operatorname = operatorname
        self.HALL_FSMInstructions_BinaryOperator = HALL_FSMInstructions_BinaryOperator
        self.HALL_FSMInstructions_BinaryOperator230 = HALL_FSMInstructions_BinaryOperator230
        
        pass
    @property
    def operatorname(self):
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
    def HALL_FSMInstructions_BinaryOperator230(self):
        return self.__HALL_FSMInstructions_BinaryOperator230

    @HALL_FSMInstructions_BinaryOperator230.setter
    def HALL_FSMInstructions_BinaryOperator230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMInstructions_BinaryOperator__HALL_FSMInstructions_BinaryOperator230", None)
        self.__HALL_FSMInstructions_BinaryOperator230 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMInstructions_PosConditionExpressionElement231"):
                opp_val = getattr(old_value, "FSMInstructions_PosConditionExpressionElement231", None)
                if opp_val == self:
                    setattr(old_value, "FSMInstructions_PosConditionExpressionElement231", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMInstructions_PosConditionExpressionElement231"):
                opp_val = getattr(value, "FSMInstructions_PosConditionExpressionElement231", None)
                setattr(value, "FSMInstructions_PosConditionExpressionElement231", self)

class HALL_FSMInstructions_VarRef(PosConditionExpressionElement):

    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


class HALL_FSMInstructions_PosConditionExpressionElement(ABC):

    pass
class FSMInstructions_PosConditionExpressionElement:

    pass
class HALL_Actions_Enable(ActionMessageExpressionElement):

    pass
class HALL_Actions_DomainPropertySet(ActionMessageExpressionElement):

    def __init__(self, name: str, HALL_Actions_DomainPropertySet: "Actions_ActionMessageExpressionElement" = None):
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
            if hasattr(old_value, "Actions_ActionMessageExpressionElement188"):
                opp_val = getattr(old_value, "Actions_ActionMessageExpressionElement188", None)
                if opp_val == self:
                    setattr(old_value, "Actions_ActionMessageExpressionElement188", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Actions_ActionMessageExpressionElement188"):
                opp_val = getattr(value, "Actions_ActionMessageExpressionElement188", None)
                setattr(value, "Actions_ActionMessageExpressionElement188", self)

class Actions_HALL_Component:

    pass
class Trigger_TriggerExpressionElement:

    pass