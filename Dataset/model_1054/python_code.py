from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class AbstractState:

    pass
class FSM_State(AbstractState):

    pass
class FSM_EndState(AbstractState):

    pass
class FSM_StartState(AbstractState):

    pass
class FSM_Transition:

    pass
class FSM_AbstractState(ABC):

    def __init__(self, name: str, envs: str, FSM_AbstractState: "FSM_StateMachine" = None, FSM_AbstractState7: set["FSM_Transition"] = None, FSM_AbstractState4: set["FSM_Transition"] = None):
        self.name = name
        self.envs = envs
        self.FSM_AbstractState = FSM_AbstractState
        self.FSM_AbstractState7 = FSM_AbstractState7 if FSM_AbstractState7 is not None else set()
        self.FSM_AbstractState4 = FSM_AbstractState4 if FSM_AbstractState4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def envs(self) -> str:
        return self.__envs

    @envs.setter
    def envs(self, envs: str):
        self.__envs = envs

    @property
    def FSM_AbstractState7(self):
        return self.__FSM_AbstractState7

    @FSM_AbstractState7.setter
    def FSM_AbstractState7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_AbstractState__FSM_AbstractState7", None)
        self.__FSM_AbstractState7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FSM_Transition8"):
                    opp_val = getattr(item, "FSM_Transition8", None)
                    
                    if opp_val == self:
                        setattr(item, "FSM_Transition8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FSM_Transition8"):
                    opp_val = getattr(item, "FSM_Transition8", None)
                    
                    setattr(item, "FSM_Transition8", self)
                    

    @property
    def FSM_AbstractState(self):
        return self.__FSM_AbstractState

    @FSM_AbstractState.setter
    def FSM_AbstractState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_AbstractState__FSM_AbstractState", None)
        self.__FSM_AbstractState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM_StateMachine"):
                opp_val = getattr(old_value, "FSM_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM_StateMachine"):
                opp_val = getattr(value, "FSM_StateMachine", None)
                if opp_val is None:
                    setattr(value, "FSM_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def FSM_AbstractState4(self):
        return self.__FSM_AbstractState4

    @FSM_AbstractState4.setter
    def FSM_AbstractState4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_AbstractState__FSM_AbstractState4", None)
        self.__FSM_AbstractState4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FSM_Transition5"):
                    opp_val = getattr(item, "FSM_Transition5", None)
                    
                    if opp_val == self:
                        setattr(item, "FSM_Transition5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FSM_Transition5"):
                    opp_val = getattr(item, "FSM_Transition5", None)
                    
                    setattr(item, "FSM_Transition5", self)
                    

class FSM_StateMachine:

    def __init__(self, code: str, FSM_StateMachine: set["FSM_AbstractState"] = None, FSM_StateMachine2: set["FSM_Transition"] = None):
        self.code = code
        self.FSM_StateMachine = FSM_StateMachine if FSM_StateMachine is not None else set()
        self.FSM_StateMachine2 = FSM_StateMachine2 if FSM_StateMachine2 is not None else set()
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def FSM_StateMachine2(self):
        return self.__FSM_StateMachine2

    @FSM_StateMachine2.setter
    def FSM_StateMachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_StateMachine__FSM_StateMachine2", None)
        self.__FSM_StateMachine2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FSM_Transition"):
                    opp_val = getattr(item, "FSM_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "FSM_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FSM_Transition"):
                    opp_val = getattr(item, "FSM_Transition", None)
                    
                    setattr(item, "FSM_Transition", self)
                    

    @property
    def FSM_StateMachine(self):
        return self.__FSM_StateMachine

    @FSM_StateMachine.setter
    def FSM_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_StateMachine__FSM_StateMachine", None)
        self.__FSM_StateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FSM_AbstractState"):
                    opp_val = getattr(item, "FSM_AbstractState", None)
                    
                    if opp_val == self:
                        setattr(item, "FSM_AbstractState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FSM_AbstractState"):
                    opp_val = getattr(item, "FSM_AbstractState", None)
                    
                    setattr(item, "FSM_AbstractState", self)
                    
