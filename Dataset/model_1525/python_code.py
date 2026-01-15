from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class lab1_Transition:

    def __init__(self, name: str, lab1_Transition: "lab1_StateMachine" = None, Transition: "lab1_State" = None, Transition4: "lab1_State" = None, outgoing: "lab1_State" = None, incoming: "lab1_State" = None):
        self.name = name
        self.lab1_Transition = lab1_Transition
        self.Transition = Transition
        self.Transition4 = Transition4
        self.outgoing = outgoing
        self.incoming = incoming
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lab1_Transition__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State7"):
                opp_val = getattr(old_value, "State7", None)
                if opp_val == self:
                    setattr(old_value, "State7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State7"):
                opp_val = getattr(value, "State7", None)
                setattr(value, "State7", self)

    @property
    def lab1_Transition(self):
        return self.__lab1_Transition

    @lab1_Transition.setter
    def lab1_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lab1_Transition__lab1_Transition", None)
        self.__lab1_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lab1_StateMachine"):
                opp_val = getattr(old_value, "lab1_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lab1_StateMachine"):
                opp_val = getattr(value, "lab1_StateMachine", None)
                if opp_val is None:
                    setattr(value, "lab1_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition4(self):
        return self.__Transition4

    @Transition4.setter
    def Transition4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lab1_Transition__Transition4", None)
        self.__Transition4 = value
        
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
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lab1_Transition__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State9"):
                opp_val = getattr(old_value, "State9", None)
                if opp_val == self:
                    setattr(old_value, "State9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State9"):
                opp_val = getattr(value, "State9", None)
                setattr(value, "State9", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lab1_Transition__Transition", None)
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

class lab1_State:

    def __init__(self, name: str, init: bool, State: "lab1_StateMachine" = None, from: set["lab1_Transition"] = None, to: set["lab1_Transition"] = None, states: "lab1_StateMachine" = None, State7: "lab1_Transition" = None, State9: "lab1_Transition" = None):
        self.name = name
        self.init = init
        self.State = State
        self.from = from if from is not None else set()
        self.to = to if to is not None else set()
        self.states = states
        self.State7 = State7
        self.State9 = State9
        
    @property
    def init(self) -> bool:
        return self.__init

    @init.setter
    def init(self, init: bool):
        self.__init = init

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
        old_value = getattr(self, f"_lab1_State__states", None)
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
    def State9(self):
        return self.__State9

    @State9.setter
    def State9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lab1_State__State9", None)
        self.__State9 = value
        
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
    def from(self):
        return self.__from

    @from.setter
    def from(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lab1_State__from", None)
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
    def State7(self):
        return self.__State7

    @State7.setter
    def State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lab1_State__State7", None)
        self.__State7 = value
        
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
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lab1_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm"):
                opp_val = getattr(old_value, "fsm", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm"):
                opp_val = getattr(value, "fsm", None)
                if opp_val is None:
                    setattr(value, "fsm", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def to(self):
        return self.__to

    @to.setter
    def to(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lab1_State__to", None)
        self.__to = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition4"):
                    opp_val = getattr(item, "Transition4", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition4"):
                    opp_val = getattr(item, "Transition4", None)
                    
                    setattr(item, "Transition4", self)
                    

class lab1_StateMachine:

    def __init__(self, name: str, fsm: set["lab1_State"] = None, lab1_StateMachine: set["lab1_Transition"] = None, StateMachine: "lab1_State" = None):
        self.name = name
        self.fsm = fsm if fsm is not None else set()
        self.lab1_StateMachine = lab1_StateMachine if lab1_StateMachine is not None else set()
        self.StateMachine = StateMachine
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fsm(self):
        return self.__fsm

    @fsm.setter
    def fsm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lab1_StateMachine__fsm", None)
        self.__fsm = value if value is not None else set()
        
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
    def lab1_StateMachine(self):
        return self.__lab1_StateMachine

    @lab1_StateMachine.setter
    def lab1_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lab1_StateMachine__lab1_StateMachine", None)
        self.__lab1_StateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lab1_Transition"):
                    opp_val = getattr(item, "lab1_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "lab1_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lab1_Transition"):
                    opp_val = getattr(item, "lab1_Transition", None)
                    
                    setattr(item, "lab1_Transition", self)
                    

    @property
    def StateMachine(self):
        return self.__StateMachine

    @StateMachine.setter
    def StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lab1_StateMachine__StateMachine", None)
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
