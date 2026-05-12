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
class NHSM_StateMachine:

    def __init__(self, name: str, StateMachine6: "NHSM_Transition" = None, owningStateMachine: set["NHSM_State"] = None, owningStateMachine9: set["NHSM_Transition"] = None, StateMachine: "NHSM_State" = None):
        self.name = name
        self.StateMachine6 = StateMachine6
        self.owningStateMachine = owningStateMachine if owningStateMachine is not None else set()
        self.owningStateMachine9 = owningStateMachine9 if owningStateMachine9 is not None else set()
        self.StateMachine = StateMachine
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def StateMachine6(self):
        return self.__StateMachine6

    @StateMachine6.setter
    def StateMachine6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NHSM_StateMachine__StateMachine6", None)
        self.__StateMachine6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedTransition"):
                opp_val = getattr(old_value, "ownedTransition", None)
                if opp_val == self:
                    setattr(old_value, "ownedTransition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedTransition"):
                opp_val = getattr(value, "ownedTransition", None)
                setattr(value, "ownedTransition", self)

    @property
    def owningStateMachine(self):
        return self.__owningStateMachine

    @owningStateMachine.setter
    def owningStateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NHSM_StateMachine__owningStateMachine", None)
        self.__owningStateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "State"):
                    opp_val = getattr(item, "State", None)
                    
                    if opp_val == self:
                        setattr(item, "State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "State"):
                    opp_val = getattr(item, "State", None)
                    
                    setattr(item, "State", self)
                    

    @property
    def StateMachine(self):
        return self.__StateMachine

    @StateMachine.setter
    def StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NHSM_StateMachine__StateMachine", None)
        self.__StateMachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedState"):
                opp_val = getattr(old_value, "ownedState", None)
                if opp_val == self:
                    setattr(old_value, "ownedState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedState"):
                opp_val = getattr(value, "ownedState", None)
                setattr(value, "ownedState", self)

    @property
    def owningStateMachine9(self):
        return self.__owningStateMachine9

    @owningStateMachine9.setter
    def owningStateMachine9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NHSM_StateMachine__owningStateMachine9", None)
        self.__owningStateMachine9 = value if value is not None else set()
        
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
                    

class NHSM_State:

    def __init__(self, name: str, NHSM_State: "NHSM_Transition" = None, NHSM_State4: "NHSM_Transition" = None, State: "NHSM_StateMachine" = None, ownedState: "NHSM_StateMachine" = None):
        self.name = name
        self.NHSM_State = NHSM_State
        self.NHSM_State4 = NHSM_State4
        self.State = State
        self.ownedState = ownedState
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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

class NHSM_Transition:

    def __init__(self, trigger: str, effect: str, NHSM_Transition: "NHSM_State" = None, NHSM_Transition3: "NHSM_State" = None, ownedTransition: "NHSM_StateMachine" = None, Transition: "NHSM_StateMachine" = None):
        self.trigger = trigger
        self.effect = effect
        self.NHSM_Transition = NHSM_Transition
        self.NHSM_Transition3 = NHSM_Transition3
        self.ownedTransition = ownedTransition
        self.Transition = Transition
        
        pass
    @property
    def trigger(self):
        return self.__trigger

    @trigger.setter
    def trigger(self, trigger: str):
        self.__trigger = trigger


    @property
    def effect(self):
        return self.__effect

    @effect.setter
    def effect(self, effect: str):
        self.__effect = effect


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
