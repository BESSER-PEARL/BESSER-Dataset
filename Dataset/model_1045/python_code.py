from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class FAbstractState:

    pass
class FSM_FRegularState(FAbstractState):

    pass
class FSM_FInitialState(FAbstractState):

    pass
class FSM_FAbstractState(ABC):

    def __init__(self, name: str, FAbstractState: "FSM_FStateMachine" = None, FSM_FAbstractState: "FSM_FTransition" = None, FSM_FAbstractState7: "FSM_FTransition" = None, states: "FSM_FStateMachine" = None):
        self.name = name
        self.FAbstractState = FAbstractState
        self.FSM_FAbstractState = FSM_FAbstractState
        self.FSM_FAbstractState7 = FSM_FAbstractState7
        self.states = states
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def FSM_FAbstractState7(self):
        return self.__FSM_FAbstractState7

    @FSM_FAbstractState7.setter
    def FSM_FAbstractState7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_FAbstractState__FSM_FAbstractState7", None)
        self.__FSM_FAbstractState7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM_FTransition6"):
                opp_val = getattr(old_value, "FSM_FTransition6", None)
                if opp_val == self:
                    setattr(old_value, "FSM_FTransition6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM_FTransition6"):
                opp_val = getattr(value, "FSM_FTransition6", None)
                setattr(value, "FSM_FTransition6", self)

    @property
    def FAbstractState(self):
        return self.__FAbstractState

    @FAbstractState.setter
    def FAbstractState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_FAbstractState__FAbstractState", None)
        self.__FAbstractState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine2"):
                opp_val = getattr(old_value, "stateMachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine2"):
                opp_val = getattr(value, "stateMachine2", None)
                if opp_val is None:
                    setattr(value, "stateMachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def states(self):
        return self.__states

    @states.setter
    def states(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_FAbstractState__states", None)
        self.__states = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FStateMachine9"):
                opp_val = getattr(old_value, "FStateMachine9", None)
                if opp_val == self:
                    setattr(old_value, "FStateMachine9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FStateMachine9"):
                opp_val = getattr(value, "FStateMachine9", None)
                setattr(value, "FStateMachine9", self)

    @property
    def FSM_FAbstractState(self):
        return self.__FSM_FAbstractState

    @FSM_FAbstractState.setter
    def FSM_FAbstractState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_FAbstractState__FSM_FAbstractState", None)
        self.__FSM_FAbstractState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM_FTransition"):
                opp_val = getattr(old_value, "FSM_FTransition", None)
                if opp_val == self:
                    setattr(old_value, "FSM_FTransition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM_FTransition"):
                opp_val = getattr(value, "FSM_FTransition", None)
                setattr(value, "FSM_FTransition", self)

class FSM_FTransition:

    def __init__(self, label: str, FTransition: "FSM_FStateMachine" = None, transitions: "FSM_FStateMachine" = None, FSM_FTransition: "FSM_FAbstractState" = None, FSM_FTransition6: "FSM_FAbstractState" = None):
        self.label = label
        self.FTransition = FTransition
        self.transitions = transitions
        self.FSM_FTransition = FSM_FTransition
        self.FSM_FTransition6 = FSM_FTransition6
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def FSM_FTransition(self):
        return self.__FSM_FTransition

    @FSM_FTransition.setter
    def FSM_FTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_FTransition__FSM_FTransition", None)
        self.__FSM_FTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM_FAbstractState"):
                opp_val = getattr(old_value, "FSM_FAbstractState", None)
                if opp_val == self:
                    setattr(old_value, "FSM_FAbstractState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM_FAbstractState"):
                opp_val = getattr(value, "FSM_FAbstractState", None)
                setattr(value, "FSM_FAbstractState", self)

    @property
    def FSM_FTransition6(self):
        return self.__FSM_FTransition6

    @FSM_FTransition6.setter
    def FSM_FTransition6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_FTransition__FSM_FTransition6", None)
        self.__FSM_FTransition6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM_FAbstractState7"):
                opp_val = getattr(old_value, "FSM_FAbstractState7", None)
                if opp_val == self:
                    setattr(old_value, "FSM_FAbstractState7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM_FAbstractState7"):
                opp_val = getattr(value, "FSM_FAbstractState7", None)
                setattr(value, "FSM_FAbstractState7", self)

    @property
    def FTransition(self):
        return self.__FTransition

    @FTransition.setter
    def FTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_FTransition__FTransition", None)
        self.__FTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine"):
                opp_val = getattr(old_value, "stateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine"):
                opp_val = getattr(value, "stateMachine", None)
                if opp_val is None:
                    setattr(value, "stateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def transitions(self):
        return self.__transitions

    @transitions.setter
    def transitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_FTransition__transitions", None)
        self.__transitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FStateMachine"):
                opp_val = getattr(old_value, "FStateMachine", None)
                if opp_val == self:
                    setattr(old_value, "FStateMachine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FStateMachine"):
                opp_val = getattr(value, "FStateMachine", None)
                setattr(value, "FStateMachine", self)

class FSM_FStateMachine:

    def __init__(self, name: str, stateMachine: set["FSM_FTransition"] = None, stateMachine2: set["FSM_FAbstractState"] = None, FStateMachine: "FSM_FTransition" = None, FStateMachine9: "FSM_FAbstractState" = None):
        self.name = name
        self.stateMachine = stateMachine if stateMachine is not None else set()
        self.stateMachine2 = stateMachine2 if stateMachine2 is not None else set()
        self.FStateMachine = FStateMachine
        self.FStateMachine9 = FStateMachine9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def FStateMachine9(self):
        return self.__FStateMachine9

    @FStateMachine9.setter
    def FStateMachine9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_FStateMachine__FStateMachine9", None)
        self.__FStateMachine9 = value
        
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
    def stateMachine(self):
        return self.__stateMachine

    @stateMachine.setter
    def stateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_FStateMachine__stateMachine", None)
        self.__stateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FTransition"):
                    opp_val = getattr(item, "FTransition", None)
                    
                    if opp_val == self:
                        setattr(item, "FTransition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FTransition"):
                    opp_val = getattr(item, "FTransition", None)
                    
                    setattr(item, "FTransition", self)
                    

    @property
    def stateMachine2(self):
        return self.__stateMachine2

    @stateMachine2.setter
    def stateMachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_FStateMachine__stateMachine2", None)
        self.__stateMachine2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FAbstractState"):
                    opp_val = getattr(item, "FAbstractState", None)
                    
                    if opp_val == self:
                        setattr(item, "FAbstractState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FAbstractState"):
                    opp_val = getattr(item, "FAbstractState", None)
                    
                    setattr(item, "FAbstractState", self)
                    

    @property
    def FStateMachine(self):
        return self.__FStateMachine

    @FStateMachine.setter
    def FStateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_FStateMachine__FStateMachine", None)
        self.__FStateMachine = value
        
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
