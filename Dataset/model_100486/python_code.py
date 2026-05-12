from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class UHSM_EObject:

    pass
class UHSM_TracedClass(ABC):

    def __init__(self, trace: str, UHSM_TracedClass: set["UHSM_EObject"] = None):
        self.trace = trace
        self.UHSM_TracedClass = UHSM_TracedClass if UHSM_TracedClass is not None else set()
        
        pass
    @property
    def trace(self):
        return self.__trace

    @trace.setter
    def trace(self, trace: str):
        self.__trace = trace


    @property
    def UHSM_TracedClass(self):
        return self.__UHSM_TracedClass

    @UHSM_TracedClass.setter
    def UHSM_TracedClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UHSM_TracedClass__UHSM_TracedClass", None)
        self.__UHSM_TracedClass = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UHSM_EObject"):
                    opp_val = getattr(item, "UHSM_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "UHSM_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UHSM_EObject"):
                    opp_val = getattr(item, "UHSM_EObject", None)
                    
                    setattr(item, "UHSM_EObject", self)
                    

class StateMachine:

    pass
class UHSM_UStateMachine(StateMachine):

    pass
class Transition:

    pass
class UHSM_UTransition(Transition):

    pass
class TracedClass:

    pass
class UHSM_Transition(TracedClass):

    def __init__(self, trigger: str, effect: str, name: str, UHSM_Transition: "UHSM_UTransition" = None, UHSM_Transition3: "UHSM_State" = None, UHSM_Transition6: "UHSM_State" = None, UHSM_Transition15: "UHSM_StateMachine" = None):
        self.trigger = trigger
        self.effect = effect
        self.name = name
        self.UHSM_Transition = UHSM_Transition
        self.UHSM_Transition3 = UHSM_Transition3
        self.UHSM_Transition6 = UHSM_Transition6
        self.UHSM_Transition15 = UHSM_Transition15
        
        pass
    @property
    def effect(self):
        return self.__effect

    @effect.setter
    def effect(self, effect: str):
        self.__effect = effect


    @property
    def trigger(self):
        return self.__trigger

    @trigger.setter
    def trigger(self, trigger: str):
        self.__trigger = trigger


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def UHSM_Transition6(self):
        return self.__UHSM_Transition6

    @UHSM_Transition6.setter
    def UHSM_Transition6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UHSM_Transition__UHSM_Transition6", None)
        self.__UHSM_Transition6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UHSM_State7"):
                opp_val = getattr(old_value, "UHSM_State7", None)
                if opp_val == self:
                    setattr(old_value, "UHSM_State7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UHSM_State7"):
                opp_val = getattr(value, "UHSM_State7", None)
                setattr(value, "UHSM_State7", self)

    @property
    def UHSM_Transition15(self):
        return self.__UHSM_Transition15

    @UHSM_Transition15.setter
    def UHSM_Transition15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UHSM_Transition__UHSM_Transition15", None)
        self.__UHSM_Transition15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UHSM_StateMachine14"):
                opp_val = getattr(old_value, "UHSM_StateMachine14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UHSM_StateMachine14"):
                opp_val = getattr(value, "UHSM_StateMachine14", None)
                if opp_val is None:
                    setattr(value, "UHSM_StateMachine14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UHSM_Transition3(self):
        return self.__UHSM_Transition3

    @UHSM_Transition3.setter
    def UHSM_Transition3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UHSM_Transition__UHSM_Transition3", None)
        self.__UHSM_Transition3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UHSM_State4"):
                opp_val = getattr(old_value, "UHSM_State4", None)
                if opp_val == self:
                    setattr(old_value, "UHSM_State4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UHSM_State4"):
                opp_val = getattr(value, "UHSM_State4", None)
                setattr(value, "UHSM_State4", self)

    @property
    def UHSM_Transition(self):
        return self.__UHSM_Transition

    @UHSM_Transition.setter
    def UHSM_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UHSM_Transition__UHSM_Transition", None)
        self.__UHSM_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UHSM_UTransition"):
                opp_val = getattr(old_value, "UHSM_UTransition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UHSM_UTransition"):
                opp_val = getattr(value, "UHSM_UTransition", None)
                if opp_val is None:
                    setattr(value, "UHSM_UTransition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UHSM_State(TracedClass):

    def __init__(self, name: str, UHSM_State10: "UHSM_CompositeState" = None, UHSM_State: "UHSM_CompositeState" = None, UHSM_State4: "UHSM_Transition" = None, UHSM_State7: "UHSM_Transition" = None, UHSM_State12: "UHSM_StateMachine" = None, UHSM_State17: "UHSM_UState" = None):
        self.name = name
        self.UHSM_State10 = UHSM_State10
        self.UHSM_State = UHSM_State
        self.UHSM_State4 = UHSM_State4
        self.UHSM_State7 = UHSM_State7
        self.UHSM_State12 = UHSM_State12
        self.UHSM_State17 = UHSM_State17
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def UHSM_State12(self):
        return self.__UHSM_State12

    @UHSM_State12.setter
    def UHSM_State12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UHSM_State__UHSM_State12", None)
        self.__UHSM_State12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UHSM_StateMachine"):
                opp_val = getattr(old_value, "UHSM_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UHSM_StateMachine"):
                opp_val = getattr(value, "UHSM_StateMachine", None)
                if opp_val is None:
                    setattr(value, "UHSM_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UHSM_State10(self):
        return self.__UHSM_State10

    @UHSM_State10.setter
    def UHSM_State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UHSM_State__UHSM_State10", None)
        self.__UHSM_State10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UHSM_CompositeState9"):
                opp_val = getattr(old_value, "UHSM_CompositeState9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UHSM_CompositeState9"):
                opp_val = getattr(value, "UHSM_CompositeState9", None)
                if opp_val is None:
                    setattr(value, "UHSM_CompositeState9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UHSM_State4(self):
        return self.__UHSM_State4

    @UHSM_State4.setter
    def UHSM_State4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UHSM_State__UHSM_State4", None)
        self.__UHSM_State4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UHSM_Transition3"):
                opp_val = getattr(old_value, "UHSM_Transition3", None)
                if opp_val == self:
                    setattr(old_value, "UHSM_Transition3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UHSM_Transition3"):
                opp_val = getattr(value, "UHSM_Transition3", None)
                setattr(value, "UHSM_Transition3", self)

    @property
    def UHSM_State7(self):
        return self.__UHSM_State7

    @UHSM_State7.setter
    def UHSM_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UHSM_State__UHSM_State7", None)
        self.__UHSM_State7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UHSM_Transition6"):
                opp_val = getattr(old_value, "UHSM_Transition6", None)
                if opp_val == self:
                    setattr(old_value, "UHSM_Transition6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UHSM_Transition6"):
                opp_val = getattr(value, "UHSM_Transition6", None)
                setattr(value, "UHSM_Transition6", self)

    @property
    def UHSM_State(self):
        return self.__UHSM_State

    @UHSM_State.setter
    def UHSM_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UHSM_State__UHSM_State", None)
        self.__UHSM_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UHSM_CompositeState"):
                opp_val = getattr(old_value, "UHSM_CompositeState", None)
                if opp_val == self:
                    setattr(old_value, "UHSM_CompositeState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UHSM_CompositeState"):
                opp_val = getattr(value, "UHSM_CompositeState", None)
                setattr(value, "UHSM_CompositeState", self)

    @property
    def UHSM_State17(self):
        return self.__UHSM_State17

    @UHSM_State17.setter
    def UHSM_State17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UHSM_State__UHSM_State17", None)
        self.__UHSM_State17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UHSM_UState"):
                opp_val = getattr(old_value, "UHSM_UState", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UHSM_UState"):
                opp_val = getattr(value, "UHSM_UState", None)
                if opp_val is None:
                    setattr(value, "UHSM_UState", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UHSM_StateMachine(TracedClass):

    def __init__(self, name: str, UHSM_StateMachine: set["UHSM_State"] = None, UHSM_StateMachine14: set["UHSM_Transition"] = None, UHSM_StateMachine19: "UHSM_UStateMachine" = None):
        self.name = name
        self.UHSM_StateMachine = UHSM_StateMachine if UHSM_StateMachine is not None else set()
        self.UHSM_StateMachine14 = UHSM_StateMachine14 if UHSM_StateMachine14 is not None else set()
        self.UHSM_StateMachine19 = UHSM_StateMachine19
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def UHSM_StateMachine14(self):
        return self.__UHSM_StateMachine14

    @UHSM_StateMachine14.setter
    def UHSM_StateMachine14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UHSM_StateMachine__UHSM_StateMachine14", None)
        self.__UHSM_StateMachine14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UHSM_Transition15"):
                    opp_val = getattr(item, "UHSM_Transition15", None)
                    
                    if opp_val == self:
                        setattr(item, "UHSM_Transition15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UHSM_Transition15"):
                    opp_val = getattr(item, "UHSM_Transition15", None)
                    
                    setattr(item, "UHSM_Transition15", self)
                    

    @property
    def UHSM_StateMachine19(self):
        return self.__UHSM_StateMachine19

    @UHSM_StateMachine19.setter
    def UHSM_StateMachine19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UHSM_StateMachine__UHSM_StateMachine19", None)
        self.__UHSM_StateMachine19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UHSM_UStateMachine"):
                opp_val = getattr(old_value, "UHSM_UStateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UHSM_UStateMachine"):
                opp_val = getattr(value, "UHSM_UStateMachine", None)
                if opp_val is None:
                    setattr(value, "UHSM_UStateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UHSM_StateMachine(self):
        return self.__UHSM_StateMachine

    @UHSM_StateMachine.setter
    def UHSM_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UHSM_StateMachine__UHSM_StateMachine", None)
        self.__UHSM_StateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UHSM_State12"):
                    opp_val = getattr(item, "UHSM_State12", None)
                    
                    if opp_val == self:
                        setattr(item, "UHSM_State12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UHSM_State12"):
                    opp_val = getattr(item, "UHSM_State12", None)
                    
                    setattr(item, "UHSM_State12", self)
                    

class State:

    pass
class UHSM_UState(State):

    pass
class UHSM_InitialState(State):

    pass
class UHSM_FinalState(State):

    pass
class UHSM_CompositeState(State):

    pass