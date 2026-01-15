from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class fsm_AbstractState(ABC):

    def __init__(self, name: str, fsm_AbstractState: "fsm_Transition" = None, fsm_AbstractState7: "fsm_Transition" = None, states: "fsm_StateMachine" = None, states11: "fsm_CompositeState" = None, AbstractState13: "fsm_CompositeState" = None, AbstractState: "fsm_StateMachine" = None):
        self.name = name
        self.fsm_AbstractState = fsm_AbstractState
        self.fsm_AbstractState7 = fsm_AbstractState7
        self.states = states
        self.states11 = states11
        self.AbstractState13 = AbstractState13
        self.AbstractState = AbstractState
        
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
        old_value = getattr(self, f"_fsm_AbstractState__states", None)
        self.__states = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine9"):
                opp_val = getattr(old_value, "StateMachine9", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine9"):
                opp_val = getattr(value, "StateMachine9", None)
                setattr(value, "StateMachine9", self)

    @property
    def fsm_AbstractState(self):
        return self.__fsm_AbstractState

    @fsm_AbstractState.setter
    def fsm_AbstractState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_AbstractState__fsm_AbstractState", None)
        self.__fsm_AbstractState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Transition"):
                opp_val = getattr(old_value, "fsm_Transition", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Transition"):
                opp_val = getattr(value, "fsm_Transition", None)
                setattr(value, "fsm_Transition", self)

    @property
    def fsm_AbstractState7(self):
        return self.__fsm_AbstractState7

    @fsm_AbstractState7.setter
    def fsm_AbstractState7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_AbstractState__fsm_AbstractState7", None)
        self.__fsm_AbstractState7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Transition6"):
                opp_val = getattr(old_value, "fsm_Transition6", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Transition6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Transition6"):
                opp_val = getattr(value, "fsm_Transition6", None)
                setattr(value, "fsm_Transition6", self)

    @property
    def AbstractState(self):
        return self.__AbstractState

    @AbstractState.setter
    def AbstractState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_AbstractState__AbstractState", None)
        self.__AbstractState = value
        
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
    def AbstractState13(self):
        return self.__AbstractState13

    @AbstractState13.setter
    def AbstractState13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_AbstractState__AbstractState13", None)
        self.__AbstractState13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "compositeStates"):
                opp_val = getattr(old_value, "compositeStates", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "compositeStates"):
                opp_val = getattr(value, "compositeStates", None)
                if opp_val is None:
                    setattr(value, "compositeStates", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def states11(self):
        return self.__states11

    @states11.setter
    def states11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_AbstractState__states11", None)
        self.__states11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompositeState"):
                opp_val = getattr(old_value, "CompositeState", None)
                if opp_val == self:
                    setattr(old_value, "CompositeState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompositeState"):
                opp_val = getattr(value, "CompositeState", None)
                setattr(value, "CompositeState", self)

class fsm_Root:

    pass
class AbstractState:

    pass
class fsm_RegularState(AbstractState):

    pass
class fsm_InitialState(AbstractState):

    pass
class fsm_CompositeState(AbstractState):

    pass
class fsm_Transition:

    def __init__(self, label: str, Transition: "fsm_StateMachine" = None, transitions: "fsm_StateMachine" = None, fsm_Transition: "fsm_AbstractState" = None, fsm_Transition6: "fsm_AbstractState" = None):
        self.label = label
        self.Transition = Transition
        self.transitions = transitions
        self.fsm_Transition = fsm_Transition
        self.fsm_Transition6 = fsm_Transition6
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def fsm_Transition(self):
        return self.__fsm_Transition

    @fsm_Transition.setter
    def fsm_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__fsm_Transition", None)
        self.__fsm_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_AbstractState"):
                opp_val = getattr(old_value, "fsm_AbstractState", None)
                if opp_val == self:
                    setattr(old_value, "fsm_AbstractState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_AbstractState"):
                opp_val = getattr(value, "fsm_AbstractState", None)
                setattr(value, "fsm_AbstractState", self)

    @property
    def transitions(self):
        return self.__transitions

    @transitions.setter
    def transitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__transitions", None)
        self.__transitions = value
        
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
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__Transition", None)
        self.__Transition = value
        
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
    def fsm_Transition6(self):
        return self.__fsm_Transition6

    @fsm_Transition6.setter
    def fsm_Transition6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__fsm_Transition6", None)
        self.__fsm_Transition6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_AbstractState7"):
                opp_val = getattr(old_value, "fsm_AbstractState7", None)
                if opp_val == self:
                    setattr(old_value, "fsm_AbstractState7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_AbstractState7"):
                opp_val = getattr(value, "fsm_AbstractState7", None)
                setattr(value, "fsm_AbstractState7", self)

class fsm_StateMachine:

    def __init__(self, name: str, stateMachine: set["fsm_Transition"] = None, StateMachine: "fsm_Transition" = None, StateMachine9: "fsm_AbstractState" = None, fsm_StateMachine: "fsm_Root" = None, stateMachine2: set["fsm_AbstractState"] = None):
        self.name = name
        self.stateMachine = stateMachine if stateMachine is not None else set()
        self.StateMachine = StateMachine
        self.StateMachine9 = StateMachine9
        self.fsm_StateMachine = fsm_StateMachine
        self.stateMachine2 = stateMachine2 if stateMachine2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def StateMachine(self):
        return self.__StateMachine

    @StateMachine.setter
    def StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_StateMachine__StateMachine", None)
        self.__StateMachine = value
        
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
    def fsm_StateMachine(self):
        return self.__fsm_StateMachine

    @fsm_StateMachine.setter
    def fsm_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_StateMachine__fsm_StateMachine", None)
        self.__fsm_StateMachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Root"):
                opp_val = getattr(old_value, "fsm_Root", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Root"):
                opp_val = getattr(value, "fsm_Root", None)
                if opp_val is None:
                    setattr(value, "fsm_Root", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def StateMachine9(self):
        return self.__StateMachine9

    @StateMachine9.setter
    def StateMachine9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_StateMachine__StateMachine9", None)
        self.__StateMachine9 = value
        
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
    def stateMachine2(self):
        return self.__stateMachine2

    @stateMachine2.setter
    def stateMachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_StateMachine__stateMachine2", None)
        self.__stateMachine2 = value if value is not None else set()
        
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
    def stateMachine(self):
        return self.__stateMachine

    @stateMachine.setter
    def stateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_StateMachine__stateMachine", None)
        self.__stateMachine = value if value is not None else set()
        
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
                    
