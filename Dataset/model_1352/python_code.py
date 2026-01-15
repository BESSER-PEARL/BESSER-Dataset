from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class AbstractState:

    pass
class statemachine_FinalState(AbstractState):

    pass
class statemachine_InitialState(AbstractState):

    pass
class Behaviour:

    pass
class StateMachineDescription:

    pass
class statemachine_Region(StateMachineDescription):

    pass
class statemachine_StateMachine(Behaviour, StateMachineDescription):

    pass
class ObeoDSMObject:

    pass
class statemachine_Transition(ObeoDSMObject):

    def __init__(self, guard: str, incomingTransitions: "statemachine_AbstractState" = None, statemachine_Transition: "statemachine_StateMachineDescription" = None, Transition: "statemachine_AbstractState" = None, Transition6: "statemachine_AbstractState" = None, outcomingTransitions: "statemachine_AbstractState" = None):
        self.guard = guard
        self.incomingTransitions = incomingTransitions
        self.statemachine_Transition = statemachine_Transition
        self.Transition = Transition
        self.Transition6 = Transition6
        self.outcomingTransitions = outcomingTransitions
        
    @property
    def guard(self) -> str:
        return self.__guard

    @guard.setter
    def guard(self, guard: str):
        self.__guard = guard

    @property
    def incomingTransitions(self):
        return self.__incomingTransitions

    @incomingTransitions.setter
    def incomingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Transition__incomingTransitions", None)
        self.__incomingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractState9"):
                opp_val = getattr(old_value, "AbstractState9", None)
                if opp_val == self:
                    setattr(old_value, "AbstractState9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractState9"):
                opp_val = getattr(value, "AbstractState9", None)
                setattr(value, "AbstractState9", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "to"):
                opp_val = getattr(old_value, "to", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "to"):
                opp_val = getattr(value, "to", None)
                if opp_val is None:
                    setattr(value, "to", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition6(self):
        return self.__Transition6

    @Transition6.setter
    def Transition6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Transition__Transition6", None)
        self.__Transition6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "from"):
                opp_val = getattr(old_value, "from", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "from"):
                opp_val = getattr(value, "from", None)
                if opp_val is None:
                    setattr(value, "from", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "statemachine_StateMachineDescription3"):
                opp_val = getattr(old_value, "statemachine_StateMachineDescription3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_StateMachineDescription3"):
                opp_val = getattr(value, "statemachine_StateMachineDescription3", None)
                if opp_val is None:
                    setattr(value, "statemachine_StateMachineDescription3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outcomingTransitions(self):
        return self.__outcomingTransitions

    @outcomingTransitions.setter
    def outcomingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Transition__outcomingTransitions", None)
        self.__outcomingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractState"):
                opp_val = getattr(old_value, "AbstractState", None)
                if opp_val == self:
                    setattr(old_value, "AbstractState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractState"):
                opp_val = getattr(value, "AbstractState", None)
                setattr(value, "AbstractState", self)

class statemachine_NamedElement(ObeoDSMObject):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class statemachine_AbstractState(ObeoDSMObject):

    pass
class NamedElement:

    pass
class statemachine_StateMachineDescription(NamedElement):

    pass
class statemachine_State(AbstractState, NamedElement):

    pass