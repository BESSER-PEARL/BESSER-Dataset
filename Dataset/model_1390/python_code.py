from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class State:

    pass
class HSM_FinalState(State):

    pass
class HSM_InitialState(State):

    pass
class HSM_State:

    def __init__(self, name: str, HSM_State: "HSM_CompositeState" = None, ownedState: "HSM_StateMachine" = None, HSM_State3: "HSM_Transition" = None, HSM_State6: "HSM_Transition" = None, State: "HSM_StateMachine" = None, HSM_State14: "HSM_CompositeState" = None):
        self.name = name
        self.HSM_State = HSM_State
        self.ownedState = ownedState
        self.HSM_State3 = HSM_State3
        self.HSM_State6 = HSM_State6
        self.State = State
        self.HSM_State14 = HSM_State14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def HSM_State(self):
        return self.__HSM_State

    @HSM_State.setter
    def HSM_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_State__HSM_State", None)
        self.__HSM_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HSM_CompositeState"):
                opp_val = getattr(old_value, "HSM_CompositeState", None)
                if opp_val == self:
                    setattr(old_value, "HSM_CompositeState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HSM_CompositeState"):
                opp_val = getattr(value, "HSM_CompositeState", None)
                setattr(value, "HSM_CompositeState", self)

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningStateMachine"):
                opp_val = getattr(old_value, "owningStateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningStateMachine"):
                opp_val = getattr(value, "owningStateMachine", None)
                if opp_val is None:
                    setattr(value, "owningStateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def HSM_State3(self):
        return self.__HSM_State3

    @HSM_State3.setter
    def HSM_State3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_State__HSM_State3", None)
        self.__HSM_State3 = value
        
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

    @property
    def HSM_State14(self):
        return self.__HSM_State14

    @HSM_State14.setter
    def HSM_State14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_State__HSM_State14", None)
        self.__HSM_State14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HSM_CompositeState13"):
                opp_val = getattr(old_value, "HSM_CompositeState13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HSM_CompositeState13"):
                opp_val = getattr(value, "HSM_CompositeState13", None)
                if opp_val is None:
                    setattr(value, "HSM_CompositeState13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def HSM_State6(self):
        return self.__HSM_State6

    @HSM_State6.setter
    def HSM_State6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_State__HSM_State6", None)
        self.__HSM_State6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HSM_Transition5"):
                opp_val = getattr(old_value, "HSM_Transition5", None)
                if opp_val == self:
                    setattr(old_value, "HSM_Transition5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HSM_Transition5"):
                opp_val = getattr(value, "HSM_Transition5", None)
                setattr(value, "HSM_Transition5", self)

    @property
    def ownedState(self):
        return self.__ownedState

    @ownedState.setter
    def ownedState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_State__ownedState", None)
        self.__ownedState = value
        
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

class HSM_Transition:

    def __init__(self, trigger: str, effect: str, HSM_Transition: "HSM_State" = None, HSM_Transition5: "HSM_State" = None, ownedTransition: "HSM_StateMachine" = None, HSM_Transition10: "HSM_CompositeState" = None, Transition: "HSM_StateMachine" = None, HSM_Transition17: "HSM_CompositeState" = None):
        self.trigger = trigger
        self.effect = effect
        self.HSM_Transition = HSM_Transition
        self.HSM_Transition5 = HSM_Transition5
        self.ownedTransition = ownedTransition
        self.HSM_Transition10 = HSM_Transition10
        self.Transition = Transition
        self.HSM_Transition17 = HSM_Transition17
        
    @property
    def trigger(self) -> str:
        return self.__trigger

    @trigger.setter
    def trigger(self, trigger: str):
        self.__trigger = trigger

    @property
    def effect(self) -> str:
        return self.__effect

    @effect.setter
    def effect(self, effect: str):
        self.__effect = effect

    @property
    def HSM_Transition5(self):
        return self.__HSM_Transition5

    @HSM_Transition5.setter
    def HSM_Transition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_Transition__HSM_Transition5", None)
        self.__HSM_Transition5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HSM_State6"):
                opp_val = getattr(old_value, "HSM_State6", None)
                if opp_val == self:
                    setattr(old_value, "HSM_State6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HSM_State6"):
                opp_val = getattr(value, "HSM_State6", None)
                setattr(value, "HSM_State6", self)

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
            if hasattr(old_value, "owningStateMachine20"):
                opp_val = getattr(old_value, "owningStateMachine20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningStateMachine20"):
                opp_val = getattr(value, "owningStateMachine20", None)
                if opp_val is None:
                    setattr(value, "owningStateMachine20", set([self]))
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
            if hasattr(old_value, "HSM_State3"):
                opp_val = getattr(old_value, "HSM_State3", None)
                if opp_val == self:
                    setattr(old_value, "HSM_State3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HSM_State3"):
                opp_val = getattr(value, "HSM_State3", None)
                setattr(value, "HSM_State3", self)

    @property
    def HSM_Transition10(self):
        return self.__HSM_Transition10

    @HSM_Transition10.setter
    def HSM_Transition10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_Transition__HSM_Transition10", None)
        self.__HSM_Transition10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HSM_CompositeState11"):
                opp_val = getattr(old_value, "HSM_CompositeState11", None)
                if opp_val == self:
                    setattr(old_value, "HSM_CompositeState11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HSM_CompositeState11"):
                opp_val = getattr(value, "HSM_CompositeState11", None)
                setattr(value, "HSM_CompositeState11", self)

    @property
    def ownedTransition(self):
        return self.__ownedTransition

    @ownedTransition.setter
    def ownedTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_Transition__ownedTransition", None)
        self.__ownedTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine8"):
                opp_val = getattr(old_value, "StateMachine8", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine8"):
                opp_val = getattr(value, "StateMachine8", None)
                setattr(value, "StateMachine8", self)

    @property
    def HSM_Transition17(self):
        return self.__HSM_Transition17

    @HSM_Transition17.setter
    def HSM_Transition17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_Transition__HSM_Transition17", None)
        self.__HSM_Transition17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HSM_CompositeState16"):
                opp_val = getattr(old_value, "HSM_CompositeState16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HSM_CompositeState16"):
                opp_val = getattr(value, "HSM_CompositeState16", None)
                if opp_val is None:
                    setattr(value, "HSM_CompositeState16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class HSM_StateMachine:

    pass
class HSM_CompositeState(State):

    pass