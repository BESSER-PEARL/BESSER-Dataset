from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class StateMachine_WashingMachine:

    pass
class State:

    pass
class StateMachine_UnNamedState(State):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class StateMachine_NamedState(State):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class StateMachine_Transition:

    def __init__(self, action: str, trigger: str, id: int, name: str, StateMachine_Transition: "StateMachine_State" = None, StateMachine_Transition2: "StateMachine_State" = None, StateMachine_Transition5: "StateMachine_State" = None, StateMachine_Transition11: "StateMachine_WashingMachine" = None):
        self.action = action
        self.trigger = trigger
        self.id = id
        self.name = name
        self.StateMachine_Transition = StateMachine_Transition
        self.StateMachine_Transition2 = StateMachine_Transition2
        self.StateMachine_Transition5 = StateMachine_Transition5
        self.StateMachine_Transition11 = StateMachine_Transition11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def trigger(self) -> str:
        return self.__trigger

    @trigger.setter
    def trigger(self, trigger: str):
        self.__trigger = trigger

    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def StateMachine_Transition2(self):
        return self.__StateMachine_Transition2

    @StateMachine_Transition2.setter
    def StateMachine_Transition2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Transition__StateMachine_Transition2", None)
        self.__StateMachine_Transition2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine_State3"):
                opp_val = getattr(old_value, "StateMachine_State3", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine_State3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine_State3"):
                opp_val = getattr(value, "StateMachine_State3", None)
                setattr(value, "StateMachine_State3", self)

    @property
    def StateMachine_Transition(self):
        return self.__StateMachine_Transition

    @StateMachine_Transition.setter
    def StateMachine_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Transition__StateMachine_Transition", None)
        self.__StateMachine_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine_State"):
                opp_val = getattr(old_value, "StateMachine_State", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine_State"):
                opp_val = getattr(value, "StateMachine_State", None)
                if opp_val is None:
                    setattr(value, "StateMachine_State", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def StateMachine_Transition11(self):
        return self.__StateMachine_Transition11

    @StateMachine_Transition11.setter
    def StateMachine_Transition11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Transition__StateMachine_Transition11", None)
        self.__StateMachine_Transition11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine_WashingMachine10"):
                opp_val = getattr(old_value, "StateMachine_WashingMachine10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine_WashingMachine10"):
                opp_val = getattr(value, "StateMachine_WashingMachine10", None)
                if opp_val is None:
                    setattr(value, "StateMachine_WashingMachine10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def StateMachine_Transition5(self):
        return self.__StateMachine_Transition5

    @StateMachine_Transition5.setter
    def StateMachine_Transition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Transition__StateMachine_Transition5", None)
        self.__StateMachine_Transition5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine_State6"):
                opp_val = getattr(old_value, "StateMachine_State6", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine_State6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine_State6"):
                opp_val = getattr(value, "StateMachine_State6", None)
                setattr(value, "StateMachine_State6", self)

class StateMachine_State(ABC):

    pass