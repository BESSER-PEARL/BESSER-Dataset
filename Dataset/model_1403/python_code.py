from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class State:

    pass
class HSM_CompositeState(State):

    pass
class HSM_StateMachine:

    def __init__(self, name: str, machine: set["HSM_State"] = None, HSM_StateMachine: set["HSM_Transition"] = None, HSM_StateMachine12: "HSM_Transition" = None, StateMachine: "HSM_State" = None):
        self.name = name
        self.machine = machine if machine is not None else set()
        self.HSM_StateMachine = HSM_StateMachine if HSM_StateMachine is not None else set()
        self.HSM_StateMachine12 = HSM_StateMachine12
        self.StateMachine = StateMachine
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def HSM_StateMachine12(self):
        return self.__HSM_StateMachine12

    @HSM_StateMachine12.setter
    def HSM_StateMachine12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_StateMachine__HSM_StateMachine12", None)
        self.__HSM_StateMachine12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HSM_Transition11"):
                opp_val = getattr(old_value, "HSM_Transition11", None)
                if opp_val == self:
                    setattr(old_value, "HSM_Transition11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HSM_Transition11"):
                opp_val = getattr(value, "HSM_Transition11", None)
                setattr(value, "HSM_Transition11", self)

    @property
    def HSM_StateMachine(self):
        return self.__HSM_StateMachine

    @HSM_StateMachine.setter
    def HSM_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_StateMachine__HSM_StateMachine", None)
        self.__HSM_StateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HSM_Transition"):
                    opp_val = getattr(item, "HSM_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "HSM_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HSM_Transition"):
                    opp_val = getattr(item, "HSM_Transition", None)
                    
                    setattr(item, "HSM_Transition", self)
                    

    @property
    def machine(self):
        return self.__machine

    @machine.setter
    def machine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_StateMachine__machine", None)
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
        old_value = getattr(self, f"_HSM_StateMachine__StateMachine", None)
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

    def addTransition(self, src: str, trg: str):
        # TODO: Implement addTransition method
        pass

class HSM_Transition:

    pass
class HSM_State:

    def __init__(self, name: str, State: "HSM_StateMachine" = None, HSM_State6: "HSM_Transition" = None, HSM_State9: "HSM_Transition" = None, HSM_State: "HSM_CompositeState" = None, states: "HSM_StateMachine" = None):
        self.name = name
        self.State = State
        self.HSM_State6 = HSM_State6
        self.HSM_State9 = HSM_State9
        self.HSM_State = HSM_State
        self.states = states
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def states(self):
        return self.__states

    @states.setter
    def states(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_State__states", None)
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
    def HSM_State9(self):
        return self.__HSM_State9

    @HSM_State9.setter
    def HSM_State9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_State__HSM_State9", None)
        self.__HSM_State9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HSM_Transition8"):
                opp_val = getattr(old_value, "HSM_Transition8", None)
                if opp_val == self:
                    setattr(old_value, "HSM_Transition8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HSM_Transition8"):
                opp_val = getattr(value, "HSM_Transition8", None)
                setattr(value, "HSM_Transition8", self)

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
