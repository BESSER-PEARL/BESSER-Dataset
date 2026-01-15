from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class fsm_SuperState:

    pass
class fsm_FSM:

    pass
class fsm_Transition:

    def __init__(self, Guard: str, Effect: str, Transition: "fsm_SuperState" = None, fsm_Transition: "fsm_State" = None, fsm_Transition10: "fsm_SuperState" = None, outTrans: "fsm_SuperState" = None):
        self.Guard = Guard
        self.Effect = Effect
        self.Transition = Transition
        self.fsm_Transition = fsm_Transition
        self.fsm_Transition10 = fsm_Transition10
        self.outTrans = outTrans
        
    @property
    def Guard(self) -> str:
        return self.__Guard

    @Guard.setter
    def Guard(self, Guard: str):
        self.__Guard = Guard

    @property
    def Effect(self) -> str:
        return self.__Effect

    @Effect.setter
    def Effect(self, Effect: str):
        self.__Effect = Effect

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
            if hasattr(old_value, "fsm_State8"):
                opp_val = getattr(old_value, "fsm_State8", None)
                if opp_val == self:
                    setattr(old_value, "fsm_State8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_State8"):
                opp_val = getattr(value, "fsm_State8", None)
                setattr(value, "fsm_State8", self)

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
            if hasattr(old_value, "src"):
                opp_val = getattr(old_value, "src", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "src"):
                opp_val = getattr(value, "src", None)
                if opp_val is None:
                    setattr(value, "src", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outTrans(self):
        return self.__outTrans

    @outTrans.setter
    def outTrans(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__outTrans", None)
        self.__outTrans = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SuperState"):
                opp_val = getattr(old_value, "SuperState", None)
                if opp_val == self:
                    setattr(old_value, "SuperState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SuperState"):
                opp_val = getattr(value, "SuperState", None)
                setattr(value, "SuperState", self)

    @property
    def fsm_Transition10(self):
        return self.__fsm_Transition10

    @fsm_Transition10.setter
    def fsm_Transition10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__fsm_Transition10", None)
        self.__fsm_Transition10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_SuperState"):
                opp_val = getattr(old_value, "fsm_SuperState", None)
                if opp_val == self:
                    setattr(old_value, "fsm_SuperState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_SuperState"):
                opp_val = getattr(value, "fsm_SuperState", None)
                setattr(value, "fsm_SuperState", self)

class State:

    pass
class fsm_TransientState(State):

    pass
class fsm_SteadyState(State):

    pass
class fsm_eAction:

    def __init__(self, exitLabel: str, fsm_eAction: "fsm_State" = None):
        self.exitLabel = exitLabel
        self.fsm_eAction = fsm_eAction
        
    @property
    def exitLabel(self) -> str:
        return self.__exitLabel

    @exitLabel.setter
    def exitLabel(self, exitLabel: str):
        self.__exitLabel = exitLabel

    @property
    def fsm_eAction(self):
        return self.__fsm_eAction

    @fsm_eAction.setter
    def fsm_eAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_eAction__fsm_eAction", None)
        self.__fsm_eAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_State6"):
                opp_val = getattr(old_value, "fsm_State6", None)
                if opp_val == self:
                    setattr(old_value, "fsm_State6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_State6"):
                opp_val = getattr(value, "fsm_State6", None)
                setattr(value, "fsm_State6", self)

class fsm_Action:

    def __init__(self, entryLabel: str, fsm_Action: "fsm_State" = None):
        self.entryLabel = entryLabel
        self.fsm_Action = fsm_Action
        
    @property
    def entryLabel(self) -> str:
        return self.__entryLabel

    @entryLabel.setter
    def entryLabel(self, entryLabel: str):
        self.__entryLabel = entryLabel

    @property
    def fsm_Action(self):
        return self.__fsm_Action

    @fsm_Action.setter
    def fsm_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Action__fsm_Action", None)
        self.__fsm_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_State4"):
                opp_val = getattr(old_value, "fsm_State4", None)
                if opp_val == self:
                    setattr(old_value, "fsm_State4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_State4"):
                opp_val = getattr(value, "fsm_State4", None)
                setattr(value, "fsm_State4", self)

class SuperState:

    pass
class fsm_InitialState(SuperState):

    def __init__(self, name: str, fsm_InitialState: "fsm_FSM" = None):
        self.name = name
        self.fsm_InitialState = fsm_InitialState
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fsm_InitialState(self):
        return self.__fsm_InitialState

    @fsm_InitialState.setter
    def fsm_InitialState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_InitialState__fsm_InitialState", None)
        self.__fsm_InitialState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_FSM2"):
                opp_val = getattr(old_value, "fsm_FSM2", None)
                if opp_val == self:
                    setattr(old_value, "fsm_FSM2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_FSM2"):
                opp_val = getattr(value, "fsm_FSM2", None)
                setattr(value, "fsm_FSM2", self)

class fsm_State(SuperState):

    def __init__(self, name: str, fsm_State4: "fsm_Action" = None, fsm_State6: "fsm_eAction" = None, fsm_State: "fsm_FSM" = None, fsm_State8: "fsm_Transition" = None):
        self.name = name
        self.fsm_State4 = fsm_State4
        self.fsm_State6 = fsm_State6
        self.fsm_State = fsm_State
        self.fsm_State8 = fsm_State8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fsm_State8(self):
        return self.__fsm_State8

    @fsm_State8.setter
    def fsm_State8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State8", None)
        self.__fsm_State8 = value
        
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
    def fsm_State4(self):
        return self.__fsm_State4

    @fsm_State4.setter
    def fsm_State4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State4", None)
        self.__fsm_State4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Action"):
                opp_val = getattr(old_value, "fsm_Action", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Action", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Action"):
                opp_val = getattr(value, "fsm_Action", None)
                setattr(value, "fsm_Action", self)

    @property
    def fsm_State6(self):
        return self.__fsm_State6

    @fsm_State6.setter
    def fsm_State6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State6", None)
        self.__fsm_State6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_eAction"):
                opp_val = getattr(old_value, "fsm_eAction", None)
                if opp_val == self:
                    setattr(old_value, "fsm_eAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_eAction"):
                opp_val = getattr(value, "fsm_eAction", None)
                setattr(value, "fsm_eAction", self)

    @property
    def fsm_State(self):
        return self.__fsm_State

    @fsm_State.setter
    def fsm_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State", None)
        self.__fsm_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_FSM"):
                opp_val = getattr(old_value, "fsm_FSM", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_FSM"):
                opp_val = getattr(value, "fsm_FSM", None)
                if opp_val is None:
                    setattr(value, "fsm_FSM", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
