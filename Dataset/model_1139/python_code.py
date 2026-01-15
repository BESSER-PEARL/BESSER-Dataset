from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class StateType(Enum):
    NONE = "NONE"
    INITIAL = "INITIAL"
    FINAL = "FINAL"


############################################
# Definition of Classes
############################################

class statemodel_Transition:

    def __init__(self, guard: str, action: str, statemodel_Transition: "statemodel_TransitionBlock" = None, statemodel_Transition8: "statemodel_State" = None):
        self.guard = guard
        self.action = action
        self.statemodel_Transition = statemodel_Transition
        self.statemodel_Transition8 = statemodel_Transition8
        
    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

    @property
    def guard(self) -> str:
        return self.__guard

    @guard.setter
    def guard(self, guard: str):
        self.__guard = guard

    @property
    def statemodel_Transition8(self):
        return self.__statemodel_Transition8

    @statemodel_Transition8.setter
    def statemodel_Transition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemodel_Transition__statemodel_Transition8", None)
        self.__statemodel_Transition8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemodel_State9"):
                opp_val = getattr(old_value, "statemodel_State9", None)
                if opp_val == self:
                    setattr(old_value, "statemodel_State9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemodel_State9"):
                opp_val = getattr(value, "statemodel_State9", None)
                setattr(value, "statemodel_State9", self)

    @property
    def statemodel_Transition(self):
        return self.__statemodel_Transition

    @statemodel_Transition.setter
    def statemodel_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemodel_Transition__statemodel_Transition", None)
        self.__statemodel_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemodel_TransitionBlock"):
                opp_val = getattr(old_value, "statemodel_TransitionBlock", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemodel_TransitionBlock"):
                opp_val = getattr(value, "statemodel_TransitionBlock", None)
                if opp_val is None:
                    setattr(value, "statemodel_TransitionBlock", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statemodel_Activity:

    pass
class Activity:

    pass
class statemodel_TransitionBlock(Activity):

    def __init__(self, event: str, statemodel_TransitionBlock: set["statemodel_Transition"] = None):
        self.event = event
        self.statemodel_TransitionBlock = statemodel_TransitionBlock if statemodel_TransitionBlock is not None else set()
        
    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def statemodel_TransitionBlock(self):
        return self.__statemodel_TransitionBlock

    @statemodel_TransitionBlock.setter
    def statemodel_TransitionBlock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemodel_TransitionBlock__statemodel_TransitionBlock", None)
        self.__statemodel_TransitionBlock = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemodel_Transition"):
                    opp_val = getattr(item, "statemodel_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "statemodel_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemodel_Transition"):
                    opp_val = getattr(item, "statemodel_Transition", None)
                    
                    setattr(item, "statemodel_Transition", self)
                    

class statemodel_Model:

    pass
class Element:

    pass
class statemodel_State(Element, Activity):

    def __init__(self, type: str, name: str, statemodel_State: "statemodel_Statemachine" = None, statemodel_State5: set["statemodel_Activity"] = None, statemodel_State9: "statemodel_Transition" = None):
        self.type = type
        self.name = name
        self.statemodel_State = statemodel_State
        self.statemodel_State5 = statemodel_State5 if statemodel_State5 is not None else set()
        self.statemodel_State9 = statemodel_State9
        
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

    @property
    def statemodel_State5(self):
        return self.__statemodel_State5

    @statemodel_State5.setter
    def statemodel_State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemodel_State__statemodel_State5", None)
        self.__statemodel_State5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemodel_Activity"):
                    opp_val = getattr(item, "statemodel_Activity", None)
                    
                    if opp_val == self:
                        setattr(item, "statemodel_Activity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemodel_Activity"):
                    opp_val = getattr(item, "statemodel_Activity", None)
                    
                    setattr(item, "statemodel_Activity", self)
                    

    @property
    def statemodel_State9(self):
        return self.__statemodel_State9

    @statemodel_State9.setter
    def statemodel_State9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemodel_State__statemodel_State9", None)
        self.__statemodel_State9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemodel_Transition8"):
                opp_val = getattr(old_value, "statemodel_Transition8", None)
                if opp_val == self:
                    setattr(old_value, "statemodel_Transition8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemodel_Transition8"):
                opp_val = getattr(value, "statemodel_Transition8", None)
                setattr(value, "statemodel_Transition8", self)

    @property
    def statemodel_State(self):
        return self.__statemodel_State

    @statemodel_State.setter
    def statemodel_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemodel_State__statemodel_State", None)
        self.__statemodel_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemodel_Statemachine"):
                opp_val = getattr(old_value, "statemodel_Statemachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemodel_Statemachine"):
                opp_val = getattr(value, "statemodel_Statemachine", None)
                if opp_val is None:
                    setattr(value, "statemodel_Statemachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statemodel_Statemachine(Element):

    pass
class statemodel_Element:

    pass
class statemodel_Import:

    def __init__(self, importURI: str, statemodel_Import: "statemodel_Model" = None):
        self.importURI = importURI
        self.statemodel_Import = statemodel_Import
        
    @property
    def importURI(self) -> str:
        return self.__importURI

    @importURI.setter
    def importURI(self, importURI: str):
        self.__importURI = importURI

    @property
    def statemodel_Import(self):
        return self.__statemodel_Import

    @statemodel_Import.setter
    def statemodel_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemodel_Import__statemodel_Import", None)
        self.__statemodel_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemodel_Model"):
                opp_val = getattr(old_value, "statemodel_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemodel_Model"):
                opp_val = getattr(value, "statemodel_Model", None)
                if opp_val is None:
                    setattr(value, "statemodel_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
