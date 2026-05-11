from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class dfamodel_Transition:

    def __init__(self, input: str, dfamodel_Transition: "dfamodel_DFA" = None, outgoingTransitions: "dfamodel_State" = None, incomingTransitions: "dfamodel_State" = None, Transition: "dfamodel_State" = None, Transition8: "dfamodel_State" = None):
        self.input = input
        self.dfamodel_Transition = dfamodel_Transition
        self.outgoingTransitions = outgoingTransitions
        self.incomingTransitions = incomingTransitions
        self.Transition = Transition
        self.Transition8 = Transition8
        
        pass
    @property
    def input(self):
        return self.__input

    @input.setter
    def input(self, input: str):
        self.__input = input


    @property
    def Transition8(self):
        return self.__Transition8

    @Transition8.setter
    def Transition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dfamodel_Transition__Transition8", None)
        self.__Transition8 = value
        
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
    def outgoingTransitions(self):
        return self.__outgoingTransitions

    @outgoingTransitions.setter
    def outgoingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dfamodel_Transition__outgoingTransitions", None)
        self.__outgoingTransitions = value
        
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
    def incomingTransitions(self):
        return self.__incomingTransitions

    @incomingTransitions.setter
    def incomingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dfamodel_Transition__incomingTransitions", None)
        self.__incomingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State5"):
                opp_val = getattr(old_value, "State5", None)
                if opp_val == self:
                    setattr(old_value, "State5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State5"):
                opp_val = getattr(value, "State5", None)
                setattr(value, "State5", self)

    @property
    def dfamodel_Transition(self):
        return self.__dfamodel_Transition

    @dfamodel_Transition.setter
    def dfamodel_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dfamodel_Transition__dfamodel_Transition", None)
        self.__dfamodel_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dfamodel_DFA2"):
                opp_val = getattr(old_value, "dfamodel_DFA2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dfamodel_DFA2"):
                opp_val = getattr(value, "dfamodel_DFA2", None)
                if opp_val is None:
                    setattr(value, "dfamodel_DFA2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dfamodel_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "from_"):
                opp_val = getattr(old_value, "from_", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "from_"):
                opp_val = getattr(value, "from_", None)
                if opp_val is None:
                    setattr(value, "from_", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dfamodel_State:

    def __init__(self, id: str, isStart: bool, isEnd: bool, dfamodel_State: "dfamodel_DFA" = None, State: "dfamodel_Transition" = None, State5: "dfamodel_Transition" = None, from_: set["dfamodel_Transition"] = None, to: set["dfamodel_Transition"] = None):
        self.id = id
        self.isStart = isStart
        self.isEnd = isEnd
        self.dfamodel_State = dfamodel_State
        self.State = State
        self.State5 = State5
        self.from_ = from_ if from_ is not None else set()
        self.to = to if to is not None else set()
        
        pass
    @property
    def isStart(self):
        return self.__isStart

    @isStart.setter
    def isStart(self, isStart: bool):
        self.__isStart = isStart


    @property
    def isEnd(self):
        return self.__isEnd

    @isEnd.setter
    def isEnd(self, isEnd: bool):
        self.__isEnd = isEnd


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def from_(self):
        return self.__from_

    @from_.setter
    def from_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dfamodel_State__from_", None)
        self.__from_ = value if value is not None else set()
        
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
    def dfamodel_State(self):
        return self.__dfamodel_State

    @dfamodel_State.setter
    def dfamodel_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dfamodel_State__dfamodel_State", None)
        self.__dfamodel_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dfamodel_DFA"):
                opp_val = getattr(old_value, "dfamodel_DFA", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dfamodel_DFA"):
                opp_val = getattr(value, "dfamodel_DFA", None)
                if opp_val is None:
                    setattr(value, "dfamodel_DFA", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def State5(self):
        return self.__State5

    @State5.setter
    def State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dfamodel_State__State5", None)
        self.__State5 = value
        
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
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dfamodel_State__State", None)
        self.__State = value
        
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
        old_value = getattr(self, f"_dfamodel_State__to", None)
        self.__to = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition8"):
                    opp_val = getattr(item, "Transition8", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition8"):
                    opp_val = getattr(item, "Transition8", None)
                    
                    setattr(item, "Transition8", self)
                    

class dfamodel_DFA:

    pass