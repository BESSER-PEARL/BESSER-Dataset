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

class emf_Transition:

    def __init__(self, action: str, emf_Transition: "emf_State" = None, emf_Transition10: "emf_TransitionToStateMapEntry" = None):
        self.action = action
        self.emf_Transition = emf_Transition
        self.emf_Transition10 = emf_Transition10
        
    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

    @property
    def emf_Transition10(self):
        return self.__emf_Transition10

    @emf_Transition10.setter
    def emf_Transition10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emf_Transition__emf_Transition10", None)
        self.__emf_Transition10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emf_TransitionToStateMapEntry9"):
                opp_val = getattr(old_value, "emf_TransitionToStateMapEntry9", None)
                if opp_val == self:
                    setattr(old_value, "emf_TransitionToStateMapEntry9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emf_TransitionToStateMapEntry9"):
                opp_val = getattr(value, "emf_TransitionToStateMapEntry9", None)
                setattr(value, "emf_TransitionToStateMapEntry9", self)

    @property
    def emf_Transition(self):
        return self.__emf_Transition

    @emf_Transition.setter
    def emf_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emf_Transition__emf_Transition", None)
        self.__emf_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emf_State7"):
                opp_val = getattr(old_value, "emf_State7", None)
                if opp_val == self:
                    setattr(old_value, "emf_State7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emf_State7"):
                opp_val = getattr(value, "emf_State7", None)
                setattr(value, "emf_State7", self)

class emf_TransitionToStateMapEntry:

    pass
class emf_Action:

    def __init__(self, event: str):
        self.event = event
        
    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

class emf_StateMachine:

    pass
class emf_State:

    def __init__(self, type: str, name: str, emf_State: set["emf_StateMachine"] = None, emf_State3: "emf_StateMachine" = None, emf_State13: "emf_TransitionToStateMapEntry" = None, emf_State7: "emf_Transition" = None):
        self.type = type
        self.name = name
        self.emf_State = emf_State if emf_State is not None else set()
        self.emf_State3 = emf_State3
        self.emf_State13 = emf_State13
        self.emf_State7 = emf_State7
        
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
    def emf_State7(self):
        return self.__emf_State7

    @emf_State7.setter
    def emf_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emf_State__emf_State7", None)
        self.__emf_State7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emf_Transition"):
                opp_val = getattr(old_value, "emf_Transition", None)
                if opp_val == self:
                    setattr(old_value, "emf_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emf_Transition"):
                opp_val = getattr(value, "emf_Transition", None)
                setattr(value, "emf_Transition", self)

    @property
    def emf_State(self):
        return self.__emf_State

    @emf_State.setter
    def emf_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emf_State__emf_State", None)
        self.__emf_State = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "emf_StateMachine"):
                    opp_val = getattr(item, "emf_StateMachine", None)
                    
                    if opp_val == self:
                        setattr(item, "emf_StateMachine", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "emf_StateMachine"):
                    opp_val = getattr(item, "emf_StateMachine", None)
                    
                    setattr(item, "emf_StateMachine", self)
                    

    @property
    def emf_State13(self):
        return self.__emf_State13

    @emf_State13.setter
    def emf_State13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emf_State__emf_State13", None)
        self.__emf_State13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emf_TransitionToStateMapEntry12"):
                opp_val = getattr(old_value, "emf_TransitionToStateMapEntry12", None)
                if opp_val == self:
                    setattr(old_value, "emf_TransitionToStateMapEntry12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emf_TransitionToStateMapEntry12"):
                opp_val = getattr(value, "emf_TransitionToStateMapEntry12", None)
                setattr(value, "emf_TransitionToStateMapEntry12", self)

    @property
    def emf_State3(self):
        return self.__emf_State3

    @emf_State3.setter
    def emf_State3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emf_State__emf_State3", None)
        self.__emf_State3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emf_StateMachine2"):
                opp_val = getattr(old_value, "emf_StateMachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emf_StateMachine2"):
                opp_val = getattr(value, "emf_StateMachine2", None)
                if opp_val is None:
                    setattr(value, "emf_StateMachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
