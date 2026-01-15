from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ActionKind(Enum):
    ENTRY = "ENTRY"
    EXIT = "EXIT"


############################################
# Definition of Classes
############################################

class NumberValue:

    pass
class statemachine_LongValue(NumberValue):

    pass
class Value:

    pass
class statemachine_ConstantValue(Value):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class statemachine_GetParameter(Value):

    pass
class statemachine_Call(Value):

    def __init__(self, actionId: str, statemachine_Call: "statemachine_CallAction" = None):
        self.actionId = actionId
        self.statemachine_Call = statemachine_Call
        
    @property
    def actionId(self) -> str:
        return self.__actionId

    @actionId.setter
    def actionId(self, actionId: str):
        self.__actionId = actionId

    @property
    def statemachine_Call(self):
        return self.__statemachine_Call

    @statemachine_Call.setter
    def statemachine_Call(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Call__statemachine_Call", None)
        self.__statemachine_Call = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_CallAction"):
                opp_val = getattr(old_value, "statemachine_CallAction", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_CallAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_CallAction"):
                opp_val = getattr(value, "statemachine_CallAction", None)
                setattr(value, "statemachine_CallAction", self)

class GAbstractAction:

    pass
class statemachine_CallAction(GAbstractAction):

    pass
class ConstantValue:

    pass
class statemachine_StringValue(ConstantValue):

    pass
class statemachine_BooleanValue(ConstantValue):

    pass
class statemachine_NumberValue(ConstantValue):

    pass
class GCompositeState:

    pass
class statemachine_GStatemachine(GCompositeState):

    def __init__(self, package: str, statemachine_GStatemachine: set["statemachine_Parameter"] = None):
        self.package = package
        self.statemachine_GStatemachine = statemachine_GStatemachine if statemachine_GStatemachine is not None else set()
        
    @property
    def package(self) -> str:
        return self.__package

    @package.setter
    def package(self, package: str):
        self.__package = package

    @property
    def statemachine_GStatemachine(self):
        return self.__statemachine_GStatemachine

    @statemachine_GStatemachine.setter
    def statemachine_GStatemachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_GStatemachine__statemachine_GStatemachine", None)
        self.__statemachine_GStatemachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_Parameter"):
                    opp_val = getattr(item, "statemachine_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_Parameter"):
                    opp_val = getattr(item, "statemachine_Parameter", None)
                    
                    setattr(item, "statemachine_Parameter", self)
                    

class GState:

    pass
class statemachine_GCompositeState(GState):

    pass
class statemachine_Value(ABC):

    pass
class GAbstractState:

    pass
class statemachine_GStartState(GAbstractState):

    pass
class statemachine_GStopState(GAbstractState):

    pass
class Named:

    pass
class statemachine_Transition(Named):

    def __init__(self, preserveTimers: bool, statemachine_Transition4: "statemachine_GAbstractState" = None, statemachine_Transition: "statemachine_GAbstractState" = None, statemachine_Transition7: "statemachine_Value" = None, statemachine_Transition9: "statemachine_Value" = None, statemachine_Transition12: set["statemachine_Value"] = None, statemachine_Transition18: "statemachine_GCompositeState" = None):
        self.preserveTimers = preserveTimers
        self.statemachine_Transition4 = statemachine_Transition4
        self.statemachine_Transition = statemachine_Transition
        self.statemachine_Transition7 = statemachine_Transition7
        self.statemachine_Transition9 = statemachine_Transition9
        self.statemachine_Transition12 = statemachine_Transition12 if statemachine_Transition12 is not None else set()
        self.statemachine_Transition18 = statemachine_Transition18
        
    @property
    def preserveTimers(self) -> bool:
        return self.__preserveTimers

    @preserveTimers.setter
    def preserveTimers(self, preserveTimers: bool):
        self.__preserveTimers = preserveTimers

    @property
    def statemachine_Transition4(self):
        return self.__statemachine_Transition4

    @statemachine_Transition4.setter
    def statemachine_Transition4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Transition__statemachine_Transition4", None)
        self.__statemachine_Transition4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_GAbstractState5"):
                opp_val = getattr(old_value, "statemachine_GAbstractState5", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_GAbstractState5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_GAbstractState5"):
                opp_val = getattr(value, "statemachine_GAbstractState5", None)
                setattr(value, "statemachine_GAbstractState5", self)

    @property
    def statemachine_Transition(self):
        return self.__statemachine_Transition

    @statemachine_Transition.setter
    def statemachine_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Transition__statemachine_Transition", None)
        self.__statemachine_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_GAbstractState2"):
                opp_val = getattr(old_value, "statemachine_GAbstractState2", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_GAbstractState2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_GAbstractState2"):
                opp_val = getattr(value, "statemachine_GAbstractState2", None)
                setattr(value, "statemachine_GAbstractState2", self)

    @property
    def statemachine_Transition18(self):
        return self.__statemachine_Transition18

    @statemachine_Transition18.setter
    def statemachine_Transition18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Transition__statemachine_Transition18", None)
        self.__statemachine_Transition18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_GCompositeState17"):
                opp_val = getattr(old_value, "statemachine_GCompositeState17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_GCompositeState17"):
                opp_val = getattr(value, "statemachine_GCompositeState17", None)
                if opp_val is None:
                    setattr(value, "statemachine_GCompositeState17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachine_Transition12(self):
        return self.__statemachine_Transition12

    @statemachine_Transition12.setter
    def statemachine_Transition12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Transition__statemachine_Transition12", None)
        self.__statemachine_Transition12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_Value13"):
                    opp_val = getattr(item, "statemachine_Value13", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_Value13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_Value13"):
                    opp_val = getattr(item, "statemachine_Value13", None)
                    
                    setattr(item, "statemachine_Value13", self)
                    

    @property
    def statemachine_Transition9(self):
        return self.__statemachine_Transition9

    @statemachine_Transition9.setter
    def statemachine_Transition9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Transition__statemachine_Transition9", None)
        self.__statemachine_Transition9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Value10"):
                opp_val = getattr(old_value, "statemachine_Value10", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Value10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Value10"):
                opp_val = getattr(value, "statemachine_Value10", None)
                setattr(value, "statemachine_Value10", self)

    @property
    def statemachine_Transition7(self):
        return self.__statemachine_Transition7

    @statemachine_Transition7.setter
    def statemachine_Transition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Transition__statemachine_Transition7", None)
        self.__statemachine_Transition7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Value"):
                opp_val = getattr(old_value, "statemachine_Value", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Value", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Value"):
                opp_val = getattr(value, "statemachine_Value", None)
                setattr(value, "statemachine_Value", self)

class statemachine_Parameter(Named):

    pass
class statemachine_GState(Named, GAbstractState):

    pass
class statemachine_GAbstractAction(ABC):

    def __init__(self, kind: str, statemachine_GAbstractAction: "statemachine_GAbstractState" = None):
        self.kind = kind
        self.statemachine_GAbstractAction = statemachine_GAbstractAction
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def statemachine_GAbstractAction(self):
        return self.__statemachine_GAbstractAction

    @statemachine_GAbstractAction.setter
    def statemachine_GAbstractAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_GAbstractAction__statemachine_GAbstractAction", None)
        self.__statemachine_GAbstractAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_GAbstractState"):
                opp_val = getattr(old_value, "statemachine_GAbstractState", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_GAbstractState"):
                opp_val = getattr(value, "statemachine_GAbstractState", None)
                if opp_val is None:
                    setattr(value, "statemachine_GAbstractState", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statemachine_GAbstractState(ABC):

    pass
class statemachine_Named:

    def __init__(self, name: str, comment: str):
        self.name = name
        self.comment = comment
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
