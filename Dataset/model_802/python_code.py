from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class k3fsm_Transition:

    def __init__(self, input: str, name: str, output: str, incomingTransitions: "k3fsm_State" = None, outgoingTransitions: "k3fsm_State" = None, Transition: "k3fsm_State" = None, Transition10: "k3fsm_State" = None):
        self.input = input
        self.name = name
        self.output = output
        self.incomingTransitions = incomingTransitions
        self.outgoingTransitions = outgoingTransitions
        self.Transition = Transition
        self.Transition10 = Transition10
        
        pass
    @property
    def output(self):
        return self.__output

    @output.setter
    def output(self, output: str):
        self.__output = output


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def input(self):
        return self.__input

    @input.setter
    def input(self, input: str):
        self.__input = input


    @property
    def outgoingTransitions(self):
        return self.__outgoingTransitions

    @outgoingTransitions.setter
    def outgoingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k3fsm_Transition__outgoingTransitions", None)
        self.__outgoingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State15"):
                opp_val = getattr(old_value, "State15", None)
                if opp_val == self:
                    setattr(old_value, "State15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State15"):
                opp_val = getattr(value, "State15", None)
                setattr(value, "State15", self)

    @property
    def Transition10(self):
        return self.__Transition10

    @Transition10.setter
    def Transition10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k3fsm_Transition__Transition10", None)
        self.__Transition10 = value
        
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
    def incomingTransitions(self):
        return self.__incomingTransitions

    @incomingTransitions.setter
    def incomingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k3fsm_Transition__incomingTransitions", None)
        self.__incomingTransitions = value
        
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
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k3fsm_Transition__Transition", None)
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

class k3fsm_State:

    def __init__(self, name: str, State13: "k3fsm_Transition" = None, State15: "k3fsm_Transition" = None, k3fsm_State4: "k3fsm_FSM" = None, State: "k3fsm_FSM" = None, k3fsm_State: "k3fsm_FSM" = None, k3fsm_State7: "k3fsm_FSM" = None, source: set["k3fsm_Transition"] = None, target: set["k3fsm_Transition"] = None, ownedStates: "k3fsm_FSM" = None):
        self.name = name
        self.State13 = State13
        self.State15 = State15
        self.k3fsm_State4 = k3fsm_State4
        self.State = State
        self.k3fsm_State = k3fsm_State
        self.k3fsm_State7 = k3fsm_State7
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.ownedStates = ownedStates
        
        pass
    @property
    def name(self):
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
        old_value = getattr(self, f"_k3fsm_State__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition10"):
                    opp_val = getattr(item, "Transition10", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition10"):
                    opp_val = getattr(item, "Transition10", None)
                    
                    setattr(item, "Transition10", self)
                    

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k3fsm_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningFSM"):
                opp_val = getattr(old_value, "owningFSM", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningFSM"):
                opp_val = getattr(value, "owningFSM", None)
                if opp_val is None:
                    setattr(value, "owningFSM", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k3fsm_State__source", None)
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
    def k3fsm_State(self):
        return self.__k3fsm_State

    @k3fsm_State.setter
    def k3fsm_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k3fsm_State__k3fsm_State", None)
        self.__k3fsm_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k3fsm_FSM"):
                opp_val = getattr(old_value, "k3fsm_FSM", None)
                if opp_val == self:
                    setattr(old_value, "k3fsm_FSM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k3fsm_FSM"):
                opp_val = getattr(value, "k3fsm_FSM", None)
                setattr(value, "k3fsm_FSM", self)

    @property
    def State15(self):
        return self.__State15

    @State15.setter
    def State15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k3fsm_State__State15", None)
        self.__State15 = value
        
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
    def k3fsm_State4(self):
        return self.__k3fsm_State4

    @k3fsm_State4.setter
    def k3fsm_State4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k3fsm_State__k3fsm_State4", None)
        self.__k3fsm_State4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k3fsm_FSM3"):
                opp_val = getattr(old_value, "k3fsm_FSM3", None)
                if opp_val == self:
                    setattr(old_value, "k3fsm_FSM3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k3fsm_FSM3"):
                opp_val = getattr(value, "k3fsm_FSM3", None)
                setattr(value, "k3fsm_FSM3", self)

    @property
    def ownedStates(self):
        return self.__ownedStates

    @ownedStates.setter
    def ownedStates(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k3fsm_State__ownedStates", None)
        self.__ownedStates = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM"):
                opp_val = getattr(old_value, "FSM", None)
                if opp_val == self:
                    setattr(old_value, "FSM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM"):
                opp_val = getattr(value, "FSM", None)
                setattr(value, "FSM", self)

    @property
    def k3fsm_State7(self):
        return self.__k3fsm_State7

    @k3fsm_State7.setter
    def k3fsm_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k3fsm_State__k3fsm_State7", None)
        self.__k3fsm_State7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k3fsm_FSM6"):
                opp_val = getattr(old_value, "k3fsm_FSM6", None)
                if opp_val == self:
                    setattr(old_value, "k3fsm_FSM6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k3fsm_FSM6"):
                opp_val = getattr(value, "k3fsm_FSM6", None)
                setattr(value, "k3fsm_FSM6", self)

    @property
    def State13(self):
        return self.__State13

    @State13.setter
    def State13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k3fsm_State__State13", None)
        self.__State13 = value
        
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

class k3fsm_FSM:

    def __init__(self, name: str, unprocessedString: str, consummedString: str, producedString: str, k3fsm_FSM3: "k3fsm_State" = None, owningFSM: set["k3fsm_State"] = None, k3fsm_FSM: "k3fsm_State" = None, k3fsm_FSM6: "k3fsm_State" = None, FSM: "k3fsm_State" = None):
        self.name = name
        self.unprocessedString = unprocessedString
        self.consummedString = consummedString
        self.producedString = producedString
        self.k3fsm_FSM3 = k3fsm_FSM3
        self.owningFSM = owningFSM if owningFSM is not None else set()
        self.k3fsm_FSM = k3fsm_FSM
        self.k3fsm_FSM6 = k3fsm_FSM6
        self.FSM = FSM
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def consummedString(self):
        return self.__consummedString

    @consummedString.setter
    def consummedString(self, consummedString: str):
        self.__consummedString = consummedString


    @property
    def unprocessedString(self):
        return self.__unprocessedString

    @unprocessedString.setter
    def unprocessedString(self, unprocessedString: str):
        self.__unprocessedString = unprocessedString


    @property
    def producedString(self):
        return self.__producedString

    @producedString.setter
    def producedString(self, producedString: str):
        self.__producedString = producedString


    @property
    def k3fsm_FSM(self):
        return self.__k3fsm_FSM

    @k3fsm_FSM.setter
    def k3fsm_FSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k3fsm_FSM__k3fsm_FSM", None)
        self.__k3fsm_FSM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k3fsm_State"):
                opp_val = getattr(old_value, "k3fsm_State", None)
                if opp_val == self:
                    setattr(old_value, "k3fsm_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k3fsm_State"):
                opp_val = getattr(value, "k3fsm_State", None)
                setattr(value, "k3fsm_State", self)

    @property
    def owningFSM(self):
        return self.__owningFSM

    @owningFSM.setter
    def owningFSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k3fsm_FSM__owningFSM", None)
        self.__owningFSM = value if value is not None else set()
        
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
    def FSM(self):
        return self.__FSM

    @FSM.setter
    def FSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k3fsm_FSM__FSM", None)
        self.__FSM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedStates"):
                opp_val = getattr(old_value, "ownedStates", None)
                if opp_val == self:
                    setattr(old_value, "ownedStates", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedStates"):
                opp_val = getattr(value, "ownedStates", None)
                setattr(value, "ownedStates", self)

    @property
    def k3fsm_FSM6(self):
        return self.__k3fsm_FSM6

    @k3fsm_FSM6.setter
    def k3fsm_FSM6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k3fsm_FSM__k3fsm_FSM6", None)
        self.__k3fsm_FSM6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k3fsm_State7"):
                opp_val = getattr(old_value, "k3fsm_State7", None)
                if opp_val == self:
                    setattr(old_value, "k3fsm_State7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k3fsm_State7"):
                opp_val = getattr(value, "k3fsm_State7", None)
                setattr(value, "k3fsm_State7", self)

    @property
    def k3fsm_FSM3(self):
        return self.__k3fsm_FSM3

    @k3fsm_FSM3.setter
    def k3fsm_FSM3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k3fsm_FSM__k3fsm_FSM3", None)
        self.__k3fsm_FSM3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k3fsm_State4"):
                opp_val = getattr(old_value, "k3fsm_State4", None)
                if opp_val == self:
                    setattr(old_value, "k3fsm_State4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k3fsm_State4"):
                opp_val = getattr(value, "k3fsm_State4", None)
                setattr(value, "k3fsm_State4", self)
