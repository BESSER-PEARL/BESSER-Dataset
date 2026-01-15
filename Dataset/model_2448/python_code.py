from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class gfsm_Machine:

    pass
class gfsm_State:

    def __init__(self, name: str, State2: "gfsm_Transition" = None, State: "gfsm_Transition" = None, gfsm_State: "gfsm_Machine" = None, from: set["gfsm_Transition"] = None, to: set["gfsm_Transition"] = None, gfsm_State13: "gfsm_Machine" = None):
        self.name = name
        self.State2 = State2
        self.State = State
        self.gfsm_State = gfsm_State
        self.from = from if from is not None else set()
        self.to = to if to is not None else set()
        self.gfsm_State13 = gfsm_State13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def State2(self):
        return self.__State2

    @State2.setter
    def State2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_State__State2", None)
        self.__State2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incommings"):
                opp_val = getattr(old_value, "incommings", None)
                if opp_val == self:
                    setattr(old_value, "incommings", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incommings"):
                opp_val = getattr(value, "incommings", None)
                setattr(value, "incommings", self)

    @property
    def to(self):
        return self.__to

    @to.setter
    def to(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_State__to", None)
        self.__to = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition6"):
                    opp_val = getattr(item, "Transition6", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition6"):
                    opp_val = getattr(item, "Transition6", None)
                    
                    setattr(item, "Transition6", self)
                    

    @property
    def gfsm_State(self):
        return self.__gfsm_State

    @gfsm_State.setter
    def gfsm_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_State__gfsm_State", None)
        self.__gfsm_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gfsm_Machine"):
                opp_val = getattr(old_value, "gfsm_Machine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gfsm_Machine"):
                opp_val = getattr(value, "gfsm_Machine", None)
                if opp_val is None:
                    setattr(value, "gfsm_Machine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def from(self):
        return self.__from

    @from.setter
    def from(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_State__from", None)
        self.__from = value if value is not None else set()
        
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
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoings"):
                opp_val = getattr(old_value, "outgoings", None)
                if opp_val == self:
                    setattr(old_value, "outgoings", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoings"):
                opp_val = getattr(value, "outgoings", None)
                setattr(value, "outgoings", self)

    @property
    def gfsm_State13(self):
        return self.__gfsm_State13

    @gfsm_State13.setter
    def gfsm_State13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_State__gfsm_State13", None)
        self.__gfsm_State13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gfsm_Machine12"):
                opp_val = getattr(old_value, "gfsm_Machine12", None)
                if opp_val == self:
                    setattr(old_value, "gfsm_Machine12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gfsm_Machine12"):
                opp_val = getattr(value, "gfsm_Machine12", None)
                setattr(value, "gfsm_Machine12", self)

class gfsm_Transition:

    def __init__(self, event: str, incommings: "gfsm_State" = None, gfsm_Transition: "gfsm_Guard" = None, Transition: "gfsm_State" = None, outgoings: "gfsm_State" = None, gfsm_Transition10: "gfsm_Machine" = None, Transition6: "gfsm_State" = None):
        self.event = event
        self.incommings = incommings
        self.gfsm_Transition = gfsm_Transition
        self.Transition = Transition
        self.outgoings = outgoings
        self.gfsm_Transition10 = gfsm_Transition10
        self.Transition6 = Transition6
        
    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

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
            if hasattr(old_value, "from"):
                opp_val = getattr(old_value, "from", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "from"):
                opp_val = getattr(value, "from", None)
                if opp_val is None:
                    setattr(value, "from", set([self]))
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
    def gfsm_Transition10(self):
        return self.__gfsm_Transition10

    @gfsm_Transition10.setter
    def gfsm_Transition10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_Transition__gfsm_Transition10", None)
        self.__gfsm_Transition10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gfsm_Machine9"):
                opp_val = getattr(old_value, "gfsm_Machine9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gfsm_Machine9"):
                opp_val = getattr(value, "gfsm_Machine9", None)
                if opp_val is None:
                    setattr(value, "gfsm_Machine9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition6(self):
        return self.__Transition6

    @Transition6.setter
    def Transition6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_Transition__Transition6", None)
        self.__Transition6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "to"):
                opp_val = getattr(old_value, "to", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "to"):
                opp_val = getattr(value, "to", None)
                if opp_val is None:
                    setattr(value, "to", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outgoings(self):
        return self.__outgoings

    @outgoings.setter
    def outgoings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_Transition__outgoings", None)
        self.__outgoings = value
        
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
    def incommings(self):
        return self.__incommings

    @incommings.setter
    def incommings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_Transition__incommings", None)
        self.__incommings = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State2"):
                opp_val = getattr(old_value, "State2", None)
                if opp_val == self:
                    setattr(old_value, "State2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State2"):
                opp_val = getattr(value, "State2", None)
                setattr(value, "State2", self)

class gfsm_Guard:

    def __init__(self, value: str, gfsm_Guard: "gfsm_Transition" = None):
        self.value = value
        self.gfsm_Guard = gfsm_Guard
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def gfsm_Guard(self):
        return self.__gfsm_Guard

    @gfsm_Guard.setter
    def gfsm_Guard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_Guard__gfsm_Guard", None)
        self.__gfsm_Guard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gfsm_Transition"):
                opp_val = getattr(old_value, "gfsm_Transition", None)
                if opp_val == self:
                    setattr(old_value, "gfsm_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gfsm_Transition"):
                opp_val = getattr(value, "gfsm_Transition", None)
                setattr(value, "gfsm_Transition", self)
