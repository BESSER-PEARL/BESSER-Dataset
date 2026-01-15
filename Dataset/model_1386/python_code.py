from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class State:

    pass
class SM_FinalState(State):

    pass
class SM_InitialState(State):

    pass
class SM_Transition:

    def __init__(self, trigger: str, effect: str, ownedTransition: "SM_StateMachine" = None, Transition: "SM_StateMachine" = None, SM_Transition: "SM_State" = None, SM_Transition3: "SM_State" = None):
        self.trigger = trigger
        self.effect = effect
        self.ownedTransition = ownedTransition
        self.Transition = Transition
        self.SM_Transition = SM_Transition
        self.SM_Transition3 = SM_Transition3
        
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
    def ownedTransition(self):
        return self.__ownedTransition

    @ownedTransition.setter
    def ownedTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SM_Transition__ownedTransition", None)
        self.__ownedTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine6"):
                opp_val = getattr(old_value, "StateMachine6", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine6"):
                opp_val = getattr(value, "StateMachine6", None)
                setattr(value, "StateMachine6", self)

    @property
    def SM_Transition(self):
        return self.__SM_Transition

    @SM_Transition.setter
    def SM_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SM_Transition__SM_Transition", None)
        self.__SM_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SM_State"):
                opp_val = getattr(old_value, "SM_State", None)
                if opp_val == self:
                    setattr(old_value, "SM_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SM_State"):
                opp_val = getattr(value, "SM_State", None)
                setattr(value, "SM_State", self)

    @property
    def SM_Transition3(self):
        return self.__SM_Transition3

    @SM_Transition3.setter
    def SM_Transition3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SM_Transition__SM_Transition3", None)
        self.__SM_Transition3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SM_State4"):
                opp_val = getattr(old_value, "SM_State4", None)
                if opp_val == self:
                    setattr(old_value, "SM_State4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SM_State4"):
                opp_val = getattr(value, "SM_State4", None)
                setattr(value, "SM_State4", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SM_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningStateMachine9"):
                opp_val = getattr(old_value, "owningStateMachine9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningStateMachine9"):
                opp_val = getattr(value, "owningStateMachine9", None)
                if opp_val is None:
                    setattr(value, "owningStateMachine9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SM_StateMachine:

    pass
class SM_State:

    def __init__(self, name: str, ownedState: "SM_StateMachine" = None, SM_State: "SM_Transition" = None, State: "SM_StateMachine" = None, SM_State4: "SM_Transition" = None):
        self.name = name
        self.ownedState = ownedState
        self.SM_State = SM_State
        self.State = State
        self.SM_State4 = SM_State4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SM_State__State", None)
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
    def SM_State4(self):
        return self.__SM_State4

    @SM_State4.setter
    def SM_State4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SM_State__SM_State4", None)
        self.__SM_State4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SM_Transition3"):
                opp_val = getattr(old_value, "SM_Transition3", None)
                if opp_val == self:
                    setattr(old_value, "SM_Transition3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SM_Transition3"):
                opp_val = getattr(value, "SM_Transition3", None)
                setattr(value, "SM_Transition3", self)

    @property
    def SM_State(self):
        return self.__SM_State

    @SM_State.setter
    def SM_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SM_State__SM_State", None)
        self.__SM_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SM_Transition"):
                opp_val = getattr(old_value, "SM_Transition", None)
                if opp_val == self:
                    setattr(old_value, "SM_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SM_Transition"):
                opp_val = getattr(value, "SM_Transition", None)
                setattr(value, "SM_Transition", self)

    @property
    def ownedState(self):
        return self.__ownedState

    @ownedState.setter
    def ownedState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SM_State__ownedState", None)
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
