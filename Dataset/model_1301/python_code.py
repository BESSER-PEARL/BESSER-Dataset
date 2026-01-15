from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class StateKind(Enum):
    DEFAULT = "DEFAULT"
    FINAL = "FINAL"
    INITIAL = "INITIAL"


############################################
# Definition of Classes
############################################

class IDElement:

    pass
class stateMachine_Event(IDElement):

    pass
class stateMachine_Transition(IDElement):

    pass
class stateMachine_State(IDElement):

    def __init__(self, kind: str, State: "stateMachine_Transition" = None, State10: "stateMachine_Transition" = None, stateMachine_State: "stateMachine_StateMachine" = None, source: set["stateMachine_Transition"] = None, target: set["stateMachine_Transition"] = None):
        self.kind = kind
        self.State = State
        self.State10 = State10
        self.stateMachine_State = stateMachine_State
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_State__source", None)
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
                    

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_State__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition7"):
                    opp_val = getattr(item, "Transition7", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition7"):
                    opp_val = getattr(item, "Transition7", None)
                    
                    setattr(item, "Transition7", self)
                    

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_State__State", None)
        self.__State = value
        
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
    def stateMachine_State(self):
        return self.__stateMachine_State

    @stateMachine_State.setter
    def stateMachine_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_State__stateMachine_State", None)
        self.__stateMachine_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_StateMachine"):
                opp_val = getattr(old_value, "stateMachine_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_StateMachine"):
                opp_val = getattr(value, "stateMachine_StateMachine", None)
                if opp_val is None:
                    setattr(value, "stateMachine_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def State10(self):
        return self.__State10

    @State10.setter
    def State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_State__State10", None)
        self.__State10 = value
        
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

class stateMachine_StateMachine(IDElement):

    pass
class stateMachine_IDElement:

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id
