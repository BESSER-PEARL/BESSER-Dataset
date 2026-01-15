from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class State:

    pass
class SimpleHierarchicalStateMachine_FinalState(State):

    pass
class SimpleHierarchicalStateMachine_InitialState(State):

    pass
class SimpleHierarchicalStateMachine_StateMachine:

    pass
class SimpleHierarchicalStateMachine_Transition:

    def __init__(self, trigger: str, effect: str, SimpleHierarchicalStateMachine_Transition: "SimpleHierarchicalStateMachine_State" = None, SimpleHierarchicalStateMachine_Transition4: "SimpleHierarchicalStateMachine_State" = None, SimpleHierarchicalStateMachine_Transition13: "SimpleHierarchicalStateMachine_StateMachine" = None):
        self.trigger = trigger
        self.effect = effect
        self.SimpleHierarchicalStateMachine_Transition = SimpleHierarchicalStateMachine_Transition
        self.SimpleHierarchicalStateMachine_Transition4 = SimpleHierarchicalStateMachine_Transition4
        self.SimpleHierarchicalStateMachine_Transition13 = SimpleHierarchicalStateMachine_Transition13
        
    @property
    def effect(self) -> str:
        return self.__effect

    @effect.setter
    def effect(self, effect: str):
        self.__effect = effect

    @property
    def trigger(self) -> str:
        return self.__trigger

    @trigger.setter
    def trigger(self, trigger: str):
        self.__trigger = trigger

    @property
    def SimpleHierarchicalStateMachine_Transition(self):
        return self.__SimpleHierarchicalStateMachine_Transition

    @SimpleHierarchicalStateMachine_Transition.setter
    def SimpleHierarchicalStateMachine_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleHierarchicalStateMachine_Transition__SimpleHierarchicalStateMachine_Transition", None)
        self.__SimpleHierarchicalStateMachine_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleHierarchicalStateMachine_State2"):
                opp_val = getattr(old_value, "SimpleHierarchicalStateMachine_State2", None)
                if opp_val == self:
                    setattr(old_value, "SimpleHierarchicalStateMachine_State2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleHierarchicalStateMachine_State2"):
                opp_val = getattr(value, "SimpleHierarchicalStateMachine_State2", None)
                setattr(value, "SimpleHierarchicalStateMachine_State2", self)

    @property
    def SimpleHierarchicalStateMachine_Transition13(self):
        return self.__SimpleHierarchicalStateMachine_Transition13

    @SimpleHierarchicalStateMachine_Transition13.setter
    def SimpleHierarchicalStateMachine_Transition13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleHierarchicalStateMachine_Transition__SimpleHierarchicalStateMachine_Transition13", None)
        self.__SimpleHierarchicalStateMachine_Transition13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleHierarchicalStateMachine_StateMachine12"):
                opp_val = getattr(old_value, "SimpleHierarchicalStateMachine_StateMachine12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleHierarchicalStateMachine_StateMachine12"):
                opp_val = getattr(value, "SimpleHierarchicalStateMachine_StateMachine12", None)
                if opp_val is None:
                    setattr(value, "SimpleHierarchicalStateMachine_StateMachine12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SimpleHierarchicalStateMachine_Transition4(self):
        return self.__SimpleHierarchicalStateMachine_Transition4

    @SimpleHierarchicalStateMachine_Transition4.setter
    def SimpleHierarchicalStateMachine_Transition4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleHierarchicalStateMachine_Transition__SimpleHierarchicalStateMachine_Transition4", None)
        self.__SimpleHierarchicalStateMachine_Transition4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleHierarchicalStateMachine_State5"):
                opp_val = getattr(old_value, "SimpleHierarchicalStateMachine_State5", None)
                if opp_val == self:
                    setattr(old_value, "SimpleHierarchicalStateMachine_State5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleHierarchicalStateMachine_State5"):
                opp_val = getattr(value, "SimpleHierarchicalStateMachine_State5", None)
                setattr(value, "SimpleHierarchicalStateMachine_State5", self)

class SimpleHierarchicalStateMachine_CompositeState(State):

    pass
class SimpleHierarchicalStateMachine_State:

    def __init__(self, name: str, SimpleHierarchicalStateMachine_State: "SimpleHierarchicalStateMachine_CompositeState" = None, SimpleHierarchicalStateMachine_State2: "SimpleHierarchicalStateMachine_Transition" = None, SimpleHierarchicalStateMachine_State5: "SimpleHierarchicalStateMachine_Transition" = None, SimpleHierarchicalStateMachine_State8: "SimpleHierarchicalStateMachine_CompositeState" = None, SimpleHierarchicalStateMachine_State10: "SimpleHierarchicalStateMachine_StateMachine" = None):
        self.name = name
        self.SimpleHierarchicalStateMachine_State = SimpleHierarchicalStateMachine_State
        self.SimpleHierarchicalStateMachine_State2 = SimpleHierarchicalStateMachine_State2
        self.SimpleHierarchicalStateMachine_State5 = SimpleHierarchicalStateMachine_State5
        self.SimpleHierarchicalStateMachine_State8 = SimpleHierarchicalStateMachine_State8
        self.SimpleHierarchicalStateMachine_State10 = SimpleHierarchicalStateMachine_State10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SimpleHierarchicalStateMachine_State(self):
        return self.__SimpleHierarchicalStateMachine_State

    @SimpleHierarchicalStateMachine_State.setter
    def SimpleHierarchicalStateMachine_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleHierarchicalStateMachine_State__SimpleHierarchicalStateMachine_State", None)
        self.__SimpleHierarchicalStateMachine_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleHierarchicalStateMachine_CompositeState"):
                opp_val = getattr(old_value, "SimpleHierarchicalStateMachine_CompositeState", None)
                if opp_val == self:
                    setattr(old_value, "SimpleHierarchicalStateMachine_CompositeState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleHierarchicalStateMachine_CompositeState"):
                opp_val = getattr(value, "SimpleHierarchicalStateMachine_CompositeState", None)
                setattr(value, "SimpleHierarchicalStateMachine_CompositeState", self)

    @property
    def SimpleHierarchicalStateMachine_State8(self):
        return self.__SimpleHierarchicalStateMachine_State8

    @SimpleHierarchicalStateMachine_State8.setter
    def SimpleHierarchicalStateMachine_State8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleHierarchicalStateMachine_State__SimpleHierarchicalStateMachine_State8", None)
        self.__SimpleHierarchicalStateMachine_State8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleHierarchicalStateMachine_CompositeState7"):
                opp_val = getattr(old_value, "SimpleHierarchicalStateMachine_CompositeState7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleHierarchicalStateMachine_CompositeState7"):
                opp_val = getattr(value, "SimpleHierarchicalStateMachine_CompositeState7", None)
                if opp_val is None:
                    setattr(value, "SimpleHierarchicalStateMachine_CompositeState7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SimpleHierarchicalStateMachine_State10(self):
        return self.__SimpleHierarchicalStateMachine_State10

    @SimpleHierarchicalStateMachine_State10.setter
    def SimpleHierarchicalStateMachine_State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleHierarchicalStateMachine_State__SimpleHierarchicalStateMachine_State10", None)
        self.__SimpleHierarchicalStateMachine_State10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleHierarchicalStateMachine_StateMachine"):
                opp_val = getattr(old_value, "SimpleHierarchicalStateMachine_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleHierarchicalStateMachine_StateMachine"):
                opp_val = getattr(value, "SimpleHierarchicalStateMachine_StateMachine", None)
                if opp_val is None:
                    setattr(value, "SimpleHierarchicalStateMachine_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SimpleHierarchicalStateMachine_State5(self):
        return self.__SimpleHierarchicalStateMachine_State5

    @SimpleHierarchicalStateMachine_State5.setter
    def SimpleHierarchicalStateMachine_State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleHierarchicalStateMachine_State__SimpleHierarchicalStateMachine_State5", None)
        self.__SimpleHierarchicalStateMachine_State5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleHierarchicalStateMachine_Transition4"):
                opp_val = getattr(old_value, "SimpleHierarchicalStateMachine_Transition4", None)
                if opp_val == self:
                    setattr(old_value, "SimpleHierarchicalStateMachine_Transition4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleHierarchicalStateMachine_Transition4"):
                opp_val = getattr(value, "SimpleHierarchicalStateMachine_Transition4", None)
                setattr(value, "SimpleHierarchicalStateMachine_Transition4", self)

    @property
    def SimpleHierarchicalStateMachine_State2(self):
        return self.__SimpleHierarchicalStateMachine_State2

    @SimpleHierarchicalStateMachine_State2.setter
    def SimpleHierarchicalStateMachine_State2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleHierarchicalStateMachine_State__SimpleHierarchicalStateMachine_State2", None)
        self.__SimpleHierarchicalStateMachine_State2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleHierarchicalStateMachine_Transition"):
                opp_val = getattr(old_value, "SimpleHierarchicalStateMachine_Transition", None)
                if opp_val == self:
                    setattr(old_value, "SimpleHierarchicalStateMachine_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleHierarchicalStateMachine_Transition"):
                opp_val = getattr(value, "SimpleHierarchicalStateMachine_Transition", None)
                setattr(value, "SimpleHierarchicalStateMachine_Transition", self)
