from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class fsml_FSMTransition:

    def __init__(self, input: str, action: str, fsml_FSMTransition: "fsml_FSMState" = None, fsml_FSMTransition4: "fsml_FSMState" = None):
        self.input = input
        self.action = action
        self.fsml_FSMTransition = fsml_FSMTransition
        self.fsml_FSMTransition4 = fsml_FSMTransition4
        
    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

    @property
    def input(self) -> str:
        return self.__input

    @input.setter
    def input(self, input: str):
        self.__input = input

    @property
    def fsml_FSMTransition(self):
        return self.__fsml_FSMTransition

    @fsml_FSMTransition.setter
    def fsml_FSMTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsml_FSMTransition__fsml_FSMTransition", None)
        self.__fsml_FSMTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsml_FSMState2"):
                opp_val = getattr(old_value, "fsml_FSMState2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsml_FSMState2"):
                opp_val = getattr(value, "fsml_FSMState2", None)
                if opp_val is None:
                    setattr(value, "fsml_FSMState2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsml_FSMTransition4(self):
        return self.__fsml_FSMTransition4

    @fsml_FSMTransition4.setter
    def fsml_FSMTransition4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsml_FSMTransition__fsml_FSMTransition4", None)
        self.__fsml_FSMTransition4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsml_FSMState5"):
                opp_val = getattr(old_value, "fsml_FSMState5", None)
                if opp_val == self:
                    setattr(old_value, "fsml_FSMState5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsml_FSMState5"):
                opp_val = getattr(value, "fsml_FSMState5", None)
                setattr(value, "fsml_FSMState5", self)

class fsml_FSMState:

    def __init__(self, initial: bool, name: str, fsml_FSMState: "fsml_FSM" = None, fsml_FSMState2: set["fsml_FSMTransition"] = None, fsml_FSMState5: "fsml_FSMTransition" = None):
        self.initial = initial
        self.name = name
        self.fsml_FSMState = fsml_FSMState
        self.fsml_FSMState2 = fsml_FSMState2 if fsml_FSMState2 is not None else set()
        self.fsml_FSMState5 = fsml_FSMState5
        
    @property
    def initial(self) -> bool:
        return self.__initial

    @initial.setter
    def initial(self, initial: bool):
        self.__initial = initial

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fsml_FSMState(self):
        return self.__fsml_FSMState

    @fsml_FSMState.setter
    def fsml_FSMState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsml_FSMState__fsml_FSMState", None)
        self.__fsml_FSMState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsml_FSM"):
                opp_val = getattr(old_value, "fsml_FSM", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsml_FSM"):
                opp_val = getattr(value, "fsml_FSM", None)
                if opp_val is None:
                    setattr(value, "fsml_FSM", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsml_FSMState5(self):
        return self.__fsml_FSMState5

    @fsml_FSMState5.setter
    def fsml_FSMState5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsml_FSMState__fsml_FSMState5", None)
        self.__fsml_FSMState5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsml_FSMTransition4"):
                opp_val = getattr(old_value, "fsml_FSMTransition4", None)
                if opp_val == self:
                    setattr(old_value, "fsml_FSMTransition4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsml_FSMTransition4"):
                opp_val = getattr(value, "fsml_FSMTransition4", None)
                setattr(value, "fsml_FSMTransition4", self)

    @property
    def fsml_FSMState2(self):
        return self.__fsml_FSMState2

    @fsml_FSMState2.setter
    def fsml_FSMState2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsml_FSMState__fsml_FSMState2", None)
        self.__fsml_FSMState2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsml_FSMTransition"):
                    opp_val = getattr(item, "fsml_FSMTransition", None)
                    
                    if opp_val == self:
                        setattr(item, "fsml_FSMTransition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsml_FSMTransition"):
                    opp_val = getattr(item, "fsml_FSMTransition", None)
                    
                    setattr(item, "fsml_FSMTransition", self)
                    

class fsml_FSM:

    pass