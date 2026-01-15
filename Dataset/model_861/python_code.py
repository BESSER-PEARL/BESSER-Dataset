from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class fsm_Transition:

    def __init__(self, name: str, input: str, output: str, fsm_Transition: "fsm_State" = None, fsm_Transition4: "fsm_State" = None):
        self.name = name
        self.input = input
        self.output = output
        self.fsm_Transition = fsm_Transition
        self.fsm_Transition4 = fsm_Transition4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def input(self) -> str:
        return self.__input

    @input.setter
    def input(self, input: str):
        self.__input = input

    @property
    def output(self) -> str:
        return self.__output

    @output.setter
    def output(self, output: str):
        self.__output = output

    @property
    def fsm_Transition4(self):
        return self.__fsm_Transition4

    @fsm_Transition4.setter
    def fsm_Transition4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__fsm_Transition4", None)
        self.__fsm_Transition4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_State5"):
                opp_val = getattr(old_value, "fsm_State5", None)
                if opp_val == self:
                    setattr(old_value, "fsm_State5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_State5"):
                opp_val = getattr(value, "fsm_State5", None)
                setattr(value, "fsm_State5", self)

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
            if hasattr(old_value, "fsm_State2"):
                opp_val = getattr(old_value, "fsm_State2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_State2"):
                opp_val = getattr(value, "fsm_State2", None)
                if opp_val is None:
                    setattr(value, "fsm_State2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fsm_FiniteStateMachine:

    def __init__(self, name: str, fsm_FiniteStateMachine: set["fsm_State"] = None):
        self.name = name
        self.fsm_FiniteStateMachine = fsm_FiniteStateMachine if fsm_FiniteStateMachine is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fsm_FiniteStateMachine(self):
        return self.__fsm_FiniteStateMachine

    @fsm_FiniteStateMachine.setter
    def fsm_FiniteStateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FiniteStateMachine__fsm_FiniteStateMachine", None)
        self.__fsm_FiniteStateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_State"):
                    opp_val = getattr(item, "fsm_State", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_State"):
                    opp_val = getattr(item, "fsm_State", None)
                    
                    setattr(item, "fsm_State", self)
                    

class fsm_State:

    def __init__(self, name: str, isInitialState: bool, fsm_State: "fsm_FiniteStateMachine" = None, fsm_State2: set["fsm_Transition"] = None, fsm_State5: "fsm_Transition" = None):
        self.name = name
        self.isInitialState = isInitialState
        self.fsm_State = fsm_State
        self.fsm_State2 = fsm_State2 if fsm_State2 is not None else set()
        self.fsm_State5 = fsm_State5
        
    @property
    def isInitialState(self) -> bool:
        return self.__isInitialState

    @isInitialState.setter
    def isInitialState(self, isInitialState: bool):
        self.__isInitialState = isInitialState

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "fsm_FiniteStateMachine"):
                opp_val = getattr(old_value, "fsm_FiniteStateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_FiniteStateMachine"):
                opp_val = getattr(value, "fsm_FiniteStateMachine", None)
                if opp_val is None:
                    setattr(value, "fsm_FiniteStateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsm_State2(self):
        return self.__fsm_State2

    @fsm_State2.setter
    def fsm_State2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State2", None)
        self.__fsm_State2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_Transition"):
                    opp_val = getattr(item, "fsm_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_Transition"):
                    opp_val = getattr(item, "fsm_Transition", None)
                    
                    setattr(item, "fsm_Transition", self)
                    

    @property
    def fsm_State5(self):
        return self.__fsm_State5

    @fsm_State5.setter
    def fsm_State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State5", None)
        self.__fsm_State5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Transition4"):
                opp_val = getattr(old_value, "fsm_Transition4", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Transition4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Transition4"):
                opp_val = getattr(value, "fsm_Transition4", None)
                setattr(value, "fsm_Transition4", self)
