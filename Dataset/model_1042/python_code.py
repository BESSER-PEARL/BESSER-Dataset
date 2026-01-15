from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class State:

    pass
class gfsm_FinalState(State):

    pass
class gfsm_InitialState(State):

    pass
class gfsm_State:

    def __init__(self, name: str, states: "gfsm_Machine" = None, target: set["gfsm_Transition"] = None, source: set["gfsm_Transition"] = None, State11: "gfsm_Transition" = None, State13: "gfsm_Transition" = None, State: "gfsm_Machine" = None):
        self.name = name
        self.states = states
        self.target = target if target is not None else set()
        self.source = source if source is not None else set()
        self.State11 = State11
        self.State13 = State13
        self.State = State
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_State__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition5"):
                    opp_val = getattr(item, "Transition5", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition5"):
                    opp_val = getattr(item, "Transition5", None)
                    
                    setattr(item, "Transition5", self)
                    

    @property
    def states(self):
        return self.__states

    @states.setter
    def states(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_State__states", None)
        self.__states = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Machine"):
                opp_val = getattr(old_value, "Machine", None)
                if opp_val == self:
                    setattr(old_value, "Machine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Machine"):
                opp_val = getattr(value, "Machine", None)
                setattr(value, "Machine", self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_State__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition7"):
                    opp_val = getattr(item, "Transition7", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition7"):
                    opp_val = getattr(item, "Transition7", None)
                    
                    setattr(item, "Transition7", self)
                    

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owning2"):
                opp_val = getattr(old_value, "owning2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owning2"):
                opp_val = getattr(value, "owning2", None)
                if opp_val is None:
                    setattr(value, "owning2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def State11(self):
        return self.__State11

    @State11.setter
    def State11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_State__State11", None)
        self.__State11 = value
        
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
    def State13(self):
        return self.__State13

    @State13.setter
    def State13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_State__State13", None)
        self.__State13 = value
        
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

class gfsm_Transition:

    def __init__(self, event: str, Transition5: "gfsm_State" = None, Transition7: "gfsm_State" = None, transitions: "gfsm_Machine" = None, incoming: "gfsm_State" = None, outgoing: "gfsm_State" = None, gfsm_Transition: "gfsm_Guard" = None, Transition: "gfsm_Machine" = None):
        self.event = event
        self.Transition5 = Transition5
        self.Transition7 = Transition7
        self.transitions = transitions
        self.incoming = incoming
        self.outgoing = outgoing
        self.gfsm_Transition = gfsm_Transition
        self.Transition = Transition
        
    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_Transition__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State13"):
                opp_val = getattr(old_value, "State13", None)
                if opp_val == self:
                    setattr(old_value, "State13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State13"):
                opp_val = getattr(value, "State13", None)
                setattr(value, "State13", self)

    @property
    def Transition7(self):
        return self.__Transition7

    @Transition7.setter
    def Transition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_Transition__Transition7", None)
        self.__Transition7 = value
        
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
    def Transition5(self):
        return self.__Transition5

    @Transition5.setter
    def Transition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_Transition__Transition5", None)
        self.__Transition5 = value
        
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
    def transitions(self):
        return self.__transitions

    @transitions.setter
    def transitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_Transition__transitions", None)
        self.__transitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Machine9"):
                opp_val = getattr(old_value, "Machine9", None)
                if opp_val == self:
                    setattr(old_value, "Machine9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Machine9"):
                opp_val = getattr(value, "Machine9", None)
                setattr(value, "Machine9", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owning"):
                opp_val = getattr(old_value, "owning", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owning"):
                opp_val = getattr(value, "owning", None)
                if opp_val is None:
                    setattr(value, "owning", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gfsm_Transition(self):
        return self.__gfsm_Transition

    @gfsm_Transition.setter
    def gfsm_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_Transition__gfsm_Transition", None)
        self.__gfsm_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gfsm_Guard"):
                opp_val = getattr(old_value, "gfsm_Guard", None)
                if opp_val == self:
                    setattr(old_value, "gfsm_Guard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gfsm_Guard"):
                opp_val = getattr(value, "gfsm_Guard", None)
                setattr(value, "gfsm_Guard", self)

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_Transition__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State11"):
                opp_val = getattr(old_value, "State11", None)
                if opp_val == self:
                    setattr(old_value, "State11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State11"):
                opp_val = getattr(value, "State11", None)
                setattr(value, "State11", self)

class gfsm_Machine:

    def __init__(self, name: str, Machine: "gfsm_State" = None, Machine9: "gfsm_Transition" = None, owning: set["gfsm_Transition"] = None, owning2: set["gfsm_State"] = None):
        self.name = name
        self.Machine = Machine
        self.Machine9 = Machine9
        self.owning = owning if owning is not None else set()
        self.owning2 = owning2 if owning2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Machine(self):
        return self.__Machine

    @Machine.setter
    def Machine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_Machine__Machine", None)
        self.__Machine = value
        
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
    def owning2(self):
        return self.__owning2

    @owning2.setter
    def owning2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_Machine__owning2", None)
        self.__owning2 = value if value is not None else set()
        
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
    def owning(self):
        return self.__owning

    @owning.setter
    def owning(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_Machine__owning", None)
        self.__owning = value if value is not None else set()
        
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
    def Machine9(self):
        return self.__Machine9

    @Machine9.setter
    def Machine9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_Machine__Machine9", None)
        self.__Machine9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transitions"):
                opp_val = getattr(old_value, "transitions", None)
                if opp_val == self:
                    setattr(old_value, "transitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transitions"):
                opp_val = getattr(value, "transitions", None)
                setattr(value, "transitions", self)

class gfsm_Guard(ABC):

    pass