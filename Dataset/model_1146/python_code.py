from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class hsm_Root:

    pass
class AbstractState:

    pass
class hsm_RegularState(AbstractState):

    pass
class hsm_InitialState(AbstractState):

    pass
class hsm_CompositeState(AbstractState):

    pass
class hsm_AbstractState(ABC):

    def __init__(self, name: str, AbstractState: "hsm_StateMachine" = None, hsm_AbstractState: "hsm_Transition" = None, states11: "hsm_CompositeState" = None, AbstractState13: "hsm_CompositeState" = None, hsm_AbstractState7: "hsm_Transition" = None, states: "hsm_StateMachine" = None):
        self.name = name
        self.AbstractState = AbstractState
        self.hsm_AbstractState = hsm_AbstractState
        self.states11 = states11
        self.AbstractState13 = AbstractState13
        self.hsm_AbstractState7 = hsm_AbstractState7
        self.states = states
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def AbstractState(self):
        return self.__AbstractState

    @AbstractState.setter
    def AbstractState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hsm_AbstractState__AbstractState", None)
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
    def hsm_AbstractState(self):
        return self.__hsm_AbstractState

    @hsm_AbstractState.setter
    def hsm_AbstractState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hsm_AbstractState__hsm_AbstractState", None)
        self.__hsm_AbstractState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hsm_Transition"):
                opp_val = getattr(old_value, "hsm_Transition", None)
                if opp_val == self:
                    setattr(old_value, "hsm_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hsm_Transition"):
                opp_val = getattr(value, "hsm_Transition", None)
                setattr(value, "hsm_Transition", self)

    @property
    def states11(self):
        return self.__states11

    @states11.setter
    def states11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hsm_AbstractState__states11", None)
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
    def hsm_AbstractState7(self):
        return self.__hsm_AbstractState7

    @hsm_AbstractState7.setter
    def hsm_AbstractState7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hsm_AbstractState__hsm_AbstractState7", None)
        self.__hsm_AbstractState7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hsm_Transition6"):
                opp_val = getattr(old_value, "hsm_Transition6", None)
                if opp_val == self:
                    setattr(old_value, "hsm_Transition6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hsm_Transition6"):
                opp_val = getattr(value, "hsm_Transition6", None)
                setattr(value, "hsm_Transition6", self)

    @property
    def states(self):
        return self.__states

    @states.setter
    def states(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hsm_AbstractState__states", None)
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
    def AbstractState13(self):
        return self.__AbstractState13

    @AbstractState13.setter
    def AbstractState13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hsm_AbstractState__AbstractState13", None)
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

class hsm_Transition:

    def __init__(self, label: str, Transition: "hsm_StateMachine" = None, transitions: "hsm_StateMachine" = None, hsm_Transition: "hsm_AbstractState" = None, hsm_Transition6: "hsm_AbstractState" = None):
        self.label = label
        self.Transition = Transition
        self.transitions = transitions
        self.hsm_Transition = hsm_Transition
        self.hsm_Transition6 = hsm_Transition6
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def hsm_Transition(self):
        return self.__hsm_Transition

    @hsm_Transition.setter
    def hsm_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hsm_Transition__hsm_Transition", None)
        self.__hsm_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hsm_AbstractState"):
                opp_val = getattr(old_value, "hsm_AbstractState", None)
                if opp_val == self:
                    setattr(old_value, "hsm_AbstractState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hsm_AbstractState"):
                opp_val = getattr(value, "hsm_AbstractState", None)
                setattr(value, "hsm_AbstractState", self)

    @property
    def transitions(self):
        return self.__transitions

    @transitions.setter
    def transitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hsm_Transition__transitions", None)
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
    def hsm_Transition6(self):
        return self.__hsm_Transition6

    @hsm_Transition6.setter
    def hsm_Transition6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hsm_Transition__hsm_Transition6", None)
        self.__hsm_Transition6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hsm_AbstractState7"):
                opp_val = getattr(old_value, "hsm_AbstractState7", None)
                if opp_val == self:
                    setattr(old_value, "hsm_AbstractState7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hsm_AbstractState7"):
                opp_val = getattr(value, "hsm_AbstractState7", None)
                setattr(value, "hsm_AbstractState7", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hsm_Transition__Transition", None)
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

class hsm_StateMachine:

    def __init__(self, name: str, stateMachine: set["hsm_Transition"] = None, stateMachine2: set["hsm_AbstractState"] = None, StateMachine: "hsm_Transition" = None, hsm_StateMachine: "hsm_Root" = None, StateMachine9: "hsm_AbstractState" = None):
        self.name = name
        self.stateMachine = stateMachine if stateMachine is not None else set()
        self.stateMachine2 = stateMachine2 if stateMachine2 is not None else set()
        self.StateMachine = StateMachine
        self.hsm_StateMachine = hsm_StateMachine
        self.StateMachine9 = StateMachine9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def hsm_StateMachine(self):
        return self.__hsm_StateMachine

    @hsm_StateMachine.setter
    def hsm_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hsm_StateMachine__hsm_StateMachine", None)
        self.__hsm_StateMachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hsm_Root"):
                opp_val = getattr(old_value, "hsm_Root", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hsm_Root"):
                opp_val = getattr(value, "hsm_Root", None)
                if opp_val is None:
                    setattr(value, "hsm_Root", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def stateMachine2(self):
        return self.__stateMachine2

    @stateMachine2.setter
    def stateMachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hsm_StateMachine__stateMachine2", None)
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
    def StateMachine9(self):
        return self.__StateMachine9

    @StateMachine9.setter
    def StateMachine9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hsm_StateMachine__StateMachine9", None)
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
    def StateMachine(self):
        return self.__StateMachine

    @StateMachine.setter
    def StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hsm_StateMachine__StateMachine", None)
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
        old_value = getattr(self, f"_hsm_StateMachine__stateMachine", None)
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
                    
