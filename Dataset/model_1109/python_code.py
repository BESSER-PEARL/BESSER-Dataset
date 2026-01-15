from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class oclstates_Statemachine:

    def __init__(self, initial: bool, name: str, value: int, oclstates_Statemachine2: set["oclstates_Event"] = None, oclstates_Statemachine4: set["oclstates_State"] = None, oclstates_Statemachine9: "oclstates_State" = None, oclstates_Statemachine: "oclstates_Module" = None, oclstates_Statemachine11: "oclstates_CompoundState" = None):
        self.initial = initial
        self.name = name
        self.value = value
        self.oclstates_Statemachine2 = oclstates_Statemachine2 if oclstates_Statemachine2 is not None else set()
        self.oclstates_Statemachine4 = oclstates_Statemachine4 if oclstates_Statemachine4 is not None else set()
        self.oclstates_Statemachine9 = oclstates_Statemachine9
        self.oclstates_Statemachine = oclstates_Statemachine
        self.oclstates_Statemachine11 = oclstates_Statemachine11
        
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
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def oclstates_Statemachine2(self):
        return self.__oclstates_Statemachine2

    @oclstates_Statemachine2.setter
    def oclstates_Statemachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oclstates_Statemachine__oclstates_Statemachine2", None)
        self.__oclstates_Statemachine2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "oclstates_Event"):
                    opp_val = getattr(item, "oclstates_Event", None)
                    
                    if opp_val == self:
                        setattr(item, "oclstates_Event", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "oclstates_Event"):
                    opp_val = getattr(item, "oclstates_Event", None)
                    
                    setattr(item, "oclstates_Event", self)
                    

    @property
    def oclstates_Statemachine4(self):
        return self.__oclstates_Statemachine4

    @oclstates_Statemachine4.setter
    def oclstates_Statemachine4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oclstates_Statemachine__oclstates_Statemachine4", None)
        self.__oclstates_Statemachine4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "oclstates_State"):
                    opp_val = getattr(item, "oclstates_State", None)
                    
                    if opp_val == self:
                        setattr(item, "oclstates_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "oclstates_State"):
                    opp_val = getattr(item, "oclstates_State", None)
                    
                    setattr(item, "oclstates_State", self)
                    

    @property
    def oclstates_Statemachine11(self):
        return self.__oclstates_Statemachine11

    @oclstates_Statemachine11.setter
    def oclstates_Statemachine11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oclstates_Statemachine__oclstates_Statemachine11", None)
        self.__oclstates_Statemachine11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oclstates_CompoundState"):
                opp_val = getattr(old_value, "oclstates_CompoundState", None)
                if opp_val == self:
                    setattr(old_value, "oclstates_CompoundState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oclstates_CompoundState"):
                opp_val = getattr(value, "oclstates_CompoundState", None)
                setattr(value, "oclstates_CompoundState", self)

    @property
    def oclstates_Statemachine(self):
        return self.__oclstates_Statemachine

    @oclstates_Statemachine.setter
    def oclstates_Statemachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oclstates_Statemachine__oclstates_Statemachine", None)
        self.__oclstates_Statemachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oclstates_Module"):
                opp_val = getattr(old_value, "oclstates_Module", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oclstates_Module"):
                opp_val = getattr(value, "oclstates_Module", None)
                if opp_val is None:
                    setattr(value, "oclstates_Module", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def oclstates_Statemachine9(self):
        return self.__oclstates_Statemachine9

    @oclstates_Statemachine9.setter
    def oclstates_Statemachine9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oclstates_Statemachine__oclstates_Statemachine9", None)
        self.__oclstates_Statemachine9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oclstates_State8"):
                opp_val = getattr(old_value, "oclstates_State8", None)
                if opp_val == self:
                    setattr(old_value, "oclstates_State8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oclstates_State8"):
                opp_val = getattr(value, "oclstates_State8", None)
                setattr(value, "oclstates_State8", self)

class State:

    pass
class oclstates_CompoundState(State):

    pass
class oclstates_SimpleState(State):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class oclstates_Transition:

    pass
class oclstates_State:

    def __init__(self, initial: bool, name: str, oclstates_State: "oclstates_Statemachine" = None, oclstates_State6: set["oclstates_Transition"] = None, oclstates_State8: "oclstates_Statemachine" = None, oclstates_State17: "oclstates_Transition" = None):
        self.initial = initial
        self.name = name
        self.oclstates_State = oclstates_State
        self.oclstates_State6 = oclstates_State6 if oclstates_State6 is not None else set()
        self.oclstates_State8 = oclstates_State8
        self.oclstates_State17 = oclstates_State17
        
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
    def oclstates_State17(self):
        return self.__oclstates_State17

    @oclstates_State17.setter
    def oclstates_State17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oclstates_State__oclstates_State17", None)
        self.__oclstates_State17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oclstates_Transition16"):
                opp_val = getattr(old_value, "oclstates_Transition16", None)
                if opp_val == self:
                    setattr(old_value, "oclstates_Transition16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oclstates_Transition16"):
                opp_val = getattr(value, "oclstates_Transition16", None)
                setattr(value, "oclstates_Transition16", self)

    @property
    def oclstates_State(self):
        return self.__oclstates_State

    @oclstates_State.setter
    def oclstates_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oclstates_State__oclstates_State", None)
        self.__oclstates_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oclstates_Statemachine4"):
                opp_val = getattr(old_value, "oclstates_Statemachine4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oclstates_Statemachine4"):
                opp_val = getattr(value, "oclstates_Statemachine4", None)
                if opp_val is None:
                    setattr(value, "oclstates_Statemachine4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def oclstates_State6(self):
        return self.__oclstates_State6

    @oclstates_State6.setter
    def oclstates_State6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oclstates_State__oclstates_State6", None)
        self.__oclstates_State6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "oclstates_Transition"):
                    opp_val = getattr(item, "oclstates_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "oclstates_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "oclstates_Transition"):
                    opp_val = getattr(item, "oclstates_Transition", None)
                    
                    setattr(item, "oclstates_Transition", self)
                    

    @property
    def oclstates_State8(self):
        return self.__oclstates_State8

    @oclstates_State8.setter
    def oclstates_State8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oclstates_State__oclstates_State8", None)
        self.__oclstates_State8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oclstates_Statemachine9"):
                opp_val = getattr(old_value, "oclstates_Statemachine9", None)
                if opp_val == self:
                    setattr(old_value, "oclstates_Statemachine9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oclstates_Statemachine9"):
                opp_val = getattr(value, "oclstates_Statemachine9", None)
                setattr(value, "oclstates_Statemachine9", self)

class oclstates_Event:

    def __init__(self, name: str, oclstates_Event: "oclstates_Statemachine" = None, oclstates_Event14: "oclstates_Transition" = None):
        self.name = name
        self.oclstates_Event = oclstates_Event
        self.oclstates_Event14 = oclstates_Event14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def oclstates_Event14(self):
        return self.__oclstates_Event14

    @oclstates_Event14.setter
    def oclstates_Event14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oclstates_Event__oclstates_Event14", None)
        self.__oclstates_Event14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oclstates_Transition13"):
                opp_val = getattr(old_value, "oclstates_Transition13", None)
                if opp_val == self:
                    setattr(old_value, "oclstates_Transition13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oclstates_Transition13"):
                opp_val = getattr(value, "oclstates_Transition13", None)
                setattr(value, "oclstates_Transition13", self)

    @property
    def oclstates_Event(self):
        return self.__oclstates_Event

    @oclstates_Event.setter
    def oclstates_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oclstates_Event__oclstates_Event", None)
        self.__oclstates_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oclstates_Statemachine2"):
                opp_val = getattr(old_value, "oclstates_Statemachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oclstates_Statemachine2"):
                opp_val = getattr(value, "oclstates_Statemachine2", None)
                if opp_val is None:
                    setattr(value, "oclstates_Statemachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class oclstates_Module:

    def __init__(self, name: str, oclstates_Module: set["oclstates_Statemachine"] = None):
        self.name = name
        self.oclstates_Module = oclstates_Module if oclstates_Module is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def oclstates_Module(self):
        return self.__oclstates_Module

    @oclstates_Module.setter
    def oclstates_Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oclstates_Module__oclstates_Module", None)
        self.__oclstates_Module = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "oclstates_Statemachine"):
                    opp_val = getattr(item, "oclstates_Statemachine", None)
                    
                    if opp_val == self:
                        setattr(item, "oclstates_Statemachine", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "oclstates_Statemachine"):
                    opp_val = getattr(item, "oclstates_Statemachine", None)
                    
                    setattr(item, "oclstates_Statemachine", self)
                    
