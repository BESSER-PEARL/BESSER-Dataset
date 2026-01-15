from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class stateMachineEditRules_DFA:

    pass
class stateMachineEditRules_State:

    def __init__(self, isStart: bool, isEnd: bool, id: str, State: "stateMachineEditRules_Transition" = None, State2: "stateMachineEditRules_Transition" = None, from: set["stateMachineEditRules_Transition"] = None, to: set["stateMachineEditRules_Transition"] = None, stateMachineEditRules_State: "stateMachineEditRules_DFA" = None):
        self.isStart = isStart
        self.isEnd = isEnd
        self.id = id
        self.State = State
        self.State2 = State2
        self.from = from if from is not None else set()
        self.to = to if to is not None else set()
        self.stateMachineEditRules_State = stateMachineEditRules_State
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def isEnd(self) -> bool:
        return self.__isEnd

    @isEnd.setter
    def isEnd(self, isEnd: bool):
        self.__isEnd = isEnd

    @property
    def isStart(self) -> bool:
        return self.__isStart

    @isStart.setter
    def isStart(self, isStart: bool):
        self.__isStart = isStart

    @property
    def stateMachineEditRules_State(self):
        return self.__stateMachineEditRules_State

    @stateMachineEditRules_State.setter
    def stateMachineEditRules_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineEditRules_State__stateMachineEditRules_State", None)
        self.__stateMachineEditRules_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineEditRules_DFA"):
                opp_val = getattr(old_value, "stateMachineEditRules_DFA", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineEditRules_DFA"):
                opp_val = getattr(value, "stateMachineEditRules_DFA", None)
                if opp_val is None:
                    setattr(value, "stateMachineEditRules_DFA", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineEditRules_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incomingTransitions"):
                opp_val = getattr(old_value, "incomingTransitions", None)
                if opp_val == self:
                    setattr(old_value, "incomingTransitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incomingTransitions"):
                opp_val = getattr(value, "incomingTransitions", None)
                setattr(value, "incomingTransitions", self)

    @property
    def State2(self):
        return self.__State2

    @State2.setter
    def State2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineEditRules_State__State2", None)
        self.__State2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoingTransitions"):
                opp_val = getattr(old_value, "outgoingTransitions", None)
                if opp_val == self:
                    setattr(old_value, "outgoingTransitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoingTransitions"):
                opp_val = getattr(value, "outgoingTransitions", None)
                setattr(value, "outgoingTransitions", self)

    @property
    def to(self):
        return self.__to

    @to.setter
    def to(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineEditRules_State__to", None)
        self.__to = value if value is not None else set()
        
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
    def from(self):
        return self.__from

    @from.setter
    def from(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineEditRules_State__from", None)
        self.__from = value if value is not None else set()
        
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
                    

class stateMachineEditRules_Transition:

    def __init__(self, input: str, incomingTransitions: "stateMachineEditRules_State" = None, outgoingTransitions: "stateMachineEditRules_State" = None, Transition5: "stateMachineEditRules_State" = None, Transition: "stateMachineEditRules_State" = None, stateMachineEditRules_Transition: "stateMachineEditRules_DFA" = None):
        self.input = input
        self.incomingTransitions = incomingTransitions
        self.outgoingTransitions = outgoingTransitions
        self.Transition5 = Transition5
        self.Transition = Transition
        self.stateMachineEditRules_Transition = stateMachineEditRules_Transition
        
    @property
    def input(self) -> str:
        return self.__input

    @input.setter
    def input(self, input: str):
        self.__input = input

    @property
    def Transition5(self):
        return self.__Transition5

    @Transition5.setter
    def Transition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineEditRules_Transition__Transition5", None)
        self.__Transition5 = value
        
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
    def incomingTransitions(self):
        return self.__incomingTransitions

    @incomingTransitions.setter
    def incomingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineEditRules_Transition__incomingTransitions", None)
        self.__incomingTransitions = value
        
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
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineEditRules_Transition__Transition", None)
        self.__Transition = value
        
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
    def stateMachineEditRules_Transition(self):
        return self.__stateMachineEditRules_Transition

    @stateMachineEditRules_Transition.setter
    def stateMachineEditRules_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineEditRules_Transition__stateMachineEditRules_Transition", None)
        self.__stateMachineEditRules_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineEditRules_DFA8"):
                opp_val = getattr(old_value, "stateMachineEditRules_DFA8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineEditRules_DFA8"):
                opp_val = getattr(value, "stateMachineEditRules_DFA8", None)
                if opp_val is None:
                    setattr(value, "stateMachineEditRules_DFA8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outgoingTransitions(self):
        return self.__outgoingTransitions

    @outgoingTransitions.setter
    def outgoingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineEditRules_Transition__outgoingTransitions", None)
        self.__outgoingTransitions = value
        
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
