from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class State:

    pass
class NHSM_FinalState(State):

    pass
class NHSM_InitialState(State):

    pass
class NHSM_Transition:

    def __init__(self, trigger: str, effect: str, cost: int, NHSM_Transition: "NHSM_State" = None, NHSM_Transition3: "NHSM_State" = None, ownedTransition: "NHSM_StateMachine" = None, Transition: "NHSM_StateMachine" = None):
        self.trigger = trigger
        self.effect = effect
        self.cost = cost
        self.NHSM_Transition = NHSM_Transition
        self.NHSM_Transition3 = NHSM_Transition3
        self.ownedTransition = ownedTransition
        self.Transition = Transition
        
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
    def cost(self) -> int:
        return self.__cost

    @cost.setter
    def cost(self, cost: int):
        self.__cost = cost

    @property
    def NHSM_Transition(self):
        return self.__NHSM_Transition

    @NHSM_Transition.setter
    def NHSM_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NHSM_Transition__NHSM_Transition", None)
        self.__NHSM_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NHSM_State"):
                opp_val = getattr(old_value, "NHSM_State", None)
                if opp_val == self:
                    setattr(old_value, "NHSM_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NHSM_State"):
                opp_val = getattr(value, "NHSM_State", None)
                setattr(value, "NHSM_State", self)

    @property
    def ownedTransition(self):
        return self.__ownedTransition

    @ownedTransition.setter
    def ownedTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NHSM_Transition__ownedTransition", None)
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
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NHSM_Transition__Transition", None)
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

    @property
    def NHSM_Transition3(self):
        return self.__NHSM_Transition3

    @NHSM_Transition3.setter
    def NHSM_Transition3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NHSM_Transition__NHSM_Transition3", None)
        self.__NHSM_Transition3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NHSM_State4"):
                opp_val = getattr(old_value, "NHSM_State4", None)
                if opp_val == self:
                    setattr(old_value, "NHSM_State4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NHSM_State4"):
                opp_val = getattr(value, "NHSM_State4", None)
                setattr(value, "NHSM_State4", self)

class NHSM_StateMachine:

    pass
class NHSM_State:

    def __init__(self, name: str, memRequirement: int, ownedState: "NHSM_StateMachine" = None, NHSM_State: "NHSM_Transition" = None, NHSM_State4: "NHSM_Transition" = None, State: "NHSM_StateMachine" = None):
        self.name = name
        self.memRequirement = memRequirement
        self.ownedState = ownedState
        self.NHSM_State = NHSM_State
        self.NHSM_State4 = NHSM_State4
        self.State = State
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def memRequirement(self) -> int:
        return self.__memRequirement

    @memRequirement.setter
    def memRequirement(self, memRequirement: int):
        self.__memRequirement = memRequirement

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NHSM_State__State", None)
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
    def NHSM_State4(self):
        return self.__NHSM_State4

    @NHSM_State4.setter
    def NHSM_State4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NHSM_State__NHSM_State4", None)
        self.__NHSM_State4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NHSM_Transition3"):
                opp_val = getattr(old_value, "NHSM_Transition3", None)
                if opp_val == self:
                    setattr(old_value, "NHSM_Transition3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NHSM_Transition3"):
                opp_val = getattr(value, "NHSM_Transition3", None)
                setattr(value, "NHSM_Transition3", self)

    @property
    def NHSM_State(self):
        return self.__NHSM_State

    @NHSM_State.setter
    def NHSM_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NHSM_State__NHSM_State", None)
        self.__NHSM_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NHSM_Transition"):
                opp_val = getattr(old_value, "NHSM_Transition", None)
                if opp_val == self:
                    setattr(old_value, "NHSM_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NHSM_Transition"):
                opp_val = getattr(value, "NHSM_Transition", None)
                setattr(value, "NHSM_Transition", self)

    @property
    def ownedState(self):
        return self.__ownedState

    @ownedState.setter
    def ownedState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NHSM_State__ownedState", None)
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
