from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class NHSM_Transition:

    pass
class NHSM_State:

    def __init__(self, name: str, states: "NHSM_StateMachine" = None, NHSM_State: "NHSM_Transition" = None, NHSM_State7: "NHSM_Transition" = None, State: "NHSM_StateMachine" = None):
        self.name = name
        self.states = states
        self.NHSM_State = NHSM_State
        self.NHSM_State7 = NHSM_State7
        self.State = State
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def states(self):
        return self.__states

    @states.setter
    def states(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NHSM_State__states", None)
        self.__states = value
        
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
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NHSM_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "machine"):
                opp_val = getattr(old_value, "machine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "machine"):
                opp_val = getattr(value, "machine", None)
                if opp_val is None:
                    setattr(value, "machine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def NHSM_State7(self):
        return self.__NHSM_State7

    @NHSM_State7.setter
    def NHSM_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NHSM_State__NHSM_State7", None)
        self.__NHSM_State7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NHSM_Transition6"):
                opp_val = getattr(old_value, "NHSM_Transition6", None)
                if opp_val == self:
                    setattr(old_value, "NHSM_Transition6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NHSM_Transition6"):
                opp_val = getattr(value, "NHSM_Transition6", None)
                setattr(value, "NHSM_Transition6", self)

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
            if hasattr(old_value, "NHSM_Transition4"):
                opp_val = getattr(old_value, "NHSM_Transition4", None)
                if opp_val == self:
                    setattr(old_value, "NHSM_Transition4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NHSM_Transition4"):
                opp_val = getattr(value, "NHSM_Transition4", None)
                setattr(value, "NHSM_Transition4", self)

class NHSM_StateMachine:

    def __init__(self, name: str, StateMachine: "NHSM_State" = None, NHSM_StateMachine10: "NHSM_Transition" = None, machine: set["NHSM_State"] = None, NHSM_StateMachine: set["NHSM_Transition"] = None):
        self.name = name
        self.StateMachine = StateMachine
        self.NHSM_StateMachine10 = NHSM_StateMachine10
        self.machine = machine if machine is not None else set()
        self.NHSM_StateMachine = NHSM_StateMachine if NHSM_StateMachine is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def machine(self):
        return self.__machine

    @machine.setter
    def machine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NHSM_StateMachine__machine", None)
        self.__machine = value if value is not None else set()
        
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
            if hasattr(old_value, "states"):
                opp_val = getattr(old_value, "states", None)
                if opp_val == self:
                    setattr(old_value, "states", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "states"):
                opp_val = getattr(value, "states", None)
                setattr(value, "states", self)

    @property
    def NHSM_StateMachine(self):
        return self.__NHSM_StateMachine

    @NHSM_StateMachine.setter
    def NHSM_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NHSM_StateMachine__NHSM_StateMachine", None)
        self.__NHSM_StateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NHSM_Transition"):
                    opp_val = getattr(item, "NHSM_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "NHSM_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NHSM_Transition"):
                    opp_val = getattr(item, "NHSM_Transition", None)
                    
                    setattr(item, "NHSM_Transition", self)
                    

    @property
    def NHSM_StateMachine10(self):
        return self.__NHSM_StateMachine10

    @NHSM_StateMachine10.setter
    def NHSM_StateMachine10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NHSM_StateMachine__NHSM_StateMachine10", None)
        self.__NHSM_StateMachine10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NHSM_Transition9"):
                opp_val = getattr(old_value, "NHSM_Transition9", None)
                if opp_val == self:
                    setattr(old_value, "NHSM_Transition9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NHSM_Transition9"):
                opp_val = getattr(value, "NHSM_Transition9", None)
                setattr(value, "NHSM_Transition9", self)
