from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class statemachine_StateMachine:

    def __init__(self, name: str, statemachine_StateMachine: set["statemachine_Transition"] = None):
        self.name = name
        self.statemachine_StateMachine = statemachine_StateMachine if statemachine_StateMachine is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statemachine_StateMachine(self):
        return self.__statemachine_StateMachine

    @statemachine_StateMachine.setter
    def statemachine_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_StateMachine__statemachine_StateMachine", None)
        self.__statemachine_StateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_Transition"):
                    opp_val = getattr(item, "statemachine_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_Transition"):
                    opp_val = getattr(item, "statemachine_Transition", None)
                    
                    setattr(item, "statemachine_Transition", self)
                    

class State:

    pass
class statemachine_Final(State):

    pass
class statemachine_Simple(State):

    pass
class statemachine_Initial(State):

    pass
class statemachine_State(ABC):

    def __init__(self, name: str, statemachine_State: "statemachine_Transition" = None, statemachine_State5: "statemachine_Transition" = None):
        self.name = name
        self.statemachine_State = statemachine_State
        self.statemachine_State5 = statemachine_State5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statemachine_State5(self):
        return self.__statemachine_State5

    @statemachine_State5.setter
    def statemachine_State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State5", None)
        self.__statemachine_State5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Transition4"):
                opp_val = getattr(old_value, "statemachine_Transition4", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Transition4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Transition4"):
                opp_val = getattr(value, "statemachine_Transition4", None)
                setattr(value, "statemachine_Transition4", self)

    @property
    def statemachine_State(self):
        return self.__statemachine_State

    @statemachine_State.setter
    def statemachine_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State", None)
        self.__statemachine_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Transition2"):
                opp_val = getattr(old_value, "statemachine_Transition2", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Transition2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Transition2"):
                opp_val = getattr(value, "statemachine_Transition2", None)
                setattr(value, "statemachine_Transition2", self)

class statemachine_Transition:

    def __init__(self, Id: int, statemachine_Transition: "statemachine_StateMachine" = None, statemachine_Transition2: "statemachine_State" = None, statemachine_Transition4: "statemachine_State" = None):
        self.Id = Id
        self.statemachine_Transition = statemachine_Transition
        self.statemachine_Transition2 = statemachine_Transition2
        self.statemachine_Transition4 = statemachine_Transition4
        
    @property
    def Id(self) -> int:
        return self.__Id

    @Id.setter
    def Id(self, Id: int):
        self.__Id = Id

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
            if hasattr(old_value, "statemachine_State5"):
                opp_val = getattr(old_value, "statemachine_State5", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_State5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_State5"):
                opp_val = getattr(value, "statemachine_State5", None)
                setattr(value, "statemachine_State5", self)

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
            if hasattr(old_value, "statemachine_StateMachine"):
                opp_val = getattr(old_value, "statemachine_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_StateMachine"):
                opp_val = getattr(value, "statemachine_StateMachine", None)
                if opp_val is None:
                    setattr(value, "statemachine_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachine_Transition2(self):
        return self.__statemachine_Transition2

    @statemachine_Transition2.setter
    def statemachine_Transition2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Transition__statemachine_Transition2", None)
        self.__statemachine_Transition2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_State"):
                opp_val = getattr(old_value, "statemachine_State", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_State"):
                opp_val = getattr(value, "statemachine_State", None)
                setattr(value, "statemachine_State", self)
