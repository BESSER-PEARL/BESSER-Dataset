from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class State:

    pass
class finalStateMachine_InitialState(State):

    pass
class finalStateMachine_FinalState(State):

    pass
class finalStateMachine_State:

    def __init__(self, name: str, finalStateMachine_State: "finalStateMachine_FSM" = None, finalStateMachine_State5: "finalStateMachine_Transition" = None, finalStateMachine_State8: "finalStateMachine_Transition" = None):
        self.name = name
        self.finalStateMachine_State = finalStateMachine_State
        self.finalStateMachine_State5 = finalStateMachine_State5
        self.finalStateMachine_State8 = finalStateMachine_State8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def finalStateMachine_State8(self):
        return self.__finalStateMachine_State8

    @finalStateMachine_State8.setter
    def finalStateMachine_State8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_finalStateMachine_State__finalStateMachine_State8", None)
        self.__finalStateMachine_State8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "finalStateMachine_Transition7"):
                opp_val = getattr(old_value, "finalStateMachine_Transition7", None)
                if opp_val == self:
                    setattr(old_value, "finalStateMachine_Transition7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "finalStateMachine_Transition7"):
                opp_val = getattr(value, "finalStateMachine_Transition7", None)
                setattr(value, "finalStateMachine_Transition7", self)

    @property
    def finalStateMachine_State5(self):
        return self.__finalStateMachine_State5

    @finalStateMachine_State5.setter
    def finalStateMachine_State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_finalStateMachine_State__finalStateMachine_State5", None)
        self.__finalStateMachine_State5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "finalStateMachine_Transition4"):
                opp_val = getattr(old_value, "finalStateMachine_Transition4", None)
                if opp_val == self:
                    setattr(old_value, "finalStateMachine_Transition4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "finalStateMachine_Transition4"):
                opp_val = getattr(value, "finalStateMachine_Transition4", None)
                setattr(value, "finalStateMachine_Transition4", self)

    @property
    def finalStateMachine_State(self):
        return self.__finalStateMachine_State

    @finalStateMachine_State.setter
    def finalStateMachine_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_finalStateMachine_State__finalStateMachine_State", None)
        self.__finalStateMachine_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "finalStateMachine_FSM2"):
                opp_val = getattr(old_value, "finalStateMachine_FSM2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "finalStateMachine_FSM2"):
                opp_val = getattr(value, "finalStateMachine_FSM2", None)
                if opp_val is None:
                    setattr(value, "finalStateMachine_FSM2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class finalStateMachine_Transition:

    def __init__(self, name: str, finalStateMachine_Transition: "finalStateMachine_FSM" = None, finalStateMachine_Transition4: "finalStateMachine_State" = None, finalStateMachine_Transition7: "finalStateMachine_State" = None):
        self.name = name
        self.finalStateMachine_Transition = finalStateMachine_Transition
        self.finalStateMachine_Transition4 = finalStateMachine_Transition4
        self.finalStateMachine_Transition7 = finalStateMachine_Transition7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def finalStateMachine_Transition4(self):
        return self.__finalStateMachine_Transition4

    @finalStateMachine_Transition4.setter
    def finalStateMachine_Transition4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_finalStateMachine_Transition__finalStateMachine_Transition4", None)
        self.__finalStateMachine_Transition4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "finalStateMachine_State5"):
                opp_val = getattr(old_value, "finalStateMachine_State5", None)
                if opp_val == self:
                    setattr(old_value, "finalStateMachine_State5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "finalStateMachine_State5"):
                opp_val = getattr(value, "finalStateMachine_State5", None)
                setattr(value, "finalStateMachine_State5", self)

    @property
    def finalStateMachine_Transition(self):
        return self.__finalStateMachine_Transition

    @finalStateMachine_Transition.setter
    def finalStateMachine_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_finalStateMachine_Transition__finalStateMachine_Transition", None)
        self.__finalStateMachine_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "finalStateMachine_FSM"):
                opp_val = getattr(old_value, "finalStateMachine_FSM", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "finalStateMachine_FSM"):
                opp_val = getattr(value, "finalStateMachine_FSM", None)
                if opp_val is None:
                    setattr(value, "finalStateMachine_FSM", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def finalStateMachine_Transition7(self):
        return self.__finalStateMachine_Transition7

    @finalStateMachine_Transition7.setter
    def finalStateMachine_Transition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_finalStateMachine_Transition__finalStateMachine_Transition7", None)
        self.__finalStateMachine_Transition7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "finalStateMachine_State8"):
                opp_val = getattr(old_value, "finalStateMachine_State8", None)
                if opp_val == self:
                    setattr(old_value, "finalStateMachine_State8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "finalStateMachine_State8"):
                opp_val = getattr(value, "finalStateMachine_State8", None)
                setattr(value, "finalStateMachine_State8", self)

class finalStateMachine_FSM:

    def __init__(self, name: str, finalStateMachine_FSM: set["finalStateMachine_Transition"] = None, finalStateMachine_FSM2: set["finalStateMachine_State"] = None):
        self.name = name
        self.finalStateMachine_FSM = finalStateMachine_FSM if finalStateMachine_FSM is not None else set()
        self.finalStateMachine_FSM2 = finalStateMachine_FSM2 if finalStateMachine_FSM2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def finalStateMachine_FSM2(self):
        return self.__finalStateMachine_FSM2

    @finalStateMachine_FSM2.setter
    def finalStateMachine_FSM2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_finalStateMachine_FSM__finalStateMachine_FSM2", None)
        self.__finalStateMachine_FSM2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "finalStateMachine_State"):
                    opp_val = getattr(item, "finalStateMachine_State", None)
                    
                    if opp_val == self:
                        setattr(item, "finalStateMachine_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "finalStateMachine_State"):
                    opp_val = getattr(item, "finalStateMachine_State", None)
                    
                    setattr(item, "finalStateMachine_State", self)
                    

    @property
    def finalStateMachine_FSM(self):
        return self.__finalStateMachine_FSM

    @finalStateMachine_FSM.setter
    def finalStateMachine_FSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_finalStateMachine_FSM__finalStateMachine_FSM", None)
        self.__finalStateMachine_FSM = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "finalStateMachine_Transition"):
                    opp_val = getattr(item, "finalStateMachine_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "finalStateMachine_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "finalStateMachine_Transition"):
                    opp_val = getattr(item, "finalStateMachine_Transition", None)
                    
                    setattr(item, "finalStateMachine_Transition", self)
                    
