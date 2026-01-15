from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class FSM_Transition:

    def __init__(self, input: str, Transition: "FSM_State" = None, Transition6: "FSM_State" = None, outgoing: "FSM_State" = None, incoming: "FSM_State" = None):
        self.input = input
        self.Transition = Transition
        self.Transition6 = Transition6
        self.outgoing = outgoing
        self.incoming = incoming
        
    @property
    def input(self) -> str:
        return self.__input

    @input.setter
    def input(self, input: str):
        self.__input = input

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_Transition__incoming", None)
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
        old_value = getattr(self, f"_FSM_Transition__Transition", None)
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
    def Transition6(self):
        return self.__Transition6

    @Transition6.setter
    def Transition6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_Transition__Transition6", None)
        self.__Transition6 = value
        
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
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_Transition__outgoing", None)
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

class FSM_State:

    def __init__(self, name: str, isAccepting: bool, FSM_State: "FSM_StateMachine" = None, FSM_State3: "FSM_StateMachine" = None, source: set["FSM_Transition"] = None, target: set["FSM_Transition"] = None, State: "FSM_Transition" = None, State9: "FSM_Transition" = None):
        self.name = name
        self.isAccepting = isAccepting
        self.FSM_State = FSM_State
        self.FSM_State3 = FSM_State3
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.State = State
        self.State9 = State9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isAccepting(self) -> bool:
        return self.__isAccepting

    @isAccepting.setter
    def isAccepting(self, isAccepting: bool):
        self.__isAccepting = isAccepting

    @property
    def FSM_State(self):
        return self.__FSM_State

    @FSM_State.setter
    def FSM_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_State__FSM_State", None)
        self.__FSM_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM_StateMachine"):
                opp_val = getattr(old_value, "FSM_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM_StateMachine"):
                opp_val = getattr(value, "FSM_StateMachine", None)
                if opp_val is None:
                    setattr(value, "FSM_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_State__target", None)
        self.__target = value if value is not None else set()
        
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
    def FSM_State3(self):
        return self.__FSM_State3

    @FSM_State3.setter
    def FSM_State3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_State__FSM_State3", None)
        self.__FSM_State3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM_StateMachine2"):
                opp_val = getattr(old_value, "FSM_StateMachine2", None)
                if opp_val == self:
                    setattr(old_value, "FSM_StateMachine2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM_StateMachine2"):
                opp_val = getattr(value, "FSM_StateMachine2", None)
                setattr(value, "FSM_StateMachine2", self)

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_State__State", None)
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
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_State__source", None)
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
    def State9(self):
        return self.__State9

    @State9.setter
    def State9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_State__State9", None)
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

class FSM_StateMachine:

    def __init__(self, name: str, FSM_StateMachine: set["FSM_State"] = None, FSM_StateMachine2: "FSM_State" = None):
        self.name = name
        self.FSM_StateMachine = FSM_StateMachine if FSM_StateMachine is not None else set()
        self.FSM_StateMachine2 = FSM_StateMachine2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def FSM_StateMachine2(self):
        return self.__FSM_StateMachine2

    @FSM_StateMachine2.setter
    def FSM_StateMachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_StateMachine__FSM_StateMachine2", None)
        self.__FSM_StateMachine2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM_State3"):
                opp_val = getattr(old_value, "FSM_State3", None)
                if opp_val == self:
                    setattr(old_value, "FSM_State3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM_State3"):
                opp_val = getattr(value, "FSM_State3", None)
                setattr(value, "FSM_State3", self)

    @property
    def FSM_StateMachine(self):
        return self.__FSM_StateMachine

    @FSM_StateMachine.setter
    def FSM_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_StateMachine__FSM_StateMachine", None)
        self.__FSM_StateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FSM_State"):
                    opp_val = getattr(item, "FSM_State", None)
                    
                    if opp_val == self:
                        setattr(item, "FSM_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FSM_State"):
                    opp_val = getattr(item, "FSM_State", None)
                    
                    setattr(item, "FSM_State", self)
                    
