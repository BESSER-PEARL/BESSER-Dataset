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

    def __init__(self, name: str, envs: str, AbstractState: "FSM_StateMachine" = None, src: set["FSM_Transition"] = None, tar: set["FSM_Transition"] = None, states: "FSM_StateMachine" = None, AbstractState9: "FSM_Transition" = None, AbstractState11: "FSM_Transition" = None):
        self.name = name
        self.envs = envs
        self.AbstractState = AbstractState
        self.src = src if src is not None else set()
        self.tar = tar if tar is not None else set()
        self.states = states
        self.AbstractState9 = AbstractState9
        self.AbstractState11 = AbstractState11
        
    @property
    def envs(self) -> str:
        return self.__envs

    @envs.setter
    def envs(self, envs: str):
        self.__envs = envs

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def states(self):
        return self.__states

    @states.setter
    def states(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_AbstractState__states", None)
        self.__states = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine"):
                opp_val = getattr(old_value, "StateMachine", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine"):
                opp_val = getattr(value, "StateMachine", None)
                setattr(value, "StateMachine", self)

    @property
    def AbstractState(self):
        return self.__AbstractState

    @AbstractState.setter
    def AbstractState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_AbstractState__AbstractState", None)
        self.__AbstractState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine"):
                opp_val = getattr(old_value, "statemachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine"):
                opp_val = getattr(value, "statemachine", None)
                if opp_val is None:
                    setattr(value, "statemachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def AbstractState9(self):
        return self.__AbstractState9

    @AbstractState9.setter
    def AbstractState9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_AbstractState__AbstractState9", None)
        self.__AbstractState9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if opp_val == self:
                    setattr(old_value, "source", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                setattr(value, "source", self)

    @property
    def AbstractState11(self):
        return self.__AbstractState11

    @AbstractState11.setter
    def AbstractState11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_AbstractState__AbstractState11", None)
        self.__AbstractState11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if opp_val == self:
                    setattr(old_value, "target", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                setattr(value, "target", self)

    @property
    def tar(self):
        return self.__tar

    @tar.setter
    def tar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_AbstractState__tar", None)
        self.__tar = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition6"):
                    opp_val = getattr(item, "Transition6", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition6"):
                    opp_val = getattr(item, "Transition6", None)
                    
                    setattr(item, "Transition6", self)
                    

    @property
    def src(self):
        return self.__src

    @src.setter
    def src(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_AbstractState__src", None)
        self.__src = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition4"):
                    opp_val = getattr(item, "Transition4", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition4"):
                    opp_val = getattr(item, "Transition4", None)
                    
                    setattr(item, "Transition4", self)
                    

class FSM_StateMachine:

    def __init__(self, code: str, statemachine: set["FSM_AbstractState"] = None, statemachine2: set["FSM_Transition"] = None, StateMachine: "FSM_AbstractState" = None, StateMachine13: "FSM_Transition" = None):
        self.code = code
        self.statemachine = statemachine if statemachine is not None else set()
        self.statemachine2 = statemachine2 if statemachine2 is not None else set()
        self.StateMachine = StateMachine
        self.StateMachine13 = StateMachine13
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def StateMachine(self):
        return self.__StateMachine

    @StateMachine.setter
    def StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_StateMachine__StateMachine", None)
        self.__StateMachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "states"):
                opp_val = getattr(old_value, "states", None)
                if opp_val == self:
                    setattr(old_value, "states", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "states"):
                opp_val = getattr(value, "states", None)
                setattr(value, "states", self)

    @property
    def StateMachine13(self):
        return self.__StateMachine13

    @StateMachine13.setter
    def StateMachine13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_StateMachine__StateMachine13", None)
        self.__StateMachine13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transitions"):
                opp_val = getattr(old_value, "transitions", None)
                if opp_val == self:
                    setattr(old_value, "transitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transitions"):
                opp_val = getattr(value, "transitions", None)
                setattr(value, "transitions", self)

    @property
    def statemachine(self):
        return self.__statemachine

    @statemachine.setter
    def statemachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_StateMachine__statemachine", None)
        self.__statemachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractState"):
                    opp_val = getattr(item, "AbstractState", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractState"):
                    opp_val = getattr(item, "AbstractState", None)
                    
                    setattr(item, "AbstractState", self)
                    

    @property
    def statemachine2(self):
        return self.__statemachine2

    @statemachine2.setter
    def statemachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_StateMachine__statemachine2", None)
        self.__statemachine2 = value if value is not None else set()
        
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
                    
