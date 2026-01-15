from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class states_State:

    def __init__(self, initial: bool, name: str, states_State6: set["states_Transition"] = None, states_State: "states_Statemachine" = None, states_State14: "states_Transition" = None):
        self.initial = initial
        self.name = name
        self.states_State6 = states_State6 if states_State6 is not None else set()
        self.states_State = states_State
        self.states_State14 = states_State14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def initial(self) -> bool:
        return self.__initial

    @initial.setter
    def initial(self, initial: bool):
        self.__initial = initial

    @property
    def states_State14(self):
        return self.__states_State14

    @states_State14.setter
    def states_State14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_states_State__states_State14", None)
        self.__states_State14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "states_Transition13"):
                opp_val = getattr(old_value, "states_Transition13", None)
                if opp_val == self:
                    setattr(old_value, "states_Transition13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "states_Transition13"):
                opp_val = getattr(value, "states_Transition13", None)
                setattr(value, "states_Transition13", self)

    @property
    def states_State6(self):
        return self.__states_State6

    @states_State6.setter
    def states_State6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_states_State__states_State6", None)
        self.__states_State6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "states_Transition"):
                    opp_val = getattr(item, "states_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "states_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "states_Transition"):
                    opp_val = getattr(item, "states_Transition", None)
                    
                    setattr(item, "states_Transition", self)
                    

    @property
    def states_State(self):
        return self.__states_State

    @states_State.setter
    def states_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_states_State__states_State", None)
        self.__states_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "states_Statemachine4"):
                opp_val = getattr(old_value, "states_Statemachine4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "states_Statemachine4"):
                opp_val = getattr(value, "states_Statemachine4", None)
                if opp_val is None:
                    setattr(value, "states_Statemachine4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class states_Event:

    def __init__(self, name: str, states_Event: "states_Statemachine" = None, states_Event11: "states_Transition" = None):
        self.name = name
        self.states_Event = states_Event
        self.states_Event11 = states_Event11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def states_Event11(self):
        return self.__states_Event11

    @states_Event11.setter
    def states_Event11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_states_Event__states_Event11", None)
        self.__states_Event11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "states_Transition10"):
                opp_val = getattr(old_value, "states_Transition10", None)
                if opp_val == self:
                    setattr(old_value, "states_Transition10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "states_Transition10"):
                opp_val = getattr(value, "states_Transition10", None)
                setattr(value, "states_Transition10", self)

    @property
    def states_Event(self):
        return self.__states_Event

    @states_Event.setter
    def states_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_states_Event__states_Event", None)
        self.__states_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "states_Statemachine2"):
                opp_val = getattr(old_value, "states_Statemachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "states_Statemachine2"):
                opp_val = getattr(value, "states_Statemachine2", None)
                if opp_val is None:
                    setattr(value, "states_Statemachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class State:

    pass
class states_CompoundState(State):

    pass
class states_SimpleState(State):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class states_Transition:

    pass
class states_Statemachine:

    def __init__(self, initial: bool, name: str, value: int, states_Statemachine: "states_Module" = None, states_Statemachine8: "states_CompoundState" = None, states_Statemachine2: set["states_Event"] = None, states_Statemachine4: set["states_State"] = None):
        self.initial = initial
        self.name = name
        self.value = value
        self.states_Statemachine = states_Statemachine
        self.states_Statemachine8 = states_Statemachine8
        self.states_Statemachine2 = states_Statemachine2 if states_Statemachine2 is not None else set()
        self.states_Statemachine4 = states_Statemachine4 if states_Statemachine4 is not None else set()
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

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
    def states_Statemachine4(self):
        return self.__states_Statemachine4

    @states_Statemachine4.setter
    def states_Statemachine4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_states_Statemachine__states_Statemachine4", None)
        self.__states_Statemachine4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "states_State"):
                    opp_val = getattr(item, "states_State", None)
                    
                    if opp_val == self:
                        setattr(item, "states_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "states_State"):
                    opp_val = getattr(item, "states_State", None)
                    
                    setattr(item, "states_State", self)
                    

    @property
    def states_Statemachine(self):
        return self.__states_Statemachine

    @states_Statemachine.setter
    def states_Statemachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_states_Statemachine__states_Statemachine", None)
        self.__states_Statemachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "states_Module"):
                opp_val = getattr(old_value, "states_Module", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "states_Module"):
                opp_val = getattr(value, "states_Module", None)
                if opp_val is None:
                    setattr(value, "states_Module", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def states_Statemachine8(self):
        return self.__states_Statemachine8

    @states_Statemachine8.setter
    def states_Statemachine8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_states_Statemachine__states_Statemachine8", None)
        self.__states_Statemachine8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "states_CompoundState"):
                opp_val = getattr(old_value, "states_CompoundState", None)
                if opp_val == self:
                    setattr(old_value, "states_CompoundState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "states_CompoundState"):
                opp_val = getattr(value, "states_CompoundState", None)
                setattr(value, "states_CompoundState", self)

    @property
    def states_Statemachine2(self):
        return self.__states_Statemachine2

    @states_Statemachine2.setter
    def states_Statemachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_states_Statemachine__states_Statemachine2", None)
        self.__states_Statemachine2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "states_Event"):
                    opp_val = getattr(item, "states_Event", None)
                    
                    if opp_val == self:
                        setattr(item, "states_Event", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "states_Event"):
                    opp_val = getattr(item, "states_Event", None)
                    
                    setattr(item, "states_Event", self)
                    

class states_Module:

    def __init__(self, name: str, states_Module: set["states_Statemachine"] = None):
        self.name = name
        self.states_Module = states_Module if states_Module is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def states_Module(self):
        return self.__states_Module

    @states_Module.setter
    def states_Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_states_Module__states_Module", None)
        self.__states_Module = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "states_Statemachine"):
                    opp_val = getattr(item, "states_Statemachine", None)
                    
                    if opp_val == self:
                        setattr(item, "states_Statemachine", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "states_Statemachine"):
                    opp_val = getattr(item, "states_Statemachine", None)
                    
                    setattr(item, "states_Statemachine", self)
                    
