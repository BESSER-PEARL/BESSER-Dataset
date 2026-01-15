from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class statemachine_mk2_Event:

    def __init__(self, description: str, statemachine_mk2_Event19: "statemachine_mk2_Transition" = None, statemachine_mk2_Event21: set["statemachine_mk2_State"] = None, statemachine_mk2_Event: "statemachine_mk2_StateMachine" = None, statemachine_mk2_Event24: set["statemachine_mk2_Transition"] = None):
        self.description = description
        self.statemachine_mk2_Event19 = statemachine_mk2_Event19
        self.statemachine_mk2_Event21 = statemachine_mk2_Event21 if statemachine_mk2_Event21 is not None else set()
        self.statemachine_mk2_Event = statemachine_mk2_Event
        self.statemachine_mk2_Event24 = statemachine_mk2_Event24 if statemachine_mk2_Event24 is not None else set()
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def statemachine_mk2_Event19(self):
        return self.__statemachine_mk2_Event19

    @statemachine_mk2_Event19.setter
    def statemachine_mk2_Event19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_mk2_Event__statemachine_mk2_Event19", None)
        self.__statemachine_mk2_Event19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_mk2_Transition18"):
                opp_val = getattr(old_value, "statemachine_mk2_Transition18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_mk2_Transition18"):
                opp_val = getattr(value, "statemachine_mk2_Transition18", None)
                if opp_val is None:
                    setattr(value, "statemachine_mk2_Transition18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachine_mk2_Event24(self):
        return self.__statemachine_mk2_Event24

    @statemachine_mk2_Event24.setter
    def statemachine_mk2_Event24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_mk2_Event__statemachine_mk2_Event24", None)
        self.__statemachine_mk2_Event24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_mk2_Transition25"):
                    opp_val = getattr(item, "statemachine_mk2_Transition25", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_mk2_Transition25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_mk2_Transition25"):
                    opp_val = getattr(item, "statemachine_mk2_Transition25", None)
                    
                    setattr(item, "statemachine_mk2_Transition25", self)
                    

    @property
    def statemachine_mk2_Event(self):
        return self.__statemachine_mk2_Event

    @statemachine_mk2_Event.setter
    def statemachine_mk2_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_mk2_Event__statemachine_mk2_Event", None)
        self.__statemachine_mk2_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_mk2_StateMachine6"):
                opp_val = getattr(old_value, "statemachine_mk2_StateMachine6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_mk2_StateMachine6"):
                opp_val = getattr(value, "statemachine_mk2_StateMachine6", None)
                if opp_val is None:
                    setattr(value, "statemachine_mk2_StateMachine6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachine_mk2_Event21(self):
        return self.__statemachine_mk2_Event21

    @statemachine_mk2_Event21.setter
    def statemachine_mk2_Event21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_mk2_Event__statemachine_mk2_Event21", None)
        self.__statemachine_mk2_Event21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_mk2_State22"):
                    opp_val = getattr(item, "statemachine_mk2_State22", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_mk2_State22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_mk2_State22"):
                    opp_val = getattr(item, "statemachine_mk2_State22", None)
                    
                    setattr(item, "statemachine_mk2_State22", self)
                    

class statemachine_mk2_Transition:

    def __init__(self, name: str, Transition: "statemachine_mk2_State" = None, Transition13: "statemachine_mk2_State" = None, outgoing: "statemachine_mk2_State" = None, incoming: "statemachine_mk2_State" = None, statemachine_mk2_Transition18: set["statemachine_mk2_Event"] = None, statemachine_mk2_Transition: "statemachine_mk2_StateMachine" = None, statemachine_mk2_Transition25: "statemachine_mk2_Event" = None):
        self.name = name
        self.Transition = Transition
        self.Transition13 = Transition13
        self.outgoing = outgoing
        self.incoming = incoming
        self.statemachine_mk2_Transition18 = statemachine_mk2_Transition18 if statemachine_mk2_Transition18 is not None else set()
        self.statemachine_mk2_Transition = statemachine_mk2_Transition
        self.statemachine_mk2_Transition25 = statemachine_mk2_Transition25
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Transition13(self):
        return self.__Transition13

    @Transition13.setter
    def Transition13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_mk2_Transition__Transition13", None)
        self.__Transition13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachine_mk2_Transition25(self):
        return self.__statemachine_mk2_Transition25

    @statemachine_mk2_Transition25.setter
    def statemachine_mk2_Transition25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_mk2_Transition__statemachine_mk2_Transition25", None)
        self.__statemachine_mk2_Transition25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_mk2_Event24"):
                opp_val = getattr(old_value, "statemachine_mk2_Event24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_mk2_Event24"):
                opp_val = getattr(value, "statemachine_mk2_Event24", None)
                if opp_val is None:
                    setattr(value, "statemachine_mk2_Event24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_mk2_Transition__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State"):
                opp_val = getattr(old_value, "State", None)
                if opp_val == self:
                    setattr(old_value, "State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State"):
                opp_val = getattr(value, "State", None)
                setattr(value, "State", self)

    @property
    def statemachine_mk2_Transition18(self):
        return self.__statemachine_mk2_Transition18

    @statemachine_mk2_Transition18.setter
    def statemachine_mk2_Transition18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_mk2_Transition__statemachine_mk2_Transition18", None)
        self.__statemachine_mk2_Transition18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_mk2_Event19"):
                    opp_val = getattr(item, "statemachine_mk2_Event19", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_mk2_Event19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_mk2_Event19"):
                    opp_val = getattr(item, "statemachine_mk2_Event19", None)
                    
                    setattr(item, "statemachine_mk2_Event19", self)
                    

    @property
    def statemachine_mk2_Transition(self):
        return self.__statemachine_mk2_Transition

    @statemachine_mk2_Transition.setter
    def statemachine_mk2_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_mk2_Transition__statemachine_mk2_Transition", None)
        self.__statemachine_mk2_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_mk2_StateMachine4"):
                opp_val = getattr(old_value, "statemachine_mk2_StateMachine4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_mk2_StateMachine4"):
                opp_val = getattr(value, "statemachine_mk2_StateMachine4", None)
                if opp_val is None:
                    setattr(value, "statemachine_mk2_StateMachine4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_mk2_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_mk2_Transition__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State16"):
                opp_val = getattr(old_value, "State16", None)
                if opp_val == self:
                    setattr(old_value, "State16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State16"):
                opp_val = getattr(value, "State16", None)
                setattr(value, "State16", self)

class statemachine_mk2_State(ABC):

    def __init__(self, name: str, source: set["statemachine_mk2_Transition"] = None, target: set["statemachine_mk2_Transition"] = None, State: "statemachine_mk2_Transition" = None, State16: "statemachine_mk2_Transition" = None, statemachine_mk2_State22: "statemachine_mk2_Event" = None, statemachine_mk2_State: "statemachine_mk2_StateMachine" = None, statemachine_mk2_State28: "statemachine_mk2_Composite_state" = None):
        self.name = name
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.State = State
        self.State16 = State16
        self.statemachine_mk2_State22 = statemachine_mk2_State22
        self.statemachine_mk2_State = statemachine_mk2_State
        self.statemachine_mk2_State28 = statemachine_mk2_State28
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statemachine_mk2_State22(self):
        return self.__statemachine_mk2_State22

    @statemachine_mk2_State22.setter
    def statemachine_mk2_State22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_mk2_State__statemachine_mk2_State22", None)
        self.__statemachine_mk2_State22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_mk2_Event21"):
                opp_val = getattr(old_value, "statemachine_mk2_Event21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_mk2_Event21"):
                opp_val = getattr(value, "statemachine_mk2_Event21", None)
                if opp_val is None:
                    setattr(value, "statemachine_mk2_Event21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_mk2_State__source", None)
        self.__source = value if value is not None else set()
        
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
                    

    @property
    def statemachine_mk2_State28(self):
        return self.__statemachine_mk2_State28

    @statemachine_mk2_State28.setter
    def statemachine_mk2_State28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_mk2_State__statemachine_mk2_State28", None)
        self.__statemachine_mk2_State28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_mk2_Composite_state27"):
                opp_val = getattr(old_value, "statemachine_mk2_Composite_state27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_mk2_Composite_state27"):
                opp_val = getattr(value, "statemachine_mk2_Composite_state27", None)
                if opp_val is None:
                    setattr(value, "statemachine_mk2_Composite_state27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def State16(self):
        return self.__State16

    @State16.setter
    def State16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_mk2_State__State16", None)
        self.__State16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incoming"):
                opp_val = getattr(old_value, "incoming", None)
                if opp_val == self:
                    setattr(old_value, "incoming", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incoming"):
                opp_val = getattr(value, "incoming", None)
                setattr(value, "incoming", self)

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_mk2_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoing"):
                opp_val = getattr(old_value, "outgoing", None)
                if opp_val == self:
                    setattr(old_value, "outgoing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoing"):
                opp_val = getattr(value, "outgoing", None)
                setattr(value, "outgoing", self)

    @property
    def statemachine_mk2_State(self):
        return self.__statemachine_mk2_State

    @statemachine_mk2_State.setter
    def statemachine_mk2_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_mk2_State__statemachine_mk2_State", None)
        self.__statemachine_mk2_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_mk2_StateMachine2"):
                opp_val = getattr(old_value, "statemachine_mk2_StateMachine2", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_mk2_StateMachine2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_mk2_StateMachine2"):
                opp_val = getattr(value, "statemachine_mk2_StateMachine2", None)
                setattr(value, "statemachine_mk2_StateMachine2", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_mk2_State__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition13"):
                    opp_val = getattr(item, "Transition13", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition13"):
                    opp_val = getattr(item, "Transition13", None)
                    
                    setattr(item, "Transition13", self)
                    

class statemachine_mk2_StateMachine:

    pass
class State:

    pass
class statemachine_mk2_SimpleState(State):

    pass
class statemachine_mk2_Final_state(State):

    pass
class statemachine_mk2_Composite_state(State):

    pass