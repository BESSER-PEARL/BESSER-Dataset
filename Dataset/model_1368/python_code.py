from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class AbstractState:

    pass
class HSM_RegularState(AbstractState):

    pass
class HSM_InitialState(AbstractState):

    pass
class HSM_CompositeState(AbstractState):

    pass
class HSM_Transition:

    def __init__(self, label: str, Transition: "HSM_StateMachine" = None, transitions: "HSM_StateMachine" = None, HSM_Transition: "HSM_AbstractState" = None, HSM_Transition6: "HSM_AbstractState" = None):
        self.label = label
        self.Transition = Transition
        self.transitions = transitions
        self.HSM_Transition = HSM_Transition
        self.HSM_Transition6 = HSM_Transition6
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def HSM_Transition6(self):
        return self.__HSM_Transition6

    @HSM_Transition6.setter
    def HSM_Transition6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_Transition__HSM_Transition6", None)
        self.__HSM_Transition6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HSM_AbstractState7"):
                opp_val = getattr(old_value, "HSM_AbstractState7", None)
                if opp_val == self:
                    setattr(old_value, "HSM_AbstractState7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HSM_AbstractState7"):
                opp_val = getattr(value, "HSM_AbstractState7", None)
                setattr(value, "HSM_AbstractState7", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_Transition__Transition", None)
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
    def HSM_Transition(self):
        return self.__HSM_Transition

    @HSM_Transition.setter
    def HSM_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_Transition__HSM_Transition", None)
        self.__HSM_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HSM_AbstractState"):
                opp_val = getattr(old_value, "HSM_AbstractState", None)
                if opp_val == self:
                    setattr(old_value, "HSM_AbstractState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HSM_AbstractState"):
                opp_val = getattr(value, "HSM_AbstractState", None)
                setattr(value, "HSM_AbstractState", self)

    @property
    def transitions(self):
        return self.__transitions

    @transitions.setter
    def transitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_Transition__transitions", None)
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

class HSM_StateMachine:

    def __init__(self, name: str, stateMachine: set["HSM_Transition"] = None, stateMachine2: set["HSM_AbstractState"] = None, StateMachine: "HSM_Transition" = None, StateMachine9: "HSM_AbstractState" = None):
        self.name = name
        self.stateMachine = stateMachine if stateMachine is not None else set()
        self.stateMachine2 = stateMachine2 if stateMachine2 is not None else set()
        self.StateMachine = StateMachine
        self.StateMachine9 = StateMachine9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def stateMachine2(self):
        return self.__stateMachine2

    @stateMachine2.setter
    def stateMachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_StateMachine__stateMachine2", None)
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
    def StateMachine(self):
        return self.__StateMachine

    @StateMachine.setter
    def StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_StateMachine__StateMachine", None)
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
    def stateMachine(self):
        return self.__stateMachine

    @stateMachine.setter
    def stateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_StateMachine__stateMachine", None)
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
                    

    @property
    def StateMachine9(self):
        return self.__StateMachine9

    @StateMachine9.setter
    def StateMachine9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_StateMachine__StateMachine9", None)
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

class HSM_AbstractState(ABC):

    def __init__(self, name: str, AbstractState: "HSM_StateMachine" = None, HSM_AbstractState: "HSM_Transition" = None, HSM_AbstractState7: "HSM_Transition" = None, states: "HSM_StateMachine" = None, states11: "HSM_CompositeState" = None, AbstractState13: "HSM_CompositeState" = None):
        self.name = name
        self.AbstractState = AbstractState
        self.HSM_AbstractState = HSM_AbstractState
        self.HSM_AbstractState7 = HSM_AbstractState7
        self.states = states
        self.states11 = states11
        self.AbstractState13 = AbstractState13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def states11(self):
        return self.__states11

    @states11.setter
    def states11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_AbstractState__states11", None)
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

    @property
    def AbstractState(self):
        return self.__AbstractState

    @AbstractState.setter
    def AbstractState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_AbstractState__AbstractState", None)
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
    def HSM_AbstractState7(self):
        return self.__HSM_AbstractState7

    @HSM_AbstractState7.setter
    def HSM_AbstractState7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_AbstractState__HSM_AbstractState7", None)
        self.__HSM_AbstractState7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HSM_Transition6"):
                opp_val = getattr(old_value, "HSM_Transition6", None)
                if opp_val == self:
                    setattr(old_value, "HSM_Transition6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HSM_Transition6"):
                opp_val = getattr(value, "HSM_Transition6", None)
                setattr(value, "HSM_Transition6", self)

    @property
    def AbstractState13(self):
        return self.__AbstractState13

    @AbstractState13.setter
    def AbstractState13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_AbstractState__AbstractState13", None)
        self.__AbstractState13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "compositeState"):
                opp_val = getattr(old_value, "compositeState", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "compositeState"):
                opp_val = getattr(value, "compositeState", None)
                if opp_val is None:
                    setattr(value, "compositeState", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def states(self):
        return self.__states

    @states.setter
    def states(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_AbstractState__states", None)
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
    def HSM_AbstractState(self):
        return self.__HSM_AbstractState

    @HSM_AbstractState.setter
    def HSM_AbstractState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_AbstractState__HSM_AbstractState", None)
        self.__HSM_AbstractState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HSM_Transition"):
                opp_val = getattr(old_value, "HSM_Transition", None)
                if opp_val == self:
                    setattr(old_value, "HSM_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HSM_Transition"):
                opp_val = getattr(value, "HSM_Transition", None)
                setattr(value, "HSM_Transition", self)
